# Code map

## Plan 00 foundation

| Path | Responsibility |
| --- | --- |
| `api/main.py` | Local, standard-library HTTP API. Its sole endpoint is `GET /api/health`. |
| `web/` | Vite + React + TypeScript browser application. |
| `web/src/api/health.ts` | Fetches the configurable local API base URL and translates timeout/HTTP failures. |
| `web/src/App.tsx` | Renders loading, successful API connection, and useful failure states. |
| `tests/test_health.py` | Starts the real API process and verifies its HTTP/JSON health contract. |
| `.env.example` | Documents the only current browser-visible configuration variable, with no value. |

Future media, transcription, notes, tutor, and storage folders are intentionally absent until their respective approved plans.

