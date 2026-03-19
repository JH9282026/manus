---
name: feature-engineering
description: "Transform raw data into informative features for machine learning. Use for: creating derived features from existing data, handling missing values and outliers, encoding categorical variables, scaling and normalizing numerical features, extracting features from text and images, performing dimensionality reduction with PCA/t-SNE, generating polynomial and interaction features, implementing time-series feature engineering, and using automated feature engineering tools like Featuretools."
---

# Feature Engineering

Transform raw data into powerful features that improve machine learning model performance.

## Overview

Feature engineering is the process of selecting, creating, and transforming features to make machine learning algorithms work effectively. It's often considered the most important factor in model performance, requiring domain knowledge, creativity, and technical skills. Good feature engineering can turn mediocre models into excellent ones by making patterns more apparent to algorithms.

## Data Preprocessing

### Handling Missing Values

```python
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer, KNNImputer

# Simple imputation
imputer = SimpleImputer(strategy='mean')  # or 'median', 'most_frequent'
df['age'] = imputer.fit_transform(df[['age']])

# KNN imputation
knn_imputer = KNNImputer(n_neighbors=5)
df_imputed = knn_imputer.fit_transform(df)

# Forward/backward fill for time series
df['value'] = df['value'].fillna(method='ffill')

# Indicator for missingness
df['age_missing'] = df['age'].isnull().astype(int)
```

### Outlier Detection and Treatment

```python
from scipy import stats

# Z-score method
z_scores = np.abs(stats.zscore(df['value']))
df_no_outliers = df[z_scores < 3]

# IQR method
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1
df_no_outliers = df[(df['value'] >= Q1 - 1.5*IQR) & (df['value'] <= Q3 + 1.5*IQR)]

# Winsorization (capping)
from scipy.stats.mstats import winsorize
df['value_winsorized'] = winsorize(df['value'], limits=[0.05, 0.05])

# Isolation Forest
from sklearn.ensemble import IsolationForest
iso_forest = IsolationForest(contamination=0.1)
outliers = iso_forest.fit_predict(df[['value']])
df_no_outliers = df[outliers == 1]
```

## Encoding Categorical Variables

### One-Hot Encoding

```python
from sklearn.preprocessing import OneHotEncoder

# Pandas get_dummies
df_encoded = pd.get_dummies(df, columns=['category'], drop_first=True)

# Sklearn OneHotEncoder
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoded = encoder.fit_transform(df[['category']])
```

### Label Encoding

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])
```

### Target Encoding

```python
def target_encode(df, column, target, smoothing=1.0):
    # Calculate global mean
    global_mean = df[target].mean()
    
    # Calculate category means and counts
    agg = df.groupby(column)[target].agg(['mean', 'count'])
    
    # Smooth the means
    smoothed = (agg['mean'] * agg['count'] + global_mean * smoothing) / (agg['count'] + smoothing)
    
    return df[column].map(smoothed)

df['category_target_encoded'] = target_encode(df, 'category', 'target')
```

### Frequency Encoding

```python
freq_encoding = df['category'].value_counts(normalize=True).to_dict()
df['category_freq'] = df['category'].map(freq_encoding)
```

## Feature Scaling and Normalization

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Standardization (Z-score normalization)
scaler = StandardScaler()
df['value_scaled'] = scaler.fit_transform(df[['value']])

# Min-Max scaling
minmax_scaler = MinMaxScaler()
df['value_minmax'] = minmax_scaler.fit_transform(df[['value']])

# Robust scaling (resistant to outliers)
robust_scaler = RobustScaler()
df['value_robust'] = robust_scaler.fit_transform(df[['value']])

# Log transformation
df['value_log'] = np.log1p(df['value'])  # log(1 + x)

# Box-Cox transformation
from scipy.stats import boxcox
df['value_boxcox'], lambda_param = boxcox(df['value'] + 1)
```

## Feature Creation

### Polynomial Features

```python
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(df[['feature1', 'feature2']])
```

### Interaction Features

```python
# Manual interactions
df['feature1_x_feature2'] = df['feature1'] * df['feature2']
df['feature1_div_feature2'] = df['feature1'] / (df['feature2'] + 1e-10)

# Ratio features
df['ratio'] = df['numerator'] / (df['denominator'] + 1e-10)
```

### Binning/Discretization

```python
# Equal-width binning
df['age_binned'] = pd.cut(df['age'], bins=5, labels=['very_young', 'young', 'middle', 'old', 'very_old'])

# Equal-frequency binning
df['age_quantile'] = pd.qcut(df['age'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

# Custom bins
bins = [0, 18, 35, 60, 100]
df['age_group'] = pd.cut(df['age'], bins=bins, labels=['child', 'young_adult', 'adult', 'senior'])
```

## Time Series Feature Engineering

