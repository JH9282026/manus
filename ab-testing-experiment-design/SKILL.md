---
name: "ab-testing-experiment-design"
description: "Design and analyze A/B tests and controlled experiments for product optimization, conversion rate improvement, and data-driven decision making. Use for calculating sample sizes, setting up experiments, analyzing test results, avoiding common statistical pitfalls, running multivariate tests, and interpreting significance."
---

# A/B Testing & Experiment Design

Design statistically valid experiments and analyze results to make confident product decisions.

## Overview

This skill covers the complete experimentation lifecycle: hypothesis formation, sample size calculation, test design, statistical analysis, and result interpretation. Use it when running website tests, feature experiments, pricing tests, or any controlled experiment requiring statistical rigor.

## Experiment Type Selection

| Goal | Test Type | When to Use | Reference |
|------|-----------|-------------|-----------|
| Compare two versions | A/B Test | Single variable change | `/references/ab-test-fundamentals.md` |
| Compare 3+ versions | A/B/n Test | Multiple variants | `/references/ab-test-fundamentals.md` |
| Test multiple variables | Multivariate (MVT) | Interaction effects matter | `/references/multivariate-testing.md` |
| Personalization | Bandit algorithms | Continuous optimization | `/references/advanced-methods.md` |
| Sequential analysis | SPRT | Early stopping needed | `/references/advanced-methods.md` |

## Sample Size Calculator

### Quick Reference Formula
```
n = (2 × σ² × (Z_α + Z_β)²) / δ²

Where:
- n = sample size per variant
- σ = standard deviation
- Z_α = Z-score for significance (1.96 for 95%)
- Z_β = Z-score for power (0.84 for 80%)
- δ = minimum detectable effect
```

### Sample Size by Baseline Conversion Rate

| Baseline CR | MDE 5% Relative | MDE 10% Relative | MDE 20% Relative |
|-------------|-----------------|------------------|------------------|
| 1% | 380,000 | 95,000 | 24,000 |
| 3% | 120,000 | 30,000 | 8,000 |
| 5% | 70,000 | 18,000 | 4,600 |
| 10% | 32,000 | 8,000 | 2,100 |
| 20% | 14,000 | 3,600 | 900 |

*Per variant, 80% power, 95% significance, two-tailed*

## Test Design Checklist

### Pre-Test Requirements
- [ ] Clear hypothesis documented
- [ ] Single primary metric defined
- [ ] Sample size calculated
- [ ] Test duration estimated
- [ ] Randomization method confirmed
- [ ] QA on both variants complete

### During Test
- [ ] Traffic split verified
- [ ] No peeking at results
- [ ] Monitoring for technical issues
- [ ] Data quality checks active

### Post-Test
- [ ] Full sample size reached
- [ ] Statistical analysis complete
- [ ] Segmentation analysis done
- [ ] Novelty effects considered
- [ ] Decision documented

## Statistical Significance Quick Guide

| P-value | Interpretation | Action |
|---------|----------------|--------|
| p < 0.01 | Strong evidence | High confidence to ship |
| p < 0.05 | Moderate evidence | Standard threshold to ship |
| 0.05 < p < 0.10 | Weak evidence | Consider extending test |
| p > 0.10 | Insufficient evidence | Do not ship based on test |

### Confidence Interval Interpretation
- If CI excludes zero (for lift) → statistically significant
- Width indicates precision of estimate
- Narrower CI = more certainty about effect size

## Common Pitfalls to Avoid

| Pitfall | Problem | Solution |
|---------|---------|----------|
| Peeking | Inflates false positive rate | Pre-commit to sample size |
| Multiple comparisons | Increases error rate | Bonferroni correction or FDR |
| Selection bias | Invalid results | Proper randomization |
| Novelty effect | Temporary behavior change | Run longer, segment new users |
| Simpson's paradox | Aggregation hides truth | Segment analysis |
| Low power | Miss real effects | Calculate sample size properly |

## Metric Selection Framework

### Primary Metric Requirements
1. **Sensitive**: Moves with expected changes
2. **Measurable**: Can be tracked accurately  
3. **Timely**: Observable within test window
4. **Aligned**: Maps to business objective

### Metric Hierarchy
| Type | Purpose | Example |
|------|---------|---------|
| Primary | Decision metric | Conversion rate |
| Secondary | Supporting evidence | Revenue per user |
| Guardrail | Prevent harm | Page load time |
| Diagnostic | Debug issues | Click-through rate |

## Analysis Output Template

```
EXPERIMENT: [Name]
HYPOTHESIS: [If we... then we expect...]
DURATION: [Start] to [End]
SAMPLE: Control: n1 | Treatment: n2

RESULTS:
┌─────────────┬─────────┬───────────┬────────┐
│ Metric      │ Control │ Treatment │ Change │
├─────────────┼─────────┼───────────┼────────┤
│ Conv Rate   │ X.XX%   │ X.XX%     │ +X.X%  │
│ 95% CI      │         │           │ [a, b] │
│ P-value     │         │           │ 0.XXX  │
└─────────────┴─────────┴───────────┴────────┘

DECISION: [Ship / Don't Ship / Iterate]
RATIONALE: [Why]
```

## Using the Reference Files

### When to Read Each Reference

**`/references/ab-test-fundamentals.md`** — Read when setting up a standard A/B test, calculating sample sizes, or reviewing statistical foundations.

**`/references/statistical-analysis.md`** — Read when analyzing test results, interpreting p-values, or calculating confidence intervals.

**`/references/multivariate-testing.md`** — Read when testing multiple variables simultaneously or when interaction effects between changes are important.

**`/references/advanced-methods.md`** — Read when using Bayesian methods, sequential testing, multi-armed bandits, or handling complex experimental designs.
