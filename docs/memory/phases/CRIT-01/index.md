# CRIT-01 Memory

## Purpose

Track provenance schema, transcript chunk integrity, transcript editor requirements, citation verifier, audit trail, and source traceability.

## Expected Codebase Mirrors

- `docs/memory/codebase/api/lagoon_local/provenance/`
- `docs/memory/codebase/web/src/provenance/`

## Prerequisite Context

- Read `docs/run-logs/SP-03-output.md` for transcript artifact contract.
- Read `docs/run-logs/SP-02-output.md` for imported media artifact contract.
- Read `docs/memory/codebase/api/lagoon_local/` before designing provenance checks.
- Validate transcript chunks include source transcript segment IDs, `mediaArtifactId`, absolute `startMs`/`endMs`, and durable local artifact references.
- Browser object URLs are untrusted preview-only references and must not appear as durable citation or backend-processing sources.
- Block `SP-04`, `SP-05`, and `SP-06` if transcript chunk timestamps remain provider-relative instead of absolute to original lecture media.
