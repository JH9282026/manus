# Type Scale and Hierarchy Systems - Typography Design System

## Introduction

This reference provides comprehensive guidance on creating typographic scales and establishing visual hierarchy through systematic sizing, weight, and spacing decisions. Use this when building type systems from scratch, selecting scale ratios, defining heading levels, or ensuring consistent typographic hierarchy across a product.

---

## Understanding Type Scales

### What Is a Type Scale?

A type scale is a set of font sizes derived from a mathematical ratio, creating harmonious proportional relationships between text sizes. Rather than choosing arbitrary pixel values, scales use multipliers that produce naturally pleasing progressions.

### The Mathematics of Scales

A type scale works by multiplying a base size by a ratio repeatedly:

```
Size = Base × Ratio^n
Where:
  Base = root font size (typically 16px)
  Ratio = scale factor (e.g., 1.25)
  n = step number (0 = base, 1 = one step up, -1 = one step down)
```

Example with base 16px and ratio 1.25 (Major Third):
```
Step -2: 16 × 1.25^-2 = 10.24px  → round to 10px
Step -1: 16 × 1.25^-1 = 12.80px  → round to 13px
Step  0: 16 × 1.25^0  = 16.00px  (base)
Step  1: 16 × 1.25^1  = 20.00px
Step  2: 16 × 1.25^2  = 25.00px  → round to 25px
Step  3: 16 × 1.25^3  = 31.25px  → round to 31px
Step  4: 16 × 1.25^4  = 39.06px  → round to 39px
Step  5: 16 × 1.25^5  = 48.83px  → round to 49px
```

### Common Scale Ratios

| Ratio | Name | Character | Best For |
|-------|------|-----------|----------|
| 1.067 | Minor Second | Minimal contrast | Dense data UIs, small screens |
| 1.125 | Major Second | Subtle steps | Compact interfaces, mobile apps |
| 1.200 | Minor Third | Moderate contrast | General-purpose, balanced |
| 1.250 | Major Third | Clear distinction | Web apps, dashboards, SaaS |
| 1.333 | Perfect Fourth | Strong hierarchy | Marketing sites, content-heavy |
| 1.414 | Augmented Fourth | Dramatic jumps | Editorial, magazines |
| 1.500 | Perfect Fifth | Bold contrast | Headings-heavy layouts |
| 1.618 | Golden Ratio | Maximum drama | Landing pages, hero-driven design |

### Choosing the Right Ratio

**Decision Framework**:

```
How many heading levels do you need?
├── 2-3 levels → Larger ratio (1.333-1.618) for clear differentiation
└── 5-6 levels → Smaller ratio (1.125-1.25) to avoid extreme sizes

What’s the primary content type?
├── Dense data/dashboards → 1.125-1.200 (compact)
├── Mixed content app → 1.200-1.250 (balanced)
├── Marketing/editorial → 1.333-1.500 (dramatic)
└── Landing pages → 1.414-1.618 (bold)

What device is primary?
├── Mobile-first → 1.125-1.200 (space-efficient)
├── Desktop-primary → 1.200-1.333 (room for expression)
└── Large displays/TV → 1.333-1.618 (visible at distance)
```

---

## Building a Complete Type Scale

### Step 1: Define Base Size

The base size is your body text size — the most frequently used text in your product.

| Context | Recommended Base | Rationale |
|---------|-----------------|------------|
| Desktop web app | 16px (1rem) | Browser default, proven readable |
| Mobile app | 16px (1rem) | iOS/Android default for body |
| Dashboard/dense UI | 14px (0.875rem) | Compact but readable |
| Marketing/editorial | 18-20px (1.125-1.25rem) | Comfortable long-form reading |
| Accessibility-focused | 18px+ (1.125rem+) | Larger default for broader audience |

**Critical rule**: Never go below 14px for body text. 12px is acceptable only for captions and labels, never for primary reading.

### Step 2: Generate the Scale

Using base 16px and ratio 1.25 (Major Third), a complete production scale:

| Token | Size | Rem | Line Height | Intended Usage |
|-------|------|-----|-------------|----------------|
| text-xs | 12px | 0.75rem | 1.33 (16px) | Captions, badges, fine print |
| text-sm | 14px | 0.875rem | 1.43 (20px) | Secondary text, metadata |
| text-base | 16px | 1rem | 1.5 (24px) | Body text, paragraphs |
| text-lg | 20px | 1.25rem | 1.4 (28px) | Lead paragraphs, emphasis |
| text-xl | 25px | 1.563rem | 1.36 (34px) | H5, card titles |
| text-2xl | 31px | 1.953rem | 1.29 (40px) | H4, section subheadings |
| text-3xl | 39px | 2.441rem | 1.23 (48px) | H3, major sections |
| text-4xl | 49px | 3.052rem | 1.16 (57px) | H2, page sections |
| text-5xl | 61px | 3.815rem | 1.11 (68px) | H1, page titles |
| text-6xl | 76px | 4.768rem | 1.07 (81px) | Display, hero headlines |

### Step 3: Assign Line Heights

Line height (leading) is critical for readability. Follow this pattern:

| Text Size Range | Line Height | Rationale |
|----------------|-------------|------------|
| 12-14px (small) | 1.4-1.5 | Small text needs more breathing room |
| 16-20px (body) | 1.5-1.6 | Optimal for extended reading |
| 24-36px (headings) | 1.2-1.3 | Tighter leading maintains cohesion |
| 40px+ (display) | 1.05-1.15 | Very tight — large text has built-in space |

