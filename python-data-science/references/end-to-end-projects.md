# End-to-End Data Science Projects

Complete workflows for data science projects from data to deployment.

---

## Project Structure

```
project/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── model.py
│   └── utils.py
├── models/
│   └── trained_model.pkl
├── reports/
│   └── figures/
├── requirements.txt
└── README.md
```

---

## Example: Customer Churn Prediction

### 1. Data Loading

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/raw/customers.csv')

# Initial exploration
print(df.info())
print(df.describe())
print(df.isnull().sum())
```

### 2. Exploratory Data Analysis

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Distribution of target
sns.countplot(data=df, x='churn')
plt.title('Churn Distribution')
plt.show()

# Correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlations')
plt.show()

# Feature distributions by churn
for col in df.select_dtypes(include=[np.number]).columns:
    plt.figure(figsize=(10, 4))
    sns.boxplot(data=df, x='churn', y=col)
    plt.title(f'{col} by Churn')
    plt.show()
```

### 3. Data Preprocessing

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Handle missing values
df = df.fillna(df.median())

# Encode categorical variables
le = LabelEncoder()
for col in df.select_dtypes(include=['object']).columns:
    if col != 'churn':
        df[col] = le.fit_transform(df[col])

# Split features and target
X = df.drop('churn', axis=1)
y = df['churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### 4. Model Training

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Cross-validation
cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
print(f"CV Accuracy: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")
```

### 5. Model Evaluation

```python
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Predictions
y_pred = model.predict(X_test_scaled)
y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]

# Metrics
print(classification_report(y_test, y_pred))
print(f"ROC AUC: {roc_auc_score(y_test, y_pred_proba):.3f}")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()
```

### 6. Model Deployment

```python
import joblib

# Save model and scaler
joblib.dump(model, 'models/churn_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')

# Load and use
loaded_model = joblib.load('models/churn_model.pkl')
loaded_scaler = joblib.load('models/scaler.pkl')

# Predict on new data
new_data_scaled = loaded_scaler.transform(new_data)
predictions = loaded_model.predict(new_data_scaled)
```
