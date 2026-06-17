# SP-01 Local App Foundation Lesson

## Purpose

Teach a beginner developer how the first Lagoon app slice fits together, how to read the current code, and how to make safe small changes without accidentally building later-phase features.

This lesson matches the current SP-01 code. It is intentionally local-first and MVP-sized: app shell, privacy defaults, local storage boundary, SQLite metadata, and one verification path.

## Sufficiency Review

The original SP-01 lesson plan was directionally correct, but too short for the current learning goal. It named the right topics, but did not give enough code reading, hands-on practice, debugging practice, or beginner checkpoints.

This expanded lesson fixes that by adding:

- exact files to open,
- line-by-line and block-by-block code tours,
- hands-on commands with expected results,
- debugging drills,
- theory Q/A sections,
- checkpoints and acceptance criteria,
- explicit MVP stop points.

Important alignment note: SP-01 uses a vault/write-blocking placeholder as a safety boundary. That does not mean encryption is required before MVP media features. Later MVP phases should use local-only artifact references unless a separate hardening plan approves encryption.

## Beginner Path

Read files in this order:

1. `web/src/app/privacyDefaults.ts`
2. `web/src/app/storageBoundary.ts`
3. `web/src/app/LagoonShell.tsx`
4. `api/lagoon_local/settings.py`
5. `api/lagoon_local/storage.py`
6. `scripts/verify_sp01_foundation.py`
7. `package.json`

Why this order: start with plain frontend data, then UI display, then backend equivalents, then storage setup, then verification commands.

## Time Plan

This is not a one-minute skim. Treat each lesson as a 60-90 minute beginner module.

- Lesson 1: Repo shape and ownership.
- Lesson 2: Privacy defaults across frontend and backend.
- Lesson 3: Local storage boundary and SQLite metadata.
- Lesson 4: App shell code tour.
- Lesson 5: Verification and safe change workflow.

## Lesson 1: Repo Shape And Ownership

### Goal

Understand what each top-level folder owns before editing code.

### Prerequisites

None. This lesson assumes the learner has only basic command-line familiarity.

### Files And Folders

- `web/`: browser UI. Owns visible text, React components, frontend constants, Vite build.
- `api/`: local Python package. Owns local privacy defaults, storage path rules, SQLite metadata setup.
- `scripts/`: project checks. Owns repeatable verification commands.
- `docs/`: plans, memory, lessons, run logs. Owns explanation and phase handoff.
- `package.json`: root command menu. Owns scripts such as `verify:sp01` and `build:web`.

### Hands-On Setup

Run:

```powershell
Get-ChildItem web,api,scripts,docs
Get-Content package.json
```

Expected result:

- You should see `web`, `api`, `scripts`, and `docs`.
- In `package.json`, you should see commands for SP-01 verification and web build.

If `Get-ChildItem` fails, check that your terminal is in:

```powershell
C:\Users\isaac\Documents\Projects\Lagoon
```

### Code Reading

Open `package.json` and find the scripts section. Read it like a command menu:

```json
"scripts": {
  "verify:sp01": "...",
  "build:web": "..."
}
```

Line-by-line meaning:

- `"scripts"`: named commands npm can run.
- `"verify:sp01"`: the narrow phase check. Use this first when SP-01 behavior changes.
- `"build:web"`: the frontend build check. Use this after the narrow check.

### Design Rule

Before editing, ask: which folder owns this change?

- User-facing copy? `web/`.
- Local storage schema? `api/`.
- Verification rule? `scripts/`.
- Lesson or phase explanation? `docs/`.

### Debugging Drill

Problem: a developer adds SQLite setup inside a React component.

Diagnosis:

- React runs in the browser.
- SQLite setup belongs to local backend/storage code.
- The change mixes UI and persistence ownership.

Fix:

- Move SQLite setup to `api/lagoon_local/storage.py`.
- Keep React focused on displaying status and controls.

### Theory Q/A

1. Q: Why separate `web/` and `api/`?
   A: UI and local data rules change for different reasons. Separate folders make each responsibility easier to test.

