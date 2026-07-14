from __future__ import annotations

import shutil
import sqlite3
import subprocess
from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4

from lagoon_local.storage import LocalStorageBoundary


class MediaArtifactNotFoundError(ValueError):
    """Raised when a durable media artifact id is unknown."""


class AudioExtractionUnavailableError(RuntimeError):
    """Raised when video audio extraction needs ffmpeg but it is unavailable."""


@dataclass(frozen=True)
class NormalizedAudio:
    media_artifact_id: str
    source_path: Path
    audio_path: Path
    mime_type: str
    duration_ms: int | None
    boundary_reason: str


def normalize_audio_for_transcription(
    storage_boundary: LocalStorageBoundary,
    media_artifact_id: str,
) -> NormalizedAudio:
    artifact = _load_media_artifact(storage_boundary, media_artifact_id)
    source_path = Path(artifact["local_path"]).resolve()
    if not source_path.is_file():
        raise MediaArtifactNotFoundError("media artifact local file is missing")
    if str(source_path).startswith("blob:"):
        raise ValueError("browser object URLs are preview-only and cannot be transcribed")

    layout = storage_boundary.ensure_layout()
    audio_dir = layout.temp_dir / "transcription_audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    if artifact["kind"] == "audio":
        audio_path = (audio_dir / f"{media_artifact_id}{artifact['extension']}").resolve()
        shutil.copy2(source_path, audio_path)
        return NormalizedAudio(
            media_artifact_id=media_artifact_id,
            source_path=source_path,
            audio_path=audio_path,
            mime_type=artifact["mime_type"],
            duration_ms=artifact["duration_ms"],
            boundary_reason="already-audio",
        )

    output_path = (audio_dir / f"{media_artifact_id}-{uuid4().hex}.wav").resolve()
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise AudioExtractionUnavailableError(
            "video audio extraction requires ffmpeg on PATH for this MVP"
        )
    subprocess.run(
        [
            ffmpeg,
            "-y",
            "-i",
            str(source_path),
            "-vn",
            "-acodec",
            "pcm_s16le",
            "-ar",
            "16000",
            "-ac",
            "1",
            str(output_path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return NormalizedAudio(
        media_artifact_id=media_artifact_id,
        source_path=source_path,
        audio_path=output_path,
        mime_type="audio/wav",
        duration_ms=artifact["duration_ms"],
        boundary_reason="extracted-from-video",
    )


def _load_media_artifact(
    storage_boundary: LocalStorageBoundary,
    media_artifact_id: str,
) -> dict[str, object]:
    layout = storage_boundary.ensure_layout()
    conn = sqlite3.connect(layout.metadata_db)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            """
            select id, local_path, mime_type, extension, duration_ms, kind
            from media_artifacts
            where id = ?
            """,
            (media_artifact_id,),
        ).fetchone()
    finally:
        conn.close()
    if row is None:
        raise MediaArtifactNotFoundError("media artifact id not found")
    return dict(row)
