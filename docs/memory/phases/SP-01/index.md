# SP-01 Memory

## Purpose

Track local app foundation: frontend shell, backend API, SQLite metadata, local artifact boundary, and initial tests.

## Stack Choice

- Chosen in SP-01 before scaffold: Vite + React + TypeScript for `web/`.
- Chosen local backend/storage boundary: Python stdlib package in `api/` using `sqlite3`, `pathlib`, and dataclasses.
- Dependency policy: npm dependencies are installed for web build; Python foundation has no external package dependency.
- Reason: fast local shell, small local-first storage surface, no cloud service, no provider calls.

## Implemented Foundation

- `web/` owns first local app shell with privacy defaults and storage boundary display.
- `api/lagoon_local/` owns local-only settings and storage layout.
- SQLite metadata schema creates `app_settings`, `lecture_workspaces`, and `vault_objects`.
- Raw lecture content remains local-only and outside Git. Encryption is a later hardening option, not an MVP requirement.
- `.gitignore` blocks local Lagoon data, databases, vault/media/transcript/embedding folders, dependencies, build outputs, and env secrets.
- `scripts/verify_sp01_foundation.py` and `.ps1` provide first verification command.
- `docs/lessons/SP-01-local-app-foundation.md` provides beginner code-tour lesson for this exact foundation.

## Verification

- Red check observed first: verifier failed on missing SP-01 files.
- Passed: `npm run verify:sp01`.
- Passed: `npm run build:web`.
- Passed: scoped Vite HTTP smoke returned `STATUS=200` and `HAS_ROOT=True` at `http://127.0.0.1:5173`.
- Browser plugin attempted and blocked by `node_repl` kernel Windows sandbox spawn failure; no DOM screenshot taken.

## Scope Guard

- No media import.
- No transcription.
- No RAG.
- No tutor logic.
- No provider calls.
- No accounts.
- No cloud sync.
- No content upload by default.

## Gotchas

- `sqlite3.Connection` context manager does not close the connection; storage code closes explicitly to avoid Windows file locks.
- Root npm verification uses PowerShell wrapper because `python` is not on PATH in this workspace.
- `web/package.json` pins dev server to `127.0.0.1:5173` because PowerShell/npm arg forwarding mangled ad hoc port args.
- Lesson doc now names simple beginner path and explicit stop-before-SP-02 features.

## Expected Codebase Mirrors

- `docs/memory/codebase/web/`
- `docs/memory/codebase/api/`
- `docs/memory/codebase/scripts/`
- `docs/memory/codebase/docs/lessons/`
