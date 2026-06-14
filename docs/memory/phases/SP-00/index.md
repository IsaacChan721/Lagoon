# SP-00 Memory

## Purpose

Track product scope, risk model, phase contracts, repo bootstrap decisions, and early architecture decisions.

## Locked MVP Scope

- Local-first single-user lecture assistant.
- First journey: create local lecture workspace, capture or import one lecture, derive transcript/notes later, ask grounded questions against selected lecture later.
- MVP excludes accounts, sharing, multi-user collaboration, cloud sync, LMS integration, autonomous broad web research, and provider calls without explicit consent.
- First implementation slice for `SP-01`: local app foundation only. It should create project structure, local runtime shell, local persistence boundary, settings/privacy consent surface, and health checks. No media capture, transcription, provider integration, or tutor logic in `SP-01`.

## Local-First Risk Model

- Default storage: local device only. Lecture media, transcripts, notes, summaries, embeddings, and tutor traces stay in local app data paths.
- External provider boundary: any upload or API call must be opt-in, feature-scoped, and logged as metadata without leaking content.
- Sensitive assets: lecture media, transcripts, embeddings, generated notes, API keys, local database, temp files, logs, provenance/citation state.
- Main threats: accidental cloud upload, key leakage, log/temp-file data exposure, malicious media/parser input, path traversal, hallucinated provenance, destructive self-improvement changes.
- Secure defaults: deny network by default for content flows, redact logs, keep raw media out of repo, store secrets outside project files, require provenance before tutor/summaries become trusted.

## Repo Boundaries

- `docs/` remains planning and memory.
- `docs/run-logs/` stores phase outputs.
- Future app folders should be introduced by `SP-01`, not `SP-00`.
- Suggested `SP-01` boundary: separate local frontend, local backend/API, local data/storage, tests, and scripts. Exact stack stays `SP-01` decision, but must preserve local-first defaults.

## SP-01 Gate

`SP-01` may start when:

- Main orchestrator accepts SP-00 MVP and non-goals.
- Local-first risk model is accepted as default.
- Repo bootstrap boundaries are accepted.
- Newly installed skills are confirmed discoverable or explicitly skipped.
- `SP-01` contract includes narrow tests for app shell, local storage boundary, privacy/settings defaults, and no network/content upload by default.

## Codebase Mirror Updates

- Decision notes created under `docs/memory/decisions/`.
- Codebase mirror created for `docs/run-logs/`.

## Open Blockers

- Codex restart/reload status for newly installed skills remains from main orchestration. Not a product blocker, but verify before `SP-01`.
- Exact `SP-01` tech stack remains intentionally deferred to `SP-01`; gate requires stack choice before scaffold.
