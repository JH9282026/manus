# Responsive Design & Breakpoints

Comprehensive guide to responsive design implementation, adaptive approaches, and breakpoint strategies.

---

## Responsive Design Fundamentals

Responsive design uses fluid grids, flexible images, and CSS media queries to create layouts that adapt smoothly to any screen size.

### Key Components

1. **Fluid Grids** — Percentage-based layouts that flow naturally
2. **Flexible Images** — Scale within containers using `max-width: 100%`
3. **Media Queries** — CSS rules based on viewport characteristics
4. **One Codebase** — Single HTML/CSS serves all devices

---

## Fluid Grid System

```css
.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

.row {
  display: flex;
  flex-wrap: wrap;
  margin: 0 -15px;
}

.column {
  width: 100%; /* Mobile default */
  padding: 0 15px;
}

@media (min-width: 768px) {
  .column-half { width: 50%; }
  .column-third { width: 33.33%; }
  .column-quarter { width: 25%; }
}
```

---

## Flexible Images

```css
/* Basic responsive images */
img {
  max-width: 100%;
  height: auto;
}

/* Responsive background images */
.hero {
  background-image: url('small.jpg');
  background-size: cover;
}

@media (min-width: 768px) {
  .hero {
    background-image: url('medium.jpg');
  }
}

@media (min-width: 1200px) {
  .hero {
    background-image: url('large.jpg');
  }
}
```

### HTML Responsive Images

```html
<!-- Using srcset and sizes -->
<img srcset="small.jpg 480w,
             medium.jpg 768w,
             large.jpg 1200w"
     sizes="(max-width: 480px) 100vw,
            (max-width: 768px) 50vw,
            33vw"
     src="medium.jpg"
     alt="Responsive image">

<!-- Using picture element -->
<picture>
  <source type="image/webp" 
          srcset="image.webp 1x, image@2x.webp 2x">
  <source type="image/jpeg" 
          srcset="image.jpg 1x, image@2x.jpg 2x">
  <img src="image.jpg" 
       alt="Description"
       loading="lazy"
       decoding="async">
</picture>
```

---

## Common Breakpoints

| Category | Width | Typical Devices |
|----------|-------|----------------|
| Small Mobile | 320-375px | iPhone SE, small Android |
| Mobile | 376-480px | iPhone, standard Android |
| Tablet | 481-768px | iPad Mini, portrait tablets |
| Large Tablet | 769-1024px | iPad, landscape tablets |
| Desktop | 1025-1200px | Laptops, small monitors |
| Large Desktop | 1201px+ | Large monitors, TVs |

---

## Mobile-First Media Queries

```css
/* Base styles for mobile (no media query needed) */
.container {
  padding: 16px;
  font-size: 16px;
}

.sidebar {
  display: none; /* Hidden on mobile */
}

.nav {
  position: fixed;
  bottom: 0;
  width: 100%;
}

/* Tablet and up (min-width: 768px) */
@media (min-width: 768px) {
  .container {
    padding: 24px;
    font-size: 18px;
  }
  
  .sidebar {
    display: block;
    width: 250px;
  }
  
  .nav {
    position: static;
    bottom: auto;
  }
}

/* Desktop and up (min-width: 1024px) */
@media (min-width: 1024px) {
  .container {
    padding: 32px;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .sidebar {
    width: 300px;
  }
}

/* Large desktop (min-width: 1200px) */
@media (min-width: 1200px) {
  .container {
    max-width: 1400px;
  }
}
```

---

## Desktop-First Media Queries (for reference)

```css
/* Base styles for desktop */
.container {
  max-width: 1200px;
  padding: 32px;
}

/* Tablet and down */
@media (max-width: 1024px) {
  .container {
    padding: 24px;
  }
}

/* Mobile */
@media (max-width: 768px) {
  .container {
    padding: 16px;
    max-width: 100%;
  }
}
```

---

## Responsive vs Adaptive Design

### Responsive Design

| Aspect | Description |
|--------|-------------|
| Approach | Fluid, continuous adaptation |
| Breakpoints | Content-based, flexible |
| Codebase | Single HTML/CSS |
| Transitions | Smooth between sizes |
| Maintenance | Easier, one codebase |

### Adaptive Design

| Aspect | Description |
|--------|-------------|
| Approach | Fixed layouts per breakpoint |
| Breakpoints | Device-specific |
| Codebase | May have multiple templates |
| Transitions | Distinct "snaps" at breakpoints |
| Control | More precise per device |

### When to Use Each

**Choose Responsive**:
- New projects from scratch
- Budget constraints (single codebase)
- Consistent content across devices
- Strong CSS team skills

**Choose Adaptive**:
- Vastly different experiences needed per device
- Legacy system updates
- Critical device-specific optimizations
- Performance concerns for specific devices

**Hybrid Approach**: Most modern projects combine both—responsive layouts with adaptive components for specific functionality.

---

## Breakpoint Best Practices

### Content-Based Breakpoints

Let content dictate breakpoints rather than specific devices. When content becomes uncomfortable, add a breakpoint.

```css
/* Based on content, not devices */
.article-grid {
  grid-template-columns: 1fr;
}

/* When two columns fit comfortably */
@media (min-width: 600px) {
  .article-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* When three columns fit */
@media (min-width: 900px) {
  .article-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

### Testing Breakpoints

- Test at breakpoint boundaries (767px, 768px, 769px)
- Test common device widths
- Test both portrait and landscape orientations
- Use browser DevTools device mode
- Test on actual devices when possible

---

## Modern CSS Layout Techniques

### CSS Grid

```css
.grid-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 768px) {
  .grid-container {
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
  }
}

@media (min-width: 1024px) {
  .grid-container {
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
  }
}
```

### CSS Flexbox

```css
.flex-container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.flex-item {
  flex: 1 1 100%; /* Full width on mobile */
}

@media (min-width: 768px) {
  .flex-item {
    flex: 1 1 calc(50% - 8px); /* Two columns */
  }
}

@media (min-width: 1024px) {
  .flex-item {
    flex: 1 1 calc(33.33% - 11px); /* Three columns */
  }
}
```

### Container Queries (Modern)

```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card {
    display: flex;
    flex-direction: row;
  }
}

@container (min-width: 600px) {
  .card {
    padding: 2rem;
  }
}
```

---

## Responsive Typography

### Fluid Typography

```css
/* Using clamp() for fluid sizing */
html {
  font-size: clamp(14px, 2.5vw, 18px);
}

h1 {
  font-size: clamp(1.75rem, 5vw, 3rem);
}

h2 {
  font-size: clamp(1.5rem, 4vw, 2.25rem);
}
```

### Media Query Typography

```css
body {
  font-size: 16px;
  line-height: 1.5;
}

@media (min-width: 768px) {
  body {
    font-size: 17px;
    line-height: 1.6;
  }
}

@media (min-width: 1200px) {
  body {
    font-size: 18px;
  }
}
```
