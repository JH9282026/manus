# Responsive Spacing Patterns

Detailed patterns for adapting spacing across breakpoints and devices.

---

## Breakpoint-Based Spacing

### Scale by Breakpoint

| Token | Mobile (<768px) | Tablet (768–1023px) | Desktop (1024px+) |
|-------|-----------------|--------------------|-----------|
| Page padding | 16px | 24px | 32px |
| Card padding | 16px | 20px | 24px |
| Section gap | 32px | 48px | 64px |
| Component gap | 12px | 16px | 16px |
| Grid gutter | 16px | 20px | 24px |
| Modal padding | 16px | 24px | 32px |

### CSS Implementation

```css
/* Mobile-first responsive spacing */
.page {
  padding: 16px;
}
@media (min-width: 768px) {
  .page { padding: 24px; }
}
@media (min-width: 1024px) {
  .page { padding: 32px; }
}
```

---

## Fluid Spacing with clamp()

Use `clamp()` for smooth spacing transitions without breakpoints:

```css
/* Section spacing that scales with viewport */
.section-gap {
  padding: clamp(48px, 8vw, 96px) 0;
}

/* Container padding */
.container {
  padding: 0 clamp(16px, 4vw, 32px);
}

/* Hero spacing */
.hero {
  padding: clamp(64px, 12vw, 160px) 0;
}

/* Component gap */
.card-grid {
  gap: clamp(16px, 2vw, 24px);
}
```

---

## Touch Target Spacing

On touch devices, ensure adequate spacing between interactive elements:

- **Minimum touch target**: 44×44px (WCAG 2.5.5)
- **Recommended**: 48×48px for primary actions
- **Minimum gap between targets**: 8px
- **Recommended gap**: 12–16px on mobile

```css
/* Ensure touch targets on mobile */
@media (pointer: coarse) {
  .btn { min-height: 48px; min-width: 48px; }
  .nav-item { padding: 12px 16px; }
  .list-item { padding: 16px; }
}
```

---

## Spacing Audit by Breakpoint

When auditing responsive spacing:

1. **Check mobile first** — Ensure nothing is too cramped on small screens
2. **Verify touch targets** — All interactive elements meet 44px minimum
3. **Test intermediate sizes** — Check tablet sizes where layouts often break
4. **Validate large screens** — Ensure spacing doesn't become excessively large
5. **Test orientation changes** — Landscape mobile needs different spacing than portrait
