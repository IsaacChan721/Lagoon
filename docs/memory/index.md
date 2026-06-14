# Lagoon Memory Vault

Purpose: keep durable, searchable Markdown memory for generated code, folders, components, contracts, and gotchas.

Use this vault before reading source broadly. Start here, then drill into phase or codebase notes.

## Sections

- `phases/`: phase-specific implementation memory.
- `codebase/`: Markdown mirror of generated code structure.
- `decisions/`: architecture and product decisions.
- `templates/`: reusable note templates.

## Agent Rule

Before touching code, read:

1. This file.
2. Current phase memory index.
3. Relevant `codebase/` mirror notes.

After changing code, update:

1. Current phase memory.
2. Codebase mirror notes for each new/changed folder or important component.
3. Decision note if contract or architecture changed.

Keep notes short. Capture purpose, public interfaces, dependencies, tests, and pitfalls. Do not paste full code.

