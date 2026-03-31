# Statistical Methods and Interpretation in Research Papers

## Introduction

Understanding statistical methods and correctly interpreting results is crucial for critical appraisal of research papers. This guide covers common statistical approaches, their appropriate use, and how to interpret findings accurately.

## Descriptive Statistics

### Measures of Central Tendency

**Mean**
- Average of all values
- Sensitive to outliers
- Appropriate for normally distributed data
- Formula: Sum of values / Number of values

**Median**
- Middle value when data ordered
- Robust to outliers
- Appropriate for skewed data
- Better than mean for non-normal distributions

**Mode**
- Most frequent value
- Can have multiple modes
- Useful for categorical data
- Less commonly reported

### Measures of Dispersion

**Standard Deviation (SD)**
- Average distance from mean
- Same units as data
- Describes variability in sample
- Larger SD = more spread

**Variance**
- Square of standard deviation
- Less intuitive than SD
- Used in many statistical tests

**Interquartile Range (IQR)**
- Range of middle 50% of data
- Q3 - Q1
- Robust to outliers
- Often reported with median

**Range**
- Maximum - Minimum
- Simple but sensitive to outliers
- Limited usefulness

### Confidence Intervals

**Definition**
- Range of plausible values for population parameter
- 95% CI most common
- Wider CI = less precision

**Interpretation**
- 95% CI: If study repeated many times, 95% of CIs would contain true value
- CI that excludes null value = statistically significant
- Provides more information than p-value alone

**Factors Affecting Width**
- Sample size (larger n = narrower CI)
- Variability (larger SD = wider CI)
- Confidence level (99% CI wider than 95% CI)

## Inferential Statistics

### Hypothesis Testing

**Null Hypothesis (H₀)**
- No difference or no effect
- What we test against
- Example: Treatment has no effect

**Alternative Hypothesis (H₁)**
- What we want to demonstrate
- Example: Treatment has effect

**P-Value**
- Probability of observing results (or more extreme) if null hypothesis true
- NOT probability that null hypothesis is true
- Conventional threshold: p < 0.05

**Type I Error (\u03b1)**
- False positive
- Rejecting null when it's true
- \u03b1 = 0.05 means 5% chance

**Type II Error (\u03b2)**
- False negative
- Failing to reject null when it's false
- Power = 1 - \u03b2 (typically 0.80 or 0.90)

### Comparing Two Groups

**T-Tests**

*Independent Samples T-Test*
- Compares means of two independent groups
- Assumptions: Normal distribution, equal variances
- Example: Treatment vs. control

*Paired T-Test*
- Compares means of same group at two time points
- Accounts for within-subject correlation
- Example: Before vs. after treatment

*Welch's T-Test*
- Variant for unequal variances
- More robust than standard t-test

**Mann-Whitney U Test**
- Non-parametric alternative to independent t-test
- Compares distributions, not means
- No normality assumption
- Use when data skewed or ordinal

**Wilcoxon Signed-Rank Test**
- Non-parametric alternative to paired t-test
- Compares paired observations
- No normality assumption

### Comparing Multiple Groups

**ANOVA (Analysis of Variance)**

*One-Way ANOVA*
- Compares means of 3+ independent groups
- Tests if at least one group differs
- Doesn't specify which groups differ
- Follow with post-hoc tests

*Repeated Measures ANOVA*
- Compares means across multiple time points
- Accounts for within-subject correlation
- More powerful than independent ANOVA

*Two-Way ANOVA*
- Two independent variables
- Tests main effects and interaction
- Example: Treatment \u00d7 Gender

**Post-Hoc Tests**
- Conducted after significant ANOVA
- Identifies which groups differ
- Controls for multiple comparisons
- Examples: Tukey HSD, Bonferroni, Dunnett

**Kruskal-Wallis Test**
- Non-parametric alternative to one-way ANOVA
- Compares distributions of 3+ groups
- No normality assumption

### Categorical Data Analysis

**Chi-Square Test**
- Tests association between categorical variables
- Compares observed vs. expected frequencies
- Requires adequate cell counts (typically \u22655)
- Example: Treatment group \u00d7 Outcome (yes/no)

