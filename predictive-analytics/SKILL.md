---
name: predictive-analytics
description: "Apply predictive analytics and machine learning for forecasting and decision-making. Use for: regression analysis, classification models, time series forecasting, customer churn prediction, demand forecasting, risk modeling, feature engineering, model evaluation, deployment strategies, and business applications of predictive models."
---

# Predictive Analytics

Use historical data and machine learning to forecast future outcomes and support data-driven decisions.

## Overview

Predictive analytics combines statistical techniques and machine learning algorithms to analyze historical data and make predictions about future events. This skill covers model selection, data preparation, training and evaluation, and deploying predictions for business value across various applications.

## Predictive Analytics Workflow

1. **Define Problem**: Identify business question and success metrics
2. **Collect Data**: Gather relevant historical data
3. **Explore Data**: Understand patterns, distributions, relationships
4. **Prepare Data**: Clean, transform, engineer features
5. **Select Model**: Choose appropriate algorithm
6. **Train Model**: Fit model to training data
7. **Evaluate Model**: Assess performance on test data
8. **Deploy Model**: Integrate into business processes
9. **Monitor Model**: Track performance and retrain as needed

## Types of Predictive Models

### Regression (Predict Continuous Values)

**Linear Regression**: Predict numeric outcome from linear relationships
- Use Case: Sales forecasting, price prediction
- Assumptions: Linear relationship, normal distribution, no multicollinearity

**Polynomial Regression**: Capture non-linear relationships
**Ridge/Lasso Regression**: Regularized regression to prevent overfitting
**Random Forest Regression**: Ensemble of decision trees
**Gradient Boosting Regression**: Sequential ensemble method (XGBoost, LightGBM)

### Classification (Predict Categories)

**Logistic Regression**: Binary classification (yes/no, true/false)
- Use Case: Churn prediction, fraud detection, email spam

**Decision Trees**: Rule-based classification
**Random Forest**: Ensemble of decision trees
**Gradient Boosting**: XGBoost, LightGBM, CatBoost
**Support Vector Machines (SVM)**: Find optimal decision boundary
**Neural Networks**: Deep learning for complex patterns
**Naive Bayes**: Probabilistic classifier

### Time Series Forecasting

**ARIMA**: Autoregressive Integrated Moving Average
**SARIMA**: Seasonal ARIMA
**Prophet**: Facebook's forecasting tool for business time series
**LSTM**: Long Short-Term Memory neural networks
**Exponential Smoothing**: Simple, trend, seasonal methods

### Clustering (Group Similar Items)

**K-Means**: Partition into K clusters
**Hierarchical Clustering**: Build cluster hierarchy
**DBSCAN**: Density-based clustering
**Use Case**: Customer segmentation, anomaly detection

## Feature Engineering

### Creating Features

**Numeric Transformations**:
- Log transformation: Handle skewed distributions
- Scaling: Normalize to 0-1 or standardize to mean=0, std=1
- Binning: Convert continuous to categorical
- Polynomial features: x², x³, x*y interactions

**Date/Time Features**:
- Day of week, month, quarter, year
- Is weekend, is holiday
- Days since event
- Cyclical encoding (sin/cos for hour, month)

**Text Features**:
- TF-IDF: Term frequency-inverse document frequency
- Word embeddings: Word2Vec, GloVe
- Sentiment scores
- Text length, word count

**Categorical Encoding**:
- One-hot encoding: Binary columns for each category
- Label encoding: Numeric codes for categories
- Target encoding: Mean of target for each category
- Frequency encoding: Count of each category

### Feature Selection

**Filter Methods**:
- Correlation with target
- Chi-square test
- Mutual information

**Wrapper Methods**:
- Forward selection
- Backward elimination
- Recursive feature elimination (RFE)

**Embedded Methods**:
- Lasso (L1 regularization)
- Tree-based feature importance
- Regularized models

## Model Evaluation

### Regression Metrics

**Mean Absolute Error (MAE)**: Average absolute difference
**Mean Squared Error (MSE)**: Average squared difference
**Root Mean Squared Error (RMSE)**: Square root of MSE
**R² Score**: Proportion of variance explained (0-1, higher better)
**Mean Absolute Percentage Error (MAPE)**: Average % error

### Classification Metrics

