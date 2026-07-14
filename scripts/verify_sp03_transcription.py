from __future__ import annotations

import importlib
import json
import os
import sqlite3
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
API_ROOT = ROOT / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


REQUIRED_FILES = [
    ROOT / "api" / "lagoon_local" / "media" / "audio.py",
    ROOT / "api" / "lagoon_local" / "transcription" / "chunking.py",
    ROOT / "api" / "lagoon_local" / "transcription" / "provider.py",
    ROOT / "api" / "lagoon_local" / "transcription" / "stitching.py",
    ROOT / "api" / "lagoon_local" / "transcript_chunks" / "chunker.py",
    ROOT / "api" / "lagoon_local" / "jobs" / "retry.py",
    ROOT / "docs" / "lessons" / "SP-03-media-transcription.md",
]


def assert_required_files_exist() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    assert not missing, f"missing SP-03 files: {missing}"


def assert_media_chunking_contract() -> None:
    chunking = importlib.import_module("lagoon_local.transcription.chunking")

    whole = chunking.plan_media_chunks(
        media_artifact_id="media-1",
        local_path=Path("lecture.m4a"),
        size_bytes=1024,
        duration_ms=60_000,
    )
    assert len(whole) == 1
    assert whole[0].chunk_id == "media-1-media-0000"
    assert whole[0].start_ms == 0
    assert whole[0].end_ms == 60_000
    assert whole[0].boundary_reason == "whole-media"

    large = chunking.plan_media_chunks(
        media_artifact_id="media-1",
        local_path=Path("lecture.m4a"),
        size_bytes=60 * 1024 * 1024,
        duration_ms=3_600_000,
        max_bytes=25 * 1024 * 1024,
        max_duration_ms=1_200_000,
    )
    assert [chunk.start_ms for chunk in large] == [0, 1_200_000, 2_400_000]
    assert large[-1].end_ms == 3_600_000
    assert all(chunk.boundary_reason in {"provider-file-limit", "reliability-duration-limit"} for chunk in large)


def assert_audio_normalization_uses_durable_media_artifact() -> None:
    storage = importlib.import_module("lagoon_local.storage")
    audio = importlib.import_module("lagoon_local.media.audio")

    with tempfile.TemporaryDirectory(prefix="lagoon-sp03-audio-") as tmp:
        root = Path(tmp)
        source = root / "lecture.m4a"
        source.write_bytes(b"fake-audio")
        boundary = storage.LocalStorageBoundary(root / "appdata")
        artifact = boundary.register_uploaded_media_artifact(
            source_path=source,
            original_name="lecture.m4a",
            mime_type="audio/mp4",
            extension=".m4a",
            duration_ms=12_000,
            kind="audio",
            metadata_confidence="fixture",
        )

        normalized = audio.normalize_audio_for_transcription(boundary, artifact.id)
        assert normalized.media_artifact_id == artifact.id
        assert normalized.source_path == artifact.local_path
        assert normalized.audio_path.exists()
        assert normalized.audio_path.read_bytes() == b"fake-audio"
        assert "blob:" not in str(normalized.source_path)
        assert normalized.boundary_reason == "already-audio"


def assert_stitching_preserves_absolute_timestamps_and_source_ids() -> None:
    schema = importlib.import_module("lagoon_local.transcription.schema")
    stitching = importlib.import_module("lagoon_local.transcription.stitching")

    chunks = [
        schema.MediaChunk("media-1-media-0000", "media-1", Path("a.wav"), 0, 0, 10_000, "whole-media"),
        schema.MediaChunk("media-1-media-0001", "media-1", Path("b.wav"), 1, 10_000, 20_000, "provider-file-limit"),
    ]
    provider_segments = {
        "media-1-media-0000": [
            {"id": "provider-a", "startMs": 500, "endMs": 1500, "text": "First sentence."}
        ],
        "media-1-media-0001": [
            {"id": "provider-b", "startMs": 250, "endMs": 1250, "text": "Second sentence."}
        ],
    }

    stitched = stitching.stitch_provider_segments(
        lecture_id="lecture-1",
        media_artifact_id="media-1",
        transcript_artifact_id="tx-1",
        media_chunks=chunks,
        provider_segments_by_chunk_id=provider_segments,
        provider_name="dry-run",
    )

    assert [segment.segment_id for segment in stitched] == ["tx-1-segment-0000", "tx-1-segment-0001"]
    assert [segment.source_segment_id for segment in stitched] == ["provider-a", "provider-b"]
    assert [segment.start_ms for segment in stitched] == [500, 10_250]
    assert [segment.end_ms for segment in stitched] == [1500, 11_250]
    assert all(segment.media_artifact_id == "media-1" for segment in stitched)


