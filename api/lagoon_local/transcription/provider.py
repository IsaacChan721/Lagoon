from __future__ import annotations

from typing import Protocol

from lagoon_local.transcription.schema import MediaChunk


class TranscriptionProvider(Protocol):
    name: str
    model: str
    diarization_status: str

    def transcribe_chunk(self, media_chunk: MediaChunk) -> list[dict[str, object]]:
        ...


class DryRunTranscriptionProvider:
    name = "dry-run"
    model = "fixture"
    diarization_status = "skipped"

    def transcribe_chunk(self, media_chunk: MediaChunk) -> list[dict[str, object]]:
        start = 0
        end = 4_000
        if media_chunk.end_ms is not None:
            end = max(1_000, min(4_000, media_chunk.end_ms - media_chunk.start_ms))
        return [
            {
                "id": f"{media_chunk.chunk_id}-provider-0000",
                "startMs": start,
                "endMs": end,
                "text": "Dry run transcript segment. It preserves timing for tests.",
            }
        ]


class OpenAITranscriptionProvider:
    name = "openai"
    model = "gpt-4o-mini-transcribe"
    diarization_status = "deferred"

    def transcribe_chunk(self, media_chunk: MediaChunk) -> list[dict[str, object]]:
        raise RuntimeError(
            "OpenAI live transcription adapter is gated until OPENAI_API_KEY and sample media are configured"
        )
