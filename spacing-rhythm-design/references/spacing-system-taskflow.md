# Spacing System: TaskFlow - Detailed Reference

Detailed reference content for spacing & rhythm.

---

## Spacing System: TaskFlow
### Foundation

**Base Unit**: 8px
**Philosophy**: Balanced whitespace for productive, calm interface

---

### Spacing Scale

| Token | rem | px | Usage |
|-------|-----|-----|-------|
| `--space-0` | 0 | 0 | Reset |
| `--space-px` | 1px | 1px | Borders |
| `--space-0.5` | 0.125rem | 2px | Hairline gaps |
| `--space-1` | 0.25rem | 4px | Tight gaps, icon-text |
| `--space-1.5` | 0.375rem | 6px | Dense lists |
| `--space-2` | 0.5rem | 8px | Related elements |
| `--space-2.5` | 0.625rem | 10px | Button padding-y |
| `--space-3` | 0.75rem | 12px | Default internal |
| `--space-4` | 1rem | 16px | Standard gap |
| `--space-5` | 1.25rem | 20px | Card padding (compact) |
| `--space-6` | 1.5rem | 24px | Card padding, gutter |
| `--space-8` | 2rem | 32px | Section title gap |
| `--space-10` | 2.5rem | 40px | Component groups |
| `--space-12` | 3rem | 48px | Minor sections |
| `--space-16` | 4rem | 64px | Major sections |
| `--space-20` | 5rem | 80px | Page sections |
| `--space-24` | 6rem | 96px | Hero spacing |

---

### Application Rules

#### Components

**Buttons**
```css
.btn-sm { padding: 6px 12px; }    /* space-1.5, space-3 */
.btn-md { padding: 10px 16px; }   /* space-2.5, space-4 */
.btn-lg { padding: 12px 24px; }   /* space-3, space-6 */
```

**Cards**
```css
.card {
  padding: 20px;             /* space-5 */
}
.card-header {
  padding: 16px 20px;        /* space-4, space-5 */
  margin: -20px -20px 20px;  /* Bleed to edges */
}
.card > * + * {
  margin-top: 16px;          /* space-4 between children */
}
```

**Form Elements**
```css
.form-group {
  margin-bottom: 20px;       /* space-5 */
}
.form-group label {
  margin-bottom: 6px;        /* space-1.5 */
}
.form-row {
  gap: 16px;                 /* space-4 */
}
```

#### Layout

**Page Structure**
```css
.page {
  padding: 32px;             /* space-8 */
}
.page-header {
  margin-bottom: 32px;       /* space-8 */
}
.page-section {
  margin-bottom: 48px;       /* space-12 */
}
.page-section:last-child {
  margin-bottom: 0;
}
```

**Content Sections**
```css
.section-title {
  margin-bottom: 24px;       /* space-6 */
}
.section-content > * + * {
  margin-top: 16px;          /* space-4 */
}
```

**Sidebar**
```css
.sidebar {
  padding: 16px;             /* space-4 */
}
.sidebar-section + .sidebar-section {
  margin-top: 24px;          /* space-6 */
  padding-top: 24px;
  border-top: 1px solid var(--border);
}
.nav-item {
  padding: 10px 12px;        /* space-2.5, space-3 */
  margin-bottom: 2px;        /* space-0.5 */
}
```

---

### Vertical Rhythm

**Baseline**: 8px (tight) to 24px (relaxed)

**Text Flow**
```css
p + p {
  margin-top: 16px;          /* space-4 */
}
h2, h3, h4 {
  margin-top: 32px;          /* space-8 */
  margin-bottom: 16px;       /* space-4 */
}
ul, ol {
  margin: 16px 0;            /* space-4 */
}
li + li {
  margin-top: 8px;           /* space-2 */
}
```

**Element Heights (8px aligned)**
```
Button sm:  32px (4 × 8px)
Button md:  40px (5 × 8px)
Button lg:  48px (6 × 8px)
Input:      44px (touch-friendly)
Nav item:   40px (5 × 8px)
Table row:  48px (6 × 8px)
Avatar sm:  32px (4 × 8px)
Avatar md:  40px (5 × 8px)
Avatar lg:  48px (6 × 8px)
```

---

### Responsive Adjustments

| Spacing Type | Mobile | Tablet | Desktop |
|--------------|--------|--------|----------|
| Page padding | 16px | 24px | 32px |
| Card padding | 16px | 20px | 24px |
| Section gap | 32px | 48px | 64px |
| Component gap | 12px | 16px | 16px |
| Grid gutter | 16px | 20px | 24px |

```css
/* Responsive page padding */
.page {
  padding: 16px;
}
@media (min-width: 768px) {
  .page {
    padding: 24px;
  }
}
@media (min-width: 1024px) {
  .page {
    padding: 32px;
  }
}
```

---

### Quick Reference

**Tight (2-4px)**: Icon-to-text, stacked badges
**Compact (8-12px)**: Related elements, list items
**Standard (16-24px)**: Component gaps, card padding
**Relaxed (32-48px)**: Section titles, component groups
**Spacious (64-96px)**: Page sections, hero areas

---

### CSS Custom Properties

```css
:root {
  --space-0: 0;
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-3: 0.75rem;  /* 12px */
  --space-4: 1rem;     /* 16px */
  --space-5: 1.25rem;  /* 20px */
  --space-6: 1.5rem;   /* 24px */
  --space-8: 2rem;     /* 32px */
  --space-10: 2.5rem;  /* 40px */
  --space-12: 3rem;    /* 48px */
  --space-16: 4rem;    /* 64px */
  --space-20: 5rem;    /* 80px */
  --space-24: 6rem;    /* 96px */
  
  /* Semantic spacing */
  --space-component-padding: var(--space-4);
  --space-card-padding: var(--space-6);
  --space-section-gap: var(--space-12);
  --space-page-padding: var(--space-8);
}
```
```

---
