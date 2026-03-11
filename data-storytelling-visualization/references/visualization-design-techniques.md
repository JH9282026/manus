# Visualization Design Techniques

## Chart Design Best Practices

### Bar Charts
- Use horizontal bars when category labels are long
- Sort bars by value (not alphabetically) unless there is a natural order
- Start y-axis at zero to avoid misleading proportions
- Add data labels for precise values when few bars
- Limit to 12-15 categories; group smaller ones as "Other"

### Line Charts
- Use for continuous data over time (not categorical comparisons)
- Limit to 5-7 lines before using small multiples
- Label lines directly instead of using a legend
- Use consistent time intervals on x-axis
- Highlight key inflection points with annotations

### Scatter Plots
- Add trend lines to show relationships
- Use size encoding for third variable (bubble chart)
- Use color encoding for categories
- Label notable outliers
- Include correlation coefficient when appropriate

### Heatmaps
- Use sequential color scale for one-direction data
- Use diverging scale for data with meaningful center (e.g., correlation)
- Sort rows/columns by similarity for pattern visibility
- Add value labels when cells are large enough
- Provide a clear color legend

---

## Color Theory for Data

### Color Palette Types

| Palette Type | Use Case | Example |
|-------------|----------|---------|
| Sequential | Ordered data (low to high) | Light blue → dark blue |
| Diverging | Data with midpoint | Red ← white → blue |
| Categorical | Nominal groups | Distinct hues |
| Highlight | Emphasis on one category | Gray + one accent color |

### Colorblind-Safe Design
- Avoid red-green combinations (8% of males affected)
- Use viridis, cividis, or ColorBrewer palettes
- Add texture, patterns, or labels as secondary encoding
- Test with colorblindness simulators (Coblis, Color Oracle)
- Ensure sufficient contrast (WCAG AA: 4.5:1 for text)

### Color Meaning Conventions
- Red/Green for financial (loss/gain) — add symbols for accessibility
- Blue for water/cold, red for heat/urgency
- Gray for context/background data
- Brand colors for organizational consistency
- Limit to 5-7 distinct colors per visualization

---

## Dashboard Design

### Layout Principles

**Inverted pyramid structure**:
1. Top: Key metrics and KPI cards (biggest, most important)
2. Middle: Trend charts and comparisons
3. Bottom: Detailed tables and breakdowns

**Grid system**:
- Use 12-column grid for flexible layouts
- KPI cards: 2-4 across the top
- Charts: 2 per row for readability
- Tables: Full width at the bottom
- White space between sections for visual breathing room

### Interactive Elements

| Element | Purpose | Best Practice |
|---------|---------|---------------|
| Filters | Narrow scope | Top of dashboard, persistent |
| Drill-down | Explore detail | Click on chart element |
| Tooltips | Show precise values | Hover on data point |
| Date range picker | Time navigation | Consistent across all charts |
| Search | Find specific items | Large datasets, tables |
| Export | Share/save | PDF, PNG, CSV options |

### Dashboard Anti-Patterns
- Too many charts (>8 per view)
- Inconsistent time periods across charts
- Missing context (no benchmarks or targets)
- Pie charts for comparison (use bars instead)
- Scrolling required to see key metrics
- No mobile-responsive design

---

## Small Multiples (Trellis Charts)

Use small multiples when:
- Comparing the same metric across 6+ categories
- Line charts would be too cluttered with multiple lines
- You want to show patterns within each category

Design rules:
- Use identical axes across all panels
- Arrange in meaningful order (alphabetical, by value, by geography)
- Label each panel clearly
- Keep individual panels simple
- Use consistent colors across all panels

---

## Annotation and Labeling

### When to Annotate
- Key inflection points (trend changes)
- Notable outliers
- Target/benchmark lines
- Time-specific events that explain data changes
- Maximum/minimum values

### Annotation Style
- Brief text (5-10 words maximum)
- Arrow or line connecting annotation to data point
- Subtle color (not competing with data)
- Consistent position relative to data points
- Remove annotations when they clutter