**The inverse relationship**: As font size increases, line height ratio decreases. This is because larger characters have more inherent whitespace.

---

## Visual Hierarchy Principles

### The Four Pillars of Typographic Hierarchy

**1. Size** — The most obvious differentiator
- Minimum 20-30% size increase between adjacent hierarchy levels
- Use scale ratios to ensure consistent jumps
- Don’t rely on size alone — combine with weight and color

**2. Weight** — Adds emphasis without changing size
- Recommended weight assignments:
  - Display/H1-H2: 700-800 (Bold/ExtraBold)
  - H3-H4: 600 (SemiBold)
  - H5-H6: 600 or 500 (SemiBold or Medium)
  - Body: 400 (Regular)
  - Secondary: 400 (Regular) + lighter color
  - Strong emphasis: 600 (SemiBold) within body text

**3. Color** — Creates depth without adding visual weight
- Primary text: Gray-900 or near-black (maximum contrast)
- Secondary text: Gray-600 (reduced but readable)
- Tertiary/disabled: Gray-400 (minimum 4.5:1 contrast)
- Use color sparingly for links and interactive elements

**4. Spacing** — Groups related content and separates sections
- More space above a heading than below it (heading belongs to content below)
- Rule of thumb: space above heading = 1.5-2x space below heading
- Paragraph spacing: 0.75-1em between paragraphs

### Hierarchy Levels in Practice

| Level | Element | Size | Weight | Color | Purpose |
|-------|---------|------|--------|-------|--------|
| 1 | Page Title (H1) | 3xl-5xl | 700 | Gray-900 | One per page, establishes context |
| 2 | Section Head (H2) | 2xl-3xl | 600 | Gray-900 | Major content divisions |
| 3 | Subsection (H3) | xl-2xl | 600 | Gray-800 | Content grouping within sections |
| 4 | Group Label (H4) | lg-xl | 600 | Gray-800 | Card titles, sidebar headings |
| 5 | Minor Head (H5) | base-lg | 600 | Gray-700 | List headers, form section labels |
| 6 | Overline/Label | xs-sm | 500+CAPS | Gray-500 | Category labels, metadata |
| 7 | Body | base | 400 | Gray-700 | Primary reading content |
| 8 | Secondary | sm | 400 | Gray-500 | Supporting information |
| 9 | Caption | xs | 400 | Gray-400 | Timestamps, fine print |

---

## Advanced Scale Techniques

### Double-Stranded Scales

Use two interlocking scales for richer hierarchy:

```
Scale A (headings):  Base × 1.333 (Perfect Fourth)
  16 → 21 → 28 → 38 → 50 → 67

Scale B (body):      Base × 1.125 (Major Second)
  12 → 13.5 → 15 → 16 → 18 → 20
```

This gives you dramatic heading jumps with subtle body text variations.

### Custom Scales

For products needing non-mathematical precision, define a custom scale by hand:

```
12 / 14 / 16 / 18 / 20 / 24 / 30 / 36 / 48 / 60
```

Advantages:
- Every size is a round number (easier for development)
- Sizes can be tuned to specific UI needs
- No awkward fractional pixels

Disadvantage:
- Lacks the inherent harmony of mathematical ratios

### Responsive Scale Adjustment

Use different ratios at different breakpoints:

| Breakpoint | Ratio | Rationale |
|-----------|-------|------------|
| Mobile (<640px) | 1.200 | Compact, space-efficient |
| Tablet (640-1024px) | 1.250 | Moderate expression |
| Desktop (1024px+) | 1.333 | Full typographic range |

This means your H1 might be 36px on mobile but 50px on desktop — different sizes but the same hierarchical relationship.

---

## Design Token Structure for Type Scale

```json
{
  "fontSize": {
    "xs": { "value": "0.75rem" },
    "sm": { "value": "0.875rem" },
    "base": { "value": "1rem" },
    "lg": { "value": "1.25rem" },
    "xl": { "value": "1.563rem" },
    "2xl": { "value": "1.953rem" },
    "3xl": { "value": "2.441rem" },
    "4xl": { "value": "3.052rem" },
    "5xl": { "value": "3.815rem" }
  },
  "lineHeight": {
    "tight": { "value": "1.1" },
    "snug": { "value": "1.25" },
    "normal": { "value": "1.5" },
    "relaxed": { "value": "1.6" },
    "loose": { "value": "1.75" }
  },
  "fontWeight": {
    "regular": { "value": "400" },
    "medium": { "value": "500" },
    "semibold": { "value": "600" },
    "bold": { "value": "700" }
  }
}
```

---

## Tools for Type Scale Creation

| Tool | URL | Best For |
|------|-----|----------|
| **Type Scale** | type-scale.com | Visual scale calculator with ratio presets |
| **Utopia** | utopia.fyi | Fluid type scale generator with clamp() output |
| **Modular Scale** | modularscale.com | Calculate any ratio-based scale |
| **Archetype** | archetypeapp.com | Interactive type system builder |
| **Typographist** | typographist.alexj.work | Font size and line height calculator |

---

## Key Takeaways

1. Use mathematical ratios for harmonious size relationships
2. Smaller ratios (1.125-1.200) work best for dense UIs; larger ratios (1.333+) for marketing
3. Line height should decrease proportionally as font size increases
4. Combine size, weight, color, and spacing for robust hierarchy
5. Never go below 14px for any readable text; 16px is the safe body default
6. Consider responsive scale shifting — use tighter ratios on smaller screens
7. Document your scale as design tokens for consistent cross-platform implementation
