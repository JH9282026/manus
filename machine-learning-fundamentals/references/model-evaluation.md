# Model Evaluation and Validation

Comprehensive guide to assessing model performance and ensuring generalization.

---

## Overview

Model evaluation determines how well a machine learning model performs and whether it will generalize to new data. Proper evaluation prevents overfitting, guides model selection, and ensures reliable deployment.

## Train-Test Split

### Basic Split

**Concept**: Divide data into training and testing sets.

**Typical Ratios**:
- 70-30 or 80-20 split
- Larger training set for small datasets
- Larger test set when data is abundant

**Implementation**:
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```

**Stratification**:
- Preserves class distribution in train/test sets
- Critical for imbalanced datasets
- Use `stratify=y` parameter

### Train-Validation-Test Split

**Three-Way Split**:
- Training (60-70%): Model training
- Validation (15-20%): Hyperparameter tuning, model selection
- Test (15-20%): Final performance evaluation

**Why Three Sets?**
- Prevents overfitting to validation set
- Test set remains completely unseen
- Honest performance estimate

**Rule**: Test set should be used only once, at the very end!

## Cross-Validation

### K-Fold Cross-Validation

**Concept**: Split data into K folds, train on K-1 folds, validate on remaining fold, repeat K times.

**Process**:
1. Divide data into K equal folds
2. For each fold:
   - Train on K-1 folds
   - Validate on held-out fold
3. Average performance across K folds

**Advantages**:
- More robust performance estimate
- Uses all data for both training and validation
- Reduces variance in performance estimate

**Typical K Values**:
- K=5: Good balance, common choice
- K=10: More thorough, higher computational cost
- K=n (Leave-One-Out): Maximum data usage, very expensive

**Implementation**:
```python
from sklearn.model_selection import cross_val_score, KFold

# K-Fold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
print(f"Mean: {scores.mean():.3f}, Std: {scores.std():.3f}")
```

### Stratified K-Fold

**Concept**: Ensures each fold has same class distribution as overall dataset.

**Use When**:
- Classification problems
- Imbalanced classes
- Small datasets

**Implementation**:
```python
from sklearn.model_selection import StratifiedKFold

skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skfold, scoring='f1_weighted')
```

### Time-Series Split

**Concept**: Respects temporal ordering, trains on past, validates on future.

**Process**:
- Fold 1: Train on [1:n], test on [n+1:n+k]
- Fold 2: Train on [1:n+k], test on [n+k+1:n+2k]
- Expanding window preserves temporal order

**Implementation**:
```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
for train_idx, test_idx in tscv.split(X):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
```

## Classification Metrics

### Confusion Matrix

**Structure**:
```
                Predicted
              Pos    Neg
Actual  Pos   TP     FN
        Neg   FP     TN
```

- True Positive (TP): Correctly predicted positive
- True Negative (TN): Correctly predicted negative
- False Positive (FP): Incorrectly predicted positive (Type I error)
- False Negative (FN): Incorrectly predicted negative (Type II error)

**Implementation**:
```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(cm, display_labels=['Negative', 'Positive'])
disp.plot()
```

### Accuracy

**Formula**: (TP + TN) / (TP + TN + FP + FN)

**Interpretation**: Proportion of correct predictions

**When to Use**:
- Balanced classes
- Equal cost of errors

**When NOT to Use**:
- Imbalanced classes (misleading!)
- Different error costs

**Example**: 95% accuracy on 95% negative class is useless (predicting all negative gives same accuracy)

### Precision

**Formula**: TP / (TP + FP)

**Interpretation**: Of all positive predictions, how many were correct?

**When to Use**:
- Cost of false positives is high
- Spam detection (don't want to mark legitimate email as spam)
- Medical diagnosis (don't want to alarm healthy patients)

**Trade-off**: High precision may sacrifice recall

### Recall (Sensitivity, True Positive Rate)

**Formula**: TP / (TP + FN)

**Interpretation**: Of all actual positives, how many did we catch?

**When to Use**:
- Cost of false negatives is high
- Fraud detection (don't want to miss fraud)
- Disease screening (don't want to miss sick patients)

**Trade-off**: High recall may sacrifice precision

### F1 Score

**Formula**: 2 * (Precision * Recall) / (Precision + Recall)

**Interpretation**: Harmonic mean of precision and recall

**When to Use**:
- Need balance between precision and recall
- Imbalanced classes
- Single metric for model comparison

**Variants**:
- F-beta: Weighted harmonic mean, β > 1 favors recall, β < 1 favors precision
- Macro F1: Average F1 across classes (treats all classes equally)
- Weighted F1: Weighted average by class support

**Implementation**:
```python
from sklearn.metrics import precision_score, recall_score, f1_score

precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
```

### ROC Curve and AUC

**ROC (Receiver Operating Characteristic)**:
- Plots True Positive Rate (Recall) vs False Positive Rate
- Shows performance across all classification thresholds
- FPR = FP / (FP + TN)

**AUC (Area Under Curve)**:
- Single number summarizing ROC curve
- Range: 0 to 1 (0.5 = random, 1.0 = perfect)
- Interpretation: Probability that model ranks random positive higher than random negative

**When to Use**:
- Comparing models
- Threshold-independent evaluation
- Imbalanced classes

**Implementation**:
```python
from sklearn.metrics import roc_curve, roc_auc_score, RocCurveDisplay

# Get predicted probabilities
y_proba = model.predict_proba(X_test)[:, 1]

# ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
auc = roc_auc_score(y_test, y_proba)

# Plot
RocCurveDisplay.from_predictions(y_test, y_proba)
```

### Precision-Recall Curve

**Concept**: Plots precision vs recall at different thresholds

**When to Use**:
- Imbalanced datasets (better than ROC)
- When positive class is rare
- Focus on positive class performance

**Average Precision (AP)**:
- Area under precision-recall curve
- Weighted mean of precisions at each threshold

**Implementation**:
```python
from sklearn.metrics import precision_recall_curve, average_precision_score

precision, recall, thresholds = precision_recall_curve(y_test, y_proba)
ap = average_precision_score(y_test, y_proba)
```

### Multi-Class Metrics

**Macro Average**:
- Calculate metric for each class, then average
- Treats all classes equally
- Use when all classes are equally important

**Weighted Average**:
- Calculate metric for each class, average weighted by support
- Accounts for class imbalance
- Use when classes have different importance

**Micro Average**:
- Aggregate TP, FP, FN across all classes, then calculate metric
- Gives more weight to larger classes

**Implementation**:
```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred, 
                           target_names=['Class0', 'Class1', 'Class2']))
