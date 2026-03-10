---
name: ab-testing-experiment-design
description: Design, execute, and analyze controlled experiments to measure causal impact of changes. Use for: A/B testing website features, pricing experiments, email subject line tests, product feature evaluation, conversion optimization experiments, multi-variant testing (A/B/n), statistical significance analysis, sample size calculation, experiment design planning, measuring treatment effects, validating hypotheses with data, and any scenario requiring evidence-based decision-making through rigorous experimental methodology.
---

# A/B Testing & Experiment Design

Design and execute controlled experiments to measure causal impact and enable evidence-based decision-making.

## Overview

This skill provides frameworks for the complete experimental lifecycle: hypothesis formation, experiment design, execution, statistical analysis, and decision-making. Apply scientific methodology to business decisions, establishing causation rather than correlation. Use when measuring impact of changes to products, pricing, marketing, or operations.

## Experiment Type Selection

| Scenario | Method | When to Use | Reference |
|----------|--------|-------------|-----------|
| Two variants comparison | Classic A/B Test | Single change, clear hypothesis | `/references/experiment-design-methodology.md` |
| Multiple variants | A/B/n Test | Testing several alternatives | `/references/experiment-design-methodology.md` |
| Interacting changes | Multivariate (MVT) | Testing combinations of factors | `/references/experiment-design-methodology.md` |
| Continuous optimization | Multi-Armed Bandit | Balancing learning and earning | `/references/statistical-methods-analysis.md` |
| Geographic rollout | Geo Experiment | Cannot randomize users | `/references/experiment-design-methodology.md` |
| Time-based variation | Switchback Test | Marketplace, supply-constrained | `/references/experiment-design-methodology.md` |

## Core Experiment Design Process

### 1. Define Hypothesis and Metrics

Formulate a clear, testable hypothesis:
- State the expected effect direction and magnitude
- Define the primary metric (Overall Evaluation Criterion)
- Identify secondary metrics and guardrail metrics
- Specify minimum detectable effect (MDE)

### 2. Calculate Sample Size

Determine required sample per variant based on:
- Baseline conversion rate or metric mean
- Minimum detectable effect (relative or absolute)
- Statistical significance level (α, typically 0.05)
- Desired power (1-β, typically 0.80)

| Baseline Rate | MDE (Relative) | Sample per Variant (α=0.05, Power=0.80) |
|---------------|----------------|----------------------------------------|
| 1% | 10% | ~1,900,000 |
| 5% | 10% | ~310,000 |
| 10% | 10% | ~140,000 |
| 20% | 10% | ~64,000 |
| 5% | 20% | ~78,000 |
| 10% | 20% | ~35,000 |

### 3. Design Randomization

Select randomization unit and method:
- **User-level**: Standard for most product experiments
- **Session-level**: When user identity unavailable
- **Device-level**: Cross-session consistency needed
- **Geographic/Cluster**: When spillover effects exist

### 4. Execute and Monitor

- Verify assignment balance (detect Sample Ratio Mismatch)
- Monitor guardrail metrics for degradation
- Track sample size accumulation
- Avoid peeking at results before adequate sample

### 5. Analyze and Decide

- Calculate treatment effect with confidence interval
- Assess statistical and practical significance
- Check for novelty effects and segment heterogeneity
- Make ship/iterate/abandon recommendation

## Statistical Methods Quick Reference

| Test Type | Data Type | When to Use |
|-----------|-----------|-------------|
| Two-sample t-test | Continuous | Mean comparison, large samples |
| Welch's t-test | Continuous | Unequal variances |
| Chi-square test | Proportions | Conversion rate comparison |
| Mann-Whitney U | Continuous | Non-normal distributions |
| Bootstrap | Any | Small samples, complex metrics |
| Bayesian A/B | Any | Need probability of winner |

## Variance Reduction Techniques

Reduce experiment duration with these approaches:

| Technique | Variance Reduction | Implementation |
|-----------|-------------------|----------------|
| CUPED | 30-50% | Pre-experiment covariate adjustment |
| Stratification | 10-30% | Randomize within strata |
| Triggered Analysis | Variable | Analyze only affected users |
| Ratio Metrics | Variable | Use rate metrics over counts |

## Common Validity Threats

| Threat | Description | Mitigation |
|--------|-------------|------------|
| Sample Ratio Mismatch | Unequal assignment rates | Check balance, investigate bugs |
| Novelty Effect | Temporary effect from newness | Run longer, compare time periods |
| Selection Bias | Non-random sample | Proper randomization |
| Interference | Units affect each other | Cluster randomization |
| Instrumentation | Tracking differences | Verify logging consistency |
| Multiple Testing | Inflated false positives | Bonferroni, Holm correction |

## Required Inputs Checklist

Before starting any experiment:

- [ ] Clear hypothesis with expected direction
- [ ] Primary metric (OEC) precisely defined
- [ ] Minimum detectable effect specified
- [ ] Baseline metric values (mean, variance)
- [ ] Sample size calculation completed
- [ ] Randomization unit selected
- [ ] Experiment duration estimated
- [ ] Guardrail metrics identified
- [ ] Stopping rules defined
- [ ] Technical implementation confirmed

## Platform Selection

| Platform | Best For | Key Features |
|----------|----------|--------------|
| Optimizely | Web/product testing | Visual editor, stats engine |
| LaunchDarkly | Feature flags | Developer-focused, fast |
| Google Optimize | Marketing tests | GA integration, free tier |
| Eppo | Data warehouse native | Warehouse-first approach |
| Statsig | Product experiments | Auto-analysis, powerful UI |
| Custom | Full control | Build to exact requirements |

## Using the Reference Files

### When to Read Each Reference

**`/references/experiment-design-methodology.md`** — Read when designing a new experiment, selecting experiment type, defining randomization strategy, or structuring the hypothesis and metrics framework.

**`/references/statistical-methods-analysis.md`** — Read when calculating sample size, selecting statistical tests, performing analysis, applying Bayesian methods, or implementing variance reduction techniques.

**`/references/implementation-platforms.md`** — Read when setting up experimentation infrastructure, selecting platforms, implementing feature flags, or building monitoring dashboards.

**`/references/common-pitfalls-validity.md`** — Read when assessing validity threats, debugging experiment issues, avoiding common mistakes, or reviewing experiment quality.
