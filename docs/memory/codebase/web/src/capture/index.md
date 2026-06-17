# web/src/capture

## Purpose

Own browser video/audio capture UI, MediaRecorder lifecycle, and local media handoff metadata.

## Contains

- `captureState.ts`
- `useMediaCapture.ts`
- `CapturePanel.tsx`

## Key Files

- `web/src/capture/captureState.ts`
- `web/src/capture/useMediaCapture.ts`
- `web/src/capture/CapturePanel.tsx`

## Interfaces

- `CapturePanel()`
- `useMediaCapture()`
- `CaptureStatus`
- `LocalMediaArtifact`
- `createLocalMediaArtifact()`

## Data Contracts

- Capture state statuses: `idle`, `requesting-permission`, `recording`, `paused`, `stopped`, `saving`, `saved`, `permission-denied`, `interrupted`.
- Browser save handoff returns stable `localReference` shaped like `media/<id>.<ext>`.
- Artifact metadata includes id, MIME type, duration, byte size, created timestamp, download name, object URL.

## Dependencies

- React hooks.
- Browser `navigator.mediaDevices.getUserMedia`.
- Browser `MediaRecorder`.
- Browser `URL.createObjectURL`.

## Tests

- `npm run verify:sp02`
- `npm run build:web`

## Gotchas

- Browser object URLs are temporary and revoked on reset/unmount.
- Web capture does not call Python storage directly in SP-02.
- Camera/microphone permission prompts are user-controlled; denial must keep app recoverable.

## Last Updated

SP-02
