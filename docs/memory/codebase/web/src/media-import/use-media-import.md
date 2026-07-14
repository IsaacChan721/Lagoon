# useMediaImport.ts

## Purpose

Owns browser file import lifecycle: validate file, create object URL, load duration metadata, save artifact state, reset preview.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\web\src\media-import\useMediaImport.ts`

## Behavior

- Unsupported files enter `unsupported`.
- Large files enter `too-large` with metadata only; SP-03 owns chunking.
- Duration load failures enter `metadata-error` and preserve `durationMs: null`.
- Object URLs are revoked on reset and unmount.
- `importTokenRef` prevents stale async duration reads from overwriting a newer file selection or reset state.

## Last Updated

SP-02 Lecture Media Import
E2E hardening pass, 2026-07-14
