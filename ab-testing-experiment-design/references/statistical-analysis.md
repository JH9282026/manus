# Statistical Analysis for A/B Tests

Guide to analyzing experiment results with statistical rigor.

---

## Frequentist Analysis

### Two-Sample Z-Test for Proportions

Used for conversion rates and other binary metrics.

```
z = (p1 - p2) / sqrt(p_pooled × (1 - p_pooled) × (1/n1 + 1/n2))

Where:
- p1, p2 = conversion rates
- n1, n2 = sample sizes
- p_pooled = (x1 + x2) / (n1 + n2)
```

#### Example Calculation
```
Control: 500 conversions / 10,000 visitors = 5.00%
Treatment: 550 conversions / 10,000 visitors = 5.50%

p_pooled = (500 + 550) / (10,000 + 10,000) = 5.25%

z = (0.055 - 0.050) / sqrt(0.0525 × 0.9475 × (1/10000 + 1/10000))
z = 0.005 / sqrt(0.0000099)
z = 0.005 / 0.00315
z = 1.59

p-value (two-tailed) = 0.112
```

**Result**: Not statistically significant at α=0.05

### Two-Sample T-Test for Means

Used for revenue, time on site, and other continuous metrics.

```
t = (x̄1 - x̄2) / sqrt(s1²/n1 + s2²/n2)

Where:
- x̄1, x̄2 = sample means
- s1, s2 = sample standard deviations
- n1, n2 = sample sizes
```

### Chi-Square Test

Used when comparing distributions across categories.

```
χ² = Σ [(Observed - Expected)² / Expected]
```

---

## Confidence Intervals

### For Proportion Difference
```
CI = (p1 - p2) ± Z × SE

Where:
- Z = 1.96 for 95% CI
- SE = sqrt(p1(1-p1)/n1 + p2(1-p2)/n2)
```

### Interpreting Confidence Intervals
| CI Range | Interpretation |
|----------|----------------|
| Does not include 0 | Statistically significant |
| Includes 0 | Not statistically significant |
| Narrow range | High precision |
| Wide range | Low precision, need more data |

### Relative Lift CI
```
Relative lift = (Treatment - Control) / Control
CI = Lift ± Z × SE_relative

Report as: "5.2% lift [1.2%, 9.4%] 95% CI"
```

---

## P-Value Interpretation

### What P-Value Means
The probability of observing results this extreme (or more) if there were no true difference.

### What P-Value Does NOT Mean
- ❌ Probability the null hypothesis is true
- ❌ Probability results are due to chance
- ❌ Effect size or practical importance

### P-Value Guidelines
| P-Value | Evidence Level | Common Action |
|---------|----------------|---------------|
| < 0.001 | Very strong | High confidence |
| < 0.01 | Strong | Standard threshold (some orgs) |
| < 0.05 | Moderate | Standard threshold |
| < 0.10 | Weak | Consider extending test |
| ≥ 0.10 | Insufficient | Cannot conclude difference |

### One-Tailed vs Two-Tailed
| Type | Use When | Alpha Allocation |
|------|----------|------------------|
| Two-tailed | Either direction possible | α/2 each tail |
| One-tailed | Only one direction expected | α in one tail |

**Default**: Always use two-tailed unless you have strong prior reason to expect only one direction.

---

## Multiple Comparisons Problem

### The Problem
Testing multiple metrics or variants increases false positive rate.

```
Family-wise error rate = 1 - (1 - α)^n

With α=0.05 and n=20 tests:
FWER = 1 - (0.95)^20 = 64% chance of at least one false positive
```

### Correction Methods

#### Bonferroni Correction
Most conservative. Divide α by number of tests.
```
Adjusted α = 0.05 / 10 tests = 0.005
```

#### Holm-Bonferroni (Step-Down)
Less conservative. Sort p-values and apply sequential correction.
```
1. Sort p-values ascending
2. For i-th p-value, compare to α/(n-i+1)
3. Reject until first non-rejection
```

