"""
DAMO-699 Capstone Project - Dataset Download & Parquet Conversion
=================================================================
Downloads Yelp Open Dataset (April 2024) from HuggingFace
and converts JSON files to Parquet format for Databricks upload.

Uses pandas + pyarrow (no Java/Spark required for local conversion).

Output structure (relative to script location):
    raw/yelp_dataset/*.json    <- downloaded JSON files
    parquet/*.parquet           <- converted Parquet files

Usage:
    pip install huggingface_hub pandas pyarrow
    python data/yelp/download_and_convert.py
"""

from huggingface_hub import hf_hub_download
import pandas as pd
import json
import os
import time

# ============================================================
# Configuration
# ============================================================
REPO_ID = "adamamer20/yelp-04-2024"

# All paths relative to this script's directory (data/yelp/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(SCRIPT_DIR, "raw", "yelp_dataset")
PARQUET_DIR = os.path.join(SCRIPT_DIR, "parquet")

FILES = [
    "yelp_dataset/yelp_academic_dataset_business.json",    # 113 MB
    "yelp_dataset/yelp_academic_dataset_review.json",       # 5.3 GB
    "yelp_dataset/yelp_academic_dataset_user.json",         # 3.4 GB
    "yelp_dataset/yelp_academic_dataset_tip.json",          # 172 MB
    "yelp_dataset/yelp_academic_dataset_checkin.json",      # 274 MB
]

# Large files are split into chunks to:
# 1. Avoid memory issues on local machine
# 2. Keep each parquet file under 500MB for Databricks UI upload (5GB limit per file)
CHUNK_SIZE = 500_000  # rows per chunk


# ============================================================
# Step 1: Download from HuggingFace
# ============================================================
def download_dataset():
    print("=" * 60)
    print("Step 1: Downloading from HuggingFace")
    print("=" * 60)

    for f in FILES:
        filename = os.path.basename(f)
        local_path = os.path.join(RAW_DIR, filename)

        if os.path.exists(local_path):
            print(f"  [SKIP] {filename} already exists")
            continue

        print(f"  [DOWNLOADING] {filename} ...")
        start = time.time()
        hf_hub_download(
            repo_id=REPO_ID,
            filename=f,
            repo_type="dataset",
            local_dir=os.path.join(SCRIPT_DIR, "raw"),
        )
        elapsed = time.time() - start
        print(f"  [DONE] {filename} ({elapsed:.1f}s)")

    print()


# ============================================================
# Step 2: Convert JSON to Parquet
# ============================================================
def read_json_lines(filepath, chunk_size):
    """Read JSON-lines file in chunks to avoid memory overflow."""
    chunk = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            chunk.append(json.loads(line))
            if len(chunk) >= chunk_size:
                yield pd.DataFrame(chunk)
                chunk = []
    if chunk:
        yield pd.DataFrame(chunk)


def convert_to_parquet():
    print("=" * 60)
    print("Step 2: Converting JSON to Parquet")
    print("=" * 60)

    os.makedirs(PARQUET_DIR, exist_ok=True)

    json_files = {
        "business": "yelp_academic_dataset_business.json",
        "review":   "yelp_academic_dataset_review.json",
        "user":     "yelp_academic_dataset_user.json",
        "tip":      "yelp_academic_dataset_tip.json",
        "checkin":  "yelp_academic_dataset_checkin.json",
    }

    for name, filename in json_files.items():
        json_path = os.path.join(RAW_DIR, filename)

        if not os.path.exists(json_path):
            print(f"  [SKIP] {filename} not found")
            continue

        print(f"  [CONVERTING] {name} ...")
        start = time.time()
        total_rows = 0
        part_idx = 0

        for chunk_df in read_json_lines(json_path, CHUNK_SIZE):
            rows_in_chunk = len(chunk_df)
            total_rows += rows_in_chunk

            part_path = os.path.join(
                PARQUET_DIR, f"{name}_part_{part_idx:03d}.parquet"
            )
            chunk_df.to_parquet(part_path, engine="pyarrow", index=False)

            file_size = os.path.getsize(part_path) / (1024 ** 2)
            print(f"    -> {name}_part_{part_idx:03d}.parquet "
                  f"({rows_in_chunk:,} rows, {file_size:.1f} MB)")
            part_idx += 1

        elapsed = time.time() - start
        print(f"  [DONE] {name}: {total_rows:,} rows total, "
              f"{part_idx} file(s) ({elapsed:.1f}s)")
        print()


# ============================================================
# Step 3: Summary
# ============================================================
def print_summary():
    print("=" * 60)
    print("Step 3: Parquet File Summary")
    print("=" * 60)

    total_size = 0
    for f in sorted(os.listdir(PARQUET_DIR)):
        if f.endswith(".parquet"):
            path = os.path.join(PARQUET_DIR, f)
            size = os.path.getsize(path)
            total_size += size
            print(f"  {f:45s} {size / (1024**2):>8.1f} MB")

    print(f"  {'':45s} {'─' * 10}")
    print(f"  {'TOTAL':45s} {total_size / (1024**3):>8.2f} GB")
    print()
    print("Next steps:")
    print("  1. Upload parquet files to Databricks Volume")
    print("     /Volumes/workspace/yelp/data/")
    print("  2. Load in Databricks notebook:")
    print('     df_review = spark.read.parquet("/Volumes/workspace/yelp/data/review_part_*.parquet")')
    print('     df_business = spark.read.parquet("/Volumes/workspace/yelp/data/business_part_000.parquet")')


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    download_dataset()
    convert_to_parquet()
    print_summary()
