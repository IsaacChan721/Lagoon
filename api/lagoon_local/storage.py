from __future__ import annotations

import os
import shutil
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Final
from uuid import uuid4

from .settings import default_privacy_settings


SCHEMA_VERSION: Final[int] = 3


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
    source_type: str
    original_name: str
    local_path: Path
    local_reference: str
    mime_type: str
    extension: str
    duration_ms: int | None
    kind: str
    size_bytes: int
    metadata_confidence: str


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
        return self._record_media_artifact(
            artifact_id=artifact_id,
            workspace_id=workspace_id,
            source_type="legacy-bytes",
            original_name=local_path.name,
            local_path=local_path,
            local_reference=f"media/{local_path.name}",
            mime_type=mime_type,
            extension=extension,
            duration_ms=duration_ms,
            kind=self._kind_for_mime_type(mime_type),
            size_bytes=len(content),
            metadata_confidence="backend",
        )

    def register_uploaded_media_artifact(
        self,
        source_path: Path,
        original_name: str,
        mime_type: str,
        extension: str,
        duration_ms: int | None,
        kind: str,
        metadata_confidence: str,
        workspace_id: str | None = None,
    ) -> MediaArtifact:
        source_path = source_path.expanduser().resolve()
        if not source_path.is_file():
            raise ValueError("uploaded media source file does not exist")
        if duration_ms is not None and duration_ms < 0:
            raise ValueError("media artifact duration cannot be negative")
        if kind not in {"video", "audio"}:
            raise ValueError("media artifact kind must be video or audio")

        normalized_extension = extension if extension.startswith(".") else f".{extension}"
        layout = self.ensure_layout()
        artifact_id = str(uuid4())
        local_path = (layout.media_dir / f"{artifact_id}{normalized_extension.lower()}").resolve()

        if layout.root not in local_path.parents:
            raise ValueError("media artifact path escaped local data root")

        shutil.copy2(source_path, local_path)
        return self._record_media_artifact(
            artifact_id=artifact_id,
            workspace_id=workspace_id,
            source_type="uploaded-file",
            original_name=original_name,
            local_path=local_path,
            local_reference=f"media/{local_path.name}",
            mime_type=mime_type,
            extension=normalized_extension.lower(),
            duration_ms=duration_ms,
            kind=kind,
            size_bytes=local_path.stat().st_size,
            metadata_confidence=metadata_confidence,
        )

    def _record_media_artifact(
        self,
        artifact_id: str,
        workspace_id: str | None,
        source_type: str,
        original_name: str,
        local_path: Path,
        local_reference: str,
        mime_type: str,
        extension: str,
        duration_ms: int | None,
        kind: str,
        size_bytes: int,
        metadata_confidence: str,
    ) -> MediaArtifact:
        layout = self.ensure_layout()
        artifact = MediaArtifact(
            id=artifact_id,
            source_type=source_type,
            original_name=original_name,
            local_path=local_path,
            local_reference=local_reference,
            mime_type=mime_type,
            extension=extension,
            duration_ms=duration_ms,
            kind=kind,
            size_bytes=size_bytes,
            metadata_confidence=metadata_confidence,
        )

        conn = sqlite3.connect(layout.metadata_db)
        try:
            conn.execute(
                """
                insert into media_artifacts (
                    id, workspace_id, source_type, original_name, local_path,
                    local_reference, mime_type, extension, duration_ms, kind,
                    size_bytes, metadata_confidence
                )
                values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    artifact.id,
                    workspace_id,
                    artifact.source_type,
                    artifact.original_name,
                    str(artifact.local_path),
                    artifact.local_reference,
                    artifact.mime_type,
                    artifact.extension,
                    artifact.duration_ms,
                    artifact.kind,
                    artifact.size_bytes,
                    artifact.metadata_confidence,
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

    def _kind_for_mime_type(self, mime_type: str) -> str:
        if mime_type.startswith("audio/"):
            return "audio"
        return "video"

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
            self._ensure_media_artifacts_schema(conn)
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

    def _ensure_media_artifacts_schema(self, conn: sqlite3.Connection) -> None:
        conn.execute(
            """
            create table if not exists media_artifacts (
                id text primary key,
                workspace_id text,
                source_type text not null,
                original_name text not null,
                local_path text not null,
                local_reference text not null,
                mime_type text not null,
                extension text not null,
                duration_ms integer,
                kind text not null,
                size_bytes integer not null,
                metadata_confidence text not null,
                created_at text not null default current_timestamp,
                foreign key (workspace_id) references lecture_workspaces(id)
            )
            """
        )

        columns = {
            row[1]: {"type": row[2], "notnull": bool(row[3])}
            for row in conn.execute("pragma table_info(media_artifacts)").fetchall()
        }
        required_columns = {
            "source_type",
            "original_name",
            "local_reference",
            "extension",
            "kind",
            "metadata_confidence",
        }
        duration_allows_null = "duration_ms" in columns and not columns["duration_ms"]["notnull"]
        if required_columns.issubset(columns) and duration_allows_null:
            return

        conn.execute("alter table media_artifacts rename to media_artifacts_legacy")
        conn.execute(
            """
            create table media_artifacts (
                id text primary key,
                workspace_id text,
                source_type text not null,
                original_name text not null,
                local_path text not null,
                local_reference text not null,
                mime_type text not null,
                extension text not null,
                duration_ms integer,
                kind text not null,
                size_bytes integer not null,
                metadata_confidence text not null,
                created_at text not null default current_timestamp,
                foreign key (workspace_id) references lecture_workspaces(id)
            )
            """
        )
        legacy_columns = {
            row[1] for row in conn.execute("pragma table_info(media_artifacts_legacy)").fetchall()
        }
        if {"id", "workspace_id", "local_path", "mime_type", "duration_ms", "size_bytes", "created_at"}.issubset(
            legacy_columns
        ):
            conn.execute(
                """
                insert into media_artifacts (
                    id, workspace_id, source_type, original_name, local_path,
                    local_reference, mime_type, extension, duration_ms, kind,
                    size_bytes, metadata_confidence, created_at
                )
                select
                    id,
                    workspace_id,
                    'legacy-bytes',
                    'legacy-media',
                    local_path,
                    'media/' || id || '.bin',
                    mime_type,
                    '.bin',
                    duration_ms,
                    case when mime_type like 'audio/%' then 'audio' else 'video' end,
                    size_bytes,
                    'backend',
                    created_at
                from media_artifacts_legacy
                """
            )
        conn.execute("drop table media_artifacts_legacy")
