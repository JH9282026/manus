# Spacing Scale Implementation

Detailed CSS custom properties, design tokens, and code examples for implementing a spacing system.

---

## CSS Custom Properties

```css
:root {
  /* Core spacing scale */
  --space-0: 0;
  --space-px: 1px;
  --space-0-5: 0.125rem;  /* 2px */
  --space-1: 0.25rem;     /* 4px */
  --space-1-5: 0.375rem;  /* 6px */
  --space-2: 0.5rem;      /* 8px */
  --space-2-5: 0.625rem;  /* 10px */
  --space-3: 0.75rem;     /* 12px */
  --space-4: 1rem;        /* 16px */
  --space-5: 1.25rem;     /* 20px */
  --space-6: 1.5rem;      /* 24px */
  --space-8: 2rem;        /* 32px */
  --space-10: 2.5rem;     /* 40px */
  --space-12: 3rem;       /* 48px */
  --space-16: 4rem;       /* 64px */
  --space-20: 5rem;       /* 80px */
  --space-24: 6rem;       /* 96px */

  /* Semantic spacing */
  --space-component-padding: var(--space-4);
  --space-card-padding: var(--space-6);
  --space-section-gap: var(--space-12);
  --space-page-padding: var(--space-8);
}
```

---

## Component Spacing Examples

### Buttons
```css
.btn-sm { padding: var(--space-1-5) var(--space-3); }   /* 6px 12px */
.btn-md { padding: var(--space-2-5) var(--space-4); }   /* 10px 16px */
.btn-lg { padding: var(--space-3) var(--space-6); }     /* 12px 24px */
```

### Cards
```css
.card {
  padding: var(--space-5);  /* 20px */
}
.card-header {
  padding: var(--space-4) var(--space-5);  /* 16px 20px */
  margin: calc(-1 * var(--space-5)) calc(-1 * var(--space-5)) var(--space-5);
}
.card > * + * {
  margin-top: var(--space-4);  /* 16px between children */
}
```

### Form Elements
```css
.form-group {
  margin-bottom: var(--space-5);  /* 20px */
}
.form-group label {
  margin-bottom: var(--space-1-5);  /* 6px */
}
.form-row {
  gap: var(--space-4);  /* 16px */
}
```

### Page Layout
```css
.page {
  padding: var(--space-8);  /* 32px */
}
.page-header {
  margin-bottom: var(--space-8);  /* 32px */
}
.page-section {
  margin-bottom: var(--space-12);  /* 48px */
}
.page-section:last-child {
  margin-bottom: 0;
}
```

### Sidebar
```css
.sidebar {
  padding: var(--space-4);  /* 16px */
}
.sidebar-section + .sidebar-section {
  margin-top: var(--space-6);  /* 24px */
  padding-top: var(--space-6);
  border-top: 1px solid var(--border);
}
.nav-item {
  padding: var(--space-2-5) var(--space-3);  /* 10px 12px */
  margin-bottom: var(--space-0-5);  /* 2px */
}
```

---

## Design Token Format (JSON)

```json
{
  "spacing": {
    "0": "0",
    "px": "1px",
    "0.5": "0.125rem",
    "1": "0.25rem",
    "1.5": "0.375rem",
    "2": "0.5rem",
    "2.5": "0.625rem",
    "3": "0.75rem",
    "4": "1rem",
    "5": "1.25rem",
    "6": "1.5rem",
    "8": "2rem",
    "10": "2.5rem",
    "12": "3rem",
    "16": "4rem",
    "20": "5rem",
    "24": "6rem"
  }
}
```

---

## Spacing Audit Checklist

When auditing an existing design for spacing consistency:

1. **Extract all unique spacing values** — List every padding and margin used
2. **Map to the scale** — Identify values that don't match the spacing scale
3. **Replace rogue values** — Round to nearest scale value
4. **Check component consistency** — Same component types should use same spacing
5. **Verify responsive behavior** — Spacing scales down appropriately on smaller screens
6. **Test touch targets** — All interactive elements meet 44×44px minimum
