# Local First Risk Model

## Status

Locked baseline for implementation phases.

## Decision

Lagoon treats lecture media, transcripts, notes, summaries, tutor-practice traces, API keys, logs, and temp files as sensitive. Default behavior keeps content local. Any external provider call must be explicit, feature-scoped, and auditable without logging raw content.

## Context

Lagoon will process recorded lectures and likely student notes. This data may contain personal, academic, copyrighted, or institution-controlled material. The project has no app source yet, so risk model sets constraints for future implementation.

## Options Considered

- Local-only default with opt-in provider boundaries: selected.
- Provider-first processing by default: rejected because it risks accidental content disclosure.
- Full offline-only model: deferred because later transcription or tutor-practice phases may need explicit provider options.

## Consequences

- No raw lecture content should be committed to repo.
- Logs must avoid raw transcript/media snippets.
- Secrets must live outside project files, preferably OS keychain or local secret store chosen in implementation.
- Temp files need scoped paths and cleanup.
- Provenance/citation state is integrity-critical, not decorative.

## Revisit Trigger

Revisit if Lagoon becomes hosted, multi-user, cloud-synced, or institution-managed.

## Related Phase

`SP-00`, `CRIT-01`, `SP-09`, `SP-10`
