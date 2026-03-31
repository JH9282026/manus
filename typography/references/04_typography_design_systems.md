# Typography in Design Systems

## Overview

Typography design systems provide consistent, scalable typographic guidelines across products and platforms. They establish rules, tokens, and components that ensure visual harmony and maintainability.

## Type System Components

### 1. Type Scale

Harmonious progression of font sizes:

**Modular Scale Ratios**:
- Minor Second: 1.067
- Major Second: 1.125
- Minor Third: 1.200
- Major Third: 1.250
- Perfect Fourth: 1.333
- Perfect Fifth: 1.500
- Golden Ratio: 1.618

**Example Scale (Major Third - 1.25)**:
```
Base: 16px
Level 1: 20px (16 × 1.25)
Level 2: 25px (20 × 1.25)
Level 3: 31px (25 × 1.25)
Level 4: 39px (31 × 1.25)
Level 5: 49px (39 × 1.25)
```

### 2. Design Tokens

**Primitive Tokens** (foundational values):
```css
:root {
  /* Font Families */
  --font-family-sans: 'Inter', system-ui, sans-serif;
  --font-family-serif: 'Merriweather', Georgia, serif;
  --font-family-mono: 'Fira Code', 'Courier New', monospace;
  
  /* Font Sizes */
  --font-size-xs: 0.75rem;    /* 12px */
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-base: 1rem;     /* 16px */
  --font-size-lg: 1.125rem;   /* 18px */
  --font-size-xl: 1.25rem;    /* 20px */
  --font-size-2xl: 1.5rem;    /* 24px */
  --font-size-3xl: 1.875rem;  /* 30px */
  --font-size-4xl: 2.25rem;   /* 36px */
  --font-size-5xl: 3rem;      /* 48px */
  
  /* Font Weights */
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  /* Line Heights */
  --line-height-tight: 1.25;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.75;
  
  /* Letter Spacing */
  --letter-spacing-tight: -0.02em;
  --letter-spacing-normal: 0;
  --letter-spacing-wide: 0.05em;
}
```

**Semantic Tokens** (contextual usage):
```css
:root {
  /* Headings */
  --heading-1-size: var(--font-size-5xl);
  --heading-1-weight: var(--font-weight-bold);
  --heading-1-line-height: var(--line-height-tight);
  
  --heading-2-size: var(--font-size-4xl);
  --heading-2-weight: var(--font-weight-semibold);
  --heading-2-line-height: var(--line-height-tight);
  
  /* Body */
  --body-size: var(--font-size-base);
  --body-weight: var(--font-weight-normal);
  --body-line-height: var(--line-height-normal);
  
  /* Small */
  --small-size: var(--font-size-sm);
  --small-weight: var(--font-weight-normal);
  --small-line-height: var(--line-height-normal);
}
```

### 3. Type Styles

Predefined combinations of properties:

```css
.heading-1 {
  font-family: var(--font-family-sans);
  font-size: var(--heading-1-size);
  font-weight: var(--heading-1-weight);
  line-height: var(--heading-1-line-height);
  letter-spacing: var(--letter-spacing-tight);
}

.body-text {
  font-family: var(--font-family-sans);
  font-size: var(--body-size);
  font-weight: var(--body-weight);
  line-height: var(--body-line-height);
  letter-spacing: var(--letter-spacing-normal);
}

.caption {
  font-family: var(--font-family-sans);
  font-size: var(--small-size);
  font-weight: var(--font-weight-normal);
  line-height: var(--line-height-normal);
  color: var(--color-text-secondary);
}
```

## Variable Fonts in Design Systems

### Benefits

1. **Performance**: Single file for all weights/widths
2. **Flexibility**: Continuous adjustment of properties
3. **Consistency**: Unified font family
4. **File Size**: Smaller than multiple static fonts

### Implementation

```css
@font-face {
  font-family: 'InterVariable';
  src: url('/fonts/Inter-Variable.woff2') format('woff2');
  font-weight: 100 900;
  font-stretch: 75% 125%;
  font-display: swap;
}

:root {
  --font-family-primary: 'InterVariable', sans-serif;
}

/* Use with font-variation-settings for custom axes */
.custom-weight {
  font-family: var(--font-family-primary);
  font-variation-settings: 'wght' 450, 'wdth' 100;
}
```

