---
name: r-statistical-analysis
description: "Perform statistical analysis using R programming language with packages like dplyr, ggplot2, tidyr, and specialized statistical libraries. Use for data manipulation, visualization, hypothesis testing, regression analysis, time series analysis, panel data modeling, and reproducible research with R Markdown."
---

# R Statistical Analysis

Perform comprehensive statistical analysis using R programming language and its extensive ecosystem of packages.

## Overview

R is a powerful open-source programming language designed specifically for statistical computing and data analysis. With over 18,000 packages available through CRAN, R provides tools for everything from basic descriptive statistics to advanced econometric modeling and machine learning. This skill covers the essential packages, methods, and best practices for conducting statistical analysis in R.

## Core Package Ecosystem

### Data Manipulation and Cleaning

| Package | Primary Use | Key Functions |
|---------|-------------|---------------|
| `dplyr` | Data manipulation | `filter()`, `mutate()`, `arrange()`, `summarise()`, pipe operator `%>%` |
| `tidyr` | Data reshaping | `gather()`, `spread()`, `unite()`, `separate()` |
| `readr` | Data import | Fast CSV reading, cleaner than base R |
| `lubridate` | Date/time handling | `year()`, `month()`, `day()`, time zone management |
| `plyr` | Split-apply-combine | Breaking large problems into manageable pieces |

### Visualization

| Package | Purpose | Best For |
|---------|---------|----------|
| `ggplot2` | Static graphics | Layered, customizable plots based on Grammar of Graphics |
| `plotly` | Interactive graphics | Web-based interactive visualizations |
| `ggpattern` | Pattern fills | Adding geometric and image-based patterns to ggplot2 |

### Statistical Modeling

| Package | Analysis Type | Key Functions |
|---------|---------------|---------------|
| `plm` | Panel data | Fixed effects, random effects models |
| `ivreg` | Instrumental variables | Two-stage least squares regression |
| `tseries` | Time series | `adf.test()` for stationarity testing |
| `urca` | Cointegration | `ca.jo()` for Johansen test |
| `vars` | Vector autoregression | `irf()` for impulse response functions |

### Machine Learning

| Package | Framework | Capabilities |
|---------|-----------|-------------|
| `mlr3` | ML operations | Model evaluation, cross-validation, hyperparameter tuning |
| `caret` | Classification & regression | Unified interface to 200+ ML algorithms |

## The Tidyverse Philosophy

The `tidyverse` is an opinionated collection of R packages that share a unified grammar and design philosophy:

- **Consistency**: Functions work together seamlessly
- **Simplicity**: Intuitive syntax reduces cognitive load
- **Brevity**: Accomplish more with less code
- **Modularity**: Composable functions for complex workflows

Core tidyverse packages: `ggplot2`, `dplyr`, `tidyr`, `purrr`, `stringr`, `readr`

## Essential Workflow Patterns

### The Pipe Operator (`%>%`)

Chain multiple operations into readable, sequential workflows:

```r
data %>%
  filter(year >= 2020) %>%
  mutate(revenue = price * quantity) %>%
  group_by(region) %>%
  summarise(total_revenue = sum(revenue)) %>%
  arrange(desc(total_revenue))
```

### Tidy Data Principles

Structure data where:
- Each column is a variable
- Each row is an observation
- Each cell contains a single value

This format optimizes data for analysis in R.

## Statistical Analysis Workflow

### 1. Data Import and Exploration

- Use `readr::read_csv()` for fast, clean CSV imports
- Explore with `summary()`, `str()`, `head()`
- Check for missing values with `is.na()`

### 2. Data Cleaning and Transformation

- Filter rows with `dplyr::filter()`
- Create new variables with `dplyr::mutate()`
- Reshape data with `tidyr::gather()` and `tidyr::spread()`
- Handle dates with `lubridate` functions

### 3. Exploratory Data Analysis

- Generate summary statistics with `dplyr::summarise()`
- Create visualizations with `ggplot2`
- Identify patterns, outliers, and relationships

### 4. Statistical Modeling

- Linear models: `lm()` (base R)
- Generalized linear models: `glm()`
- Panel data: `plm::plm()`
- Time series: `tseries`, `urca`, `vars` packages
- Machine learning: `mlr3` or `caret` frameworks

### 5. Model Evaluation and Validation

- Check model diagnostics
- Perform cross-validation
- Compare models using AIC, BIC, or other criteria

### 6. Reporting and Reproducibility

