# SP-04 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Add video understanding only where it improves lecture learning value.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-04/index.md`
- media and transcript memory notes

## In Scope

- Key frame or key moment extraction.
- Visual evidence linked to transcript time ranges.
- Visual claim guardrails.
- Verification fixtures.

## Out Of Scope

- No generated factual claims without visual evidence.
- No broad computer vision platform.
- No tutor behavior.

## Execution Steps

1. Confirm provenance gate allows visual enrichment.
2. Read media/transcript contracts.
3. Define minimal visual extraction path.
4. Link visual outputs to transcript timestamps.
5. Add no-fake-visual-claims checks.
6. Verify with sample or fixture.

## Acceptance Criteria

- Visual notes reference exact media time ranges.
- Unsupported visual claims are blocked or marked uncertain.
- Extraction failure does not break transcript workflow.
- Outputs are stored in local memory/artifact boundary.

## Definition Of Done

- Visual enrichment has test or manual verification.
- Provenance is preserved.
- Memory notes explain when this phase should run.

## Verification

- Run relevant media/visual tests.
- Use screenshot/frame checks where available.
- Run `git status --short`.

## Troubleshooting

- If frame extraction fails, test media codec and timestamp handling.
- If model output overclaims, tighten prompt/schema and add citation check.
- If cost is high, reduce sampled frames before changing feature scope.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite visual-understanding context first, then build toward frame extraction, visual evidence, and claim guardrails.

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

- Key frame or key moment extraction logic.
- Visual artifact records linked to media and transcript time ranges.
- Guardrails for uncertain or unsupported visual claims.
- Fixtures or manual checks for frame extraction and evidence links.

### Lesson 1: Why Visual Evidence Exists

- Prerequisites: none.
- Explain: visuals help understand slides, diagrams, boards, and demos that transcript text may miss.
- Coding example: show a visual note object with `mediaArtifactId`, `timeRange`, `framePath`, and `observedText`.
- Theory Q/A: Why avoid broad computer vision? MVP needs lecture learning value, not general image analysis.
- Key takeaways: visual output must point back to exact media time.

### Lesson 2: Frame Extraction

- Prerequisites: understand visual evidence object.
- Explain: extraction samples frames or key moments from recorded media.
- Coding example: show pseudocode for `extractFrames(mediaPath, timestamps)` returning local frame paths.
- Theory Q/A: Why test codec and timestamps first? Most extraction bugs are format or offset problems.
- Key takeaways: frame paths, timestamps, and media IDs must stay synchronized.

### Lesson 3: Claim Guardrails

- Prerequisites: understand frame extraction.
- Explain: app may describe visible evidence but must not invent unseen facts.
- Coding example: show a schema field `claimStatus: "supported" | "uncertain" | "blocked"`.
- Theory Q/A: What happens when model overclaims? Tighten schema and mark unsupported output uncertain or blocked.
- Key takeaways: visual analysis needs evidence links and uncertainty labels.

## Memory Updates

Update `docs/memory/phases/SP-04/index.md` and codebase notes for visual artifact flow, evidence links, and limitations.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-04>`.
3. Run `git commit -m "SP-04: complete phase"`.
4. Run `git push`.

Commit only scoped SP-04 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-04-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
