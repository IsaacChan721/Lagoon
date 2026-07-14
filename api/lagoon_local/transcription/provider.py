from __future__ import annotations

import json
import os
import subprocess
import tempfile
from pathlib import Path
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


class LocalWhisperCppProvider:
    name = "local-whisper-cpp"
    diarization_status = "skipped"

    def __init__(
        self,
        binary_path: str | Path,
        model_path: str | Path,
        extra_args: list[str] | None = None,
    ) -> None:
        self.binary_path = str(binary_path)
        self.model_path = Path(model_path)
        self.extra_args = extra_args or []
        self.model = str(self.model_path)

    @classmethod
    def from_environment(cls) -> "LocalWhisperCppProvider":
        binary_path = os.environ.get("LAGOON_WHISPER_CPP_BINARY", "whisper-cli")
        model_path = os.environ.get("LAGOON_WHISPER_CPP_MODEL")
        if not model_path:
            raise RuntimeError("LAGOON_WHISPER_CPP_MODEL must point to a local ggml Whisper model")
        return cls(binary_path=binary_path, model_path=model_path)

    def transcribe_chunk(self, media_chunk: MediaChunk) -> list[dict[str, object]]:
        if not self.model_path.is_file():
            raise RuntimeError(f"local Whisper model not found: {self.model_path}")
        if not media_chunk.local_path.is_file():
            raise RuntimeError(f"audio chunk not found: {media_chunk.local_path}")

        with tempfile.TemporaryDirectory(prefix="lagoon-whisper-cpp-") as tmp:
            output_base = Path(tmp) / media_chunk.chunk_id
            command = [
                self.binary_path,
                *self.extra_args,
                "-m",
                str(self.model_path),
                "-f",
                str(media_chunk.local_path),
                "-oj",
                "-of",
                str(output_base),
            ]
            completed = subprocess.run(command, check=False, capture_output=True, text=True)
            if completed.returncode != 0:
                detail = (completed.stderr or completed.stdout or "local Whisper CLI failed").strip()
                raise RuntimeError(detail)
            output_path = output_base.with_suffix(".json")
            if not output_path.is_file():
                raise RuntimeError("local Whisper CLI did not write JSON output")
            payload = json.loads(output_path.read_text(encoding="utf-8"))
        return _segments_from_whisper_cpp_json(media_chunk.chunk_id, payload)


def _segments_from_whisper_cpp_json(
    chunk_id: str,
    payload: dict[str, object],
) -> list[dict[str, object]]:
    raw_segments = payload.get("transcription") or payload.get("segments") or []
    if not isinstance(raw_segments, list):
        raise RuntimeError("local Whisper JSON has no segment list")

    segments: list[dict[str, object]] = []
    for index, raw_segment in enumerate(raw_segments):
        if not isinstance(raw_segment, dict):
            continue
        text = str(raw_segment.get("text", "")).strip()
        if not text:
            continue
        start_ms, end_ms = _segment_times_ms(raw_segment)
        segments.append(
            {
                "id": f"{chunk_id}-local-{index:04d}",
                "startMs": start_ms,
                "endMs": end_ms,
                "text": text,
            }
        )
    return segments


def _segment_times_ms(raw_segment: dict[str, object]) -> tuple[int, int]:
    timestamps = raw_segment.get("timestamps")
    if isinstance(timestamps, dict):
        return (
            _timestamp_to_ms(str(timestamps.get("from", "0"))),
            _timestamp_to_ms(str(timestamps.get("to", "0"))),
        )

    if "start" in raw_segment or "end" in raw_segment:
        return (_number_to_ms(raw_segment.get("start", 0)), _number_to_ms(raw_segment.get("end", 0)))
    if "t0" in raw_segment or "t1" in raw_segment:
        return (int(raw_segment.get("t0", 0)), int(raw_segment.get("t1", 0)))
    return (0, 0)


def _number_to_ms(value: object) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value * 1000)
    text = str(value)
    if ":" in text:
        return _timestamp_to_ms(text)
    number = float(text)
    if number < 10_000:
        return int(number * 1000)
    return int(number)


def _timestamp_to_ms(value: str) -> int:
    normalized = value.strip().replace(",", ".")
    parts = normalized.split(":")
    if len(parts) != 3:
        return _number_to_ms(normalized)
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = float(parts[2])
    return int(((hours * 60 * 60) + (minutes * 60) + seconds) * 1000)


def create_transcription_provider(provider_name: str) -> TranscriptionProvider:
    if provider_name == "dry-run":
        return DryRunTranscriptionProvider()
    if provider_name == "local-whisper-cpp":
        return LocalWhisperCppProvider.from_environment()
    if provider_name == "openai":
        return OpenAITranscriptionProvider()
    raise ValueError(f"unknown transcription provider: {provider_name}")


class OpenAITranscriptionProvider:
    name = "openai"
    model = "gpt-4o-mini-transcribe"
    diarization_status = "deferred"

    def transcribe_chunk(self, media_chunk: MediaChunk) -> list[dict[str, object]]:
        raise RuntimeError(
            "OpenAI live transcription adapter is gated until OPENAI_API_KEY and sample media are configured"
        )
