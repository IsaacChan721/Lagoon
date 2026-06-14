# SA-00 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Validate Lagoon skill readiness before project implementation starts.

## Inputs

- `docs/plans/phase-skill-map.md`
- `docs/plans/skill-acquisition-report.md`
- `docs/memory/index.md`
- `docs/memory/phases/SA-00/index.md`

## In Scope

- Confirm installed `SKILL.md` paths.
- Validate required skills where validation scripts exist.
- Quarantine or reject untrusted skills.
- Update skill map findings.

## Out Of Scope

- No app scaffolding.
- No feature implementation.
- No unvetted third-party skill install.

## Execution Steps

1. Read package, phase memory, and skill acquisition report.
2. Inspect required skill paths.
3. Validate trusted skills with available validation scripts.
4. Record unavailable, skipped, quarantined, or caveated skills.
5. Update phase skill map only if current facts differ.
6. Stop at readiness report.

## Acceptance Criteria

- Every required skill is marked installed, skipped, unavailable, or quarantined.
- Untrusted skills are not enabled.
- Skill map reflects current usable skill set.
- Next phase knows exact blockers, if any.

## Definition Of Done

- Skill readiness is documented.
- No project source implementation happened.
- Memory note records decisions and blockers.
- Handoff output is written.

## Verification

- Run `rg -n "SKILL.md|quarantine|unavailable|validated" docs/plans docs/memory`.
- Run `git status --short`.

## Troubleshooting

- If validation fails, inspect `SKILL.md` frontmatter first.
- If install path is missing, mark skill unavailable instead of inventing replacement.
- If network blocks validation, record blocker and continue with local evidence.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite context first, then build toward exact files and commands.

### Created In This Phase

- Skill readiness notes in `docs/memory/phases/SA-00/index.md`.
- Any corrected skill availability facts in `docs/plans/phase-skill-map.md`.
- Handoff report in `docs/run-logs/SA-00-output.md`.

### Lesson 1: What A Codex Skill Is

- Prerequisites: none.
- Explain: a skill is a local `SKILL.md` instruction file Codex reads when task matches its description.
- Coding example: run `rg -n "name:|description:" C:\Users\isaac\.codex\skills -g SKILL.md` and explain how frontmatter identifies a skill.
- Theory Q/A: Why validate skills before coding? Broken or untrusted instructions can make later phase work unsafe or inconsistent.
- Key takeaways: skills are project tooling, not app runtime code; readiness must be explicit before implementation starts.

### Lesson 2: Skill Safety And Trust

- Prerequisites: understand Lesson 1.
- Explain: unavailable, skipped, validated, and quarantined states.
- Coding example: show how a missing path becomes an `unavailable` note instead of a guessed replacement.
- Theory Q/A: Why quarantine instead of delete? Quarantine preserves evidence while preventing unsafe use.
- Key takeaways: never enable untrusted automation silently; document every blocker for next phase.

### Lesson 3: Reading The Phase Output

- Prerequisites: understand skill states.
- Explain: how `SA-00-output.md` tells `SP-00` which workflows are usable.
- Coding example: use `rg -n "validated|quarantined|unavailable" docs` to trace a skill decision from report to memory.
- Theory Q/A: What should a beginner check first? Whether required skills are usable and whether any caveat changes the next phase.
- Key takeaways: phase memory is the learning map; output file is the handoff snapshot.

## Memory Updates

Update `docs/memory/phases/SA-00/index.md` with installed skills, skipped skills, caveats, and next gate.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SA-00>`.
3. Run `git commit -m "SA-00: complete phase"`.
4. Run `git push`.

Commit only scoped SA-00 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SA-00-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
