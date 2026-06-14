# SP-10 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Add optional encrypted cloud sync only after local MVP is stable.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-10/index.md`
- storage, security, and release memory notes

## In Scope

- Opt-in sync contract.
- Encryption before upload.
- Supabase schema/RLS if Supabase is chosen.
- Conflict and recovery behavior.

## Out Of Scope

- No default cloud upload.
- No plaintext lecture sync.
- No sync before `SP-09` readiness.

## Execution Steps

1. Confirm local MVP release gate.
2. Read storage/security memory.
3. Define opt-in sync model and encrypted payload boundary.
4. Add schema/RLS only if cloud sync is approved.
5. Implement conflict detection and recovery behavior.
6. Verify sync with encryption and opt-out path.

## Acceptance Criteria

- Cloud sync is disabled by default.
- Data is encrypted before upload.
- RLS/auth policy protects user data.
- Conflict behavior is deterministic.

## Definition Of Done

- Sync tests pass or blocker is explicit.
- Security review covers auth, RLS, and encryption.
- Memory notes capture setup, risks, and rollback.

## Verification

- Run sync unit/integration tests.
- Verify no plaintext lecture content leaves local storage.
- Run `git status --short`.

## Troubleshooting

- If RLS is uncertain, block release of sync.
- If encryption key handling is weak, keep sync disabled.
- If conflicts corrupt local state, restore from local-first source.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite cloud-sync context first, then build toward opt-in consent, encryption, RLS/auth, conflicts, and recovery.

### Created In This Phase

- Opt-in sync contract and consent surface.
- Encryption-before-upload path.
- Cloud schema/auth/RLS policy if Supabase or another provider is chosen.
- Conflict resolution and recovery behavior.
- Security review for plaintext leakage, keys, and authorization.

### Lesson 1: Why Sync Is Opt-In

- Prerequisites: none.
- Explain: Lagoon is local-first; cloud sync is optional and disabled by default.
- Coding example: show settings fields `syncEnabled: false`, `lastSyncedAt`, and `provider`.
- Theory Q/A: Why no default cloud upload? Lecture content is sensitive and must stay local unless user chooses sync.
- Key takeaways: consent is a product and security requirement.

### Lesson 2: Encryption Before Upload

- Prerequisites: understand opt-in sync.
- Explain: lecture content must be encrypted locally before any network transfer.
- Coding example: show pseudocode `ciphertext = encrypt(plaintext, localKey)` before `upload(ciphertext)`.
- Theory Q/A: Why block on weak key handling? Encryption fails if keys are exposed or stored badly.
- Key takeaways: never send plaintext lecture content to cloud storage.

### Lesson 3: Auth And RLS

- Prerequisites: understand encryption path.
- Explain: auth identifies the user; row-level security limits which rows that user can access.
- Coding example: show a policy concept: user can select rows only where `owner_id = auth.uid()`.
- Theory Q/A: Why block if RLS is uncertain? Misconfigured policy can expose private lecture metadata or ciphertext.
- Key takeaways: encryption and authorization both matter.

### Lesson 4: Conflicts And Recovery

- Prerequisites: understand auth and sync data flow.
- Explain: sync must handle local/cloud version conflicts without corrupting local source of truth.
- Coding example: show metadata fields `version`, `updatedAt`, `deviceId`, and `conflictState`.
- Theory Q/A: Why restore from local-first source after corruption? Local data remains primary in Lagoon model.
- Key takeaways: deterministic conflict rules protect user work.

## Memory Updates

Update `docs/memory/phases/SP-10/index.md` and codebase notes for sync contract, encryption, schema/RLS, and rollback.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-10>`.
3. Run `git commit -m "SP-10: complete phase"`.
4. Run `git push`.

Commit only scoped SP-10 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-10-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
