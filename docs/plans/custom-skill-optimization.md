# Lagoon Custom Skill Optimization

## Purpose

Define how Lagoon-specific skills should be created later without bloating agent context.

## Create Only After Repetition

Create a custom skill only after the same workflow repeats at least twice in real implementation. Until then, keep guidance in phase docs.

## Skill Shape

Each Lagoon skill should have:

- `SKILL.md` under 150 lines when possible.
- Frontmatter with only `name` and `description`.
- A short workflow.
- Inputs needed.
- Done signal.
- "Load references only when..." section.
- No phase-specific status or historical chat content.

## Reference Split

Use one-level references:

```text
lagoon-rag-evals/
  SKILL.md
  references/
    retrieval-metrics.md
    citation-evals.md
  scripts/
    run_retrieval_eval.py
```

Do not nest references deeper than one level.

## Script Rule

Use scripts for deterministic, repeated, fragile workflows:

- eval metric calculation
- transcript chunk validation
- citation integrity checks
- key/vault smoke tests
- media fixture inspection

Scripts must:
- support dry-run where useful,
- avoid secrets in output,
- write only to explicit paths,
- have one smoke command in the skill.

## Trigger Design

Skill descriptions must be narrow:

- Good: "Use when implementing or verifying Lagoon transcript chunking, FFmpeg audio extraction, chunk retries, or transcript stitching."
- Bad: "Use for Lagoon."

## Context Hygiene

Never copy full phase plans into a skill. Skills are reusable procedure. Phase docs are project state.

If a skill starts needing more than 150 lines, move examples into references and list exact trigger conditions for reading each reference.

## Validation

Before activating a custom skill:

```powershell
$env:PYTHONUTF8='1'
uv run --with pyyaml python C:\Users\isaac\.codex\skills\.system\skill-creator\scripts\quick_validate.py <skill-folder>
```

Forward-test important skills with a fresh subagent using only:
- the skill path,
- one realistic task,
- minimal repo context.

## Proposed Custom Skills

| Skill | Create After | Mandatory References/Scripts |
|---|---|---|
| `lagoon-orchestrator` | `SP-00` and `SP-01` are stable | phase gate checklist |
| `lagoon-local-first-security` | vault/keychain exists | vault smoke script, log redaction checklist |
| `lagoon-media-pipeline` | first transcription pipeline works | FFmpeg chunk script, stitch validator |
| `lagoon-rag-evals` | first retrieval fixture exists | retrieval metrics script, citation evals |
| `lagoon-tutor-policy` | tutor grading traces exist | grading rubric refs, citation policy |
| `lagoon-skill-governance` | first proposal flow exists | proposal schema validator, eval-before-enable checklist |

