---
name: typography-type-design
description: "Apply typography principles and type design techniques for print and digital media. Use for: typeface selection, font pairing, typographic hierarchy, responsive typography, variable fonts, web font optimization, type scale systems, and creating readable, aesthetically effective text layouts."
---

# Typography & Type Design

Apply professional typography principles to create readable, hierarchical, and aesthetically effective text layouts for print and digital media.

## Overview

Typography is the most impactful design decision — it accounts for 90%+ of most design surfaces. Good typography creates hierarchy, guides reading, conveys brand personality, and ensures accessibility. Poor typography — wrong font, bad spacing, inconsistent sizing — undermines even the best content. This skill covers typeface selection, font pairing, hierarchical type systems, responsive web typography, variable fonts, and performance optimization.

## Typeface Classification & Selection

| Classification | Characteristics | Personality | Best For | Reference |
|---------------|----------------|-------------|----------|-----------|
| Geometric sans | Perfect circles, uniform strokes | Modern, clean, tech | Tech brands, dashboards, UI | `/references/typeface-selection.md` |
| Humanist sans | Calligraphic influence, warm | Friendly, approachable | Body text, education, healthcare | `/references/typeface-selection.md` |
| Neo-grotesque sans | Neutral, minimal variation | Professional, universal | Corporate, government, neutral brands | `/references/typeface-selection.md` |
| Old-style serif | Diagonal stress, bracketed serifs | Traditional, authoritative | Books, editorial, law/finance | `/references/typeface-selection.md` |
| Modern/Didone serif | High contrast, thin serifs | Elegant, luxury | Fashion, luxury, magazine headers | `/references/typeface-selection.md` |
| Slab serif | Thick, block serifs | Bold, sturdy, confident | Headlines, posters, construction | `/references/typeface-selection.md` |
| Monospace | Equal-width characters | Technical, code-like | Code, data tables, technical docs | `/references/typeface-selection.md` |
| Display/decorative | Unique, personality-driven | Variable | Logos, headlines only (never body) | `/references/typeface-selection.md` |

### Selection Decision Matrix

| Criterion | Weight | How to Evaluate |
|-----------|--------|-----------------|
| Readability at target size | Critical | Test at actual use size on target device |
| Character set completeness | High | Verify language support, special characters |
| Weight range available | High | Need at least Regular, Bold; prefer 4+ weights |
| License and cost | Medium | Google Fonts (free), Adobe Fonts (subscription), purchasing |
| Brand alignment | High | Does the personality match the brand? |
| x-height | High for body text | Taller x-height = better readability at small sizes |
| OpenType features | Medium | Ligatures, old-style figures, small caps |

## Font Pairing Framework

### Proven Pairing Strategies

| Strategy | Heading Font | Body Font | Example | Reference |
|----------|-------------|-----------|---------|-----------|
| Contrast (serif + sans) | Serif display | Sans-serif body | Playfair Display + Source Sans Pro | `/references/hierarchy-systems.md` |
| Superfamily | Same family, different optical size | Same family, text optical size | IBM Plex Sans + IBM Plex Serif | `/references/hierarchy-systems.md` |
| Weight contrast | Heavy weight | Light/regular weight | Montserrat Black + Montserrat Light | `/references/hierarchy-systems.md` |
| Classification contrast | Geometric sans | Humanist sans | Futura + Gill Sans | `/references/hierarchy-systems.md` |

### Pairing Rules
- **Maximum 2 typefaces** per project (3 if one is monospace for code)
- **Contrast, don't conflict** — pair fonts that are clearly different, not subtly different
- **Match x-height** — fonts with similar x-heights pair more harmoniously
- **Test at actual sizes** — a pair that works at 72pt may fail at 14pt
- **Use weight and style** within one family before adding a second

## Type Scale Systems

### Modular Scale Ratios

| Ratio | Value | Character | Best For |
|-------|-------|-----------|----------|
| Minor Second | 1.067 | Very subtle | Dense data interfaces |
| Major Second | 1.125 | Gentle | Content-heavy sites, documentation |
| Minor Third | 1.200 | Balanced | General purpose, editorial |
| Major Third | 1.250 | Clear contrast | Marketing sites, landing pages |
| Perfect Fourth | 1.333 | Strong | Blogs, magazines, presentations |
| Golden Ratio | 1.618 | Dramatic | Headlines, posters, hero sections |

