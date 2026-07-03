from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class MediaChunk:
    chunk_id: str
    media_artifact_id: str
    local_path: Path
    chunk_index: int
    start_ms: int
    end_ms: int | None
    boundary_reason: str

    def to_json(self) -> dict[str, Any]:
        data = asdict(self)
        data["local_path"] = str(self.local_path)
        return data


@dataclass(frozen=True)
class TranscriptSegment:
    segment_id: str
    lecture_id: str
    media_artifact_id: str
    transcript_artifact_id: str
    start_ms: int
    end_ms: int
    text: str
    source_segment_id: str
    provider: str
    speaker: str | None = None

    def to_json(self) -> dict[str, Any]:
        return {
            "segmentId": self.segment_id,
            "lectureId": self.lecture_id,
            "mediaArtifactId": self.media_artifact_id,
            "transcriptArtifactId": self.transcript_artifact_id,
            "startMs": self.start_ms,
            "endMs": self.end_ms,
            "text": self.text,
            "sourceSegmentId": self.source_segment_id,
            "provider": self.provider,
            "speaker": self.speaker,
        }


@dataclass(frozen=True)
class TranscriptChunk:
    chunk_id: str
    lecture_id: str
    media_artifact_id: str
    transcript_artifact_id: str
    segment_ids: list[str]
    start_ms: int
    end_ms: int
    text: str
    boundary_reason: str
    embedding_status: str
    provider_metadata: dict[str, Any]
    speaker_labels: list[str]

    def to_json(self) -> dict[str, Any]:
        return {
            "chunkId": self.chunk_id,
            "lectureId": self.lecture_id,
            "mediaArtifactId": self.media_artifact_id,
            "transcriptArtifactId": self.transcript_artifact_id,
            "segmentIds": self.segment_ids,
            "startMs": self.start_ms,
            "endMs": self.end_ms,
            "text": self.text,
            "boundaryReason": self.boundary_reason,
            "embeddingStatus": self.embedding_status,
            "providerMetadata": self.provider_metadata,
            "speakerLabels": self.speaker_labels,
        }
