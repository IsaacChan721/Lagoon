# Lagoon Prompt Packages

Use these packages to start each phase in a fresh convo with minimal context.

Memory-bank strategy lives at `docs/plans/memory-bank-strategy.md`.

## Workflow

1. Start a fresh phase convo.
2. Paste the next phase `package.md`.
3. Agent loads `package.md`, `plan.md`, memory index, and phase memory.
4. Agent executes only the current phase plan in `caveman full`, with temporary normal prose only for clarity or safety.
5. Agent writes `docs/run-logs/<PHASE>-output.md`.
6. Agent updates matching `docs/memory/` notes for changed folders/components.
7. Orchestrator reviews output, updates memory, and unlocks the next phase.

## What The LLM Does

The LLM acts as a narrow phase worker, not the whole project brain.

- It reads the phase contract from the package.
- It reads the phase execution plan from `plan.md`.
- It loads only the mandatory skills in that package.
- It uses `caveman full` by default for compact execution.
- It uses only the listed tools/plugins.
- It works inside the current phase's file scope.
- It writes the phase result into the matching output file.
- It updates `docs/memory/` so later agents can read concise notes instead of broad source.
- It reports summary, blockers, contract changes, skill changes, memory updates, tests, next gate, and whether the phase plan was followed or changed.

The main orchestration convo stays outside these packages and only handles:
- phase order
- contract updates
- cross-phase decisions
- skill map updates
- final review

## Package Structure

Each phase folder contains:

- `package.md`: paste-ready convo prompt
- `plan.md`: structured execution plan
- `output.md`: phase result template

Each phase also has memory:

- `docs/memory/phases/<phase-id>/index.md`
- matching codebase notes under `docs/memory/codebase/`

## Rules

- Keep one phase per convo.
- Do not mix later phases into the current package.
- Do not load all phase plans. Load only the current phase `plan.md`.
- Do not load optional skills until the trigger appears.
- Do not paste full docs or raw tool output into the prompt unless the package says to.
- If the phase needs a new contract, update the output file and return here before continuing.
- If code creates or changes a folder/component, update its memory mirror before closing the phase.