2. Q: Why keep `docs/` separate from runtime code?
   A: Docs explain decisions and lessons without becoming app logic.

3. Q: Why have `scripts/`?
   A: Scripts give repeatable checks so the next developer can verify the same contract.

4. Q: Why avoid broad refactors in SP-01?
   A: SP-01 proves the foundation. Broad refactors make it harder to know what broke.

5. Q: What is the main beginner mistake here?
   A: Putting logic in the first file that is easy to edit instead of the file that owns that responsibility.

### Checkpoint

Task: write down which folder should own each change:

- Add a new privacy row to the UI.
- Add a new SQLite metadata table.
- Add a new verification rule.
- Add a new lesson note.

Acceptance criteria:

- UI row -> `web/`.
- SQLite table -> `api/`.
- Verification rule -> `scripts/`.
- Lesson note -> `docs/`.

### Key Takeaways

- Folder ownership comes before code changes.
- SP-01 is a foundation phase, not a feature phase.
- Small scoped changes are easier to verify.

## Lesson 2: Privacy Defaults Across Frontend And Backend

### Goal

Understand how Lagoon expresses local-first defaults in both TypeScript and Python.

### Prerequisites

Know the repo folders from Lesson 1. Basic boolean knowledge helps: `true` means enabled, `false` means disabled.

### Files

- `web/src/app/privacyDefaults.ts`
- `api/lagoon_local/settings.py`
- `web/src/app/LagoonShell.tsx`
- `scripts/verify_sp01_foundation.py`

### Zero-Prerequisite Terms

- Privacy default: what the app does before the user changes settings.
- Local-only: lecture content stays on the device by default.
- Provider call: request to an external AI/API service.
- Telemetry: app usage/error data sent outside the device.
- Log redaction: removing sensitive details from logs.

### Code Reading: Frontend Defaults

Open `web/src/app/privacyDefaults.ts`:

```ts
export type PrivacyDefaults = {
  localOnly: boolean;
  networkEnabledForContent: boolean;
  providerCallsEnabled: boolean;
  cloudSyncEnabled: boolean;
  telemetryEnabled: boolean;
  redactLogs: boolean;
};
```

Block-by-block meaning:

- `export type PrivacyDefaults`: defines the shape of the object other files may import.
- `localOnly`: should be `true` for MVP.
- `networkEnabledForContent`: should be `false`; lecture content should not use network by default.
- `providerCallsEnabled`: should be `false`; no AI/provider call by default.
- `cloudSyncEnabled`: should be `false`; no cloud sync in MVP.
- `telemetryEnabled`: should be `false`; no usage reporting by default.
- `redactLogs`: should be `true`; logs should avoid sensitive content.

Now read:

```ts
export const privacyDefaults: PrivacyDefaults = {
  localOnly: true,
  networkEnabledForContent: false,
  providerCallsEnabled: false,
  cloudSyncEnabled: false,
  telemetryEnabled: false,
  redactLogs: true,
};
```

Each value is part of the MVP contract. If a beginner changes one of these, they are changing product behavior, not just code style.

### Code Reading: Backend Defaults

Open `api/lagoon_local/settings.py`:

```python
@dataclass(frozen=True)
class PrivacySettings:
    local_only: bool = True
    network_enabled_for_content: bool = False
    provider_calls_enabled: bool = False
    cloud_sync_enabled: bool = False
    telemetry_enabled: bool = False
    redact_logs: bool = True
```

Line-by-line meaning:

- `@dataclass(frozen=True)`: Python creates a simple immutable settings object.
- `local_only: bool = True`: default local-only behavior.
- `network_enabled_for_content: bool = False`: no content network by default.
- `provider_calls_enabled: bool = False`: no external providers by default.
- `cloud_sync_enabled: bool = False`: no cloud sync by default.
- `telemetry_enabled: bool = False`: no telemetry by default.
- `redact_logs: bool = True`: logs should redact sensitive data.

Then:

```python
def to_metadata(self) -> dict[str, bool]:
    return asdict(self)
```

Meaning:

- Converts the settings object into a dictionary.
- Storage code can then insert each setting into SQLite metadata.