**Fisher's Exact Test**
- Alternative to chi-square for small samples
- Exact p-value calculation
- Use when cell counts < 5

**McNemar's Test**
- For paired categorical data
- Tests change in proportions
- Example: Before vs. after treatment (yes/no outcome)

### Correlation and Regression

**Correlation**

*Pearson Correlation (r)*
- Measures linear relationship
- Range: -1 to +1
- Assumptions: Linear relationship, normal distribution
- r = 0: No correlation
- r = ±0.3: Weak correlation
- r = ±0.5: Moderate correlation
- r = ±0.7: Strong correlation

*Spearman Correlation (\u03c1)*
- Non-parametric alternative
- Measures monotonic relationship
- No normality assumption
- Use for ordinal data or non-linear relationships

**Simple Linear Regression**
- Predicts outcome from one predictor
- Y = \u03b2₀ + \u03b2₁X + \u03b5
- \u03b2₁ = slope (change in Y per unit X)
- R² = proportion of variance explained

**Multiple Regression**
- Predicts outcome from multiple predictors
- Controls for confounding
- Assesses independent effects
- Check for multicollinearity

**Logistic Regression**
- For binary outcomes
- Predicts probability of outcome
- Odds ratios as effect measures
- Can include multiple predictors

### Survival Analysis

**Kaplan-Meier Curves**
- Estimates survival over time
- Accounts for censoring
- Visual comparison of groups
- Log-rank test for group differences

**Cox Proportional Hazards Regression**
- Predicts time to event
- Hazard ratios as effect measures
- Can include multiple predictors
- Assumes proportional hazards

## Effect Sizes

### Continuous Outcomes

**Mean Difference (MD)**
- Absolute difference in means
- Same units as outcome
- Clinically interpretable

**Standardized Mean Difference (SMD)**
- Difference in standard deviation units
- Cohen's d or Hedges' g
- Enables comparison across studies
- Interpretation:
  - 0.2 = small effect
  - 0.5 = medium effect
  - 0.8 = large effect

### Binary Outcomes

**Risk Ratio (RR)**
- Ratio of risks in two groups
- RR = 1: No difference
- RR > 1: Increased risk
- RR < 1: Decreased risk

**Odds Ratio (OR)**
- Ratio of odds in two groups
- Similar interpretation to RR
- Approximates RR when outcome rare
- Commonly used in case-control studies and logistic regression

**Risk Difference (RD)**
- Absolute difference in risks
- Clinically meaningful
- Number Needed to Treat (NNT) = 1 / RD

**Number Needed to Treat (NNT)**
- Number of patients to treat to prevent one event
- Lower NNT = more effective
- Example: NNT = 10 means treat 10 to prevent 1 event

## Multiple Comparisons

### Problem
- Multiple tests increase false positive rate
- With 20 tests at \u03b1 = 0.05, expect 1 false positive
- Family-wise error rate increases

### Corrections

**Bonferroni Correction**
- Divide \u03b1 by number of tests
- Example: 10 tests, \u03b1 = 0.05/10 = 0.005
- Conservative (may miss true effects)

**Holm-Bonferroni**
- Sequential Bonferroni
- Less conservative than Bonferroni
- Controls family-wise error rate

**False Discovery Rate (FDR)**
- Controls proportion of false positives among significant results
- Less conservative than Bonferroni
- Benjamini-Hochberg procedure

**Pre-Specification**
- Specify primary outcome and analyses in advance
- Reduces need for correction
- Distinguish primary from secondary analyses

## Common Statistical Errors

### Misinterpretation of P-Values

**Errors**
- P-value is NOT probability that null hypothesis is true
- P < 0.05 does NOT mean result is important
- P > 0.05 does NOT mean no effect exists
- P-value depends on sample size

**Correct Interpretation**
- P-value is probability of observing data (or more extreme) if null true
- Consider effect size and confidence interval
- Non-significant result may be due to low power

### Confusing Statistical and Clinical Significance

**Statistical Significance**
- P < 0.05
- Depends on sample size
- Large sample can make trivial effect significant

**Clinical Significance**
- Meaningful difference in practice
- Depends on context and values
- Small effect may be clinically important (or not)

