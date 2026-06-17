# scripts

## Purpose

Repository verification scripts.

## Contains

- `verify_sp01_foundation.py`
- `verify_sp01_foundation.ps1`
- `verify_sp02_capture.py`
- `verify_sp02_capture.ps1`

## Key Files

- `scripts/verify_sp01_foundation.py`
- `scripts/verify_sp01_foundation.ps1`
- `scripts/verify_sp02_capture.py`
- `scripts/verify_sp02_capture.ps1`

## Interfaces

- `npm run verify:sp01`
- `npm run verify:sp02`
- `npm run test`

## Dependencies

- Python stdlib.
- PowerShell wrapper for runtime discovery.

## Tests

- Self-run by `npm run verify:sp01`.
- SP-02 capture verifier runs by `npm run verify:sp02`.

## Gotchas

- Wrapper falls back to Codex bundled Python when PATH Python is missing.

## Last Updated

SP-02
