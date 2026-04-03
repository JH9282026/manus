# Color System Implementation - Color Palette Design

## Introduction

This reference provides comprehensive guidance on implementing color systems using design tokens, naming conventions, and tooling. Use this when translating color palettes into production-ready code, building token systems for design-to-development handoff, or setting up color management infrastructure for scalable products.

---

## Design Tokens for Color

### What Are Design Tokens?

Design tokens are the single source of truth for design decisions, stored as platform-agnostic data. For color, tokens capture every color value used in a product and assign it a semantic name that communicates intent rather than appearance.

### Token Architecture: Three Levels

A mature color token system uses three tiers:

**Level 1 — Global/Primitive Tokens**
Raw color values with descriptive names. These form your color dictionary.

```json
{
  "color": {
    "blue": {
      "50": { "value": "#EFF6FF" },
      "100": { "value": "#DBEAFE" },
      "200": { "value": "#BFDBFE" },
      "300": { "value": "#93C5FD" },
      "400": { "value": "#60A5FA" },
      "500": { "value": "#3B82F6" },
      "600": { "value": "#2563EB" },
      "700": { "value": "#1D4ED8" },
      "800": { "value": "#1E40AF" },
      "900": { "value": "#1E3A8A" }
    },
    "red": {
      "500": { "value": "#EF4444" },
      "600": { "value": "#DC2626" },
      "700": { "value": "#B91C1C" }
    }
  }
}
```

**Level 2 — Alias/Semantic Tokens**
Map primitives to design intent. These are what components reference.

```json
{
  "color": {
    "primary": { "value": "{color.blue.600}" },
    "primary-hover": { "value": "{color.blue.500}" },
    "primary-active": { "value": "{color.blue.700}" },
    "error": { "value": "{color.red.500}" },
    "error-text": { "value": "{color.red.700}" },
    "text-primary": { "value": "{color.gray.900}" },
    "text-secondary": { "value": "{color.gray.600}" },
    "bg-primary": { "value": "{color.white}" },
    "bg-secondary": { "value": "{color.gray.50}" },
    "border-default": { "value": "{color.gray.200}" }
  }
}
```

**Level 3 — Component Tokens**
Bind semantic tokens to specific component properties.

```json
{
  "button": {
    "primary": {
      "bg": { "value": "{color.primary}" },
      "bg-hover": { "value": "{color.primary-hover}" },
      "text": { "value": "{color.white}" },
      "border": { "value": "transparent" }
    },
    "secondary": {
      "bg": { "value": "{color.white}" },
      "bg-hover": { "value": "{color.primary}" },
      "text": { "value": "{color.primary}" },
      "border": { "value": "{color.primary}" }
    }
  }
}
```

### Why Three Levels?

| Level | Changes When | Example Scenario |
|-------|-------------|------------------|
| Primitive | Brand refresh, color palette overhaul | "We changed our blue from #3B82F6 to #2563EB" |
| Semantic | Design system evolution, role reassignment | "Primary is now purple instead of blue" |
| Component | Component redesign | "Buttons now use a different hover pattern" |

This separation means a brand color change only touches Level 1, automatically propagating through the system.

---

## Naming Conventions

### Naming Strategy Comparison

| Strategy | Example | Pros | Cons |
|----------|---------|------|------|
| Descriptive (color-based) | `blue-500`, `red-600` | Easy to understand, no abstraction | Breaks if brand colors change |
| Semantic (intent-based) | `color-primary`, `color-error` | Resilient to changes, clear purpose | Requires documentation |
| Numbered scale | `color-1`, `color-2` | Simple system | No meaning, hard to remember |
| T-shirt sizing | `color-brand-lg`, `color-brand-sm` | Intuitive sizing | Limited granularity |

**Recommended approach**: Use descriptive names at the primitive level and semantic names at the alias/component level.

### Token Naming Format

Follow a consistent naming pattern:

```
{category}-{property}-{variant}-{state}
```

