# storageBoundary

## Purpose

Frontend declaration of local persistence boundary.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\web\src\app\storageBoundary.ts`

## Owns

- `StorageBoundary` type.
- `storageBoundary` constant.

## Public Interface

- `mode: "local-only"`
- `metadata: "sqlite"`
- `vault: "encrypted-local-vault"`
- `contentUploadDefault: "blocked"`
- `rawContentInRepo: "forbidden"`

## Data Contracts

- Mirrors local-first decision notes.

## Dependencies

- TypeScript only.

## Tests

- `npm run verify:sp01`.
- `npm run build:web`.

## Gotchas

- This is boundary metadata, not encryption implementation.

## Last Updated

SP-01

