---
name: "interactive-infographics-web-visualization"
description: "Build interactive data visualizations and infographics for the web using JavaScript libraries and modern web technologies. Use for: D3.js visualizations, interactive charts, scrollytelling, animated data stories, responsive data dashboards, map visualizations, and web-based data exploration tools."
---

# Interactive Infographics & Web Visualization

Build engaging interactive data visualizations and infographics for the web that let users explore, filter, and discover insights.

## Overview

Interactive infographics go beyond static images — they let users hover for details, filter by category, scroll through data narratives, and explore datasets visually. This skill covers JavaScript visualization libraries, interaction design patterns, responsive implementation, scrollytelling techniques, and performance optimization. The goal is to create web-based data experiences that are both informative and engaging.

## Library Selection Guide

| Library | Type | Learning Curve | Customization | Best For | Reference |
|---------|------|---------------|---------------|----------|-----------|
| D3.js | Low-level SVG/Canvas | Steep | Unlimited | Custom, bespoke visualizations | `/references/javascript-libraries-tools.md` |
| Chart.js | Declarative charting | Easy | Medium | Standard chart types, quick setup | `/references/javascript-libraries-tools.md` |
| Plotly.js | Scientific/analytical | Medium | High | Data science, 3D plots, dashboards | `/references/javascript-libraries-tools.md` |
| Highcharts | Enterprise charting | Easy | High | Business dashboards, export features | `/references/javascript-libraries-tools.md` |
| Vega-Lite | Grammar of graphics | Medium | High | Concise spec-driven charts | `/references/javascript-libraries-tools.md` |
| Observable Plot | Modern, concise | Easy–Medium | Medium | Notebooks, exploratory analysis | `/references/javascript-libraries-tools.md` |
| Leaflet / Mapbox GL | Map visualization | Medium | High | Geographic data, choropleths | `/references/javascript-libraries-tools.md` |
| Three.js | 3D visualization | Steep | Unlimited | 3D data viz, immersive experiences | `/references/javascript-libraries-tools.md` |

### Decision Guide

| Scenario | Recommended Library | Why |
|----------|-------------------|-----|
| Simple bar/line/pie chart | Chart.js or Highcharts | Fast setup, responsive out of box |
| Custom, unique visualization | D3.js | Full control over every element |
| Geographic/map data | Leaflet (simple) or Mapbox GL (complex) | Purpose-built for maps |
| Data-heavy dashboard | Plotly.js or Highcharts | Built-in zoom, pan, export |
| Scrollytelling narrative | D3.js + Scrollama | Best for scroll-triggered animations |
| Specification-driven workflow | Vega-Lite | Declarative JSON spec |

## Interaction Design Patterns

| Pattern | Implementation | User Value | Reference |
|---------|---------------|------------|-----------|
| Hover tooltips | Show data details on mouseover | Explore individual data points | `/references/interactivity-design.md` |
| Click to filter | Toggle categories on/off | Focus on specific subsets | `/references/interactivity-design.md` |
| Brush/selection | Drag to select range | Zoom into time periods or ranges | `/references/interactivity-design.md` |
| Linked views | Interaction in one chart filters another | Cross-dimensional analysis | `/references/interactivity-design.md` |
| Animated transitions | Smooth morph between data states | Show change over time | `/references/interactivity-design.md` |
| Search/autocomplete | Find specific data points | Navigate large datasets | `/references/interactivity-design.md` |
| Scroll-triggered | Reveal visualizations as user scrolls | Guided data narrative | `/references/interactivity-design.md` |
| Zoom/pan | Navigate large or detailed visualizations | Explore at multiple scales | `/references/interactivity-design.md` |

### Tooltip Best Practices
- Show on hover (desktop) and tap (mobile)
- Position to avoid clipping at edges
- Include: data value, label, context (e.g., "15% above average")
- Keep concise — 2–4 lines maximum
- Dismiss on mouse exit or outside tap
- Use a subtle animation (100–200ms fade) for polish

