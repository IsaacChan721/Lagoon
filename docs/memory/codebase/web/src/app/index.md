# web/src/app

## Purpose

Local app shell, privacy defaults, storage boundary display, and capture panel placement.

## Contains

- `LagoonShell.tsx`
- `privacyDefaults.ts`
- `storageBoundary.ts`
- Imports `../capture/CapturePanel`

## Key Files

- `LagoonShell.tsx`

## Interfaces

- `LagoonShell`
- `privacyDefaults`
- `storageBoundary`

## Dependencies

- React JSX.

## Tests

- `npm run build:web`
- `npm run verify:sp01` checks default/boundary source strings.

## Gotchas

- This folder places media capture in the shell but does not own capture state; `web/src/capture/` owns that domain.
- Still no transcription, RAG, tutor, provider calls, accounts, or sync.

## Last Updated

SP-02
