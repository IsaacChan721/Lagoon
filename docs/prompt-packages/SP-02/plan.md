# SP-02 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

Treat this phase as an MVP import slice. Prefer beginner-readable code/docs over abstractions. Add no transcription, visual AI, RAG, tutor, provider calls, accounts, cloud sync, or encryption.

## Goal

Replace recording with local lecture media import. User selects an existing lecture audio/video file, previews it locally, validates support, extracts basic metadata, and creates a stable media artifact for SP-03.

## Inputs

Read `docs/run-logs/SP-01-output.md`, `docs/memory/phases/SP-01/index.md`, `docs/memory/phases/SP-02/index.md`, `docs/memory/codebase/web/`, `docs/memory/codebase/api/lagoon_local/`, and current SP-02 package/plan.

## In Scope

Local file picker. Browser preview. Format validation. File size/duration metadata. Local media artifact metadata. Python storage boundary for imported media. Verification and memory updates.

## Out Of Scope

No recording. No screen recording. No transcription. No frame extraction beyond basic preview metadata. No visual model calls. No summaries. No RAG. No tutor. No cloud upload. No encryption.

## Execution Steps

1. Confirm SP-01 foundation gate and clean current worktree.
2. Remove current SP-02 recording implementation and docs.
3. Add media import UI and local preview under `web/src/media-import/`.
4. Add shared media artifact types for uploaded audio/video.
5. Update `LocalStorageBoundary` so imported media metadata and local file handoff are explicit and SP-03-ready.
6. Add `npm run verify:sp02` backed by an import-focused verifier.
7. Update SP-02 lesson, memory mirrors, package, run log template, and phase docs.
8. Run checks and create a corrective SP-02 commit.

## Acceptance Criteria

User can select a supported lecture file. App shows audio/video preview locally. App displays filename, type, size, duration when available, and stable local reference. Unsupported formats show clear recoverable error. SP-03 can consume the artifact contract without recording assumptions.

## Definition Of Done

No browser recording API or recording workflow remains. `npm run verify:sp02`, `npm run verify:sp01`, and `npm run build:web` pass. Memory/docs describe media import. Handoff explains visual strategy and SP-03 contract.

## Verification

Run `npm run verify:sp02`. Run `npm run verify:sp01`. Run `npm run build:web`. Run a scoped source scan for old browser recording APIs and old SP-02 recording paths; confirm no active implementation remains. Run `git status --short`.

## Troubleshooting

If browser cannot preview a codec, still accept metadata only and show metadata error state. If duration is unavailable until metadata loads, keep `durationMs: null` until loaded. If file is too large, store metadata and leave chunking to SP-03. If MIME type is missing, infer from extension and mark confidence low. If browser cannot write app-data directly, keep object URL preview and let Python storage own durable local file handoff.

## Lesson Plan

Create `docs/lessons/SP-02-lecture-media-import.md`. Teach file import, preview, metadata, local-only storage, and why SP-03 owns transcription.

## Memory Updates

Update `docs/memory/phases/SP-02/index.md`, `docs/memory/codebase/web/src/media-import/`, `docs/memory/codebase/api/lagoon_local/storage.md`, `docs/memory/codebase/scripts/`, and related root/web memory notes.

## Git Checkpoint

Commit only scoped corrective SP-02 files. Commit message: `SP-02: replace capture with lecture media import`. Push if remote exists; otherwise report no remote.

## Handoff Output

Write `docs/run-logs/SP-02-output.md` with summary, blockers, contract changes, skill changes, memory updates, phase plan status, tests run, and next gate.

## Visual + Audio Strategy

Default design is audio-first, visuals-supporting. SP-02 imports and previews whole media. SP-03 extracts audio and transcribes with timestamps. SP-04 samples visual frames/slides and links them to transcript segments.

Do not send whole lecture video to a multimodal model by default. For budget, sample frames only at slide/scene changes or at coarse intervals, then analyze representative frames if needed.

Record this decision in memory as: transcript is primary evidence; visuals are supporting evidence unless a future phase proves visual extraction reliable and affordable.
