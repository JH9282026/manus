# Feature Engineering

Comprehensive guide to preparing and transforming data for machine learning models.

---

## Overview

Feature engineering is the process of creating, transforming, and selecting features to improve model performance. High-quality features often matter more than algorithm choice, making this a critical skill for successful machine learning projects.

## Data Preprocessing

### Handling Missing Values

**Detection**:
- Use pandas: `df.isnull().sum()`
- Visualize with heatmaps: `sns.heatmap(df.isnull())`

**Strategies**:

**1. Deletion**:
- Remove rows: When missing data is < 5% and random
- Remove columns: When > 60% missing and not critical
- Pros: Simple, no imputation bias
- Cons: Loses information, reduces sample size

**2. Imputation**:
- Mean/Median: For numerical features (median robust to outliers)
- Mode: For categorical features
- Forward/Backward fill: For time-series data
- KNN Imputation: Use similar samples to impute
- Model-based: Predict missing values using other features
- Constant: Fill with specific value (e.g., 0, "Unknown")

**3. Indicator Variables**:
- Create binary flag for missingness
- Preserves information about missing pattern
- Useful when missingness is informative

**Implementation**:
```python
from sklearn.impute import SimpleImputer, KNNImputer

# Mean imputation
imputer = SimpleImputer(strategy='mean')
df_imputed = imputer.fit_transform(df)

# KNN imputation
knn_imputer = KNNImputer(n_neighbors=5)
df_imputed = knn_imputer.fit_transform(df)
```

### Handling Outliers

**Detection Methods**:
- Statistical: Z-score (|z| > 3), IQR (Q1 - 1.5*IQR, Q3 + 1.5*IQR)
- Visualization: Box plots, scatter plots
- Model-based: Isolation Forest, Local Outlier Factor

**Treatment Strategies**:
- **Remove**: When outliers are errors or not representative
- **Cap/Winsorize**: Replace with threshold values (e.g., 1st/99th percentile)
- **Transform**: Log, square root to reduce impact
- **Separate Model**: Build specific model for outlier segment
- **Keep**: When outliers are valid and important

**Implementation**:
```python
# IQR method
Q1 = df['feature'].quantile(0.25)
Q3 = df['feature'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Cap outliers
df['feature'] = df['feature'].clip(lower, upper)
```

### Feature Scaling

**Why Scale?**
- Distance-based algorithms (KNN, SVM, K-Means) sensitive to scale
- Gradient descent converges faster
- Regularization (L1/L2) requires comparable scales
- Neural networks train more stably

**Methods**:

**1. Standardization (Z-score normalization)**:
- Transform to mean=0, std=1
- Formula: (x - μ) / σ
- Use when: Features normally distributed, outliers present
- Preserves outlier information

**2. Min-Max Scaling**:
- Transform to [0, 1] range
- Formula: (x - min) / (max - min)
- Use when: Bounded range needed, no outliers
- Sensitive to outliers

**3. Robust Scaling**:
- Uses median and IQR instead of mean and std
- Formula: (x - median) / IQR
- Use when: Outliers present
- Robust to extreme values

