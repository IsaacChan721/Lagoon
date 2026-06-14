# Lagoon Context and Skill Optimization

## Goal

Keep Lagoon agents effective by minimizing irrelevant context, loading skills progressively, and splitting work across focused subagents.

## External Best Practices Used

- Anthropic's context engineering guidance warns that long context windows still suffer from context pollution and relevance problems, and recommends shaping context deliberately for each agent task: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic's tool-writing guidance recommends context-efficient tools that return relevant subsets instead of dumping full datasets into the model: https://www.anthropic.com/engineering/writing-tools-for-agents
- OpenAI prompt guidance recommends placing instructions first and clearly separating instructions from context: https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api
- GitHub/Microsoft Copilot customization guidance treats custom instructions and skills as targeted context, not a place to dump every project detail: https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses

## Context Budget

Use these maximum working sets unless the main agent approves an exception:

| Agent Type | Max Skills Loaded | Max Repo Docs Loaded | Max Source Files Loaded | Notes |
|---|---:|---:|---:|---|
| Main orchestrator | 2 | 3 | 0-2 | Registry, current phase gate, risks only |
| Phase implementer | 1-3 | 1-2 | 3-6 | Current phase only |
| Reviewer | 1-2 | 1 | diff + touched files | No unrelated docs |
| Debugger | 1-2 | 1 | failing path only | Logs/test output first |
| Security critic | 2-3 | 2 | trust-boundary files | Security docs allowed |
| UI verifier | 1-2 | 1 | UI files only | Browser state over source dump |

## Memory Bank Policy

Use `docs/memory/` as repo-side, Obsidian-compatible memory. It is the durable context layer for agents and humans.

Read order:

1. `docs/memory/index.md`
2. Current phase memory at `docs/memory/phases/<phase-id>/index.md`
3. Relevant codebase mirror notes under `docs/memory/codebase/`
4. Source files only after memory notes point to them or prove stale

Update rule:

- Every generated or meaningfully changed folder gets an `index.md` mirror under `docs/memory/codebase/`.
- Every important component, route, service, schema, worker, script, or evaluator gets a short `.md` note.
- Phase agents must report memory updates in their output file.
- Notes explain purpose, interfaces, dependencies, tests, and gotchas; they do not paste full code.

## Skill Loading Policy

Classify skills per task:

- **Mandatory:** required before action; load at start.
- **Conditional:** load only after trigger appears.
- **Reference-only:** do not load; main agent has already summarized needed rule.
- **Forbidden:** do not load/use in this phase.

Examples:
- `security-best-practices` is mandatory for threat model/security work, conditional for normal feature coding.
- `openai-docs` is conditional until a concrete OpenAI API/model decision appears.
- `web-design-guidelines` is conditional until UI review/audit begins because it fetches live external guidance.
- `speech` and `transcribe` are conditional because they require network/API-key handling for live use.

## Phase Prompt Shape

Use this structure for every phase subagent:

```text
Instructions:
- You are the <phase/task> agent.
- Load mandatory skills only: <skills>.
- Keep optional skills closed unless trigger appears: <conditions>.
- Do not inspect unrelated phases.
- Return summary, changed files, tests, risks, next gate.

Context:
- Phase contract: <200-500 word distilled contract>.
- Interfaces needed: <types/API names>.
- Files in scope: <paths>.
- Acceptance checklist: <short checklist>.
```

## Skill Optimization Rules

1. Prefer small, trigger-specific skills over broad always-on instructions.
2. Keep custom Lagoon `SKILL.md` under 150 lines when possible.
3. Move long examples, schemas, and command recipes into `references/` files and load them only by trigger.
4. Put deterministic fragile workflows into scripts, not prose.
5. Avoid duplicating project plans inside skills; skills should describe reusable procedure, not current phase state.
6. Add an "Inputs needed" and "Done signal" section to every custom Lagoon skill.
7. Validate each custom skill with `quick_validate.py`.
8. Forward-test complex custom skills with a fresh subagent using minimal context.

## Context Overflow Triggers

Stop and compress when any is true:
- More than 3 skills are open.
- More than 6 source files are open.
- Agent needs two unrelated phases.
- Tool output exceeds what is needed to answer next decision.
- Same API docs are reloaded repeatedly.
- Prompt contains historical chat details instead of current contract.

Compression action:
- Write/update a short phase note in `docs/memory/` or `docs/plans/`.
- Replace raw output with a 5-10 bullet interface summary.
- Continue with only current task, touched files, and acceptance checklist.

## Tool Output Policy

- Use `rg` and targeted reads before broad file dumps.
- Prefer exact test failures, line references, and small snippets.
- Browser agents should use DOM snapshots/screenshots as evidence, not entire app source.
- OpenAI/Supabase docs lookups must answer one concrete API question at a time.
- Do not paste full docs into prompts; cite URL and keep distilled rule.

## Model Routing

- Use mini model for narrow code, docs, fixtures, and simple tests.
- Use standard model for multi-file integration and debugging.
- Use strongest model for architecture, security, data model, tutor/rubric policy, and failed debug escalation.
- Downshift after blocker resolved.

## Custom Lagoon Skill Timing

Do not create custom Lagoon skills before there is real code and repeated behavior. Create after first stable implementation pattern:

- `lagoon-orchestrator`: after `SP-00` and `SP-01`.
- `lagoon-local-first-security`: after vault/keychain works.
- `lagoon-media-pipeline`: after first transcription pipeline works.
- `lagoon-rag-evals`: after first retrieval eval fixture exists.
- `lagoon-tutor-policy`: after tutor loop has working grading traces.
- `lagoon-skill-governance`: after first real proposal/eval/approval flow.
