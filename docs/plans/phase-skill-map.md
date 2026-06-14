# Lagoon Phase Skill Map

Every phase implementer prompt must include:

1. Load mandatory `SKILL.md` files first.
2. Use only your assigned phase contract.
3. Write no broad refactors.
4. Return changed files, tests run, risks, and open questions.
5. Escalate to stronger model only for architecture, security, or debugging blockers with evidence.
6. Keep optional skills closed until their trigger appears.

## Installed Global Skill Paths

New skills:
- `C:\Users\isaac\.codex\skills\speech\SKILL.md`
- `C:\Users\isaac\.codex\skills\transcribe\SKILL.md`
- `C:\Users\isaac\.codex\skills\react-best-practices\SKILL.md`
- `C:\Users\isaac\.codex\skills\web-design-guidelines\SKILL.md`
- `C:\Users\isaac\.codex\skills\composition-patterns\SKILL.md`

Existing relevant skills:
- `C:\Users\isaac\.codex\skills\caveman\SKILL.md`
- `C:\Users\isaac\.codex\skills\.system\skill-installer\SKILL.md`
- `C:\Users\isaac\.codex\skills\.system\skill-creator\SKILL.md`
- `C:\Users\isaac\.codex\skills\.system\openai-docs\SKILL.md`
- `C:\Users\isaac\.codex\skills\security-threat-model\SKILL.md`
- `C:\Users\isaac\.codex\skills\security-best-practices\SKILL.md`
- `C:\Users\isaac\.codex\skills\playwright\SKILL.md`
- `C:\Users\isaac\.codex\skills\playwright-interactive\SKILL.md`
- `C:\Users\isaac\.codex\skills\screenshot\SKILL.md`
- `C:\Users\isaac\.codex\skills\sentry\SKILL.md`
- `C:\Users\isaac\.codex\skills\jupyter-notebook\SKILL.md`

Plugin skills to reference by name when available:
- `Browser:browser`
- `OpenAI Developers:agents-sdk`
- `OpenAI Developers:openai-api-troubleshooting`
- `Supabase:supabase`
- `Supabase:supabase-postgres-best-practices`
- `Superpowers:brainstorming`
- `Superpowers:writing-plans`
- `Superpowers:subagent-driven-development`
- `Superpowers:test-driven-development`
- `Superpowers:systematic-debugging`
- `Superpowers:verification-before-completion`

## Phase Allocation

Each row splits **mandatory** skills from **conditional** skills. Mandatory skills load at task start. Conditional skills load only when the trigger appears.

| Phase Agent | Mandatory Skills | Conditional Skills |
|---|---|---|
| `SA-00 Skill Acquisition` | `skill-installer`, `skill-creator` | `security-threat-model`, `security-best-practices` for third-party audit |
| `SP-00 Product/Risk/Repo` | `caveman`, `Superpowers:brainstorming`, `Superpowers:writing-plans` | `security-threat-model` for threat model, `security-best-practices` for security defaults, `openai-docs` for provider decisions |
| `SP-01 Local App Foundation` | `Superpowers:test-driven-development`, `react-best-practices`, `composition-patterns` | `web-design-guidelines` for UI audit, `Browser:browser`/`playwright` for local verification, `security-best-practices` for FastAPI/React security |
| `SP-02 Video + Audio Capture` | `Superpowers:test-driven-development`, `Superpowers:systematic-debugging`, `Browser:browser` | `playwright` for scripted E2E, `screenshot` for visual capture issues, `web-design-guidelines` for UI review |
| `SP-03 Media + Transcription` | `transcribe`, `Superpowers:test-driven-development`, `Superpowers:systematic-debugging` | `openai-docs` for API/model details, `OpenAI Developers:openai-api-troubleshooting` for API failures, `Superpowers:verification-before-completion` before gate |
| `CRIT-01 Provenance Gate` | `security-threat-model`, `Superpowers:test-driven-development` | `security-best-practices` for implementation review, `Superpowers:verification-before-completion` before gate |
| `SP-04 Video Understanding` | `Superpowers:systematic-debugging`, `playwright` | `openai-docs` for vision API decisions, `imagegen` only for generated visual fixtures, `screenshot` for frame/OCR QA |
| `SP-05 Memory + RAG` | `openai-docs`, `Superpowers:test-driven-development` | `security-best-practices` for encrypted storage review, `jupyter-notebook` for eval experiments, `Superpowers:verification-before-completion` before gate |
| `SP-06 Summaries + Sources` | `openai-docs`, `Superpowers:systematic-debugging` | `Browser:browser` for source/UI checks, `security-best-practices` for web/source trust, `Superpowers:verification-before-completion` before gate |
| `SP-07 Tutor Agent` | `openai-docs`, `Superpowers:test-driven-development` | `OpenAI Developers:agents-sdk` only for architecture comparison, `OpenAI Developers:openai-api-troubleshooting` for API failures, `speech` only for spoken tutor output |
| `SP-08 Gated Improvement` | `skill-creator`, `security-threat-model`, `Superpowers:verification-before-completion` | `security-best-practices` for proposal sandboxing, `Superpowers:subagent-driven-development` during execution |
| `SP-09 Hardening + Packaging` | `playwright`, `Superpowers:verification-before-completion` | `Browser:browser` for manual smoke, `sentry` for production error review, `security-best-practices` for release audit, `web-design-guidelines` for UI audit |
| `SP-10 Optional Cloud Sync` | `Supabase:supabase`, `security-threat-model` | `Supabase:supabase-postgres-best-practices` for schema/RLS, `security-best-practices` for crypto/auth review, `Superpowers:verification-before-completion` before gate |

## Model Routing

- `gpt-5.5`: main orchestrator, security critic, tutor policy, skill governance, final review.
- `gpt-5.4`: integration agents touching several modules.
- `gpt-5.4-mini`: scaffolding, focused tests, UI components, docs, mechanical fixes.
- Escalate only after a subagent reports a concrete blocker, failing test, or ambiguous security decision.

## Context Budget

Follow `docs/plans/context-and-skill-optimization.md`. Default: 1-3 loaded skills per phase agent, 1-2 repo docs, and only touched source files.
