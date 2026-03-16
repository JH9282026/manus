---
name: python-data-science
description: "Perform data science tasks using Python with NumPy, Pandas, Scikit-learn, Matplotlib, and Seaborn. Use for data manipulation, exploratory analysis, machine learning, statistical modeling, data visualization, feature engineering, and building end-to-end data science pipelines."
---

# Python Data Science

Perform comprehensive data science tasks using Python's powerful ecosystem of libraries.

## Overview

Python has become the dominant language for data science due to its extensive library ecosystem, readability, and versatility. This skill covers the essential libraries and workflows for data manipulation (Pandas), numerical computing (NumPy), machine learning (Scikit-learn), and visualization (Matplotlib, Seaborn). Together, these tools enable end-to-end data science pipelines from raw data to predictive models.

## Core Library Ecosystem

### NumPy: Numerical Computing Foundation

| Feature | Purpose | Key Advantage |
|---------|---------|---------------|
| ndarray | Multidimensional arrays | 10-50x faster than Python lists |
| Vectorization | Element-wise operations | Eliminates slow Python loops |
| Broadcasting | Operations on different shapes | Automatic array alignment |
| Linear algebra | Matrix operations | Optimized BLAS/LAPACK routines |
| Random numbers | Statistical sampling | Comprehensive distribution library |

### Pandas: Data Manipulation and Analysis

| Structure | Description | Best For |
|-----------|-------------|----------|
| Series | 1D labeled array | Single variable, time series |
| DataFrame | 2D labeled table | Tabular data, spreadsheet-like |
| Index | Row/column labels | Fast lookups, alignment |
| MultiIndex | Hierarchical indexing | Multi-dimensional data |

### Scikit-learn: Machine Learning

| Component | Purpose | Examples |
|-----------|---------|----------|
| Estimators | ML algorithms | `LinearRegression()`, `RandomForestClassifier()` |
| Transformers | Data preprocessing | `StandardScaler()`, `PCA()` |
| Pipelines | Workflow chaining | Combine preprocessing + modeling |
| Model selection | Evaluation tools | `cross_val_score()`, `GridSearchCV()` |

### Visualization Libraries

| Library | Strength | Use Case |
|---------|----------|----------|
| Matplotlib | Flexibility, control | Publication-quality static plots |
| Seaborn | Statistical graphics | Quick, attractive statistical visualizations |
| Plotly | Interactivity | Web-based interactive dashboards |

## Data Science Workflow

### 1. Data Import and Exploration

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data.csv')

# Quick exploration
df.info()  # Data types, missing values
df.describe()  # Summary statistics
df.head()  # First rows
```

### 2. Data Cleaning and Transformation

```python
# Handle missing values
df.dropna()  # Remove rows with missing values
df.fillna(value)  # Fill missing values

# Data type conversion
df['date'] = pd.to_datetime(df['date'])
df['category'] = df['category'].astype('category')

# Feature engineering
df['revenue'] = df['price'] * df['quantity']
df['year'] = df['date'].dt.year
```

### 3. Exploratory Data Analysis

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Statistical summaries
df.groupby('category')['sales'].agg(['mean', 'median', 'std'])

# Correlations
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True)

# Distributions
sns.histplot(df['sales'], kde=True)
```

### 4. Feature Engineering and Preprocessing

```python
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Encode categorical variables
le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])

# Split data
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### 5. Model Building and Evaluation

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Predictions
y_pred = model.predict(X_test_scaled)

# Evaluate
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))
```

## NumPy Essentials

### Array Creation

```python
# From lists
arr = np.array([1, 2, 3, 4, 5])

# Special arrays
np.zeros((3, 4))  # 3x4 array of zeros
np.ones((2, 3))  # 2x3 array of ones
np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1

# Random arrays
np.random.rand(3, 3)  # Uniform [0, 1)
np.random.randn(3, 3)  # Standard normal
np.random.randint(0, 10, (3, 3))  # Random integers
```

### Array Operations

```python
# Element-wise operations
arr + 10
arr * 2
arr ** 2
np.sqrt(arr)

# Aggregations
arr.sum()
arr.mean()
arr.std()
arr.min()
arr.max()

# Along axes
arr.sum(axis=0)  # Sum columns
arr.mean(axis=1)  # Mean of rows
```

