# Markdown Presentation Rules

Use these rules for every new or updated Lagoon plan, lesson, run log, handoff, audit, README, memory note, and prompt package.

> [!IMPORTANT]
> Markdown should be learner-readable when rendered on GitHub. Do not write docs as plain TXT with headings sprinkled in.

## Required Shape

Every substantial document should start with:

| Section | Purpose |
| --- | --- |
| Title | Clear document name. |
| Callout | One short `NOTE`, `TIP`, `IMPORTANT`, or `WARNING` block that frames the doc. |
| Dashboard | Small table with phase, goal, scope, checks, owner, or status. |
| Quick Navigation | Table of links for long docs. |
| Main Sections | Short chunks with tables, checklists, code blocks, and examples. |
| Verification | Exact commands or checks, with expected result. |
| Stop Points | What must not be built or assumed yet. |

Short notes may omit Quick Navigation, but still need enough structure to render cleanly.

## Visual Tools

Prefer GitHub-rendered structure:

| Use | For |
| --- | --- |
| Tables | File maps, command menus, concept definitions, phase boundaries, acceptance criteria. |
| Checklists | Learner checkpoints, done criteria, release readiness, review gates. |
| Callouts | Safety notes, MVP boundaries, important context, tips. |
| Code fences | Commands, snippets, examples, expected output. |
| `<details>` blocks | Optional deep dives, long code tours, advanced notes. |
| Horizontal rules | Separate major learning modules or phase sections. |

## Writing Rules

- Keep paragraphs short: 1-3 sentences.
- Put dense facts in tables instead of long comma-heavy prose.
- Use learner-facing labels: `Goal`, `Why it matters`, `Files`, `Commands`, `Checkpoint`, `Expected result`.
- Prefer concrete codebase paths and commands over abstract explanation.
- Keep phase boundaries visible: say what is in scope and out of scope.
- For safety, privacy, auth, external providers, destructive actions, or cost: use clear normal prose, then return to concise style.
- Avoid decorative-only formatting. Every table or callout must make reading easier.

## Lesson Template

```markdown
# {PHASE_ID} {Lesson Name}

> [!NOTE]
> One-sentence phase/lesson frame.

## Learning Dashboard

| Item | Details |
| --- | --- |
| Learner goal | ... |
| Main feature | ... |
| Phase boundary | ... |
| Best first check | `...` |
| Time box | ... |

## Quick Navigation

| Section | Best for |
| --- | --- |
| [Beginner Path](#beginner-path) | ... |
| [Lesson Map](#lesson-map) | ... |

## Beginner Path

1. `path/to/file`
2. `path/to/other-file`

## Lesson Map

| Lesson | Focus | Done when |
| --- | --- | --- |
| 1 | ... | ... |

---

## Lesson 1: ...

### Goal

...

### Files

| File | Why open it |
| --- | --- |
| `...` | ... |

### Checkpoint

- [ ] ...
- [ ] ...
```

## Plan Template

```markdown
# {PHASE_ID} Plan

> [!IMPORTANT]
> One-sentence contract and boundary.

## Plan Dashboard

| Item | Details |
| --- | --- |
| Phase | `{PHASE_ID}` |
| Goal | ... |
| In scope | ... |
| Out of scope | ... |
| Verification | `...` |

## Task Map

| Step | Work | Files | Check |
| --- | --- | --- | --- |
| 1 | ... | `...` | ... |

## Acceptance Criteria

- [ ] ...
- [ ] ...

## Stop Points

| Do not build | Reason |
| --- | --- |
| ... | ... |
```

