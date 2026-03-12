# Responsive Design Patterns

## CSS Layout Strategies

### Flexbox Patterns
- **Navigation**: `display: flex; flex-wrap: wrap;` for responsive nav
- **Card layouts**: `flex: 1 1 300px;` for auto-wrapping cards
- **Sticky footer**: `flex-grow: 1` on main content
- **Centering**: `display: flex; align-items: center; justify-content: center;`

### CSS Grid Patterns
- **Auto-fit columns**: `grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))`
- **Holy grail layout**: Named grid areas with responsive reflow
- **Magazine layout**: `grid-template-rows: masonry` for varied content
- **Sidebar + content**: `grid-template-columns: minmax(200px, 25%) 1fr`

### Container Queries
- Size components based on container, not viewport
- Use `container-type: inline-size` on parent
- Query with `@container (min-width: 400px)`
- Better for reusable components than media queries

---

## Responsive Typography

### Fluid Type Scale
- Base size: 16px (1rem)
- Use `clamp()` for fluid sizing: `font-size: clamp(1rem, 2.5vw, 1.5rem)`
- Maintain readable line length: 45-75 characters
- Adjust line-height for mobile: 1.5-1.7 for body text

### Type Scale
| Level | Mobile | Desktop |
|-------|--------|---------|
| H1 | 1.75rem | 2.5rem |
| H2 | 1.5rem | 2rem |
| H3 | 1.25rem | 1.5rem |
| Body | 1rem | 1rem |
| Small | 0.875rem | 0.875rem |

---

## Responsive Images

### srcset and sizes
```html
<img
  srcset="image-400.jpg 400w, image-800.jpg 800w, image-1200.jpg 1200w"
  sizes="(max-width: 600px) 100vw, (max-width: 1024px) 50vw, 33vw"
  src="image-800.jpg"
  alt="Description"
  loading="lazy"
>
```

### Picture Element for Art Direction
```html
<picture>
  <source media="(min-width: 1024px)" srcset="hero-wide.webp">
  <source media="(min-width: 768px)" srcset="hero-medium.webp">
  <img src="hero-mobile.webp" alt="Hero image">
</picture>
```

---

## Responsive Component Patterns

### Navigation
| Viewport | Pattern |
|----------|---------|
| Mobile (<768px) | Hamburger menu or bottom tab bar |
| Tablet (768-1024px) | Collapsed sidebar or icon-only nav |
| Desktop (>1024px) | Full horizontal or sidebar navigation |

### Data Tables
| Approach | When to Use |
|----------|-------------|
| Horizontal scroll | Few columns, user expects table |
| Card layout | Many columns, mobile priority |
| Priority columns | Show key columns, hide others |
| Collapsible rows | Detail on demand |
