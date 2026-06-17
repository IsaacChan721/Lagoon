# captureState.ts

## Purpose

Defines capture state names and local media artifact metadata for SP-02.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\web\src\capture\captureState.ts`

## Owns

- `CaptureStatus`
- `LocalMediaArtifact`
- `CaptureState`
- `initialCaptureState`
- `createLocalMediaArtifact()`
- `captureInterrupted()`

## Public Interface

- Import types/functions from `web/src/capture/captureState.ts`.

## Data Contracts

- Saved browser artifacts use local-only `media/<id>.<ext>` references.
- Artifact `objectUrl` is for browser download only, not durable storage.

## Tests

- `npm run verify:sp02`
- `npm run build:web`

## Gotchas

- `localReference` is stable metadata, but actual browser bytes require user download or future native bridge.

## Last Updated

SP-02
