# MVP Scope Local First

## Status

Locked for `SP-01`; revisit only at phase gate.

## Decision

Lagoon MVP is a local-first, single-user lecture assistant. It helps one user create a local lecture workspace, capture or import one lecture, and later produce grounded transcript-backed notes, summaries, and tutor answers for the selected lecture.

## Context

Phase order starts with local app foundation, then capture, transcription, provenance, understanding, memory/RAG, summaries, tutor, improvement loop, hardening, and optional cloud sync. `SP-00` must remove product ambiguity before implementation begins.

## Options Considered

- Local-first MVP with optional provider calls: best fit for privacy and phase order.
- Cloud-first account app: rejected for MVP because auth, sync, hosting, and multi-tenant security would dominate early phases.
- Full tutor/research suite first: rejected because capture, transcript, provenance, and local memory must exist before reliable tutoring.

## Consequences

- `SP-01` builds foundation only, not lecture intelligence.
- Provider/API choices stay deferred until concrete provider phases.
- Cloud sync stays out of MVP until `SP-10`.
- All early storage and logs assume sensitive lecture content.

## Revisit Trigger

Revisit if user requires multi-device sync, collaborative classrooms, hosted accounts, or remote processing as a core MVP requirement.

## Related Phase

`SP-00`, `SP-01`, `SP-10`
