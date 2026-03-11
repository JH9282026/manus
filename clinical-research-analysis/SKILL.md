---
name: "clinical-research-analysis"
description: "Analyze clinical trial data, research protocols, and medical study outcomes for healthcare decision-making and pharmaceutical development. Use for: Phase I-IV clinical trial analysis, regulatory submissions, meta-analyses, pharmacovigilance, benefit-risk assessments, drug development milestones, health technology assessments, and real-world evidence evaluation."
---

# Clinical Research Analysis

Analyze clinical trial data, research protocols, and medical study outcomes to generate actionable insights for evidence-based healthcare decisions.

## Overview

Provide systematic evaluation and synthesis of clinical research data including clinical trial results, observational studies, regulatory submissions, and post-market surveillance. Apply validated statistical methodologies (intention-to-treat, Kaplan-Meier, Cox proportional hazards) and quality frameworks (CONSORT, STROBE) to deliver rigorous, regulatory-compliant analysis.

## Analysis Type Selection

| Analysis Need | Method | Output | Reference |
|---|---|---|---|
| Single RCT results | Per-protocol + ITT analysis | CSR-ready tables, figures, listings | `/references/statistical-methods.md` |
| Cross-study comparison | Meta-analysis (random effects) | Forest plots, I² heterogeneity | `/references/meta-analysis.md` |
| Safety signal detection | Disproportionality analysis | Signal-to-noise ratios, PRR | `/references/safety-analysis.md` |
| Regulatory submission | ICH E3 CSR format | ISS, ISE, benefit-risk assessment | `/references/regulatory-standards.md` |
| Real-world evidence | Observational cohort analysis | Comparative effectiveness reports | `/references/statistical-methods.md` |

## Clinical Trial Analysis Framework

### Phase-Specific Analysis Focus

| Phase | Primary Objective | Key Endpoints | Sample Size |
|---|---|---|---|
| Phase I | Safety, dosing | MTD, DLT, PK parameters | 20-80 |
| Phase II | Efficacy signals | Preliminary efficacy, dose-response | 100-300 |
| Phase III | Confirmatory efficacy | Primary efficacy, safety profile | 300-3,000+ |
| Phase IV | Post-market surveillance | Long-term safety, real-world effectiveness | 1,000+ |

### Standard Analysis Workflow

1. **Data validation** — Verify CDISC SDTM/ADaM compliance, check completeness
2. **Demographics** — Summarize baseline characteristics, assess balance between arms
3. **Primary analysis** — Analyze primary endpoint per statistical analysis plan (SAP)
4. **Secondary analysis** — Evaluate secondary and exploratory endpoints
5. **Safety analysis** — Tabulate adverse events, SAEs, lab abnormalities
6. **Subgroup analysis** — Pre-specified subgroup analyses per protocol
7. **Sensitivity analysis** — Test robustness of findings under alternative assumptions

## Data Quality Assessment

| Quality Dimension | Check | Action if Failed |
|---|---|---|
| Completeness | Missing data patterns, dropout rates | Apply missing data methodology (MMRM, MI) |
| Consistency | Cross-variable validation, range checks | Query resolution, protocol deviation log |
| Protocol compliance | Inclusion/exclusion verification | Per-protocol vs. ITT sensitivity |
| Site performance | Enrollment rates, query volumes | Site monitoring, potential exclusion |

## Regulatory Submission Checklist

- [ ] Clinical Study Report (CSR) per ICH E3
- [ ] Integrated Summary of Safety (ISS)
- [ ] Integrated Summary of Efficacy (ISE)
- [ ] CONSORT flow diagram
- [ ] Statistical analysis plan (SAP) with amendments
- [ ] Data listings, tables, and figures (TFLs)
- [ ] Benefit-risk assessment framework
- [ ] Periodic Safety Update Report (PSUR) if applicable

## Using the Reference Files

**`/references/statistical-methods.md`** — Read when selecting or implementing statistical methodologies, handling missing data, or performing survival analysis.

**`/references/meta-analysis.md`** — Read when conducting systematic reviews, pooling data across studies, or assessing heterogeneity.

**`/references/safety-analysis.md`** — Read when analyzing adverse events, detecting safety signals, or preparing pharmacovigilance reports.

**`/references/regulatory-standards.md`** — Read when preparing regulatory submissions, following ICH guidelines, or ensuring compliance with FDA/EMA requirements.
