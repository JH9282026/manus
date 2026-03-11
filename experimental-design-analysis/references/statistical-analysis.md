# Statistical Analysis of Experiments

## ANOVA (Analysis of Variance)

### One-Way ANOVA
Compare means across 3+ groups:
1. Check assumptions: normality, equal variance, independence
2. Calculate F-statistic: Between-group variance / within-group variance
3. If F is significant: Conduct post-hoc pairwise comparisons
4. Report: F(df_between, df_within) = value, p-value, effect size (η²)

### Post-Hoc Tests

| Test | When to Use |
|---|---|
| Tukey HSD | All pairwise comparisons, equal sample sizes |
| Bonferroni | Few planned comparisons |
| Dunnett | Compare all groups to a single control |
| Games-Howell | Unequal variances |
| Scheffé | Complex contrasts |

### Two-Way Factorial ANOVA
- Tests main effect of Factor A
- Tests main effect of Factor B
- Tests interaction effect (A × B)
- Interaction effect is often the most interesting finding
- Plot interaction diagrams to visualize

---

## Regression Analysis

### Linear Regression for Experiments
- Useful when factors are continuous
- Can handle both categorical and continuous predictors
- Model: Y = β₀ + β₁X₁ + β₂X₂ + β₁₂X₁X₂ + ε
- Include interaction terms when factorial design is used

### Key Diagnostics
- **Residual plots**: Check for patterns (should be random)
- **Q-Q plot**: Verify normality assumption
- **Leverage/influence**: Identify influential observations
- **Multicollinearity**: Check VIF (variance inflation factor)
- **R²**: Proportion of variance explained (don't over-rely on it)

---

## Non-Parametric Alternatives

| Parametric Test | Non-Parametric Alternative | When to Use |
|---|---|---|
| Independent t-test | Mann-Whitney U | Non-normal data, ordinal data |
| Paired t-test | Wilcoxon signed-rank | Paired non-normal data |
| One-way ANOVA | Kruskal-Wallis | Non-normal, 3+ groups |
| Two-way ANOVA | Friedman test | Repeated measures, non-normal |
| Pearson correlation | Spearman correlation | Non-linear relationships |

---

## Multiple Testing Correction

When running multiple comparisons, control the family-wise error rate:

| Method | Approach | Strictness |
|---|---|---|
| Bonferroni | Divide α by number of tests | Very conservative |
| Holm-Bonferroni | Step-down procedure | Less conservative |
| Benjamini-Hochberg | Controls false discovery rate | Moderate |
| No correction | Accept inflated Type I error | Exploratory only |

---

## Reporting Experimental Results

### Required Elements
1. **Design description**: Factors, levels, blocking, randomization
2. **Sample size justification**: Power analysis or practical constraints
3. **Descriptive statistics**: Means, SDs, confidence intervals by group
4. **Test results**: Test statistic, degrees of freedom, p-value
5. **Effect size**: Cohen's d, η², R², or practical difference
6. **Visualizations**: Box plots, interaction plots, forest plots
7. **Assumptions checked**: Normality, homogeneity, independence
8. **Practical significance**: Does the statistical difference matter in context?
