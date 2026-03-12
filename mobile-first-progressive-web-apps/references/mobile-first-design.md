# Mobile-First Design

## Responsive Design Strategy

### Breakpoint System
| Breakpoint | Target | CSS |
|-----------|--------|-----|
| Default | Mobile (320px+) | Base styles (no media query) |
| 768px | Tablet | `@media (min-width: 768px)` |
| 1024px | Desktop | `@media (min-width: 1024px)` |
| 1440px | Large desktop | `@media (min-width: 1440px)` |

### Layout Patterns
- **Stack to grid**: Single column mobile → multi-column desktop
- **Off-canvas**: Hidden navigation on mobile, visible on desktop
- **Column drop**: Remove columns as viewport shrinks
- **Layout shifter**: Different layouts per breakpoint

---

## Touch Interaction Design

### Touch Target Sizes
- Minimum: 44×44px (Apple HIG)
- Recommended: 48×48px (Material Design)
- Spacing between targets: 8px minimum

### Thumb Zone Optimization
- **Easy reach** (bottom center): Primary actions, navigation
- **Stretch zone** (top, far sides): Secondary actions
- **Hard to reach** (top corners): Rarely used actions

### Gesture Support
| Gesture | Use Case | Consideration |
|---------|----------|---------------|
| Tap | Primary interaction | Clear feedback |
| Swipe | Navigation, dismiss | Provide alternatives |
| Long press | Context menu | Discoverability issue |
| Pinch/zoom | Images, maps | Don't block with viewport meta |
| Pull to refresh | Content update | Platform convention |

---

## Mobile Performance Optimization

### Critical Rendering Path
1. Minimize critical CSS (inline above-fold styles)
2. Defer non-critical JavaScript
3. Optimize images (WebP, responsive srcset)
4. Implement lazy loading for below-fold content
5. Use font-display: swap for web fonts

### Image Optimization
| Format | Use Case | Browser Support |
|--------|----------|----------------|
| WebP | Photos, complex images | 95%+ |
| AVIF | Next-gen compression | 85%+ |
| SVG | Icons, illustrations | Universal |
| PNG | Transparency needed | Universal |

### Performance Budget
| Resource | Budget |
|----------|--------|
| Total page weight | <500KB (mobile) |
| JavaScript | <150KB compressed |
| CSS | <50KB compressed |
| Images | <200KB (above fold) |
| Fonts | <100KB |
| Time to Interactive | <3.5s on 3G |

---

## Mobile Navigation Patterns

| Pattern | When to Use |
|---------|------------|
| Bottom tab bar | 3-5 primary destinations |
| Hamburger menu | 5+ sections, secondary nav |
| Tab bar (top) | Content categories |
| Gesture navigation | Sequential content (stories) |
| Search-first | Content-heavy apps |
