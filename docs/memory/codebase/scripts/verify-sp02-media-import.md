# verify_sp02_media_import

## Purpose

Narrow SP-02 gate check for lecture media import source contracts, local storage handoff, docs, and removal of old browser recording APIs.

## Real Code Paths

- `C:\Users\isaac\Documents\Projects\Lagoon\scripts\verify_sp02_media_import.py`
- `C:\Users\isaac\Documents\Projects\Lagoon\scripts\verify_sp02_media_import.ps1`

## Interface

- `npm run verify:sp02`

## Checks

- Required media-import files exist.
- Old recording folder, verifier, and lesson are removed.
- Frontend contract includes statuses, supported extensions, object URL lifecycle, audio/video preview, and artifact shape.
- Python storage can register uploaded media into app-data `media/` with SQLite metadata.
- SP-02 docs describe lecture media import and audio-first visual strategy.

## Last Updated

SP-02 Lecture Media Import
