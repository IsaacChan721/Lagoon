# api

## Purpose

Local-only service and storage boundary for Lagoon metadata and vault layout.

## Contains

- `README.md`
- `lagoon_local/`

## Key Files

- `api/lagoon_local/settings.py`
- `api/lagoon_local/storage.py`

## Interfaces

- Python import root: add `api/` to `sys.path`.
- Public package: `lagoon_local`.

## Dependencies

- Python stdlib only for SP-01.

## Tests

- `npm run verify:sp01`

## Gotchas

- Raw content writes are blocked until encryption provider exists.
- No API server/provider endpoints in SP-01.

## Last Updated

SP-01

