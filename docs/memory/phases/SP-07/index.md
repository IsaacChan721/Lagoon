# SP-07 Memory

## Purpose

Track simple tutor-practice sessions, question generation, grading, selected-lecture boundaries, transcript chunk evidence, and evidence-backed feedback.

## Expected Codebase Mirrors

- `docs/memory/codebase/api/lagoon_local/tutor/`
- `docs/memory/codebase/web/src/tutor/`

## Prerequisite Context

- Read `docs/run-logs/SP-06-output.md` for summary/evidence contract.
- Read `docs/run-logs/SP-05-output.md` for retrieval and selected-lecture boundaries.
- Read `docs/run-logs/CRIT-01-output.md` for provenance requirements.
- Tutor input should come from SP-05 retrieval over SP-03 transcript chunks.
- Preserve `lectureIds`, `chunkId`, citation IDs, and absolute time ranges in tutor prompts, answers, grading, and feedback.
- If selected lecture retrieval lacks evidence, tutor should admit unknown instead of using unrelated memory.
