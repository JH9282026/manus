---
name: "business-intelligence-analytics"
description: "Develop BI strategy, design dashboards, implement data visualization, and establish analytics governance to transform data into actionable insights. Use for: BI platform selection (Tableau, Power BI, Looker), executive dashboard design, KPI framework development, self-service analytics enablement, data storytelling, semantic layer design, and analytics governance frameworks."
---

# Business Intelligence & Analytics

Transform organizational data into actionable insights through comprehensive BI strategy, dashboard development, and analytics governance.

## Overview

This skill enables end-to-end business intelligence capabilities from strategy through implementation. Use this to assess analytics maturity, design impactful visualizations, implement BI platforms, enable self-service analytics, and establish governance frameworks that democratize data access.

## BI Platform Selection Matrix

| Platform | Best For | Strengths | Considerations |
|----------|----------|-----------|----------------|
| Tableau | Visual exploration | Advanced visualizations, flexibility | License costs, learning curve |
| Power BI | Microsoft ecosystem | Office 365 integration, cost | Desktop-focused, governance |
| Looker | Embedded analytics | Semantic layer, governance | Technical setup, LookML |
| Qlik | Associative analysis | In-memory, discovery | Data modeling complexity |

## Dashboard Type Framework

| Type | Audience | Refresh | Focus |
|------|----------|---------|-------|
| Strategic | C-Suite | Weekly/Monthly | KPIs, trends, goals |
| Operational | Managers | Daily/Real-time | Performance, exceptions |
| Analytical | Analysts | On-demand | Deep-dive, exploration |
| Tactical | Teams | Real-time | Tasks, activities |

## Dashboard Design Principles

### Visual Hierarchy
1. Most important metrics at top-left
2. Support details flow top-to-bottom, left-to-right
3. Use size and color to indicate importance
4. Group related metrics together

### Chart Selection Guide

| Data Type | Best Charts |
|-----------|-------------|
| Comparison | Bar, column, bullet |
| Trend over time | Line, area, sparkline |
| Part-to-whole | Pie (limited), treemap, stacked bar |
| Distribution | Histogram, box plot |
| Relationship | Scatter, bubble |
| Geographic | Map, choropleth |

### Design Standards
- **Colors**: 5-7 maximum, colorblind-safe palettes
- **Typography**: 2 fonts maximum, hierarchy through size
- **Whitespace**: Minimum 10% for readability
- **Mobile**: Responsive design for all dashboards

## KPI Framework Development

### KPI Hierarchy
1. **Strategic KPIs**: Board/C-Suite level (5-10 metrics)
2. **Operational KPIs**: Department level (10-20 per area)
3. **Tactical Metrics**: Team level (as needed)

### KPI Definition Template

| Element | Description |
|---------|-------------|
| Name | Clear, unambiguous title |
| Definition | Precise calculation formula |
| Owner | Accountable individual |
| Source | Data source and system |
| Frequency | Refresh cadence |
| Target | Goal or benchmark |
| Threshold | Red/yellow/green ranges |

## Self-Service Analytics Maturity

| Level | Characteristics | Capabilities |
|-------|-----------------|--------------|
| 1 - Reports | Static reports | View predefined reports |
| 2 - Dashboards | Interactive dashboards | Filter, drill-down |
| 3 - Exploration | Ad-hoc analysis | Create visualizations |
| 4 - Advanced | Predictive insights | Build models, advanced analytics |

## Semantic Layer Design

### Purpose
- Single source of truth for business metrics
- Consistent definitions across organization
- Abstract complexity from end users
- Enable governed self-service

### Components
- **Dimensions**: Descriptive attributes (customer, product, time)
- **Measures**: Quantitative values (revenue, quantity)
- **Hierarchies**: Drill paths (year > quarter > month)
- **Relationships**: Table connections

## Data Storytelling Framework

### Structure
1. **Context**: Set the scene, explain why it matters
2. **Data**: Present key findings visually
3. **Insight**: Interpret what data means
4. **Action**: Recommend next steps

### Narrative Techniques
- Lead with the insight, not the data
- Use comparison (vs. target, vs. prior period)
- Highlight anomalies and exceptions
- Connect to business outcomes

## Analytics Governance Framework

| Area | Components |
|------|------------|
| Data Quality | Validation rules, quality scores, monitoring |
| Access Control | Role-based access, row-level security |
| Standards | Naming conventions, design guidelines |
| Change Management | Version control, approval workflows |
| Documentation | Data dictionaries, lineage |

## Using the Reference Files

### When to Read Each Reference

**`/references/platform-implementation.md`** — Read when evaluating BI platforms, planning implementations, or designing technical architecture.

**`/references/dashboard-design.md`** — Read when designing dashboards, creating visualization standards, or building executive reports.

**`/references/analytics-governance.md`** — Read when establishing data governance, defining access controls, or creating analytics policies.

## Reference Files

This skill includes the following detailed reference materials:

- [Analytics Governance](./references/analytics-governance.md)
- [Dashboard Design](./references/dashboard-design.md)
- [Platform Implementation](./references/platform-implementation.md)
