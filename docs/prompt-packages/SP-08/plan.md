# SP-08 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Add gated improvement loop for tutor and workflow skill proposals.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/plans/custom-skill-optimization.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-08/index.md`
- tutor and eval memory notes

## In Scope

- Skill proposal artifacts.
- Eval-before-enable gate.
- Rollback and disable path.
- Security review for generated skills.

## Out Of Scope

- No auto-install of untrusted skills.
- No marketplace skill intake.
- No hidden tool escalation.

## Execution Steps

1. Read custom skill governance docs.
2. Define proposal format and review states.
3. Add eval gate before any skill activation.
4. Add rollback/disable behavior.
5. Add security checks for skill content.
6. Verify proposal flow with fixture.

## Acceptance Criteria

- New skills are proposal-only by default.
- Eval result is required before enablement.
- Rollback path exists.
- Security review blocks unsafe instructions.

## Definition Of Done

- Governance flow is tested or documented with fixture.
- No untrusted skill is installed automatically.
- Memory notes capture policy and caveats.

## Verification

- Run skill governance tests if present.
- Inspect generated proposal files for hidden commands/tool escalation.
- Run `git status --short`.

## Troubleshooting

- If skill value is unclear, keep proposal disabled.
- If eval is flaky, require repeated pass before enablement.
- If security concern appears, quarantine proposal and block phase.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite skill-governance context first, then build toward proposals, evals, rollback, and security review.

### Created In This Phase

- Skill proposal artifact format.
- Eval-before-enable gate.
- Rollback and disable path.
- Security review notes for generated skills.

### Lesson 1: Why Skills Need Governance

- Prerequisites: none.
- Explain: generated skills can change agent behavior, so they start disabled until reviewed.
- Coding example: show a proposal file with `status: proposed`, `owner`, `risk`, and `evalCommand`.
- Theory Q/A: Why not auto-install useful-looking skills? Hidden instructions can cause unsafe tool use or bad code changes.
- Key takeaways: proposal first, enablement later.

### Lesson 2: Eval-Before-Enable

- Prerequisites: understand proposal status.
- Explain: a skill must pass repeatable checks before it becomes trusted.
- Coding example: show `npm run test:skill-governance` or a fixture command recording pass/fail evidence.
- Theory Q/A: Why require repeated pass for flaky evals? Flaky behavior is not reliable enough for automation.
- Key takeaways: evidence beats intention.

### Lesson 3: Rollback And Disable

- Prerequisites: understand eval gates.
- Explain: every enabled skill needs a documented way to disable or revert it.
- Coding example: show metadata fields `enabledAt`, `enabledBy`, and `rollbackSteps`.
- Theory Q/A: Why write rollback before enabling? Incidents need clear steps under pressure.
- Key takeaways: governance includes exit paths.

### Lesson 4: Security Review

- Prerequisites: understand rollback.
- Explain: review checks for hidden escalation, destructive commands, secrets, and unsafe network use.
- Coding example: use `rg -n "rm |git reset|require_escalated|API_KEY|token" proposed-skill-path`.
- Theory Q/A: What if concern appears? Quarantine and block rather than partially trust.
- Key takeaways: generated automation is code with security impact.

## Memory Updates

Update `docs/memory/phases/SP-08/index.md` and codebase notes for skill proposal lifecycle, eval gate, and rollback path.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-08>`.
3. Run `git commit -m "SP-08: complete phase"`.
4. Run `git push`.

Commit only scoped SP-08 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-08-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
