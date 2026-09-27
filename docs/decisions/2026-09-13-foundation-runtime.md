# Foundation runtime and dependency decision — 2026-09-13

## Recorded environment

| Runtime | Result |
| --- | --- |
| Node.js | `v24.13.0` installed |
| npm | `11.6.2` installed |
| Python | Python `3.14.7` and `3.10` installed for the interactive user; `py -0p` lists both. The isolated Codex sandbox account does not see those registrations. |
| FFmpeg | Not installed or available on PATH |
| Ollama | Not installed or available on PATH |

## Decision

Use Vite, React, TypeScript, and the React Vite plugin for the smallest conventional browser foundation. Use only the Python standard library (`http.server`) for the local API and its health test; no Python package manager or Python dependency file is needed for Plan 00.

The UI uses `VITE_API_BASE_URL`, defaulting to `http://127.0.0.1:8000`, so local API configuration is explicit without exposing secrets. `.env.example` lists only that name and no value.

FFmpeg and Ollama are intentionally not installed or configured. They are out of scope for this foundation slice. Python 3.10+ is required to run the API and its boundary test. On this machine, the Python launcher works in the user's interactive PowerShell session; the isolated Codex command sandbox cannot discover the user's Python registrations, so checks requiring Python must use the installed executable with local process access or be run in the interactive session.

