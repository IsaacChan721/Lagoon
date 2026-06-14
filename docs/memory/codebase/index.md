# Codebase Memory Mirror

This folder mirrors generated code folders with Markdown notes instead of code.

Example:

```text
web/src/components/RecorderControls.tsx
docs/memory/codebase/web/src/components/recorder-controls.md
```

## Mirror Rules

- Create one `index.md` per meaningful code folder.
- Create one note per important component, service, route, worker, schema, or script.
- Use kebab-case note names.
- Keep each note under 150 lines where possible.
- Link back to real code paths with absolute paths when known.
- Do not paste implementation code unless a tiny snippet is necessary.

## Note Contents

Each note should include:

- Purpose
- Owns
- Public interface
- Dependencies
- Data contracts
- Tests
- Gotchas
- Last updated by phase

