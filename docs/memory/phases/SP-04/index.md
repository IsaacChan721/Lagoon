# SP-04 Memory

## Purpose

Track frame sampling, OCR, selected vision analysis, frame evidence, transcript-video alignment, and transcript chunk links.

## Expected Codebase Mirrors

- `docs/memory/codebase/api/lagoon_local/video/`
- `docs/memory/codebase/api/lagoon_local/visuals/`
- `docs/memory/codebase/api/lagoon_local/ocr/`
- `docs/memory/codebase/scripts/`

## Prerequisite Context

- Read `docs/run-logs/CRIT-01-output.md` before trusting transcript/media provenance.
- Read `docs/run-logs/SP-03-output.md` for transcript timestamps.
- Read `docs/run-logs/SP-02-output.md` for imported media artifact references.
- Use SP-03 absolute `startMs`/`endMs` values as the only timeline coordinate system.
- Link visual artifacts to nearby transcript chunk IDs and transcript segment IDs when available.
- Use durable local media artifact paths for extraction. Browser object URLs remain frontend preview-only.
- Keep transcript primary. Visual outputs support slides, diagrams, boards, and demos, with uncertainty labels when evidence is weak.
