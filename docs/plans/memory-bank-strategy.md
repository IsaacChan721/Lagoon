# Lagoon Memory Bank Strategy

## Decision

Use a repo-side, Obsidian-compatible Markdown vault at `docs/memory/`.

Do not depend on an Obsidian tool as the system of record. Obsidian can open and edit the vault because it is plain Markdown, but the repo remains canonical.

## Why This Works

Developers solving agent context problems generally converge on durable, searchable, file-based memory:

- Plain Markdown is diffable, reviewable, searchable with `rg`, and easy for agents to load selectively.
- Folder-level `index.md` files let agents read summaries before opening source.
- A codebase mirror avoids rereading implementation files when the agent only needs purpose, interfaces, and gotchas.
- A later retrieval layer can index the Markdown vault if `rg` is no longer enough.

## Source Notes

- Obsidian vaults are local folders of Markdown files, so this structure remains Obsidian-compatible: https://help.obsidian.md/vault
- Obsidian imports and stores Markdown files directly: https://obsidian.md/help/import/markdown
- File-based agent memory patterns use hierarchical files as persistent context: https://openagenthub.io/patterns/memory-context/file-based-memory/
- Agentic coding memory-bank workflows use Markdown memory as active project context: https://tweag.github.io/agentic-coding-handbook/WORKFLOW_MEMORY_BANK/
- Research on codebase memory suggests structure-aware retrieval can improve code agent performance; that is a later upgrade after Markdown memory exists: https://arxiv.org/abs/2603.27277

## Structure

```text
docs/memory/
  index.md
  phases/
    SP-01/index.md
  codebase/
    web/src/components/recorder-controls.md
    api/app/routes/lectures.md
  decisions/
    local-first-encryption.md
  templates/
    folder-index.md
    component-note.md
    decision-note.md
```

## Agent Workflow

1. Read `docs/memory/index.md`.
2. Read current phase memory.
3. Read relevant codebase mirror notes.
4. Read source only when memory is missing, stale, or too vague.
5. Update memory after changing code.
6. Report memory updates in phase output.

## Upgrade Path

Start:
- Markdown vault plus `rg`.

When vault becomes large:
- Add generated `docs/memory/search-index.json`.
- Add a tiny script to find notes by title, tags, code path, and phase.

When semantic search becomes needed:
- Add embeddings over `docs/memory/`, not over raw code first.
- Keep Markdown notes as source of truth.

## Guardrails

- Never paste full code into memory notes.
- Prefer links to real code paths.
- Keep notes short.
- Update memory in same phase that changes code.
- Mark stale notes rather than silently trusting them.

