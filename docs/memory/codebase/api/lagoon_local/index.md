# lagoon_local

## Purpose

Python package for local privacy defaults and persistence boundary.

## Contains

- `__init__.py`
- `settings.py`
- `storage.py`

## Key Files

- `settings.py`
- `storage.py`

## Interfaces

- `default_privacy_settings()`
- `LocalStorageBoundary.ensure_layout()`
- `LocalStorageBoundary.write_content_blob()`
- `LocalStorageBoundary.save_media_artifact()`

## Dependencies

- `dataclasses`
- `pathlib`
- `sqlite3`

## Tests

- `npm run verify:sp01`
- `npm run verify:sp02`

## Gotchas

- `write_content_blob` raises as a safety placeholder.
- SP-02 media artifact writes are allowed to local-only `media/` and SQLite metadata; no cloud or provider path.

## Last Updated

SP-02
