# SP-08 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Document post-MVP improvement proposals without activating generated skills.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/plans/custom-skill-optimization.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-08/index.md`
- tutor, retrieval, transcript chunk, and eval memory notes

## In Scope

- Manual improvement proposal notes.
- Eval-before-implementation gate.
- Retrieval/chunk-quality eval requirement for tutor or RAG improvements.
- Explicit user approval path.
- Security review checklist for any future generated skill.

## Out Of Scope

- No generated skill activation in MVP.
- No auto-install of untrusted skills.
- No marketplace skill intake.
- No hidden tool escalation.

## Execution Steps

1. Read custom skill governance docs.
2. Define lightweight proposal note format and review states.
3. Add eval gate before any future implementation, including transcript chunk, retrieval, or tutor-policy changes.
4. Add explicit user approval requirement.
5. Add security checklist for future generated skill content.
6. Verify proposal flow with a small fixture.

## Acceptance Criteria

- Improvements are proposal-only by default.
- Eval result is required before implementation, with retrieval/chunk-quality evidence for RAG or tutor changes.
- User approval path exists.
- Security review blocks unsafe future skill instructions.

## Definition Of Done

- Governance flow is tested or documented with fixture.
- No generated or untrusted skill is installed automatically.
- Memory notes record policy and caveats.

## Verification

- Run proposal governance tests if present.
- Inspect generated proposal files for hidden commands/tool escalation.
- Run `git status --short`.

## Troubleshooting

- If improvement value is unclear, keep proposal deferred.
- If proposal changes transcript chunking, embeddings, retrieval, or tutor policy, require fixture evidence before approval.
- If eval is flaky, require repeated pass before implementation.
- If security concern appears, quarantine proposal and block phase.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite improvement-governance context first, then build toward proposals, evals, approval, and security review.

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

- Manual improvement proposal artifact format.
- Eval-before-implementation gate for skill, retrieval, transcript chunk, and tutor changes.
- User approval path.
- Security review notes for any future generated skills.

### Lesson 1: Why Improvements Need Governance

- Prerequisites: none.
- Explain: improvements can change user workflows or agent behavior, so MVP records proposals instead of activating new skills.
- Coding example: show a proposal file with `status: proposed`, `owner`, `risk`, and `evalCommand`.
- Theory Q/A: Why not auto-install useful-looking skills? Hidden instructions can cause unsafe tool use or bad code changes.
- Key takeaways: proposal first, implementation later.

### Lesson 2: Eval-Before-Implementation

- Prerequisites: understand proposal status.
- Explain: an improvement must pass repeatable checks before it becomes implementation work.
- Coding example: show `npm run test:skill-governance` or a fixture command recording pass/fail evidence.
- Theory Q/A: Why require repeated pass for flaky evals? Flaky behavior is not reliable enough for automation.
- Key takeaways: evidence beats intention.

### Lesson 3: Approval And Deferral

- Prerequisites: understand eval gates.
- Explain: every improvement needs explicit user approval before implementation.
- Coding example: show metadata fields `approvedBy`, `approvedAt`, and `deferredReason`.
- Theory Q/A: Why require approval before implementation? It prevents speculative complexity from entering MVP.
- Key takeaways: governance includes clear approval and deferral paths.

### Lesson 4: Security Review

- Prerequisites: understand rollback.
- Explain: review checks for hidden escalation, destructive commands, secrets, and unsafe network use.
- Coding example: use `rg -n "rm |git reset|require_escalated|API_KEY|token" proposed-skill-path`.
- Theory Q/A: What if concern appears? Quarantine and block rather than partially trust.
- Key takeaways: generated automation is code with security impact.

## Memory Updates

Update `docs/memory/phases/SP-08/index.md` and codebase notes for improvement proposal lifecycle, eval gate, and approval path.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-08>`.
3. Run `git commit -m "SP-08: complete phase"`.
4. Run `git push`.

Commit only scoped SP-08 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-08-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