### Hands-On Exercise

Run:

```powershell
npm run verify:sp01
```

Expected result:

- Verification passes.
- If it fails, read the first failure message before changing code.

Optional safe experiment:

1. Temporarily change `telemetryEnabled` in `web/src/app/privacyDefaults.ts` from `false` to `true`.
2. Run `npm run verify:sp01`.
3. Observe whether the verifier catches it.
4. Change it back to `false`.

Do not leave the setting changed.

### Debugging Drill

Problem: the UI shows `Cloud sync On`.

Reasoning path:

1. UI reads `privacyDefaults.cloudSyncEnabled`.
2. `cloudSyncEnabled` should be `false`.
3. If it is `true`, the frontend default is wrong.
4. If frontend is false but UI still says On, inspect `LagoonShell.tsx` mapping logic.

Fix:

- Restore `cloudSyncEnabled: false`.
- Re-run `npm run verify:sp01`.

### Theory Q/A

1. Q: Why define privacy defaults twice, frontend and backend?
   A: Frontend displays user-facing state; backend persists local metadata. SP-01 keeps them explicit until shared schema generation exists.

2. Q: Why is `cloudSyncEnabled` false?
   A: Cloud sync is outside MVP and creates auth, storage, privacy, and conflict complexity.

3. Q: Why is `providerCallsEnabled` false?
   A: External calls should require explicit feature-level consent.

4. Q: Why is `redactLogs` true?
   A: Lecture content can be sensitive, so logs should not expose raw content.

5. Q: Why not add a settings UI yet?
   A: SP-01 only displays defaults. Editing settings belongs to a later feature slice.

### Checkpoint

Task: explain why these defaults are safe:

- `localOnly: true`
- `networkEnabledForContent: false`
- `cloudSyncEnabled: false`
- `redactLogs: true`

Acceptance criteria:

- Answer mentions local-first MVP.
- Answer mentions no default upload.
- Answer mentions sensitive lecture data.

### Key Takeaways

- Privacy defaults are product decisions.
- Frontend and backend must stay conceptually aligned.
- No cloud sync, provider calls, telemetry, or content network by default.

## Lesson 3: Local Storage Boundary And SQLite Metadata

### Goal

Understand how SP-01 creates local folders and metadata without implementing later media storage.

### Prerequisites

Know privacy defaults from Lesson 2. Basic understanding of folders and database tables helps.

### Files

- `api/lagoon_local/storage.py`
- `api/lagoon_local/settings.py`
- `docs/memory/codebase/api/lagoon_local/storage.md`

### Zero-Prerequisite Terms

- Storage boundary: the code that decides where local app data lives.
- SQLite: a small local database stored in one file.
- Metadata: information about content, not the full content itself.
- App data path: OS-specific folder for local application data.
- Safety placeholder: code that blocks risky behavior until a later phase designs it.

### Code Reading: Constants And Error

Open `api/lagoon_local/storage.py`:

```python
SCHEMA_VERSION: Final[int] = 1
```

Meaning:

- Current metadata schema version is `1`.
- Later schema changes can increment this.

```python
class EncryptionNotConfiguredError(RuntimeError):
    """Raised when content write is attempted before vault encryption exists."""
```

Beginner interpretation:

- This error blocks raw content writes in SP-01.
- It is a safety placeholder from the first foundation slice.
- It does not mean encryption is required before MVP capture/retrieval. Current alignment says later MVP phases should use local-only artifact references first.

### Code Reading: Data Layout

```python
@dataclass(frozen=True)
class StorageLayout:
    root: Path
    metadata_db: Path
    vault_dir: Path
    temp_dir: Path
    logs_dir: Path
```

Line-by-line meaning:

- `root`: main Lagoon local data folder.
- `metadata_db`: SQLite database path.
- `vault_dir`: placeholder folder for future content/artifact storage.
- `temp_dir`: temporary files.
- `logs_dir`: logs.

### Code Reading: Default Data Root

```python
def default_data_root() -> Path:
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
        return Path(base) / "Lagoon"
```

Meaning:

