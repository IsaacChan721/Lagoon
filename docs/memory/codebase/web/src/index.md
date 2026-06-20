# web/src

## Purpose

Frontend source root for Lagoon shell.

## Contains

- `main.tsx`
- `App.tsx`
- `styles.css`
- `app/`
- `media-import/`

## Key Files

- `main.tsx`
- `App.tsx`
- `media-import/MediaImportPanel.tsx`

## Interfaces

- `App` React component.

## Dependencies

- React.
- React DOM.

## Tests

- `npm run build:web`
- `npm run verify:sp02`

## Gotchas

- Keep app entry small; feature state now belongs under domain folders such as `src/media-import/`.

## Last Updated

SP-02
