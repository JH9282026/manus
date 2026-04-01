---
name: tableau-visualization
description: "Create interactive data visualizations and dashboards using Tableau. Use for: dashboard design, data connection and preparation, chart creation, calculated fields, parameters and filters, interactive visualizations, storytelling with data, performance optimization, Tableau Server/Online publishing, data blending, LOD expressions, and visual analytics."
---

# Tableau Visualization

Create compelling, interactive data visualizations and dashboards for business intelligence and analytics.

## Overview

Tableau is a leading data visualization platform that transforms raw data into interactive, shareable dashboards. This skill covers connecting to data sources, creating visualizations, designing dashboards, and leveraging advanced features like calculated fields, parameters, and Level of Detail (LOD) expressions for sophisticated analytics.

## Getting Started

### Data Connection

**Supported Data Sources**:
- Files: Excel, CSV, JSON, PDF, Spatial files
- Databases: SQL Server, PostgreSQL, MySQL, Oracle, Teradata
- Cloud: Snowflake, Amazon Redshift, Google BigQuery, Azure SQL
- Applications: Salesforce, Google Analytics, SAP HANA
- Web Data Connectors: Custom APIs and web services

**Connection Types**:
- **Live Connection**: Query data directly from source in real-time
- **Extract**: Import data snapshot for faster performance and offline access
- **Hybrid**: Combine live and extract connections

### Data Preparation

**Data Interpreter**: Automatically detect and clean data structure
**Pivot**: Transform columns to rows or vice versa
**Split**: Separate values in a single column
**Union**: Combine tables with same structure
**Join**: Merge tables based on common fields (Inner, Left, Right, Full Outer, Cross)
**Blend**: Combine data from multiple sources in a single view

## Visualization Types

### Basic Charts

| Chart Type | Use Case | Best For |
|------------|----------|----------|
| Bar Chart | Compare categories | Categorical comparisons, rankings |
| Line Chart | Show trends over time | Time series, continuous data |
| Scatter Plot | Show correlation | Relationship between two measures |
| Pie Chart | Show proportions | Part-to-whole (use sparingly) |
| Map | Geographic data | Location-based analysis |
| Text Table | Detailed data | Precise values, small datasets |
| Heat Map | Show patterns | Density, intensity across dimensions |

### Advanced Visualizations

**Dual-Axis Charts**: Combine two measures with different scales
**Bullet Graphs**: Compare actual vs target performance
**Waterfall Charts**: Show cumulative effect of sequential values
**Gantt Charts**: Project timelines and schedules
**Box Plots**: Display distribution and outliers
**Treemaps**: Hierarchical data with nested rectangles
**Packed Bubbles**: Show relative sizes and groupings

## Calculated Fields

### Basic Calculations

```
// Simple arithmetic
Profit Margin = ([Profit] / [Sales]) * 100

// String manipulation
Full Name = [First Name] + " " + [Last Name]

// Date calculations
Days Since Order = DATEDIFF('day', [Order Date], TODAY())

// Conditional logic
Customer Segment = 
IF [Sales] > 10000 THEN "High Value"
ELSEIF [Sales] > 5000 THEN "Medium Value"
ELSE "Low Value"
END
```

### Aggregate Functions

```
// Sum, Average, Min, Max
Total Sales = SUM([Sales])
Average Order Value = AVG([Order Amount])
Highest Price = MAX([Price])

// Count
Customer Count = COUNTD([Customer ID])
Order Count = COUNT([Order ID])

// Conditional aggregation
High Value Sales = SUM(IF [Order Amount] > 1000 THEN [Sales] END)
```

### Table Calculations

```
// Running total
RUNNING_SUM(SUM([Sales]))

// Percent of total
SUM([Sales]) / TOTAL(SUM([Sales]))

// Year over year growth
(ZN(SUM([Sales])) - LOOKUP(ZN(SUM([Sales])), -12)) / ABS(LOOKUP(ZN(SUM([Sales])), -12))

// Moving average
WINDOW_AVG(SUM([Sales]), -6, 0)

// Rank
RANK(SUM([Sales]))
```

### Level of Detail (LOD) Expressions

```
// FIXED: Compute at specific level regardless of view
{FIXED [Customer ID] : SUM([Sales])}

// INCLUDE: Add dimensions to view level
{INCLUDE [Product Category] : AVG([Sales])}

// EXCLUDE: Remove dimensions from view level
{EXCLUDE [Region] : SUM([Sales])}

// Practical examples
Customer Lifetime Value = {FIXED [Customer ID] : SUM([Sales])}
Average Sales Per Customer = {FIXED [Customer ID] : SUM([Sales])} / COUNTD([Customer ID])
```

## Dashboard Design

### Layout Best Practices

**Visual Hierarchy**:
- Place most important information in top-left (F-pattern reading)
- Use size and color to emphasize key metrics
- Group related visualizations together
- Maintain consistent spacing and alignment

**Dashboard Objects**:
- **Horizontal/Vertical Containers**: Organize layout
- **Text**: Add titles, descriptions, instructions
- **Images**: Include logos, icons, branding
- **Web Page**: Embed external content
- **Blank**: Add spacing and separation
- **Navigation**: Create buttons for multi-dashboard navigation