- On Windows, use `%LOCALAPPDATA%\Lagoon` when possible.
- This keeps app data outside the Git repo.

```python
    xdg_data_home = os.environ.get("XDG_DATA_HOME")
    if xdg_data_home:
        return Path(xdg_data_home) / "lagoon"

    return Path.home() / ".local" / "share" / "lagoon"
```

Meaning:

- On Linux-like systems, use XDG app data path if available.
- Otherwise, use a conventional home-folder app data path.

### Code Reading: Ensuring Layout

```python
def ensure_layout(self) -> StorageLayout:
    layout = StorageLayout(
        root=self.root,
        metadata_db=self.root / "metadata.sqlite3",
        vault_dir=self.root / "vault",
        temp_dir=self.root / "tmp",
        logs_dir=self.root / "logs",
    )
```

Meaning:

- Builds all important paths from one root.
- Does not create files yet; it describes where they should be.

```python
layout.vault_dir.mkdir(parents=True, exist_ok=True)
layout.temp_dir.mkdir(parents=True, exist_ok=True)
layout.logs_dir.mkdir(parents=True, exist_ok=True)
self._ensure_metadata(layout.metadata_db)
return layout
```

Meaning:

- Creates folders if missing.
- Creates/updates metadata database.
- Returns the final layout object.

### Code Reading: SQLite Tables

Inside `_ensure_metadata`, read each `create table` block:

- `app_settings`: stores settings like `schema_version`, `local_only`, `cloud_sync_enabled`.
- `lecture_workspaces`: future workspace metadata, not full lecture media.
- `vault_objects`: placeholder metadata for future artifacts.

Important: SP-01 does not save raw lecture media, transcript text, or embeddings.

### Hands-On Exercise

Run:

```powershell
npm run verify:sp01
```

Then inspect storage code:

```powershell
Select-String -Path api\lagoon_local\storage.py -Pattern "create table|app_settings|lecture_workspaces|vault_objects"
```

Expected result:

- You should see all three table names.
- You should see `create table if not exists`.

### Debugging Drill

Problem: Windows test fails because SQLite database file is locked.

Reasoning path:

1. SQLite connections can keep files open.
2. `storage.py` uses `conn = sqlite3.connect(...)`.
3. The `finally: conn.close()` block releases the connection.
4. If someone removes `conn.close()`, Windows file locks can persist.

Fix:

- Restore `finally: conn.close()`.
- Re-run `npm run verify:sp01`.

### Theory Q/A

1. Q: Why put metadata in SQLite?
   A: SQLite is local, simple, and enough for MVP metadata.

2. Q: Why keep app data outside the repo?
   A: Raw lecture data should not be committed to Git.

3. Q: Why block `write_content_blob` in SP-01?
   A: SP-01 proves the boundary before later phases decide exact artifact-writing behavior.

4. Q: Does SP-01 require encryption before MVP capture?
   A: No. Current phase alignment says encryption is a later hardening option, not an MVP blocker.

5. Q: Why create tables before using them?
   A: Verification can prove the foundation exists before features depend on it.

### Checkpoint

Task: explain what `ensure_layout()` does and does not do.

Acceptance criteria:

- Mentions folder creation.
- Mentions SQLite metadata setup.
- Says it does not upload content.
- Says it does not implement media capture.
- Says raw content writes remain blocked in SP-01.

### Key Takeaways

- SP-01 owns metadata foundation, not full content storage.
- Local data paths keep sensitive content out of the repo.
- The write-blocking error is a safety placeholder, not a demand to add encryption now.

## Lesson 4: App Shell Code Tour

### Goal

Understand how the React app displays local-first defaults without implementing later workflows.

### Prerequisites

Know the privacy defaults and storage boundary from Lessons 2 and 3. Basic JSX familiarity helps.

### Files

- `web/src/app/LagoonShell.tsx`
- `web/src/app/privacyDefaults.ts`
- `web/src/app/storageBoundary.ts`
- `web/src/main.tsx`
- `web/src/styles.css`

### Code Reading: Imports

Open `web/src/app/LagoonShell.tsx`:

