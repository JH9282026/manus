---
name: "data-visualization-dashboard-creation"
description: "Design and build interactive dashboards and data visualizations that transform complex data into clear, actionable insights. Use for: creating executive KPI dashboards, sales performance dashboards, customer analytics views, operational monitoring displays, financial reporting dashboards, choosing chart types, designing visual encodings, optimizing dashboard performance, and implementing data storytelling."
---

# Data Visualization & Dashboard Creation

Design and build interactive dashboards and data visualizations that transform complex data into actionable insights for stakeholders at all levels.

## Overview

Provide frameworks for the full dashboard lifecycle: requirements gathering, chart type selection, visual encoding, layout design, interactivity specification, performance optimization, and governance. Cover tools like Tableau, Power BI, Looker, and code-based options (D3.js, Plotly, Dash).

## Chart Type Selection Guide

| Data Relationship | Recommended Charts | When to Use |
|---|---|---|
| Trend over time | Line, area, sparkline | Track KPIs, seasonal patterns, growth |
| Comparison | Bar, bullet, lollipop | Compare categories, rank items |
| Distribution | Histogram, box plot, violin | Understand data spread, outliers |
| Composition | Stacked bar, treemap, donut | Part-to-whole relationships |
| Correlation | Scatter, bubble, heat map | Find relationships between variables |
| Geographic | Choropleth, point map, flow map | Location-based analysis |
| KPI summary | Card, gauge, traffic light | Executive-level status monitoring |

## Dashboard Design Principles

### Visual Encoding Hierarchy

Apply encodings in order of perceptual accuracy:
1. Position along common scale (most accurate)
2. Length
3. Angle/slope
4. Area
5. Volume
6. Color saturation/hue (least accurate)

### Layout Best Practices

- Place highest-priority KPIs in the top-left quadrant
- Use Z-pattern or F-pattern reading flow
- Limit to 5-9 visual elements per view
- Maintain consistent alignment and spacing
- Group related metrics with visual containers
- Design for the target device (desktop, tablet, mobile)

### Interactivity Patterns

| Pattern | Purpose | Implementation |
|---|---|---|
| Filter/slicer | Narrow data scope | Date range, dropdown, checkbox |
| Drill-down | Explore detail levels | Click hierarchy navigation |
| Drill-through | Cross-page navigation | Link from summary to detail |
| Hover tooltip | Show additional context | On-demand detail display |
| Brushing | Cross-highlight related data | Linked selections across charts |
| Parameter controls | What-if analysis | Slider, input controls |

## Dashboard Types

| Type | Audience | Refresh | Complexity |
|---|---|---|---|
| Strategic/Executive | C-suite | Weekly/monthly | Low (5-8 KPIs) |
| Operational | Managers | Real-time/daily | Medium (monitoring) |
| Analytical | Analysts | On-demand | High (exploratory) |
| Embedded | End users | Varies | Medium (contextual) |

## Performance Optimization

- Target sub-5-second load times for primary views
- Use extracts/materialized views over live queries for large datasets
- Implement incremental refresh strategies
- Minimize calculated fields in real-time queries
- Use aggregated tables for summary views
- Cache frequently accessed data

## Platform Comparison

| Platform | Strengths | Best For |
|---|---|---|
| Tableau | Visual analytics, flexibility | Analytical exploration |
| Power BI | Microsoft ecosystem, cost | Enterprise reporting |
| Looker | Data modeling, governance | Data-driven orgs |
| Metabase | Open source, simplicity | Small teams, startups |
| D3.js | Full customization | Custom web visualizations |
| Plotly/Dash | Python integration | Data science teams |
| Streamlit | Rapid prototyping | ML model dashboards |

## Using the Reference Files

### When to Read Each Reference

**`/references/dashboard-design-process.md`** — Read when planning a new dashboard from scratch, gathering requirements, or creating wireframes and layout designs.

**`/references/chart-types-and-encoding.md`** — Read when selecting specific chart types, configuring visual encodings, or designing individual visualizations for specific data relationships.

**`/references/platform-implementation.md`** — Read when implementing dashboards on specific platforms (Tableau, Power BI, Looker, D3.js) or optimizing performance and deployment.
