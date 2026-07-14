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
    ROOT / "web" / "src" / "media-import" / "mediaImportState.ts",
    ROOT / "web" / "src" / "media-import" / "useMediaImport.ts",
    ROOT / "web" / "src" / "media-import" / "MediaImportPanel.tsx",
    ROOT / "docs" / "lessons" / "SP-02-lecture-media-import.md",
]


FORBIDDEN_SOURCE_TOKENS = [
    "get" + "User" + "Media",
    "Media" + "Recorder",
    "start" + "Capture",
    "pause" + "Capture",
    "resume" + "Capture",
    "stop" + "Capture",
    "Camera" + " preview",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def assert_required_files_exist() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    assert not missing, f"missing SP-02 media import files: {missing}"
    old_feature_dir = ROOT / "web" / "src" / ("cap" + "ture")
    old_verifier = ROOT / "scripts" / ("verify_sp02_" + "cap" + "ture.py")
    old_lesson = ROOT / "docs" / "lessons" / ("SP-02-video-audio-" + "cap" + "ture.md")
    assert not old_feature_dir.exists(), "old SP-02 recording folder still exists"
    assert not old_verifier.exists(), "old SP-02 recording verifier still exists"
    assert not old_lesson.exists(), "old SP-02 recording lesson still exists"


def assert_frontend_media_import_contract() -> None:
    state_source = read(ROOT / "web" / "src" / "media-import" / "mediaImportState.ts")
    hook_source = read(ROOT / "web" / "src" / "media-import" / "useMediaImport.ts")
    panel_source = read(ROOT / "web" / "src" / "media-import" / "MediaImportPanel.tsx")
    shell_source = read(ROOT / "web" / "src" / "app" / "LagoonShell.tsx")

    for token in [
        "UploadedMediaArtifact",
        'sourceType: "uploaded-file"',
        'kind: "video" | "audio"',
        '"idle"',
        '"validating"',
        '"ready"',
        '"unsupported"',
        '"too-large"',
        '"metadata-error"',
        '"saved"',
        "localReference",
        "metadataConfidence",
    ]:
        assert token in state_source, f"media import state missing {token}"

    for extension in [".mp4", ".webm", ".mov", ".m4v", ".mp3", ".m4a", ".wav", ".mpeg", ".mpga"]:
        assert extension in state_source, f"supported extension missing {extension}"

    assert "URL.createObjectURL" in hook_source
    assert "URL.revokeObjectURL" in hook_source
    assert "loadedmetadata" in hook_source
    assert "objectUrlRef" in hook_source
    assert "importTokenRef" in hook_source
    assert "accept={acceptedMediaInput}" in panel_source
    assert "<video" in panel_source
    assert "<audio" in panel_source
    assert "MediaImportPanel" in shell_source
    assert "../media-import/MediaImportPanel" in shell_source


def assert_no_recording_apis_remain() -> None:
    source_paths = [
        *list((ROOT / "web" / "src").rglob("*")),
        *list((ROOT / "scripts").rglob("*")),
    ]
    docs_paths = [
        ROOT / "docs" / "prompt-packages" / "SP-02" / "plan.md",
        ROOT / "docs" / "prompt-packages" / "SP-02" / "package.md",
        ROOT / "docs" / "memory" / "phases" / "SP-02" / "index.md",
        ROOT / "docs" / "run-logs" / "SP-02-output.md",
    ]
    for path in [p for p in source_paths + docs_paths if p.is_file()]:
        text = read(path)
        for token in FORBIDDEN_SOURCE_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} still contains {token}"


def assert_storage_media_contract() -> None:
    storage = importlib.import_module("lagoon_local.storage")

    with tempfile.TemporaryDirectory(prefix="lagoon-sp02-") as tmp:
        boundary = storage.LocalStorageBoundary(Path(tmp))
        layout = boundary.ensure_layout()
        source = Path(tmp) / "lecture.mp4"
        source.write_bytes(b"fake-mp4-content")

        artifact = boundary.register_uploaded_media_artifact(
            source_path=source,
            original_name="lecture.mp4",
            mime_type="video/mp4",
            extension=".mp4",
            duration_ms=None,
            kind="video",
            metadata_confidence="browser",
        )

        assert artifact.source_type == "uploaded-file"
        assert artifact.original_name == "lecture.mp4"
        assert artifact.extension == ".mp4"
        assert artifact.kind == "video"
        assert artifact.local_path.parent == layout.media_dir
        assert artifact.local_reference == f"media/{artifact.local_path.name}"
        assert artifact.size_bytes == len(b"fake-mp4-content")
        assert artifact.duration_ms is None

        conn = sqlite3.connect(layout.metadata_db)
        try:
            row = conn.execute(
                """
                select source_type, original_name, mime_type, extension, duration_ms,
                       kind, local_path, local_reference, size_bytes, metadata_confidence
                from media_artifacts
                where id = ?
                """,
                (artifact.id,),
            ).fetchone()
        finally:
            conn.close()

        assert row == (
            "uploaded-file",
            "lecture.mp4",
            "video/mp4",
            ".mp4",
            None,
            "video",
            str(artifact.local_path),
            artifact.local_reference,
            artifact.size_bytes,
            "browser",
        )


def assert_docs_describe_import_contract() -> None:
    docs = [
        ROOT / "docs" / "prompt-packages" / "SP-02" / "plan.md",
        ROOT / "docs" / "prompt-packages" / "SP-02" / "package.md",
        ROOT / "docs" / "memory" / "phases" / "SP-02" / "index.md",
        ROOT / "docs" / "run-logs" / "SP-02-output.md",
        ROOT / "docs" / "lessons" / "SP-02-lecture-media-import.md",
    ]
    for path in docs:
        source = read(path)
        assert "Lecture Media Import" in source or "lecture media import" in source
        assert "import" in source.lower()
        assert "transcript is primary evidence" in source.lower()


def main() -> None:
    assert_required_files_exist()
    assert_frontend_media_import_contract()
    assert_no_recording_apis_remain()
    assert_storage_media_contract()
    assert_docs_describe_import_contract()
    print("SP-02 lecture media import verification passed")


if __name__ == "__main__":
    main()
