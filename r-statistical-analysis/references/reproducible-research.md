# Reproducible Research with R

Comprehensive guide to creating reproducible analyses using R Markdown, project organization, and version control.

---

## R Markdown Fundamentals

### Basic Document Structure

```markdown
---
title: "Analysis Report"
author: "Your Name"
date: "`r Sys.Date()`"
output: html_document
---

# Introduction

This is regular markdown text.

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE, warning = FALSE, message = FALSE)
library(tidyverse)
```

## Data Analysis

```{r load-data}
data <- read_csv("data.csv")
```

```{r summary}
summary(data)
```

## Visualization

```{r plot, fig.width=8, fig.height=6}
ggplot(data, aes(x = x, y = y)) +
  geom_point()
```

## Conclusion

The analysis shows...
```

### Output Formats

```yaml
# HTML document
output: html_document

# PDF document (requires LaTeX)
output: pdf_document

# Word document
output: word_document

# Presentation (HTML)
output: ioslides_presentation

# Presentation (PDF)
output: beamer_presentation

# Dashboard
output: flexdashboard::flex_dashboard

# Multiple formats
output:
  html_document:
    toc: true
    toc_float: true
  pdf_document:
    toc: true
```

### Chunk Options

```r
# Display code and output
```{r}
code here
```

# Hide code, show output
```{r echo=FALSE}
code here
```

# Show code, hide output
```{r results='hide'}
code here
```

# Hide code and output (but run it)
```{r include=FALSE}
code here
```

# Don't run code
```{r eval=FALSE}
code here
```

# Figure options
```{r fig.width=8, fig.height=6, fig.cap="Caption text"}
plot code
```

# Cache results
```{r cache=TRUE}
expensive computation
```
```

### Inline Code

```markdown
The mean value is `r mean(data$value)`.

We analyzed `r nrow(data)` observations.

The correlation is `r round(cor(data$x, data$y), 3)`.
```

---

## Advanced R Markdown

### Parameterized Reports

```yaml
---
title: "Parameterized Report"
output: html_document
params:
  region: "North"
  year: 2024
  threshold: 100
---
```

```{r}
# Access parameters
data_filtered <- data %>%
  filter(
    region == params$region,
    year == params$year,
    value > params$threshold
  )
```

Render with different parameters:

```r
rmarkdown::render(
  "report.Rmd",
  params = list(region = "South", year = 2023, threshold = 150),
  output_file = "report_south_2023.html"
)
```

### Child Documents

```markdown
# Main Report

```{r child="section1.Rmd"}
```

```{r child="section2.Rmd"}
```
```

### Custom Templates

```r
# Create package with custom template
usethis::use_rmarkdown_template("my_template")

# Use template
rmarkdown::draft("new_report.Rmd", template = "my_template", package = "mypackage")
```

---

## Project Organization

### Recommended Structure

```
project/
├── README.md
├── project.Rproj
├── .gitignore
├── data/
│   ├── raw/
│   │   └── original_data.csv
│   └── processed/
│       └── cleaned_data.rds
├── scripts/
│   ├── 01_import.R
│   ├── 02_clean.R
│   ├── 03_analyze.R
│   └── 04_visualize.R
├── R/
│   ├── functions.R
│   └── utils.R
├── output/
│   ├── figures/
│   │   ├── plot1.png
│   │   └── plot2.png
│   └── tables/
│       └── summary_table.csv
├── reports/
│   ├── analysis.Rmd
│   └── analysis.html
└── docs/
    └── methodology.md
```

### Using here Package

```r
library(here)

# Automatically finds project root
data <- read_csv(here("data", "raw", "original_data.csv"))

# Works regardless of working directory
source(here("R", "functions.R"))

# Save output
ggsave(here("output", "figures", "plot1.png"))
```

### ProjectTemplate

```r
library(ProjectTemplate)

# Create new project
create.project("my_project")

# Load project (loads data, libraries, functions)
load.project()

