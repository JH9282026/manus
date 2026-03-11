# Statistical Methods for A/B Testing

Detailed guidance on statistical analysis for experiments.

---

## Hypothesis Testing Framework

### Setup
- **H₀ (Null)**: No difference between variants
- **H₁ (Alternative)**: Meaningful difference exists
- **α (Significance)**: False positive rate (typically 0.05)
- **β (Type II Error)**: False negative rate (typically 0.20)

### Decision Rules
- If p-value < α: Reject null hypothesis
- If p-value ≥ α: Fail to reject null hypothesis

---

## Test Selection Guide

| Data Type | Test | When to Use |
|-----------|------|-------------|
| Continuous, normal | t-test | Revenue, time metrics |
| Continuous, non-normal | Mann-Whitney | Skewed distributions |
| Proportions | Chi-square | Conversion rates |
| Rates | Poisson test | Count data |
| Multiple groups | ANOVA | 3+ variants |

---

## Sample Size Formulas

### For Proportions
```
n = 2 × (Zα/2 + Zβ)² × p̄(1 - p̄) / (p₁ - p₂)²

Where:
- Zα/2 = 1.96 for 95% confidence
- Zβ = 0.84 for 80% power
- p̄ = pooled proportion
```

### For Means
```
n = 2 × (Zα/2 + Zβ)² × σ² / Δ²

Where:
- σ = standard deviation
- Δ = minimum detectable difference
```

---

## Confidence Intervals

Always report effect sizes with confidence intervals:

### For Proportions
CI = (p₁ - p₂) ± Zα/2 × SE

### For Means
CI = (μ₁ - μ₂) ± tα/2 × SE

---

## Multiple Testing Correction

### Bonferroni Correction
Adjusted α = α / number of tests

### Holm-Bonferroni
Sequentially adjusted thresholds

### False Discovery Rate (FDR)
Control expected proportion of false positives

---

## Bayesian Approach

### Benefits
- Probability of hypothesis being true
- Intuitive interpretation
- Built-in stopping rules

### Outputs
- Posterior probability
- Credible intervals
- Expected loss

---

## Variance Reduction Techniques

### CUPED (Controlled-experiment Using Pre-Experiment Data)
Use pre-experiment data to reduce variance and increase sensitivity.

### Stratified Sampling
Balance covariates across variants.

### Regression Adjustment
Control for confounding variables.
