# Lagoon MVP Plan Validation Checklist

> [!IMPORTANT]
> This checklist validates the plan, not the unbuilt application. Re-run it whenever the MVP scope or a provider choice changes.

## Validation Dashboard

| Item | Result |
| --- | --- |
| Plan reviewed | `docs/plans/mvp-build-plan.md` |
| Initial score | 8/10 |
| Corrections made | Long-transcript note handling and audio-only, cleanup-safe transcription flow |
| Final score | 10/10 |
| Verification | Markdown checks pass; requirements are traceable to a slice and done criterion |

## Quick Navigation

| Section | Purpose |
| --- | --- |
| [Checklist](#checklist) | The ten scoring checks |
| [Review Log](#review-log) | What was fixed before the final score |
| [Verification](#verification) | Repeatable document checks |
| [Stop Point](#stop-point) | What this score does not claim |

## Checklist

Give one point only when the plan is explicit, testable, and within MVP scope.

| # | Check | Result | Evidence |
| --- | --- | --- | --- |
| 1 | The outcome is one complete learner flow, not a feature list. | 1/1 | Plan opening and Definition of Done. |
| 2 | Input type and duration are bounded; temporary media ownership is explicit. | 1/1 | MP4, 60 minutes, per-job temporary storage and cleanup. |
| 3 | Transcription provider, audio-only transfer, language, output, and privacy boundary are named. | 1/1 | AssemblyAI receives extracted audio only; English plain text; disclosure, cleanup, and deletion-failure behavior. |
| 4 | Notes have the five agreed sections and handle a long transcript. | 1/1 | Slice 3 requires chunking and combined notes. |
| 5 | Tutor behavior is free-form, teacher-oriented, and lesson-grounded. | 1/1 | Tutor requirement and Slice 4 test. |
| 6 | UI states and latest-lesson persistence are defined without design scope. | 1/1 | Feedback and continuity requirements. |
| 7 | The layout assigns each responsibility to one simple folder. | 1/1 | Project Layout. |
| 8 | Work is divided into sequential, independently testable slices. | 1/1 | Build Slices table. |
| 9 | Tests avoid real keys/media and include an end-to-end smoke test. | 1/1 | Test Rules and Definition of Done. |
| 10 | Scope exclusions prevent non-MVP architecture and features. | 1/1 | Boundaries and Stop Points. |

## Review Log

| Pass | Score | Finding | Resolution |
| --- | --- | --- | --- |
| 1 | 8/10 | A one-hour MP4 can exceed the transcription provider's local-upload limit; note generation did not explicitly handle long transcript context. | Added a 2 GB input cap and required chunked, combined notes. |
| 2 | 10/10 | The initial scope was complete, but it still sent and retained the MP4 beyond the user's intended audio-only path. | Superseded by the audio-only review below. |
| 3 | 9/10 | The plan said to extract audio, but did not specify cleanup after every failure or removal of provider-side data. | Added per-job cleanup, post-upload local-audio deletion, and post-retrieval AssemblyAI deletion. |
| 4 | 10/10 | All ten checks are explicit, testable, and trace to a build slice or release gate. | No further change required. |

## Verification

Run these from the repository root:

```powershell
git diff --check
rg -n "60 minutes|audio|AssemblyAI|delete|five-section|Tutor|Definition of Done" docs/plans/mvp-build-plan.md
```

Expected result: no `git diff --check` output, and the search finds the core requirements in the plan.

## Stop Point

A 10/10 plan score means the MVP contract is complete and appropriately small. It does not prove that the application, provider account, local model, or user interface is working; those are implementation checks in the build slices.
