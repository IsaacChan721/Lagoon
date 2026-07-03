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
            segment_index = len(stitched)
            start_ms = int(provider_segment["startMs"]) + chunk.start_ms
            end_ms = int(provider_segment["endMs"]) + chunk.start_ms
            stitched.append(
                TranscriptSegment(
                    segment_id=f"{transcript_artifact_id}-segment-{segment_index:04d}",
                    lecture_id=lecture_id,
                    media_artifact_id=media_artifact_id,
                    transcript_artifact_id=transcript_artifact_id,
                    start_ms=start_ms,
                    end_ms=end_ms,
                    text=str(provider_segment["text"]).strip(),
                    source_segment_id=str(provider_segment["id"]),
                    provider=provider_name,
                    speaker=provider_segment.get("speaker"),
                )
            )
    return stitched
