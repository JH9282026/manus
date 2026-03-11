# Statistical Methods & Testing

## Descriptive Statistics

### Measures of Central Tendency
- **Mean**: Sum of values / count. Sensitive to outliers. Use for symmetric distributions.
- **Median**: Middle value. Robust to outliers. Use for skewed distributions.
- **Mode**: Most frequent value. Use for categorical data or multimodal distributions.

### Measures of Dispersion
- **Range**: Max - Min. Simplest but most sensitive to outliers.
- **IQR**: Q3 - Q1. Robust measure of spread.
- **Variance**: Average squared deviation from mean.
- **Standard Deviation**: Square root of variance. Same units as data.
- **Coefficient of Variation**: (SD / Mean) × 100. Compare variability across different scales.

### Distribution Shape
- **Skewness**: 0 = symmetric, positive = right tail, negative = left tail
- **Kurtosis**: 3 = normal (mesokurtic), >3 = heavy tails (leptokurtic), <3 = light tails (platykurtic)

---

## Hypothesis Testing Framework

### Step-by-Step Process

1. **State hypotheses**: H₀ (null — no effect) and H₁ (alternative — effect exists)
2. **Choose significance level**: α = 0.05 (standard), 0.01 (stringent), 0.10 (exploratory)
3. **Select test**: Based on data type, sample size, and assumptions
4. **Check assumptions**: Normality, independence, homogeneity of variance
5. **Calculate test statistic**: t, F, χ², z, U, etc.
6. **Determine p-value**: Probability of observing result if H₀ is true
7. **Make decision**: Reject H₀ if p < α
8. **Report effect size**: Practical significance beyond statistical significance

### Common Statistical Tests

**t-Tests**:
- Independent samples: Compare means of two groups
- Paired samples: Compare means of same group at two times
- One-sample: Compare sample mean to known value
- Assumptions: Normality (or n > 30), independence, homogeneity of variance

**ANOVA**:
- One-way: Compare means across 3+ groups on one factor
- Two-way: Two factors simultaneously, test interaction effects
- Repeated measures: Same subjects measured multiple times
- Post-hoc tests: Tukey HSD, Bonferroni for pairwise comparisons

**Chi-Square Tests**:
- Goodness of fit: Does observed distribution match expected?
- Test of independence: Are two categorical variables related?
- Assumption: Expected frequency ≥ 5 in each cell

### Effect Size Measures

| Test | Effect Size | Small | Medium | Large |
|------|------------|-------|--------|-------|
| t-test | Cohen's d | 0.2 | 0.5 | 0.8 |
| ANOVA | Eta squared (η²) | 0.01 | 0.06 | 0.14 |
| Correlation | r | 0.1 | 0.3 | 0.5 |
| Chi-square | Cramér's V | 0.1 | 0.3 | 0.5 |

---

## Regression Analysis

### Linear Regression
- **Assumptions**: Linearity, independence, homoscedasticity, normality of residuals, no multicollinearity
- **Diagnostics**: Residual plots, Q-Q plot, VIF for multicollinearity, Durbin-Watson for autocorrelation
- **Feature selection**: Forward/backward stepwise, LASSO regularization, AIC/BIC criteria

### Logistic Regression
- **Use**: Binary outcome prediction (yes/no, churn/retain, buy/not buy)
- **Output**: Probability (0-1), classified via threshold (typically 0.5)
- **Interpretation**: Odds ratios — exp(coefficient) = multiplicative change in odds
- **Evaluation**: Confusion matrix, ROC curve, AUC

### Regularized Regression
- **Ridge (L2)**: Shrinks coefficients, handles multicollinearity, keeps all features
- **LASSO (L1)**: Shrinks coefficients to zero, performs feature selection
- **Elastic Net**: Combines L1 and L2, best of both approaches

---

## Confidence Intervals

**Interpretation**: "We are 95% confident the true parameter lies within this interval."

**Width factors**:
- Confidence level (higher = wider)
- Sample size (larger = narrower)
- Variability (more = wider)

**Common CIs**:
- Mean: x̄ ± t(α/2) × (s/√n)
- Proportion: p̂ ± z(α/2) × √(p̂(1-p̂)/n)
- Difference in means: (x̄₁ - x̄₂) ± t × SE
