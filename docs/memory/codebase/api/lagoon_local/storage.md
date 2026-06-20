# storage.py

## Purpose

Defines local data root, SQLite metadata schema, local artifact directories, temp directory, and log directory.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\api\lagoon_local\storage.py`

## Owns

- `StorageLayout`
- `MediaArtifact`
- `LocalStorageBoundary`
- `EncryptionNotConfiguredError` safety placeholder from SP-01

## Public Interface

- `default_data_root() -> Path`
- `LocalStorageBoundary(root: Path | None)`
- `ensure_layout() -> StorageLayout`
- `write_content_blob(content) -> raises EncryptionNotConfiguredError` in SP-01
- `save_media_artifact(content, mime_type, duration_ms, workspace_id=None) -> MediaArtifact`
- `register_uploaded_media_artifact(source_path, original_name, mime_type, extension, duration_ms, kind, metadata_confidence, workspace_id=None) -> MediaArtifact`

## Data Contracts

- Metadata database: `metadata.sqlite3`.
- Tables: `app_settings`, `lecture_workspaces`, `vault_objects`, `media_artifacts`.
- Imported media files are copied under app-data `media/` with metadata in SQLite.
- `media_artifacts` stores source type, original name, local path, local reference, MIME type, extension, nullable duration, kind, size, and metadata confidence.
- Vault object rows remain metadata placeholders; `write_content_blob` still raises until encryption/provider plan exists.

## Dependencies

- Python stdlib `sqlite3`, `pathlib`, `os`, dataclasses.

## Tests

- Verified by `npm run verify:sp01`.
- Verified by `npm run verify:sp02`.

## Gotchas

- Explicitly close sqlite connections on Windows.
- Content writes intentionally fail in SP-01. This is a safety placeholder, not a requirement to implement encryption before MVP media features.
- `register_uploaded_media_artifact` is local-only unencrypted MVP media handoff, not transcript/content vault storage.

## Last Updated

SP-02
