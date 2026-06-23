# Lagoon Lessons

Use this folder as the learner-facing guide for Lagoon phases.

> [!TIP]
> Open these files on GitHub, not as raw text, when learning. GitHub renders tables, checklists, callouts, code blocks, and collapsible sections into a cleaner study view.

## Lesson Catalog

| Phase | Lesson | Best for | Time |
| --- | --- | --- | --- |
| SP-01 | [Local App Foundation](SP-01-local-app-foundation.md) | repo shape, privacy defaults, local storage boundary, safe verification | 60-90 min |
| SP-02 | [Lecture Media Import](SP-02-lecture-media-import.md) | media file selection, browser preview, artifact metadata, local persistence | 45-75 min |

## Study Flow

1. Read the lesson overview table.
2. Run the listed verification command before edits.
3. Expand code-tour sections only when you need deeper detail.
4. Complete the checkpoint before moving to the next lesson.
5. Re-run checks after any code change.

## Phase Rules

| Rule | Meaning |
| --- | --- |
| One phase at a time | Do not build later workflow features inside earlier foundation lessons. |
| Local-first by default | No cloud sync, telemetry, provider calls, or content network unless a later phase explicitly allows it. |
| Verify small | Run the narrow phase verifier before broad checks. |
| Preserve learner clarity | Prefer tables, short sections, and examples over walls of prose. |

## Command Menu

```powershell
npm run verify:sp01
npm run verify:sp02
npm run build:web
```

