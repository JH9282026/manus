# Meta-Analysis Methods

Conduct systematic reviews and quantitative synthesis across clinical studies.

---

## Systematic Review Process

### PRISMA Framework

Follow the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) checklist:

1. **Define research question** using PICOS framework (Population, Intervention, Comparator, Outcome, Study design)
2. **Search strategy** — Develop comprehensive search across PubMed, Cochrane, Embase, ClinicalTrials.gov
3. **Study selection** — Apply predefined inclusion/exclusion criteria with dual review
4. **Data extraction** — Standardized extraction forms with inter-rater reliability checks
5. **Quality assessment** — Risk of bias assessment (Cochrane RoB 2.0 for RCTs, Newcastle-Ottawa for observational)
6. **Synthesis** — Quantitative meta-analysis or narrative synthesis

---

## Quantitative Meta-Analysis

### Effect Size Calculation

| Outcome Type | Effect Measure | Interpretation |
|---|---|---|
| Continuous | Mean difference, standardized mean difference (SMD) | Magnitude of treatment effect |
| Binary | Odds ratio, risk ratio, risk difference | Likelihood of outcome |
| Time-to-event | Hazard ratio | Rate of event occurrence |

### Pooling Methods

**Fixed-effects model** — Assumes single true effect size across studies
- Use when studies are methodologically similar
- Weighted by inverse variance
- Gives more weight to larger studies

**Random-effects model** — Assumes effect sizes vary across studies
- Use when heterogeneity expected
- DerSimonian-Laird or REML estimation
- Gives relatively more weight to smaller studies
- Generally preferred for clinical meta-analyses

### Heterogeneity Assessment

| Measure | Interpretation |
|---|---|
| Q statistic (Cochran's) | Tests whether variability exceeds sampling error (p < 0.10 indicates heterogeneity) |
| I² statistic | Proportion of variability due to heterogeneity (25% low, 50% moderate, 75% high) |
| τ² (tau-squared) | Estimated between-study variance |
| Prediction interval | Range of likely effects in future studies |

### Subgroup and Sensitivity Analysis

- **Subgroup analysis** — Explore potential effect modifiers (age, disease severity, dose)
- **Sensitivity analysis** — Assess robustness by excluding studies (leave-one-out, quality-based)
- **Meta-regression** — Model relationship between study characteristics and effect size
- **Funnel plots** — Assess publication bias (Egger's test, trim-and-fill)
