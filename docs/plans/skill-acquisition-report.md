# SA-00 Skill Acquisition Report

Date: 2026-05-24

## Result

SA-00 installed and validated the vetted global skills needed before Lagoon phase work starts.

Installed:
- `speech` from `openai/skills`
- `transcribe` from `openai/skills`
- `react-best-practices` from `vercel-labs/agent-skills`
- `web-design-guidelines` from `vercel-labs/agent-skills`
- `composition-patterns` from `vercel-labs/agent-skills`

Skipped:
- `frontend-skill`: not present in the current `openai/skills` `main` branch during install. Use `react-best-practices`, `web-design-guidelines`, and `composition-patterns` as the frontend skill set until an official replacement exists.

Added replacement:
- `transcribe`: official OpenAI curated skill, directly useful for Lagoon media/transcription phases.

## Validation

Validated with the official `skill-creator` `quick_validate.py` script:
- `speech`: valid
- `transcribe`: valid
- `react-best-practices`: valid
- `web-design-guidelines`: valid
- `composition-patterns`: valid after rerunning validator with `PYTHONUTF8=1`

Validation command pattern:

```powershell
$env:PYTHONUTF8='1'
$env:UV_CACHE_DIR='C:\Users\isaac\Documents\Projects\Lagoon\.uv-cache'
uv run --with pyyaml python C:\Users\isaac\.codex\skills\.system\skill-creator\scripts\quick_validate.py <skill-folder>
```

## Security Audit Notes

Security scan checked installed skill folders for risky strings including shell execution, destructive commands, secrets, token handling, and arbitrary eval/exec.

Independent audit verdicts:

| Skill | Verdict | Notes |
|---|---|---|
| `speech` | Approved with caveats | OpenAI SDK wrapper only; no shell-outs or destructive ops. Requires `OPENAI_API_KEY` and network. Its `references/codex-network.md` mentions lowering sandbox approvals, so do not follow that guidance without explicit main-agent/user approval. |
| `transcribe` | Approved with caveats | OpenAI SDK wrapper only; no suspicious install artifact or command execution. Requires `OPENAI_API_KEY` and network. |
| `react-best-practices` | Approved | Documentation/rules only. No scripts, key handling, install hooks, or destructive commands. |
| `web-design-guidelines` | Approved with caveats | Documentation only, but instructs agents to fetch latest guidelines from GitHub Raw, so reviews are network-dependent. |
| `composition-patterns` | Approved | Documentation/rules/metadata only. No runtime code, hidden tooling, or key/network requirement beyond ordinary references. |

Operational guardrails:
- Run `speech` and `transcribe` only after OpenAI key setup is complete.
- Prefer dry-run or fixture-driven tests before live API calls.
- Never allow a downloaded skill to grant itself permission to write outside its assigned phase.
- Third-party skills remain guidance only unless a phase plan explicitly grants a tool/action.

## Restart Requirement

Codex must be restarted or have skills reloaded before newly installed global skills appear in the automatic skill list. Until then, agents can still be explicitly pointed at the installed `SKILL.md` paths.
