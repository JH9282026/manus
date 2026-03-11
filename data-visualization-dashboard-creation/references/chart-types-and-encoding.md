# Chart Types and Visual Encoding

## Trend Visualizations

### Line Charts
- Use for continuous data over time
- Limit to 5-7 lines before visual clutter occurs
- Apply meaningful color coding with legend
- Consider dual-axis only when absolutely necessary (misleading risk)

### Area Charts
- Use for volume/magnitude emphasis over time
- Stacked areas for composition trends
- Ensure transparency when overlapping
- Avoid when precise comparison matters (use line instead)

### Sparklines
- Miniature trend lines embedded in tables or cards
- Show trend direction and shape without axis detail
- Ideal for KPI cards and summary views
- Include start/end value labels for context

---

## Comparison Visualizations

### Bar Charts
- Horizontal bars for category names that are long
- Vertical bars for time-based comparisons
- Sort by value (not alphabetically) unless order is meaningful
- Include data labels for precise reading

### Bullet Charts
- Compare actual to target with qualitative ranges
- Superior to gauges for single-metric comparison
- Use background bands for poor/satisfactory/good ranges
- Compact design enables multiple metrics in small space

### Lollipop Charts
- Cleaner alternative to bar charts for many categories
- Reduce visual weight while maintaining precision
- Combine dot precision with line connection to axis

---

## Distribution Visualizations

### Histograms
- Show frequency distribution of continuous data
- Choose bin width carefully (too many or few bins mislead)
- Add density curve overlay for shape clarity
- Use for understanding data spread and skewness

### Box Plots
- Show median, quartiles, and outliers
- Excellent for comparing distributions across categories
- Include jittered points for small datasets
- Explain to non-technical audiences (annotations help)

### Violin Plots
- Combine box plot statistics with density visualization
- Show distribution shape more intuitively than box plots
- Use when comparing multiple group distributions

---

## Composition Visualizations

### Treemaps
- Show hierarchical part-to-whole relationships
- Size encodes magnitude, color encodes category or metric
- Best for showing relative sizes across many categories
- Avoid for precise comparison (use stacked bar instead)

### Stacked Bar Charts
- Show composition across categories or time
- 100% stacked for proportion comparison
- Standard stacked for absolute values
- Limit to 5-7 segments for readability

### Pie/Donut Charts
- Use sparingly; humans poorly judge angles
- Limit to 3-5 slices maximum
- Always include data labels
- Donut preferred (center space for total/KPI)

---

## Relationship Visualizations

### Scatter Plots
- Show correlation between two continuous variables
- Add trend line for relationship direction
- Use size encoding for third variable (bubble chart)
- Color for categorical grouping

### Heat Maps
- Show patterns in matrix data (time × category)
- Use sequential or diverging color scales
- Include value labels in cells when count is manageable
- Ideal for calendar views, correlation matrices

---

## Geographic Visualizations

### Choropleth Maps
- Color-encode regions by metric value
- Normalize by population/area to avoid misleading
- Use sequential color scale for continuous data
- Include legend with clear break points

### Point Maps
- Plot individual locations with size/color encoding
- Use clustering for dense point patterns
- Consider hex bins for large datasets
- Add tooltip for location detail on hover

---

## Visual Encoding Best Practices

### Encoding Selection by Data Type

| Data Type | Primary Encoding | Secondary Encoding |
|---|---|---|
| Quantitative | Position, length | Size, color intensity |
| Ordinal | Position, length | Color intensity |
| Nominal | Color hue, shape | Position (grouped) |
| Temporal | Position (x-axis) | Animation |
| Geographic | Position (map) | Color, size |

### Color Usage Rules

1. Use sequential palettes for ordered data (light to dark)
2. Use diverging palettes for data with meaningful center (red-white-blue)
3. Use categorical palettes for unordered groups (max 7 distinct)
4. Reserve red/green for semantic meaning (bad/good)
5. Test all palettes for color blindness accessibility