### Interactivity

**Filters**:
- Dimension filters: Filter by categorical values
- Measure filters: Filter by numeric ranges
- Date filters: Relative, range, or specific dates
- Context filters: Apply before other filters for performance
- Cascading filters: Dependent filter selections

**Actions**:
- **Filter Actions**: Click to filter other sheets
- **Highlight Actions**: Hover or click to emphasize related data
- **URL Actions**: Open web pages with dynamic parameters
- **Go to Sheet**: Navigate between dashboards
- **Change Parameter**: Update parameter values via interaction

**Parameters**:
```
// Create dynamic calculations
IF [Parameter: Metric] = "Sales" THEN SUM([Sales])
ELSEIF [Parameter: Metric] = "Profit" THEN SUM([Profit])
ELSE SUM([Quantity])
END

// Dynamic date ranges
[Order Date] >= [Parameter: Start Date] AND [Order Date] <= [Parameter: End Date]

// Top N filtering
RANK(SUM([Sales])) <= [Parameter: Top N]
```

## Advanced Features

### Sets

**Dynamic Sets**: Automatically update based on conditions
**Fixed Sets**: Manually selected members
**Combined Sets**: Union, intersection, or difference of sets

```
// In/Out of set
IF [Customer ID] IN [Top Customers Set] THEN "Top Customer" ELSE "Other" END

// Set actions
Create sets dynamically through dashboard interactions
```

### Groups and Hierarchies

**Groups**: Combine dimension members into higher-level categories
**Hierarchies**: Create drill-down paths (e.g., Year > Quarter > Month > Day)

### Analytics Pane

**Constant Line**: Reference line at fixed value
**Average Line**: Show mean across view
**Median with Quartiles**: Display distribution
**Box Plot**: Show statistical distribution
**Totals**: Grand totals and subtotals
**Trend Line**: Linear, logarithmic, exponential, polynomial
**Forecast**: Predictive forecasting with confidence intervals
**Clusters**: Automatic grouping based on similarity

## Performance Optimization

### Data Optimization

- **Use Extracts**: Faster than live connections for large datasets
- **Aggregate Data**: Pre-aggregate at appropriate level
- **Filter Data**: Reduce data volume at source
- **Incremental Refresh**: Update only new/changed data
- **Optimize Joins**: Minimize number of joins, use appropriate join types

### Calculation Optimization

- **Avoid Row-Level Calculations**: Use aggregate calculations when possible
- **Use Boolean Over String**: `[Sales] > 1000` instead of `IF [Sales] > 1000 THEN "Yes" ELSE "No" END`
- **Minimize LOD Expressions**: Use only when necessary
- **Simplify Table Calculations**: Reduce complexity and scope

### Dashboard Optimization

- **Limit Number of Sheets**: 8-10 visualizations maximum per dashboard
- **Reduce Marks**: Filter to essential data points
- **Hide Unused Fields**: Improve metadata performance
- **Use Device Layouts**: Optimize for desktop, tablet, phone separately

## Publishing and Sharing

### Tableau Server/Online

**Publishing Workbooks**:
- Set permissions (View, Edit, Save)
- Configure data source credentials
- Schedule extract refreshes
- Enable web editing

**Subscriptions**: Email snapshots on schedule
**Alerts**: Notify when data meets conditions
**Metrics**: Track KPIs on mobile devices

### Embedding

**Embed Code**: Integrate dashboards in websites
**JavaScript API**: Programmatic control and interaction
**REST API**: Automate publishing and management

## Storytelling with Data

### Story Points

Create narrative flow through sequential dashboards:
1. Overview: High-level summary
2. Deep Dive: Detailed analysis
3. Insights: Key findings
4. Recommendations: Action items

### Annotations

- **Mark Annotations**: Highlight specific data points
- **Point Annotations**: Add notes at coordinates
- **Area Annotations**: Describe regions or time periods

## Best Practices

### Design Principles

- **Simplicity**: Remove unnecessary elements
- **Consistency**: Use uniform colors, fonts, sizes
- **Clarity**: Clear labels and titles
- **Accessibility**: Color-blind friendly palettes, sufficient contrast
- **Mobile-First**: Design for smallest screen first

### Color Usage

- **Categorical**: Distinct colors for different categories (max 7-10)
- **Sequential**: Gradients for ordered data (light to dark)
- **Diverging**: Two-color gradient for data with meaningful midpoint
- **Highlighting**: Use color sparingly to emphasize key insights

### Tooltips

Customize tooltips to provide context:
- Include relevant dimensions and measures
- Add calculated fields for additional insights
- Use Viz in Tooltip for detailed drill-downs
- Keep concise and scannable

## Using the Reference Files

### When to Read Each Reference

**`/references/advanced-calculations.md`** — Read when creating complex calculated fields, LOD expressions, or table calculations for sophisticated analysis.

**`/references/dashboard-examples.md`** — Read when designing dashboards for specific use cases like sales analytics, marketing dashboards, or operational reporting.

**`/references/performance-tuning.md`** — Read when optimizing slow dashboards, working with large datasets, or improving user experience.
