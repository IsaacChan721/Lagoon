# verify_sp01_foundation

## Purpose

Narrow SP-01 gate check for required files, privacy defaults, SQLite metadata schema, vault write blocking, frontend boundary declarations, and beginner lesson presence.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\scripts\verify_sp01_foundation.py`

## Owns

- SP-01 foundation acceptance smoke.
- Temporary storage layout verification.

## Public Interface

- `python scripts/verify_sp01_foundation.py`
- `powershell -ExecutionPolicy Bypass -File scripts/verify_sp01_foundation.ps1`
- `npm run verify:sp01`

## Data Contracts

- Required app files must exist.
- Backend privacy defaults must deny content network, providers, cloud sync, and telemetry.
- SQLite tables must exist.
- Raw vault writes must raise `EncryptionNotConfiguredError`.
- Beginner lesson must include `Beginner Path` and `Sufficiency Review`.

## Dependencies

- Python stdlib only.

## Tests

- Red check observed before scaffold.
- Green check: `npm run verify:sp01`.

## Gotchas

- Uses explicit sqlite connection close to avoid Windows temp cleanup locks.

## Last Updated

SP-01 follow-up
