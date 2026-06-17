# LagoonShell

## Purpose

User-facing local shell for privacy defaults, storage boundary, and SP-02 capture entry point.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\web\src\app\LagoonShell.tsx`

## Owns

- Local workspace heading/status.
- Storage boundary summary.
- Privacy default status list.
- Capture panel placement.

## Public Interface

- `LagoonShell()`

## Data Contracts

- Reads `privacyDefaults`.
- Reads `storageBoundary`.
- Renders `CapturePanel`.

## Dependencies

- React JSX.
- `web/src/capture/CapturePanel.tsx`.

## Tests

- `npm run build:web`.
- `npm run verify:sp02`.

## Gotchas

- Shell does not own capture internals; capture state and MediaRecorder live in `web/src/capture/`.
- No workspace creation, provider, transcription, RAG, or sync actions yet.

## Last Updated

SP-02