```ts
import { privacyDefaults } from "./privacyDefaults";
import { storageBoundary } from "./storageBoundary";
```

Meaning:

- The component reads plain data objects.
- It does not fetch data from a server.
- It does not call a provider.

### Code Reading: Settings Array

```ts
const settings = [
  ["Local data", privacyDefaults.localOnly ? "On" : "Off"],
  ["Content network", privacyDefaults.networkEnabledForContent ? "On" : "Off"],
  ["Provider calls", privacyDefaults.providerCallsEnabled ? "On" : "Off"],
  ["Cloud sync", privacyDefaults.cloudSyncEnabled ? "On" : "Off"],
  ["Telemetry", privacyDefaults.telemetryEnabled ? "On" : "Off"],
  ["Log redaction", privacyDefaults.redactLogs ? "On" : "Off"],
] as const;
```

Line-by-line meaning:

- Each row pairs a label with a display value.
- `? "On" : "Off"` turns booleans into readable UI text.
- `as const` tells TypeScript these rows are fixed literal values.

Expected display:

- Local data: On.
- Content network: Off.
- Provider calls: Off.
- Cloud sync: Off.
- Telemetry: Off.
- Log redaction: On.

### Code Reading: Main Component

```tsx
export function LagoonShell() {
  return (
    <main className="lagoon-shell">
```

Meaning:

- Exports a React component.
- Returns JSX.
- `className` connects to CSS.

```tsx
<section className="workspace-panel" aria-labelledby="workspace-title">
```

Meaning:

- Groups the workspace summary.
- `aria-labelledby` helps assistive technology connect the section to its heading.

```tsx
<p className="workspace-status">Ready for local metadata. Vault locked.</p>
```

Meaning:

- The app is not claiming full lecture capture yet.
- "Vault locked" means SP-01 does not write raw content.
- It should be read as a safety state, not a mandate to implement encryption immediately.

### Code Reading: Boundary Display

```tsx
<dt>Upload</dt>
<dd>{storageBoundary.contentUploadDefault}</dd>
```

Meaning:

- Shows upload default from `storageBoundary`.
- Should display `blocked`.
- This reinforces no-upload MVP behavior.

### Hands-On Exercise

Run:

```powershell
npm run dev:web
```

Open:

```text
http://127.0.0.1:5173
```

Expected page signals:

- "Local Lecture Workspace"
- "Ready for local metadata. Vault locked."
- "Privacy Defaults"
- Content network Off
- Provider calls Off
- Cloud sync Off
- Upload blocked

Stop the dev server after inspection.

### Debugging Drill

Problem: UI says `Provider calls On`.

Reasoning path:

1. `LagoonShell.tsx` displays `privacyDefaults.providerCallsEnabled`.
2. Open `privacyDefaults.ts`.
3. If value is `true`, default is wrong.
4. If value is `false`, inspect the ternary in `LagoonShell.tsx`.

Fix:

- Restore `providerCallsEnabled: false`.
- Re-run `npm run verify:sp01`.
- Re-run `npm run build:web`.

### Theory Q/A

1. Q: Why does the app shell only display status?
   A: SP-01 proves the foundation before adding workflows.

2. Q: Why not add a "Start Recording" button now?
   A: Media capture belongs to SP-02.

3. Q: Why use imported constants instead of hardcoded text everywhere?
   A: It keeps defaults centralized and easier to verify.

4. Q: Why include accessibility attributes?
   A: Even MVP UI should be understandable to assistive technologies.

5. Q: Why show blocked upload in UI?
   A: Privacy defaults should be visible to users, not hidden in backend code.

### Checkpoint

Task: trace how "Cloud sync Off" appears on screen.

Acceptance criteria:

- Starts at `privacyDefaults.cloudSyncEnabled`.
- Points to `settings` array in `LagoonShell.tsx`.
- Explains ternary conversion to "Off".
- Explains why this matters for MVP.

### Key Takeaways

- SP-01 UI is a status shell.
- It displays local-first defaults.
- It does not implement capture, upload, sync, transcription, or tutoring.

## Lesson 5: Verification And Safe Change Workflow

