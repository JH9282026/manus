# Hypothesis Testing Fundamentals

## Overview
Statistical hypothesis testing is a systematic method of statistical inference used to determine whether data provides sufficient evidence to reject a particular assumption about a population. It is fundamental to scientific research, business analytics, and data-driven decision-making.

## Core Concepts

### Null Hypothesis (H₀)
The null hypothesis is the default assumption that there is no effect, no difference, or no relationship between variables.

**Characteristics:**
- Represents the status quo
- Assumes no change or no impact
- Always contains equality (=, ≤, or ≥)
- Presumed true until evidence proves otherwise
- Similar to "presumption of innocence" in legal systems

**Examples:**
- There is no difference in salary based on gender
- The new drug has no effect on disease symptoms
- There is no relationship between height and shoe size
- The mean GPA is equal to 2.0
- The proportion is no more than 30%

### Alternative Hypothesis (H₁ or Hₐ)
The alternative hypothesis proposes that an effect, difference, or relationship does exist.

**Characteristics:**
- Contradicts the null hypothesis
- Represents the research claim
- Always uses inequality (≠, >, or <)
- Accepted only when null is rejected
- Often what researcher hopes to prove

**Examples:**
- Male workers have higher salary than female workers
- The new drug significantly reduces symptoms
- There is a positive relationship between height and shoe size
- The mean GPA is different from 2.0
- The proportion is more than 30%

### Types of Hypotheses

**Two-Sided (Two-Tailed) Hypothesis**
- Tests for difference in either direction
- H₀: μ = value
- H₁: μ ≠ value
- Used when direction is unknown or irrelevant

**One-Sided (One-Tailed) Hypothesis**
- Tests for difference in specific direction
- Right-tailed: H₀: μ ≤ value, H₁: μ > value
- Left-tailed: H₀: μ ≥ value, H₁: μ < value
- Used when direction is specified by research question

## The Hypothesis Testing Process

### Step 1: State the Hypotheses
Clearly define null (H₀) and alternative (H₁) hypotheses based on research question.

**Example:**
- Research Question: Does the new teaching method improve test scores?
- H₀: μ_new ≤ μ_old (new method is not better)
- H₁: μ_new > μ_old (new method is better)

### Step 2: Choose Significance Level (α)
Select maximum acceptable probability of Type I error.

**Common Significance Levels:**
- α = 0.05 (5%) - Most common
- α = 0.01 (1%) - More stringent
- α = 0.10 (10%) - More lenient

**Considerations:**
- Field standards and conventions
- Consequences of Type I error
- Sample size and power
- Research context

### Step 3: Collect and Prepare Data
Gather data using appropriate sampling methods.

**Requirements:**
- Representative sample
- Adequate sample size
- Random sampling when possible
- Data quality checks
- Assumption verification

### Step 4: Select Appropriate Test
Choose statistical test based on:
- Data type (continuous, categorical)
- Distribution (normal, non-normal)
- Sample size
- Number of groups
- Independence of observations

### Step 5: Calculate Test Statistic
Compute value quantifying deviation from null hypothesis.

**Common Test Statistics:**
- Z-statistic (large samples, known variance)
- T-statistic (small samples, unknown variance)
- Chi-square statistic (categorical data)
- F-statistic (comparing variances, ANOVA)

### Step 6: Determine P-value or Critical Value
Calculate probability of observing results if H₀ is true.

**P-value Approach:**
- Calculate p-value from test statistic
- Compare p-value to α
- More common in modern practice

**Critical Value Approach:**
- Determine critical value from distribution
- Compare test statistic to critical value
- Traditional approach

### Step 7: Make Decision
Decide whether to reject or fail to reject null hypothesis.

**Decision Rules:**
- If p-value ≤ α: Reject H₀
- If p-value > α: Fail to reject H₀
- If |test statistic| > critical value: Reject H₀
- If |test statistic| ≤ critical value: Fail to reject H₀

### Step 8: Interpret and Report
State conclusion in context of research question.

**Reporting Elements:**
- Test used and why
- Test statistic value
- P-value
- Decision (reject or fail to reject H₀)
- Practical interpretation
- Confidence interval (when applicable)
- Effect size

## Types of Errors

### Type I Error (α)
Rejecting true null hypothesis (false positive).

**Characteristics:**
- Probability = α (significance level)
- Concluding effect exists when it doesn't
- More serious in some contexts
- Controlled by choosing α

**Example:**
- Concluding drug is effective when it isn't
- Finding guilty person who is innocent

### Type II Error (β)
Failing to reject false null hypothesis (false negative).

**Characteristics:**
- Probability = β
- Missing real effect
- Related to statistical power (1 - β)
- Affected by sample size, effect size, α

**Example:**
- Concluding drug is ineffective when it works
- Finding innocent person who is guilty

### Balancing Errors
- Decreasing α increases β (and vice versa)
- Increase sample size to reduce both
- Consider consequences of each error type
- Choose α based on error cost trade-off

