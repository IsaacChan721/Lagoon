# api

## Purpose

Local-only service and storage boundary for Lagoon metadata and local artifact layout.

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

- Python stdlib only.

## Tests

- `npm run verify:sp01`
- `npm run verify:sp02`

## Gotchas

- Raw content writes are blocked as a safety placeholder; SP-02 adds local-only media artifact file handoff.
- No API server/provider endpoints.

## Last Updated

SP-02