### Type Scale Example (Base 16px, Ratio 1.250)

| Level | Name | Size | Line Height | Use |
|-------|------|------|-------------|-----|
| -1 | Small | 12.8px | 1.5 | Captions, footnotes |
| 0 | Body | 16px | 1.5 | Paragraph text |
| 1 | Large | 20px | 1.4 | Lead paragraphs, intro text |
| 2 | H4 | 25px | 1.3 | Subsection headings |
| 3 | H3 | 31.25px | 1.3 | Section headings |
| 4 | H2 | 39px | 1.2 | Page headings |
| 5 | H1 | 48.8px | 1.1 | Hero headlines |
| 6 | Display | 61px | 1.05 | Display / banner text |

## Responsive Typography

### Fluid Type Scaling

| Approach | Implementation | Pros | Cons |
|----------|---------------|------|------|
| Media query breakpoints | `@media` with fixed sizes | Simple, predictable | Jumpy transitions |
| Fluid `clamp()` | `font-size: clamp(1rem, 2.5vw, 2rem)` | Smooth scaling | Slightly complex syntax |
| Modular scale per breakpoint | Different scale ratio at each breakpoint | Full control | More CSS to maintain |
| Container queries | Scale based on parent width | Component-level responsive | Newer browser support |

### Responsive Rules
- **Minimum body text: 16px** — never go below on any device
- **Maximum line length: 75 characters** — use `max-width: 65ch` on text containers
- **Scale headings down on mobile** — H1 on mobile might be H2 size on desktop
- **Increase line height on mobile** — 1.5–1.7 for body text on small screens
- **Test on real devices** — simulator font rendering differs from actual devices

## Web Font Performance

| Technique | Impact | Implementation | Reference |
|-----------|--------|---------------|-----------|
| `font-display: swap` | Prevents invisible text (FOIT) | CSS @font-face declaration | `/references/web-typography.md` |
| Subset fonts | Reduce file size 50–80% | Remove unused characters | `/references/web-typography.md` |
| WOFF2 format | Smallest file size | Modern standard format | `/references/web-typography.md` |
| Preload critical fonts | Faster first paint | `<link rel="preload">` | `/references/web-typography.md` |
| Variable fonts | One file replaces multiple weights | Reduces HTTP requests | `/references/web-typography.md` |
| System font stack | Zero load time | `system-ui, -apple-system, ...` | `/references/web-typography.md` |
| Self-host (not CDN) | Better privacy, control | Download and serve from your domain | `/references/web-typography.md` |

### Variable Font Advantages
- **Single file** replaces 4–8 weight files (Regular, Medium, SemiBold, Bold, etc.)
- **Arbitrary weights** — use `font-weight: 450` for exact brand match
- **Width axis** — adjust condensed/expanded from one file
- **Smaller total download** — one variable file is smaller than 3+ static files
- **Animation** — smoothly animate between weights, widths, or optical sizes

## Best Practices

- **Start with the body text** — choose body font first, then find a heading partner
- **Use no more than 2 typefaces** — constraints breed consistency
- **Set a type scale and stick to it** — don't freestyle font sizes
- **Test with real content** — lorem ipsum hides readability problems
- **Prioritize readability over aesthetics** — an unreadable but "cool" font is a failure
- **Always set `line-height`, `letter-spacing`, and `max-width`** — defaults are rarely optimal

## Using the Reference Files

**`/references/typeface-selection.md`** — Read when choosing typefaces for a project. Covers classification details, evaluation criteria, licensing, and recommended fonts by use case.

**`/references/hierarchy-systems.md`** — Read when building type hierarchies or pairing fonts. Covers modular scales, spacing systems, heading/body relationships, and visual weight.

**`/references/web-typography.md`** — Read when implementing typography on the web. Covers `@font-face`, variable fonts, fluid type, performance optimization, and CSS typographic properties.

**`/references/advanced-techniques.md`** — Read when working with OpenType features, multi-language typography, or complex layouts. Covers ligatures, contextual alternates, vertical rhythm, and print typography.
