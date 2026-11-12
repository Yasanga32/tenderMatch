"""Preprocess raw tender responses into clean datasets."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"


def preprocess() -> None:
    """Clean and transform raw tender data into data/processed/."""
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    # TODO: Implement preprocessing logic


if __name__ == "__main__":
    preprocess()