```

## Regression Metrics

### Mean Absolute Error (MAE)

**Formula**: (1/n) Σ|y_true - y_pred|

**Interpretation**: Average absolute difference between predictions and actual values

**Characteristics**:
- Same units as target variable
- Robust to outliers
- All errors weighted equally

**When to Use**:
- Outliers should not dominate
- Interpretability important

### Mean Squared Error (MSE)

**Formula**: (1/n) Σ(y_true - y_pred)²

**Interpretation**: Average squared difference

**Characteristics**:
- Penalizes large errors more (squared term)
- Not in original units
- Sensitive to outliers

**When to Use**:
- Large errors are particularly bad
- Optimization (differentiable)

### Root Mean Squared Error (RMSE)

**Formula**: √MSE

**Interpretation**: Square root of MSE

**Characteristics**:
- Same units as target variable
- Penalizes large errors
- Most common regression metric

**When to Use**:
- Standard regression evaluation
- Comparing models on same dataset

### R² Score (Coefficient of Determination)

**Formula**: 1 - (SS_res / SS_tot)
- SS_res: Sum of squared residuals
- SS_tot: Total sum of squares

**Interpretation**: Proportion of variance in target explained by model

**Range**:
- 1.0: Perfect predictions
- 0.0: Model as good as predicting mean
- Negative: Model worse than predicting mean

**When to Use**:
- Comparing models
- Understanding explanatory power
- Communicating to non-technical stakeholders

**Limitations**:
- Can be misleading with non-linear relationships
- Increases with more features (use adjusted R²)

### Mean Absolute Percentage Error (MAPE)

**Formula**: (100/n) Σ|((y_true - y_pred) / y_true)|

**Interpretation**: Average percentage error

**Characteristics**:
- Scale-independent (percentage)
- Interpretable
- Undefined when y_true = 0

**When to Use**:
- Comparing across different scales
- Business reporting (percentages intuitive)

**Implementation**:
```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
```

## Overfitting and Underfitting

### Overfitting

**Symptoms**:
- High training accuracy, low validation/test accuracy
- Large gap between training and validation performance
- Model too complex for data

**Causes**:
- Too many features relative to samples
- Model too complex (deep trees, many parameters)
- Insufficient regularization
- Training too long (neural networks)

**Solutions**:
- Regularization (L1, L2, dropout)
- Reduce model complexity
- More training data
- Cross-validation
- Early stopping
- Feature selection

### Underfitting

**Symptoms**:
- Low training and validation accuracy
- Model too simple for data
- High bias

**Causes**:
- Model too simple
- Insufficient features
- Too much regularization
- Insufficient training

**Solutions**:
- Increase model complexity
- Add more features
- Reduce regularization
- Train longer
- Try different algorithm

### Bias-Variance Trade-off

**Bias**: Error from incorrect assumptions (underfitting)
**Variance**: Error from sensitivity to training data (overfitting)

**Goal**: Minimize total error = Bias² + Variance + Irreducible Error

**Strategies**:
- Simple models: High bias, low variance
- Complex models: Low bias, high variance
- Ensemble methods: Balance both

## Learning Curves

**Concept**: Plot training and validation performance vs training set size

**Interpretation**:
- **High bias (underfitting)**: Both curves plateau at low performance, close together
- **High variance (overfitting)**: Large gap between curves, training performance high
- **Good fit**: Curves converge at high performance

**Use Cases**:
- Diagnose overfitting/underfitting
- Determine if more data would help
- Guide model complexity decisions

**Implementation**:
```python
from sklearn.model_selection import learning_curve

train_sizes, train_scores, val_scores = learning_curve(
    model, X, y, cv=5, train_sizes=np.linspace(0.1, 1.0, 10)
)

plt.plot(train_sizes, train_scores.mean(axis=1), label='Training')
plt.plot(train_sizes, val_scores.mean(axis=1), label='Validation')
plt.legend()
```

## Validation Strategies for Special Cases

### Imbalanced Data

**Stratified Sampling**: Preserve class distribution
**Metrics**: Use F1, precision-recall, ROC-AUC instead of accuracy
**Resampling**: SMOTE, undersampling in training only

### Time-Series Data

**No Random Shuffling**: Respect temporal order
**Walk-Forward Validation**: Train on past, test on future
**Expanding Window**: Increase training set over time

### Small Datasets

**Leave-One-Out CV**: Maximum data usage
**Bootstrapping**: Resample with replacement
**Nested CV**: Outer loop for evaluation, inner for hyperparameter tuning

### Grouped Data

**Group K-Fold**: Ensure same group not in train and test
**Use Case**: Patient data (multiple samples per patient)

## Best Practices

**General**:
- Always use separate test set for final evaluation
- Use cross-validation for robust estimates
- Choose metrics aligned with business objectives
- Report multiple metrics for comprehensive view
- Visualize results (confusion matrix, ROC curve)

**Avoiding Data Leakage**:
- Fit preprocessing on training data only
- No information from test set in training
- Careful with time-series (no future information)

**Hyperparameter Tuning**:
- Use validation set or cross-validation
- Never tune on test set
- Consider nested cross-validation for unbiased estimates

**Reporting**:
- Report mean and standard deviation from CV
- Include confidence intervals
- Show learning curves
- Document all preprocessing steps
