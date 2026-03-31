# Statistical Analysis Methods in Quantitative Research

## Introduction to Statistical Analysis

Statistical analysis transforms raw data into meaningful information, enabling researchers to describe phenomena, test hypotheses, identify relationships, and make inferences about populations. This guide covers fundamental and advanced statistical methods commonly used in quantitative research.

## Descriptive Statistics

### Measures of Central Tendency

**Mean (Arithmetic Average)**
- Sum of values divided by number of values
- Most common measure
- Sensitive to outliers
- Appropriate for interval/ratio data

**Median**
- Middle value when ordered
- Resistant to outliers
- Appropriate for ordinal, interval, ratio data
- Better than mean for skewed distributions

**Mode**
- Most frequent value
- Can have multiple modes
- Appropriate for all levels of measurement
- Useful for categorical data

### Measures of Variability

**Range**
- Difference between maximum and minimum
- Simple but limited
- Sensitive to outliers
- Provides basic spread information

**Variance**
- Average squared deviation from mean
- Foundation for many statistics
- Units are squared
- Sensitive to outliers

**Standard Deviation (SD)**
- Square root of variance
- Same units as original data
- Most common variability measure
- Interpretable with normal distribution

**Interquartile Range (IQR)**
- Range of middle 50% of data
- Q3 - Q1
- Resistant to outliers
- Used with median

**Coefficient of Variation**
- SD divided by mean
- Relative variability
- Compares variability across different scales
- Expressed as percentage

### Measures of Distribution Shape

**Skewness**
- Asymmetry of distribution
- Positive skew: Tail to right
- Negative skew: Tail to left
- Zero: Symmetric

**Kurtosis**
- Peakedness of distribution
- Positive: Heavy tails, peaked
- Negative: Light tails, flat
- Affects statistical tests

### Frequency Distributions

**Frequency Tables**
- Count of observations per category
- Percentages and cumulative percentages
- Appropriate for categorical data
- Foundation for chi-square tests

**Histograms**
- Visual representation of distribution
- Continuous data
- Identify shape and outliers
- Assess normality

**Box Plots**
- Visual summary of distribution
- Shows median, quartiles, outliers
- Compare groups
- Identify skewness

## Inferential Statistics

### Hypothesis Testing Framework

**Null Hypothesis (H₀)**
- No effect or relationship
- Status quo
- What we test against
- Assume true until evidence otherwise

**Alternative Hypothesis (H₁ or Hₐ)**
- Effect or relationship exists
- Research hypothesis
- What we hope to support
- Directional or non-directional

**Type I Error (α)**
- Reject true null hypothesis
- False positive
- Significance level (typically .05)
- Controlled by researcher

**Type II Error (β)**
- Fail to reject false null hypothesis
- False negative
- Related to statistical power
- Power = 1 - β

**Statistical Power**
- Probability of detecting true effect
- Typically aim for .80
- Affected by sample size, effect size, α
- Calculated via power analysis

**P-Value**
- Probability of obtaining results if H₀ true
- Not probability H₀ is true
- Compare to α level
- Smaller p-value = stronger evidence against H₀

**Effect Size**
- Magnitude of effect
- Independent of sample size
- Practical significance
- Examples: Cohen's d, r, η²

### Parametric Tests

**Assumptions:**
- Normal distribution
- Homogeneity of variance
- Independence of observations
- Interval or ratio data

**Independent Samples t-Test**

**Purpose**: Compare means of two independent groups

**Assumptions:**
- Independent groups
- Normal distribution
- Homogeneity of variance
- Interval/ratio DV

**Effect Size**: Cohen's d

**Example**: Compare test scores between treatment and control groups

**Paired Samples t-Test**

**Purpose**: Compare means of two related groups

**Assumptions:**
- Related/paired observations
- Normal distribution of differences
- Interval/ratio DV

**Effect Size**: Cohen's d

**Example**: Compare pre-test and post-test scores

**One-Way ANOVA**

**Purpose**: Compare means of three or more independent groups

**Assumptions:**
- Independent groups
- Normal distribution
- Homogeneity of variance
- Interval/ratio DV

**Effect Size**: η² (eta squared)

**Post-Hoc Tests**: Tukey HSD, Bonferroni, Scheffé

**Example**: Compare test scores across three teaching methods

**Repeated Measures ANOVA**

**Purpose**: Compare means across three or more time points or conditions