def assert_provider_segment_validation_is_strict() -> None:
    schema = importlib.import_module("lagoon_local.transcription.schema")
    stitching = importlib.import_module("lagoon_local.transcription.stitching")

    chunk = schema.MediaChunk("media-1-media-0000", "media-1", Path("a.wav"), 0, 0, 10_000, "whole-media")
    stitched = stitching.stitch_provider_segments(
        lecture_id="lecture-1",
        media_artifact_id="media-1",
        transcript_artifact_id="tx-1",
        media_chunks=[chunk],
        provider_segments_by_chunk_id={
            "media-1-media-0000": [
                {"id": "blank", "startMs": 0, "endMs": 1000, "text": "   "},
                {"id": "good", "startMs": 1000, "endMs": 2000, "text": "Real text."},
            ]
        },
        provider_name="fixture",
    )
    assert [segment.source_segment_id for segment in stitched] == ["good"]

    for bad_segment in [
        {"startMs": 0, "endMs": 1000, "text": "Missing id."},
        {"id": "bad-time", "startMs": 1000, "endMs": 1000, "text": "Bad time."},
        {"id": "bad-start", "startMs": "nope", "endMs": 1000, "text": "Bad start."},
    ]:
        try:
            stitching.stitch_provider_segments(
                lecture_id="lecture-1",
                media_artifact_id="media-1",
                transcript_artifact_id="tx-1",
                media_chunks=[chunk],
                provider_segments_by_chunk_id={"media-1-media-0000": [bad_segment]},
                provider_name="fixture",
            )
        except ValueError:
            pass
        else:
            raise AssertionError(f"invalid provider segment was accepted: {bad_segment}")


def assert_transcript_chunks_preserve_boundaries_and_provenance() -> None:
    schema = importlib.import_module("lagoon_local.transcription.schema")
    chunker = importlib.import_module("lagoon_local.transcript_chunks.chunker")

    segments = [
        schema.TranscriptSegment(
            segment_id="s1",
            lecture_id="lecture-1",
            media_artifact_id="media-1",
            transcript_artifact_id="tx-1",
            start_ms=0,
            end_ms=900,
            text="Alpha starts here.",
            source_segment_id="p1",
            provider="fixture",
        ),
        schema.TranscriptSegment(
            segment_id="s2",
            lecture_id="lecture-1",
            media_artifact_id="media-1",
            transcript_artifact_id="tx-1",
            start_ms=3_000,
            end_ms=4_000,
            text="Beta resumes after a pause.",
            source_segment_id="p2",
            provider="fixture",
        ),
        schema.TranscriptSegment(
            segment_id="s3",
            lecture_id="lecture-1",
            media_artifact_id="media-1",
            transcript_artifact_id="tx-1",
            start_ms=4_100,
            end_ms=5_000,
            text="Gamma stays nearby.",
            source_segment_id="p3",
            provider="fixture",
        ),
    ]

    chunks = chunker.build_transcript_chunks(
        lecture_id="lecture-1",
        media_artifact_id="media-1",
        transcript_artifact_id="tx-1",
        segments=segments,
        max_chars=80,
        pause_boundary_ms=1_500,
    )

    assert len(chunks) == 2
    assert chunks[0].segment_ids == ["s1"]
    assert chunks[0].boundary_reason == "pause-boundary"
    assert chunks[1].segment_ids == ["s2", "s3"]
    assert chunks[1].start_ms == 3_000
    assert chunks[1].end_ms == 5_000
    assert all(chunk.media_artifact_id == "media-1" for chunk in chunks)
    assert all(not chunk.text.endswith(" Bet") for chunk in chunks)

    forced = chunker.build_transcript_chunks(
        lecture_id="lecture-1",
        media_artifact_id="media-1",
        transcript_artifact_id="tx-1",
        segments=[
            schema.TranscriptSegment(
                segment_id="s-long",
                lecture_id="lecture-1",
                media_artifact_id="media-1",
                transcript_artifact_id="tx-1",
                start_ms=0,
                end_ms=10_000,
                text="word " * 30,
                source_segment_id="p-long",
                provider="fixture",
            )
        ],
        max_chars=40,
    )
    assert len(forced) > 1
    assert any(chunk.boundary_reason == "forced-size-limit" for chunk in forced)
    assert all(len(chunk.text) <= 40 for chunk in forced)
    assert all(chunk.text == chunk.text.strip() for chunk in forced)
    assert all(set(chunk.text.split()) == {"word"} for chunk in forced)


def assert_retry_policy_classifies_failures() -> None:
    retry = importlib.import_module("lagoon_local.jobs.retry")

    assert retry.classify_transcription_error("401 invalid api key") == "auth"
    assert retry.classify_transcription_error("quota exceeded") == "quota"
    assert retry.classify_transcription_error("413 payload too large") == "payload"
    assert retry.classify_transcription_error("connection reset by peer") == "network"
    assert retry.should_retry("network", attempt=1, max_attempts=3) is True
    assert retry.should_retry("auth", attempt=1, max_attempts=3) is False
    assert retry.should_retry("network", attempt=3, max_attempts=3) is False


