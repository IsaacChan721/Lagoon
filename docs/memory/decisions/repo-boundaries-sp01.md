# Repo Boundaries For SP-01

## Status

Locked as boundary guidance; exact stack deferred to `SP-01`.

## Decision

`SP-00` creates no implementation scaffold. `SP-01` owns first app folders and must keep docs, app runtime, local data/storage, tests, and scripts separated. `docs/` remains planning, memory, and run logs.

## Context

Current repo is minimal: `.git`, `.uv-cache`, `.codex`, `AGENTS.md`, and `docs/`. No build, lint, test, frontend, backend, or package files are present. `SP-00` output should not invent implementation files before the foundation phase.

## Options Considered

- Scaffold app in `SP-00`: rejected as out of scope.
- Leave all folder choices undefined: rejected because `SP-01` needs boundary constraints.
- Define boundary guidance now and exact files later: selected.

## Consequences

- `SP-01` must discover or choose stack before scaffold.
- `SP-01` should add tests with first app files.
- Docs changes remain in `docs/`; app code should not live under `docs/`.

## Revisit Trigger

Revisit if `SP-01` selects a stack whose conventional layout needs adjusted boundaries.

## Related Phase

`SP-00`, `SP-01`
