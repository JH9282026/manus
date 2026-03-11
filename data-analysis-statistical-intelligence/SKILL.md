---
name: "data-analysis-statistical-intelligence"
description: "Execute comprehensive statistical analysis, predictive modeling, hypothesis testing, machine learning, and data visualization to extract actionable insights from any dataset. Use for: exploratory data analysis, descriptive/inferential statistics, regression, classification, clustering, time series forecasting, A/B testing, data cleaning, feature engineering, and dashboard creation."
---

# Data Analysis & Statistical Intelligence

Autonomously analyze datasets of any complexity, extract meaningful insights, build predictive models, and deliver actionable recommendations.

## Overview

Encompass the complete data science lifecycle from initial exploration through advanced machine learning and statistical inference to visualization and reporting. Apply appropriate statistical tests, build predictive models, and communicate findings effectively.

## Analysis Type Selection

| Analysis Goal | Methods | Tools |
|--------------|---------|-------|
| Understand distributions | Descriptive stats, histograms, box plots | Pandas, Matplotlib |
| Find relationships | Correlation, regression, scatter plots | Scipy, Statsmodels |
| Compare groups | t-tests, ANOVA, chi-square | Scipy, Statsmodels |
| Predict outcomes | Regression, classification, ensemble models | Scikit-learn, XGBoost |
| Find segments | K-means, hierarchical, DBSCAN | Scikit-learn |
| Forecast time series | ARIMA, Prophet, exponential smoothing | Statsmodels, Prophet |
| Reduce dimensions | PCA, t-SNE, UMAP | Scikit-learn |
| Detect anomalies | Isolation Forest, LOF, Z-score | Scikit-learn, PyOD |

## Statistical Test Selection Guide

| Data Type | Groups | Distribution | Recommended Test |
|-----------|--------|-------------|-----------------|
| Continuous | 2 independent | Normal | Independent t-test |
| Continuous | 2 paired | Normal | Paired t-test |
| Continuous | 2 independent | Non-normal | Mann-Whitney U |
| Continuous | 3+ independent | Normal | One-way ANOVA |
| Continuous | 3+ independent | Non-normal | Kruskal-Wallis |
| Categorical | 2 categories | N/A | Chi-square / Fisher exact |
| Continuous | Correlation | Normal | Pearson correlation |
| Continuous | Correlation | Non-normal | Spearman correlation |
| Continuous | Prediction | Linear relationship | Linear regression |
| Binary | Prediction | N/A | Logistic regression |

## Data Quality Assessment Checklist

| Dimension | Check | Action |
|-----------|-------|--------|
| Completeness | % missing per column | Impute (mean/median/KNN) or drop |
| Accuracy | Outlier detection (IQR/Z-score) | Cap, transform, or remove |
| Consistency | Duplicate records | Deduplicate |
| Validity | Values within expected ranges | Flag and investigate |
| Timeliness | Data freshness | Verify recency |
| Uniqueness | Primary key violations | Resolve conflicts |

## ML Model Selection Framework

| Problem Type | Small Data (<1K) | Medium (1K-100K) | Large (>100K) |
|-------------|-----------------|-------------------|---------------|
| Classification | Logistic Reg, KNN | Random Forest, SVM | XGBoost, Neural Net |
| Regression | Linear Reg, Ridge | Random Forest, SVR | XGBoost, LightGBM |
| Clustering | K-Means, Hierarchical | DBSCAN, GMM | Mini-batch K-Means |
| Time Series | Exp Smoothing | ARIMA, Prophet | LSTM, Transformer |

## Model Evaluation Metrics

| Task | Metric | Use When |
|------|--------|----------|
| Classification | Accuracy | Balanced classes |
| Classification | F1-Score | Imbalanced classes |
| Classification | AUC-ROC | Ranking/threshold tuning |
| Regression | RMSE | Penalize large errors |
| Regression | MAE | Robust to outliers |
| Regression | R² | Explain variance |
| Clustering | Silhouette Score | Compare cluster quality |
| Clustering | Elbow Method | Choose k |

## Using the Reference Files

### When to Read Each Reference

**`/references/statistical-methods-testing.md`** — Read when performing hypothesis tests, calculating confidence intervals, selecting statistical tests, or interpreting p-values and effect sizes.

**`/references/ml-predictive-modeling.md`** — Read when building classification, regression, or clustering models, performing feature engineering, or evaluating model performance.

**`/references/data-cleaning-visualization.md`** — Read when handling missing data, detecting outliers, transforming features, or creating publication-quality visualizations and dashboards.
