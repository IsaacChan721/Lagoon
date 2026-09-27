# Lagoon

Lagoon is a local learning-tool MVP. This repository currently contains **Plan 00: Foundation** only: a React browser UI and a Python health API. It does not accept media, call AI services, store lessons, or require any API keys.

## Prerequisites

- Node.js 24.13.0 (recorded on the development machine)
- Python 3.10 or later (required to run the API)

FFmpeg and Ollama are not required for this foundation. They were not available on the development machine and are deliberately not installed or configured in this slice.

## First-time setup

1. Copy `.env.example` to `web/.env` only if the API is not running at `http://127.0.0.1:8000`. Set `VITE_API_BASE_URL` there to the API origin. Do not put secrets in this file.
2. In one terminal, start the API:

   ```powershell
   py api/main.py
   ```

3. In a second terminal, install the UI dependencies and start Vite:

   ```powershell
   cd web
   npm install
   npm run dev
   ```

4. Open the local URL printed by Vite (normally `http://127.0.0.1:5173`). The page automatically calls `GET /api/health` and shows either “API connection successful” or a useful failure message.

## Verification

Run this exact automated API-boundary verification command from the repository root:

```powershell
py -m unittest tests.test_health
```

The test starts the real local Python API on an unused loopback port, calls its health endpoint, and checks the JSON response. It uses no network service, key, media, or private data.

For the manual UI check, start both processes as above, load the Vite URL, and confirm the visible status changes to **API connection successful** with the API message `Lagoon API is healthy.` Stop the API and reload to confirm that the page instead reports a connection failure.

## Code map

- `api/main.py` — standard-library local HTTP API; exposes `GET /api/health`.
- `web/src/api/health.ts` — browser API client and error handling.
- `web/src/App.tsx` — minimal visible health state.
- `tests/test_health.py` — real Python HTTP boundary test.
- `docs/memory/code-map.md` — maintained component/folder map.
- `docs/decisions/2026-09-13-foundation-runtime.md` — runtime and dependency choices.

## Scope

Plan 00 intentionally does not include uploads, FFmpeg processing, transcription, notes, tutor chat, authentication, deployment, a database, or polish. See `docs/plans/00-foundation-plan.md`.

