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
    ROOT / "web" / "src" / "capture" / "captureState.ts",
    ROOT / "web" / "src" / "capture" / "useMediaCapture.ts",
    ROOT / "web" / "src" / "capture" / "CapturePanel.tsx",
    ROOT / "api" / "lagoon_local" / "storage.py",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def assert_required_files_exist() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    assert not missing, f"missing SP-02 files: {missing}"


def assert_frontend_capture_contract() -> None:
    state_source = read(ROOT / "web" / "src" / "capture" / "captureState.ts")
    hook_source = read(ROOT / "web" / "src" / "capture" / "useMediaCapture.ts")
    panel_source = read(ROOT / "web" / "src" / "capture" / "CapturePanel.tsx")
    shell_source = read(ROOT / "web" / "src" / "app" / "LagoonShell.tsx")

    for token in [
        "idle",
        "requesting-permission",
        "recording",
        "paused",
        "saving",
        "saved",
        "permission-denied",
        "interrupted",
    ]:
        assert token in state_source, f"capture state missing {token}"

    assert "navigator.mediaDevices.getUserMedia" in hook_source
    assert "MediaRecorder" in hook_source
    assert "captureInterrupted" in hook_source
    assert "LocalMediaArtifact" in hook_source
    assert "URL.createObjectURL" in hook_source
    assert "transcript" not in hook_source.lower()
    assert "summary" not in hook_source.lower()
    assert "rag" not in hook_source.lower()

    for label in ["Start", "Pause", "Resume", "Stop", "Save"]:
        assert label in panel_source, f"capture control missing {label}"

    assert "CapturePanel" in shell_source


def assert_storage_media_contract() -> None:
    storage = importlib.import_module("lagoon_local.storage")

    with tempfile.TemporaryDirectory(prefix="lagoon-sp02-") as tmp:
        boundary = storage.LocalStorageBoundary(Path(tmp))
        layout = boundary.ensure_layout()

        assert hasattr(layout, "media_dir")
        assert layout.media_dir.exists()

        artifact = boundary.save_media_artifact(
            content=b"fake-webm",
            mime_type="video/webm",
            duration_ms=1234,
        )
        assert artifact.local_path.exists()
        assert artifact.local_path.parent == layout.media_dir
        assert str(artifact.local_path).startswith(str(layout.root))
        assert artifact.mime_type == "video/webm"
        assert artifact.duration_ms == 1234

        conn = sqlite3.connect(layout.metadata_db)
        try:
            rows = conn.execute(
                "select id, mime_type, duration_ms, local_path from media_artifacts"
            ).fetchall()
        finally:
            conn.close()

        assert len(rows) == 1
        assert rows[0][0] == artifact.id
        assert rows[0][1] == "video/webm"
        assert rows[0][2] == 1234
        assert rows[0][3] == str(artifact.local_path)


def assert_gitignore_keeps_media_local() -> None:
    gitignore_source = read(ROOT / ".gitignore")
    assert "media/" in gitignore_source
    assert "*.webm" in gitignore_source


def main() -> None:
    assert_required_files_exist()
    assert_frontend_capture_contract()
    assert_storage_media_contract()
    assert_gitignore_keeps_media_local()
    print("SP-02 capture verification passed")


if __name__ == "__main__":
    main()
