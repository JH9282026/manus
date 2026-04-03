# Grid Specifications Detail

Detailed grid specifications for different project types and configurations.

---

## Standard 12-Column Grid (Desktop)

```
┌───────┬─────────────────────────────────────────────┐
│       │  24px  │ col │ 24px │ col │ 24px │...     24px │
│ 240px │ margin │     │gutter│     │gutter│      margin │
│sidebar│        │     │      │     │      │             │
└───────┴────────┴─────┴──────┴─────┴──────┴─────────────┘

         │──────── 12-column grid ─────────│
```

---

## Grid Math

For a 1200px container with 12 columns and 24px gutters:

- Total gutter space: 11 gutters × 24px = 264px
- Available column space: 1200px - 264px = 936px
- Each column width: 936px / 12 = 78px
- Column + gutter: 78px + 24px = 102px

---

## Dashboard Grid with Sidebar

### Breakpoint Configurations

| Breakpoint | Sidebar | Columns | Gutter | Margin |
|------------|---------|---------|--------|--------|
| Mobile (<768px) | Hidden (hamburger) | 4 | 16px | 16px |
| Tablet (768–1023px) | Collapsed (64px icons) | 8 | 20px | 20px |
| Desktop (1024–1439px) | Full (240px) | 12 | 24px | 24px |
| Large (1440px+) | Full (280px) | 12 | 24px | 24px |

### Content Area Calculation

At 1280px viewport with 240px sidebar:
- Content area: 1280px - 240px = 1040px
- Margins: 24px each side = 48px
- Grid area: 1040px - 48px = 992px
- 11 gutters: 264px
- Column width: (992px - 264px) / 12 = 60.67px (fluid)

---

## Content-Centered Grid

For blog/article layouts:

- Max content width: 680–720px (optimal reading width)
- This equals roughly 8 columns in a 12-column grid
- Center with 2 empty columns on each side
- Sidebar (if needed) fits in the rightmost 3–4 columns

---

## E-Commerce Product Grid

| Breakpoint | Products per Row | Column Span |
|------------|-----------------|-------------|
| Mobile | 2 | 2 cols each |
| Tablet | 3 | ~2.67 cols each |
| Desktop | 4 | 3 cols each |
| Large | 5 | ~2.4 cols each |

Product card aspect ratios:
- Portrait (3:4) for fashion
- Square (1:1) for general products
- Landscape (4:3) for electronics
