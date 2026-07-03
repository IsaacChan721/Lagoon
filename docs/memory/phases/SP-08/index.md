# SP-08 Memory

## Purpose

Track manual post-MVP improvement proposals, evaluation-before-implementation, transcript chunk/RAG proposal gates, approval flow, audit trail, and deferral.

## Expected Codebase Mirrors

- `docs/memory/codebase/api/lagoon_local/proposals/`
- `docs/memory/codebase/web/src/proposals/`
- `docs/memory/codebase/docs/proposals/`

## Prerequisite Context

- Read `docs/run-logs/SP-07-output.md` for tutor behavior and eval gaps.
- Read `docs/run-logs/SP-06-output.md` for summary behavior.
- Read `docs/run-logs/SP-05-output.md` for retrieval behavior.
- Read `docs/run-logs/SP-03-output.md` for transcript chunk behavior.
- Read `docs/run-logs/CRIT-01-output.md` for security/provenance gates.
- Proposals that change chunking, embeddings, retrieval, summaries, or tutor policy need eval fixture evidence and rollback notes before approval.
- Never auto-enable provider, embedding, or skill changes from generated proposals.
