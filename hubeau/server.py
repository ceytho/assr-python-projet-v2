#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import requests


# Cache and rate limiting state (module-level dicts, shared across requests)
_cache = {}
_rate_limit_log = {}


def load_config(config_path: str = "") -> dict:
    """Parse a config file and return a dict with configuration values."""

    config_dict = {}

    return config_dict


def fetch_hardness(api_url: str, code_reseau: str, size: int = 10) -> list:
    """Query the Hub'eau API and return a simplified list of hardness measurements.

    Each record in the returned list must contain:
        commune, departement, date, hardness_f, unit, distributor, network.
    """

    data = []

    return data


def cache_get(key: str):
    """Return the cached value for key if it exists and has not expired.

    Returns None on a cache miss or if the entry has expired.
    """

    return None


def cache_set(key: str, value, ttl: int):
    """Store value in the cache under key with a time-to-live in seconds."""

    pass

class HubeauHandler(BaseHTTPRequestHandler):
    """HTTP request handler for the Hub'eau proxy API."""

    config = {}  # shared configuration, loaded at startup

    def do_GET(self):
        """Route incoming GET requests to the appropriate handler."""

        pass

    def handle_hardness(self, params: dict):
        """Handle GET /hardness with mandatory code_reseau query parameter."""

        pass

    def handle_cache(self):
        """Handle GET /cache -- return cache statistics as JSON."""

        pass

    def handle_health(self):
        """Handle GET /health -- return a simple status response."""

        pass


def run_server(host: str, port: int, config: dict):
    """Start the HTTP server and serve requests until interrupted."""

    HubeauHandler.config = config
    server = HTTPServer((host, port), HubeauHandler)
    print(f"Server running on http://{host}:{port}")
    server.serve_forever()


def main():
    """Entry point: load configuration and start the server."""

    base_dir = Path(__file__).parent
    config_path = base_dir / "config.ini"
    config = load_config(str(config_path))

    host = config["server"]["host"]
    port = int(config["server"]["port"])

    run_server(host, port, config)


if __name__ == "__main__":
    main()
