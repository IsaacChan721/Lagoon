from __future__ import annotations

import math
from pathlib import Path

from lagoon_local.transcription.schema import MediaChunk


OPENAI_FILE_LIMIT_BYTES = 25 * 1024 * 1024
DEFAULT_RELIABILITY_DURATION_MS = 20 * 60 * 1000


def plan_media_chunks(
    media_artifact_id: str,
    local_path: Path,
    size_bytes: int,
    duration_ms: int | None,
    max_bytes: int = OPENAI_FILE_LIMIT_BYTES,
    max_duration_ms: int = DEFAULT_RELIABILITY_DURATION_MS,
) -> list[MediaChunk]:
    if size_bytes <= 0:
        raise ValueError("media size must be positive")
    if duration_ms is not None and duration_ms <= 0:
        raise ValueError("media duration must be positive when known")

    if size_bytes <= max_bytes and (duration_ms is None or duration_ms <= max_duration_ms):
        return [
            MediaChunk(
                chunk_id=f"{media_artifact_id}-media-0000",
                media_artifact_id=media_artifact_id,
                local_path=local_path,
                chunk_index=0,
                start_ms=0,
                end_ms=duration_ms,
                boundary_reason="whole-media",
            )
        ]

    if duration_ms is None:
        raise ValueError("large media requires known duration for deterministic chunking")

    chunks_by_size = math.ceil(size_bytes / max_bytes)
    chunks_by_duration = math.ceil(duration_ms / max_duration_ms)
    chunk_count = max(chunks_by_size, chunks_by_duration)
    span_ms = math.ceil(duration_ms / chunk_count)
    reason = "provider-file-limit" if chunks_by_size >= chunks_by_duration else "reliability-duration-limit"

    chunks: list[MediaChunk] = []
    for index in range(chunk_count):
        start_ms = index * span_ms
        end_ms = min(duration_ms, (index + 1) * span_ms)
        chunks.append(
            MediaChunk(
                chunk_id=f"{media_artifact_id}-media-{index:04d}",
                media_artifact_id=media_artifact_id,
                local_path=local_path,
                chunk_index=index,
                start_ms=start_ms,
                end_ms=end_ms,
                boundary_reason=reason,
            )
        )
    return chunks
