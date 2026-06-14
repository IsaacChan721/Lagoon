# SP-02 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Add video and audio capture layer with reliable recording lifecycle.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-02/index.md`
- relevant app and storage memory notes

## In Scope

- Capture permission flow.
- Recording start, pause, stop, save handoff.
- Local media artifact metadata.
- Capture verification.

## Out Of Scope

- No transcription.
- No summarization.
- No RAG.
- No cloud upload.

## Execution Steps

1. Confirm `SP-01` foundation gate.
2. Read capture-related app and storage notes.
3. Add capture UI/control flow.
4. Store raw media through approved local boundary.
5. Add failure states for denied permission and interrupted recording.
6. Verify recording lifecycle.

## Acceptance Criteria

- User can start and stop recording.
- Permission denial is handled.
- Saved media has stable local reference.
- Transcription remains untouched.

## Definition Of Done

- Capture path verified manually or by automated browser test.
- Error states are visible and recoverable.
- Memory notes include media folder/component behavior.

## Verification

- Run relevant app checks.
- Use Browser or Playwright to verify capture controls when available.
- Run `git status --short`.

## Troubleshooting

- If browser blocks media devices, use mock media flags or documented manual check.
- If file save fails, inspect storage boundary and permissions.
- If lifecycle race appears, add state-machine style test before fixing.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite media-capture context first, then build toward browser APIs, state, and local save handoff.

### Created In This Phase

- Capture UI and permission flow.
- Recording lifecycle code for start, pause, stop, and save.
- Local media metadata records.
- Tests or manual checks for capture controls and failure states.

### Lesson 1: Browser Capture Basics

- Prerequisites: none.
- Explain: browser capture asks user permission before audio/video stream access.
- Coding example: show `navigator.mediaDevices.getUserMedia({ audio: true, video: true })` and identify success/error branches.
- Theory Q/A: Why handle denied permission first? Denial is common and must not break app state.
- Key takeaways: permission is user-controlled; app must recover cleanly.

### Lesson 2: Recording Lifecycle

- Prerequisites: understand capture permission.
- Explain: recorder state moves through idle, requesting, recording, paused, saving, saved, and error.
- Coding example: show a small TypeScript union type for `RecordingState`.
- Theory Q/A: Why model states explicitly? Start/stop races become easier to test and reason about.
- Key takeaways: lifecycle bugs come from unclear state transitions; make transitions visible.

### Lesson 3: Local Media Handoff

- Prerequisites: understand recording lifecycle.
- Explain: raw media becomes a local artifact reference, not a transcript yet.
- Coding example: show a metadata object with `id`, `localPath`, `durationMs`, `mimeType`, and `createdAt`.
- Theory Q/A: Why store metadata separately from bytes? Metadata lets later phases find and process media without reading large files constantly.
- Key takeaways: capture produces media artifacts only; transcription waits for `SP-03`.

## Memory Updates

Update `docs/memory/phases/SP-02/index.md` and relevant codebase notes for capture components, storage handoff, and known browser constraints.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-02>`.
3. Run `git commit -m "SP-02: complete phase"`.
4. Run `git push`.

Commit only scoped SP-02 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-02-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
