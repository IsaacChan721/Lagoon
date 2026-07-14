from __future__ import annotations

import json
import os
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4

from lagoon_local.jobs.retry import run_with_retry
from lagoon_local.media.audio import normalize_audio_for_transcription
from lagoon_local.storage import LocalStorageBoundary
from lagoon_local.transcript_chunks.chunker import build_transcript_chunks
from lagoon_local.transcription.chunking import plan_media_chunks
from lagoon_local.transcription.provider import TranscriptionProvider, create_transcription_provider
from lagoon_local.transcription.stitching import stitch_provider_segments


@dataclass(frozen=True)
class TranscriptionPipelineResult:
    transcript_artifact_id: str
    transcript_chunks_artifact_id: str
    transcript_artifact_path: Path
    transcript_chunks_path: Path


def transcribe_media_artifact(
    storage_boundary: LocalStorageBoundary,
    lecture_id: str,
    media_artifact_id: str,
    provider: TranscriptionProvider | None = None,
    provider_name: str | None = None,
    transcript_chunk_max_chars: int = 1_200,
) -> TranscriptionPipelineResult:
    layout = storage_boundary.ensure_layout()
    if provider is None:
        selected_provider = provider_name or os.environ.get("LAGOON_TRANSCRIPTION_PROVIDER", "dry-run")
        provider = create_transcription_provider(selected_provider)
    normalized_audio = normalize_audio_for_transcription(storage_boundary, media_artifact_id)
    transcript_artifact_id = f"transcript-{uuid4()}"
    transcript_chunks_artifact_id = f"transcript-chunks-{uuid4()}"

    media_chunks = plan_media_chunks(
        media_artifact_id=media_artifact_id,
        local_path=normalized_audio.audio_path,
        size_bytes=normalized_audio.audio_path.stat().st_size,
        duration_ms=normalized_audio.duration_ms,
    )
    provider_segments_by_chunk_id = {
        chunk.chunk_id: run_with_retry(lambda chunk=chunk: provider.transcribe_chunk(chunk))
        for chunk in media_chunks
    }
    segments = stitch_provider_segments(
        lecture_id=lecture_id,
        media_artifact_id=media_artifact_id,
        transcript_artifact_id=transcript_artifact_id,
        media_chunks=media_chunks,
        provider_segments_by_chunk_id=provider_segments_by_chunk_id,
        provider_name=provider.name,
    )
    transcript_chunks = build_transcript_chunks(
        lecture_id=lecture_id,
        media_artifact_id=media_artifact_id,
        transcript_artifact_id=transcript_artifact_id,
        segments=segments,
        max_chars=transcript_chunk_max_chars,
    )

    transcript_path = layout.transcripts_dir / f"{transcript_artifact_id}.json"
    chunks_path = layout.transcript_chunks_dir / f"{transcript_chunks_artifact_id}.json"
    transcript_payload = {
        "transcriptArtifactId": transcript_artifact_id,
        "lectureId": lecture_id,
        "mediaArtifactId": media_artifact_id,
        "segments": [segment.to_json() for segment in segments],
        "mediaChunks": [chunk.to_json() for chunk in media_chunks],
        "providerMetadata": {
            "provider": provider.name,
            "model": provider.model,
            "audioBoundaryReason": normalized_audio.boundary_reason,
        },
        "diarizationStatus": provider.diarization_status,
    }
    chunks_payload = {
        "transcriptChunksArtifactId": transcript_chunks_artifact_id,
        "lectureId": lecture_id,
        "mediaArtifactId": media_artifact_id,
        "transcriptArtifactId": transcript_artifact_id,
        "chunks": [chunk.to_json() for chunk in transcript_chunks],
    }
    transcript_path.write_text(json.dumps(transcript_payload, indent=2), encoding="utf-8")
    chunks_path.write_text(json.dumps(chunks_payload, indent=2), encoding="utf-8")
    _record_outputs(
        storage_boundary,
        lecture_id,
        media_artifact_id,
        transcript_artifact_id,
        transcript_chunks_artifact_id,
        transcript_path,
        chunks_path,
        provider.name,
    )
    return TranscriptionPipelineResult(
        transcript_artifact_id=transcript_artifact_id,
        transcript_chunks_artifact_id=transcript_chunks_artifact_id,
        transcript_artifact_path=transcript_path,
        transcript_chunks_path=chunks_path,
    )


def _record_outputs(
    storage_boundary: LocalStorageBoundary,
    lecture_id: str,
    media_artifact_id: str,
    transcript_artifact_id: str,
    transcript_chunks_artifact_id: str,
    transcript_path: Path,
    chunks_path: Path,
    provider_name: str,
) -> None:
    layout = storage_boundary.ensure_layout()
    conn = sqlite3.connect(layout.metadata_db)
    try:
        conn.execute(
            """
            insert into transcript_artifacts (
                id, lecture_id, media_artifact_id, local_path, provider, status
            )
            values (?, ?, ?, ?, ?, ?)
            """,
            (transcript_artifact_id, lecture_id, media_artifact_id, str(transcript_path), provider_name, "complete"),
        )
        conn.execute(
            """
            insert into transcript_chunk_artifacts (
                id, lecture_id, media_artifact_id, transcript_artifact_id, local_path, embedding_status
            )
            values (?, ?, ?, ?, ?, ?)
            """,
            (
                transcript_chunks_artifact_id,
                lecture_id,
                media_artifact_id,
                transcript_artifact_id,
                str(chunks_path),
                "pending",
            ),
        )
        conn.commit()
    finally:
        conn.close()
