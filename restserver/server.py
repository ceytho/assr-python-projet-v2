#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


def load_config(config_path: str = "") -> dict:
    """Parse a config file and return a dict with configuration values."""

    config_dict = {}

    return config_dict


def load_data(csv_path: Path) -> list:
    """Load CSV data and return content as a list of dicts.

    Each dict must contain the keys: city, date, temp_c (float), humidity_pct (int).
    """

    data = []

    return data


def filter_data(data: list, filters: dict) -> list:
    """Filter data records according to provided criteria.

    Supported filters:
        city (str)      : exact match on the city field
        min_temp (float): keep records where temp_c >= min_temp
        max_temp (float): keep records where temp_c <= max_temp
    """

    result = data

    return result


def compute_stats(data: list) -> dict:
    """Compute aggregated statistics over the dataset.

    Returns a dict with keys: count, temp_c, humidity_pct.
    Each numeric key maps to a dict with min, max and avg values.
    """

    stats = {}

    return stats


def build_html(data: list) -> str:
    """Generate a valid HTML page containing a table of weather records."""

    html = ""

    return html


class WeatherHandler(BaseHTTPRequestHandler):
    """HTTP request handler for the weather REST API."""

    data = []  # shared dataset, loaded once at startup

    def do_GET(self):
        """Route incoming GET requests to the appropriate handler."""

        pass

    def handle_data(self, params: dict):
        """Handle GET /data with optional query string filters."""

        pass

    def handle_stats(self):
        """Handle GET /stats — return aggregated statistics as JSON."""

        pass

    def handle_html(self):
        """Handle GET /html — return a dynamic HTML page."""

        pass


def run_server(host: str, port: int, csv_path: Path):
    """Start the HTTP server and serve requests until interrupted."""

    WeatherHandler.data = load_data(csv_path)
    server = HTTPServer((host, port), WeatherHandler)
    print(f"Server running on http://{host}:{port}")
    server.serve_forever()


def main():
    """Entry point: load configuration and start the server."""

    base_dir = Path(__file__).parent
    config_path = base_dir / "config.ini"
    config = load_config(str(config_path))

    host = config["server"]["host"]
    port = int(config["server"]["port"])
    csv_path = Path(config["data"]["path"])

    run_server(host, port, csv_path)


if __name__ == "__main__":
    main()
