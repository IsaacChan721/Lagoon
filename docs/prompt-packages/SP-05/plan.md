# SP-05 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Build local memory and RAG layer for lecture retrieval.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-05/index.md`
- transcript, summary, and storage memory notes

## In Scope

- Local indexing.
- Retrieval over selected lecture artifacts.
- Eval fixtures and retrieval metrics.
- Citation-preserving result shape.

## Out Of Scope

- No tutor UX beyond retrieval contract.
- No cloud vector store.
- No skill improvement loop.

## Execution Steps

1. Confirm transcript artifacts are stable.
2. Define local index inputs and outputs.
3. Implement chunking/indexing/retrieval path.
4. Add held-out eval fixtures.
5. Verify selected lecture filtering.
6. Update memory for retrieval contracts.

## Acceptance Criteria

- Retrieval returns relevant lecture chunks with citations.
- Selected lecture boundary is enforced.
- Eval fixture measures retrieval quality.
- Local storage remains default.

## Definition Of Done

- Retrieval tests/evals run.
- Index rebuild behavior is documented.
- Tutor phase can consume retrieval contract.

## Verification

- Run retrieval unit tests and eval fixtures.
- Check citation fields in retrieval output.
- Run `git status --short`.

## Troubleshooting

- If retrieval quality is low, inspect chunking before changing model.
- If citations are missing, block tutor phase.
- If index drift appears, add deterministic fixture.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite retrieval context first, then build toward indexing, search results, citations, and evals.

### Created In This Phase

- Local index over selected lecture artifacts.
- Retrieval contract for relevant chunks with citations.
- Eval fixtures and retrieval metrics.
- Index rebuild rules and drift checks.

### Lesson 1: What Retrieval Does

- Prerequisites: none.
- Explain: retrieval finds the best lecture chunks for a user question before any tutor answer.
- Coding example: show a query returning `chunkText`, `score`, `citation`, and `lectureId`.
- Theory Q/A: Why retrieve before answering? It grounds responses in selected lecture evidence.
- Key takeaways: retrieval is evidence selection, not final tutoring.

### Lesson 2: Local Indexing

- Prerequisites: understand retrieval result shape.
- Explain: local index stores searchable representations of transcript or summary chunks.
- Coding example: show pseudocode for `indexLecture(lectureId, chunks)` and `searchLecture(lectureId, query)`.
- Theory Q/A: Why enforce selected lecture boundary? It prevents answers from leaking across classes or topics.
- Key takeaways: every search needs scope, chunk IDs, and citations.

### Lesson 3: Eval Fixtures

- Prerequisites: understand indexing.
- Explain: eval fixtures ask known questions and check whether expected chunks return.
- Coding example: show a fixture with `question`, `expectedChunkId`, and `minScore`.
- Theory Q/A: Why inspect chunking before changing model? Bad chunks make even strong retrieval look weak.
- Key takeaways: deterministic evals make retrieval quality visible over time.

### Lesson 4: Tutor Contract

- Prerequisites: understand evals and citations.
- Explain: `SP-07` tutor consumes retrieval output and must preserve citation fields.
- Coding example: show a TypeScript type for `RetrievedEvidence[]`.
- Theory Q/A: Why block tutor if citations are missing? Tutor feedback would be ungrounded.
- Key takeaways: retrieval output is a contract between memory and tutor features.

## Memory Updates

Update `docs/memory/phases/SP-05/index.md` and codebase notes for RAG contracts, evals, and selected lecture filtering.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-05>`.
3. Run `git commit -m "SP-05: complete phase"`.
4. Run `git push`.

Commit only scoped SP-05 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-05-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
