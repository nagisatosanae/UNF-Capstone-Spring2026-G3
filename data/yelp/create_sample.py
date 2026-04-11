"""
DAMO-699 Capstone Project - Create Sample Dataset
==================================================
Extracts a small subset from the full Yelp JSON files,
preserving the original file structure and format.

Generates ~50MB of sample data for git-friendly sharing.

Output structure (relative to script location):
    sample/*.json

Usage:
    python data/yelp/create_sample.py

Input:  raw/yelp_dataset/*.json  (full dataset)
Output: sample/*.json            (small subset)
"""

import json
import os

# ============================================================
# Configuration
# ============================================================

# All paths relative to this script's directory (data/yelp/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(SCRIPT_DIR, "raw", "yelp_dataset")
SAMPLE_DIR = os.path.join(SCRIPT_DIR, "sample")

# Number of rows to extract per file (~50MB total)
SAMPLE_SIZES = {
    "yelp_academic_dataset_review.json": 50_000,     # ~38 MB
    "yelp_academic_dataset_business.json": 10_000,    # ~7 MB
    "yelp_academic_dataset_user.json": 5_000,         # ~3 MB
    "yelp_academic_dataset_tip.json": 5_000,          # ~1 MB
    "yelp_academic_dataset_checkin.json": 5_000,       # ~1 MB
}


# ============================================================
# Main
# ============================================================
def create_samples():
    os.makedirs(SAMPLE_DIR, exist_ok=True)

    total_size = 0

    for filename, n_rows in SAMPLE_SIZES.items():
        input_path = os.path.join(RAW_DIR, filename)
        output_path = os.path.join(SAMPLE_DIR, filename)

        if not os.path.exists(input_path):
            print(f"  [SKIP] {filename} not found in {RAW_DIR}")
            continue

        print(f"  [SAMPLING] {filename} -> {n_rows:,} rows ...")

        count = 0
        with open(input_path, "r", encoding="utf-8") as fin, \
             open(output_path, "w", encoding="utf-8") as fout:
            for line in fin:
                if count >= n_rows:
                    break
                # Validate JSON and write as-is (preserves original format)
                json.loads(line)
                fout.write(line)
                count += 1

        file_size = os.path.getsize(output_path)
        total_size += file_size
        print(f"  [DONE]     {filename}: {count:,} rows, {file_size / (1024**2):.1f} MB")

    print()
    print(f"  {'=' * 50}")
    print(f"  Total sample size: {total_size / (1024**2):.1f} MB")
    print(f"  Output directory:  {SAMPLE_DIR}")
    print()
    print("  These files have the same JSON-lines format as the originals.")
    print("  Safe to push to git (under GitHub's 100MB per-file limit).")


if __name__ == "__main__":
    print("=" * 55)
    print("Creating sample dataset (~50MB)")
    print("=" * 55)
    create_samples()
