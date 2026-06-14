# SP-01 Local App Foundation Lesson

## Purpose

Teach a beginner developer how the first Lagoon app slice fits together.

This lesson matches the current SP-01 code. It stays small on purpose: app shell, local settings, storage boundary, and one verification path.

## Sufficiency Review

The original SP-01 lesson plan is good enough for phase direction: it teaches repo shape, storage boundary, app shell, and verification in the right order.

This file adds what the plan was missing for beginners:

- exact files to open first,
- what each file owns,
- tiny code-reading exercises,
- commands to run,
- what not to build yet.

## Beginner Path

Read files in this order:

1. `web/src/app/privacyDefaults.ts`
2. `web/src/app/storageBoundary.ts`
3. `web/src/app/LagoonShell.tsx`
4. `api/lagoon_local/settings.py`
5. `api/lagoon_local/storage.py`
6. `scripts/verify_sp01_foundation.py`

Why this order: start with plain data, then UI, then local persistence, then verification.

## Lesson 1: Repo Shape

Lagoon starts with three working folders:

- `web/`: browser UI.
- `api/`: local data rules.
- `scripts/`: checks a developer can run.

Exercise:

```powershell
Get-ChildItem web,api,scripts
```

Question: which folder should own user-facing text? Answer: `web/`.

Question: which folder should own SQLite and vault rules? Answer: `api/`.

## Lesson 2: Privacy Defaults

Open `web/src/app/privacyDefaults.ts` and `api/lagoon_local/settings.py`.

Both say content network, provider calls, cloud sync, and telemetry are off by default.

Exercise:

```powershell
npm run verify:sp01
```

If a default changes in one place but not the other, the verifier should fail after it is extended for that new setting.

## Lesson 3: Local Storage Boundary

Open `api/lagoon_local/storage.py`.

Beginner mental model:

- metadata goes into SQLite,
- sensitive content belongs in the vault,
- vault writes are blocked until encryption exists.

Important method:

```python
LocalStorageBoundary.ensure_layout()
```

What it does:

- creates local folders,
- creates `metadata.sqlite3`,
- creates basic tables.

What it does not do:

- save raw lecture media,
- encrypt content,
- upload content.

## Lesson 4: App Shell

Open `web/src/app/LagoonShell.tsx`.

The component only displays current defaults. It does not create lectures, record media, call providers, or sync data.

Exercise:

```powershell
npm run dev:web
```

Open `http://127.0.0.1:5173`.

Check that the page shows:

- local workspace,
- vault locked,
- privacy defaults,
- upload blocked.

## Lesson 5: Verification

Run:

```powershell
npm run verify:sp01
npm run build:web
```

Use `verify:sp01` first because it checks the phase contract. Use `build:web` second because it checks TypeScript and bundling.

## Keep It Simple Rules

- Add one small thing at a time.
- Prefer plain constants before custom hooks/classes.
- Keep storage rules in `api/`.
- Keep display code in `web/`.
- Keep phase checks in `scripts/`.
- Move later ideas to run-log next steps instead of building them early.

## Stop Before These Features

Do not add these in SP-01:

- media capture,
- transcription,
- RAG,
- tutor logic,
- provider calls,
- accounts,
- cloud sync.

Those belong to later phases.

