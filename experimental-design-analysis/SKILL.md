---
name: "experimental-design-analysis"
description: "Create statistically optimal experimental designs and conduct rigorous analysis of experimental data to maximize information while minimizing resources. Use for: A/B testing design, factorial experiment planning, sample size calculation, randomization strategies, blocking and stratification, power analysis, ANOVA, regression analysis, and interpreting experimental results."
---

# Experimental Design & Analysis

Create statistically sound experimental designs and conduct rigorous analysis to extract maximum information from experiments while minimizing resource requirements.

## Overview

Provide frameworks for designing experiments from simple A/B tests to complex factorial designs. Cover randomization, blocking, sample size calculation, power analysis, and statistical analysis methods including ANOVA, regression, and non-parametric alternatives.

## Experiment Design Selection

| Design | Factors | Best For | Complexity |
|---|---|---|---|
| A/B test | 1 factor, 2 levels | Simple comparisons | Low |
| A/B/n test | 1 factor, n levels | Multiple variants | Low |
| Full factorial | 2+ factors, all combinations | Understanding interactions | Medium |
| Fractional factorial | Many factors, subset of combos | Screening many factors | Medium-High |
| Randomized block | 1+ factors + blocking variable | Reducing variability | Medium |
| Latin square | 2 blocking variables | Two sources of variability | Medium |
| Split-plot | Hard-to-change + easy factors | Nested randomization | High |
| Response surface | Continuous factors | Optimizing a response | High |

## Sample Size and Power

### Key Parameters

| Parameter | Description | Typical Values |
|---|---|---|
| Effect size | Minimum detectable difference | Business-relevant threshold |
| Power (1-β) | Probability of detecting real effect | 0.80 or 0.90 |
| Significance (α) | False positive rate | 0.05 (5%) |
| Variance | Variability in the outcome | From pilot data or history |

### Quick Sample Size Rules of Thumb
- Detecting 5% relative change: ~16,000 per group
- Detecting 10% relative change: ~4,000 per group
- Detecting 20% relative change: ~1,000 per group
- (For conversion rates around 5%, two-sided test, α=0.05, β=0.20)

## Randomization Methods

| Method | When to Use |
|---|---|
| Simple random | Default for most experiments |
| Stratified random | When important covariates exist |
| Cluster random | When units are naturally grouped |
| Blocked random | When known sources of variability exist |
| Adaptive/sequential | When sample sizes are expensive |

## Analysis Decision Tree

| Data Type | Groups | Method |
|---|---|---|
| Continuous, normal | 2 | t-test (independent or paired) |
| Continuous, normal | 3+ | One-way ANOVA |
| Continuous, normal | 2+ factors | Factorial ANOVA |
| Continuous, non-normal | 2 | Mann-Whitney U / Wilcoxon |
| Continuous, non-normal | 3+ | Kruskal-Wallis |
| Proportions | 2 | Chi-square / Fisher exact |
| Proportions | 2+ | Chi-square test |
| Count data | Any | Poisson/negative binomial regression |
| Time-to-event | Any | Log-rank test, Cox regression |

## Using the Reference Files

### When to Read Each Reference

**`/references/design-methods.md`** — Read when planning specific experiment designs: factorial, blocking, response surface, or when calculating sample sizes and power.

**`/references/statistical-analysis.md`** — Read when analyzing experimental data, interpreting results, checking assumptions, or selecting appropriate statistical tests.

## Reference Files

This skill includes the following detailed reference materials:

- [Design Methods](./references/design-methods.md)
- [Statistical Analysis](./references/statistical-analysis.md)
