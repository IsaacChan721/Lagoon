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

### Lesson Depth Standard

Every lesson below must be written and taught as a 60-90 minute beginner module, not a quick concept note. Use the lesson bullets as topic seeds, then expand them with this structure:

1. Zero-prerequisite setup, 5-10 minutes: define every term used in the lesson, explain why the learner should care, and name the files or planned files they will touch.
2. File map, 10-15 minutes: list each relevant file, folder, command, schema, component, or artifact. For future files, mark them `planned`. Explain what each one owns and what it must not own.
3. Line-by-line code reading, 15-25 minutes: walk through the smallest real code sample available. If implementation does not exist yet, write planned pseudocode and later replace it with real code. Explain each line or block in beginner language, including imports, data shapes, function inputs, outputs, errors, and side effects.
4. Guided hands-on exercise, 15-25 minutes: have the learner run a command, inspect output, trace data through one function, update a harmless fixture, or write a tiny example. Include expected output and what to do if it differs.
5. Debugging or design exercise, 10-20 minutes: give one realistic failure, ask the learner to diagnose it, then provide the answer and the reasoning path.
6. Theory questions and answers, 10-15 minutes: include at least five Q/A pairs that connect the hands-on work to architecture, privacy, security, testing, or user experience.
7. Checkpoint, 5-10 minutes: include a small task the learner can complete without help, plus acceptance criteria.
8. Key takeaways, 5 minutes: list what the learner should remember before moving to the next lesson.

Each lesson must include concrete code or command examples. Prefer real snippets from this codebase once the phase exists. Avoid abstract-only examples. When a lesson covers safety, privacy, auth, encryption, destructive actions, or external providers, spell out the risk clearly and then return to concise style.
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
