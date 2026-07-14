from __future__ import annotations

from typing import Any

from lagoon_local.transcription.schema import MediaChunk, TranscriptSegment


def stitch_provider_segments(
    lecture_id: str,
    media_artifact_id: str,
    transcript_artifact_id: str,
    media_chunks: list[MediaChunk],
    provider_segments_by_chunk_id: dict[str, list[dict[str, Any]]],
    provider_name: str,
) -> list[TranscriptSegment]:
    stitched: list[TranscriptSegment] = []
    ordered_chunks = sorted(media_chunks, key=lambda chunk: chunk.chunk_index)
    for chunk in ordered_chunks:
        provider_segments = provider_segments_by_chunk_id.get(chunk.chunk_id, [])
        for provider_segment in provider_segments:
            text = str(provider_segment.get("text", "")).strip()
            if not text:
                continue

            segment_index = len(stitched)
            start_ms = _required_ms(provider_segment, "startMs") + chunk.start_ms
            end_ms = _required_ms(provider_segment, "endMs") + chunk.start_ms
            if end_ms <= start_ms:
                raise ValueError("provider segment endMs must be greater than startMs")

            source_segment_id = provider_segment.get("id")
            if source_segment_id is None or str(source_segment_id).strip() == "":
                raise ValueError("provider segment id is required for provenance")

            speaker = provider_segment.get("speaker")
            stitched.append(
                TranscriptSegment(
                    segment_id=f"{transcript_artifact_id}-segment-{segment_index:04d}",
                    lecture_id=lecture_id,
                    media_artifact_id=media_artifact_id,
                    transcript_artifact_id=transcript_artifact_id,
                    start_ms=start_ms,
                    end_ms=end_ms,
                    text=text,
                    source_segment_id=str(source_segment_id),
                    provider=provider_name,
                    speaker=str(speaker) if speaker is not None else None,
                )
            )
    return stitched


def _required_ms(provider_segment: dict[str, Any], key: str) -> int:
    if key not in provider_segment:
        raise ValueError(f"provider segment {key} is required")

    try:
        return int(provider_segment[key])
    except (TypeError, ValueError) as exc:
        raise ValueError(f"provider segment {key} must be milliseconds") from exc
