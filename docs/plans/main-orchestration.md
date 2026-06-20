# Lagoon Main Orchestration Plan

## Status

SA-00 has run far enough to unblock phase planning:
- Required installable skills are installed or explicitly skipped.
- Installed skills are validated.
- Phase-agent skill map is written in `docs/plans/phase-skill-map.md`.
- Security audit notes are written in `docs/plans/skill-acquisition-report.md`.

Remaining external action:
- Restart Codex or reload skills so newly installed global skills are discoverable by trigger metadata.

## Phase Order

1. `SA-00 Skill Acquisition`
2. `SP-00 Product, Risk, Repo`
3. `SP-01 Local App Foundation`
4. `SP-02 Lecture Media Import`
5. `SP-03 Media + Transcription`
6. `CRIT-01 Provenance Gate`
7. `SP-04 Video Understanding`
8. `SP-05 Local Memory + Retrieval`
9. `SP-06 Transcript-Grounded Summaries`
10. `SP-07 Tutor Practice`
11. `SP-08 Post-MVP Improvement Proposals`
12. `SP-09 Hardening + Packaging`
13. `SP-10 Deferred Cloud Sync Decision`

## Main Agent Responsibilities

- Maintain the canonical phase contract and data model.
- Dispatch one focused subagent per implementation task when work is independent.
- Prevent phase agents from mutating canonical lecture memory directly; require structured outputs, patches, or proposals.
- Keep every phase as an MVP slice: beginner-readable code/docs, no extra logic unless required by acceptance criteria, safety, or verification.
- Move marginal improvements to phase handoff next steps instead of adding complexity during the phase.
- Own user confirmations, security decisions, privacy gates, provider/API consent, and final promotion.
- Verify every phase with tests and UI/browser smoke checks where relevant.
- Require each phase to finish with its own `git add`, `git commit`, and `git push` after verification and handoff.
- Enforce the context budget in `docs/plans/context-and-skill-optimization.md`.

## Subagent Prompt Contract

Use this template for every phase implementer:

```text
Load only the mandatory SKILL.md files for this task:
<1-3 exact skill paths or plugin skill names>

Keep optional skills closed until a concrete need appears:
<optional skill names and trigger conditions>

Use only this assigned phase contract:
<phase summary and acceptance checklist>

Rules:
- Keep context under the phase budget.
- Write no broad refactors.
- Keep code beginner-readable. Add no marginal or speculative logic.
- Do not edit files outside assigned scope unless the main agent approves.
- Return changed files, tests run, risks, and open questions.
- Summarize large docs before using them; quote only small relevant parts.
- Escalate to stronger model only for architecture, security, or debugging blockers with evidence.
- After verification and handoff, run phase-scoped git add, git commit, and git push.
```

## Acceptance Gate

No phase may start until:
- its required skills are installed or explicitly skipped,
- `SKILL.md` files are validated or treated as external plugin skills,
- any third-party skill used by the phase has no unexpected scripts/tool escalation,
- the phase contract includes tests and done criteria,
- Codex restart/reload status is known,
- the current phase has a context budget and mandatory/optional skill split.

## Context Loading Policy

Default working set:
- `docs/plans/main-orchestration.md`
- `docs/plans/context-and-skill-optimization.md`
- `docs/memory/index.md`
- current phase memory note
- one phase contract
- only mandatory skills for the current task
- only file snippets needed for the current edit

Do not load all phase plans, all skills, or all API docs into one agent. Use retrieval by path, `rg`, and narrow file reads. If an agent needs more than one phase's context, stop and ask the main agent to provide a distilled interface summary instead of loading both phases wholesale.

## Memory Bank

Use `docs/memory/` as the durable project memory bank. It mirrors generated code with Markdown notes, so agents can understand folders/components without reading full source.

Every phase must:
- read `docs/memory/index.md` and its phase memory before broad source inspection,
- update `docs/memory/phases/<phase-id>/index.md`,
- update matching `docs/memory/codebase/` notes for generated or changed folders/components,
- report memory updates in its output file.

## Custom Lagoon Skills

Create these after the first implementation pass proves the patterns are stable:
- `lagoon-orchestrator`: phase gates, subagent contracts, promotion rules.
- `lagoon-local-first-security`: local-only boundaries, temp-file/log redaction, and no-upload checks.
- `lagoon-media-pipeline`: FFmpeg chunking, retries, transcript stitching.
- `lagoon-retrieval-evals`: simple retrieval metrics, citation checks, held-out fixtures.
- `lagoon-tutor-policy`: grading rules, selected-lecture boundary, no fake citations.
- `lagoon-improvement-governance`: proposal-only artifacts, eval-before-implementation, approval gates.

Do not create these prematurely. Each custom skill needs concrete examples from the real codebase, concise `SKILL.md`, and validation with `quick_validate.py`.

Follow `docs/plans/custom-skill-optimization.md` when creating or updating custom skills.
