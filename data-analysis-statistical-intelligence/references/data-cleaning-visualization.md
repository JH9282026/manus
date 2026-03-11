# Data Cleaning & Visualization

## Data Cleaning Workflow

### Step 1: Initial Assessment

```
1. Check shape (rows, columns)
2. Review data types (dtypes)
3. Calculate missing value percentages
4. Identify duplicate records
5. Review summary statistics
6. Check value distributions
```

### Step 2: Missing Data Handling

| Strategy | When to Use | Method |
|----------|-------------|--------|
| Drop rows | <5% missing, MCAR | df.dropna() |
| Drop columns | >50% missing | df.drop(columns=[...]) |
| Mean/Median imputation | Numeric, MCAR/MAR | SimpleImputer |
| Mode imputation | Categorical | SimpleImputer(strategy='most_frequent') |
| KNN imputation | Complex patterns | KNNImputer |
| Multiple imputation | Research/statistical rigor | IterativeImputer |
| Forward/backward fill | Time series | df.fillna(method='ffill') |
| Indicator variable | Missingness is informative | Add is_missing column |

### Step 3: Outlier Detection and Treatment

| Method | Definition | Best For |
|--------|-----------|----------|
| Z-score | \|z\| > 3 | Normal distributions |
| IQR | < Q1 - 1.5×IQR or > Q3 + 1.5×IQR | General purpose |
| Isolation Forest | Anomaly score | High-dimensional data |
| DBSCAN | Noise points | Spatial/cluster data |

**Treatment Options**:
- Remove: Only if clearly erroneous
- Cap/Winsorize: Replace with percentile values (1st/99th)
- Transform: Log, sqrt, Box-Cox to reduce impact
- Keep: If outliers represent real phenomenon

### Step 4: Data Type Corrections

- Convert string dates to datetime
- Cast numeric strings to float/int
- Standardize categorical values (case, spelling, whitespace)
- Create appropriate categorical dtypes for memory efficiency

---

## Visualization Best Practices

### Chart Selection Guide

| Data Relationship | Chart Type | When to Use |
|------------------|------------|-------------|
| Distribution (1 var) | Histogram, KDE | Continuous variable shape |
| Distribution (1 var) | Bar chart | Categorical frequency |
| Comparison | Grouped bar, dot plot | Compare categories |
| Relationship | Scatter plot | Two continuous variables |
| Relationship | Heatmap | Correlation matrix |
| Composition | Stacked bar, pie (sparingly) | Parts of a whole |
| Trend | Line chart | Time series |
| Ranking | Horizontal bar | Ordered categories |
| Distribution + Comparison | Box plot, violin | Distribution across groups |

### Color Guidelines

- Use colorblind-safe palettes (viridis, cividis, ColorBrewer)
- Sequential palette for ordered data (light to dark)
- Diverging palette for data with meaningful center point
- Categorical palette for nominal groups (max 8-10 colors)
- Highlight key data points with accent color

### Dashboard Design Principles

1. **Start with the key metric** — Most important number prominently displayed
2. **Progressive detail** — Summary → trends → breakdown → detail
3. **Limit to 5-7 visualizations** — Avoid dashboard overload
4. **Consistent formatting** — Same colors, fonts, scales across charts
5. **Add context** — Benchmarks, targets, previous period comparisons
6. **Enable interaction** — Filters, drill-downs, tooltips for exploration
7. **Mobile-friendly** — Design for the smallest expected screen

### Storytelling with Data

1. **Set the context** — Why are we looking at this data?
2. **Present the finding** — What does the data show?
3. **Provide evidence** — Supporting visualizations and statistics
4. **Explain implications** — What does this mean for the business?
5. **Recommend action** — What should we do next?