Examples:
```
color-bg-primary          → Primary background color
color-bg-primary-hover     → Primary background on hover
color-text-primary         → Primary text color
color-text-on-primary      → Text color placed on primary bg
color-border-default       → Default border color
color-border-focus         → Focus state border color
color-icon-primary         → Primary icon color
color-surface-elevated     → Elevated surface (cards, modals)
```

### Dark Mode Token Strategy

Two common approaches:

**Approach 1: Separate token sets** (recommended for major theme differences)
```
light/color-bg-primary: #FFFFFF
dark/color-bg-primary: #1E293B
light/color-text-primary: #0F172A
dark/color-text-primary: #F1F5F9
```

**Approach 2: CSS custom properties with theme class**
```css
:root {
  --color-bg-primary: #FFFFFF;
  --color-text-primary: #0F172A;
}

[data-theme="dark"] {
  --color-bg-primary: #1E293B;
  --color-text-primary: #F1F5F9;
}
```

Approach 2 is simpler for web projects; Approach 1 is better for multi-platform systems using tools like Style Dictionary.

---

## Implementation in Code

### CSS Custom Properties

The most common web implementation:

```css
:root {
  /* Primitives */
  --blue-50: #EFF6FF;
  --blue-500: #3B82F6;
  --blue-600: #2563EB;
  --blue-700: #1D4ED8;
  --gray-50: #F8FAFC;
  --gray-200: #E2E8F0;
  --gray-600: #475569;
  --gray-900: #0F172A;
  --red-500: #EF4444;
  --red-700: #B91C1C;
  --green-500: #22C55E;
  --green-700: #15803D;

  /* Semantic tokens */
  --color-primary: var(--blue-600);
  --color-primary-hover: var(--blue-500);
  --color-primary-active: var(--blue-700);
  --color-bg: var(--white, #FFFFFF);
  --color-bg-secondary: var(--gray-50);
  --color-text: var(--gray-900);
  --color-text-secondary: var(--gray-600);
  --color-border: var(--gray-200);
  --color-error: var(--red-500);
  --color-error-text: var(--red-700);
  --color-success: var(--green-500);
  --color-success-text: var(--green-700);
}
```

