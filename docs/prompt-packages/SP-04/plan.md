# SP-04 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Add video understanding only where it improves lecture learning value.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-04/index.md`
- media and transcript memory notes

## In Scope

- Key frame or key moment extraction.
- Visual evidence linked to transcript time ranges.
- Visual claim guardrails.
- Verification fixtures.

## Out Of Scope

- No generated factual claims without visual evidence.
- No broad computer vision platform.
- No tutor behavior.

## Execution Steps

1. Confirm provenance gate allows visual enrichment.
2. Read media/transcript contracts.
3. Define minimal visual extraction path.
4. Link visual outputs to transcript timestamps.
5. Add no-fake-visual-claims checks.
6. Verify with sample or fixture.

## Acceptance Criteria

- Visual notes reference exact media time ranges.
- Unsupported visual claims are blocked or marked uncertain.
- Extraction failure does not break transcript workflow.
- Outputs are stored in local memory/artifact boundary.

## Definition Of Done

- Visual enrichment has test or manual verification.
- Provenance is preserved.
- Memory notes explain when this phase should run.

## Verification

- Run relevant media/visual tests.
- Use screenshot/frame checks where available.
- Run `git status --short`.

## Troubleshooting

- If frame extraction fails, test media codec and timestamp handling.
- If model output overclaims, tighten prompt/schema and add citation check.
- If cost is high, reduce sampled frames before changing feature scope.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite visual-understanding context first, then build toward frame extraction, visual evidence, and claim guardrails.

### Created In This Phase

- Key frame or key moment extraction logic.
- Visual artifact records linked to media and transcript time ranges.
- Guardrails for uncertain or unsupported visual claims.
- Fixtures or manual checks for frame extraction and evidence links.

### Lesson 1: Why Visual Evidence Exists

- Prerequisites: none.
- Explain: visuals help understand slides, diagrams, boards, and demos that transcript text may miss.
- Coding example: show a visual note object with `mediaArtifactId`, `timeRange`, `framePath`, and `observedText`.
- Theory Q/A: Why avoid broad computer vision? MVP needs lecture learning value, not general image analysis.
- Key takeaways: visual output must point back to exact media time.

### Lesson 2: Frame Extraction

- Prerequisites: understand visual evidence object.
- Explain: extraction samples frames or key moments from recorded media.
- Coding example: show pseudocode for `extractFrames(mediaPath, timestamps)` returning local frame paths.
- Theory Q/A: Why test codec and timestamps first? Most extraction bugs are format or offset problems.
- Key takeaways: frame paths, timestamps, and media IDs must stay synchronized.

### Lesson 3: Claim Guardrails

- Prerequisites: understand frame extraction.
- Explain: app may describe visible evidence but must not invent unseen facts.
- Coding example: show a schema field `claimStatus: "supported" | "uncertain" | "blocked"`.
- Theory Q/A: What happens when model overclaims? Tighten schema and mark unsupported output uncertain or blocked.
- Key takeaways: visual analysis needs evidence links and uncertainty labels.

## Memory Updates

Update `docs/memory/phases/SP-04/index.md` and codebase notes for visual artifact flow, evidence links, and limitations.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-04>`.
3. Run `git commit -m "SP-04: complete phase"`.
4. Run `git push`.

Commit only scoped SP-04 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-04-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
