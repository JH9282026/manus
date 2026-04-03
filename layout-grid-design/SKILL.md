---
name: layout-grid-design
description: "Establish grid systems that create consistent, proportional layouts across pages and breakpoints. Use for: defining column grids, setting gutters and margins, creating modular layout templates, applying grid-based alignment, and ensuring visual consistency across desktop, tablet, and mobile designs."
---

# Layout Grids

Establish grid systems that create consistent, proportional layouts across pages and breakpoints.

# Skill: Layout Grids

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Layout Grids |
| **Category** | Visual Design |
| **Phase** | 3 - Visual Design |
| **Estimated Time** | 20-30 minutes |
| **Dependencies** | `wireframing.md` |
| **Outputs** | Grid specifications, column systems, responsive breakpoints |

## Description
Layout Grids establish the underlying structure for all visual layouts. A well-defined grid system ensures consistency, alignment, and predictable responsive behavior across all screens and components.

## When to Use
- After wireframes establish basic layout needs
- Setting up design system foundations
- Before designing detailed components
- Ensuring responsive design consistency
- When layouts feel misaligned or chaotic

---

## Instructions for AI Agents
### Step 1: Determine Grid Type

**Grid types by project:**

| Project Type | Recommended Grid | Rationale |
|--------------|------------------|----------|
| Marketing/Landing | 12-column | Flexible for varied layouts |
| Dashboard/App | 12-column with sidebar | Consistent app structure |
| Content/Blog | 12-column, content-centered | Reading focus |
| E-commerce | 12-column | Product grids flexibility |
| Mobile App | 4-column | Touch-friendly sizing |

### Step 2: Define Grid Specifications

**Grid system template:**

```markdown

## Grid System: [PROJECT]
### Desktop (1280px+)
| Property | Value |
|----------|-------|
| Container width | 1200px (max) |
| Columns | 12 |
| Column width | 72px (fluid) |
| Gutter | 24px |
| Margin (outside) | 32px |

### Tablet (768px - 1279px)
| Property | Value |
|----------|-------|
| Container width | 100% - 48px |
| Columns | 12 (or 8) |
| Gutter | 20px |
| Margin | 24px |

### Mobile (320px - 767px)
| Property | Value |
|----------|-------|
| Container width | 100% - 32px |
| Columns | 4 |
| Gutter | 16px |
| Margin | 16px |
```

### Step 3: Define Breakpoints

**Standard breakpoint system:**

```markdown
### Breakpoints

| Name | Min Width | Target Devices |
|------|-----------|----------------|
| xs | 0px | Small phones |
| sm | 640px | Large phones |
| md | 768px | Tablets portrait |
| lg | 1024px | Tablets landscape, laptops |
| xl | 1280px | Desktops |
| 2xl | 1536px | Large desktops |

### Mobile-First Approach
```css
/* Base styles: Mobile */
.element { ... }

/* Tablet and up */
@media (min-width: 768px) { ... }

/* Desktop and up */
@media (min-width: 1024px) { ... }
```
```

### Step 4: Column Layouts

**Common layout patterns:**

```markdown
### Layout Patterns

#### Full Width
```
│──────────── 12 columns ────────────│
```
Use: Hero sections, full-width images

#### Two Column (Equal)
```
│─── 6 col ───││─── 6 col ───│
```
Use: Feature comparisons, side-by-side content

#### Two Column (Sidebar)
```
│─ 3 ─││────── 9 columns ──────│
```
Use: Dashboard with navigation sidebar

#### Content + Sidebar
```
│───── 8 col ─────││─ 4 col ─│
```
Use: Blog posts with sidebar, forms with help

#### Three Column
```
│─ 4 col ─││─ 4 col ─││─ 4 col ─│
```
Use: Feature cards, product grid

#### Four Column
```
│ 3 ││ 3 ││ 3 ││ 3 │
```
Use: Stats, icon features, footer links

#### Centered Content
```
│ 2 ││───── 8 col ─────││ 2 │
```
Use: Article content, focused forms
```

### Step 5: Application Examples

**Grid in context:**

```markdown
### Page Layouts

#### Dashboard Layout
```
+---+----------------------------------+
|   |  Header (full width)             |
| S +----------------------------------+
| i |                                  |
| d |     Main Content Area            |
| e |     (9 columns)                  |
| b |                                  |
| a +----------------------------------+
| r |  (3 col spans height)            |
+---+----------------------------------+

Sidebar: 240px fixed
Content: Fluid (12-col grid within)
```

#### Landing Page
```
+--------------------------------------+
|  Nav (12 col, constrained center)    |
+--------------------------------------+
|                                      |
|  Hero (12 col, may break grid)       |
|                                      |
+--------------------------------------+
|  Features (4+4+4 or 6+6)             |
+--------------------------------------+
|  CTA (centered, 8 col)               |
+--------------------------------------+
|  Footer (12 col, 4+4+4)              |
+--------------------------------------+
```
```

---

## Example Input/Output
### Example Input

```markdown
**Project**: TaskFlow dashboard application
**Key layouts**: Dashboard, project list, task detail
**Sidebar needed**: Yes, persistent navigation
**Priority**: Desktop-first but responsive
```

### Example Output

```markdown

## Prompts Library
### Quick Grid Setup
```
Create a grid system for [PROJECT TYPE]:
- Primary device: [Desktop/Mobile]
- Sidebar needed: [Yes/No]
- Max content width: [Width]

Provide: breakpoints, column count, gutter sizes, margin sizes
```

### Layout Pattern
```
How should this content be laid out:
[CONTENT DESCRIPTION]

On:
- Desktop (12 columns)
- Tablet (8 columns)
- Mobile (4 columns)

Provide column spans for each element at each breakpoint.
```

---

## Success Criteria
### Minimum Requirements
- [ ] Column system defined
- [ ] Gutter sizes specified
- [ ] Breakpoints established
- [ ] Key layouts mapped to grid
- [ ] Responsive behavior documented

### Quality Indicators
- [ ] Grid supports all wireframed layouts
- [ ] Consistent spacing throughout
- [ ] Mobile-friendly column collapse
- [ ] Flexible for future layouts

---

## Related Skills
- **Previous**: `wireframing.md` - Layout structure to formalize
- **Next**: `spacing_rhythm.md` - Vertical spacing complements grid
- **Related**: `responsive_design.md` - Grid enables responsiveness

## Using the Reference Files

### When to Read Each Reference

**`./references/grid-system-taskflow.md`** — Read when you need detailed guidance on grid system taskflow aspects of this skill.
