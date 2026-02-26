#!/usr/bin/env python3

from pathlib import Path


def load_config(config_path: str = "") -> dict:
    """Parse a config file and return a dict with configuration values."""

    config_dict = {}

    return config_dict


def download_page(url: str, timeout: int = 10) -> str:
    """Download the HTML content of a page and return it as a string.

    Raises an exception if the HTTP request fails
    """

    html = ""

    return html


def parse_books(html: str) -> list:
    """Parse an HTML page from books.toscrape.com and extract book records.

    Each record must be a dict containing:
        title (str), price (str), rating (int), availability (str), url (str).

    The rating is encoded as a CSS class on the star element:
        "One", "Two", "Three", "Four", "Five" -> convert to integer
    """

    data = []

    return data


def export_csv(data: list, output_path: Path) -> None:
    """Write the list of book records to a CSV file with a semicolon separator.

    The file must include a header row and use UTF-8 encoding.
    Columns : title, price, rating, availability, url.
    """

    pass


def main():
    """Entry point: load configuration, scrape pages and export results."""

    base_dir = Path(__file__).parent
    config_path = base_dir / "config.ini"
    config = load_config(str(config_path))

    start_url = config["scraper"]["start_url"]
    base_url = config["scraper"]["base_url"]
    max_pages = int(config["scraper"]["max_pages"])
    timeout = int(config["scraper"]["timeout"])
    output_path = Path(config["output"]["path"])

    all_books = []
    url = start_url
    page = 1
    while url and page <= max_pages:
        html = download_page(url, timeout)
        books = parse_books(html)
        all_books.extend(books)
        print(f"Page {page}/{max_pages} : {len(books)} livres récupérés")
        page += 1

    export_csv(all_books, output_path)


if __name__ == "__main__":
    main()
