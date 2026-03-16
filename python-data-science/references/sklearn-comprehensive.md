# Scikit-learn Comprehensive Guide

Complete guide to machine learning with Scikit-learn.

---

## Model Selection

### Classification Algorithms

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# Logistic Regression
model = LogisticRegression(max_iter=1000, random_state=42)

# Decision Tree
model = DecisionTreeClassifier(max_depth=5, random_state=42)

# Random Forest
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)

# Gradient Boosting
model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)

# Support Vector Machine
model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)

# K-Nearest Neighbors
model = KNeighborsClassifier(n_neighbors=5)

# Naive Bayes
model = GaussianNB()
```

### Regression Algorithms

```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR

# Linear Regression
model = LinearRegression()

# Ridge Regression (L2 regularization)
model = Ridge(alpha=1.0)

# Lasso Regression (L1 regularization)
model = Lasso(alpha=1.0)

# Elastic Net (L1 + L2)
model = ElasticNet(alpha=1.0, l1_ratio=0.5)

# Decision Tree
model = DecisionTreeRegressor(max_depth=5, random_state=42)

# Random Forest
model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)

# Gradient Boosting
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)

# Support Vector Regression
model = SVR(kernel='rbf', C=1.0, gamma='scale')
```

---

## Preprocessing

### Scaling and Normalization

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, Normalizer

# StandardScaler: mean=0, std=1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# MinMaxScaler: range [0, 1]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_train)

# RobustScaler: robust to outliers
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X_train)

# Normalizer: normalize samples to unit norm
normalizer = Normalizer(norm='l2')
X_normalized = normalizer.fit_transform(X)
```

### Encoding Categorical Variables

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

# LabelEncoder: for target variable
le = LabelEncoder()
y_encoded = le.fit_transform(y)
y_decoded = le.inverse_transform(y_encoded)

# OneHotEncoder: for features
ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
X_encoded = ohe.fit_transform(X_categorical)

# OrdinalEncoder: for ordinal features
oe = OrdinalEncoder(categories=[['low', 'medium', 'high']])
X_encoded = oe.fit_transform(X_ordinal)
```

### Feature Engineering

```python
from sklearn.preprocessing import PolynomialFeatures, PowerTransformer
from sklearn.feature_selection import SelectKBest, f_classif, RFE

# Polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Power transformation (Box-Cox, Yeo-Johnson)
pt = PowerTransformer(method='yeo-johnson')
X_transformed = pt.fit_transform(X)

# Feature selection - SelectKBest
selector = SelectKBest(score_func=f_classif, k=10)
X_selected = selector.fit_transform(X, y)

# Recursive Feature Elimination
rfe = RFE(estimator=RandomForestClassifier(), n_features_to_select=10)
X_selected = rfe.fit_transform(X, y)
```

---

## Model Evaluation

### Classification Metrics

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve
)

# Basic metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='weighted')
recall = recall_score(y_true, y_pred, average='weighted')
f1 = f1_score(y_true, y_pred, average='weighted')

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Classification report
report = classification_report(y_true, y_pred)

# ROC AUC
auc = roc_auc_score(y_true, y_pred_proba)
fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba)
```

### Regression Metrics

```python
from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score,
    mean_absolute_percentage_error, explained_variance_score
)

# Mean Squared Error
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)

# Mean Absolute Error
mae = mean_absolute_error(y_true, y_pred)

# R-squared
r2 = r2_score(y_true, y_pred)

# Mean Absolute Percentage Error
mape = mean_absolute_percentage_error(y_true, y_pred)

# Explained Variance
ev = explained_variance_score(y_true, y_pred)
```

---

## Cross-Validation

### Cross-Validation Strategies

```python
from sklearn.model_selection import (
    cross_val_score, cross_validate, KFold, StratifiedKFold,
    TimeSeriesSplit, LeaveOneOut
)

# Simple cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

# Cross-validate with multiple metrics
scoring = ['accuracy', 'precision', 'recall', 'f1']
scores = cross_validate(model, X, y, cv=5, scoring=scoring)

# K-Fold
kf = KFold(n_splits=5, shuffle=True, random_state=42)
for train_idx, val_idx in kf.split(X):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]

# Stratified K-Fold (preserves class distribution)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for train_idx, val_idx in skf.split(X, y):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]

# Time Series Split
tscv = TimeSeriesSplit(n_splits=5)
for train_idx, val_idx in tscv.split(X):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]

# Leave-One-Out
loo = LeaveOneOut()
scores = cross_val_score(model, X, y, cv=loo)
```

---

## Hyperparameter Tuning

### Grid Search

```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Grid search
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train, y_train)

# Best parameters and score
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_}")

# Best model
best_model = grid_search.best_estimator_
```

### Randomized Search

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

# Define parameter distributions
param_dist = {
    'n_estimators': randint(100, 500),
    'max_depth': randint(10, 50),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10),
    'max_features': uniform(0.1, 0.9)
}

# Randomized search
random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_dist,
    n_iter=50,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42,
    verbose=1
)

random_search.fit(X_train, y_train)
```

---

## Pipelines

### Basic Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

# Create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=10)),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train pipeline
pipeline.fit(X_train, y_train)

# Predict
y_pred = pipeline.predict(X_test)

# Access pipeline steps
scaler = pipeline.named_steps['scaler']
pca = pipeline.named_steps['pca']
classifier = pipeline.named_steps['classifier']
```

### Pipeline with GridSearchCV

```python
# Define parameter grid for pipeline
param_grid = {
    'pca__n_components': [5, 10, 15, 20],
    'classifier__n_estimators': [100, 200, 300],
    'classifier__max_depth': [10, 20, 30]
}

# Grid search on pipeline
grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)
```

### ColumnTransformer

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Define transformers for different column types
numeric_features = ['age', 'income', 'score']
categorical_features = ['category', 'region']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# Create pipeline with preprocessor
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

pipeline.fit(X_train, y_train)
```

---

## Ensemble Methods

### Voting Classifier

```python
from sklearn.ensemble import VotingClassifier

# Create base models
model1 = LogisticRegression(random_state=42)
model2 = RandomForestClassifier(random_state=42)
model3 = SVC(probability=True, random_state=42)

# Hard voting
voting_clf = VotingClassifier(
    estimators=[('lr', model1), ('rf', model2), ('svc', model3)],
    voting='hard'
)

# Soft voting (uses predicted probabilities)
voting_clf = VotingClassifier(
    estimators=[('lr', model1), ('rf', model2), ('svc', model3)],
    voting='soft'
)

voting_clf.fit(X_train, y_train)
```

### Stacking

```python
from sklearn.ensemble import StackingClassifier

# Base models
base_models = [
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('gb', GradientBoostingClassifier(n_estimators=100, random_state=42)),
    ('svc', SVC(probability=True, random_state=42))
]

# Meta-model
meta_model = LogisticRegression()

# Stacking classifier
stacking_clf = StackingClassifier(
    estimators=base_models,
    final_estimator=meta_model,
    cv=5
)

stacking_clf.fit(X_train, y_train)
```
