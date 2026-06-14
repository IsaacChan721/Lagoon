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

## Dependencies

- `dataclasses`
- `pathlib`
- `sqlite3`

## Tests

- `npm run verify:sp01`

## Gotchas

- `write_content_blob` raises until encryption/key provider is implemented.

## Last Updated

SP-01