#### False Discovery Rate (FDR)
Controls expected proportion of false positives among rejected tests.
```
Benjamini-Hochberg procedure:
1. Sort p-values ascending
2. For i-th p-value, compare to (i/n) × α
3. Find largest i where p(i) ≤ (i/n) × α
4. Reject all hypotheses with smaller p-values
```

### When to Correct
| Scenario | Correction Needed? |
|----------|-------------------|
| Multiple variants vs control | Yes - Bonferroni |
| Primary + secondary metrics | Only correct secondary |
| Exploratory segments | Yes - FDR |
| Guardrail metrics | No - evaluated independently |

---

## Power Analysis

### What is Statistical Power?
Probability of detecting a true effect when it exists.

```
Power = 1 - β
β = probability of Type II error (false negative)
```

### Post-Hoc Power (Observed Power)
**Do NOT use** for interpreting null results. It's a function of p-value and adds no information.

### Prospective Power Uses
- Sample size planning
- Evaluating test feasibility
- Comparing test designs

### Power Curves
Shows relationship between effect size and power for given sample size.

```
For n=10,000 per variant, α=0.05:
- 5% baseline conversion
- MDE 5% relative → 33% power (underpowered)
- MDE 10% relative → 80% power (adequate)
- MDE 20% relative → 99% power (overpowered)
```

---

## Effect Size Measures

### Cohen's d (Continuous Metrics)
```
d = (x̄1 - x̄2) / pooled_SD

Interpretation:
- Small: d = 0.2
- Medium: d = 0.5
- Large: d = 0.8
```

### Odds Ratio (Binary Metrics)
```
OR = (a/b) / (c/d)

Where:
- a = treatment successes
- b = treatment failures
- c = control successes
- d = control failures
```

### Relative Risk
```
RR = (Treatment conversion) / (Control conversion)

RR = 1: No difference
RR > 1: Treatment better
RR < 1: Control better
```

---

## Segment Analysis

### Purpose
Understand if treatment effect varies across user groups.

### Common Segments
- Device type (mobile/desktop)
- User tenure (new/existing)
- Geography
- Traffic source
- User behavior (high/low activity)

### Cautions
1. **Multiple comparisons**: Correct for number of segments
2. **Pre-specify**: Define segments before looking at results
3. **Sample size**: Each segment needs adequate power
4. **Simpson's paradox**: Overall result may differ from segments

### Interaction Effects
```
If treatment works better for mobile users:
- Overall lift: 3%
- Mobile lift: 8%
- Desktop lift: 1%

This is an interaction between treatment and device.
```

---

## Results Reporting Template

```
## Summary
Treatment [increased/decreased] [metric] by [X%] 
([lower%, upper%] 95% CI, p=[value]).

## Statistical Details
| Metric | Control | Treatment | Δ | 95% CI | p-value |
|--------|---------|-----------|---|--------|---------|
| Primary | X | Y | Z% | [a,b] | 0.XXX |

## Sample
- Control: N users, M conversions
- Treatment: N users, M conversions
- SRM check: passed (p=0.XX)

## Segments
| Segment | n | Lift | 95% CI | p-value |
|---------|---|------|--------|---------|
| Mobile | X | Y% | [a,b] | 0.XXX |

## Decision
[Ship/Iterate/Kill] because [reasoning]
```

---

## Common Mistakes

### Analysis Errors
| Mistake | Problem | Solution |
|---------|---------|----------|
| Peeking | Inflates false positives | Sequential methods or wait |
| Wrong test | Invalid p-values | Match test to data type |
| Ignoring variance | Incorrect conclusions | Use proper SE formulas |
| Post-hoc hypotheses | Confirmation bias | Pre-register analysis |

### Interpretation Errors
| Mistake | Correct Interpretation |
|---------|----------------------|
| "p=0.06 means trending" | Not significant at α=0.05 |
| "Not significant = no effect" | Could lack power |
| "p=0.001 means huge effect" | P-value ≠ effect size |
