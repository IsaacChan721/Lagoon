# SP-02 Memory

## Purpose

Track lecture media import, browser-local preview, uploaded media artifact metadata, and local-only storage handoff for SP-03.

## Implemented In SP-02

- Added `web/src/media-import/` for lecture file selection, validation, preview, metadata extraction, and artifact status.
- Import statuses: `idle`, `validating`, `ready`, `unsupported`, `too-large`, `metadata-error`, and `saved`.
- Supported extensions: `.mp4`, `.webm`, `.mov`, `.m4v`, `.mp3`, `.m4a`, `.wav`, `.mpeg`, and `.mpga`.
- Browser preview uses object URLs and revokes them on reset/unmount.
- Video imports render with `<video controls>`; audio imports render with `<audio controls>`.
- Uploaded artifact contract includes `sourceType: "uploaded-file"`, original filename, MIME type, extension, size, duration, media kind, durable local reference, preview-only object URL, creation time, and metadata confidence.
- Added `LocalStorageBoundary.register_uploaded_media_artifact()` for copying imported media into app-data `media/` and recording SQLite metadata.
- Raw media paths remain ignored by Git via `media/` and media extension rules.
- Added `npm run verify:sp02` as narrow import verifier.
- Added beginner lesson `docs/lessons/SP-02-lecture-media-import.md`.

## Verification

- Red observed: `npm run verify:sp02` first failed on missing media import files.
- Green checks must include `npm run verify:sp02`, `npm run verify:sp01`, and `npm run build:web`.

## Scope Guard

- No transcription.
- No summarization.
- No RAG.
- No tutor logic.
- No provider calls.
- No accounts.
- No cloud sync.
- No encryption added.

## Visual + Audio Strategy

Default design is audio-first, visuals-supporting. Transcript is primary evidence; visuals are supporting evidence unless a future phase proves visual extraction reliable and affordable.

SP-02 imports and previews whole media. SP-03 extracts audio, transcribes with absolute timestamps, and creates semantic transcript chunks for RAG. SP-04 samples visual frames/slides and links them to transcript segments/chunks. Do not send whole lecture video to a multimodal model by default.

## Gotchas

- Browser object URLs are temporary preview references, not durable file paths.
- Browser cannot write directly into app-data without a native bridge or user-selected file path.
- Python storage owns durable local file registration for imported media.
- If browser duration metadata is unavailable, artifact keeps `durationMs: null`.
- If MIME type is empty, frontend infers from extension and marks confidence as `extension-fallback`.

## Expected Codebase Mirrors

- `docs/memory/codebase/web/src/media-import/`
- `docs/memory/codebase/api/lagoon_local/`
- `docs/memory/codebase/scripts/`
