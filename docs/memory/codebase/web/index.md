# web

## Purpose

Vite React TypeScript local app shell.

## Contains

- `index.html`
- `package.json`
- `tsconfig.json`
- `src/`
- Inline favicon data URL in `index.html` to avoid dev-server `/favicon.ico` 404 noise.

## Key Files

- `web/src/App.tsx`
- `web/src/app/LagoonShell.tsx`

## Interfaces

- `npm run dev:web`
- `npm run build:web`

## Dependencies

- React 19.
- Vite 8.
- TypeScript 5.
- Browser File/object URL APIs for SP-02 Lecture Media Import.

## Tests

- `npm run build:web`
- Scoped HTTP smoke against Vite dev server.
- Browser E2E smoke against `http://127.0.0.1:5173`: initial render, unsupported file, supported audio metadata failure, save, reset, and mobile overflow.
- `npm run verify:sp02`

## Gotchas

- Dev server binds `127.0.0.1:5173` by default.
- SP-02 adds lecture media import UI only; no transcription/provider/sync.
- `@vitejs/plugin-react` was removed because no custom Vite config uses it; fewer dependencies for MVP.

## Last Updated

SP-02
E2E hardening pass, 2026-07-14
