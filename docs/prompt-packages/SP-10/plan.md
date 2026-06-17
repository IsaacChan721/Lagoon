# SP-10 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Defer cloud sync and document a post-MVP decision gate.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-10/index.md`
- storage, security, and release memory notes

## In Scope

- Post-MVP sync decision criteria.
- Explicit user approval requirements.
- Risks and non-goals for cloud sync.
- Future implementation checklist.

## Out Of Scope

- No cloud sync implementation in MVP.
- No Supabase/RLS/schema work in MVP.
- No encryption system work in MVP.
- No default cloud upload.

## Execution Steps

1. Confirm local MVP release gate.
2. Read storage/security memory.
3. Document why sync is deferred from MVP.
4. Define user approval criteria for any future sync project.
5. List future security questions: auth, encryption, RLS, conflicts, recovery.
6. Verify no MVP code path uploads lecture content.

## Acceptance Criteria

- Cloud sync is absent from MVP runtime.
- Future sync requires explicit user approval and a new implementation plan.
- Security questions are listed but not implemented.
- No default upload path exists.

## Definition Of Done

- Deferred sync decision is documented.
- Verification confirms no upload path was added.
- Memory notes capture risks and future checklist.

## Verification

- Verify no cloud sync code path exists in MVP.
- Verify no plaintext lecture content leaves local storage.
- Run `git status --short`.

## Troubleshooting

- If user requests sync, create a new post-MVP plan first.
- If auth/RLS/encryption is uncertain, keep sync out of MVP.
- If future sync risk is high, document blocker instead of implementing.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite post-MVP planning context first, then build toward why cloud sync is deferred, what approval would require, and how to verify no upload path exists.

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

- Deferred sync decision note.
- Future approval checklist.
- Risk register for auth, encryption, RLS, conflicts, and recovery.
- Verification that MVP has no cloud upload path.

### Lesson 1: Why Sync Is Deferred

- Prerequisites: none.
- Explain: Lagoon MVP is local-first, so cloud sync is deferred until the local app is useful and stable.
- Coding example: show settings fields with no `syncEnabled` runtime path and a future-only `syncDecisionStatus`.
- Theory Q/A: Why no default cloud upload? Lecture content is sensitive and sync adds auth, storage, conflicts, and privacy work outside MVP.
- Key takeaways: deferral is a valid product decision; consent is required before future sync work.

### Lesson 2: Future Security Questions

- Prerequisites: understand sync deferral.
- Explain: future sync must answer auth, encryption, authorization, conflicts, and recovery before code starts.
- Coding example: show a checklist object with `authPlan`, `encryptionPlan`, `authorizationPlan`, and `rollbackPlan`.
- Theory Q/A: Why not implement encryption now? MVP does not upload content, so encryption work would add complexity without user-visible value.
- Key takeaways: never add sync primitives before the product needs and risks are approved.

### Lesson 3: Approval Gate

- Prerequisites: understand future security questions.
- Explain: future sync needs explicit user approval and a separate plan before Supabase, RLS, or provider code appears.
- Coding example: show a decision record with `approvedBy`, `approvedAt`, `provider`, `threatModelPath`, and `rollbackPath`.
- Theory Q/A: Why block if RLS is uncertain? Misconfigured policy can expose private lecture metadata or content.
- Key takeaways: authorization still matters later, but it is not MVP implementation work.

### Lesson 4: No-Upload Verification

- Prerequisites: understand approval gate.
- Explain: MVP verification should prove no lecture content upload path exists.
- Coding example: run `rg -n "fetch\\(|axios|upload|Supabase|syncEnabled|cloud" api web docs` and explain expected findings.
- Theory Q/A: Why verify absence? Local-first promises fail if hidden upload paths appear.
- Key takeaways: no-upload verification protects MVP simplicity and user trust.

## Memory Updates

Update `docs/memory/phases/SP-10/index.md` and codebase notes for deferred sync decision, future checklist, and no-upload verification.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-10>`.
3. Run `git commit -m "SP-10: complete phase"`.
4. Run `git push`.

Commit only scoped SP-10 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-10-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