**Example**
- Drug reduces blood pressure by 1 mmHg (p < 0.001)
- Statistically significant but clinically trivial

### Ignoring Confidence Intervals

**Errors**
- Focusing only on p-value
- Not considering precision of estimate
- Ignoring range of plausible values

**Correct Approach**
- Report and interpret confidence intervals
- Wide CI indicates imprecision
- CI provides more information than p-value

### Inappropriate Statistical Tests

**Errors**
- Using parametric test when assumptions violated
- Using t-test for multiple groups (should use ANOVA)
- Using multiple t-tests instead of ANOVA (inflates Type I error)
- Ignoring paired nature of data

**Correct Approach**
- Check assumptions before choosing test
- Use appropriate test for data structure
- Consider non-parametric alternatives if assumptions violated

### Correlation vs. Causation

**Error**
- Assuming correlation implies causation
- Confounding variables may explain association

**Correct Approach**
- Correlation shows association, not causation
- Consider alternative explanations
- Experimental designs (RCTs) better for causation
- Hill's criteria for causation

## Interpreting Results

### Assessing Magnitude

**Effect Size**
- How large is the difference?
- Is it clinically meaningful?
- Consider context and baseline risk

**Confidence Interval**
- What is the range of plausible values?
- Does it include clinically important values?
- How precise is the estimate?

### Assessing Precision

**Sample Size**
- Larger sample = more precise estimate
- Check if adequately powered

**Confidence Interval Width**
- Narrow CI = precise estimate
- Wide CI = imprecise estimate

### Assessing Significance

**P-Value**
- Is result statistically significant?
- Consider multiple comparisons
- Don't over-interpret borderline p-values

**Clinical Significance**
- Is result clinically meaningful?
- Does it change practice?
- Do benefits outweigh harms and costs?

## Reporting Statistics

### Essential Elements

**Descriptive Statistics**
- Mean ± SD or Median (IQR)
- Sample sizes for all groups
- Baseline characteristics

**Inferential Statistics**
- Test statistic and p-value
- Effect size and confidence interval
- Degrees of freedom (for t-tests, ANOVA)

**Example**
- "Mean blood pressure was lower in treatment group (120 ± 10 mmHg) than control (130 ± 12 mmHg), mean difference -10 mmHg (95% CI: -15 to -5), t(98) = -4.2, p < 0.001."

### Figures and Tables

**Tables**
- Baseline characteristics (Table 1)
- Main results by outcome
- Clear labels and units
- Footnotes for abbreviations and statistics

**Figures**
- Bar charts for categorical data
- Box plots for continuous data
- Line graphs for trends over time
- Forest plots for meta-analysis
- Kaplan-Meier curves for survival
- Error bars (SE or CI, specify which)

## Advanced Topics

### Bayesian Statistics

**Approach**
- Incorporates prior knowledge
- Updates beliefs with data
- Provides probability of hypothesis
- Credible intervals instead of confidence intervals

**Advantages**
- More intuitive interpretation
- Can incorporate prior evidence
- Handles small samples better

**Challenges**
- Requires specification of priors
- More complex computation
- Less familiar to many readers

### Missing Data

**Types**
- Missing Completely at Random (MCAR)
- Missing at Random (MAR)
- Missing Not at Random (MNAR)

**Approaches**
- Complete case analysis (listwise deletion)
- Multiple imputation
- Maximum likelihood
- Sensitivity analysis

**Reporting**
- Report amount and pattern of missing data
- Describe how missing data handled
- Assess impact on results

### Propensity Score Methods

**Purpose**
- Reduce confounding in observational studies
- Balance groups on observed covariates
- Approximate randomization

**Methods**
- Matching
- Stratification
- Inverse probability weighting
- Covariate adjustment

**Limitations**
- Only controls for measured confounders
- Assumes no unmeasured confounding
- Requires large sample size

## Conclusion

Understanding statistical methods and interpretation is essential for critical appraisal of research. Focus on effect sizes and confidence intervals, not just p-values. Consider clinical significance alongside statistical significance. Be aware of common errors and limitations. With these skills, you can better evaluate research quality and applicability to your context.
