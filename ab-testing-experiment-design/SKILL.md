---
name: "ab-testing-experiment-design"
description: "Design, execute, and analyze controlled experiments to measure causal impact of changes. Use for: A/B test design, hypothesis formulation, sample size calculation, randomization strategy, statistical analysis, multivariate testing, sequential testing, Bayesian analysis, experiment monitoring, and evidence-based decision-making."
---

# A/B Testing & Experiment Design

Apply scientific methodology to business decisions through rigorous controlled experiments.

## Overview

Measure causal impact of changes rather than mere correlation. Design experiments that establish whether specific changes actually caused observed outcomes, enabling evidence-based decisions for product features, pricing, marketing, and operations.

## Experiment Lifecycle

| Phase | Activities | Outputs |
|-------|------------|--------|
| Hypothesis | Form testable hypothesis | Hypothesis statement |
| Design | Calculate sample size, define metrics | Design document |
| Execution | Randomize, assign treatments | Monitoring data |
| Analysis | Statistical testing, interpretation | Results report |
| Decision | Recommend action | Ship/iterate/abandon |

## Experiment Types

| Type | Variants | Use Case |
|------|----------|----------|
| A/B Test | 2 | Single change comparison |
| A/B/n Test | 3+ | Multiple variants |
| Multivariate | Many | Factor combinations |
| Sequential | Variable | Early stopping |
| Bandit | Adaptive | Optimization focus |

## Key Parameters

### Required Inputs
- **Hypothesis**: Expected effect and direction
- **Primary Metric**: Overall Evaluation Criterion (OEC)
- **MDE**: Minimum Detectable Effect
- **Significance Level (α)**: Typically 0.05
- **Statistical Power (1-β)**: Typically 0.80-0.90

### Design Decisions
- Randomization unit (user, session, device)
- Traffic allocation per variant
- Experiment duration
- Guardrail metrics

## Sample Size Calculation

Required sample depends on:
- Baseline conversion rate
- Minimum detectable effect
- Significance level
- Statistical power
- Number of variants

Formula: n = 2 × (Zα + Zβ)² × p(1-p) / MDE²

## Statistical Methods

| Method | Type | Best For |
|--------|------|----------|
| t-test | Frequentist | Continuous metrics |
| Chi-square | Frequentist | Proportions |
| Mann-Whitney | Non-parametric | Non-normal data |
| Bayesian | Probability | Business context |
| Sequential | Adaptive | Early decisions |

## Guardrail Metrics

Protect against unintended harm:
- Page load time
- Error rates
- Customer complaints
- Churn indicators

## Common Pitfalls

- Peeking at results before completion
- Multiple testing without correction
- Sample ratio mismatch (SRM)
- Novelty/primacy effects
- Carryover between variants

## Deliverables

### Design Document
- Hypothesis statement
- Metric definitions
- Sample size calculations
- Randomization plan
- Timeline and milestones

### Analysis Report
- Results with confidence intervals
- Effect sizes (not just p-values)
- Segment analysis
- Recommendations

## Using the Reference Files

### `/references/statistical-methods.md`
Read when performing statistical analysis, calculating sample sizes, or interpreting results.

### `/references/multivariate-testing.md`
Read when designing experiments with multiple factors or variants.

## Reference Files

This skill includes the following detailed reference materials:

- [Ab Test Fundamentals](references/ab-test-fundamentals.md)
- [Advanced Methods](references/advanced-methods.md)
- [Multivariate Testing](references/multivariate-testing.md)
- [Statistical Analysis](references/statistical-analysis.md)
- [Statistical Methods](references/statistical-methods.md)
