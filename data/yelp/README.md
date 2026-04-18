# DAMO-699 Capstone Project — Yelp Dataset

## Project Title
**Using Yelp Data to Estimate Business Demand and Identify Key Drivers for Location-Based Decision Support**

- Team: Sunghoon Ahn, Eun Soo Park, Thiri Htet Oo, Jayanthi Muthuselvan
- Program: Master's in Data Analytics, University of Niagara Falls, Canada
- Course: DAMO-699-1 Capstone Project
- Advisor: Touraj BaniRostam

---

## 1. Project Overview

The rapid growth of digital platforms has produced large-scale customer data — online reviews, ratings, and location-based activity. Prior work often relies on indirect indicators such as star ratings or sentiment scores, which do not fully capture real customer engagement or demand.

This project proposes a predictive analytics framework that integrates multiple Yelp data sources (reviews, business attributes, and check-in activity) to estimate business demand and identify the key drivers influencing customer behavior. Business demand is operationalized using customer check-in activity as a proxy for real-world engagement and visit frequency, with the goal of supporting more effective location-based decision-making.

### Objectives
- Develop predictive models that estimate business demand using Yelp data.
- Evaluate and compare the performance of different machine learning models.
- Identify the key drivers of business demand using model-based interpretation techniques.
- Examine how location and temporal factors influence variations in business demand.

---

## 2. Dataset

The project uses the **Yelp Open Dataset (April 2024)**, a publicly available large-scale dataset released for academic use under the Yelp Dataset User Agreement.

- Yelp Official: https://www.yelp.com/dataset/
- HuggingFace mirror: https://huggingface.co/datasets/adamamer20/yelp-04-2024

### Overview

| Item | Details |
|---|---|
| Name | Yelp Open Dataset (April 2024) |
| Total Size | ~10M records, ~9.2 GB uncompressed |
| Format | JSON Lines (converted to Parquet for large-scale processing) |
| License | Yelp Dataset User Agreement (academic use) |
| Integration Key | `business_id` |

### File Composition

| File | Records | Size | Role |
|---|---|---|---|
| `review.json`   | 6,990,280 | 5.3 GB | Textual feedback, star ratings, engagement metrics (useful/funny/cool), timestamps — used for sentiment, review volume, text features |
| `business.json` | 150,346   | 113 MB | Category, location (latitude/longitude), operational attributes — structural and location features |
| `checkin.json`  | 131,930   | 274 MB | Timestamped visit records — **target variable** (demand proxy via aggregated check-in count) |
| `tip.json`      | 908,915   | 172 MB | Optional supplementary short-text data |
| `user.json`     | 1,987,897 | 3.4 GB | Social-network information — excluded (out of scope) |

### Target Variable
**Aggregated check-in count per business**, derived from `checkin.json`, representing customer visit frequency.

### Data Access in this Repository
Due to the dataset's scale, processing is conducted in a cloud-based environment using a distributed framework (PySpark on Databricks), with data stored in Parquet format for efficient querying. A smaller subset is used locally for initial exploration and development.

- **Sample** (~50 MB): `data/yelp/sample/*.json` — committed for quick inspection.
- **Full dataset**: downloaded via `download_and_convert.py` into `data/yelp/raw/` and converted to Parquet in `data/yelp/parquet/`.

---

## 3. Data Analytics Pipeline

The project follows a structured data analytics pipeline.

### 3.1 Data Preprocessing
Data cleaning, handling missing values, merging datasets using the `business_id` key, and selecting relevant features.

### 3.2 Exploratory Data Analysis (EDA)
Demand distribution, review patterns, customer engagement trends, and check-in activity are examined to identify key patterns.

### 3.3 Feature Engineering
Raw data is transformed into modeling inputs across three groups:
- **Review-based features**: sentiment scores, review counts, text characteristics
- **Business features**: category, location, ratings
- **Temporal features**: peak hours, weekday vs. weekend patterns

### 3.4 Predictive Modeling

| Model | Role |
|---|---|
| Linear Regression | Baseline |
| Random Forest | Ensemble |
| Gradient Boosting | Ensemble |
| XGBoost | Structured data, nonlinear relationships |

Hyperparameter tuning is applied to improve performance.

### 3.5 Evaluation
Model performance is evaluated using **RMSE**, **MAE**, and **R²**. Cross-validation is used to ensure robustness and reduce overfitting, and models are compared to identify the best-performing approach.

### 3.6 Interpretation
Driver analysis is conducted using feature importance and model-based interpretation techniques to identify key factors influencing business demand and support location-based decision-making.

---

## 4. Expected Outcomes

- Models that accurately estimate business demand using large-scale Yelp data.
- Identification of key drivers of customer engagement across review-based, business, and temporal factors.
- Temporal patterns associated with high-demand businesses, such as peak activity periods.
- Findings that support data-driven decision-making for improving business operations and performance.

---

## 5. Analysis Tools

- **Python** — Pandas (preprocessing), Scikit-learn (modeling)
- **NLP techniques** — feature extraction from review text
- **PySpark on Databricks** — distributed processing for large-scale data
- **Parquet** — storage format for efficient querying and scalability

---

## 6. Data Folder Structure

```
data/yelp/
├── README.md                       # This file
├── create_sample.py                # Creates ~50 MB sample from full dataset
├── download_and_convert.py         # Downloads from HuggingFace, converts JSON → Parquet
├── sample/                         # Small JSON sample (committed to git)
│   ├── yelp_academic_dataset_business.json
│   ├── yelp_academic_dataset_checkin.json
│   ├── yelp_academic_dataset_review.json
│   ├── yelp_academic_dataset_tip.json
│   └── yelp_academic_dataset_user.json
├── raw/                            # Full JSON dataset (gitignored)
│   └── yelp_dataset/*.json
└── parquet/                        # Converted Parquet files (gitignored)
    └── *.parquet
```

### Reproducing the Dataset

```bash
# 1. Install dependencies
pip install huggingface_hub pandas pyarrow

# 2. Download full dataset and convert to Parquet
python data/yelp/download_and_convert.py

# 3. (Optional) Re-generate the small sample
python data/yelp/create_sample.py