def assert_fixture_transcription_path_writes_artifacts() -> None:
    storage = importlib.import_module("lagoon_local.storage")
    provider = importlib.import_module("lagoon_local.transcription.provider")
    pipeline = importlib.import_module("lagoon_local.transcription.pipeline")

    with tempfile.TemporaryDirectory(prefix="lagoon-sp03-pipeline-") as tmp:
        root = Path(tmp)
        source = root / "lecture.m4a"
        source.write_bytes(b"fixture-audio")
        boundary = storage.LocalStorageBoundary(root / "appdata")
        artifact = boundary.register_uploaded_media_artifact(
            source_path=source,
            original_name="lecture.m4a",
            mime_type="audio/mp4",
            extension=".m4a",
            duration_ms=8_000,
            kind="audio",
            metadata_confidence="fixture",
        )

        result = pipeline.transcribe_media_artifact(
            storage_boundary=boundary,
            lecture_id="lecture-1",
            media_artifact_id=artifact.id,
            provider=provider.DryRunTranscriptionProvider(),
            transcript_chunk_max_chars=120,
        )

        assert result.transcript_artifact_path.exists()
        assert result.transcript_chunks_path.exists()
        transcript = json.loads(result.transcript_artifact_path.read_text(encoding="utf-8"))
        chunks = json.loads(result.transcript_chunks_path.read_text(encoding="utf-8"))
        assert transcript["mediaArtifactId"] == artifact.id
        assert transcript["providerMetadata"]["provider"] == "dry-run"
        assert transcript["diarizationStatus"] == "skipped"
        assert chunks["chunks"][0]["mediaArtifactId"] == artifact.id
        assert chunks["chunks"][0]["segmentIds"]

        conn = sqlite3.connect(boundary.ensure_layout().metadata_db)
        try:
            transcript_rows = conn.execute("select id, media_artifact_id from transcript_artifacts").fetchall()
            chunk_rows = conn.execute("select id, transcript_artifact_id from transcript_chunk_artifacts").fetchall()
        finally:
            conn.close()
        assert transcript_rows == [(result.transcript_artifact_id, artifact.id)]
        assert chunk_rows == [(result.transcript_chunks_artifact_id, result.transcript_artifact_id)]


def assert_local_whisper_cpp_provider_uses_free_cli_contract() -> None:
    provider_module = importlib.import_module("lagoon_local.transcription.provider")
    schema = importlib.import_module("lagoon_local.transcription.schema")

    with tempfile.TemporaryDirectory(prefix="lagoon-sp03-local-whisper-") as tmp:
        root = Path(tmp)
        fake_cli = root / "fake_whisper_cpp.py"
        fake_model = root / "ggml-tiny.en.bin"
        audio = root / "chunk.wav"
        fake_model.write_bytes(b"model")
        audio.write_bytes(b"wav")
        fake_cli.write_text(
            "\n".join(
                [
                    "from __future__ import annotations",
                    "import json",
                    "import sys",
                    "from pathlib import Path",
                    "output_base = Path(sys.argv[sys.argv.index('-of') + 1])",
                    "payload = {",
                    "    'transcription': [",
                    "        {'timestamps': {'from': '00:00:00.500', 'to': '00:00:01.250'}, 'text': 'Local free segment.'},",
                    "        {'timestamps': {'from': '00:00:02.000', 'to': '00:00:03.000'}, 'text': 'Second local segment.'},",
                    "    ]",
                    "}",
                    "output_base.with_suffix('.json').write_text(json.dumps(payload), encoding='utf-8')",
                ]
            ),
            encoding="utf-8",
        )

        provider = provider_module.LocalWhisperCppProvider(
            binary_path=sys.executable,
            model_path=fake_model,
            extra_args=[str(fake_cli)],
        )
        segments = provider.transcribe_chunk(
            schema.MediaChunk("media-1-media-0000", "media-1", audio, 0, 0, 5_000, "whole-media")
        )

    assert provider.name == "local-whisper-cpp"
    assert provider.model == str(fake_model)
    assert provider.diarization_status == "skipped"
    assert segments == [
        {"id": "media-1-media-0000-local-0000", "startMs": 500, "endMs": 1250, "text": "Local free segment."},
        {"id": "media-1-media-0000-local-0001", "startMs": 2000, "endMs": 3000, "text": "Second local segment."},
    ]
    assert provider_module.create_transcription_provider("dry-run").name == "dry-run"


def assert_live_call_gate_is_explicit() -> None:
    has_key = bool(os.environ.get("OPENAI_API_KEY"))
    sample = ROOT / "docs" / "lessons" / "fixtures" / "sp03-sample.m4a"
    if has_key and sample.exists():
        print("SP-03 live transcription prerequisites present; fixture verifier still uses dry-run provider")
    else:
        print("SP-03 live transcription skipped: OPENAI_API_KEY or sample media missing")


def main() -> None:
    assert_required_files_exist()
    assert_media_chunking_contract()
    assert_audio_normalization_uses_durable_media_artifact()
    assert_stitching_preserves_absolute_timestamps_and_source_ids()
    assert_provider_segment_validation_is_strict()
    assert_transcript_chunks_preserve_boundaries_and_provenance()
    assert_retry_policy_classifies_failures()
    assert_fixture_transcription_path_writes_artifacts()
    assert_local_whisper_cpp_provider_uses_free_cli_contract()
    assert_live_call_gate_is_explicit()
    print("SP-03 media transcription verification passed")


if __name__ == "__main__":
    main()
