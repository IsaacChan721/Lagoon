# SP-03 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Implement media processing and transcription pipeline.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-03/index.md`
- media capture and storage memory notes

## In Scope

- Media chunking.
- Transcription request flow.
- Retry and failure handling.
- Transcript stitching.
- Transcript artifact storage.

## Out Of Scope

- No source enrichment.
- No video understanding beyond needed media metadata.
- No tutor features.

## Execution Steps

1. Confirm `SP-02` media artifact contract.
2. Read transcription skill/API docs only as needed.
3. Add chunking and transcription pipeline.
4. Stitch transcript with timestamps and source media references.
5. Add retry/error states.
6. Verify transcript output with fixture or sample media.

## Acceptance Criteria

- Media artifact can produce transcript artifact.
- Transcript keeps media provenance and timestamps.
- Retry/failure behavior is deterministic.
- Large media is chunked or blocked with clear message.

## Definition Of Done

- Pipeline check passes with fixture/sample.
- Transcript artifact is saved locally.
- Failure states are documented in memory and handoff.

## Verification

- Run unit/integration tests for chunking and stitching.
- Run one transcription fixture path if credentials and sample exist.
- Run `git status --short`.

## Troubleshooting

- If API fails, classify auth, quota, network, or payload issue first.
- If stitching drifts, test chunk boundaries.
- If files are too large, reduce chunk size before changing API contract.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite transcription context first, then build toward chunking, provider calls, stitching, and storage.

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

- Media chunking pipeline.
- Transcription request and retry flow.
- Transcript stitching logic with timestamps.
- Transcript artifact schema and local storage.
- Tests or fixtures for chunking, retry, and stitching behavior.

### Lesson 1: From Media To Transcript

- Prerequisites: none.
- Explain: transcription turns local audio/video into timed text segments.
- Coding example: show a transcript segment object with `startMs`, `endMs`, `text`, and `mediaArtifactId`.
- Theory Q/A: Why keep timestamps? They connect answers, summaries, and citations back to exact lecture moments.
- Key takeaways: transcript is structured data, not just one text blob.

### Lesson 2: Chunking Large Media

- Prerequisites: understand transcript segments.
- Explain: large files must be split or rejected with clear reason.
- Coding example: show pseudocode for `chunkMedia(file, maxDurationMs)` returning ordered chunk descriptors.
- Theory Q/A: Why avoid changing API contract first? Bad chunk boundaries usually cause drift before provider choice matters.
- Key takeaways: deterministic chunk IDs and time ranges make stitching testable.

### Lesson 3: Retry And Failure Handling

- Prerequisites: understand chunking.
- Explain: failures are classified as auth, quota, network, payload, or unknown.
- Coding example: show a retry rule that retries network errors but not auth errors.
- Theory Q/A: Why classify before retrying? Retrying permanent failures wastes time and can hide real setup issues.
- Key takeaways: retries need limits, error classes, and visible user states.

### Lesson 4: Stitching And Storage

- Prerequisites: understand chunking and retry.
- Explain: stitched transcript preserves segment order and media provenance.
- Coding example: show sorting chunks by `chunkIndex`, then offsetting segment times by chunk start time.
- Theory Q/A: What proves stitching works? Fixture with known chunk boundaries and expected timestamps.
- Key takeaways: transcript storage must preserve source media ID, timestamps, and failure caveats.

## Memory Updates

Update `docs/memory/phases/SP-03/index.md` and codebase notes for media pipeline, transcript schema, retry rules, and caveats.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-03>`.
3. Run `git commit -m "SP-03: complete phase"`.
4. Run `git push`.

Commit only scoped SP-03 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-03-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