### Tailwind CSS Configuration

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: 'var(--color-primary)',
          hover: 'var(--color-primary-hover)',
          active: 'var(--color-primary-active)',
        },
        surface: {
          DEFAULT: 'var(--color-bg)',
          secondary: 'var(--color-bg-secondary)',
        },
        content: {
          DEFAULT: 'var(--color-text)',
          secondary: 'var(--color-text-secondary)',
        },
        semantic: {
          error: 'var(--color-error)',
          success: 'var(--color-success)',
        }
      }
    }
  }
}
```

### JavaScript/TypeScript Token Object

```typescript
export const colors = {
  primary: {
    DEFAULT: '#2563EB',
    hover: '#3B82F6',
    active: '#1D4ED8',
    light: '#EFF6FF',
  },
  neutral: {
    50: '#F8FAFC',
    100: '#F1F5F9',
    200: '#E2E8F0',
    300: '#CBD5E1',
    400: '#94A3B8',
    500: '#64748B',
    600: '#475569',
    700: '#334155',
    800: '#1E293B',
    900: '#0F172A',
  },
  semantic: {
    success: '#22C55E',
    warning: '#F59E0B',
    error: '#EF4444',
    info: '#3B82F6',
  },
} as const;
```

---

## Tooling for Color System Management

### Design-to-Code Pipeline Tools

| Tool | Purpose | Key Feature |
|------|---------|-------------|
| **Style Dictionary** | Token transformation | Converts tokens to CSS, iOS, Android, and more |
| **Tokens Studio** (Figma) | Token management in design | Syncs Figma styles with JSON tokens |
| **Figma Variables** | Native Figma token system | Built-in theming, modes, and scoping |
| **Supernova** | Design system platform | Full pipeline from design to code |
| **Specify** | Token delivery | Automated token distribution to repos |
| **Cobalt UI** | Token build tool | W3C Design Token Format support |

### Color Generation and Palette Tools

| Tool | Use Case | Output |
|------|----------|--------|
| **Coolors** | Quick palette generation | HEX, RGB, export to code |
| **Realtime Colors** | Preview palette on a live UI mockup | Visual preview, CSS export |
| **Leonardo** (Adobe) | Contrast-based color generation | Generates scales that meet specific contrast targets |
| **Huetone** | Perceptually uniform palette building | OKLCH-based scales |
| **Radix Colors** | Pre-built accessible scales | CSS, Tailwind config |
| **Open Color** | Open-source color palette | JSON, CSS, Sass, Less |

---

## Color Scale Generation Methods

### HSL Lightness Stepping

The simplest approach — adjust lightness in even steps:

```
Base: hsl(220, 70%, 50%)  → shade-500
50:  hsl(220, 70%, 97%)
100: hsl(220, 70%, 93%)
200: hsl(220, 70%, 85%)
300: hsl(220, 70%, 72%)
400: hsl(220, 70%, 60%)
500: hsl(220, 70%, 50%)  ← base
600: hsl(220, 70%, 42%)
700: hsl(220, 70%, 35%)
800: hsl(220, 70%, 25%)
900: hsl(220, 70%, 15%)
```

**Limitation**: HSL produces perceptually uneven steps — some jumps look bigger than others.

### OKLCH (Recommended for Perceptual Uniformity)

OKLCH is a perceptually uniform color space that produces visually even shade ramps:

```css
/* Modern CSS supports OKLCH natively */
--blue-50: oklch(0.97 0.02 250);
--blue-100: oklch(0.93 0.04 250);
--blue-200: oklch(0.85 0.08 250);
--blue-300: oklch(0.75 0.12 250);
--blue-400: oklch(0.65 0.16 250);
--blue-500: oklch(0.55 0.20 250);
--blue-600: oklch(0.48 0.18 250);
--blue-700: oklch(0.40 0.16 250);
--blue-800: oklch(0.32 0.12 250);
--blue-900: oklch(0.24 0.08 250);
```

**Advantages of OKLCH**:
- Perceptually uniform lightness
- Chroma (saturation) control independent of lightness
- Hue stability across the scale
- Native CSS support in modern browsers

---

## Governance and Maintenance

### Color Audit Checklist

Regularly audit your color system:

```
□ All tokens map to the defined palette (no rogue hex values)
□ Semantic tokens are used in components (not primitives directly)
□ Dark mode tokens independently verified for contrast
□ No duplicate or near-duplicate colors in the system
□ Unused colors identified and removed
□ New colors go through approval process
□ Token documentation is current
□ Design file and code tokens are in sync
```

### Versioning Strategy

Version your color tokens alongside your design system:

- **Patch** (1.0.1): Fix contrast issues, adjust specific shade values
- **Minor** (1.1.0): Add new semantic tokens, introduce new color roles
- **Major** (2.0.0): Rename token structure, change brand colors, breaking changes

### Documentation Requirements

Every color token should be documented with:

1. **Token name**: The semantic name used in code
2. **Value**: Current hex/RGB value
3. **Usage**: Where and how to use this token
4. **Contrast info**: Which backgrounds/foregrounds it pairs with safely
5. **Do/Don't examples**: Visual examples of correct and incorrect usage

---

## Key Takeaways

1. Use three-tier token architecture: primitive → semantic → component
2. Semantic names create resilient systems that survive brand changes
3. OKLCH produces more perceptually uniform color scales than HSL
4. Style Dictionary is the industry standard for multi-platform token distribution
5. Automate design-to-code sync with Tokens Studio or Figma Variables
6. Audit color systems regularly to prevent token sprawl
7. Document every token with usage guidelines and contrast pairing information
