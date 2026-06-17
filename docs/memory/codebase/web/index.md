# web

## Purpose

Vite React TypeScript local app shell.

## Contains

- `index.html`
- `package.json`
- `tsconfig.json`
- `src/`

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
- Browser MediaRecorder API for SP-02 capture.

## Tests

- `npm run build:web`
- Scoped HTTP smoke against Vite dev server.
- `npm run verify:sp02`

## Gotchas

- Dev server binds `127.0.0.1:5173` by default.
- SP-02 adds media capture UI only; no transcription/provider/sync.
- `@vitejs/plugin-react` was removed because no custom Vite config uses it; fewer dependencies for MVP.

## Last Updated

SP-02
