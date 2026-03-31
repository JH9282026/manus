# Modern CSS Techniques and Best Practices

## Advanced Layout Systems

### CSS Grid

CSS Grid is a two-dimensional layout system for creating complex, responsive layouts.

#### Basic Grid Setup

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto;
  gap: 1.5rem;
}

/* Named grid areas */
.layout {
  display: grid;
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "footer footer footer";
  grid-template-columns: 250px 1fr 1fr;
  grid-template-rows: auto 1fr auto;
  gap: 1rem;
  min-height: 100vh;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }
```

#### Advanced Grid Patterns

**Auto-fit and Auto-fill**
```css
/* Auto-fit: Collapses empty tracks */
.grid-auto-fit {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

/* Auto-fill: Maintains empty tracks */
.grid-auto-fill {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}
```

**Masonry-style Layout**
```css
.masonry {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-auto-rows: 10px;
  gap: 1rem;
}

.masonry-item {
  grid-row-end: span var(--row-span);
}
```

```javascript
// Calculate row span based on content height
const items = document.querySelectorAll('.masonry-item');
const rowHeight = 10;

items.forEach(item => {
  const height = item.offsetHeight;
  const rowSpan = Math.ceil(height / rowHeight);
  item.style.setProperty('--row-span', rowSpan);
});
```

**Grid with Subgrid**
```css
.parent-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.child-grid {
  display: grid;
  grid-template-columns: subgrid;
  grid-column: span 3;
}
```

### Flexbox Advanced Patterns

#### Equal Height Columns

```css
.flex-container {
  display: flex;
  gap: 1rem;
}

.flex-item {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.flex-item-content {
  flex: 1;
}

.flex-item-footer {
  margin-top: auto;
}
```

#### Holy Grail Layout

```css
.holy-grail {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.holy-grail-header,
.holy-grail-footer {
  flex: none;
}

.holy-grail-body {
  display: flex;
  flex: 1;
}

.holy-grail-content {
  flex: 1;
  order: 2;
}

.holy-grail-nav {
  flex: 0 0 200px;
  order: 1;
}

.holy-grail-aside {
  flex: 0 0 200px;
  order: 3;
}

@media (max-width: 768px) {
  .holy-grail-body {
    flex-direction: column;
  }
  
  .holy-grail-nav,
  .holy-grail-aside {
    flex: none;
  }
}
```

## Modern CSS Features

### CSS Custom Properties (Variables)

#### Dynamic Theming

```css
:root {
  /* Light theme (default) */
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --text-primary: #212529;
  --text-secondary: #6c757d;
  --accent: #007bff;
}

[data-theme="dark"] {
  --bg-primary: #212529;
  --bg-secondary: #343a40;
  --text-primary: #f8f9fa;
  --text-secondary: #adb5bd;
  --accent: #0d6efd;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  transition: background-color 0.3s, color 0.3s;
}

.card {
  background-color: var(--bg-secondary);
  color: var(--text-primary);
}

.button {
  background-color: var(--accent);
  color: white;
}
```

```javascript
// Toggle theme
const toggleTheme = () => {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
};

// Load saved theme
const savedTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', savedTheme);
```

#### Responsive Variables

```css
:root {
  --spacing: 1rem;
  --font-size: 1rem;
}

@media (min-width: 768px) {
  :root {
    --spacing: 1.5rem;
    --font-size: 1.125rem;
  }
}

@media (min-width: 1024px) {
  :root {
    --spacing: 2rem;
    --font-size: 1.25rem;
  }
}

.section {
  padding: var(--spacing);
  font-size: var(--font-size);
}
```

### Container Queries

```css
.card-container {
  container-type: inline-size;
  container-name: card;
}

.card {
  padding: 1rem;
}

.card-title {
  font-size: 1.25rem;
}

/* When container is at least 400px wide */
@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 150px 1fr;
    gap: 1rem;
  }
  
  .card-title {
    font-size: 1.5rem;
  }
}

/* When container is at least 600px wide */
@container card (min-width: 600px) {
  .card {
    grid-template-columns: 200px 1fr;
  }
  
  .card-title {
    font-size: 2rem;
  }
}
```

### CSS Nesting

```css
/* Native CSS nesting (modern browsers) */
.card {
  padding: 1rem;
  background: white;
  border-radius: 8px;
  
  & .card-header {
    margin-bottom: 1rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #e0e0e0;
    
    & .card-title {
      font-size: 1.5rem;
      font-weight: 600;
    }
  }
  
  & .card-body {
    line-height: 1.6;
  }
  
  &:hover {
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  @media (min-width: 768px) {
    padding: 1.5rem;
  }
}
```

### CSS Layers (Cascade Layers)

```css
/* Define layer order */
@layer reset, base, components, utilities;

/* Reset layer */
@layer reset {
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
}

/* Base layer */
@layer base {
  body {
    font-family: system-ui, sans-serif;
    line-height: 1.6;
  }
}

/* Components layer */
@layer components {
  .button {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
}

/* Utilities layer (highest priority) */
@layer utilities {
  .text-center {
    text-align: center;
  }
  
  .mt-4 {
    margin-top: 1rem;
  }
}
```

## Advanced Styling Techniques

### Clamp, Min, Max Functions

```css
/* Fluid typography */
h1 {
  font-size: clamp(2rem, 5vw + 1rem, 4rem);
  /* min: 2rem, preferred: 5vw + 1rem, max: 4rem */
}

/* Responsive spacing */
.section {
  padding: clamp(1rem, 5vw, 3rem);
}

/* Flexible widths */
.container {
  width: min(90%, 1200px);
  margin: 0 auto;
}

.sidebar {
  width: max(200px, 20%);
}
```

### Aspect Ratio

```css
/* Modern aspect ratio */
.video-container {
  aspect-ratio: 16 / 9;
  width: 100%;
}

.square {
  aspect-ratio: 1;
}

.portrait {
  aspect-ratio: 3 / 4;
}

/* Fallback for older browsers */
.video-container-fallback {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 */
}

.video-container-fallback iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
```

### Logical Properties

```css
/* Traditional */
.element {
  margin-left: 1rem;
  margin-right: 1rem;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

/* Logical properties (RTL/LTR aware) */
.element {
  margin-inline: 1rem;      /* left and right */
  padding-block: 0.5rem;    /* top and bottom */
}

.element {
  margin-inline-start: 1rem;  /* left in LTR, right in RTL */
  margin-inline-end: 1rem;    /* right in LTR, left in RTL */
  margin-block-start: 0.5rem; /* top */
  margin-block-end: 0.5rem;   /* bottom */
}

/* Border */
.element {
  border-inline-start: 2px solid blue;
  border-block-end: 1px solid gray;
}
```

### Scroll Snap

```css
.scroll-container {
  scroll-snap-type: x mandatory;
  overflow-x: scroll;
  display: flex;
  gap: 1rem;
}

.scroll-item {
  scroll-snap-align: start;
  flex: 0 0 100%;
}

/* Vertical scroll snap */
.vertical-scroll {
  scroll-snap-type: y mandatory;
  overflow-y: scroll;
  height: 100vh;
}

.section {
  scroll-snap-align: start;
  height: 100vh;
}

/* Scroll padding */
.scroll-container {
  scroll-padding: 1rem;
}
```

### Smooth Scrolling

```css
html {
  scroll-behavior: smooth;
}

/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }
}
```

## Animation and Transitions

### CSS Transitions

```css
.button {
  background-color: #007bff;
  color: white;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.button:hover {
  background-color: #0056b3;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Multiple properties with different timings */
.card {
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease,
    background-color 0.2s ease;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  background-color: #f8f9fa;
}
```

### CSS Animations

```css
/* Fade in animation */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-in {
  animation: fadeIn 0.6s ease-out;
}

/* Slide in from left */
@keyframes slideInLeft {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.slide-in-left {
  animation: slideInLeft 0.5s ease-out;
}

/* Pulse animation */
@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}

.pulse {
  animation: pulse 2s ease-in-out infinite;
}

/* Loading spinner */
@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #007bff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
```

### View Transitions API

```css
/* Enable view transitions */
@view-transition {
  navigation: auto;
}

/* Customize transition */
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 0.5s;
}

/* Fade transition */
::view-transition-old(root) {
  animation-name: fade-out;
}

::view-transition-new(root) {
  animation-name: fade-in;
}

@keyframes fade-out {
  to { opacity: 0; }
}

@keyframes fade-in {
  from { opacity: 0; }
}
```

```javascript
// Trigger view transition
if (document.startViewTransition) {
  document.startViewTransition(() => {
    // Update DOM
    updateContent();
  });
} else {
  // Fallback for browsers without support
  updateContent();
}
```

## Performance Optimization

### CSS Containment

```css
.card {
  contain: layout style paint;
  /* Isolates element for better performance */
}

.sidebar {
  contain: size layout;
  /* Size won't affect other elements */
}
```

### Content Visibility

```css
.off-screen-content {
  content-visibility: auto;
  /* Browser skips rendering until needed */
}

.hidden-section {
  content-visibility: hidden;
  /* Similar to display: none but maintains layout */
}
```

### Will-Change

```css
/* Hint browser about upcoming changes */
.animated-element {
  will-change: transform, opacity;
}

/* Remove after animation */
.animated-element.animation-complete {
  will-change: auto;
}
```

## Best Practices

### BEM Methodology

```css
/* Block */
.card { }

/* Element */
.card__header { }
.card__body { }
.card__footer { }

/* Modifier */
.card--featured { }
.card--large { }
.card__header--dark { }
```

### Utility-First CSS

```css
/* Utility classes */
.flex { display: flex; }
.flex-col { flex-direction: column; }
.items-center { align-items: center; }
.justify-between { justify-content: space-between; }
.gap-4 { gap: 1rem; }
.p-4 { padding: 1rem; }
.mt-4 { margin-top: 1rem; }
.text-center { text-align: center; }
.font-bold { font-weight: 700; }
.rounded { border-radius: 0.25rem; }
.shadow { box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); }
```

### CSS Organization

```css
/* 1. Custom Properties */
:root {
  --color-primary: #007bff;
}

/* 2. Reset/Normalize */
* {
  box-sizing: border-box;
}

/* 3. Base Styles */
body {
  font-family: system-ui, sans-serif;
}

/* 4. Layout */
.container { }
.grid { }

/* 5. Components */
.button { }
.card { }

/* 6. Utilities */
.text-center { }
.mt-4 { }

/* 7. Media Queries */
@media (min-width: 768px) { }
```

## Conclusion

Modern CSS provides powerful tools for creating sophisticated, performant, and maintainable stylesheets. Key techniques include:

1. **Advanced Layouts**: Grid and Flexbox for complex designs
2. **Custom Properties**: Dynamic theming and responsive values
3. **Modern Features**: Container queries, nesting, layers
4. **Responsive Design**: Fluid typography, logical properties
5. **Animations**: Smooth transitions and engaging effects
6. **Performance**: Containment, content visibility, optimization
7. **Organization**: BEM, utility-first, structured CSS

Staying current with CSS features enables developers to build better web experiences with less code and better performance.