**Assumptions:**
- Related observations
- Normal distribution
- Sphericity (equal variances of differences)
- Interval/ratio DV

**Effect Size**: Partial η²

**Correction**: Greenhouse-Geisser or Huynh-Feldt if sphericity violated

**Example**: Compare performance across four time points

**Factorial ANOVA**

**Purpose**: Examine effects of two or more independent variables

**Types:**
- Two-way ANOVA (2 IVs)
- Three-way ANOVA (3 IVs)
- Higher-order designs

**Effects:**
- Main effects (each IV separately)
- Interaction effects (IVs combined)

**Example**: Examine effects of teaching method and class size on achievement

**ANCOVA (Analysis of Covariance)**

**Purpose**: Compare means while controlling for covariates

**Advantages:**
- Reduces error variance
- Controls for confounds
- Increases statistical power
- Adjusts for baseline differences

**Assumptions:**
- All ANOVA assumptions
- Linear relationship between covariate and DV
- Homogeneity of regression slopes

**Example**: Compare treatment effects controlling for baseline scores

**MANOVA (Multivariate Analysis of Variance)**

**Purpose**: Compare groups on multiple dependent variables simultaneously

**Advantages:**
- Controls for Type I error across DVs
- Detects patterns across DVs
- More powerful when DVs correlated

**Test Statistics**: Wilks' Lambda, Pillai's Trace, Hotelling's Trace

**Example**: Compare groups on multiple outcome measures

### Non-Parametric Tests

**When to Use:**
- Violations of parametric assumptions
- Ordinal data
- Small sample sizes
- Non-normal distributions

**Mann-Whitney U Test**

**Purpose**: Non-parametric alternative to independent t-test

**Compares**: Ranks of two independent groups

**Effect Size**: r = Z / √N

**Example**: Compare ordinal ratings between two groups

**Wilcoxon Signed-Rank Test**

**Purpose**: Non-parametric alternative to paired t-test

**Compares**: Ranks of two related groups

**Effect Size**: r = Z / √N

**Example**: Compare pre-post ordinal ratings

**Kruskal-Wallis Test**

**Purpose**: Non-parametric alternative to one-way ANOVA

**Compares**: Ranks of three or more independent groups

**Post-Hoc**: Dunn's test with Bonferroni correction

**Example**: Compare ordinal ratings across three groups

**Friedman Test**

**Purpose**: Non-parametric alternative to repeated measures ANOVA

**Compares**: Ranks across three or more related groups

**Post-Hoc**: Wilcoxon signed-rank with Bonferroni correction

**Example**: Compare ordinal ratings across multiple time points

**Chi-Square Tests**

**Chi-Square Goodness of Fit**

**Purpose**: Test if observed frequencies match expected frequencies

**Example**: Test if die rolls are equally distributed

**Chi-Square Test of Independence**

**Purpose**: Test relationship between two categorical variables

**Effect Size**: Cramér's V, phi coefficient

**Example**: Test relationship between gender and voting preference

**Fisher's Exact Test**

**Purpose**: Alternative to chi-square for small samples

**When to Use**: Expected frequencies < 5

**Example**: 2x2 contingency tables with small samples

## Correlation and Regression

### Correlation Analysis

**Pearson Correlation (r)**

**Purpose**: Measure linear relationship between two continuous variables

**Range**: -1 to +1

**Assumptions:**
- Linear relationship
- Bivariate normal distribution
- Interval/ratio data

**Interpretation:**
- r = 0: No linear relationship
- r = ±.10 to ±.29: Small
- r = ±.30 to ±.49: Medium
- r = ±.50 to ±1.0: Large

**Spearman Correlation (ρ)**

**Purpose**: Non-parametric correlation for ordinal or non-normal data

**Based on**: Ranks

**When to Use**: Ordinal data, non-linear monotonic relationships, outliers

**Kendall's Tau (τ)**

**Purpose**: Alternative non-parametric correlation

**Advantages**: Better for small samples, more accurate p-values

**Point-Biserial Correlation**

**Purpose**: Correlation between continuous and dichotomous variables

**Example**: Relationship between test score and pass/fail

**Partial Correlation**

**Purpose**: Correlation between two variables controlling for third variable

**Removes**: Influence of control variable

**Example**: Correlation between X and Y controlling for Z

### Simple Linear Regression

**Purpose**: Predict DV from single IV

**Equation**: Y = a + bX + e

**Components:**
- Y: Dependent variable
- X: Independent variable
- a: Intercept
- b: Slope (regression coefficient)
- e: Error term

