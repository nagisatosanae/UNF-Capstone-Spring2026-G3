# DAMO-699 Capstone Project - Topic & Dataset Summary
## Topic: Key Factors in Online Review Text That Impact Business Ratings

### Problem Statement
> "This project investigates which textual factors in online reviews most significantly influence business ratings. By applying sentiment analysis and topic modeling to large-scale Yelp review data, we aim to identify the key drivers of customer satisfaction across different business categories, providing actionable insights for business owners and platform designers."

### Business Relevance
- Online reviews influence 93% of consumer purchasing decisions (BrightLocal Survey)
- Star ratings alone do not capture the nuanced factors driving customer satisfaction
- Understanding which aspects (service, price, quality, ambiance) matter most per industry helps businesses prioritize improvements
- Insights can inform recommendation algorithms and review summarization features on platforms

---

## Intended Research Direction

We plan to explore what textual factors in online reviews most significantly influence business ratings. Specific hypotheses, research questions, and methodology will be refined after the literature review and initial data exploration.

---

## Dataset: Yelp Open Dataset (April 2024)

| Item | Details |
|---|---|
| **Name** | Yelp Open Dataset (April 2024) |
| **Yelp Official** | https://www.yelp.com/dataset/ |
| **HuggingFace** | https://huggingface.co/datasets/adamamer20/yelp-04-2024 |
| **Total Size** | ~10M records, ~4.4 GB compressed / **~9.2 GB** uncompressed |
| **License** | Yelp Dataset User Agreement |
| **Access** | Free (download via HuggingFace) |

### Data Composition (6 JSON Files)

| File | Records | Size | Key Columns |
|---|---|---|---|
| `review.json` | 6,990,280 | 5.3 GB | review_id, user_id, business_id, **stars**, date, **text**, useful, funny, cool |
| `user.json` | 1,987,897 | 3.4 GB | user_id, name, review_count, yelping_since, **friends** (social graph), fans, elite, average_stars, compliment_* |
| `business.json` | 150,346 | 113 MB | business_id, name, address, city, state, **latitude/longitude**, **stars**, review_count, **categories**, attributes, hours |
| `tip.json` | 908,915 | 172 MB | text, date, compliment_count, business_id, user_id |
| `checkin.json` | 131,930 | 274 MB | business_id, date (check-in timestamps) |
| `photo.json` | 200,100 | - | photo_id, business_id, caption, label |

### Files Used for This Project

| File | Role in Project | Hypothesis |
|---|---|---|
| **`review.json`** | Primary data source -- review `text` for NLP analysis, `stars` as target variable | H1, H2, H3 |
| **`business.json`** | Join key for `categories` to enable cross-industry comparison | H3 |
| `tip.json` | Optional supplementary text data | - |
| `user.json` | Not used (social graph not in scope) | - |
| `checkin.json` | Not used | - |

### Rationale: Why This Dataset Is Suitable for the Capstone

**Alignment with Research Direction**
1. **Text + Rating Paired Data**: Each of the 6.9M reviews contains both free-text (`text`) and a numeric rating (`stars` 1-5). This direct pairing is essential for studying the relationship between review content and ratings -- no external labeling or annotation is needed.
2. **Multi-Category Coverage**: `business.json` contains 150K businesses across diverse categories (Restaurants, Shopping, Health, Home Services, Automotive, etc.), enabling cross-industry comparison of what textual factors matter most in different sectors.

**Scale & Technical Justification**
3. **Big Data Scale**: At 5.3 GB of review text alone (~9.2 GB total uncompressed), this dataset exceeds the capacity of local tools like pandas, justifying the use of PySpark and Databricks -- a core requirement for demonstrating big data competency in the capstone.
4. **Parquet-Ready**: JSON structure converts cleanly to columnar Parquet format, enabling efficient querying in Spark (read only needed columns, predicate pushdown, compression).

**Academic & Ethical Suitability**
5. **Strong Academic Foundation**: The Yelp Dataset has been used in hundreds of peer-reviewed papers through the Yelp Dataset Challenge. This extensive prior work provides a solid base for the literature review and ensures the dataset is recognized as credible in academic contexts.
6. **Ethical Compliance**: Publicly released by Yelp specifically for academic/educational use under their Dataset User Agreement. No web scraping or unauthorized data collection is involved, satisfying TCPS 2 (CORE-2022) ethical research requirements.

**Practical Advantages**
7. **Clean and Well-Structured**: Official dataset with consistent schema, minimal missing values, and well-documented fields -- reducing preprocessing overhead and allowing focus on analysis.
8. **Temporal Depth**: Reviews span multiple years, providing robust sample sizes across categories and time periods for reliable statistical analysis.

---

## Planned Technical Environment

- **Platform**: Considering a cloud-based analytics platform; currently evaluating Databricks Free Edition (PySpark + SQL) as a primary candidate
- **Processing**: PySpark for large-scale text preprocessing and analysis
- **Storage**: Parquet files uploaded to cloud storage (e.g., Databricks Unity Catalog Volumes)
- **Analysis Tools**: To be determined after methodology is finalized

---

## Full Dataset Download & Parquet Conversion

### Download (HuggingFace Hub)

```python
pip install huggingface_hub

from huggingface_hub import hf_hub_download

files = [
    'yelp_dataset/yelp_academic_dataset_business.json',    # 113 MB
    'yelp_dataset/yelp_academic_dataset_review.json',       # 5.3 GB
    'yelp_dataset/yelp_academic_dataset_user.json',         # 3.4 GB
    'yelp_dataset/yelp_academic_dataset_tip.json',          # 172 MB
    'yelp_dataset/yelp_academic_dataset_checkin.json',      # 274 MB
]

for f in files:
    hf_hub_download(
        repo_id='adamamer20/yelp-04-2024',
        filename=f,
        repo_type='dataset',
        local_dir='./data'
    )
```

### Parquet Conversion

See `download_and_convert.py` for the full pipeline script.

**Usage:**
```bash
pip install huggingface_hub pandas pyarrow
python code/download_and_convert.py
```

This script automatically:
1. Downloads all 5 JSON files from HuggingFace to `data/raw/` (skips if already downloaded)
2. Converts each JSON to Parquet format in `data/parquet/`
3. Splits large files (review, user) into ~500K-row parts for easier upload
4. Prints a summary of all generated Parquet files with sizes

---

## Sample Data (`data/sample/`)

The full dataset (~9.2 GB) is too large for GitHub (100MB per-file limit). Instead, a **small sample subset (~50MB)** is included in `data/sample/` for quick reference.

| File | Full Records | Sample Records | Sample Size |
|---|---|---|---|
| `review.json` | 6,990,280 | 50,000 | ~38 MB |
| `business.json` | 150,346 | 10,000 | ~7 MB |
| `user.json` | 1,987,897 | 5,000 | ~3 MB |
| `tip.json` | 908,915 | 5,000 | ~1 MB |
| `checkin.json` | 131,930 | 5,000 | ~1 MB |

- Same file names, same JSON-lines format, same columns as the originals
- Generated by `create_sample.py`
- To regenerate: `python code/create_sample.py`
- For the full dataset, run `download_and_convert.py`

### Output Directories

All scripts output to the project root `data/` directory regardless of where they are executed:

```
data/
├── raw/yelp_dataset/   <- download_and_convert.py (Step 1: download)
├── parquet/            <- download_and_convert.py (Step 2: convert)
└── sample/             <- create_sample.py
```

**Dataset Source Links:**
- Yelp Official: https://www.yelp.com/dataset/
- HuggingFace: https://huggingface.co/datasets/adamamer20/yelp-04-2024
