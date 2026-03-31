# Web Typography and Responsive Design

## Overview

Responsive typography ensures text adapts seamlessly to various device screens, maintaining readability and visual appeal across different resolutions and sizes. This involves fluid scaling, appropriate breakpoints, and performance optimization.

## Core Principles

### 1. Fluid Typography

Fluid typography uses relative units and CSS functions to create scalable fonts that resize proportionally based on viewport size.

#### Relative Units

**rem (Root Em)**
- Relative to root font size
- Consistent scaling
- Preferred for most typography

**em**
- Relative to parent font size
- Useful for component-based scaling
- Can compound (be careful)

**Viewport Units**
- `vw`: Viewport width
- `vh`: Viewport height
- `vmin`: Smaller of vw or vh
- `vmax`: Larger of vw or vh

#### CSS clamp() Function

```css
/* Syntax: clamp(minimum, preferred, maximum) */
font-size: clamp(1rem, 2.5vw, 2rem);

/* Practical examples */
h1 {
  font-size: clamp(2rem, 5vw + 1rem, 4rem);
}

body {
  font-size: clamp(1rem, 0.9rem + 0.5vw, 1.25rem);
}
```

**Benefits**:
- Prevents text from becoming too small or large
- Smooth scaling across viewports
- Single declaration replaces multiple media queries

### 2. Responsive Type Scale

Adjust type scale based on screen size:

```css
/* Mobile-first approach */
:root {
  --font-size-base: 1rem;
  --font-size-h1: 2rem;
  --font-size-h2: 1.5rem;
  --font-size-h3: 1.25rem;
}

/* Tablet */
@media (min-width: 768px) {
  :root {
    --font-size-h1: 2.5rem;
    --font-size-h2: 2rem;
    --font-size-h3: 1.5rem;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  :root {
    --font-size-h1: 3rem;
    --font-size-h2: 2.25rem;
    --font-size-h3: 1.75rem;
  }
}
```

### 3. Line Length Control

Optimal line length: 45-75 characters (66 ideal)

```css
.content {
  max-inline-size: 65ch; /* Character units */
  margin-inline: auto;
}

/* Alternative with max-width */
.content {
  max-width: 700px;
  margin: 0 auto;
}
```

### 4. Responsive Line Height

```css
body {
  font-size: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
  line-height: 1.6; /* Unitless - scales with font-size */
}

h1 {
  font-size: clamp(2rem, 5vw, 3.5rem);
  line-height: 1.2; /* Tighter for headings */
}
```

## Performance Optimization

### 1. Font Loading Strategies

#### font-display Property

```css
@font-face {
  font-family: 'CustomFont';
  src: url('custom-font.woff2') format('woff2');
  font-display: swap; /* Show fallback immediately, swap when loaded */
}
```

**Options**:
- `auto`: Browser default
- `block`: Hide text briefly, then show custom font
- `swap`: Show fallback immediately, swap when loaded (recommended)
- `fallback`: Brief block period, swap if loaded quickly
- `optional`: Use custom font only if cached

#### Preloading Fonts

```html
<link rel="preload" 
      href="/fonts/custom-font.woff2" 
      as="font" 
      type="font/woff2" 
      crossorigin>
```

### 2. Variable Fonts

Single file containing multiple styles:

```css
@font-face {
  font-family: 'InterVariable';
  src: url('Inter-Variable.woff2') format('woff2');
  font-weight: 100 900; /* Weight range */
  font-display: swap;
}

h1 {
  font-family: 'InterVariable';
  font-weight: 700;
}

body {
  font-family: 'InterVariable';
  font-weight: 400;
}
```

**Benefits**:
- Reduced HTTP requests
- Smaller total file size
- Smooth weight transitions
- Better performance

### 3. Font Subsetting

Include only needed characters:

```css
/* Google Fonts with subset */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&subset=latin&display=swap');
```

### 4. System Font Stack

Fast, no download required:

```css
body {
  font-family: 
    -apple-system, 
    BlinkMacSystemFont, 
    'Segoe UI', 
    Roboto, 
    'Helvetica Neue', 
    Arial, 
    sans-serif;
}
```

## Responsive Typography Patterns

### Mobile-First Approach

```css
/* Base (Mobile) */
body {
  font-size: 1rem;
  line-height: 1.6;
}

h1 {
  font-size: 2rem;
  line-height: 1.2;
  margin-bottom: 1rem;
}

/* Tablet */
@media (min-width: 768px) {
  body {
    font-size: 1.125rem;
  }
  
  h1 {
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  body {
    font-size: 1.25rem;
  }
  
  h1 {
    font-size: 3rem;
    margin-bottom: 2rem;
  }
}
```

### Container Queries (Modern)

```css
.card {
  container-type: inline-size;
}

.card h2 {
  font-size: 1.5rem;
}

@container (min-width: 400px) {
  .card h2 {
    font-size: 2rem;
  }
}
```

## Best Practices

1. **Use rem for font sizes**: Respects user preferences
2. **Set base font size on html**: Typically 16px
3. **Use unitless line-height**: Scales proportionally
4. **Limit line length**: 45-75 characters
5. **Test on real devices**: Emulators aren't perfect
6. **Consider reading distance**: Mobile vs desktop
7. **Maintain hierarchy**: Across all breakpoints
8. **Optimize font loading**: Use font-display: swap
9. **Prefer system fonts or variable fonts**: For performance
10. **Use clamp() for fluid scaling**: Smooth transitions

## Common Breakpoints

```css
/* Mobile: < 768px (default) */
/* Tablet: 768px - 1023px */
@media (min-width: 768px) { }

/* Desktop: 1024px - 1439px */
@media (min-width: 1024px) { }

/* Large Desktop: 1440px+ */
@media (min-width: 1440px) { }
```

## Testing Checklist

- [ ] Text readable at 320px width (smallest mobile)
- [ ] Text readable at 1920px+ width (large desktop)
- [ ] Line length appropriate at all sizes
- [ ] Hierarchy clear at all breakpoints
- [ ] No horizontal scrolling
- [ ] Fonts load quickly
- [ ] Fallback fonts acceptable
- [ ] Text scales with browser zoom (200%)
- [ ] Contrast ratios meet WCAG standards

## Conclusion

Responsive typography is essential for modern web design. By using fluid scaling techniques, optimizing font loading, and testing across devices, you can create text that is readable, performant, and visually appealing on any screen size.