## Statistical Power

### Definition
Probability of correctly rejecting false null hypothesis.

**Formula:**
Power = 1 - β

**Interpretation:**
- Power = 0.80 means 80% chance of detecting real effect
- Higher power = better ability to detect effects
- Minimum acceptable power typically 0.80

### Factors Affecting Power

**Sample Size**
- Larger sample = higher power
- Most controllable factor
- Diminishing returns at very large sizes

**Effect Size**
- Larger effect = easier to detect
- Often not controllable
- Important for sample size planning

**Significance Level (α)**
- Higher α = higher power
- But increases Type I error risk
- Trade-off to consider

**Variability**
- Lower variability = higher power
- Better measurement reduces variability
- Homogeneous samples have less variability

## Assumptions and Conditions

### Common Assumptions

**Independence**
- Observations independent of each other
- No correlation between data points
- Violated by repeated measures, clustering
- Critical for valid inference

**Normality**
- Data follows normal distribution
- More important for small samples
- Central Limit Theorem helps with large samples
- Check with histograms, Q-Q plots, tests

**Equal Variance (Homoscedasticity)**
- Groups have similar variability
- Required for some tests (t-test, ANOVA)
- Check with Levene's test, F-test
- Robust tests available if violated

**Random Sampling**
- Sample randomly selected from population
- Ensures representativeness
- Allows generalization
- Often assumed but not always met

### Checking Assumptions

**Visual Methods:**
- Histograms for normality
- Q-Q plots for normality
- Scatter plots for linearity
- Residual plots for homoscedasticity

**Statistical Tests:**
- Shapiro-Wilk test for normality
- Kolmogorov-Smirnov test for normality
- Levene's test for equal variance
- Durbin-Watson test for independence

**Remedies for Violations:**
- Transformations (log, square root)
- Non-parametric tests
- Robust methods
- Larger sample sizes
- Different test selection

## Practical vs. Statistical Significance

### Statistical Significance
Indicates result is unlikely due to chance.

**Characteristics:**
- Based on p-value < α
- Affected by sample size
- Doesn't indicate importance
- Can be significant but trivial

### Practical Significance
Indicates result is meaningful in real-world context.

**Characteristics:**
- Based on effect size
- Considers practical impact
- Independent of sample size
- Requires domain knowledge

### Effect Size Measures

**Cohen's d**
- Standardized mean difference
- Small: 0.2, Medium: 0.5, Large: 0.8
- Independent of sample size

**Correlation Coefficient (r)**
- Strength of relationship
- Small: 0.1, Medium: 0.3, Large: 0.5

**Odds Ratio**
- Ratio of odds between groups
- Common in medical research

**R-squared**
- Proportion of variance explained
- Used in regression

## Best Practices

1. **Plan Before Collecting Data**: Define hypotheses and analysis plan
2. **Check Assumptions**: Verify test requirements are met
3. **Use Appropriate Test**: Match test to data and question
4. **Report Completely**: Include all relevant statistics
5. **Consider Effect Size**: Don't rely solely on p-values
6. **Avoid P-Hacking**: Don't manipulate data for significance
7. **Replicate Findings**: Confirm results with new data
8. **Interpret Carefully**: Statistical significance ≠ practical importance
9. **Use Confidence Intervals**: Provide range of plausible values
10. **Be Transparent**: Report all tests conducted, not just significant ones

## Common Mistakes

1. **Accepting the Null**: Should say "fail to reject," not "accept"
2. **Confusing Significance with Importance**: p < 0.05 doesn't mean large effect
3. **Ignoring Assumptions**: Using tests when assumptions violated
4. **Multiple Testing**: Not adjusting for multiple comparisons
5. **Cherry-Picking**: Reporting only significant results
6. **Misinterpreting P-values**: P-value is not probability H₀ is true
7. **Ignoring Effect Size**: Focusing only on statistical significance
8. **Insufficient Power**: Using too small sample size
9. **Causal Claims**: Inferring causation from correlation
10. **Ignoring Context**: Not considering practical implications

## References

- Wikipedia. "Statistical Hypothesis Test" https://en.wikipedia.org/wiki/Statistical_hypothesis_test
- Britannica. "Statistics - Hypothesis Testing" https://www.britannica.com/science/statistics/Hypothesis-testing
- Investopedia. "Hypothesis Testing: 4 Steps and Example" https://www.investopedia.com/terms/h/hypothesistesting.asp
- Simplilearn. "Hypothesis Testing in Statistics" https://www.simplilearn.com/tutorials/statistics-tutorial/hypothesis-testing-in-statistics
- Scribbr. "Hypothesis Testing | A Step-by-Step Guide" https://www.scribbr.com/statistics/hypothesis-testing/
- DataCamp. "Hypothesis Testing Made Easy" https://www.datacamp.com/tutorial/hypothesis-testing
