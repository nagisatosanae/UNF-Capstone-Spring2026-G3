# UNF-Capstone-Spring2026

## 1. Problem Definition

This dataset is being considered for a capstone project focused on mortgage lending analytics. The problem is to understand which borrower, loan, and geographic factors may be associated with mortgage application outcomes.

The goal of the project is to analyze mortgage lending patterns and determine whether a sample of mortgage application data can be used for exploratory analysis and possible predictive modeling of approval and denial outcomes.

This project supports decision-making in lending analytics, mortgage market analysis, and policy review. It can help identify patterns in mortgage approvals and denials across different applicant and loan characteristics.

This problem is important because mortgage decisions affect access to housing, credit, and long-term financial stability. Studying lending patterns can improve transparency and provide useful insights for banking and finance-related analysis.

---

## 2. Dataset

The dataset used in this folder is based on the **Home Mortgage Disclosure Act (HMDA) Loan/Application Records (LAR)** dataset.

- **Source of data:**  
  FFIEC / CFPB HMDA Data  
  Official source: https://ffiec.cfpb.gov/data-publication/snapshot-national-loan-level-dataset/2024

- **Number of samples and features:**  
  The original 2024 HMDA dataset contains millions of mortgage application records and many variables related to applicant demographics, loan characteristics, property information, lender identifiers, and geography. This folder contains a sample CSV version prepared for dataset review and initial project exploration.

- **Target variable (if applicable):**  
  A likely target variable for future modeling is `action_taken`, which can be used to study mortgage application outcomes such as approved/originated versus denied.

- **Data limitations:**  
  - This folder contains a sample of the original HMDA dataset, not the full dataset.
  - Some fields may contain missing, exempt, or not-applicable values.
  - Some variables may require recoding before analysis.
  - Sensitive demographic variables must be interpreted carefully.
  - Results based on the sample may not fully represent the complete dataset.

---

## 3. Data Preprocessing

*(To be implemented)*

Planned preprocessing steps include:

- **Missing value handling:**  
  Missing, exempt, and not-applicable values will be reviewed and handled based on the meaning of each variable.

- **Encoding techniques:**  
  Categorical variables such as loan type, loan purpose, race, ethnicity, sex, and occupancy type may be encoded into analysis-ready format if modeling is performed.

- **Feature selection or engineering:**  
  Relevant variables will be selected based on the final research question. Additional features may be created later, such as grouped mortgage outcome categories.

---

## 4. Exploratory Data Analysis (EDA)

*(To be implemented)*

The exploratory analysis is expected to focus on mortgage lending patterns in the HMDA data.

- **Important patterns:**  
  Potential patterns to explore include differences in mortgage outcomes by income, loan amount, loan purpose, geography, and applicant characteristics.

- **Correlations:**  
  Relationships among numeric variables such as loan amount, property value, and income may be examined.

- **Visualizations:**  
  Planned visualizations include bar charts, histograms, boxplots, count plots, and heatmaps.

---

## 5. Modeling Approach

*(To be implemented)*

This dataset may be used for classification modeling of mortgage application outcomes.

- **Which models were selected?**  
  Possible models include Logistic Regression, Decision Tree, Random Forest, and XGBoost.

- **Why were these models chosen?**  
  These models are suitable for structured tabular data and can support both baseline and more advanced predictive analysis.

- **Baseline vs improved models:**  
  A baseline model would likely be built first, followed by improved models after preprocessing, feature selection, and tuning.

---

## 6. Evaluation

*(To be implemented)*

If modeling is performed, the evaluation will be based on common classification metrics.

- **Metrics used:**  
  Accuracy, Precision, Recall, F1-score, and ROC-AUC if applicable.

- **Model performance comparison:**  
  Model performance would be compared to determine which approach best fits the project objective.

---

## 7. Results & Insights

*(To be implemented)*

This section will be completed after the data analysis and modeling stages.

- **What did you learn?**  
  The project is expected to identify key factors associated with mortgage application outcomes.

- **What insights were discovered?**  
  Final insights may include lending patterns across borrower groups, loan types, and geographic areas.

---

## 8. Recommendations

*(To be implemented)*

This section will provide recommendations after the final results are available.

- **What should be done based on your results?**  
  Possible recommendations may include deeper review of lending trends, analysis of approval and denial patterns, and further investigation of important variables.

- **Business or real-world impact:**  
  This dataset has potential value for finance, banking, and policy-related analytics because it supports the study of mortgage lending behavior using public data.

---

## 9. Project Structure

```bash
hmda/
├── README.md
└── hmda_2024_sample.csv