### Goal

Learn how to verify SP-01 after changes and how to avoid accidental scope creep.

### Prerequisites

Complete Lessons 1-4. Know which files own UI, storage, privacy defaults, and checks.

### Files

- `scripts/verify_sp01_foundation.py`
- `scripts/verify_sp01_foundation.ps1`
- `package.json`
- `web/package.json`

### Verification Commands

Run the narrow check first:

```powershell
npm run verify:sp01
```

Then run the web build:

```powershell
npm run build:web
```

Why this order:

- `verify:sp01` checks the phase contract.
- `build:web` checks TypeScript and bundling.
- Narrow failure messages are usually easier to diagnose.

### Code Reading: Verification Script

Open `scripts/verify_sp01_foundation.py`.

Read it as a checklist, not as magic:

- required files exist,
- privacy defaults deny network/provider/cloud/telemetry,
- storage schema exists,
- content upload is blocked,
- lesson file exists,
- expected lesson sections exist.

When a verifier fails, do not immediately edit random code. Read the exact failed assertion and trace it to the owning file.

### Hands-On Exercise

Run:

```powershell
npm run verify:sp01
npm run build:web
```

Expected result:

- Both pass.

If `verify:sp01` fails:

1. Read the failure text.
2. Identify the owning folder.
3. Fix the smallest cause.
4. Re-run `npm run verify:sp01`.

If `build:web` fails:

1. Read the TypeScript/Vite error.
2. Open the file and line named in the error.
3. Fix syntax/type issue.
4. Re-run `npm run build:web`.

### Safe Change Drill

Task: add a harmless UI-only text tweak.

Steps:

1. Open `web/src/app/LagoonShell.tsx`.
2. Change "Ready for local metadata. Vault locked." to another local-only status sentence.
3. Do not add buttons, state, network calls, or storage writes.
4. Run:

```powershell
npm run verify:sp01
npm run build:web
```

Acceptance criteria:

- Both commands pass.
- UI still communicates local-only foundation.
- No SP-02+ feature appears.

### Scope-Creep Drill

Problem: a developer wants to add "Upload lecture" in SP-01.

Reasoning path:

1. SP-01 out-of-scope list blocks media capture and upload.
2. Privacy defaults say content upload is blocked.
3. SP-02 owns capture.
4. Cloud upload is not MVP.

Correct action:

- Do not implement upload.
- Add idea to run-log next steps if useful.
- Keep SP-01 foundation clean.

### Theory Q/A

1. Q: Why run verification after docs-only lesson changes?
   A: SP-01 verifier checks lesson presence/sections, and docs can drift from code.

2. Q: Why not trust manual inspection only?
   A: Repeatable commands catch regressions faster and help future developers.

3. Q: Why keep verifier narrow?
   A: Narrow checks explain phase-specific failures clearly.

4. Q: Why still run `build:web`?
   A: A phase contract can pass while TypeScript or bundling fails.

5. Q: Why leave future ideas out of code?
   A: Future ideas add complexity before their acceptance criteria and tests exist.

### Checkpoint

Task: describe the safe SP-01 change workflow.

Acceptance criteria:

- Explore owner file.
- Make one small scoped change.
- Run `npm run verify:sp01`.
- Run `npm run build:web`.
- Record anything out of scope as next-step docs, not code.

### Key Takeaways

- Verification is part of the lesson, not an afterthought.
- SP-01 is done when foundation behavior is clear and checked.
- Do not build SP-02+ features inside SP-01.

## Keep It Simple Rules

- Add one small thing at a time.
- Prefer plain constants before custom hooks/classes.
- Keep storage rules in `api/`.
- Keep display code in `web/`.
- Keep phase checks in `scripts/`.
- Keep lessons and rationale in `docs/`.
- Move later ideas to run-log next steps instead of building them early.

## Stop Before These Features

Do not add these in SP-01:

- media capture,
- transcription,
- RAG or vector search,
- tutor practice,
- provider calls,
- accounts,
- cloud sync,
- encryption system work.

Those belong to later phases or post-MVP hardening decisions.
