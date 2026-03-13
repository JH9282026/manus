---
name: "demographic-research"
description: "Conduct comprehensive population studies and demographic analysis to understand population characteristics, trends, migration patterns, and generational cohorts. Use for: market sizing by demographics, retail expansion planning, healthcare capacity forecasting, workforce development analysis, housing demand modeling, generational cohort analysis, census data interpretation, and demographic projection scenarios."
---

# Demographic Research

Investigate, analyze, and interpret population-related data to inform strategic decision-making across business, policy, and planning contexts.

## Overview

Transform raw demographic data into actionable insights covering age, gender, ethnicity, education, income, household composition, and geographic distribution. Encompasses descriptive analysis (current profiles) and predictive modeling (future projections).

## Core Data Sources

| Source | Coverage | Frequency | Best For |
|---|---|---|---|
| U.S. Census (Decennial) | Full population | Every 10 years | Baseline counts |
| American Community Survey (ACS) | 1% sample | Annual (1-yr, 5-yr) | Detailed characteristics |
| Current Population Survey (CPS) | 60K households | Monthly | Labor force, income |
| Esri/Claritas | Proprietary | Annual updates | Consumer segmentation |
| UN Population Division | Global | Biennial | International comparison |
| World Bank | Global | Annual | Development indicators |
| Eurostat | EU member states | Annual | European demographics |

## Generational Cohort Definitions

| Generation | Birth Years | Current Age (2026) | Key Characteristics |
|---|---|---|---|
| Gen Alpha | 2013–present | 0–13 | Digital natives from birth |
| Gen Z | 1997–2012 | 14–29 | Mobile-first, diversity-focused |
| Millennials | 1981–1996 | 30–45 | Tech-savvy, experience-driven |
| Gen X | 1965–1980 | 46–61 | Independent, pragmatic |
| Baby Boomers | 1946–1964 | 62–80 | Wealth holders, aging care needs |
| Silent Gen | 1928–1945 | 81–98 | Legacy planning, healthcare |

## Key Demographic Metrics

- **Total Fertility Rate (TFR)**: Average children per woman
- **Dependency Ratio**: Non-working-age / working-age population
- **Net Migration Rate**: Immigrants minus emigrants per 1,000
- **Median Age**: Population midpoint indicator of aging
- **Diversity Index**: Probability two random people differ in race/ethnicity
- **Headship Rate**: Proportion of age group heading households

## Analysis Framework

### Step 1: Define Geographic Scope and Variables
Specify regions (MSA, county, ZIP), time periods, and demographic variables.

### Step 2: Collect and Validate Data
Pull from census APIs, proprietary databases, and statistical agencies. Check margins of error for small-area estimates.

### Step 3: Build Demographic Profile
Create population pyramids, income distributions, educational attainment tables, and household composition breakdowns.

### Step 4: Analyze Trends
Calculate compound annual growth rates, identify inflection points, and compare against benchmarks.

### Step 5: Develop Projections
Apply cohort-component method (fertility + mortality + migration) to forecast population by age/sex groups.

### Step 6: Synthesize Insights
Translate demographics into strategic implications for the specific use case.

## Common Use Cases

| Use Case | Key Metrics | Projection Horizon |
|---|---|---|
| Retail site selection | Population density, income, age | 5–10 years |
| Healthcare planning | Age distribution, chronic disease rates | 10–20 years |
| Workforce development | Working-age pop, education levels | 5–15 years |
| Housing demand | Household formation, headship rates | 10–20 years |
| Product portfolio | Generational cohort sizes, spending power | 5–10 years |

## Using the Reference Files

### When to Read Each Reference

**`/references/census-data-methods.md`** — Read when working with U.S. Census data, understanding survey methodology, margins of error, or geographic hierarchies.

**`/references/projection-techniques.md`** — Read when building demographic forecasts, selecting projection methodologies, or documenting assumption scenarios.

**`/references/generational-analysis.md`** — Read when conducting generational cohort analysis, understanding generational attitudes, or sizing generational market segments.

## Reference Files

This skill includes the following detailed reference materials:

- [Census Data Methods](references/census-data-methods.md)
- [Generational Analysis](references/generational-analysis.md)
- [Projection Techniques](references/projection-techniques.md)