### Registered Axes

- **wght** (Weight): 100-900
- **wdth** (Width): 50-200 (percentage)
- **slnt** (Slant): -10 to 0 (degrees)
- **ital** (Italic): 0 or 1
- **opsz** (Optical Size): 6-72 (points)

## Responsive Typography System

### Breakpoint-Based Scaling

```css
:root {
  /* Mobile */
  --heading-1: 2rem;
  --heading-2: 1.5rem;
  --body: 1rem;
}

@media (min-width: 768px) {
  :root {
    /* Tablet */
    --heading-1: 2.5rem;
    --heading-2: 2rem;
    --body: 1.125rem;
  }
}

@media (min-width: 1024px) {
  :root {
    /* Desktop */
    --heading-1: 3rem;
    --heading-2: 2.25rem;
    --body: 1.125rem;
  }
}
```

### Fluid Typography

```css
:root {
  --fluid-min-width: 320;
  --fluid-max-width: 1140;
  
  --fluid-screen: 100vw;
  --fluid-bp: calc(
    (var(--fluid-screen) - var(--fluid-min-width) / 16 * 1rem) /
    (var(--fluid-max-width) - var(--fluid-min-width))
  );
}

h1 {
  font-size: clamp(2rem, 4vw + 1rem, 4rem);
}

body {
  font-size: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
}
```

## Component Typography

### Button Typography

```css
.button {
  font-family: var(--font-family-sans);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
  letter-spacing: 0.02em;
  text-transform: none;
}

.button--small {
  font-size: var(--font-size-sm);
}

.button--large {
  font-size: var(--font-size-lg);
}
```

### Form Typography

```css
.form-label {
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  line-height: var(--line-height-normal);
  margin-bottom: 0.5rem;
}

.form-input {
  font-family: var(--font-family-sans);
  font-size: var(--font-size-base);
  line-height: var(--line-height-normal);
}

.form-help-text {
  font-size: var(--font-size-xs);
  color: var(--color-text-secondary);
  margin-top: 0.25rem;
}
```

## Documentation

### Type Specimen

Document all type styles with examples:

```markdown
# Heading 1
Font: Inter Bold
Size: 48px / 3rem
Line Height: 1.2
Weight: 700
Use: Page titles, hero headings

# Heading 2
Font: Inter Semibold
Size: 36px / 2.25rem
Line Height: 1.3
Weight: 600
Use: Section headings

Body Text
Font: Inter Regular
Size: 16px / 1rem
Line Height: 1.6
Weight: 400
Use: Main content, paragraphs
```

### Usage Guidelines

```markdown
## Typography Guidelines

### Headings
- Use semantic HTML (h1-h6)
- Only one h1 per page
- Don't skip heading levels
- Keep headings concise

### Body Text
- Minimum 16px font size
- Line length 50-75 characters
- Line height 1.5-1.6
- Left-aligned for readability

### Emphasis
- Use <strong> for importance
- Use <em> for stress emphasis
- Avoid all caps for long text
- Use color sparingly
```

## Tooling and Automation

### Figma Variables

```javascript
// Export design tokens from Figma
{
  "typography": {
    "heading-1": {
      "fontFamily": "Inter",
      "fontSize": "48px",
      "fontWeight": 700,
      "lineHeight": "1.2"
    }
  }
}
```

### Style Dictionary

```javascript
// tokens.json
{
  "size": {
    "font": {
      "base": { "value": "16" },
      "large": { "value": "20" }
    }
  }
}

// Generates CSS, SCSS, JS, etc.
```

## Best Practices

1. **Start with Base Size**: Define body text first
2. **Use Modular Scale**: Maintain mathematical harmony
3. **Limit Font Families**: 2-3 maximum
4. **Document Everything**: Clear usage guidelines
5. **Test Across Platforms**: Ensure consistency
6. **Version Control**: Track changes to type system
7. **Provide Examples**: Show real-world usage
8. **Consider Accessibility**: Meet WCAG standards
9. **Plan for Growth**: Scalable token structure
10. **Automate**: Use tools for consistency

## Conclusion

A well-designed typography system provides consistency, scalability, and maintainability across products. By establishing clear tokens, scales, and guidelines, teams can work efficiently while ensuring high-quality, accessible typography.
