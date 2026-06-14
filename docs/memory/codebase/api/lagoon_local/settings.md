# settings.py

## Purpose

Defines SP-01 privacy defaults for local-first behavior.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\api\lagoon_local\settings.py`

## Owns

- `PrivacySettings` dataclass.
- `default_privacy_settings()`.

## Public Interface

- `PrivacySettings.to_metadata() -> dict[str, bool]`
- `default_privacy_settings() -> PrivacySettings`

## Data Contracts

- `local_only = True`
- `network_enabled_for_content = False`
- `provider_calls_enabled = False`
- `cloud_sync_enabled = False`
- `telemetry_enabled = False`
- `redact_logs = True`

## Dependencies

- Python stdlib dataclasses.

## Tests

- Verified by `scripts/verify_sp01_foundation.py`.

## Gotchas

- Frontend mirror exists in `web/src/app/privacyDefaults.ts`; keep defaults aligned.

## Last Updated

SP-01

