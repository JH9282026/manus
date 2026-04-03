---
name: grid-layout-design
description: "Define column-based grid systems, breakpoints, and layout patterns for consistent, responsive page structure. Use for: establishing 12-column grid specifications, defining responsive breakpoints, creating layout templates for dashboards and landing pages, specifying sidebar and content area configurations, and generating CSS grid or flexbox implementations."
---

# Grid Layout Design

Establish the underlying column-based grid structure for all visual layouts, ensuring consistency, alignment, and predictable responsive behavior.

## Overview

Layout Grids establish the underlying structure for all visual layouts. A well-defined grid system ensures consistency, alignment, and predictable responsive behavior across all screens and components. This skill covers grid type selection, column and gutter specifications, breakpoint systems, common layout patterns, and CSS implementation.

## When to Use

- After wireframes establish basic layout needs
- Setting up design system foundations
- Before designing detailed components
- Ensuring responsive design consistency
- When layouts feel misaligned or chaotic

## Grid Type by Project

| Project Type | Recommended Grid | Rationale |
|--------------|------------------|----------|
| Marketing / Landing | 12-column | Flexible for varied layouts |
| Dashboard / App | 12-column with sidebar | Consistent app structure |
| Content / Blog | 12-column, content-centered | Reading focus |
| E-commerce | 12-column | Product grid flexibility |
| Mobile App | 4-column | Touch-friendly sizing |

## Grid Specifications

### Desktop (1024px+)

| Property | Value |
|----------|-------|
| Container max-width | 1200px |
| Columns | 12 |
| Gutter | 24px |
| Margin (outside) | 24–32px |

### Tablet (768px – 1023px)

| Property | Value |
|----------|-------|
| Container width | 100% - 48px |
| Columns | 8 (or 12) |
| Gutter | 20px |
| Margin | 20–24px |

### Mobile (320px – 767px)

| Property | Value |
|----------|-------|
| Container width | 100% - 32px |
| Columns | 4 |
| Gutter | 16px |
| Margin | 16px |

## Breakpoint System

| Name | Min Width | Target Devices |
|------|-----------|----------------|
| xs | 0px | Small phones |
| sm | 640px | Large phones |
| md | 768px | Tablets portrait |
| lg | 1024px | Tablets landscape, laptops |
| xl | 1280px | Desktops |
| 2xl | 1536px | Large desktops |

Use **mobile-first** approach: base styles for mobile, `@media (min-width: ...)` for larger screens.

## Common Layout Patterns

| Pattern | Columns | Use Case |
|---------|---------|----------|
| Full Width | 12 | Hero sections, full-width images |
| Two Column (Equal) | 6 + 6 | Feature comparisons, side-by-side |
| Two Column (Sidebar) | 3 + 9 | Dashboard with navigation sidebar |
| Content + Sidebar | 8 + 4 | Blog posts with sidebar, forms with help |
| Three Column | 4 + 4 + 4 | Feature cards, product grids |
| Four Column | 3 + 3 + 3 + 3 | Stats, icon features, footer links |
| Centered Content | 2 + 8 + 2 | Article content, focused forms |

## Dashboard Layout Pattern

```
+--------+-----------------------------------+
|        |  Header (full width)              |
| Side   +-----------------------------------+
| bar    |                                   |
| (fixed)|     Main Content Area             |
| 240px  |     (12-col grid within)          |
|        |                                   |
+--------+-----------------------------------+

Sidebar: 240px fixed (64px collapsed on tablet, hidden on mobile)
Content: Fluid with 12-column grid
```

## Landing Page Layout Pattern

```
+---------------------------------------+
|  Nav (12 col, constrained center)     |
+---------------------------------------+
|  Hero (12 col, may break grid)        |
+---------------------------------------+
|  Features (4+4+4 or 6+6)             |
+---------------------------------------+
|  CTA (centered, 8 col)               |
+---------------------------------------+
|  Footer (12 col, 4+4+4)              |
+---------------------------------------+
```

## Responsive Collapse Rules

Define how layouts collapse at smaller breakpoints:

| Desktop Layout | Tablet | Mobile |
|---------------|--------|--------|
| 4-column card grid (3+3+3+3) | 2-column (6+6) | 1-column (12) |
| Content + sidebar (8+4) | Full width stacked | Full width stacked |
| 3-column (4+4+4) | 2-column + full (6+6, 12) | 1-column (12) |
| Sidebar navigation | Collapsed icons (64px) | Hidden (hamburger) |

## CSS Grid Implementation

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
  padding: 0 24px;
  max-width: 1200px;
  margin: 0 auto;
}

@media (max-width: 1023px) {
  .grid-container {
    grid-template-columns: repeat(8, 1fr);
    gap: 20px;
    padding: 0 20px;
  }
}

@media (max-width: 767px) {
  .grid-container {
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    padding: 0 16px;
  }
}
```

## Design Tokens

```json
{
  "grid": {
    "columns": 12,
    "gutter": { "desktop": "24px", "tablet": "20px", "mobile": "16px" },
    "margin": { "desktop": "24px", "tablet": "20px", "mobile": "16px" },
    "maxWidth": "1200px"
  },
  "sidebar": { "widthFull": "240px", "widthCollapsed": "64px" },
  "breakpoints": { "sm": "640px", "md": "768px", "lg": "1024px", "xl": "1280px", "2xl": "1536px" }
}
```

## Best Practices

1. **Start with content needs** — Let content requirements drive grid decisions
2. **Use consistent gutters** — Same gutter width at each breakpoint
3. **Design for mobile first** — Progressive enhancement from 4-column base
4. **Avoid breaking the grid** — All elements should snap to column boundaries
5. **Document collapse rules** — Specify exactly how each layout adapts
6. **Test with real content** — Grids that work with lorem ipsum may fail with real data

## Using the Reference Files

### When to Read Each Reference

**`./references/grid-specifications-detail.md`** — Read when needing detailed grid specifications for specific project types, including sidebar configurations, max-width calculations, and grid math.

**`./references/layout-patterns-examples.md`** — Read when designing specific page layouts (dashboard, landing page, task detail) or needing concrete examples of grid application with ASCII diagrams.

**`./references/grid-implementation-css.md`** — Read when implementing grids in CSS, needing utility class definitions, responsive media queries, or Tailwind/Bootstrap grid equivalents.
