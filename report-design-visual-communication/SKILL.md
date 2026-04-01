---
name: report-design-visual-communication
description: "Design professional business reports with effective visual communication and data presentation. Use for: report layout design, data table formatting, executive summary creation, chart design, visual hierarchy in documents, report typography, branded report templates, and annual/quarterly report design."
---

# Report Design & Visual Communication

Design professional, visually compelling business reports that communicate data and insights clearly through layout, typography, charts, and visual hierarchy.

## Overview

A well-designed report transforms raw data into clear, actionable communication. Poor report design — walls of text, inconsistent formatting, unlabeled charts — buries insights and erodes credibility. This skill covers layout principles, typography systems, chart selection and design, table formatting, color strategy, and template creation for recurring reports. Every design choice should serve comprehension and decision-making.

## Report Type Design Guide

| Report Type | Page Count | Visual Density | Chart:Text Ratio | Layout Focus | Reference |
|------------|------------|---------------|------------------|-------------|-----------|
| Executive summary | 1–2 pages | High (dense insights) | 60:40 | KPI cards, sparklines, bullet points | `/references/layout-principles.md` |
| Monthly business review | 5–10 pages | Medium–High | 50:50 | Section headers, consistent charts | `/references/data-visualization.md` |
| Annual report | 20–50 pages | Medium | 40:60 | Branded, narrative + data | `/references/layout-principles.md` |
| Technical analysis | 10–30 pages | Low–Medium | 30:70 | Detailed tables, footnotes | `/references/templates-examples.md` |
| Client deliverable | 5–15 pages | Medium | 50:50 | Branded cover, clean layout | `/references/templates-examples.md` |
| Board presentation (PDF) | 10–20 slides | High | 70:30 | One insight per page, large type | `/references/layout-principles.md` |

## Layout Design Principles

### Grid Systems for Reports

| Grid Type | Columns | Margin | Best For |
|-----------|---------|--------|----------|
| Single column | 1 | 1" all sides | Narrative-heavy, letters, memos |
| Two-column | 2 + gutter | 0.75" | Data + commentary side by side |
| Modular grid | 4–6 columns | 0.5–0.75" | Complex dashboards, annual reports |
| Asymmetric | 1/3 + 2/3 | Variable | Sidebar metrics + main content |

### Visual Hierarchy Rules

| Level | Purpose | Formatting | Example |
|-------|---------|-----------|---------|
| 1 (Primary) | Page/section title | 24–32pt, bold, brand color | "Q4 2026 Financial Review" |
| 2 (Secondary) | Subsection header | 16–20pt, semi-bold | "Revenue by Region" |
| 3 (Tertiary) | Chart title / table header | 12–14pt, bold | "Monthly Revenue Trend" |
| 4 (Body) | Main text content | 10–12pt, regular | Paragraph text |
| 5 (Caption) | Notes, sources, footnotes | 8–10pt, light/italic | "Source: Internal CRM data, Dec 2026" |

### Page Anatomy
- **Header:** Report title or section name, page number, date
- **Body:** Content area following grid system
- **Sidebar (optional):** KPI callouts, quick stats, navigation
- **Footer:** Confidentiality notice, version, data source
- **White space:** Minimum 25% of page should be empty — crowded pages lose readers

## Typography for Reports

### Font Pairing Strategy

| Combination | Heading Font | Body Font | Tone |
|------------|-------------|-----------|------|
| Corporate/professional | Helvetica Neue / Arial | Georgia / Garamond | Traditional authority |
| Modern/clean | Inter / DM Sans | Inter / Source Sans Pro | Contemporary clarity |
| Technical | IBM Plex Sans | IBM Plex Mono (for data) | Technical precision |
| Premium/editorial | Playfair Display | Lora / Source Serif | Sophisticated narrative |

### Typography Rules
- **Line height:** 1.4–1.6× for body text, 1.1–1.2× for headings
- **Line length:** 50–75 characters per line for optimal readability
- **Paragraph spacing:** Use space-after (6–12pt), not double line breaks
- **Alignment:** Left-aligned body text (never centered for paragraphs, never justified on screen)
- **Number formatting:** Use tabular/monospace figures in tables so columns align

## Chart Selection Guide

| Data Relationship | Chart Type | Maximum Categories | When to Avoid |
|------------------|------------|-------------------|---------------|
| Trend over time | Line chart | 5 lines max | Fewer than 4 data points |
| Category comparison | Horizontal bar | 15 bars max | Time-series data |
| Part of whole | Donut/pie | 5 segments max | More than 6 categories |
| Correlation | Scatter plot | 3 series max | No relationship exists |
| Distribution | Histogram/box plot | — | Categorical data |
| Ranking | Horizontal bar (sorted) | 20 max | No meaningful order |
| KPI/metric | Big number + sparkline | 1 per card | When trend matters more than current value |
| Geographic | Choropleth map | — | Non-geographic data |

### Chart Design Rules
- **Always title your charts** — readers scan visually and need context
- **Label axes** — including units (e.g., "Revenue ($M)" not just "Revenue")
- **Start bar charts at zero** — truncated axes distort perception
- **Use direct labels** over legends when possible — reduces eye movement
- **Limit colors** — 3–5 max; use one accent color to highlight key data
- **Sort meaningfully** — alphabetical order rarely reveals insight; sort by value

## Table Formatting

| Element | Best Practice | Anti-Pattern |
|---------|--------------|-------------|
| Row shading | Alternate light/white rows | Heavy grid lines everywhere |
| Alignment | Left for text, right for numbers | Center-aligned numbers |
| Header row | Bold, background color, frozen | No visual distinction from data |
| Number formatting | Consistent decimals, thousands separators | Raw unformatted numbers |
| Column width | Proportional to content | All columns equal width |
| Row height | Consistent, with padding | Cramped rows with no spacing |
| Totals | Bold, separated by line | Mixed in with data rows |

## Color Strategy

| Purpose | Color Usage | Example |
|---------|------------|---------|
| Brand alignment | Primary brand color for headers, accents | Blue headers, dark gray body |
| Data encoding | Sequential palette for magnitude, diverging for +/- | Revenue heat from light to dark blue |
| Status indicators | Red/amber/green for performance | KPIs colored by threshold |
| Emphasis | Single accent color against neutral | Orange highlight on key finding |
| Accessibility | 4.5:1 contrast, colorblind-safe palettes | Use patterns + color together |

## Best Practices

- **One insight per page** — every page should have a clear takeaway visible in 5 seconds
- **Lead with the conclusion** — state the insight first, then show the supporting data
- **Design for scanning** — executives read headers, look at charts, then read text if interested
- **Be consistent** — same chart style, colors, and layout patterns throughout the report
- **Source everything** — every chart and table needs a data source citation
- **Print-test your reports** — many executives still print reports; verify readability at grayscale

## Using the Reference Files

**`/references/layout-principles.md`** — Read when designing page layouts. Covers grid systems, visual hierarchy, page anatomy, and multi-page flow.

**`/references/typography-color.md`** — Read when selecting fonts or defining color palettes. Covers font pairing, number formatting, brand color application, and accessibility.

**`/references/data-visualization.md`** — Read when creating charts or visualizing data. Covers chart selection, design rules, axis formatting, and annotation techniques.

**`/references/templates-examples.md`** — Read when building reusable report templates. Covers template structures for different report types, style guides, and example layouts.
