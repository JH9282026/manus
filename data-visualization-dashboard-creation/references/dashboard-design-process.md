# Dashboard Design Process

## Requirements Gathering

### Stakeholder Interview Framework

Conduct structured interviews to define dashboard purpose:

1. **Who** — Identify primary users, their roles, and analytical sophistication
2. **What** — Define key questions the dashboard must answer
3. **When** — Determine refresh frequency and time-sensitivity
4. **Where** — Specify devices, screen sizes, and viewing contexts
5. **Why** — Clarify decisions that will be informed by the dashboard
6. **How** — Understand current reporting processes being replaced

### Metric Definition Template

For each KPI, document:
- **Metric name**: Clear, unambiguous label
- **Business definition**: Plain-language explanation
- **Calculation formula**: Exact mathematical formula
- **Data source**: Table, field, and transformation logic
- **Dimensions**: How the metric breaks down (by region, product, time)
- **Benchmarks**: Targets, thresholds, and comparison points
- **Owner**: Who is accountable for this metric

### Audience Profiles

| Profile | Needs | Design Implications |
|---|---|---|
| Executive | High-level status, exceptions | Traffic lights, sparklines, minimal detail |
| Manager | Team performance, trends | Comparison charts, drill-down capability |
| Analyst | Deep exploration, raw data | Filters, cross-tabs, export options |
| External | Curated narrative | Guided flow, limited interactivity |

---

## Information Architecture

### Dashboard Navigation Patterns

**Hub-and-spoke**: Overview page with drill-through to detail pages
- Best for: Executive dashboards with multiple KPI areas
- Structure: 1 overview + N detail pages

**Tabbed**: Equal-weight sections accessible via tabs
- Best for: Functional dashboards (sales, marketing, ops tabs)
- Structure: 3-7 parallel tab views

**Guided narrative**: Sequential pages telling a data story
- Best for: Presentations, reports, onboarding
- Structure: Linear flow with next/previous navigation

**Single-page**: All content on one scrollable page
- Best for: Operational monitoring, simple KPI tracking
- Structure: Sectioned single page with anchor links

### Wireframing Best Practices

1. Start with paper sketches to explore layout options
2. Use low-fidelity wireframes (gray boxes) before visual design
3. Map data elements to specific screen positions
4. Define filter placement and interaction flow
5. Get stakeholder approval on wireframes before building
6. Document responsive behavior for each breakpoint

---

## Dashboard Layout Patterns

### Executive Summary Layout

```
┌─────────────────────────────────────────┐
│  KPI Card  │  KPI Card  │  KPI Card     │
├────────────┴────────────┴───────────────┤
│  Primary Trend Chart (full width)       │
├─────────────────┬───────────────────────┤
│  Comparison     │  Composition          │
│  Chart          │  Chart                │
├─────────────────┴───────────────────────┤
│  Detail Table with sparklines           │
└─────────────────────────────────────────┘
```

### Operational Dashboard Layout

```
┌─────────────────────────────────────────┐
│  Filters / Date Range / Controls        │
├──────────┬──────────────────────────────┤
│  Sidebar │  Main visualization area     │
│  KPIs    │                              │
│  and     │  (Large chart or map)        │
│  alerts  │                              │
│          ├──────────────────────────────┤
│          │  Supporting detail charts    │
└──────────┴──────────────────────────────┘
```

---

## Color Strategy

### Dashboard Color Palette Structure

- **Primary brand color**: Main accent for key elements
- **Sequential palette**: Light-to-dark for continuous data
- **Diverging palette**: Two-hue scale for above/below threshold
- **Categorical palette**: Distinct hues for nominal categories (limit to 7)
- **Semantic colors**: Green=good, amber=warning, red=critical
- **Neutral grays**: Backgrounds, gridlines, secondary text

### Accessibility Requirements

- Maintain 4.5:1 contrast ratio for text (WCAG AA)
- Ensure charts are readable without color (use patterns, labels)
- Test with color blindness simulators (deuteranopia, protanopia)
- Provide text alternatives for all visual encodings

---

## Governance and Maintenance

### Dashboard Lifecycle Management

1. **Development**: Build, test, and validate with stakeholders
2. **Deployment**: Publish with access controls and documentation
3. **Monitoring**: Track usage, performance, and data freshness
4. **Optimization**: Iterate based on user feedback and analytics
5. **Retirement**: Archive or decommission when no longer needed

### Change Management Process

- Version control all dashboard definitions
- Document changes in a changelog
- Test changes in staging before production
- Notify users of significant changes
- Maintain rollback capability for critical dashboards
