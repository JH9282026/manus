# Statistical Methods for Clinical Research

Validated statistical approaches for clinical trial analysis.

---

## Primary Analysis Methods

### Intention-to-Treat (ITT) Analysis

Analyze all randomized subjects in their assigned group regardless of compliance:
- Preserves randomization benefits
- Provides conservative efficacy estimate
- Required by most regulatory agencies as primary analysis
- Handle missing data using validated imputation methods

### Per-Protocol Analysis

Analyze only subjects who completed the study per protocol:
- Provides estimate of treatment effect under ideal conditions
- Used as sensitivity analysis to support ITT findings
- Higher risk of selection bias
- Useful for non-inferiority trials where ITT may be anti-conservative

---

## Survival Analysis

### Kaplan-Meier Method

- Estimate survival probability over time for time-to-event endpoints
- Plot survival curves comparing treatment arms
- Calculate median survival time and confidence intervals
- Test difference between curves using log-rank test
- Report hazard ratio from Cox proportional hazards model

### Cox Proportional Hazards Model

- Model time-to-event data with covariates
- Estimate adjusted hazard ratios
- Test proportional hazards assumption (Schoenfeld residuals)
- Include pre-specified covariates from SAP
- Stratified analysis for heterogeneous populations

---

## Missing Data Handling

| Method | Assumption | When to Use |
|---|---|---|
| Complete case analysis | Missing completely at random (MCAR) | Small proportion missing, MCAR justified |
| Last observation carried forward (LOCF) | Last value represents outcome | Legacy method, becoming less accepted |
| Mixed model repeated measures (MMRM) | Missing at random (MAR) | Preferred for continuous longitudinal data |
| Multiple imputation (MI) | MAR with uncertainty estimation | Complex missing patterns, sensitivity analyses |
| Tipping point analysis | Range of assumptions | Sensitivity analysis for missing data impact |

---

## Sample Size and Power

### Key Parameters

- **Alpha (Type I error)** — Typically 0.05 (two-sided) or 0.025 (one-sided)
- **Power (1 - Type II error)** — Typically 80% or 90%
- **Effect size** — Minimum clinically meaningful difference
- **Variability** — Standard deviation or event rate estimates
- **Dropout rate** — Inflate sample size to account for attrition

### Interim Analysis

- Pre-specify interim analyses in protocol and SAP
- Apply alpha spending functions (O'Brien-Fleming, Lan-DeMets)
- Maintain blinding of investigators during data monitoring
- Independent Data Safety Monitoring Board (DSMB) reviews
