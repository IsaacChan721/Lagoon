# docs/run-logs

## Purpose

Store phase-agent outputs for Lagoon orchestration review and phase handoff.

## Contains

- One Markdown output file per phase or critical gate.
- Current file: `SP-00-output.md`.

## Key Files

- `docs/run-logs/SP-00-output.md`: Product/risk/repo scope handoff for `SP-00`.

## Interfaces

- Phase agents write summary, blockers, contract changes, skill changes, memory updates, phase status, tests, and next gate.
- Main orchestrator reads outputs to unlock or revise next phase.

## Dependencies

- `docs/prompt-packages/<phase>/package.md`
- `docs/prompt-packages/<phase>/plan.md`
- `docs/memory/phases/<phase>/index.md`

## Tests

- `rg -n "MVP|local-first|gate|SP-01|threat" docs/plans docs/memory`
- `git status --short`

## Gotchas

- Run logs are handoff artifacts, not canonical implementation source.
- If output changes contract, main orchestrator must approve before next phase.

## Last Updated

`SP-00`
