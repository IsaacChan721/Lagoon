# privacyDefaults

## Purpose

Frontend mirror of SP-01 local-first privacy defaults.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\web\src\app\privacyDefaults.ts`

## Owns

- `PrivacyDefaults` type.
- `privacyDefaults` constant.

## Public Interface

- `privacyDefaults.localOnly`
- `privacyDefaults.networkEnabledForContent`
- `privacyDefaults.providerCallsEnabled`
- `privacyDefaults.cloudSyncEnabled`
- `privacyDefaults.telemetryEnabled`
- `privacyDefaults.redactLogs`

## Data Contracts

- Defaults match `api/lagoon_local/settings.py`.

## Dependencies

- TypeScript only.

## Tests

- `npm run verify:sp01`.
- `npm run build:web`.

## Gotchas

- Keep in sync with backend defaults until shared schema generation exists.

## Last Updated

SP-01

