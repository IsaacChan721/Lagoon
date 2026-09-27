export type HealthResponse = {
  status: 'ok'
  message: string
}

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'

export async function getHealth(): Promise<HealthResponse> {
  const controller = new AbortController()
  const timeout = window.setTimeout(() => controller.abort(), 5_000)

  try {
    const response = await fetch(`${apiBaseUrl}/api/health`, { signal: controller.signal })
    if (!response.ok) {
      throw new Error(`The API returned HTTP ${response.status}.`)
    }
    return (await response.json()) as HealthResponse
  } catch (error) {
    if (error instanceof DOMException && error.name === 'AbortError') {
      throw new Error('The API did not respond within five seconds.')
    }
    throw error
  } finally {
    window.clearTimeout(timeout)
  }
}

