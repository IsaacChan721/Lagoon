# scripts

## Purpose

Repository verification scripts.

## Contains

- `verify_sp01_foundation.py`
- `verify_sp01_foundation.ps1`
- `verify_sp02_media_import.py`
- `verify_sp02_media_import.ps1`
- `verify_sp03_transcription.py`
- `verify_sp03_transcription.ps1`

## Key Files

- `scripts/verify_sp01_foundation.py`
- `scripts/verify_sp01_foundation.ps1`
- `scripts/verify_sp02_media_import.py`
- `scripts/verify_sp02_media_import.ps1`
- `scripts/verify_sp03_transcription.py`
- `scripts/verify_sp03_transcription.ps1`

## Interfaces

- `npm run verify:sp01`
- `npm run verify:sp02`
- `npm run verify:sp03`
- `npm run test`

## Dependencies

- Python stdlib.
- PowerShell wrapper for runtime discovery.

## Tests

- Self-run by `npm run verify:sp01`.
- SP-02 Lecture Media Import verifier runs by `npm run verify:sp02`.
- SP-03 media transcription verifier runs by `npm run verify:sp03`.

## Gotchas

- Wrapper falls back to Codex bundled Python when PATH Python is missing.

## Last Updated

SP-02
SP-03
