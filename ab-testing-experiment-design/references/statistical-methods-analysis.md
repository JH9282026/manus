# Statistical Methods & Analysis

Comprehensive guide to statistical analysis for A/B testing.

---

## Sample Size Calculation

### Formula for Proportions (Conversion Rate)

For two-sided test comparing two proportions:

```
n = 2 × [(Zα/2 + Zβ)² × p̄(1-p̄)] / δ²
```

Where:
- n = sample size per variant
- Zα/2 = critical value for significance level (1.96 for α=0.05)
- Zβ = critical value for power (0.84 for 80% power)
- p̄ = pooled proportion estimate
- δ = minimum detectable effect (absolute)

### Sample Size Table - Conversion Rate Experiments

| Baseline Rate | 5% Relative MDE | 10% Relative MDE | 20% Relative MDE |
|---------------|-----------------|------------------|------------------|
| 1% | 7,660,000 | 1,920,000 | 480,000 |
| 2% | 3,765,000 | 942,000 | 236,000 |
| 5% | 1,458,000 | 365,000 | 92,000 |
| 10% | 688,000 | 172,000 | 43,000 |
| 20% | 307,000 | 77,000 | 20,000 |
| 50% | 76,000 | 19,000 | 5,000 |

*Per variant, α=0.05, power=80%, two-sided test*

### Formula for Continuous Metrics

```
n = 2 × [(Zα/2 + Zβ)² × σ²] / δ²
```

Where:
- σ² = variance of the metric
- δ = minimum detectable effect (absolute difference in means)

---

## Statistical Tests

### Proportion Comparison (Chi-Square / Z-Test)

**Use when:** Comparing conversion rates between variants

**Test statistic:**
```
Z = (p1 - p2) / √[p̄(1-p̄)(1/n1 + 1/n2)]
```

**Assumptions:**
- Independent observations
- np ≥ 5 and n(1-p) ≥ 5 for normal approximation

### Two-Sample T-Test

**Use when:** Comparing means of continuous metrics

**Test statistic:**
```
t = (x̄1 - x̄2) / √(s²pooled × (1/n1 + 1/n2))
```

**Assumptions:**
- Independent observations
- Normally distributed (relaxed for large n by CLT)
- Equal variances (use Welch's if unequal)

### Welch's T-Test

**Use when:** Means comparison with unequal variances

Preferred over pooled t-test in most A/B scenarios as variance often differs between variants.

### Mann-Whitney U Test

**Use when:** Comparing medians or ranks, non-normal distributions

**Advantages:**
- No normality assumption
- Robust to outliers
- Tests median difference

### Delta Method

**Use when:** Testing ratio metrics (e.g., revenue per click)

Estimate variance of ratio using:
```
Var(X/Y) ≈ (μx/μy)² × [Var(X)/μx² + Var(Y)/μy² - 2Cov(X,Y)/(μx×μy)]
```

### Bootstrap Methods

**Use when:**
- Complex metrics without closed-form variance
- Small sample sizes
- Non-standard test statistics

**Procedure:**
1. Resample with replacement B times (B ≥ 10,000)
2. Calculate test statistic for each resample
3. Construct confidence interval from percentiles

---

## Confidence Intervals

### Interpretation

A 95% CI means: If we repeated this experiment many times, 95% of calculated intervals would contain the true effect.

**NOT:** 95% probability the true effect is in this interval.

### Effect Size Reporting

Always report:
- Point estimate of effect
- 95% confidence interval
- Relative effect (% change from baseline)

Example: "Conversion increased by 0.5 percentage points (95% CI: 0.2 to 0.8), a 10% relative improvement."

---

## Multiple Testing Correction

### When Correction is Needed

| Scenario | Correction Needed? |
|----------|--------------------|
| One primary metric | No |
| Multiple primary metrics | Yes |
| Multiple variants vs control | Yes |
| Pre-specified subgroups | Depends on goal |
| Exploratory subgroups | Report as exploratory |
| Guardrail metrics | No (different purpose) |

### Correction Methods

| Method | Formula | Use When |
|--------|---------|----------|
| Bonferroni | α_adj = α / k | Conservative, any dependency |
| Holm | Sequential rejection | Less conservative than Bonferroni |
| Benjamini-Hochberg | FDR control | Many tests, some false positives OK |
| Šidák | α_adj = 1-(1-α)^(1/k) | Independent tests |

---

## Variance Reduction

### CUPED (Controlled Experiment Using Pre-Experiment Data)

Reduce variance by adjusting for pre-experiment covariates:

```
Y_adjusted = Y - θ × (X - E[X])
```

Where:
- Y = outcome metric
- X = pre-experiment covariate (same metric, prior period)
- θ = Cov(Y, X) / Var(X)

**Typical variance reduction:** 30-50%

### Stratified Sampling

Randomize within strata defined by important covariates:
- Reduces variance from between-strata variation
- Ensures balance on stratification variables

**Typical variance reduction:** 10-30%

### Triggered Analysis

Analyze only users who encountered the treatment:
- Reduces noise from unaffected users
- Increases sensitivity for feature experiments

**Requirements:**
- Clear trigger definition
- Trigger rate similar across variants

---

## Bayesian A/B Testing

### Key Differences from Frequentist

| Aspect | Frequentist | Bayesian |
|--------|-------------|----------|
| Output | p-value, CI | Posterior distribution |
| Interpretation | Long-run error rates | Probability of hypothesis |
| Prior information | Not incorporated | Explicitly included |
| Sample size | Fixed | Can update continuously |
| Decision | Reject/fail to reject | Probability of being best |

### Bayesian Outputs

- **Probability of being best:** P(Treatment > Control)
- **Expected loss:** Expected downside if wrong decision
- **Credible interval:** 95% probability true effect in interval

### When to Use Bayesian

- Need intuitive probability statements
- Want to incorporate prior knowledge
- Continuous monitoring required
- Decision theory framework preferred

---

## Sequential Testing

### The Peeking Problem

Looking at results before reaching planned sample size inflates Type I error.

| Peeks | Actual α at Each Peek | Cumulative α |
|-------|----------------------|---------------|
| 1 (at end) | 5% | 5% |
| 2 | 2.9% | 8% |
| 5 | 1.8% | 14% |
| 10 | 1.2% | 19% |
| Continuous | ~0.1% | ~40% |

### Sequential Testing Methods

**Group Sequential:**
- Pre-specify analysis times
- Adjust α at each look (O'Brien-Fleming, Pocock)
- Maintains overall Type I error

**Always-Valid Inference:**
- Confidence sequences valid at any stopping time
- More conservative but flexible

**mSPRT (Mixture Sequential Probability Ratio Test):**
- Continuous monitoring allowed
- Controls Type I error at any sample size

---

## Analysis Reporting Template

### Required Elements

1. **Sample summary**
   - Users per variant
   - Sample ratio (check for SRM)
   - Key covariate balance

2. **Primary metric results**
   - Control and treatment values
   - Absolute and relative effect
   - Confidence interval
   - p-value

3. **Secondary metrics**
   - Same format as primary
   - Note if multiple testing corrected

4. **Guardrail metrics**
   - Confirm no significant degradation

5. **Validity checks**
   - SRM test
   - AA test (if available)
   - Novelty effect check

6. **Recommendation**
   - Ship / Iterate / Abandon
   - Confidence level
   - Expected impact
