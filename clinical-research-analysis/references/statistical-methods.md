# Statistical Methods for Clinical Research

## Survival Analysis

### Kaplan-Meier Method
Estimate survival function from time-to-event data.

**Application**
- Overall survival (OS)
- Progression-free survival (PFS)
- Time to response
- Duration of response

**Key Outputs**
- Survival curves
- Median survival time
- Survival rates at specific timepoints
- 95% confidence intervals

### Cox Proportional Hazards
Assess effect of covariates on survival.

**Assumptions**
- Proportional hazards over time
- Log-linear relationship
- Censoring independent of survival

**Key Outputs**
- Hazard ratios (HR)
- 95% confidence intervals
- p-values
- Adjusted analyses

---

## Efficacy Analysis Methods

### Intention-to-Treat (ITT)
- Include all randomized subjects
- Analyze as randomized
- Preserves randomization benefits
- Primary analysis for regulatory submissions

### Per-Protocol (PP)
- Include only compliant subjects
- Sensitivity analysis
- May overestimate treatment effect
- Supplementary to ITT

### Modified ITT (mITT)
- Exclude subjects who never received treatment
- Exclude major protocol violations
- Common compromise approach

---

## Repeated Measures Analysis

### Mixed Models (MMRM)
- Mixed-effects model for repeated measures
- Handles missing data under MAR
- Accounts for correlation structure
- Standard for longitudinal trials

### Analysis Components
- Fixed effects: treatment, time, interaction
- Random effects: subject-level variation
- Covariance structure: unstructured, compound symmetry

---

## Missing Data Handling

| Method | Assumption | Use Case |
|--------|------------|----------|
| Complete case | MCAR | Sensitivity only |
| LOCF | Stable post-dropout | Historical, limited use |
| MMRM | MAR | Primary analysis |
| Multiple imputation | MAR | Sensitivity analysis |
| Tipping point | MNAR exploration | Sensitivity analysis |

### Missing Data Assessment
- Characterize missing data patterns
- Assess randomness assumption
- Plan sensitivity analyses
- Document approach in SAP

---

## Subgroup Analysis

### Pre-specified Subgroups
- Define in protocol/SAP
- Biological plausibility
- Adequate sample size
- Adjust for multiplicity

### Interpretation Guidelines
- Interaction test p-value
- Consistency across subgroups
- Clinical plausibility
- Pre-specification status
