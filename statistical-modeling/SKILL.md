---
name: statistical-modeling
description: "Build and validate statistical models including linear regression, logistic regression, GLMs, mixed effects models, and survival analysis. Use for hypothesis testing, predictive modeling, causal inference, model diagnostics, and statistical inference with proper validation techniques."
---

# Statistical Modeling

Build, validate, and interpret statistical models for inference and prediction.

## Overview

Statistical modeling uses mathematical frameworks to represent relationships between variables, test hypotheses, and make predictions. This skill covers regression techniques, generalized linear models, model diagnostics, validation methods, and best practices for statistical inference. Applications span research, business analytics, healthcare, and social sciences.

## Model Types

| Model Type | Response Variable | Link Function | Use Cases |
|------------|-------------------|---------------|-----------|
| Linear Regression | Continuous | Identity | Sales prediction, price modeling |
| Logistic Regression | Binary | Logit | Classification, probability estimation |
| Poisson Regression | Count | Log | Event counts, rare events |
| Cox Regression | Time-to-event | - | Survival analysis, churn prediction |
| Mixed Effects | Continuous/Binary | Various | Hierarchical data, repeated measures |

## Linear Regression

### Simple Linear Regression

Model: Y = β₀ + β₁X + ε

```python
import statsmodels.api as sm
import numpy as np

# Add intercept
X = sm.add_constant(X)

# Fit model
model = sm.OLS(y, X)
results = model.fit()

# Summary
print(results.summary())

# Predictions
predictions = results.predict(X_new)

# Confidence intervals
conf_int = results.conf_int(alpha=0.05)
```

### Multiple Linear Regression

Model: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ + ε

```python
# Multiple predictors
X = df[['feature1', 'feature2', 'feature3']]
X = sm.add_constant(X)
y = df['target']

model = sm.OLS(y, X)
results = model.fit()

# Coefficients
print(results.params)

# P-values
print(results.pvalues)

# R-squared
print(f"R-squared: {results.rsquared}")
print(f"Adjusted R-squared: {results.rsquared_adj}")
```

### Assumptions

1. **Linearity** — Relationship between X and Y is linear
2. **Independence** — Observations are independent
3. **Homoscedasticity** — Constant variance of residuals
4. **Normality** — Residuals are normally distributed
5. **No multicollinearity** — Predictors are not highly correlated

### Diagnostics

```python
import matplotlib.pyplot as plt

# Residual plot
plt.scatter(results.fittedvalues, results.resid)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Fitted')
plt.show()

# Q-Q plot
from scipy import stats
stats.probplot(results.resid, dist="norm", plot=plt)
plt.title('Normal Q-Q Plot')
plt.show()

# Influence plot
from statsmodels.graphics.regressionplots import influence_plot
influence_plot(results, criterion="cooks")
plt.show()

# VIF for multicollinearity
from statsmodels.stats.outliers_influence import variance_inflation_factor

vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif_data)
```

## Logistic Regression

### Binary Logistic Regression

Model: log(p/(1-p)) = β₀ + β₁X₁ + ... + βₚXₚ

```python
# Fit logistic regression
model = sm.Logit(y, X)
results = model.fit()

print(results.summary())

# Odds ratios
odds_ratios = np.exp(results.params)
print(odds_ratios)

# Predictions (probabilities)
probabilities = results.predict(X_new)

# Classification
predictions = (probabilities > 0.5).astype(int)
```

### Model Evaluation

```python
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)
print(cm)

# Classification report
print(classification_report(y_true, y_pred))

# ROC curve
fpr, tpr, thresholds = roc_curve(y_true, y_prob)
auc = roc_auc_score(y_true, y_prob)

plt.plot(fpr, tpr, label=f'AUC = {auc:.3f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

## Generalized Linear Models (GLM)

### Poisson Regression

For count data:

```python
# Fit Poisson regression
model = sm.GLM(y, X, family=sm.families.Poisson())
results = model.fit()

print(results.summary())

# Check for overdispersion
print(f"Pearson chi2/df: {results.pearson_chi2 / results.df_resid}")

# If overdispersed, use Negative Binomial
model_nb = sm.GLM(y, X, family=sm.families.NegativeBinomial())
results_nb = model_nb.fit()
```

### Gamma Regression

For positive continuous data:

```python
model = sm.GLM(y, X, family=sm.families.Gamma(link=sm.families.links.log()))
results = model.fit()
```

## Model Selection

### Information Criteria

```python
# AIC (Akaike Information Criterion)
print(f"AIC: {results.aic}")

# BIC (Bayesian Information Criterion)
print(f"BIC: {results.bic}")

