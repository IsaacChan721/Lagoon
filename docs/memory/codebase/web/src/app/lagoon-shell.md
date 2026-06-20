# LagoonShell

## Purpose

User-facing local shell for privacy defaults, storage boundary, and SP-02 Lecture Media Import entry point.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\web\src\app\LagoonShell.tsx`

## Owns

- Local workspace heading/status.
- Storage boundary summary.
- Privacy default status list.
- Media import panel placement.

## Public Interface

- `LagoonShell()`

## Data Contracts

- Reads `privacyDefaults`.
- Reads `storageBoundary`.
- Renders `MediaImportPanel`.

## Dependencies

- React JSX.
- `web/src/media-import/MediaImportPanel.tsx`.

## Tests

- `npm run build:web`.
- `npm run verify:sp02`.

## Gotchas

- Shell does not own import internals; media import state lives in `web/src/media-import/`.
- No workspace creation, provider, transcription, RAG, or sync actions yet.

## Last Updated

SP-02
