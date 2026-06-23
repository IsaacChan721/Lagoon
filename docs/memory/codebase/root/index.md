# Repo Root

## Purpose

Owns workspace scripts, dependency lock, git ignore policy, and package workspace boundary.

## Contains

- `package.json` root scripts and web workspace declaration.
- `package-lock.json` npm dependency lock.
- `.gitignore` local-first exclusion rules.
- `docs/lessons/` beginner learning material.
- `AGENTS.md` project instructions, including Markdown presentation requirements.

## Key Files

- `package.json`
- `package-lock.json`
- `.gitignore`
- `AGENTS.md`

## Interfaces

- `npm run verify:sp01`
- `npm run verify:sp02`
- `npm run test`
- `npm run dev:web`
- `npm run build:web`
- `npm audit`

## Dependencies

- npm workspace: `web`
- PowerShell for verification wrapper on Windows.

## Tests

- `npm run verify:sp01`
- `npm run verify:sp02`
- `npm run build:web`
- `npm audit`

## Gotchas

- Local content/data folders are ignored to prevent accidental raw lecture data commits.
- Raw media extensions remain ignored for imported lecture media.
- `python` is not on PATH here; verification wrapper falls back to Codex bundled Python.
- `*.tsbuildinfo` is ignored because TypeScript build info is generated.
- npm audit is clean after moving build tools to dev dependencies and updating Vite.
- New or updated Markdown should follow `docs/plans/markdown-presentation-rules.md`.

## Last Updated

Markdown presentation standard added after SP-02