**4. MaxAbs Scaling**:
- Scales to [-1, 1] by dividing by max absolute value
- Preserves sparsity (doesn't shift/center)
- Use for: Sparse data

**Implementation**:
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use same scaler!

# Min-Max
minmax = MinMaxScaler()
X_scaled = minmax.fit_transform(X_train)
```

**Important**: Fit scaler on training data only, then transform both train and test!

## Feature Transformation

### Numerical Transformations

**Log Transform**:
- Reduces right skewness
- Handles exponential relationships
- Use for: Income, prices, counts
- Formula: log(x + 1) to handle zeros

**Square Root / Cube Root**:
- Moderate skewness reduction
- Less aggressive than log
- Preserves zeros

**Box-Cox Transform**:
- Automatically finds optimal power transformation
- Requires positive values
- Makes distribution more normal

**Yeo-Johnson Transform**:
- Like Box-Cox but handles negative values
- More flexible

**Binning/Discretization**:
- Convert continuous to categorical
- Equal-width bins: Same range per bin
- Equal-frequency bins: Same count per bin
- Custom bins: Domain-driven thresholds
- Use when: Non-linear relationships, interpretability needed

**Polynomial Features**:
- Create x², x³, x*y interactions
- Captures non-linear relationships
- Warning: Increases dimensionality rapidly

**Implementation**:
```python
import numpy as np
from sklearn.preprocessing import PowerTransformer, PolynomialFeatures

# Log transform
df['log_income'] = np.log1p(df['income'])

# Box-Cox
pt = PowerTransformer(method='box-cox')
df['transformed'] = pt.fit_transform(df[['feature']])

# Polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)
```

### Categorical Encoding

**1. Label Encoding**:
- Assign integer to each category
- Use for: Ordinal variables (low, medium, high)
- Warning: Implies ordering for nominal variables

**2. One-Hot Encoding**:
- Create binary column for each category
- Use for: Nominal variables with few categories (< 10-15)
- Pros: No ordinal assumption
- Cons: High dimensionality with many categories

**3. Ordinal Encoding**:
- Map categories to ordered integers
- Use for: Ordinal variables with natural order
- Example: education level, satisfaction rating

**4. Target Encoding (Mean Encoding)**:
- Replace category with target mean for that category
- Use for: High-cardinality categoricals
- Warning: Risk of overfitting, use cross-validation

**5. Frequency Encoding**:
- Replace with category frequency
- Captures importance of category
- Simple and effective

**6. Binary Encoding**:
- Convert to binary, then one-hot encode binary digits
- More compact than one-hot for high cardinality

**7. Hashing**:
- Hash categories to fixed number of buckets
- Handles unseen categories
- Some collision acceptable

**Implementation**:
```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import category_encoders as ce

# Label encoding
le = LabelEncoder()
df['encoded'] = le.fit_transform(df['category'])

# One-hot encoding
ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoded = ohe.fit_transform(df[['category']])

# Target encoding
te = ce.TargetEncoder()
df['encoded'] = te.fit_transform(df['category'], df['target'])
```

### Date/Time Features

**Extraction**:
- Year, month, day, day of week, hour
- Quarter, week of year
- Is weekend, is holiday
- Time since epoch
- Season

**Cyclical Encoding**:
- Encode cyclical features (hour, month) as sin/cos
- Preserves cyclical nature (23:00 close to 00:00)

**Implementation**:
```python
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

# Cyclical encoding
df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)
```

## Feature Creation

### Domain-Specific Features

**Aggregations**:
- Sum, mean, median, std, min, max
- Count, count distinct
- Ratios and percentages

**Interactions**:
- Multiply features: price * quantity
- Divide features: total / count
- Difference: current - previous

**Text Features**:
- Length, word count, character count
- Presence of keywords
- Sentiment scores
- TF-IDF vectors

**Geospatial Features**:
- Distance between coordinates
- Proximity to landmarks
- Clustering of locations

### Automated Feature Engineering

**Featuretools**:
- Automated feature generation from relational data
- Deep feature synthesis
- Handles temporal relationships

**tsfresh**:
- Automated time-series feature extraction
- 100+ statistical features
- Feature selection included

## Feature Selection

### Why Select Features?

- Reduce overfitting
- Improve model performance
- Decrease training time
- Enhance interpretability
- Reduce storage and memory

### Filter Methods

**Correlation-Based**:
- Remove highly correlated features (> 0.9)
- Pearson for linear, Spearman for monotonic

**Statistical Tests**:
- Chi-square test for categorical features
- ANOVA F-test for numerical features
- Mutual information for non-linear relationships

**Variance Threshold**:
- Remove low-variance features
- Features with same value in > 95% samples

**Implementation**:
```python
from sklearn.feature_selection import SelectKBest, chi2, f_classif, VarianceThreshold

# Chi-square for categorical
selector = SelectKBest(chi2, k=10)
X_selected = selector.fit_transform(X, y)

# ANOVA F-test for numerical
selector = SelectKBest(f_classif, k=10)
X_selected = selector.fit_transform(X, y)

# Variance threshold
vt = VarianceThreshold(threshold=0.01)
X_selected = vt.fit_transform(X)
```

### Wrapper Methods

**Recursive Feature Elimination (RFE)**:
- Train model, remove least important feature
- Repeat until desired number of features
- Computationally expensive but effective

**Forward Selection**:
- Start with no features
- Add feature that improves performance most
- Repeat until no improvement

**Backward Elimination**:
- Start with all features
- Remove feature that hurts performance least
- Repeat until performance degrades

**Implementation**:
```python
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

# RFE
model = RandomForestClassifier()
rfe = RFE(estimator=model, n_features_to_select=10)
X_selected = rfe.fit_transform(X, y)
```

### Embedded Methods

**L1 Regularization (Lasso)**:
- Drives coefficients to exactly zero
- Automatic feature selection
- Fast and effective

**Tree-Based Feature Importance**:
- Random Forest, Gradient Boosting
- Importance based on split quality
- Handles non-linear relationships

**Implementation**:
```python
from sklearn.linear_model import LassoCV
from sklearn.ensemble import RandomForestClassifier

# Lasso
lasso = LassoCV(cv=5)
lasso.fit(X, y)
important_features = X.columns[lasso.coef_ != 0]

# Random Forest
rf = RandomForestClassifier()
rf.fit(X, y)
importances = pd.Series(rf.feature_importances_, index=X.columns)
top_features = importances.nlargest(10)
```

## Best Practices

**General Principles**:
- Understand domain before engineering features
- Start simple, add complexity incrementally
- Document all transformations for reproducibility
- Use pipelines to prevent data leakage
- Validate feature importance with multiple methods

**Avoiding Data Leakage**:
- Fit transformers on training data only
- Apply same transformations to test data
- Don't use future information for past predictions
- Be careful with target encoding

**Handling High Cardinality**:
- Group rare categories into "Other"
- Use target encoding with cross-validation
- Consider embeddings for very high cardinality

**Time-Series Specific**:
- Create lag features (previous values)
- Rolling statistics (moving average, std)
- Difference features (current - previous)
- Respect temporal order in train/test split

## Tools and Libraries

**Python**:
- pandas: Data manipulation
- scikit-learn: Preprocessing and selection
- category_encoders: Advanced encoding methods
- featuretools: Automated feature engineering
- tsfresh: Time-series features

**Pipelines**:
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('selector', SelectKBest(k=10)),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```
