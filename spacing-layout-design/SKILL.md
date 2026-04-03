---
name: spacing-layout-design
description: "Create mathematical spacing systems and vertical rhythm for consistent whitespace, visual hierarchy, and pleasing proportions in UI design. Use for: establishing spacing scales and base units, defining component padding and margins, creating vertical rhythm with baseline grids, building responsive spacing that adapts across breakpoints, and setting design system spacing tokens."
---

# Spacing & Layout Design

Create mathematical spacing systems that ensure visual consistency, establish hierarchy, and create pleasing proportions throughout the design.

## Overview

Spacing & Rhythm creates a mathematical system for whitespace that ensures visual consistency, establishes hierarchy, and creates pleasing proportions. Good spacing is invisible but essential. This skill covers base unit selection, spacing scale creation, component padding standards, vertical rhythm, and responsive spacing adjustments.

## When to Use

- After typography scale is established
- Before component design begins
- When layouts feel cramped or chaotic
- Establishing design system foundations
- Ensuring responsive spacing across breakpoints

## Base Unit Selection

| Base | Scale | Best For |
|------|-------|----------|
| 4px | Compact, dense UI | Dashboards, data-heavy apps |
| 8px | Balanced, standard | Most web applications |
| 16px | Spacious, editorial | Marketing sites, content-focused |

Choose based on information density and audience. Most applications use **8px** as the base unit.

## Spacing Scale (8px Base)

| Token | Value | Pixels | Usage |
|-------|-------|--------|-------|
| space-0.5 | 0.125rem | 2px | Micro gaps, hairlines |
| space-1 | 0.25rem | 4px | Icon-text gap, tight spacing |
| space-2 | 0.5rem | 8px | Related elements |
| space-3 | 0.75rem | 12px | Default component padding |
| space-4 | 1rem | 16px | Standard gap |
| space-5 | 1.25rem | 20px | Component spacing |
| space-6 | 1.5rem | 24px | Card padding, sections |
| space-8 | 2rem | 32px | Large gaps, page headers |
| space-10 | 2.5rem | 40px | Section spacing |
| space-12 | 3rem | 48px | Major sections |
| space-16 | 4rem | 64px | Page sections |
| space-20 | 5rem | 80px | Hero spacing |
| space-24 | 6rem | 96px | Maximum gaps |

## Component Internal Spacing

| Component | Padding | Internal Gap |
|-----------|---------|-------------|
| Button (sm) | 8px 12px | 6px (icon-text) |
| Button (md) | 10px 16px | 8px |
| Button (lg) | 12px 24px | 10px |
| Input | 12px 16px | — |
| Card | 20px or 24px | 16px |
| Modal | 24px | 20px |
| Table cell | 12px 16px | — |
| List item | 12px 16px | — |

## Component External Spacing

| Relationship | Spacing |
|--------------|--------|
| Related items (same group) | 8px |
| Items in a list | 12px |
| Components in same section | 16–24px |
| Section title to content | 16–24px |
| Between sections | 48–64px |
| Page title to content | 32px |
| Major page sections | 64–96px |

## Text Spacing

| Element | Margin Bottom |
|---------|---------------|
| Paragraph | 16px (1rem) |
| Heading to paragraph | 8–12px |
| Paragraph to heading | 32px |
| List items | 8px |
| Between list groups | 24px |

## Vertical Rhythm

- **Base line-height unit**: 24px (for 16px body text × 1.5)
- All spacing aligns to 4px or 8px increments

### Element Heights (8px aligned)

| Element | Height |
|---------|--------|
| Button sm | 32px (4 × 8px) |
| Button md | 40px (5 × 8px) |
| Button lg | 48px (6 × 8px) |
| Input | 44px (touch-friendly) |
| Nav item | 40px (5 × 8px) |
| Table row | 48px (6 × 8px) |
| Avatar sm/md/lg | 32px / 40px / 48px |

## Responsive Spacing

| Spacing Type | Mobile | Tablet | Desktop |
|--------------|--------|--------|----------|
| Page padding | 16px | 24px | 32px |
| Card padding | 16px | 20px | 24px |
| Section gap | 32px | 48px | 64px |
| Component gap | 12px | 16px | 16px |
| Grid gutter | 16px | 20px | 24px |

Use CSS `clamp()` for fluid spacing:
```css
.section-gap { padding: clamp(48px, 8vw, 96px) 0; }
.container { padding: 0 clamp(16px, 4vw, 32px); }
```

### Touch Considerations
- Minimum touch target: 44×44px
- Minimum tap spacing: 8px between targets
- Use larger spacing on mobile for finger-friendly interaction

## Quick Reference

| Category | Range | Use Cases |
|----------|-------|-----------|
| **Tight** | 2–4px | Icon-to-text, stacked badges |
| **Compact** | 8–12px | Related elements, list items |
| **Standard** | 16–24px | Component gaps, card padding |
| **Relaxed** | 32–48px | Section titles, component groups |
| **Spacious** | 64–96px | Page sections, hero areas |

## Best Practices

1. **Stick to the scale** — Never use arbitrary pixel values outside the scale
2. **Use semantic tokens** — Name by purpose (`--space-card-padding`) not just value
3. **Test at all breakpoints** — Spacing that works on desktop may be too generous on mobile
4. **Audit regularly** — Check that all components use the spacing scale consistently
5. **Align to the grid** — All element heights should be multiples of your base unit

## Using the Reference Files

### When to Read Each Reference

**`./references/spacing-scale-implementation.md`** — Read when implementing CSS custom properties for the spacing scale, building design tokens, or needing detailed code examples for applying spacing.

**`./references/vertical-rhythm-guide.md`** — Read when establishing baseline grids, aligning element heights, or needing detailed vertical rhythm patterns for text and components.

**`./references/responsive-spacing-patterns.md`** — Read when designing responsive spacing adjustments, implementing fluid spacing with clamp(), or auditing spacing across breakpoints.
