# Grid System: TaskFlow - Detailed Reference

Detailed reference content for layout grids.

---

## Grid System: TaskFlow
### Overview

**Grid Type**: 12-column with fixed sidebar
**Approach**: Desktop-first with fluid content area

---

### Breakpoints

| Name | Width | Columns | Sidebar |
|------|-------|---------|--------|
| Mobile | <768px | 4 | Hidden (hamburger) |
| Tablet | 768-1023px | 8 | Collapsed (icons only) |
| Desktop | 1024-1439px | 12 | Full (240px) |
| Large | 1440px+ | 12 | Full (280px) |

---

### Grid Specifications

#### Desktop (1024px+)

```
┌───────┬─────────────────────────────────────────────┐
│       │  24px  │ col │ 24px │ col │ 24px │...     24px │
│ 240px │ margin │     │gutter│     │gutter│      margin │
│sidebar│        │     │      │     │      │             │
└───────┴────────┴─────┴──────┴─────┴──────┴─────────────┘

         │──────── 12-column grid ─────────│
```

**Specifications:**
| Property | Value |
|----------|-------|
| Sidebar width | 240px fixed |
| Content area | Fluid (remaining) |
| Columns in content | 12 |
| Gutter | 24px |
| Content margin | 24px (left/right) |
| Content max-width | 1200px |

#### Tablet (768-1023px)

**Specifications:**
| Property | Value |
|----------|-------|
| Sidebar width | 64px (icons only) |
| Columns | 8 |
| Gutter | 20px |
| Margin | 20px |

#### Mobile (<768px)

**Specifications:**
| Property | Value |
|----------|-------|
| Sidebar | Hidden (hamburger menu) |
| Columns | 4 |
| Gutter | 16px |
| Margin | 16px |

---

### Layout Templates

#### Dashboard Main
```
Desktop:
┌───────┬──────────────────────────────────────┐
│ Side  │  Page Header (12 col)              │
│  bar  ├────────────┬────────────┬────────────┤
│       │   Stat    │    Stat   │   Stat    │
│       │  (4 col)  │  (4 col)  │  (4 col)  │
│       ├────────────┴────────────┴────────────┤
│       │                                    │
│       │   Main Content (12 col)           │
│       │                                    │
└───────┴──────────────────────────────────────┘

Mobile:
┌───────────────┐
│  [☰] Header  │
├───────────────┤
│  Stat (full) │
├───────────────┤
│  Stat (full) │
├───────────────┤
│  Main (full) │
├───────────────┤
│  [Tab Bar]   │
└───────────────┘
```

#### Project List
```
Desktop: 4-column card grid
│ Card │ Card │ Card │ Card │  (3-col each)
│ Card │ Card │ Card │ Card │

Tablet: 2-column
│ Card │ Card │  (4-col each)
│ Card │ Card │

Mobile: 1-column
│ Card (full) │
│ Card (full) │
```

#### Task Detail (Side Panel)
```
Desktop:
┌───────┬────────────────────┬──────────────┐
│ Side  │   Task List      │  Task Detail  │
│  bar  │   (7 col)        │   (5 col)     │
│       │                  │   Slides in   │
└───────┴────────────────────┴──────────────┘

Mobile: Full-screen overlay
```

---

### CSS Implementation

```css
/* Grid Container */
.grid-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
  padding: 0 24px;
  max-width: 1200px;
  margin: 0 auto;
}

/* Span utilities */
.col-span-12 { grid-column: span 12; }
.col-span-8 { grid-column: span 8; }
.col-span-6 { grid-column: span 6; }
.col-span-4 { grid-column: span 4; }
.col-span-3 { grid-column: span 3; }

/* Responsive */
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
  
  .col-span-6,
  .col-span-4,
  .col-span-3 {
    grid-column: span 4; /* Full width on mobile */
  }
}
```

---

### Design Tokens

```json
{
  "grid": {
    "columns": 12,
    "gutter": {
      "desktop": "24px",
      "tablet": "20px",
      "mobile": "16px"
    },
    "margin": {
      "desktop": "24px",
      "tablet": "20px", 
      "mobile": "16px"
    },
    "maxWidth": "1200px"
  },
  "sidebar": {
    "widthFull": "240px",
    "widthCollapsed": "64px"
  },
  "breakpoints": {
    "sm": "640px",
    "md": "768px",
    "lg": "1024px",
    "xl": "1280px",
    "2xl": "1536px"
  }
}
```
```

---
