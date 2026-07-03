# CRIT-01 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Gate source provenance and security before enrichment phases continue.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/memory/index.md`
- `docs/memory/phases/CRIT-01/index.md`
- transcript, transcript chunk, and storage memory notes

## In Scope

- Validate transcript integrity assumptions.
- Validate transcript chunk provenance and timestamp continuity.
- Review citation/source trust boundary.
- Review prompt-injection and unsafe content paths.
- Block next phase if provenance policy is weak.

## Out Of Scope

- No new feature implementation.
- No online source ingestion unless needed for review sample.
- No broad refactor.

## Execution Steps

1. Read security and provenance docs/memory.
2. Identify assets, attackers, and trust boundaries.
3. Review transcript/source evidence chain, including transcript segment IDs, transcript chunk IDs, media artifact IDs, and absolute time ranges.
4. Confirm browser object URLs are excluded from durable provenance and backend processing.
5. Define citation requirements and blocked source types.
6. Return pass/fail gate with required fixes.

## Acceptance Criteria

- Trust boundaries are explicit.
- Citation/provenance policy is testable.
- Transcript chunks cite source transcript segments and original media time ranges.
- Durable artifact IDs, not browser object URLs, are used for trusted evidence.
- Prompt-injection risks are named with mitigations.
- `SP-04` or `SP-06` is blocked if source policy is incomplete.

## Definition Of Done

- Gate result is clear: pass, conditional pass, or blocked.
- Required fixes are actionable.
- Memory and handoff output are updated.

## Verification

- Run `rg -n "provenance|citation|trust boundary|prompt injection|transcript chunk|mediaArtifactId|object URL" docs`.
- Run any available security/static checks.
- Run `git status --short`.

## Troubleshooting

- If transcript chunk evidence chain is missing, block rather than guess.
- If timestamps are relative to provider chunks but not converted to absolute lecture time, block downstream citation use.
- If source type is ambiguous, classify as untrusted until policy says otherwise.
- If online content can enter prompts, require sanitization and citation checks.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite provenance context first, then build toward trust boundaries, prompt-injection risks, and gate decisions.

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

- Provenance gate result: pass, conditional pass, or blocked.
- Trust-boundary notes for transcript, transcript chunk, source, prompt, and storage paths.
- Required fixes for weak citation or unsafe content handling.
- Handoff report explaining whether enrichment phases may continue.

### Lesson 1: What Provenance Means

- Prerequisites: none.
- Explain: provenance records where a fact came from and why app can trust it.
- Coding example: show a citation object with `sourceType`, `artifactId`, `chunkId`, `segmentIds`, `timeRange`, `quote`, and `confidence`.
- Theory Q/A: Why block if evidence is missing? Later summaries and tutor answers would look trustworthy without proof.
- Key takeaways: no evidence means no trusted claim.

### Lesson 2: Trust Boundaries

- Prerequisites: understand provenance.
- Explain: local transcript, external web source, model output, and user input have different trust levels.
- Coding example: show enum values like `trusted_local`, `untrusted_external`, and `generated_unverified`.
- Theory Q/A: Why classify ambiguous sources as untrusted? It prevents accidental promotion of unsafe content.
- Key takeaways: trust is explicit metadata, not a feeling.

### Lesson 3: Prompt-Injection Defense

- Prerequisites: understand trust boundaries.
- Explain: external text can contain instructions that should not control the app.
- Coding example: show a sanitizer that strips instruction-like source text from tool prompts while keeping cited content.
- Theory Q/A: What is the safest default for online content? Treat it as evidence to cite, not instructions to obey.
- Key takeaways: source content can inform answers but must not override system or app rules.

### Lesson 4: Gate Decision

- Prerequisites: understand provenance and injection risk.
- Explain: gate result tells later phases whether source-dependent work can proceed.
- Coding example: show a simple gate checklist with booleans for citations, source policy, injection handling, and storage safety.
- Theory Q/A: Why use conditional pass? It lets safe work continue while naming fixes required before risky paths.
- Key takeaways: gate protects future features from building on weak evidence.

## Memory Updates

Update `docs/memory/phases/CRIT-01/index.md` with gate result, transcript/chunk provenance risks, required mitigations, and next phase permission.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for CRIT-01>`.
3. Run `git commit -m "CRIT-01: complete phase"`.
4. Run `git push`.

Commit only scoped CRIT-01 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/CRIT-01-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
