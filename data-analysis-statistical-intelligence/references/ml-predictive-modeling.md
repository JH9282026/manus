# Machine Learning & Predictive Modeling

## Classification Models

### Logistic Regression
- Best for: Binary classification, interpretable results
- Strengths: Fast, interpretable, probabilistic output
- Weaknesses: Assumes linear decision boundary

### Decision Trees
- Best for: Non-linear relationships, interpretability
- Strengths: No assumptions, handles mixed data types, visual
- Weaknesses: Overfitting, instability

### Random Forest
- Best for: General-purpose classification, feature importance
- Strengths: Robust, handles high dimensions, low variance
- Key hyperparameters: n_estimators (100-500), max_depth, min_samples_split

### Gradient Boosting (XGBoost, LightGBM)
- Best for: Maximum predictive accuracy, structured data
- Strengths: State-of-the-art performance, handles missing data
- Key hyperparameters: learning_rate (0.01-0.3), max_depth (3-8), n_estimators

### SVM
- Best for: High-dimensional data, clear margin of separation
- Strengths: Effective in high dimensions, memory efficient
- Weaknesses: Slow on large datasets, sensitive to scaling

---

## Feature Engineering

### Numeric Features
- **Standardization**: z = (x - mean) / std — Use for distance-based models
- **Min-Max Normalization**: (x - min) / (max - min) — Scale to [0,1]
- **Log Transform**: Reduce right skew — Use for exponential distributions
- **Binning**: Convert continuous to categorical — Use for non-linear relationships
- **Polynomial**: Create x², x³, interaction terms

### Categorical Features
- **One-Hot Encoding**: Create binary columns per category — Use for nominal data
- **Label Encoding**: Map categories to integers — Use for ordinal data or tree models
- **Target Encoding**: Replace category with mean of target — Use with regularization
- **Frequency Encoding**: Replace with occurrence count — Useful for high cardinality

### Datetime Features
- Extract: year, month, day, day_of_week, hour, minute
- Calculate: days_since_event, time_until_deadline
- Cyclical encoding: sin/cos transformation for periodic features

### Text Features
- Bag of Words / TF-IDF for basic text representation
- Word embeddings (Word2Vec, GloVe) for semantic representation
- Sentence embeddings for document-level features

---

## Model Evaluation

### Cross-Validation Strategies

| Method | Description | Use When |
|--------|-------------|----------|
| K-Fold (k=5 or 10) | Split into k folds, train on k-1, test on 1 | General purpose |
| Stratified K-Fold | Maintain class proportions | Imbalanced classes |
| Time Series Split | Expanding window, no future data leakage | Time-dependent data |
| Leave-One-Out | Each sample as test set | Very small datasets |
| Group K-Fold | Keep groups together | Grouped/hierarchical data |

### Classification Metrics

| Metric | Formula | Optimize When |
|--------|---------|---------------|
| Accuracy | (TP+TN)/(TP+TN+FP+FN) | Balanced classes |
| Precision | TP/(TP+FP) | False positives costly (spam) |
| Recall | TP/(TP+FN) | False negatives costly (medical) |
| F1-Score | 2×(P×R)/(P+R) | Balance precision/recall |
| AUC-ROC | Area under ROC curve | Ranking quality |

### Handling Imbalanced Data

| Technique | Description |
|-----------|-------------|
| SMOTE | Synthetic oversampling of minority class |
| Random undersampling | Remove majority class samples |
| Class weights | Penalize misclassification of minority class |
| Threshold tuning | Adjust decision threshold from 0.5 |
| Ensemble methods | Balanced random forest, EasyEnsemble |

---

## Hyperparameter Tuning

| Method | Description | Best For |
|--------|-------------|----------|
| Grid Search | Exhaustive search over parameter grid | Small search space |
| Random Search | Random combinations from distributions | Large search space |
| Bayesian Optimization | Sequential model-based optimization | Expensive evaluations |
| Optuna/Hyperopt | Efficient Bayesian with pruning | Production tuning |
