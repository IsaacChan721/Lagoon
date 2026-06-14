# storage.py

## Purpose

Defines local data root, SQLite metadata schema, vault directory, temp directory, and log directory.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\api\lagoon_local\storage.py`

## Owns

- `StorageLayout`
- `LocalStorageBoundary`
- `EncryptionNotConfiguredError`

## Public Interface

- `default_data_root() -> Path`
- `LocalStorageBoundary(root: Path | None)`
- `ensure_layout() -> StorageLayout`
- `write_content_blob(content) -> raises EncryptionNotConfiguredError`

## Data Contracts

- Metadata database: `metadata.sqlite3`.
- Tables: `app_settings`, `lecture_workspaces`, `vault_objects`.
- Vault object rows store metadata and encrypted blob paths only.

## Dependencies

- Python stdlib `sqlite3`, `pathlib`, `os`, dataclasses.

## Tests

- Verified by `npm run verify:sp01`.

## Gotchas

- Explicitly close sqlite connections on Windows.
- Content writes intentionally fail until encryption provider/key storage is chosen in later phase.

## Last Updated

SP-01

