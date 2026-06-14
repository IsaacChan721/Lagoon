# Lagoon Local API Boundary

`api/` owns local-only metadata and vault boundaries for the desktop-local app.

SP-01 uses Python stdlib only:

- `sqlite3` for local metadata.
- `pathlib` for local data layout.
- no provider calls.
- no content network upload.

Raw lecture content writes stay blocked until an encryption provider is added in a later phase.