**Accuracy**: % of correct predictions
**Precision**: True Positives / (True Positives + False Positives)
**Recall (Sensitivity)**: True Positives / (True Positives + False Negatives)
**F1 Score**: Harmonic mean of precision and recall
**ROC-AUC**: Area under ROC curve (0.5-1.0, higher better)
**Confusion Matrix**: Breakdown of predictions vs actuals

### Cross-Validation

**K-Fold**: Split data into K folds, train on K-1, test on 1
**Stratified K-Fold**: Maintain class distribution in each fold
**Time Series Split**: Respect temporal order
**Leave-One-Out**: Each sample used as test set once

## Common Use Cases

### Customer Churn Prediction

**Problem**: Predict which customers will cancel service
**Features**: Usage patterns, customer service interactions, demographics, tenure
**Model**: Logistic regression, random forest, gradient boosting
**Outcome**: Proactive retention campaigns

### Demand Forecasting

**Problem**: Predict future product demand
**Features**: Historical sales, seasonality, promotions, external factors
**Model**: ARIMA, Prophet, LSTM
**Outcome**: Optimized inventory, reduced stockouts

### Credit Risk Modeling

**Problem**: Predict loan default probability
**Features**: Credit history, income, debt-to-income ratio, employment
**Model**: Logistic regression, gradient boosting
**Outcome**: Informed lending decisions

### Price Optimization

**Problem**: Predict optimal pricing for maximum revenue
**Features**: Historical prices, demand elasticity, competitor prices, costs
**Model**: Regression, reinforcement learning
**Outcome**: Dynamic pricing strategies

### Fraud Detection

**Problem**: Identify fraudulent transactions
**Features**: Transaction amount, location, time, user behavior
**Model**: Anomaly detection, random forest, neural networks
**Outcome**: Reduced fraud losses

## Model Deployment

### Deployment Strategies

**Batch Prediction**: Scheduled predictions on datasets
**Real-Time API**: On-demand predictions via REST API
**Edge Deployment**: Models on devices (mobile, IoT)
**Embedded**: Models in applications

### Model Serving

**Flask/FastAPI**: Python web frameworks for ML APIs
**TensorFlow Serving**: Serve TensorFlow models
**MLflow**: Model registry and deployment
**SageMaker**: AWS managed ML deployment
**Azure ML**: Microsoft managed ML platform

### Monitoring

**Data Drift**: Input data distribution changes
**Concept Drift**: Relationship between features and target changes
**Model Performance**: Track accuracy, precision, recall over time
**Retraining Triggers**: Automatic retraining when performance degrades

## Tools and Libraries

### Python Libraries

**scikit-learn**: General machine learning
**pandas**: Data manipulation
**numpy**: Numerical computing
**statsmodels**: Statistical models
**XGBoost/LightGBM/CatBoost**: Gradient boosting
**TensorFlow/PyTorch**: Deep learning
**Prophet**: Time series forecasting

### Platforms

**Jupyter Notebooks**: Interactive development
**Google Colab**: Free cloud notebooks with GPU
**Databricks**: Unified analytics platform
**AWS SageMaker**: End-to-end ML platform
**Azure Machine Learning**: Microsoft ML platform
**Google Vertex AI**: Google Cloud ML platform

## Best Practices

### Data Preparation

- Handle missing values appropriately
- Remove or cap outliers
- Scale features for distance-based algorithms
- Split data before any preprocessing (avoid data leakage)
- Use stratified sampling for imbalanced classes

### Model Development

- Start simple (baseline model)
- Use cross-validation for robust evaluation
- Tune hyperparameters systematically (grid search, random search)
- Ensemble multiple models for better performance
- Document assumptions and limitations

### Deployment

- Version control for code and models
- A/B test new models before full deployment
- Monitor performance continuously
- Plan for model retraining
- Ensure reproducibility

## Using the Reference Files

### When to Read Each Reference

**`/references/algorithm-selection-guide.md`** — Read when choosing between regression, classification, or time series models for specific business problems.

**`/references/feature-engineering-techniques.md`** — Read when creating features from raw data, handling categorical variables, or engineering time-based features.

**`/references/model-deployment-patterns.md`** — Read when deploying models to production, setting up APIs, or implementing monitoring and retraining strategies.

## References

- [Algorithm Selection Guide](references/algorithm-selection-guide.md)
- [Feature Engineering Techniques](references/feature-engineering-techniques.md)
- [Model Deployment Patterns](references/model-deployment-patterns.md)
