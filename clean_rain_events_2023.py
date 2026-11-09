"""Clean and validate a 2023 monthly rainfall-events CSV.

Usage:
    python clean_rain_events_2023.py path/to/rain_events_2023.csv path/to/output_folder

Requires: pandas
"""

import argparse
from pathlib import Path

import pandas as pd

MONTH_MAP = {
    "jan": 1, "january": 1,
    "feb": 2, "february": 2,
    "mar": 3, "march": 3,
    "apr": 4, "april": 4,
    "may": 5,
    "jun": 6, "june": 6,
    "jul": 7, "july": 7,
    "aug": 8, "august": 8,
    "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10,
    "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}


def clean_rain_events(input_csv: Path, output_folder: Path) -> Path:
    """Standardize months, verify all 12 months, and save a cleaned CSV."""
    rain_df = pd.read_csv(input_csv)
    print("Original rain-events table:")
    print(rain_df)

    if "month" not in rain_df.columns:
        raise ValueError("Input CSV must contain a 'month' column.")

    rain_df["month"] = (
        rain_df["month"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(MONTH_MAP)
    )

    if rain_df["month"].isna().any():
        raise ValueError("Some month names could not be converted.")

    if sorted(rain_df["month"].astype(int).tolist()) != list(range(1, 13)):
        raise ValueError("Rain-events table must contain each month from 1 to 12 exactly once.")

    rain_df["month"] = rain_df["month"].astype(int)
    rain_df = rain_df.sort_values("month")

    output_folder.mkdir(parents=True, exist_ok=True)
    output_csv = output_folder / "rain_events_2023_fixed.csv"
    rain_df.to_csv(output_csv, index=False)

    print("\nCorrected rain-events table:")
    print(rain_df)
    print("\nSaved to:", output_csv)
    return output_csv


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", type=Path, help="Path to original 2023 rain-events CSV")
    parser.add_argument("output_folder", type=Path, help="Folder for cleaned CSV")
    args = parser.parse_args()
    clean_rain_events(args.input_csv, args.output_folder)


if __name__ == "__main__":
    main()
