import { useEffect, useState } from 'react'
import { getHealth } from './api/health'

type HealthState =
  | { kind: 'loading' }
  | { kind: 'success'; message: string }
  | { kind: 'failure'; message: string }

export default function App() {
  const [health, setHealth] = useState<HealthState>({ kind: 'loading' })

  useEffect(() => {
    getHealth()
      .then((response) => setHealth({ kind: 'success', message: response.message }))
      .catch(() =>
        setHealth({
          kind: 'failure',
          message: 'Could not reach the local API. Start it with: py api/main.py',
        }),
      )
  }, [])

  return (
    <main>
      <h1>Lagoon</h1>
      <p>Foundation: browser-to-local-API health check.</p>
      <section aria-live="polite" aria-label="API health">
        {health.kind === 'loading' && <p role="status">Checking local API…</p>}
        {health.kind === 'success' && (
          <p role="status">API connection successful: {health.message}</p>
        )}
        {health.kind === 'failure' && <p role="alert">{health.message}</p>}
      </section>
    </main>
  )
}

