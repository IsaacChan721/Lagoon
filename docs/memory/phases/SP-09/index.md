# SP-09 Memory

## Purpose

Track hardening, packaging, release smoke tests, observability, cost dashboard, media/transcript privacy review, and Windows install behavior.

## Expected Codebase Mirrors

- `docs/memory/codebase/tests/`
- `docs/memory/codebase/packaging/`
- `docs/memory/codebase/observability/`

## Prerequisite Context

- Read all prior run logs in `docs/run-logs/`.
- Read all phase memory notes in `docs/memory/phases/`.
- Read root, web, API, and scripts memory before hardening.
- Release checks must include raw imported media, extracted audio, transcript artifacts, transcript chunks, embeddings if present, provider keys, temp files, logs, and tutor traces.
- Block release if any lecture content can leave local storage without explicit user approval.
