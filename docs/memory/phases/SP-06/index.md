# SP-06 Memory

## Purpose

Track transcript chunk-grounded summaries, local evidence policy, citation coverage, and summary UI.

## Expected Codebase Mirrors

- `docs/memory/codebase/api/lagoon_local/summaries/`
- `docs/memory/codebase/api/lagoon_local/evidence/`
- `docs/memory/codebase/web/src/summaries/`

## Prerequisite Context

- Read `docs/run-logs/SP-05-output.md` for retrieval contract.
- Read `docs/run-logs/SP-04-output.md` for visual support outputs if present.
- Read `docs/run-logs/CRIT-01-output.md` before emitting grounded summaries.
- Read `docs/run-logs/SP-03-output.md` for transcript artifacts.
- Prefer SP-03 transcript chunks and SP-05 retrieval results as summary evidence.
- Every factual claim should cite transcript chunk IDs, transcript segment IDs, visual artifact IDs when used, and absolute `startMs`/`endMs`.
- Do not cite browser object URLs or provider-relative chunk timestamps.
