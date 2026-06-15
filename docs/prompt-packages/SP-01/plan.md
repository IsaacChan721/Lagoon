# SP-01 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Create Lagoon local app foundation after `SP-00` gate passes.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/plans/phase-skill-map.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-01/index.md`
- relevant `docs/memory/codebase/` notes

## In Scope

- Scaffold local app shell.
- Define storage boundary.
- Add first test and dev commands.
- Add codebase memory for generated folders.

## Out Of Scope

- No media capture.
- No transcription.
- No tutor behavior.
- No cloud sync.

## Execution Steps

1. Confirm `SP-00` gate in memory or run log.
2. Read package, this plan, and relevant memory.
3. Choose repo structure from approved `SP-00` decision.
4. Scaffold minimal app shell and local vault boundary.
5. Add narrow verification command.
6. Update memory for generated folders.

## Acceptance Criteria

- App opens to usable local shell.
- Storage boundary is explicit.
- Test/dev command exists or blocker is documented.
- Generated folders have memory notes.

## Definition Of Done

- Narrow checks pass or exact failure is reported.
- No media pipeline work leaked into phase.
- Memory and handoff output are updated.

## Verification

- Run discovered unit/build check.
- If UI exists, verify with Browser or Playwright.
- Run `git status --short`.

## Troubleshooting

- If scaffold fails, inspect package manager and lockfile first.
- If browser verification fails, capture screenshot and console errors.
- If storage decision is missing, block and return to `SP-00`.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite app-foundation context first, then build toward frontend, backend, and verification.

Write the concrete beginner lesson to `docs/lessons/SP-01-local-app-foundation.md`.

The lesson should state whether this plan is sufficient. If it is sufficient, say why and add the missing beginner code-tour details. If it is not sufficient, list exact gaps and update this plan before coding.

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

- `web/` local app shell with privacy/storage UI.
- `api/lagoon_local/` local settings and storage boundary.
- SQLite metadata schema for settings, workspaces, and vault objects.
- `.gitignore` local data protections.
- `scripts/verify_sp01_foundation.py` and PowerShell verification wrapper.
- Codebase mirror notes under `docs/memory/codebase/`.
- Beginner lesson under `docs/lessons/`.

### Lesson 1: Repo Shape

- Prerequisites: none.
- Explain: `web/` owns user interface, `api/` owns local data rules, `scripts/` owns verification.
- Coding example: show `Get-ChildItem web,api,scripts` and map each folder to one responsibility.
- Theory Q/A: Why split UI from local storage? Privacy and persistence rules need a stable boundary independent of components.
- Key takeaways: know folder ownership before editing; avoid mixing app shell, storage, and tests.

### Lesson 2: Local Storage Boundary

- Prerequisites: understand repo shape.
- Explain: SQLite tracks metadata; vault writes stay blocked until real encryption exists.
- Coding example: show pseudocode for `create_workspace()` writing metadata but `write_vault_object()` raising `EncryptionNotConfiguredError`.
- Theory Q/A: Why intentionally block vault content writes? Storing sensitive lecture content without encryption would violate local-first safety.
- Key takeaways: metadata is allowed; sensitive content needs encryption before persistence.

### Lesson 3: App Shell And Privacy Defaults

- Prerequisites: understand storage boundary.
- Explain: first UI should expose local-only defaults and avoid provider calls.
- Coding example: show a React state example for a `networkUploadsEnabled = false` default.
- Theory Q/A: What should a beginner verify in UI? Local-only messaging and disabled upload defaults are visible.
- Key takeaways: privacy is part of UX, not just backend code.

### Lesson 4: Verification Path

- Prerequisites: understand app shell and storage boundary.
- Explain: `npm run verify:sp01` proves foundation files and safety defaults exist.
- Coding example: run `npm run verify:sp01`, then inspect failures before changing code.
- Theory Q/A: Why narrow checks first? They pinpoint foundation regressions before broader builds blur the cause.
- Key takeaways: every phase needs one small reliable check and one broader confidence check.

## Memory Updates

Update `docs/memory/phases/SP-01/index.md` and matching `docs/memory/codebase/` notes for generated folders.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-01>`.
3. Run `git commit -m "SP-01: complete phase"`.
4. Run `git push`.

Commit only scoped SP-01 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-01-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
