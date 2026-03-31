# Assumptions and Diagnostic Checks in Hypothesis Testing

## Overview
Statistical tests rely on assumptions about data. Violating these assumptions can lead to incorrect conclusions. This guide covers common assumptions, how to check them, and what to do when they're violated.

## Common Assumptions

### Independence
Observations are independent of each other.

**What It Means:**
- One observation doesn't influence another
- No correlation between data points
- Each measurement is separate

**When Violated:**
- Repeated measures on same subjects
- Clustered or nested data
- Time series data
- Spatial correlation

**Consequences:**
- Underestimated standard errors
- Inflated Type I error rate
- Invalid p-values

**How to Check:**
- Study design review
- Durbin-Watson test (time series)
- Residual plots for patterns

**Solutions:**
- Use appropriate models (mixed effects, GEE)
- Account for clustering
- Time series methods
- Adjust standard errors

### Normality
Data follows normal (Gaussian) distribution.

**What It Means:**
- Bell-shaped, symmetric distribution
- Mean = median = mode
- 68-95-99.7 rule applies

**When Required:**
- T-tests (especially small samples)
- ANOVA
- Linear regression (residuals)
- Parametric tests generally

**Less Important When:**
- Large sample sizes (Central Limit Theorem)
- Robust tests used
- Non-parametric alternatives available

**How to Check:**

**Visual Methods:**
- Histogram: Should be bell-shaped
- Q-Q plot: Points should fall on diagonal line
- Boxplot: Check for symmetry and outliers

**Statistical Tests:**
- Shapiro-Wilk test (n < 50)
- Kolmogorov-Smirnov test
- Anderson-Darling test

**Interpretation:**
- p > 0.05: Data consistent with normality
- p ≤ 0.05: Evidence of non-normality
- Visual inspection often more useful than tests

**Solutions:**
- Transformations (log, square root, Box-Cox)
- Non-parametric tests
- Robust methods
- Larger sample size
- Bootstrap methods

### Homogeneity of Variance (Homoscedasticity)
Groups have equal variances.

**What It Means:**
- Spread of data similar across groups
- Variance constant across levels
- No systematic change in variability

**When Required:**
- Independent samples t-test
- ANOVA
- Linear regression
- Pooled variance methods

**How to Check:**

**Visual Methods:**
- Side-by-side boxplots: Similar box sizes
- Residual plots: Random scatter, no funnel shape
- Spread-location plots

**Statistical Tests:**
- Levene's test (robust to non-normality)
- Bartlett's test (sensitive to non-normality)
- F-test (two groups only)

**Rule of Thumb:**
- Largest variance / smallest variance < 3 is acceptable

**Solutions:**
- Welch's t-test (unequal variances)
- Welch's ANOVA
- Transformations
- Weighted least squares
- Robust methods

### Linearity
Relationship between variables is linear.

**What It Means:**
- Straight-line relationship
- Constant rate of change
- No curves or bends

**When Required:**
- Linear regression
- Pearson correlation
- ANCOVA

**How to Check:**
- Scatterplots: Look for linear pattern
- Residual plots: Random scatter around zero
- Component-plus-residual plots

**Solutions:**
- Polynomial terms
- Transformations
- Non-linear regression
- Spline methods
- Generalized additive models

### No Multicollinearity
Predictor variables not highly correlated (regression).

**What It Means:**
- Independent variables independent of each other
- No redundant predictors
- Each predictor adds unique information

**Consequences:**
- Unstable coefficient estimates
- Large standard errors
- Difficulty interpreting effects
- Inflated variance inflation factors

**How to Check:**
- Correlation matrix: r > 0.8 problematic
- Variance Inflation Factor (VIF): VIF > 10 problematic
- Tolerance: < 0.1 problematic
- Condition index: > 30 problematic

**Solutions:**
- Remove redundant variables
- Combine correlated variables
- Principal components analysis
- Ridge regression
- Collect more data

## Diagnostic Procedures

### For T-Tests

**Assumptions to Check:**
1. Independence
2. Normality (especially n < 30)
3. Equal variances (independent samples)

**Procedure:**
```
1. Check independence through design
2. Create histograms and Q-Q plots
3. Run Shapiro-Wilk test
4. Conduct Levene's test (independent samples)
5. Examine boxplots for outliers
```

**Decision Tree:**
- Assumptions met → Proceed with t-test
- Non-normal, n < 30 → Mann-Whitney U or Wilcoxon
- Unequal variances → Welch's t-test
- Outliers present → Consider robust methods or transformation

### For ANOVA

**Assumptions to Check:**
1. Independence
2. Normality within each group
3. Homogeneity of variance across groups

**Procedure:**
```
1. Check independence through design
2. Create Q-Q plots for each group
3. Run Shapiro-Wilk for each group
4. Conduct Levene's test
5. Examine residual plots
```

**Decision Tree:**
- Assumptions met → Proceed with ANOVA
- Non-normal → Kruskal-Wallis test
- Unequal variances → Welch's ANOVA
- Both violated → Non-parametric or transformation

### For Regression

**Assumptions to Check:**
1. Linearity
2. Independence of errors
3. Homoscedasticity of errors
4. Normality of errors
5. No multicollinearity

