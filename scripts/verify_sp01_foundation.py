from __future__ import annotations

import importlib
import sqlite3
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
API_ROOT = ROOT / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


REQUIRED_FILES = [
    ROOT / "package.json",
    ROOT / "web" / "package.json",
    ROOT / "web" / "index.html",
    ROOT / "web" / "src" / "App.tsx",
    ROOT / "web" / "src" / "app" / "LagoonShell.tsx",
    ROOT / "web" / "src" / "app" / "privacyDefaults.ts",
    ROOT / "web" / "src" / "app" / "storageBoundary.ts",
    ROOT / "api" / "lagoon_local" / "settings.py",
    ROOT / "api" / "lagoon_local" / "storage.py",
    ROOT / "docs" / "lessons" / "SP-01-local-app-foundation.md",
]


def assert_required_files_exist() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    assert not missing, f"missing required files: {missing}"


def assert_privacy_defaults() -> None:
    settings = importlib.import_module("lagoon_local.settings")
    defaults = settings.default_privacy_settings()

    assert defaults.local_only is True
    assert defaults.network_enabled_for_content is False
    assert defaults.provider_calls_enabled is False
    assert defaults.cloud_sync_enabled is False
    assert defaults.telemetry_enabled is False
    assert defaults.redact_logs is True


def assert_storage_boundary() -> None:
    storage = importlib.import_module("lagoon_local.storage")

    with tempfile.TemporaryDirectory(prefix="lagoon-sp01-") as tmp:
        boundary = storage.LocalStorageBoundary(Path(tmp))
        layout = boundary.ensure_layout()

        assert layout.root == Path(tmp)
        assert layout.metadata_db.exists()
        assert layout.vault_dir.exists()
        assert not str(layout.root).startswith(str(ROOT))

        conn = sqlite3.connect(layout.metadata_db)
        try:
            rows = conn.execute(
                "select name from sqlite_master where type = 'table'"
            ).fetchall()
            tables = {row[0] for row in rows}
        finally:
            conn.close()

        assert "app_settings" in tables
        assert "lecture_workspaces" in tables
        assert "vault_objects" in tables

        try:
            boundary.write_content_blob("raw-content")
        except storage.EncryptionNotConfiguredError:
            pass
        else:
            raise AssertionError("vault accepted raw content without encryption")


def assert_frontend_declares_local_boundary() -> None:
    boundary_source = (ROOT / "web" / "src" / "app" / "storageBoundary.ts").read_text()
    privacy_source = (ROOT / "web" / "src" / "app" / "privacyDefaults.ts").read_text()

    assert "local-only" in boundary_source
    assert "networkEnabledForContent: false" in privacy_source
    assert "providerCallsEnabled: false" in privacy_source
    assert "cloudSyncEnabled: false" in privacy_source


def assert_beginner_safety_docs_exist() -> None:
    lesson_source = (
        ROOT / "docs" / "lessons" / "SP-01-local-app-foundation.md"
    ).read_text()
    gitignore_source = (ROOT / ".gitignore").read_text()

    assert "Beginner Path" in lesson_source
    assert "Sufficiency Review" in lesson_source
    assert "*.tsbuildinfo" in gitignore_source


def main() -> None:
    assert_required_files_exist()
    assert_privacy_defaults()
    assert_storage_boundary()
    assert_frontend_declares_local_boundary()
    assert_beginner_safety_docs_exist()
    print("SP-01 foundation verification passed")


if __name__ == "__main__":
    main()