**R²**: Proportion of variance explained

**Assumptions:**
- Linearity
- Independence of errors
- Homoscedasticity
- Normality of residuals
- No multicollinearity (for multiple regression)

**Interpretation:**
- Slope: Change in Y for one-unit change in X
- Intercept: Value of Y when X = 0
- R²: Percentage of variance explained

### Multiple Linear Regression

**Purpose**: Predict DV from multiple IVs

**Equation**: Y = a + b₁X₁ + b₂X₂ + ... + bₖXₖ + e

**Methods:**

**Simultaneous (Enter)**
- All IVs entered at once
- Tests full model
- Most common

**Hierarchical**
- IVs entered in blocks
- Theory-driven order
- Tests incremental variance

**Stepwise**
- Statistical selection of IVs
- Forward, backward, or both
- Data-driven, atheoretical

**Interpretation:**

**Unstandardized Coefficients (b)**
- Original units
- Specific to sample
- Used for prediction

**Standardized Coefficients (β)**
- Standard deviation units
- Compare relative importance
- Independent of scale

**R² and Adjusted R²**
- R²: Proportion of variance explained
- Adjusted R²: Accounts for number of predictors
- Use adjusted R² for model comparison

**Multicollinearity**
- High correlation among IVs
- Inflates standard errors
- Check VIF (< 10) and tolerance (> .10)

### Logistic Regression

**Purpose**: Predict categorical DV from continuous or categorical IVs

**Binary Logistic Regression**
- Dichotomous DV
- Predicts probability of outcome
- Odds ratios for interpretation

**Multinomial Logistic Regression**
- Nominal DV with 3+ categories
- Multiple comparisons
- Reference category

**Ordinal Logistic Regression**
- Ordinal DV
- Proportional odds assumption
- Cumulative probabilities

**Interpretation:**
- Odds Ratio (OR): Change in odds for one-unit change in IV
- OR = 1: No effect
- OR > 1: Increased odds
- OR < 1: Decreased odds

## Advanced Statistical Methods

### Factor Analysis

**Exploratory Factor Analysis (EFA)**

**Purpose**: Identify underlying factor structure

**Process:**
1. Assess suitability (KMO, Bartlett's test)
2. Extract factors (eigenvalue > 1, scree plot)
3. Rotate factors (varimax, promax)
4. Interpret and name factors

**Confirmatory Factor Analysis (CFA)**

**Purpose**: Test hypothesized factor structure

**Fit Indices:**
- χ²: Non-significant preferred
- CFI, TLI: > .90 or .95
- RMSEA: < .08 or .06
- SRMR: < .08

### Structural Equation Modeling (SEM)**

**Purpose**: Test complex relationships among variables

**Components:**
- Measurement model (CFA)
- Structural model (path analysis)
- Latent and observed variables

**Advantages:**
- Tests complex models
- Accounts for measurement error
- Multiple DVs
- Mediation and moderation

### Multilevel Modeling (HLM)**

**Purpose**: Analyze nested or hierarchical data

**Examples:**
- Students within schools
- Repeated measures within individuals
- Employees within organizations

**Advantages:**
- Accounts for non-independence
- Partitions variance across levels
- Tests cross-level interactions

### Time Series Analysis

**Purpose**: Analyze data collected over time

**Methods:**
- ARIMA models
- Interrupted time series
- Growth curve modeling
- Survival analysis

**Applications:**
- Trend analysis
- Forecasting
- Intervention effects
- Longitudinal data

## Statistical Software

**SPSS**
- User-friendly interface
- Comprehensive statistics
- Widely used in social sciences
- Point-and-click and syntax

**R**
- Open-source and free
- Extensive packages
- Flexible and powerful
- Steep learning curve

**SAS**
- Powerful and comprehensive
- Industry standard
- Expensive
- Programming-based

**Stata**
- Econometrics focus
- User-friendly
- Good documentation
- Moderate cost

**JASP**
- Free and open-source
- User-friendly
- Bayesian statistics
- Similar to SPSS

**Mplus**
- SEM and advanced modeling
- Comprehensive
- Expensive
- Syntax-based

## Conclusion

Statistical analysis is essential for transforming data into knowledge. Selecting appropriate methods requires understanding research questions, data characteristics, assumptions, and interpretation. Mastery of statistical methods enables rigorous quantitative research that advances understanding and informs evidence-based practice.
