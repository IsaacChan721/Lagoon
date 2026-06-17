# SP-05 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Build simple local lecture memory and retrieval.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-05/index.md`
- transcript, summary, and storage memory notes

## In Scope

- Local text chunking and indexing.
- Retrieval over selected lecture artifacts.
- Small eval fixtures and retrieval checks.
- Citation-preserving result shape.

## Out Of Scope

- No tutor UX beyond retrieval contract.
- No embeddings or vector database for MVP unless simple text search fails with evidence.
- No cloud vector store.
- No skill improvement loop.

## Execution Steps

1. Confirm transcript artifacts are stable.
2. Define local text index inputs and outputs.
3. Implement chunking and simple local search/retrieval path.
4. Add small held-out eval fixtures.
5. Verify selected lecture filtering.
6. Update memory for retrieval contracts.

## Acceptance Criteria

- Retrieval returns relevant lecture chunks with citations.
- Selected lecture boundary is enforced.
- Eval fixture measures basic retrieval quality.
- Local storage remains default.

## Definition Of Done

- Retrieval tests or small evals run.
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

Design this phase memory as beginner lesson material. Put no-prerequisite retrieval context first, then build toward local text indexing, search results, citations, and evals.

### Lesson Depth Standard

Every lesson below must be written and taught as a 60-90 minute beginner module, not a quick concept note. Use the lesson bullets as topic seeds, then expand them with this structure:

1. Zero-prerequisite setup, 5-10 minutes: define every term used in the lesson, explain why the learner should care, and name the files or planned files they will touch.
2. File map, 10-15 minutes: list each relevant file, folder, command, schema, component, or artifact. For future files, mark them `planned`. Explain what each one owns and what it must not own.
3. Line-by-line code reading, 15-25 minutes: walk through the smallest real code sample available. If implementation does not exist yet, write planned pseudocode and later replace it with real code. Explain each line or block in beginner language, including imports, data shapes, function inputs, outputs, errors, and side effects.
4. Guided hands-on exercise, 15-25 minutes: have the learner run a command, inspect output, trace data through one function, update a harmless fixture, or write a tiny example. Include expected output and what to do if it differs.
5. Debugging or design exercise, 10-20 minutes: give one realistic failure, ask the learner to diagnose it, then provide the answer and the reasoning path.
6. Theory questions and answers, 10-15 minutes: include at least five Q/A pairs that connect the hands-on work to architecture, privacy, security, testing, or user experience.
7. Checkpoint, 5-10 minutes: include a small task the learner can complete without help, plus acceptance criteria.
8. Key takeaways, 5 minutes: list what the learner should remember before moving to the next lesson.

Each lesson must include concrete code or command examples. Prefer real snippets from this codebase once the phase exists. Avoid abstract-only examples. When a lesson covers safety, privacy, auth, encryption, destructive actions, or external providers, spell out the risk clearly and then return to concise style.
### Created In This Phase

- Local text index over selected lecture artifacts.
- Retrieval contract for relevant chunks with citations.
- Small eval fixtures and retrieval checks.
- Index rebuild rules and drift checks.

### Lesson 1: What Retrieval Does

- Prerequisites: none.
- Explain: retrieval finds the best lecture chunks for a user question before any tutor answer.
- Coding example: show a query returning `chunkText`, `score`, `citation`, and `lectureId`.
- Theory Q/A: Why retrieve before answering? It grounds responses in selected lecture evidence.
- Key takeaways: retrieval is evidence selection, not final tutoring.

### Lesson 2: Local Indexing

- Prerequisites: understand retrieval result shape.
- Explain: local index stores searchable text chunks from transcript or summary artifacts.
- Coding example: show pseudocode for `indexLectureText(lectureId, chunks)` and `searchLectureText(lectureId, query)`.
- Theory Q/A: Why use simple text search first? MVP should prove the retrieval contract before adding embeddings, vector stores, or provider complexity.
- Key takeaways: every search needs scope, chunk IDs, and citations; vector search is a later optimization.

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

Update `docs/memory/phases/SP-05/index.md` and codebase notes for local retrieval contracts, evals, and selected lecture filtering.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-05>`.
3. Run `git commit -m "SP-05: complete phase"`.
4. Run `git push`.

Commit only scoped SP-05 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-05-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