```python
# Date/time features
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['dayofweek'] = df['date'].dt.dayofweek
df['quarter'] = df['date'].dt.quarter
df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)

# Lag features
df['value_lag1'] = df['value'].shift(1)
df['value_lag7'] = df['value'].shift(7)

# Rolling statistics
df['value_rolling_mean_7'] = df['value'].rolling(window=7).mean()
df['value_rolling_std_7'] = df['value'].rolling(window=7).std()
df['value_rolling_min_7'] = df['value'].rolling(window=7).min()
df['value_rolling_max_7'] = df['value'].rolling(window=7).max()

# Expanding statistics
df['value_expanding_mean'] = df['value'].expanding().mean()

# Difference features
df['value_diff'] = df['value'].diff()
df['value_pct_change'] = df['value'].pct_change()

# Seasonal features
df['sin_month'] = np.sin(2 * np.pi * df['month'] / 12)
df['cos_month'] = np.cos(2 * np.pi * df['month'] / 12)
```

## Text Feature Engineering

```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# TF-IDF
tfidf = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
tfidf_features = tfidf.fit_transform(df['text'])

# Count vectorization
count_vec = CountVectorizer(max_features=500)
count_features = count_vec.fit_transform(df['text'])

# Text statistics
df['text_length'] = df['text'].str.len()
df['word_count'] = df['text'].str.split().str.len()
df['avg_word_length'] = df['text'].apply(lambda x: np.mean([len(word) for word in x.split()]))
df['uppercase_count'] = df['text'].str.count(r'[A-Z]')
df['special_char_count'] = df['text'].str.count(r'[^a-zA-Z0-9\s]')

# Sentiment analysis
from textblob import TextBlob
df['sentiment'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
```

## Dimensionality Reduction

### PCA (Principal Component Analysis)

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=0.95)  # Keep 95% of variance
pca_features = pca.fit_transform(df_scaled)

print(f"Original features: {df_scaled.shape[1]}")
print(f"Reduced features: {pca_features.shape[1]}")
```

### t-SNE

```python
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=42)
tsne_features = tsne.fit_transform(df_scaled)
```

### Feature Selection

```python
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif, RFE
from sklearn.ensemble import RandomForestClassifier

# Univariate feature selection
selector = SelectKBest(f_classif, k=10)
X_selected = selector.fit_transform(X, y)

# Mutual information
mi_selector = SelectKBest(mutual_info_classif, k=10)
X_mi = mi_selector.fit_transform(X, y)

# Recursive Feature Elimination
rfe = RFE(estimator=RandomForestClassifier(), n_features_to_select=10)
X_rfe = rfe.fit_transform(X, y)

# Feature importance from tree-based models
rf = RandomForestClassifier()
rf.fit(X, y)
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)
```

## Automated Feature Engineering

### Featuretools

```python
import featuretools as ft

# Create entity set
es = ft.EntitySet(id='data')
es = es.add_dataframe(dataframe_name='transactions', dataframe=transactions_df, index='transaction_id')
es = es.add_dataframe(dataframe_name='customers', dataframe=customers_df, index='customer_id')

# Define relationships
es = es.add_relationship('customers', 'customer_id', 'transactions', 'customer_id')

# Generate features
feature_matrix, feature_defs = ft.dfs(
    entityset=es,
    target_dataframe_name='transactions',
    max_depth=2,
    verbose=True
)
```

## Domain-Specific Features

### E-commerce

```python
# Customer behavior features
df['days_since_last_purchase'] = (pd.Timestamp.now() - df['last_purchase_date']).dt.days
df['purchase_frequency'] = df['total_purchases'] / df['days_as_customer']
df['avg_order_value'] = df['total_spent'] / df['total_purchases']
df['cart_abandonment_rate'] = df['abandoned_carts'] / df['total_carts']

# Product features
df['discount_percentage'] = (df['original_price'] - df['sale_price']) / df['original_price'] * 100
df['price_per_unit'] = df['price'] / df['quantity']
```

### Finance

```python
# Technical indicators
df['SMA_20'] = df['close'].rolling(window=20).mean()
df['EMA_12'] = df['close'].ewm(span=12).mean()
df['RSI'] = calculate_rsi(df['close'], period=14)
df['MACD'] = df['EMA_12'] - df['close'].ewm(span=26).mean()
df['volatility'] = df['returns'].rolling(window=20).std()
```

## Best Practices

**General Principles:**
- Understand your data and domain
- Start simple, then add complexity
- Create features based on business logic
- Validate features on holdout set
- Document feature engineering steps

**Avoiding Data Leakage:**
- Fit transformers only on training data
- Use pipelines to prevent leakage
- Be careful with target encoding
- Don't use future information in time series

**Feature Quality:**
- Check for high correlation (multicollinearity)
- Remove low-variance features
- Validate feature distributions
- Monitor feature importance

**Scalability:**
- Use efficient data structures (categorical dtype)
- Implement incremental processing for large datasets
- Cache intermediate results
- Parallelize feature computation

## Tools and Libraries

- **pandas**: Data manipulation
- **scikit-learn**: Preprocessing and feature selection
- **Featuretools**: Automated feature engineering
- **category_encoders**: Advanced encoding techniques
- **tsfresh**: Time series feature extraction
- **NLTK/spaCy**: Text processing
- **OpenCV**: Image feature extraction

## Learning Path

1. **Basics**: Missing values, encoding, scaling
2. **Intermediate**: Feature creation, interactions, binning
3. **Advanced**: Automated engineering, domain-specific features
4. **Expert**: Custom transformers, pipeline optimization

See `references/` for advanced techniques, domain-specific patterns, and automation strategies.
