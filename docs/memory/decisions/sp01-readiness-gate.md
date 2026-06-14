# SP-01 Readiness Gate

## Status

Locked gate for starting implementation.

## Decision

`SP-01` can start after the main orchestrator accepts MVP scope, local-first risk model, repo boundary guidance, and skill reload status. `SP-01` must produce a foundation with narrow verification before later media/provider phases begin.

## Context

The phase plan requires clear MVP scope, explicit local-first security assumptions, chosen repo boundaries, and no product ambiguity before `SP-01`.

## Options Considered

- Start coding immediately after `SP-00`: rejected because skill reload and stack choice still need explicit `SP-01` handling.
- Require full product spec for all phases: rejected because later phases can refine their own contracts.
- Require only local foundation criteria: selected.

## Consequences

- `SP-01` acceptance must include app shell, local persistence boundary, privacy/settings defaults, and no network/content upload by default.
- Media capture, transcription, provider calls, and tutor logic remain locked out until later phases.
- Skill discoverability check should happen before implementation tasks run.

## Revisit Trigger

Revisit if `SP-01` contract changes from local foundation into media or AI integration.

## Related Phase

`SP-00`, `SP-01`