**Procedure:**
```
1. Create scatterplots (linearity)
2. Plot residuals vs. fitted values (homoscedasticity)
3. Q-Q plot of residuals (normality)
4. Calculate VIF (multicollinearity)
5. Durbin-Watson test (independence)
6. Check for influential points (Cook's distance)
```

**Residual Plots:**
- Random scatter → Assumptions met
- Funnel shape → Heteroscedasticity
- Curved pattern → Non-linearity
- Clusters → Independence violation

### For Chi-Square Tests

**Assumptions to Check:**
1. Independence
2. Expected frequencies ≥ 5

**Procedure:**
```
1. Check independence through design
2. Calculate expected frequencies
3. Verify all expected frequencies ≥ 5
```

**Solutions:**
- Expected < 5 → Fisher's exact test
- Combine categories if meaningful
- Collect more data

## Transformations

### Common Transformations

**Log Transformation**
- Use: Right-skewed data
- Formula: log(x) or ln(x)
- Note: Requires x > 0
- Effect: Reduces right skew, stabilizes variance

**Square Root Transformation**
- Use: Count data, Poisson-distributed
- Formula: √x
- Note: Works for x ≥ 0
- Effect: Moderate skew reduction

**Reciprocal Transformation**
- Use: Severe right skew
- Formula: 1/x
- Note: Changes interpretation
- Effect: Strong skew reduction

**Box-Cox Transformation**
- Use: Find optimal transformation
- Formula: (x^λ - 1) / λ
- Note: Automated selection of λ
- Effect: Maximizes normality

**Arcsine Transformation**
- Use: Proportions, percentages
- Formula: arcsin(√p)
- Effect: Stabilizes variance for proportions

### When to Transform

**Good Reasons:**
- Improve normality
- Stabilize variance
- Linearize relationships
- Meet test assumptions

**Cautions:**
- Changes interpretation
- May not help
- Can create new problems
- Report both original and transformed

## Outliers and Influential Points

### Identifying Outliers

**Visual Methods:**
- Boxplots: Points beyond whiskers
- Scatterplots: Points far from pattern
- Residual plots: Extreme residuals

**Statistical Methods:**
- Z-scores: |z| > 3 potential outlier
- IQR method: < Q1 - 1.5×IQR or > Q3 + 1.5×IQR
- Grubbs' test
- Dixon's test

### Influential Points (Regression)

**Cook's Distance**
- Measures influence on regression
- D > 1 or D > 4/n concerning
- Combines leverage and residual

**Leverage**
- Hat values
- High leverage: far from mean of predictors
- h > 2(k+1)/n concerning

**DFFITS**
- Change in fitted value when point removed
- |DFFITS| > 2√(k/n) concerning

### Handling Outliers

**Steps:**
1. Verify data entry (not error)
2. Understand why outlier exists
3. Consider context and domain knowledge
4. Assess impact on results

**Options:**
- Keep if legitimate data point
- Remove if data error
- Winsorize (replace with less extreme value)
- Use robust methods
- Report sensitivity analysis

**Never:**
- Remove just to get significance
- Remove without justification
- Fail to report removal

## Robust Methods

### When to Use
- Assumptions violated
- Outliers present
- Non-normal data
- Small samples
- Exploratory analysis

### Robust Alternatives

**Robust T-Tests:**
- Yuen's test (trimmed means)
- Percentile bootstrap
- Permutation tests

**Robust ANOVA:**
- Welch's ANOVA
- Kruskal-Wallis test
- Trimmed means ANOVA

**Robust Regression:**
- M-estimators
- Least absolute deviations
- Quantile regression
- Robust standard errors

**Robust Correlation:**
- Spearman's rho
- Kendall's tau
- Winsorized correlation

## Reporting Assumption Checks

### In Methods Section
\"Assumptions of normality and homogeneity of variance were assessed through visual inspection of Q-Q plots and histograms, and confirmed with Shapiro-Wilk and Levene's tests, respectively. All assumptions were met (p > 0.05 for all tests).\"

### When Assumptions Violated
\"Visual inspection and Shapiro-Wilk tests indicated non-normal distributions in both groups (p < 0.05). Therefore, a Mann-Whitney U test was used instead of an independent samples t-test.\"

### For Transformations
\"Data were log-transformed to meet normality assumptions. Analysis was conducted on transformed data, and results were back-transformed for interpretation.\"

## Best Practices

1. **Check Assumptions:** Always verify before analysis
2. **Use Multiple Methods:** Combine visual and statistical checks
3. **Prioritize Visual:** Plots often more informative than tests
4. **Consider Sample Size:** Large samples make tests overly sensitive
5. **Document Decisions:** Record assumption checks and decisions
6. **Report Violations:** Be transparent about assumption violations
7. **Use Appropriate Alternatives:** Switch to robust methods when needed
8. **Don't P-Hack:** Don't try multiple transformations to get significance
9. **Consult Expert:** Get statistical advice for complex situations
10. **Sensitivity Analysis:** Test robustness of conclusions

## References

- Penn State. \"Checking Assumptions\" https://online.stat.psu.edu/stat500/lesson/7
- UCLA Statistical Consulting. \"Regression Diagnostics\" https://stats.oarc.ucla.edu/r/dae/robust-regression/
- Field, A. (2013). Discovering Statistics Using IBM SPSS Statistics
