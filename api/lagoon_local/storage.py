from __future__ import annotations

import os
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Final
from uuid import uuid4

from .settings import default_privacy_settings


SCHEMA_VERSION: Final[int] = 2


class EncryptionNotConfiguredError(RuntimeError):
    """Raised when content write is attempted before vault encryption exists."""


@dataclass(frozen=True)
class StorageLayout:
    root: Path
    metadata_db: Path
    vault_dir: Path
    media_dir: Path
    temp_dir: Path
    logs_dir: Path


@dataclass(frozen=True)
class MediaArtifact:
    id: str
    local_path: Path
    mime_type: str
    duration_ms: int
    size_bytes: int


def default_data_root() -> Path:
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
        return Path(base) / "Lagoon"

    xdg_data_home = os.environ.get("XDG_DATA_HOME")
    if xdg_data_home:
        return Path(xdg_data_home) / "lagoon"

    return Path.home() / ".local" / "share" / "lagoon"


class LocalStorageBoundary:
    def __init__(self, root: Path | None = None) -> None:
        self.root = (root or default_data_root()).expanduser().resolve()

    def ensure_layout(self) -> StorageLayout:
        layout = StorageLayout(
            root=self.root,
            metadata_db=self.root / "metadata.sqlite3",
            vault_dir=self.root / "vault",
            media_dir=self.root / "media",
            temp_dir=self.root / "tmp",
            logs_dir=self.root / "logs",
        )

        layout.vault_dir.mkdir(parents=True, exist_ok=True)
        layout.media_dir.mkdir(parents=True, exist_ok=True)
        layout.temp_dir.mkdir(parents=True, exist_ok=True)
        layout.logs_dir.mkdir(parents=True, exist_ok=True)
        self._ensure_metadata(layout.metadata_db)
        return layout

    def write_content_blob(self, _content: str | bytes) -> None:
        raise EncryptionNotConfiguredError(
            "Encrypted vault provider is not configured in SP-01."
        )

    def save_media_artifact(
        self,
        content: bytes,
        mime_type: str,
        duration_ms: int,
        workspace_id: str | None = None,
    ) -> MediaArtifact:
        if not content:
            raise ValueError("media artifact content is empty")
        if duration_ms < 0:
            raise ValueError("media artifact duration cannot be negative")

        layout = self.ensure_layout()
        artifact_id = str(uuid4())
        extension = self._extension_for_mime_type(mime_type)
        local_path = (layout.media_dir / f"{artifact_id}{extension}").resolve()

        if layout.root not in local_path.parents:
            raise ValueError("media artifact path escaped local data root")

        local_path.write_bytes(content)
        artifact = MediaArtifact(
            id=artifact_id,
            local_path=local_path,
            mime_type=mime_type,
            duration_ms=duration_ms,
            size_bytes=len(content),
        )

        conn = sqlite3.connect(layout.metadata_db)
        try:
            conn.execute(
                """
                insert into media_artifacts (
                    id, workspace_id, local_path, mime_type, duration_ms, size_bytes
                )
                values (?, ?, ?, ?, ?, ?)
                """,
                (
                    artifact.id,
                    workspace_id,
                    str(artifact.local_path),
                    artifact.mime_type,
                    artifact.duration_ms,
                    artifact.size_bytes,
                ),
            )
            conn.commit()
        finally:
            conn.close()

        return artifact

    def _extension_for_mime_type(self, mime_type: str) -> str:
        if mime_type == "video/webm":
            return ".webm"
        if mime_type == "audio/webm":
            return ".webm"
        if mime_type == "video/mp4":
            return ".mp4"
        if mime_type == "audio/wav":
            return ".wav"
        return ".bin"

    def _ensure_metadata(self, database_path: Path) -> None:
        database_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(database_path)
        try:
            conn.execute(
                """
                create table if not exists app_settings (
                    key text primary key,
                    value text not null,
                    updated_at text not null default current_timestamp
                )
                """
            )
            conn.execute(
                """
                create table if not exists lecture_workspaces (
                    id text primary key,
                    title text not null,
                    created_at text not null default current_timestamp,
                    updated_at text not null default current_timestamp
                )
                """
            )
            conn.execute(
                """
                create table if not exists vault_objects (
                    id text primary key,
                    workspace_id text,
                    kind text not null,
                    encrypted_blob_path text not null,
                    sha256 text not null,
                    created_at text not null default current_timestamp,
                    foreign key (workspace_id) references lecture_workspaces(id)
                )
                """
            )
            conn.execute(
                """
                create table if not exists media_artifacts (
                    id text primary key,
                    workspace_id text,
                    local_path text not null,
                    mime_type text not null,
                    duration_ms integer not null,
                    size_bytes integer not null,
                    created_at text not null default current_timestamp,
                    foreign key (workspace_id) references lecture_workspaces(id)
                )
                """
            )
            conn.execute(
                """
                insert into app_settings (key, value, updated_at)
                values ('schema_version', ?, current_timestamp)
                on conflict(key) do update set
                    value = excluded.value,
                    updated_at = current_timestamp
                """,
                (str(SCHEMA_VERSION),),
            )
            for key, value in default_privacy_settings().to_metadata().items():
                conn.execute(
                    """
                    insert or ignore into app_settings (key, value)
                    values (?, ?)
                    """,
                    (key, str(value).lower()),
                )
            conn.commit()
        finally:
            conn.close()
