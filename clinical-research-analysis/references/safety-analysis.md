# Safety Analysis and Pharmacovigilance

Methods for detecting and evaluating drug safety signals.

---

## Adverse Event Analysis

### Standard Safety Tables

| Table | Content | Reporting Level |
|---|---|---|
| Overall AE summary | Incidence by treatment arm | SOC and preferred term |
| SAE listing | All serious adverse events | Individual case detail |
| AE leading to discontinuation | Events causing withdrawal | By treatment arm |
| Deaths | All-cause and related mortality | Narrative summary |
| Lab abnormalities | Clinically significant shifts | By parameter and grade |
| Vital signs | Mean changes and outliers | By timepoint |

### Adverse Event Grading

Use CTCAE (Common Terminology Criteria for Adverse Events) grading:
- **Grade 1** — Mild; asymptomatic or mild symptoms
- **Grade 2** — Moderate; minimal intervention indicated
- **Grade 3** — Severe; hospitalization indicated
- **Grade 4** — Life-threatening; urgent intervention
- **Grade 5** — Death related to adverse event

---

## Signal Detection Methods

### Spontaneous Reporting Analysis

| Method | Description | Threshold |
|---|---|---|
| Proportional Reporting Ratio (PRR) | Ratio of reporting rates (drug vs. all drugs) | PRR ≥ 2 + chi-square ≥ 4 + N ≥ 3 |
| Reporting Odds Ratio (ROR) | Odds ratio from 2x2 table | Lower 95% CI > 1 |
| Bayesian Confidence Propagation (BCPNN) | Information component with Bayesian shrinkage | IC025 > 0 |
| Multi-item Gamma Poisson Shrinker (MGPS) | Empirical Bayes shrinkage estimator | EB05 > 2 |

### Benefit-Risk Assessment

**Framework:** Structured benefit-risk assessment per ICH guidance

1. Define the decision context and therapeutic area
2. Identify and prioritize benefits and risks
3. Assess magnitude and probability of each
4. Integrate findings using visual displays (forest plots, value trees)
5. Draw conclusions with uncertainty characterization

---

## Post-Market Surveillance

### Real-World Safety Monitoring

- Analyze electronic health records for safety signals
- Monitor spontaneous adverse event reporting systems (FAERS, EudraVigilance)
- Conduct observational safety studies (cohort, case-control)
- Implement Risk Evaluation and Mitigation Strategies (REMS)
- Prepare Periodic Benefit-Risk Evaluation Reports (PBRERs)

### Pharmacovigilance Reporting

| Report Type | Frequency | Audience | Content |
|---|---|---|---|
| Individual case safety report (ICSR) | Within 15 days (serious) | Regulatory authority | Individual case details |
| PSUR/PBRER | Per regulatory schedule | Regulatory authority | Cumulative safety review |
| Signal assessment report | As signals detected | Safety committee | Signal evaluation and recommendation |
| Risk management plan (RMP) | At approval, updated | Regulatory authority | Risk minimization measures |
