# api/lagoon_local/jobs

> [!NOTE]
> Job helpers classify transcription failures and keep retry behavior deterministic.

## Dashboard

| Item | Details |
| --- | --- |
| Real path | `C:\Users\isaac\Documents\Projects\Lagoon\api\lagoon_local\jobs\` |
| Main file | `retry.py` |
| Phase | `SP-03` |
| Verification | `npm run verify:sp03` |

## Public Interface

| Function | Purpose |
| --- | --- |
| `classify_transcription_error(message)` | Maps provider/local error strings to `auth`, `quota`, `payload`, `network`, `codec`, or `unknown`. |
| `should_retry(failure_kind, attempt, max_attempts)` | Retries only bounded `network` and `unknown` failures. |
| `run_with_retry(operation, max_attempts=3)` | Runs provider operation with deterministic retry policy. |

## Gotchas

- Auth, quota, payload, and codec failures do not retry.
- Unknown retries are bounded to avoid hidden loops.
