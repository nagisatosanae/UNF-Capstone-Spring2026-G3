# Capstone Project  
## Usage-Driven Demand and Revenue Forecasting using Large-Scale Event Data

---

## 1. Project Overview  

This project aims to build a data-driven forecasting and decision model using large-scale event data.

The core objectives are:
- Predict demand patterns  
- Estimate revenue  
- Support operational and strategic decisions  

Although the dataset originates from an urban transportation domain, the analytical framework is designed to simulate industrial aftermarket demand and revenue behavior.

---

## 2. Business Context (Industrial Interpretation)

In industrial environments:

- Equipment usage → Component wear  
- Wear → Maintenance / replacement  
- Replacement → Revenue generation  

This project models that structure using event-based data.

### Mapping Logic

| Taxi Data | Industrial Interpretation |
|----------|--------------------------|
| Trip occurrence | Equipment usage |
| Trip frequency | Operating intensity |
| Distance / duration | Wear proxy |
| Repeated trips | Replacement cycle |
| Fare amount | Revenue |
| High-demand zones | High-value customers |

Key idea:

This dataset is used as a proxy to simulate usage-driven demand behavior, which is the dominant mechanism behind industrial aftermarket revenue.

---

## 3. Dataset Description  

Source: NYC Taxi and Limousine Commission (TLC)

Dataset: NYC Yellow Taxi Trip Data (January 2023)

### Data Characteristics

- Rows: ~3,066,766  
- Features: 19  
- Format: Parquet (columnar, compressed)  

---
## Data Source  

The dataset used in this project is publicly available from the NYC Taxi and Limousine Commission (TLC).

Official page:  
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page  

Direct download link (January 2023):  
https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet  

---

## Data Access  

Due to environment constraints, the full dataset is not stored in this repository.

Instead:

- Full dataset is processed in Databricks  
- A sample dataset (100,000 rows) is provided for quick testing  

---

## How to Reproduce  

To reproduce the dataset:

1. Download the parquet file from the link above  
2. Load into Databricks or a Python environment  

Example:

```python
import pandas as pd

df = pd.read_parquet("yellow_tripdata_2023-01.parquet")
```

Or using Spark:

```python
df = spark.read.parquet("path_to_file")
```

---

## Notes  

- The original dataset contains millions of rows  
- The parquet format is compressed and optimized for large-scale processing  
- Only a subset is included in this repository for convenience  
---

## 4. Sample Data  

Included in this repository:

data/taxi_sample_100k.csv

- 100,000 rows subset  
- Provided for quick access and reproducibility  

---

## 5. Full Dataset Location  

The full dataset is stored and processed in Databricks:

/Volumes/workspace/default/capston/

Due to size limitations, it is not included in this repository.

---

## 6. Data Structure  

### Key Features

Time  
- tpep_pickup_datetime  
- tpep_dropoff_datetime  

Usage Proxy  
- trip_distance  
- passenger_count  

Location  
- PULocationID  
- DOLocationID  

Revenue  
- fare_amount  
- tip_amount  
- total_amount  

---

## 7. Data Processing  

Steps:

1. Data loading (Parquet → Spark DataFrame)  
2. Schema validation  
3. Basic filtering (invalid values removal)  
4. Feature engineering  

---

### Engineered Features (Planned)

- pickup_hour  
- day_of_week  
- trip_duration  
- average_speed  
- demand intensity metrics  

---

## 8. Project Objectives  

### Technical Objectives

- Handle large-scale data (millions of rows)  
- Perform feature engineering  
- Build predictive models  

---

### Business Objectives

- Demand forecasting  
- Revenue estimation  
- Operational optimization  

---

## 9. Modeling Plan  

### Machine Learning Models

- Linear Regression (baseline)  
- Random Forest  
- Gradient Boosting (XGBoost)  

---

### Deep Learning (Optional)

- LSTM (time-series forecasting)  
- Feedforward neural networks  

---

### Target Problems

1. Demand prediction  
   - Trips per hour / location  

2. Revenue prediction  
   - Expected fare / total revenue  

3. Pattern detection  
   - High-demand time windows  
   - High-value zones  

---

## 10. Expected Outputs  

- Demand forecast (time-based)  
- Revenue estimation  
- Feature importance analysis  
- Operational recommendations  

---

## 11. Limitations  

### Data Limitations

- Not actual industrial data  
- No explicit maintenance or failure records  
- No customer-level contract data  

---

### Modeling Limitations

- Usage is inferred, not physically measured  
- Revenue is transactional, not lifecycle-based  

---

### Interpretation Limitation

This dataset represents behavioral demand, while industrial systems are driven by physical degradation.

---

## 12. Justification  

Despite domain differences, both systems share a common structure:

usage → demand → revenue  

Therefore, large-scale event data can approximate:
- Demand patterns  
- Replacement cycles  
- Revenue generation behavior  

---

## 13. Tools and Environment  

- Databricks (Spark)  
- Python (pandas, PySpark)  
- GitHub  

---

## 14. Future Work  

- Integrate multiple months of data  
- Advanced feature engineering  
- Anomaly detection  
- Optimization models  
- Dashboard (Power BI / Tableau)  

---

## 15. Conclusion  

This project demonstrates how large-scale event data can be transformed into a decision-support system.

The methodology is transferable to industrial domains, especially:
- Aftermarket services  
- Maintenance planning  
- Revenue forecasting  

---

## Note  

Full dataset is processed in Databricks due to size constraints.  
Only a sample is provided for reproducibility and evaluation.
