# Common Statistical Tests for Hypothesis Testing

## Overview
Different statistical tests are used for different types of data and research questions. This guide covers the most common hypothesis tests, when to use them, and how to interpret results.

## Tests for Continuous Data

### Z-Test
**Purpose:** Compare sample mean to population mean (known variance) or compare two means with large samples.

**When to Use:**
- Large sample size (n > 30)
- Population standard deviation known
- Data approximately normally distributed

**Formula:**
```
Z = (X̄ - μ) / (σ / √n)
```

**Example:** Testing if average height of sample differs from known population average.

### T-Test
**Purpose:** Compare means when population variance unknown or sample size small.

**Types:**

**One-Sample T-Test**
- Compare sample mean to hypothesized value
- H₀: μ = μ₀
- Example: Is average test score different from 75?

**Independent Samples T-Test**
- Compare means of two independent groups
- H₀: μ₁ = μ₂
- Example: Do men and women have different average salaries?

**Paired Samples T-Test**
- Compare means of same group at two times
- H₀: μ_diff = 0
- Example: Do students score higher after training?

**Assumptions:**
- Normality (especially for small samples)
- Independence of observations
- Equal variances (for independent samples)

### ANOVA (Analysis of Variance)
**Purpose:** Compare means of three or more groups simultaneously.

**When to Use:**
- Comparing 3+ groups
- One continuous dependent variable
- One or more categorical independent variables

**Types:**

**One-Way ANOVA**
- One independent variable
- Example: Compare test scores across three teaching methods

**Two-Way ANOVA**
- Two independent variables
- Tests main effects and interaction
- Example: Effect of teaching method and gender on scores

**Repeated Measures ANOVA**
- Same subjects measured multiple times
- Example: Test scores at three time points

**Post-Hoc Tests:**
- Tukey HSD
- Bonferroni
- Scheffé
- Used after significant ANOVA to identify which groups differ

## Tests for Categorical Data

### Chi-Square Test
**Purpose:** Test relationships between categorical variables.

**Types:**

**Chi-Square Test of Independence**
- Test if two categorical variables are related
- H₀: Variables are independent
- Example: Is gender related to product preference?

**Chi-Square Goodness-of-Fit**
- Test if observed frequencies match expected
- H₀: Data fits specified distribution
- Example: Are dice rolls uniformly distributed?

**Assumptions:**
- Expected frequency ≥ 5 in each cell
- Independent observations
- Random sampling

### Fisher's Exact Test
**Purpose:** Alternative to chi-square for small samples.

**When to Use:**
- 2×2 contingency tables
- Small expected frequencies
- Exact p-values needed

## Tests for Relationships

### Correlation Tests
**Purpose:** Test if two continuous variables are related.

**Pearson Correlation**
- Linear relationship
- Both variables continuous and normally distributed
- H₀: ρ = 0 (no correlation)

**Spearman Correlation**
- Monotonic relationship
- Ordinal data or non-normal distributions
- Rank-based test

**Kendall's Tau**
- Alternative rank correlation
- Better for small samples with ties

### Regression Tests
**Purpose:** Test if independent variables predict dependent variable.

**Simple Linear Regression**
- One predictor
- Tests if slope ≠ 0
- H₀: β₁ = 0

**Multiple Regression**
- Multiple predictors
- Tests overall model and individual predictors
- F-test for overall model
- T-tests for individual coefficients

## Non-Parametric Tests

### When to Use
- Data not normally distributed
- Ordinal data
- Small sample sizes
- Outliers present
- Assumptions of parametric tests violated

### Common Non-Parametric Tests

**Mann-Whitney U Test**
- Non-parametric alternative to independent t-test
- Compares medians of two independent groups
- Rank-based test

**Wilcoxon Signed-Rank Test**
- Non-parametric alternative to paired t-test
- Compares two related samples
- Tests median difference

**Kruskal-Wallis Test**
- Non-parametric alternative to one-way ANOVA
- Compares medians of 3+ independent groups
- Rank-based test

**Friedman Test**
- Non-parametric alternative to repeated measures ANOVA
- Compares related samples across 3+ conditions

## Test Selection Guide

### Decision Tree

**1. What type of data?**
- Continuous → Go to 2
- Categorical → Go to 5

**2. How many groups?**
- One group → One-sample t-test or Z-test
- Two groups → Go to 3
- Three or more groups → ANOVA

**3. Are groups independent or related?**
- Independent → Independent t-test
- Related/Paired → Paired t-test

**4. Are assumptions met?**
- Yes → Use parametric test
- No → Use non-parametric alternative

**5. Categorical data - what are you testing?**
- Relationship between variables → Chi-square test
- Goodness of fit → Chi-square goodness-of-fit
- Small sample → Fisher's exact test

## Interpreting Results

### Test Output Components

**Test Statistic**
- Quantifies deviation from null hypothesis
- Larger absolute value = more evidence against H₀

**Degrees of Freedom (df)**
- Related to sample size
- Affects critical values and p-values

**P-Value**
- Probability of results if H₀ true
- Compare to α for decision

**Confidence Interval**
- Range of plausible values
- Provides effect size information

### Reporting Results

**Example T-Test:**
\"An independent samples t-test revealed a statistically significant difference in test scores between the treatment group (M = 85.3, SD = 12.1) and control group (M = 78.6, SD = 11.8), t(48) = 2.34, p = 0.023, 95% CI [1.2, 12.2], Cohen's d = 0.57.\"

**Example ANOVA:**
\"A one-way ANOVA showed a significant effect of teaching method on test scores, F(2, 87) = 5.67, p = 0.005, η² = 0.12. Post-hoc Tukey tests revealed that Method A (M = 82.3) significantly outperformed Method C (M = 75.1, p = 0.004).\"

**Example Chi-Square:**
\"A chi-square test of independence revealed a significant association between gender and product preference, χ²(2) = 8.45, p = 0.015, Cramer's V = 0.29.\"

## Common Mistakes

1. **Wrong Test Selection:** Using parametric test when assumptions violated
2. **Multiple Testing:** Not correcting for multiple comparisons
3. **Ignoring Assumptions:** Not checking normality, independence, etc.
4. **Confusing Correlation and Causation:** Significant relationship ≠ causation
5. **Ignoring Effect Size:** Focusing only on p-value
6. **One-Tailed When Two-Tailed Appropriate:** Using one-tailed to get significance
7. **Post-Hoc Without Correction:** Multiple comparisons without adjustment

## Software Implementation

### R Examples
```r
# T-test
t.test(group1, group2)

# ANOVA
aov_result <- aov(score ~ method, data = df)
summary(aov_result)

# Chi-square
chisq.test(table(var1, var2))

# Correlation
cor.test(x, y, method = "pearson")
```

### Python Examples
```python
from scipy import stats

# T-test
stats.ttest_ind(group1, group2)

# ANOVA
stats.f_oneway(group1, group2, group3)

# Chi-square
stats.chi2_contingency(contingency_table)

# Correlation
stats.pearsonr(x, y)
```

## References

- Investopedia. \"Hypothesis Testing\" https://www.investopedia.com/terms/h/hypothesistesting.asp
- Penn State. \"Statistical Hypothesis Testing\" https://online.stat.psu.edu/stat502/lesson/1
- DataCamp. \"Hypothesis Testing Made Easy\" https://www.datacamp.com/tutorial/hypothesis-testing