### Broadcasting

```python
# Automatically align arrays of different shapes
arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
arr + scalar  # Adds 10 to every element

vector = np.array([1, 2, 3])
arr + vector  # Adds vector to each row
```

## Pandas Essentials

### DataFrame Operations

```python
# Selection
df['column']  # Single column (Series)
df[['col1', 'col2']]  # Multiple columns (DataFrame)
df.loc[0]  # Row by label
df.iloc[0]  # Row by position
df.loc[df['age'] > 30]  # Boolean indexing

# Filtering
df[df['sales'] > 1000]
df[(df['year'] >= 2020) & (df['region'] == 'North')]

# Sorting
df.sort_values('sales', ascending=False)
df.sort_values(['region', 'sales'], ascending=[True, False])
```

### Grouping and Aggregation

```python
# Group by single column
df.groupby('category')['sales'].mean()

# Group by multiple columns
df.groupby(['region', 'category'])['sales'].sum()

# Multiple aggregations
df.groupby('category').agg({
    'sales': ['sum', 'mean', 'count'],
    'profit': ['sum', 'mean']
})

# Custom aggregations
df.groupby('category')['sales'].agg(['mean', 'std', lambda x: x.max() - x.min()])
```

### Merging and Joining

```python
# Merge (SQL-like joins)
pd.merge(df1, df2, on='key')  # Inner join
pd.merge(df1, df2, on='key', how='left')  # Left join
pd.merge(df1, df2, on='key', how='outer')  # Full outer join

# Concatenate
pd.concat([df1, df2], axis=0)  # Stack vertically
pd.concat([df1, df2], axis=1)  # Stack horizontally

# Join on index
df1.join(df2, how='inner')
```

### Time Series Operations

```python
# Set datetime index
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Resampling
df.resample('M').sum()  # Monthly sum
df.resample('W').mean()  # Weekly mean

# Rolling windows
df['sales'].rolling(window=7).mean()  # 7-day moving average
df['sales'].rolling(window=30).std()  # 30-day rolling std

# Shifting
df['sales_lag1'] = df['sales'].shift(1)  # Previous value
df['sales_diff'] = df['sales'].diff()  # First difference
```

## Scikit-learn Essentials

### Model Selection Guide

| Task | Algorithm | When to Use |
|------|-----------|-------------|
| Classification | Logistic Regression | Linear decision boundary, interpretability |
| Classification | Random Forest | Non-linear, feature importance, robust |
| Classification | SVM | High-dimensional, clear margin of separation |
| Classification | Gradient Boosting | Maximum accuracy, willing to tune |
| Regression | Linear Regression | Linear relationships, interpretability |
| Regression | Random Forest | Non-linear, robust to outliers |
| Regression | Gradient Boosting | Maximum accuracy, complex relationships |
| Clustering | K-Means | Spherical clusters, known number of clusters |
| Clustering | DBSCAN | Arbitrary shapes, unknown number of clusters |
| Dimensionality | PCA | Linear relationships, variance preservation |
| Dimensionality | t-SNE | Visualization, non-linear relationships |

### Preprocessing

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder

# Scaling
scaler = StandardScaler()  # Mean=0, Std=1
X_scaled = scaler.fit_transform(X_train)

scaler = MinMaxScaler()  # Range [0, 1]
X_scaled = scaler.fit_transform(X_train)

# Encoding
le = LabelEncoder()  # For target variable
y_encoded = le.fit_transform(y)

ohe = OneHotEncoder()  # For categorical features
X_encoded = ohe.fit_transform(X_categorical)
```

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score, KFold

# Simple cross-validation
scores = cross_val_score(model, X, y, cv=5)
print(f"Mean accuracy: {scores.mean():.3f} (+/- {scores.std():.3f})")

# Custom cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
for train_idx, val_idx in kf.split(X):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]
    # Train and evaluate
```

### Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Grid search
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_}")

