# SP-02 Memory

## Purpose

Track browser video/audio capture, recording state machine, local-only media file handoff, and capture UI.

## Implemented In SP-02

- Added `web/src/capture/` for browser capture UI, state vocabulary, and MediaRecorder hook.
- Capture statuses now include `idle`, `requesting-permission`, `recording`, `paused`, `stopped`, `saving`, `saved`, `permission-denied`, and `interrupted`.
- Browser capture requests `navigator.mediaDevices.getUserMedia({ audio: true, video: true })`.
- Recording lifecycle supports start, pause, resume, stop, save, and reset.
- Save creates a browser-local `LocalMediaArtifact` with stable `media/<id>.<ext>` reference, MIME type, duration, size, timestamp, download name, and object URL.
- Added `LocalStorageBoundary.save_media_artifact()` for local-only Python media file handoff into app-data `media/` with SQLite `media_artifacts` metadata.
- Raw media paths remain ignored by Git via `media/` and `*.webm`.
- Added `npm run verify:sp02` as narrow capture verifier.
- Added beginner lesson `docs/lessons/SP-02-video-audio-capture.md`.

## Verification

- Red observed: `verify_sp02_capture.py` first failed on missing capture files.
- Green: `npm run verify:sp02`.
- Green regression: `npm run verify:sp01`.
- Green build: `npm run build:web`.
- HTTP smoke: Vite started inside one PowerShell command and returned `STATUS=200`, `HAS_ROOT=True`.
- Browser connector blocked by Windows sandbox spawn failure: `CreateProcessAsUserW failed: 5`.
- Playwright fallback unavailable without remote npm execution; escalation to download `@playwright/cli` was rejected by policy.

## Scope Guard

- No transcription.
- No summarization.
- No RAG.
- No tutor logic.
- No provider calls.
- No accounts.
- No cloud sync.
- No encryption added.

## Gotchas

- Browser cannot write directly into app data without a native bridge or user-selected file path. Current browser save handoff exposes a download/object URL and stable local reference.
- Python storage can persist bytes locally now, but the web app does not call Python directly in SP-02.
- Permission denial is handled as a visible recoverable state.
- Interrupted recording is handled when capture APIs are unavailable, recorder errors, or stop/save happens out of order.

## Expected Codebase Mirrors

- `docs/memory/codebase/web/src/capture/`
- `docs/memory/codebase/web/src/components/`
- `docs/memory/codebase/api/lagoon_local/`
- `docs/memory/codebase/scripts/`
