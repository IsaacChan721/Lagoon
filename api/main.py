"""Small, local HTTP API for Lagoon's foundation slice."""

from __future__ import annotations

import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class LagoonHandler(BaseHTTPRequestHandler):
    """Serve the one foundation endpoint and allow the Vite origin to call it."""

    def do_GET(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        if self.path == "/api/health":
            self._send_json(HTTPStatus.OK, {"status": "ok", "message": "Lagoon API is healthy."})
            return

        self._send_json(HTTPStatus.NOT_FOUND, {"error": "Not found."})

    def do_OPTIONS(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        self.send_response(HTTPStatus.NO_CONTENT)
        self._send_cors_headers()
        self.end_headers()

    def _send_json(self, status: HTTPStatus, body: dict[str, str]) -> None:
        encoded = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self._send_cors_headers()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def _send_cors_headers(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "http://127.0.0.1:5173")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the local Lagoon API.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8000, type=int)
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), LagoonHandler)
    print(f"Lagoon API listening at http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

