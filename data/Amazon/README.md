# UNF-Capstone-Spring2026


# Customer Sentiment Intelligence and Product Performance Analytics using Amazon Reviews

---

## 1. Problem Definition

This project aims to analyze large-scale Amazon review data to understand customer sentiment, product performance, and customer satisfaction using data analytics and natural language processing (NLP).

### Goal of the Project
The goal is to:
- Extract sentiment from customer reviews
- Identify patterns in product performance
- Build predictive models to classify customer sentiment

### Decision Supported
This project supports:
- Product improvement decisions
- Customer satisfaction strategies
- Market positioning and product quality enhancement

### Importance of the Problem
Customer reviews play a critical role in influencing purchasing decisions. Understanding customer sentiment helps businesses:
- Improve product quality
- Reduce negative feedback
- Increase customer retention and satisfaction

---

## 2. Dataset

### Source of Data
- Amazon Reviews Dataset (amazon_reviews_500k.csv)

### Number of Samples and Features
- Records: ~500,000
- Features:
  - product_id
  - user_id
  - rating
  - review_text
  - review_time
  - verified_purchase
  - helpfulness_score

### Target Variable
- Sentiment (derived from review text)
- Rating (used as supporting variable)

### Data Limitations
- Reviews are subjective and may contain bias
- Presence of noisy and unstructured text
- No direct sales or revenue data
- Possible fake or manipulated reviews

---

## 3. Data Preprocessing

The dataset was prepared using the following steps:

### Missing Value Handling
- Removed null and incomplete records
- Filled missing categorical values where necessary

### Encoding Techniques
- Label encoding for categorical variables
- Conversion of text into numerical format using TF-IDF

### Feature Selection / Engineering
- Extracted sentiment scores using NLP
- Created sentiment labels (positive, neutral, negative)
- Generated time-based features (year, month)
- Created text-based features (word count, review length)

---

## 4. Exploratory Data Analysis (EDA)

EDA was conducted to identify patterns and relationships in the data.

### Important Patterns
- Majority of reviews are positive
- Certain products receive significantly more reviews
- Customer activity varies over time

### Correlations
- Positive correlation between rating and sentiment
- Higher review frequency indicates higher product popularity

### Visualizations
- Rating distribution histogram
- Sentiment distribution bar chart
- Time-series plots of reviews
- Top products by review count

---

## 5. Modeling Approach

### Models Selected
- Logistic Regression (baseline model)
- Random Forest (improved model)
- Gradient Boosting (advanced model)

### Why These Models
- Logistic Regression provides a simple baseline
- Random Forest improves accuracy and handles non-linearity
- Gradient Boosting enhances performance for complex patterns

### Baseline vs Improved Models
- Baseline: Logistic Regression
- Improved Models: Random Forest and Gradient Boosting

---

## 6. Evaluation

### Metrics Used
- Accuracy
- Precision
- Recall
- F1-score

### Model Performance Comparison
- Logistic Regression provided moderate accuracy
- Random Forest improved classification performance
- Gradient Boosting achieved the best results in capturing sentiment patterns

---

## 7. Results & Insights

### Key Learnings
- Most customers express positive sentiment
- Negative reviews highlight recurring product issues
- Sentiment analysis provides deeper insights beyond ratings

### Insights Discovered
- High-rated products generally have positive sentiment
- Some products show mismatches between rating and sentiment
- Customer feedback reveals specific product improvement areas

---

## 8. Recommendations

### Actionable Recommendations
- Improve products with consistent negative sentiment
- Use sentiment analysis for real-time customer feedback monitoring
- Focus marketing on high-performing products
- Address recurring issues identified in reviews

### Business Impact
- Improved product quality
- Better customer satisfaction
- Enhanced decision-making using data-driven insights

---

## 9. Project Structure

