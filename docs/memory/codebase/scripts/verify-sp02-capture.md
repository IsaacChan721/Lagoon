# verify_sp02_capture

## Purpose

Narrow SP-02 gate check for browser capture source contracts, local media storage handoff, and ignored raw media paths.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\scripts\verify_sp02_capture.py`

## Owns

- Required capture file presence.
- State vocabulary checks.
- `getUserMedia`, `MediaRecorder`, object URL, and failure-state source checks.
- Python `save_media_artifact()` integration check with temp app-data root.
- `.gitignore` media boundary check.

## Public Interface

- `python scripts/verify_sp02_capture.py`
- `powershell -ExecutionPolicy Bypass -File scripts/verify_sp02_capture.ps1`
- `npm run verify:sp02`

## Dependencies

- Python stdlib only.
- PowerShell wrapper can fall back to Codex bundled Python.

## Tests

- Red check observed before capture implementation.
- Green check: `npm run verify:sp02`.

## Gotchas

- Verifier scans source contracts and runs Python storage handoff; it does not automate real camera permission.

## Last Updated

SP-02
