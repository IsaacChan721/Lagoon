# useMediaCapture.ts

## Purpose

Owns browser capture permission request, MediaRecorder lifecycle, and save-handoff behavior.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\web\src\capture\useMediaCapture.ts`

## Owns

- `useMediaCapture()`
- Start, pause, resume, stop, save, reset actions.
- Camera preview `videoRef`.
- Stream, recorder, chunk, blob, object URL cleanup.

## Data Contracts

- Requests `{ audio: true, video: true }`.
- Converts stopped chunks into one Blob.
- Creates `LocalMediaArtifact` only after Save.

## Failure States

- `permission-denied`: browser returns `NotAllowedError` or `SecurityError`.
- `interrupted`: unsupported capture, recorder error, stop before active media, or save before stopped blob.

## Tests

- `npm run verify:sp02`
- `npm run build:web`

## Gotchas

- `onstop` is async from the user's click path; state moves to `stopped` before Save can create artifact.
- Track cleanup happens on recorder stop and component unmount.

## Last Updated

SP-02
