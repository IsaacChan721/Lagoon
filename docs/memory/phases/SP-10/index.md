# SP-10 Memory

## Purpose

Track deferred cloud sync decision, transcript chunk/embedding sensitivity, future approval checklist, no-upload verification, and post-MVP risk questions.

## Expected Codebase Mirrors

- `docs/memory/codebase/docs/sync-decision/`
- `docs/memory/codebase/docs/no-upload-verification/`

## Prerequisite Context

- Read `docs/run-logs/SP-09-output.md` before any sync decision.
- Read all prior run logs in `docs/run-logs/`.
- Read `docs/memory/decisions/local-first-risk-model.md`.
- Treat `api/lagoon_local/sync/` and `web/src/sync/` as future roots only if user explicitly approves cloud sync implementation.
- Treat media, transcripts, transcript chunks, embeddings, summaries, tutor traces, and provenance records as sensitive sync data.
- Future sync requires explicit user approval, threat model, encryption plan, RLS/authz plan, conflict handling, deletion/export plan, and rollback.
- Verify no MVP upload path exists for transcript chunks or embeddings.
