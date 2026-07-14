# web/src/media-import

## Purpose

Own SP-02 Lecture Media Import UI, validation, browser preview, metadata extraction, and uploaded media artifact shape.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\web\src\media-import\`

## Contains

- `mediaImportState.ts`
- `useMediaImport.ts`
- `MediaImportPanel.tsx`

## Contracts

- Supports `.mp4`, `.webm`, `.mov`, `.m4v`, `.mp3`, `.m4a`, `.wav`, `.mpeg`, and `.mpga`.
- Uses object URLs for preview and revokes them on reset/unmount.
- Guards async duration metadata reads with `importTokenRef` so stale reads cannot overwrite newer state.
- Emits uploaded artifact metadata with stable `media/<id>.<ext>` local reference.
- Uses `<video controls>` for video and `<audio controls>` for audio.

## Last Updated

SP-02 Lecture Media Import
E2E hardening pass, 2026-07-14
