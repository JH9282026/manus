# Power Analysis and Sample Size Determination

## Overview
Statistical power and sample size are critical considerations in hypothesis testing. Adequate power ensures ability to detect real effects, while appropriate sample size balances statistical requirements with practical constraints.

## Statistical Power

### Definition
Power is the probability of correctly rejecting a false null hypothesis (detecting a true effect).

**Formula:**
Power = 1 - β (where β = Type II error rate)

**Interpretation:**
- Power = 0.80 means 80% chance of detecting effect if it exists
- Higher power = better ability to detect effects
- Minimum acceptable power typically 0.80 (80%)

### Factors Affecting Power

**1. Sample Size (n)**
- Larger sample = higher power
- Most controllable factor
- Diminishing returns at very large sizes
- Primary focus of power analysis

**2. Effect Size**
- Larger effect = easier to detect = higher power
- Often not controllable (inherent to phenomenon)
- Important for planning studies
- Estimate from pilot studies or literature

**3. Significance Level (α)**
- Higher α = higher power
- But increases Type I error risk
- Trade-off between Type I and Type II errors
- Usually fixed at 0.05

**4. Variability (σ)**
- Lower variability = higher power
- Better measurement reduces variability
- Homogeneous samples have less variability
- Can be reduced through design improvements

### Power Curves
Graphs showing relationship between sample size and power for given effect size and α.

**Uses:**
- Visualize power-sample size relationship
- Compare different scenarios
- Communicate with stakeholders
- Justify sample size choices

## Effect Size

### Definition
Standardized measure of magnitude of difference or relationship.

**Importance:**
- Independent of sample size
- Indicates practical significance
- Essential for power analysis
- Allows comparison across studies

### Common Effect Size Measures

**Cohen's d (Mean Differences)**
```
d = (M₁ - M₂) / SD_pooled
```

**Interpretation:**
- Small: d = 0.2
- Medium: d = 0.5
- Large: d = 0.8

**Correlation Coefficient (r)**
**Interpretation:**
- Small: r = 0.1
- Medium: r = 0.3
- Large: r = 0.5

**Cohen's f (ANOVA)**
**Interpretation:**
- Small: f = 0.10
- Medium: f = 0.25
- Large: f = 0.40

**Odds Ratio (OR)**
- OR = 1: No effect
- OR > 1: Increased odds
- OR < 1: Decreased odds

**R-squared (Regression)**
- Proportion of variance explained
- 0 to 1 scale
- Higher = stronger relationship

### Estimating Effect Size

**From Literature:**
- Review similar studies
- Meta-analyses provide pooled estimates
- Consider context differences

**From Pilot Studies:**
- Conduct small preliminary study
- Calculate effect size from pilot data
- Use with caution (imprecise with small n)

**Minimum Detectable Effect:**
- Smallest effect of practical importance
- Based on domain knowledge
- Cost-benefit considerations

## Sample Size Determination

### A Priori Power Analysis
Determine required sample size before data collection.

**Inputs Needed:**
1. Desired power (typically 0.80 or 0.90)
2. Significance level α (typically 0.05)
3. Expected effect size
4. Type of statistical test

**Process:**
1. Specify hypotheses and test
2. Determine desired power
3. Estimate effect size
4. Calculate required sample size
5. Adjust for practical constraints
6. Document assumptions

### Sample Size Formulas

**One-Sample T-Test:**
```
n = (Z_α + Z_β)² × σ² / δ²
```
Where δ = expected difference from null value

**Two-Sample T-Test:**
```
n_per_group = 2(Z_α + Z_β)² × σ² / δ²
```

**Proportion Test:**
```
n = (Z_α + Z_β)² × [p₁(1-p₁) + p₂(1-p₂)] / (p₁ - p₂)²
```

**Correlation:**
```
n = [(Z_α + Z_β) / C]² + 3
```
Where C = 0.5 × ln[(1+r)/(1-r)]

### Practical Considerations

**Budget Constraints:**
- Cost per participant
- Total available budget
- Balance power with feasibility

**Time Constraints:**
- Recruitment timeline
- Data collection duration
- Analysis deadlines

**Population Availability:**
- Size of accessible population
- Recruitment challenges
- Rare populations

**Attrition:**
- Expected dropout rate
- Oversample to account for loss
- Typical: add 10-20% to calculated n

## Power Analysis Examples

