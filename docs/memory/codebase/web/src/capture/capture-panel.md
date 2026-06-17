# CapturePanel.tsx

## Purpose

Renders SP-02 capture controls, preview, visible state message, and saved artifact link.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\web\src\capture\CapturePanel.tsx`

## Owns

- Start, Pause, Resume, Stop, Save, Reset buttons.
- Camera preview container.
- Capture status message.
- Local media artifact metadata display and download link.

## Dependencies

- `useMediaCapture()`.

## Tests

- `npm run verify:sp02`
- `npm run build:web`

## Gotchas

- Buttons are state-gated; Save only enables after Stop.
- Download link uses temporary object URL; later phases may replace with a native local bridge.

## Last Updated

SP-02
