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

## Tests

- `npm run build:web`
- Scoped HTTP smoke against Vite dev server.

## Gotchas

- Dev server binds `127.0.0.1:5173` by default.
- No media/provider UI actions in SP-01.
- `@vitejs/plugin-react` was removed because no custom Vite config uses it; fewer dependencies for MVP.

## Last Updated

SP-01 follow-up