## Scrollytelling Architecture

| Component | Role | Implementation |
|-----------|------|---------------|
| Scroll trigger library | Detect scroll position | Scrollama, GSAP ScrollTrigger, Intersection Observer |
| Sticky graphic container | Visualization stays fixed while text scrolls | `position: sticky; top: 0;` |
| Step text sections | Narrative blocks that trigger vis updates | Semantic HTML sections with data attributes |
| Transition functions | Update visualization per step | D3 transitions, CSS transforms, GSAP |
| Progress indicator | Show reader position in story | Dot navigation or progress bar |

### Scrollytelling Layout Pattern
```
┌──────────────────────────────┐
│  ┌──────────┐  ┌──────────┐ │
│  │ Sticky    │  │ Step 1   │ │
│  │ Graphic   │  │ text...  │ │
│  │ Container │  ├──────────┤ │
│  │           │  │ Step 2   │ │
│  │ (updates  │  │ text...  │ │
│  │  on each  │  ├──────────┤ │
│  │  step)    │  │ Step 3   │ │
│  │           │  │ text...  │ │
│  └──────────┘  └──────────┘ │
└──────────────────────────────┘
```

## Responsive Visualization Strategies

| Screen Size | Strategy | Implementation |
|------------|----------|----------------|
| Desktop (>1024px) | Full visualization with all interactions | Full SVG/Canvas, tooltips on hover |
| Tablet (768–1024px) | Simplified layout, larger touch targets | Reduce data density, larger labels |
| Mobile (<768px) | Small multiples or simplified chart | Swipeable panels, tap interactions |

### Responsive Techniques
- Use `viewBox` on SVG elements for automatic scaling
- Recalculate dimensions on `resize` event (debounced)
- Reduce number of data points on mobile (aggregate to larger buckets)
- Replace hover interactions with tap on touch devices
- Consider small multiples instead of one complex interactive chart
- Hide secondary controls on mobile, show primary interaction only

## Performance Optimization

| Technique | When to Apply | Impact |
|-----------|--------------|--------|
| Use Canvas instead of SVG | >1,000 data points | Major rendering speed improvement |
| Virtual scrolling | Long lists or tables | Only render visible rows |
| Debounce interactions | Resize, scroll, filter | Prevent layout thrash |
| Web Workers | Heavy data processing | Keep UI responsive |
| Lazy load visualizations | Below-the-fold content | Faster initial page load |
| Precompute aggregations | Complex calculations | Instant filter response |

### SVG vs Canvas Decision

| Factor | SVG | Canvas |
|--------|-----|--------|
| Data points | <1,000 | 1,000–100,000+ |
| Interactivity | Built-in DOM events | Manual hit detection |
| Accessibility | Good (DOM elements) | Poor (pixel-based) |
| Animation | CSS/SMIL/JS | RequestAnimationFrame |
| Text rendering | Excellent | Good (manual positioning) |
| Print quality | Perfect (vector) | Depends on resolution |

## Best Practices

- **Progressive disclosure** — show overview first, let users drill into details on demand
- **Annotate insights** — don't just show data; highlight what's interesting and why
- **Design for no-JavaScript fallback** — show a static image or key statistics if JS fails
- **Test on mobile first** — most web traffic is mobile; your visualization must work on small screens
- **Use semantic HTML** — screen readers should convey meaning even without visuals
- **Keep initial load fast** — defer heavy visualizations until the user scrolls to them

## Using the Reference Files

**`/references/javascript-libraries-tools.md`** — Read when selecting or implementing a visualization library. Covers D3.js patterns, Chart.js setup, Plotly configuration, and map libraries with code examples.

**`/references/interactivity-design.md`** — Read when designing user interactions. Covers tooltip patterns, filtering, brushing, linked views, scrollytelling architecture, and responsive techniques.