# Lower is better
# BIC penalizes complexity more than AIC
```

### Stepwise Selection

```python
# Forward selection
def forward_selection(X, y, significance_level=0.05):
    initial_features = []
    best_features = list(initial_features)
    
    while True:
        remaining_features = list(set(X.columns) - set(best_features))
        new_pval = pd.Series(index=remaining_features, dtype=float)
        
        for new_column in remaining_features:
            model = sm.OLS(y, sm.add_constant(X[best_features + [new_column]])).fit()
            new_pval[new_column] = model.pvalues[new_column]
        
        min_p_value = new_pval.min()
        if min_p_value < significance_level:
            best_features.append(new_pval.idxmin())
        else:
            break
    
    return best_features

selected_features = forward_selection(X, y)
```

## Model Validation

### Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Fit on training data
model = sm.OLS(y_train, sm.add_constant(X_train))
results = model.fit()

# Evaluate on test data
y_pred = results.predict(sm.add_constant(X_test))
test_mse = ((y_test - y_pred) ** 2).mean()
test_r2 = 1 - (((y_test - y_pred) ** 2).sum() / ((y_test - y_test.mean()) ** 2).sum())

print(f"Test MSE: {test_mse}")
print(f"Test R²: {test_r2}")
```

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=5, scoring='r2')

print(f"CV R² scores: {scores}")
print(f"Mean R²: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

### Bootstrap Validation

```python
from sklearn.utils import resample

n_iterations = 1000
stats = []

for i in range(n_iterations):
    # Resample with replacement
    X_boot, y_boot = resample(X, y, random_state=i)
    
    # Fit model
    model = sm.OLS(y_boot, sm.add_constant(X_boot))
    results = model.fit()
    
    # Store statistic
    stats.append(results.params[1])  # Coefficient of interest

# Bootstrap confidence interval
ci_lower = np.percentile(stats, 2.5)
ci_upper = np.percentile(stats, 97.5)
print(f"95% Bootstrap CI: [{ci_lower:.3f}, {ci_upper:.3f}]")
```

## Mixed Effects Models

### Random Intercept Model

```python
import statsmodels.formula.api as smf

# Fit mixed effects model
model = smf.mixedlm("y ~ x1 + x2", data=df, groups=df["group_id"])
results = model.fit()

print(results.summary())

# Random effects
print(results.random_effects)
```

### Random Slope Model

```python
# Random intercept and slope
model = smf.mixedlm(
    "y ~ x1 + x2",
    data=df,
    groups=df["group_id"],
    re_formula="~x1"
)
results = model.fit()
```

## Survival Analysis

### Kaplan-Meier Estimator

```python
from lifelines import KaplanMeierFitter

kmf = KaplanMeierFitter()
kmf.fit(durations=df['time'], event_observed=df['event'])

# Plot survival function
kmf.plot_survival_function()
plt.title('Kaplan-Meier Survival Curve')
plt.show()

# Median survival time
print(f"Median survival: {kmf.median_survival_time_}")
```

### Cox Proportional Hazards

```python
from lifelines import CoxPHFitter

cph = CoxPHFitter()
cph.fit(df, duration_col='time', event_col='event')

# Summary
print(cph.summary)

# Hazard ratios
print(cph.hazard_ratios_)

# Plot
cph.plot()
plt.show()

# Check proportional hazards assumption
cph.check_assumptions(df, p_value_threshold=0.05)
```

## Best Practices

### Model Building

1. **Start with exploratory analysis** — Understand data before modeling
2. **Check assumptions** — Validate model assumptions
3. **Use domain knowledge** — Inform feature selection
4. **Avoid overfitting** — Balance complexity and performance

### Interpretation

1. **Report effect sizes** — Not just p-values
2. **Provide confidence intervals** — Quantify uncertainty
3. **Consider practical significance** — Statistical ≠ practical
4. **Visualize results** — Plots aid interpretation

### Validation

1. **Use holdout data** — Test on unseen data
2. **Cross-validate** — Assess stability
3. **Check residuals** — Diagnose model fit
4. **Compare models** — Use information criteria

## Using the Reference Files

### When to Read Each Reference

**`/references/regression-advanced.md`** — Read when building complex regression models, handling violations of assumptions, or implementing regularization.

**`/references/glm-comprehensive.md`** — Read when working with non-normal response variables, choosing link functions, or diagnosing GLM fit.

**`/references/model-validation-techniques.md`** — Read when validating models, implementing cross-validation strategies, or assessing predictive performance.

**`/references/mixed-effects-survival.md`** — Read when analyzing hierarchical data, repeated measures, or time-to-event outcomes.

## References

- [Glm Comprehensive](references/glm-comprehensive.md)
- [Mixed Effects Survival](references/mixed-effects-survival.md)
- [Model Validation Techniques](references/model-validation-techniques.md)
- [Regression Advanced](references/regression-advanced.md)
