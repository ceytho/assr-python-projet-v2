#!/usr/bin/env python3

from pathlib import Path

import boto3


def load_config(config_path: str = "") -> dict:
    """Parse a config file and return a dict with configuration values."""

    config_dict = {}

    return config_dict


def create_s3_client():
    """Create and return a boto3 S3 client configured for anonymous access.

    Pour accéder à un bucket public sans credentials AWS, utiliser :
        from botocore import UNSIGNED
        from botocore.config import Config
        Config(signature_version=UNSIGNED)
    """

    client = None

    return client


def download_csv(client, bucket: str, key: str) -> list:
    """Download a CSV file from S3 and return its content as a list of dicts.
    """

    records = []

    return records


def clean_records(records: list) -> list:
    """Convert numeric fields and replace missing values (9999.9) with None."""

    cleaned = []

    return cleaned


def filter_records(records: list, filters: dict) -> list:
    """Keep only records whose TEMP field falls within [min_temp_f, max_temp_f]."""

    result = records

    return result


def generate_report(records: list) -> dict:
    """Compute processing statistics and return them as a dict."""

    report = {}

    return report


def export_csv(records: list, output_path: Path) -> None:
    """Write processed records to a CSV file with a semicolon separator.

    The file must include a header row and use UTF-8 encoding.
    """

    pass


def main():
    """Entry point: load configuration, process files and write outputs."""

    base_dir = Path(__file__).parent
    config_path = base_dir / "config.ini"
    config = load_config(str(config_path))

    bucket = config["s3"]["bucket"]
    keys = [k.strip() for k in config["s3"]["keys"].split(",")]
    filters = {
        "min_temp_f": float(config["filter"]["min_temp_f"]),
        "max_temp_f": float(config["filter"]["max_temp_f"]),
    }
    csv_path = Path(config["output"]["csv_path"])
    report_path = Path(config["output"]["report_path"])

    client = create_s3_client()
    all_records = []

    for key in keys:
        records = download_csv(client, bucket, key)
        all_records.extend(records)

    cleaned = clean_records(all_records)
    filtered = filter_records(cleaned, filters)

    export_csv(filtered, csv_path)

    report = generate_report(filtered)


if __name__ == "__main__":
    main()
