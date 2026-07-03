# SP-05 Memory

## Purpose

Track local retrieval over SP-03 transcript chunks, optional embedding metadata, small eval fixtures, selected-lecture boundaries, and citation-backed retrieval.

## Expected Codebase Mirrors

- `docs/memory/codebase/api/lagoon_local/memory/`
- `docs/memory/codebase/api/lagoon_local/retrieval/`
- `docs/memory/codebase/api/lagoon_local/evals/`
- `docs/memory/codebase/scripts/`

## Prerequisite Context

- Read `docs/run-logs/SP-04-output.md` for visual support outputs if present.
- Read `docs/run-logs/CRIT-01-output.md` for provenance gates.
- Read `docs/run-logs/SP-03-output.md` for transcript artifacts and timestamp schema.
- Use SP-03 transcript chunks as canonical retrieval units.
- Retrieval output must preserve `chunkId`, source `segmentIds`, `mediaArtifactId`, absolute `startMs`/`endMs`, and citation metadata.
- Do not rechunk transcript text unless the new index row still references original chunk IDs and segment IDs.
- Embeddings are expected future optimization. MVP can use local text search if it keeps the same retrieval contract and marks `embeddingStatus`.
- If embeddings are added, require local-only storage, cost controls, rebuild rules, and fallback search.
