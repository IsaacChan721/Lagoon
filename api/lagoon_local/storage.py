from __future__ import annotations

import os
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Final

from .settings import default_privacy_settings


SCHEMA_VERSION: Final[int] = 1


class EncryptionNotConfiguredError(RuntimeError):
    """Raised when content write is attempted before vault encryption exists."""


@dataclass(frozen=True)
class StorageLayout:
    root: Path
    metadata_db: Path
    vault_dir: Path
    temp_dir: Path
    logs_dir: Path


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
            temp_dir=self.root / "tmp",
            logs_dir=self.root / "logs",
        )

        layout.vault_dir.mkdir(parents=True, exist_ok=True)
        layout.temp_dir.mkdir(parents=True, exist_ok=True)
        layout.logs_dir.mkdir(parents=True, exist_ok=True)
        self._ensure_metadata(layout.metadata_db)
        return layout

    def write_content_blob(self, _content: str | bytes) -> None:
        raise EncryptionNotConfiguredError(
            "Encrypted vault provider is not configured in SP-01."
        )

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
                insert or ignore into app_settings (key, value)
                values ('schema_version', ?)
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
