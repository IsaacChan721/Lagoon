# Worker Plan 06: Documentation and Release Handoff

> [!IMPORTANT]
> The final worker documents and verifies the completed MVP; it does not add features or hardening.

## Contract

| Item | Requirement |
| --- | --- |
| Prerequisite | Plans 00-05 passed |
| Deliverable | Accurate beginner setup, verification, limitations, code map, decisions, and run logs |
| Reader | A new local developer with no prior project knowledge |
| Quality gate | [Readiness Audit](mvp-plan-readiness-audit.md) scores 10/10 before work; controller records all common quality checks afterward |

## Goal

Prove that a new local developer can set up, verify, and understand the bounded MVP without relying on this conversation. Success means the controller has enough independent evidence to truthfully declare the end goal met.

## Tasks

1. Reconcile README setup/run/test instructions with the actual project commands and required local dependencies.
2. Document configuration names and privacy behavior: temporary MP4/audio, AssemblyAI audio transfer/deletion, and local retention of latest lesson data.
3. Update code map, decisions, and run logs so every non-obvious component and provider/model/storage choice is traceable.
4. Run all automated suites and the documented end-to-end smoke procedure; record outcomes and known local prerequisites.
5. Check the release gate against every Definition of Done item and report any remaining gap honestly.

## Acceptance Criteria

- [ ] A beginner can follow the README from a clean checkout to start, test, and repeat the fixture smoke flow.
- [ ] Documentation names all required dependencies/configuration without exposing secrets.
- [ ] Docs correctly state MVP limits and privacy/cleanup behavior.
- [ ] The code map and run logs point to current paths and successful verification commands.
- [ ] Every Definition of Done checkbox is evidenced, or the plan records a specific blocking gap and does not claim release.

## Controller Verification

Have an independent controller follow the README literally in a clean local environment, run the recorded checks, inspect the Definition of Done mapping, and apply every item in the controller's Common Independent Quality Gate. Mark the MVP complete only if this plan and every prior gate pass with no failed quality-gate item.

## Outcome and Next Step

| Verification result | Report to user | Next step |
| --- | --- | --- |
| Pass | “Handoff passed — MVP successful” with clean-setup and Definition-of-Done evidence. | Commit/tag the MVP checkpoint; record release-ready status. |
| Fail | “Handoff failed — MVP not yet successful” with the exact unmet Definition-of-Done item. | Reopen the responsible numbered plan; re-run this independent handoff verification afterward. |
| Blocked | “Handoff blocked — MVP not yet successful” with the missing access, machine setup, or decision. | Resolve the blocker and repeat clean-environment verification. |

## Stop Point

Do not turn documentation review into dependency upgrades, deployment, security hardening, or new functionality.
