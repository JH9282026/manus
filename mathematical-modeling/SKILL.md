---
name: "mathematical-modeling"
description: "Develop and analyze mathematical representations of real-world systems for prediction, optimization, and decision support. Use for: predictive modeling, optimization problems, simulation design, system dynamics, statistical modeling, operations research, engineering analysis."
---

# Mathematical Modeling

Develop mathematical representations of real-world systems to predict behavior, optimize performance, and support decisions.

## Overview

Create, validate, and apply mathematical models across scientific, engineering, and business domains. Cover model formulation, parameter estimation, validation, sensitivity analysis, and interpretation.

## Quick Start: Model Type Selection

| Problem Type | Model Category | Reference |
|-------------|---------------|-----------|
| Prediction from data | Statistical/regression | `/references/modeling-techniques.md` |
| System behavior over time | Differential equations | `/references/modeling-techniques.md` |
| Resource allocation | Optimization (LP/IP) | `/references/optimization-simulation.md` |
| Uncertainty quantification | Stochastic models | `/references/optimization-simulation.md` |
| Complex system dynamics | Simulation | `/references/optimization-simulation.md` |

## Modeling Process

1. **Define problem** — Identify variables, constraints, objectives
2. **Formulate model** — Choose mathematical framework, define equations
3. **Estimate parameters** — Fit model to data, calibrate
4. **Validate** — Test against holdout data or known solutions
5. **Analyze** — Sensitivity analysis, scenario testing
6. **Interpret** — Translate results to actionable insights
7. **Communicate** — Document assumptions, limitations, conclusions

## Common Model Types

| Type | Mathematical Form | Applications |
|------|------------------|-------------|
| Linear regression | y = β₀ + β₁x + ε | Forecasting, trend analysis |
| Logistic regression | p = 1/(1+e^(-z)) | Classification, probability |
| Differential equations | dy/dt = f(y,t) | Population, physics, chemistry |
| Linear programming | min cᵀx s.t. Ax ≤ b | Resource allocation |
| Markov chains | P(Xₙ₊₁|Xₙ) | State transitions, queuing |
| Monte Carlo | Random sampling | Risk analysis, integration |
| Agent-based | Rule-based entities | Social systems, ecology |

## Model Validation Criteria

| Criterion | Method |
|-----------|--------|
| Goodness of fit | R², RMSE, MAE |
| Predictive accuracy | Cross-validation, holdout test |
| Parameter stability | Bootstrap, confidence intervals |
| Structural validity | Domain expert review |
| Sensitivity | Parameter perturbation analysis |

## Using the Reference Files

### When to Read Each Reference

**`/references/modeling-techniques.md`** — Read when formulating models using regression, differential equations, time series, or statistical methods.

**`/references/optimization-simulation.md`** — Read when solving optimization problems, designing simulations, or conducting Monte Carlo analysis.

## Reference Files

This skill includes the following detailed reference materials:

- [Modeling Techniques](references/modeling-techniques.md)
- [Optimization Simulation](references/optimization-simulation.md)
