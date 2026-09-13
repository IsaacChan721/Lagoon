# Worker Plan 00: Foundation

> [!IMPORTANT]
> Establish the smallest runnable local UI/API boundary; do not build media or AI features here.

## Contract

| Item | Requirement |
| --- | --- |
| Inputs | Empty `api/` and `web/` scaffold plus the MVP build plan |
| Deliverable | Vite React TypeScript UI, Python local API, health endpoint, `.env.example`, and beginner setup README |
| Owner | One worker agent |
| Handoff | Run log, code map, commands/results, exact paths changed, and [10/10 readiness score](mvp-plan-readiness-audit.md) |

## Goal

Create a reproducible local starting point where the browser demonstrably communicates with the API. Success means the next worker can add media handling without guessing how to run, configure, or test the app.

## Tasks

1. Record installed Node.js, Python, FFmpeg, and Ollama versions; record dependency or runtime choices in `docs/decisions/`.
2. Create the smallest React/Vite UI and Python API with a health endpoint.
3. Add an API client and one visible health result so the browser proves it can reach the API.
4. Add `.env.example` containing names only, never values or secrets.
5. Write setup, run, and verification instructions in the root README; add a code map and run log.

## Acceptance Criteria

- [ ] A clean local setup can start the UI and API using only documented commands.
- [ ] Loading the UI reaches the local health endpoint and visibly reports success or a useful failure.
- [ ] Automated health/API-boundary test passes, and its exact command is in the README.
- [ ] `.env.example` has no secret value; no real key is tracked.
- [ ] No upload, transcription, notes, tutor, auth, deployment, or database feature is added.

## Controller Verification

Run the README verification command, inspect the health response in the UI, review `.env.example`, apply every item in the controller's Common Independent Quality Gate, and confirm the run log records the result. Do not assign Plan 01 until all five criteria pass and the quality-gate record is entirely pass.

## Outcome and Next Step

| Verification result | Report to user | Next step |
| --- | --- | --- |
| Pass | “Foundation passed” with health-test result and changed paths. | Commit/checkpoint; assign [Plan 01](01-media-extraction-plan.md). |
| Fail | “Foundation failed” with the exact failed acceptance item and command output. | Correct only Plan 00, then repeat all controller checks. |
| Blocked | “Foundation blocked” with the missing runtime or setup detail. | Wait for a human decision; do not start media work. |

## Stop Point

If FFmpeg or Ollama is unavailable, document the finding but do not install, configure, or depend on a paid service in this slice.