# Project structure is automatically created
# Data in data/ is automatically loaded
# Functions in lib/ are automatically sourced
# Configuration in config/global.dcf
```

---

## Version Control with Git

### Initial Setup

```bash
# Initialize repository
git init

# Configure user
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Create .gitignore
echo ".Rproj.user
.Rhistory
.RData
.Ruserdata
data/raw/
*.html" > .gitignore

# First commit
git add .
git commit -m "Initial commit"
```

### Basic Workflow

```bash
# Check status
git status

# Stage changes
git add script.R
git add .

# Commit changes
git commit -m "Add data cleaning script"

# View history
git log
git log --oneline

# View changes
git diff
git diff script.R
```

### Branching

```bash
# Create and switch to new branch
git checkout -b feature-analysis

# Switch branches
git checkout main

# Merge branch
git checkout main
git merge feature-analysis

# Delete branch
git branch -d feature-analysis
```

### Remote Repositories

```bash
# Add remote
git remote add origin https://github.com/username/repo.git

# Push to remote
git push -u origin main

# Pull from remote
git pull origin main

# Clone repository
git clone https://github.com/username/repo.git
```

---

## Dependency Management

### Using renv

```r
# Initialize renv for project
renv::init()

# Install packages (tracked by renv)
install.packages("dplyr")

# Save current state
renv::snapshot()

# Restore packages from lockfile
renv::restore()

# Update packages
renv::update()

# Check status
renv::status()
```

### Session Info

```r
# Include at end of reports
sessionInfo()

# Or more detailed
devtools::session_info()
```

---

## Documentation

### Function Documentation with roxygen2

```r
#' Calculate Summary Statistics
#'
#' This function calculates mean, median, and standard deviation
#' for a numeric vector.
#'
#' @param x A numeric vector
#' @param na.rm Logical. Should missing values be removed? Default is TRUE.
#' @return A named vector with summary statistics
#' @examples
#' calc_summary(c(1, 2, 3, 4, 5))
#' calc_summary(c(1, 2, NA, 4, 5), na.rm = TRUE)
#' @export
calc_summary <- function(x, na.rm = TRUE) {
  c(
    mean = mean(x, na.rm = na.rm),
    median = median(x, na.rm = na.rm),
    sd = sd(x, na.rm = na.rm)
  )
}
```

### README Template

```markdown
# Project Title

## Overview
Brief description of the project and its goals.

## Data
Description of data sources and structure.

## Requirements
- R version 4.0+
- Required packages: dplyr, ggplot2, etc.

## Installation
```r
# Install required packages
install.packages(c("dplyr", "ggplot2"))

# Or use renv
renv::restore()
```

## Usage
```r
# Load project
source("scripts/01_import.R")
source("scripts/02_clean.R")
source("scripts/03_analyze.R")

# Or render report
rmarkdown::render("reports/analysis.Rmd")
```

## Project Structure
Description of directory organization.

## Results
Summary of key findings.

## License
MIT License

## Contact
Your contact information.
```

---

## Best Practices

### Code Style

```r
# Use consistent naming (snake_case recommended)
my_variable <- 10
my_function <- function(x) { x + 1 }

# Use <- for assignment, not =
x <- 5

# Space after commas, around operators
data[1, 2]
x <- y + z

# Indent with 2 spaces
if (condition) {
  do_something()
}

# Use styler package to format code
styler::style_file("script.R")
styler::style_dir("R/")

# Use lintr to check code
lintr::lint("script.R")
```

### Reproducibility Checklist

1. **Set seed for random operations**
   ```r
   set.seed(123)
   ```

2. **Use relative paths, not absolute**
   ```r
   # Good
   read_csv(here("data", "file.csv"))
   
   # Bad
   read_csv("/Users/yourname/project/data/file.csv")
   ```

3. **Document package versions**
   ```r
   sessionInfo()
   ```

4. **Use renv for dependency management**

5. **Include README with setup instructions**

6. **Use version control (Git)**

7. **Write clear comments**

8. **Separate data, code, and output**

9. **Use R Markdown for reports**

10. **Test code on fresh R session**