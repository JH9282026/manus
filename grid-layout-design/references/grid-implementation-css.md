# Grid Implementation CSS

CSS implementation patterns for grid systems including utilities, responsive media queries, and framework equivalents.

---

## CSS Grid Implementation

### Base Grid Container

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
  padding: 0 24px;
  max-width: 1200px;
  margin: 0 auto;
}
```

### Column Span Utilities

```css
.col-span-1  { grid-column: span 1; }
.col-span-2  { grid-column: span 2; }
.col-span-3  { grid-column: span 3; }
.col-span-4  { grid-column: span 4; }
.col-span-5  { grid-column: span 5; }
.col-span-6  { grid-column: span 6; }
.col-span-7  { grid-column: span 7; }
.col-span-8  { grid-column: span 8; }
.col-span-9  { grid-column: span 9; }
.col-span-10 { grid-column: span 10; }
.col-span-11 { grid-column: span 11; }
.col-span-12 { grid-column: span 12; }
```

### Responsive Grid

```css
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

  /* Full width on mobile */
  .col-span-6,
  .col-span-4,
  .col-span-3 {
    grid-column: span 4;
  }
}
```

---

## Flexbox Alternative

```css
.flex-grid {
  display: flex;
  flex-wrap: wrap;
  margin: 0 -12px;  /* half gutter */
}

.flex-col {
  padding: 0 12px;  /* half gutter */
  box-sizing: border-box;
}

.flex-col-6  { width: 50%; }
.flex-col-4  { width: 33.333%; }
.flex-col-3  { width: 25%; }
.flex-col-12 { width: 100%; }
```

---

## Tailwind CSS Equivalents

| Custom Grid | Tailwind Equivalent |
|------------|--------------------|
| `.grid-container` | `grid grid-cols-12 gap-6 px-6 max-w-screen-xl mx-auto` |
| `.col-span-6` | `col-span-6` |
| `.col-span-4` | `col-span-4` |
| Responsive 4-col | `grid-cols-4 md:grid-cols-8 lg:grid-cols-12` |
| Gap responsive | `gap-4 md:gap-5 lg:gap-6` |

---

## Sidebar + Content Layout

```css
.app-layout {
  display: grid;
  grid-template-columns: 240px 1fr;
  min-height: 100vh;
}

@media (max-width: 1023px) {
  .app-layout {
    grid-template-columns: 64px 1fr;
  }
}

@media (max-width: 767px) {
  .app-layout {
    grid-template-columns: 1fr;
  }
}
```

---

## Grid Debug Overlay

Add a visual grid overlay during development:

```css
.grid-debug {
  position: fixed;
  inset: 0;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
  padding: 0 24px;
  max-width: 1200px;
  margin: 0 auto;
  pointer-events: none;
  z-index: 9999;
}

.grid-debug > div {
  background: rgba(255, 0, 0, 0.08);
  border-left: 1px solid rgba(255, 0, 0, 0.15);
  border-right: 1px solid rgba(255, 0, 0, 0.15);
}
```

Toggle with a keyboard shortcut during design reviews.