### Example 1: T-Test
**Scenario:** Compare two teaching methods

**Inputs:**
- Desired power: 0.80
- α = 0.05 (two-tailed)
- Expected effect size: d = 0.5 (medium)
- Test: Independent samples t-test

**Result:** n = 64 per group (128 total)

### Example 2: ANOVA
**Scenario:** Compare three diet programs

**Inputs:**
- Desired power: 0.90
- α = 0.05
- Expected effect size: f = 0.25 (medium)
- Test: One-way ANOVA, 3 groups

**Result:** n = 52 per group (156 total)

### Example 3: Correlation
**Scenario:** Relationship between study time and grades

**Inputs:**
- Desired power: 0.80
- α = 0.05 (two-tailed)
- Expected correlation: r = 0.30 (medium)
- Test: Pearson correlation

**Result:** n = 84

## Post-Hoc Power Analysis

### Definition
Calculate achieved power after data collection.

**Uses:**
- Understand study's ability to detect effects
- Interpret non-significant results
- Plan future studies

**Cautions:**
- Controversial practice
- Can be misleading
- Better to focus on confidence intervals
- Don't use to justify non-significant results

### When Post-Hoc Power is Useful

**Acceptable Uses:**
- Planning follow-up studies
- Meta-analysis contributions
- Understanding literature
- Grant applications for new studies

**Inappropriate Uses:**
- Explaining away non-significant results
- Claiming study was "underpowered" post-hoc
- Avoiding reporting negative findings

## Software Tools

### G*Power
Free, comprehensive power analysis software.

**Features:**
- Wide range of statistical tests
- Graphical interface
- Power curves
- Sensitivity analyses

### R Packages
```r
# pwr package
library(pwr)

# T-test
pwr.t.test(d = 0.5, power = 0.80, sig.level = 0.05, type = "two.sample")

# ANOVA
pwr.anova.test(k = 3, f = 0.25, power = 0.80, sig.level = 0.05)

# Correlation
pwr.r.test(r = 0.30, power = 0.80, sig.level = 0.05)

# Proportion
pwr.2p.test(h = 0.3, power = 0.80, sig.level = 0.05)
```

### Python
```python
from statsmodels.stats.power import TTestIndPower

# T-test power analysis
analysis = TTestIndPower()
sample_size = analysis.solve_power(effect_size=0.5, power=0.80, alpha=0.05)
```

## Best Practices

1. **Conduct A Priori Analysis:** Determine sample size before data collection
2. **Be Conservative:** Use conservative effect size estimates
3. **Account for Attrition:** Oversample to compensate for dropouts
4. **Document Assumptions:** Record all inputs and rationale
5. **Consider Practical Constraints:** Balance statistical ideals with reality
6. **Use Multiple Scenarios:** Test sensitivity to assumptions
7. **Consult Statistician:** Get expert input for complex designs
8. **Report Power Analysis:** Include in methods section
9. **Don't Misuse Post-Hoc Power:** Avoid inappropriate interpretations
10. **Prioritize Effect Sizes:** Focus on magnitude, not just significance

## Common Mistakes

1. **No Power Analysis:** Collecting data without sample size justification
2. **Unrealistic Effect Sizes:** Assuming large effects without evidence
3. **Ignoring Attrition:** Not accounting for dropout
4. **Post-Hoc Excuses:** Using low power to explain non-significant results
5. **Underpowered Studies:** Proceeding with insufficient sample size
6. **Overpowered Studies:** Wasting resources on unnecessarily large samples
7. **Wrong Test:** Calculating power for different test than used
8. **Ignoring Multiple Comparisons:** Not adjusting for multiple tests

## Reporting Power Analysis

### In Research Proposals
\"An a priori power analysis using G*Power indicated that a sample size of 64 participants per group would provide 80% power to detect a medium effect size (d = 0.5) using an independent samples t-test with α = 0.05 (two-tailed). Accounting for an expected 15% attrition rate, we will recruit 74 participants per group (148 total).\"

### In Published Papers
\"Sample size was determined through a priori power analysis (G*Power 3.1) targeting 80% power to detect a medium effect (f = 0.25) with α = 0.05 for a one-way ANOVA with three groups, resulting in a target of 52 participants per group.\"

## References

- Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences
- G*Power: https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower
- Penn State. \"Power and Sample Size\" https://online.stat.psu.edu/stat500/lesson/6
