#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import httpx


def load_config(config_path: str = "") -> dict:
    """Parse a config file and return a dict object with values."""

    config_dict = {}

    return config_dict


def load_packages(db_path: Path, driver: str) -> list:
    """Parse package catalogue and return content as a list of dict."""

    data = []

    return data


def check_vulnerabilities(api_url: str, package: str, version: str) -> int:
    """Check package version against OSV API and return vulnerability count."""

    count = 0

    return count


def export_csv(packages: list, api_url: str, output_path: Path) -> None:
    """Check each package against OSV API and write results to a CSV file."""

    pass


class AuditHandler(BaseHTTPRequestHandler):
    """HTTP request handler for the audit server."""

    def do_GET(self):
        """Handle GET requests for /audit and /health routes."""

        pass


def run_server(host: str, port: int, packages: list, api_url: str) -> None:
    """Start the HTTP server and serve audit results on the given host:port."""

    pass


def main():
    """Check each package against OSV API and output results."""

    base_dir = Path(__file__).parent
    config_path = base_dir / "config.ini"
    config = load_config(str(config_path))

    packages = load_packages(config["db"]["path"], config["db"]["driver"])
    mode = config["app"]["mode"]

    if mode == "stdout":
        for pkg in packages:
            count = check_vulnerabilities(
                config["api"]["url"], pkg["package"], pkg["version"]
            )
    elif mode == "csv":
        export_csv(packages, config["api"]["url"], Path(config["output"]["path"]))
    elif mode == "server":
        run_server(
            config["server"]["host"],
            int(config["server"]["port"]),
            packages,
            config["api"]["url"],
        )


if __name__ == "__main__":
    main()
