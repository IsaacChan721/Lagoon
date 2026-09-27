"""API-boundary tests for Lagoon's foundation health endpoint."""

from __future__ import annotations

import json
import socket
import subprocess
import sys
import time
import unittest
from pathlib import Path
from urllib.request import urlopen


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class HealthEndpointTests(unittest.TestCase):
    def test_health_endpoint_returns_expected_json(self) -> None:
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            port = probe.getsockname()[1]

        process = subprocess.Popen(
            [sys.executable, "api/main.py", "--port", str(port)],
            cwd=REPOSITORY_ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            url = f"http://127.0.0.1:{port}/api/health"
            for _ in range(30):
                try:
                    with urlopen(url, timeout=0.25) as response:
                        self.assertEqual(response.status, 200)
                        self.assertEqual(response.headers["Content-Type"], "application/json; charset=utf-8")
                        self.assertEqual(
                            json.load(response),
                            {"status": "ok", "message": "Lagoon API is healthy."},
                        )
                        return
                except OSError:
                    time.sleep(0.1)
            self.fail("The local API did not become ready.")
        finally:
            process.terminate()
            process.wait(timeout=5)