- Use `knitr` for dynamic report generation
- Combine code, output, and narrative in R Markdown
- Ensure analyses are fully reproducible

## Best Practices

### Before Starting Analysis

1. **Define your analytical goals clearly** — Know what questions you're trying to answer
2. **Understand your data structure** — Examine variables, types, and relationships
3. **Plan your workflow** — Sketch out the analysis pipeline before coding

### During Analysis

1. **Use the pipe operator** — Create readable, sequential workflows
2. **Follow tidy data principles** — Structure data for efficient analysis
3. **Leverage tidyverse consistency** — Use compatible packages that work together
4. **Comment your code** — Explain why, not just what
5. **Work iteratively** — Build complexity gradually, testing at each step

### After Analysis

1. **Document thoroughly** — Use R Markdown for reproducible reports
2. **Validate results** — Check assumptions, test on holdout data
3. **Visualize effectively** — Use ggplot2 to communicate findings clearly
4. **Share reproducibly** — Provide code, data, and documentation

## Finding and Selecting Packages

### CRAN (Comprehensive R Archive Network)

- Search by name or keywords at https://cran.r-project.org/
- Browse task views for curated package lists by domain
- Check package documentation and vignettes

### Evaluation Criteria

1. **Maintenance status** — Recently updated packages are more reliable
2. **Documentation quality** — Good vignettes and examples
3. **Community adoption** — Download statistics and GitHub stars
4. **Dependencies** — Fewer dependencies reduce conflicts
5. **Performance** — Benchmarks for computationally intensive tasks

### Installation

```r
# From CRAN
install.packages("package_name")

# From GitHub (development version)
devtools::install_github("username/repository")
```

## Common Analysis Scenarios

### Descriptive Statistics

- Use `dplyr::summarise()` with `mean()`, `median()`, `sd()`, `quantile()`
- Group by categories with `group_by()` before summarizing

### Hypothesis Testing

- t-tests: `t.test()`
- ANOVA: `aov()` or `anova()`
- Chi-square: `chisq.test()`
- Non-parametric tests: `wilcox.test()`, `kruskal.test()`

### Regression Analysis

- Simple linear: `lm(y ~ x, data = df)`
- Multiple regression: `lm(y ~ x1 + x2 + x3, data = df)`
- Logistic regression: `glm(y ~ x, family = binomial, data = df)`
- Panel data: `plm(y ~ x, data = df, model = "within")`

### Time Series Analysis

- Test stationarity: `tseries::adf.test()`
- Cointegration: `urca::ca.jo()`
- VAR models: `vars::VAR()`
- Forecasting: `forecast` package

### Machine Learning

- Framework setup: `mlr3` or `caret`
- Model training with cross-validation
- Hyperparameter tuning
- Model evaluation and comparison

## Project Organization

### Directory Structure

```
project/
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   ├── 01_import.R
│   ├── 02_clean.R
│   ├── 03_analyze.R
│   └── 04_visualize.R
├── output/
│   ├── figures/
│   └── tables/
├── reports/
│   └── analysis.Rmd
└── README.md
```

### Use ProjectTemplate

Automate project setup with the `ProjectTemplate` package:
- Standardized directory structure
- Automatic data loading
- Configuration management
- Built-in best practices

## Troubleshooting Common Issues

### Package Conflicts

- Use `package::function()` syntax to specify package explicitly
- Load packages in consistent order
- Use `conflicted` package to manage namespace conflicts

### Memory Management

- Use `data.table` for very large datasets
- Process data in chunks when possible
- Clear unused objects with `rm()` and `gc()`

### Performance Optimization

- Vectorize operations instead of loops
- Use `apply` family functions for iteration
- Profile code with `profvis` package
- Consider `Rcpp` for computationally intensive tasks

## Using the Reference Files

### When to Read Each Reference

**`/references/tidyverse-deep-dive.md`** — Read when working extensively with data manipulation, needing advanced dplyr/tidyr techniques, or building complex data pipelines.

**`/references/statistical-modeling-guide.md`** — Read when conducting regression analysis, panel data modeling, time series analysis, or need detailed guidance on model specification and diagnostics.

**`/references/visualization-techniques.md`** — Read when creating publication-quality graphics, building interactive visualizations, or customizing ggplot2 themes and aesthetics.

**`/references/machine-learning-workflows.md`** — Read when implementing machine learning models, performing cross-validation, tuning hyperparameters, or comparing multiple algorithms.

**`/references/reproducible-research.md`** — Read when setting up R Markdown reports, creating parameterized documents, or establishing reproducible analysis workflows.