# Random search (faster for large parameter spaces)
random_search = RandomizedSearchCV(RandomForestClassifier(), param_grid, n_iter=20, cv=5)
random_search.fit(X_train, y_train)
```

### Pipelines

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

# Create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=10)),
    ('classifier', RandomForestClassifier())
])

# Train pipeline
pipeline.fit(X_train, y_train)

# Predict
y_pred = pipeline.predict(X_test)
```

## Visualization Best Practices

### Matplotlib Basics

```python
import matplotlib.pyplot as plt

# Basic plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Line 1')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.legend()
plt.grid(True)
plt.show()

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y1)
axes[0, 1].scatter(x, y2)
axes[1, 0].bar(categories, values)
axes[1, 1].hist(data, bins=30)
plt.tight_layout()
```

### Seaborn for Statistical Graphics

```python
import seaborn as sns

# Set style
sns.set_style('whitegrid')
sns.set_palette('husl')

# Distribution plots
sns.histplot(data=df, x='value', hue='category', kde=True)
sns.boxplot(data=df, x='category', y='value')
sns.violinplot(data=df, x='category', y='value')

# Relationship plots
sns.scatterplot(data=df, x='x', y='y', hue='category', size='value')
sns.lineplot(data=df, x='date', y='value', hue='category')
sns.regplot(data=df, x='x', y='y')  # With regression line

# Matrix plots
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
sns.clustermap(df.corr(), cmap='coolwarm')  # With hierarchical clustering

# Pair plots
sns.pairplot(df, hue='category')
```

## Integration: NumPy, Pandas, Scikit-learn

### Seamless Data Flow

```python
# 1. Load data with Pandas
df = pd.read_csv('data.csv')

# 2. Explore and clean with Pandas
df = df.dropna()
df['new_feature'] = df['feature1'] * df['feature2']

# 3. Convert to NumPy for Scikit-learn
X = df[['feature1', 'feature2', 'new_feature']].values  # NumPy array
y = df['target'].values

# 4. Train model with Scikit-learn (expects NumPy arrays)
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X, y)

# 5. Predictions back to Pandas for analysis
df['predictions'] = model.predict(X)
df['residuals'] = df['target'] - df['predictions']

# 6. Analyze results with Pandas
df.groupby('category')['residuals'].agg(['mean', 'std'])
```

## Best Practices

### Code Organization

1. **Import conventions** — Use standard aliases
   ```python
   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   import seaborn as sns
   from sklearn.model_selection import train_test_split
   ```

2. **Separate concerns** — Modularize data loading, preprocessing, modeling, evaluation

3. **Use functions** — Encapsulate reusable logic

4. **Document code** — Docstrings for functions, comments for complex logic

### Performance Optimization

1. **Vectorize with NumPy** — Avoid Python loops on arrays
2. **Use Pandas methods** — Built-in operations are optimized
3. **Avoid chained indexing** — Use `.loc[]` instead of `df[condition][column]`
4. **Use appropriate data types** — `category` for categorical, `int32` instead of `int64` when possible
5. **Process in chunks** — For large datasets, use `pd.read_csv(chunksize=10000)`

### Reproducibility

1. **Set random seeds** — `np.random.seed(42)`, `random_state=42` in Scikit-learn
2. **Version dependencies** — Use `requirements.txt` or `environment.yml`
3. **Document environment** — Python version, library versions
4. **Save models** — Use `joblib` or `pickle` to save trained models

## Using the Reference Files

### When to Read Each Reference

**`/references/numpy-advanced.md`** — Read when working with multidimensional arrays, performing linear algebra operations, optimizing numerical computations, or implementing custom algorithms.

**`/references/pandas-advanced.md`** — Read when handling complex data transformations, working with time series, performing advanced grouping operations, or optimizing DataFrame performance.

**`/references/sklearn-comprehensive.md`** — Read when building machine learning pipelines, implementing advanced preprocessing, performing model selection, or working with ensemble methods.

**`/references/visualization-gallery.md`** — Read when creating publication-quality visualizations, building interactive dashboards, or customizing plot aesthetics.

**`/references/end-to-end-projects.md`** — Read when starting a new data science project, structuring workflows, or implementing complete analysis pipelines from data to deployment.