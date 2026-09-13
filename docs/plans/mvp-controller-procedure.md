# Lagoon MVP Controller Procedure

> [!IMPORTANT]
> The controller coordinates workers; it does not silently implement, waive a gate, or expand scope.

## Dashboard

| Item | Rule |
| --- | --- |
| Goal | Deliver the one-flow MVP in `mvp-build-plan.md` |
| Units of work | Seven sequential worker plans, `00` through `06` |
| Authority | One controller agent validates every handoff; one worker agent owns one slice |
| Evidence | Tests, manual checks where required, changed-file list, and a run log |
| Advancement | Only after every exit criterion for the current plan passes |
| Plan-quality gate | [Readiness Audit](mvp-plan-readiness-audit.md) must score 10/10 before implementation |

## End Goal

The MVP is successful only when one local learner can select a valid MP4, receive an English plain-text transcript and all five note sections, ask one lesson-grounded tutor question, and reopen the latest completed lesson after restart. The MP4, local audio, and provider-side data must be cleaned up as specified in the build plan.

## Controller Loop

1. Read this procedure, the active worker plan, `docs/plans/mvp-build-plan.md`, and any prior run log.
2. Confirm its entry criteria and that no earlier slice remains open. Assign exactly that plan to a worker.
3. Ask the worker to return: implementation summary, changed files, commands run with results, known limitations, and `docs/run-logs/` entry.
4. Independently inspect the changed paths, run the worker plan's automated checks, and perform its manual check if one is required.
5. Compare results to the plan's exit criteria. Record **pass**, **fail**, or **blocked** in a run log.
6. Advance only on **pass**. On **fail**, return the specific failed criterion to the same worker. On **blocked**, stop and ask the human for the missing credential, installation, or decision.

## Required Gate Report

The controller posts one concise status report after every verification. It must name the active plan, goal, result, evidence, failed criterion (when applicable), and next action.

| Result | Meaning | Required next action | User notification |
| --- | --- | --- | --- |
| **Pass** | Every acceptance criterion is evidenced and checks pass. | Commit/checkpoint the slice; assign the named next plan. | “Plan NN passed. Evidence: … Next: Plan NN+1.” |
| **Fail** | A criterion, test, manual check, or scope boundary failed. | Keep the next plan closed; return only the failure details to the current worker. | “Plan NN did not pass. Failed: … Next: correct and re-verify.” |
| **Blocked** | Progress needs a human decision, credential, or unavailable dependency. | Stop implementation; document the exact need and safe alternatives. | “Plan NN is blocked by … No later plan will start.” |

Never use “mostly complete,” “best effort,” or a green UI state as a pass result. The run log must contain the exact commands, results, manual observations, and changed-file list supporting the decision.

## Common Independent Quality Gate

For every slice, the controller must independently inspect the implementation and evidence for all of the following before reporting **pass**:

- Design and scope: the change is the smallest design that satisfies the active plan and does not add a future feature.
- Functionality and failure behavior: the intended user path and the plan's negative/error path both behave as specified.
- Test quality: tests exercise the real boundary, would fail if the behavior regressed, and use no real secrets or private media.
- Data and safety: temporary-media, provider, storage, secret, and privacy rules remain true for the changed code.
- Maintainability and documentation: code is understandable, the diff contains no unrelated change, and README/code map/decision/run-log updates are accurate.

Record a pass/fail/block result for each bullet in the run log. Any failed bullet fails the slice even when its automated suite is green.

## Global Guardrails

- Keep the MVP boundary in `mvp-build-plan.md`: one temporary MP4, English plain-text transcript, five-section notes, and grounded local tutor chat.
- Never commit API keys, private lessons, real tutor chats, or retained MP4/audio. Use synthetic fixtures and fake clients in automated tests.
- Each worker updates `docs/memory/` for new folders/components, `docs/decisions/` for provider/model/storage changes, and `docs/run-logs/` for completion evidence.
- Do not begin a later plan merely because code exists; the previous plan's acceptance criteria must be demonstrated.
- A provider cleanup failure is a visible application failure with an in-session retry path, not a successful completion.

## Sequence and Handoffs

| Order | Worker plan | Controller verifies before assigning next |
| --- | --- | --- |
| 0 | [Foundation](00-foundation-plan.md) | UI-to-health path, setup guidance, configuration boundary |
| 1 | [Media](01-media-extraction-plan.md) | MP4/duration validation and local cleanup in both outcomes |
| 2 | [Transcription](02-transcription-plan.md) | Audio-only provider boundary plus local/provider cleanup behavior |
| 3 | [Notes](03-notes-plan.md) | Five sections for multi-chunk text |
| 4 | [Tutor](04-tutor-plan.md) | Relevant grounding and bounded unsupported answers |
| 5 | [Full flow](05-full-flow-plan.md) | End-to-end fixture journey, UI states, and restart restoration |
| 6 | [Handoff](06-handoff-plan.md) | A beginner independently repeats setup and smoke test |

Before assigning any row, the controller also records a 10/10 pre-execution score using the [Readiness Audit](mvp-plan-readiness-audit.md). After delivery, it records the same ten criteria with evidence.

## Release Gate

The controller may call the MVP complete only when every worker plan is passed and every checkbox in the build plan's Definition of Done is demonstrably satisfied. The final report must state **MVP successful** only after Plan 06 independently reproduces the complete flow; otherwise it must state **MVP not yet successful** and list the remaining failed or blocked criteria.

## Stop Point

This procedure does not authorize deployment, queues, a database, accounts, cloud sync, or features outside the MVP.
