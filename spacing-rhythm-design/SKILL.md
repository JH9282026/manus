---
name: spacing-rhythm-design
description: "Establish visual rhythm and spacing systems using consistent scales for padding, margins, and element relationships. Use for: creating spacing tokens, defining vertical rhythm, applying the 8px grid system, establishing component spacing rules, and creating harmonious visual density across UI layouts."
---

# Spacing & Rhythm

Establish visual rhythm and spacing systems using consistent scales for padding, margins, and element relationships.

# Skill: Spacing & Rhythm

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Spacing & Rhythm |
| **Category** | Visual Design |
| **Phase** | 3 - Visual Design |
| **Estimated Time** | 20-30 minutes |
| **Dependencies** | `typography.md`, `layout_grids.md` |
| **Outputs** | Spacing scale, rhythm guidelines, padding/margin standards |

## Description
Spacing & Rhythm creates a mathematical system for whitespace that ensures visual consistency, establishes hierarchy, and creates pleasing proportions throughout the design. Good spacing is invisible but essential.

## When to Use
- After typography scale is established
- Before component design
- When layouts feel cramped or chaotic
- Establishing design system foundations
- Ensuring responsive spacing

---

## Instructions for AI Agents
### Step 1: Establish Base Unit

**Common base units:**

| Base | Scale | Best For |
|------|-------|----------|
| 4px | Compact, dense UI | Dashboards, data |
| 8px | Balanced, standard | Most applications |
| 16px | Spacious, editorial | Marketing, content |

**Prompt for spacing decision:**
```
For [PROJECT TYPE] targeting [AUDIENCE] with [DENSITY] information density:

1. Recommended base unit: [4/8/16]px
2. Scale multiplier approach: [Linear/Fibonacci/Custom]
3. Minimum spacing: [Value]
4. Maximum practical spacing: [Value]
```

### Step 2: Create Spacing Scale

**8px base scale (most common):**

```markdown

## Spacing Scale
| Token | Value | Pixels | Usage |
|-------|-------|--------|-------|
| space-0 | 0 | 0px | Reset, collapse |
| space-0.5 | 0.125rem | 2px | Micro gaps, hairlines |
| space-1 | 0.25rem | 4px | Icon-text gap, tight |
| space-2 | 0.5rem | 8px | Related elements |
| space-3 | 0.75rem | 12px | Default component padding |
| space-4 | 1rem | 16px | Standard gap |
| space-5 | 1.25rem | 20px | Component spacing |
| space-6 | 1.5rem | 24px | Card padding, sections |
| space-8 | 2rem | 32px | Large gaps |
| space-10 | 2.5rem | 40px | Section spacing |
| space-12 | 3rem | 48px | Major sections |
| space-16 | 4rem | 64px | Page sections |
| space-20 | 5rem | 80px | Hero spacing |
| space-24 | 6rem | 96px | Maximum gaps |
```

### Step 3: Define Usage Patterns

**Spacing application guide:**

```markdown

## Spacing Applications
### Component Internal Spacing

| Component | Padding | Internal Gap |
|-----------|---------|-------------|
| Button (sm) | 8px 12px | 6px (icon-text) |
| Button (md) | 10px 16px | 8px |
| Button (lg) | 12px 24px | 10px |
| Input | 12px 16px | - |
| Card | 20px or 24px | 16px |
| Modal | 24px | 20px |
| Table cell | 12px 16px | - |
| List item | 12px 16px | - |

### Component External Spacing

| Relationship | Spacing |
|--------------|--------|
| Related items (same group) | 8px |
| Items in a list | 12px |
| Components in same section | 16-24px |
| Section title to content | 16-24px |
| Between sections | 48-64px |
| Page title to content | 32px |
| Major page sections | 64-96px |

### Text Spacing

| Element | Margin Bottom |
|---------|---------------|
| Paragraph | 16px (1rem) |
| Heading to paragraph | 8-12px |
| Paragraph to heading | 32px |
| List items | 8px |
| Between list groups | 24px |
```

### Step 4: Vertical Rhythm

**Establishing baseline grid:**

```markdown

## Vertical Rhythm
### Baseline Grid
- Base line-height unit: 24px (for 16px body text × 1.5)
- All spacing should align to 4px or 8px increments

### Element Heights

| Element | Height | Lines (24px) |
|---------|--------|-------------|
| Single line text | 24px | 1 |
| Button (md) | 40px | ~1.67 (aligned to 8px) |
| Input (md) | 44px | ~1.83 (touch-friendly) |
| Nav item | 40px | ~1.67 |
| Table row | 48px | 2 |
| Card header | 64px | ~2.67 |

### Section Rhythm

```
| 96px | <- Page top padding
|------|
| Page Title (H1)
| 32px |
|------|
| Section
| 64px |
|------|
| Section
| 64px |
|------|
| 96px | <- Page bottom padding
```
```

### Step 5: Responsive Spacing

**Spacing adjustments by breakpoint:**

```markdown

## Responsive Spacing
### Scale by Breakpoint

| Token | Mobile | Tablet | Desktop |
|-------|--------|--------|----------|
| Section gap | 48px | 64px | 80px |
| Container padding | 16px | 24px | 32px |
| Card padding | 16px | 20px | 24px |
| Component gap | 12px | 16px | 16px |

### Fluid Spacing (CSS)

```css
/* Section spacing that scales with viewport */
.section-gap {
  padding: clamp(48px, 8vw, 96px) 0;
}

/* Container padding */
.container {
  padding: 0 clamp(16px, 4vw, 32px);
}
```

### Touch Considerations

- Minimum touch target: 44×44px
- Minimum tap spacing: 8px between targets
- Larger spacing on mobile for fat fingers
```

---

## Example Input/Output
### Example Input

```markdown
**Project**: TaskFlow dashboard
**Type**: SaaS application, moderate density
**Typography base**: 16px
**Grid gutter**: 24px
```

### Example Output

```markdown

## Prompts Library
### Spacing Scale Generation
```
Create a spacing scale for [PROJECT TYPE]:
- Base unit: [4/8/16]px
- Density: [Compact/Balanced/Spacious]
- Include: Token names, pixel values, use cases
```

### Component Spacing Audit
```
Review spacing in this component:
[COMPONENT SPEC]

Check:
1. Is internal spacing consistent?
2. Is external spacing defined?
3. Does it align to the spacing scale?
4. Touch targets adequate?
```

---

## Success Criteria
### Minimum Requirements
- [ ] Base unit established
- [ ] Complete spacing scale
- [ ] Component padding defined
- [ ] Section spacing defined
- [ ] Responsive considerations

### Quality Indicators
- [ ] Consistent spacing throughout design
- [ ] Clear hierarchy through spacing
- [ ] Comfortable, not cramped
- [ ] Touch-friendly targets
- [ ] Scale supports all use cases

---

## Related Skills
- **Previous**: `typography.md` - Line heights inform rhythm
- **Previous**: `layout_grids.md` - Grid gutters align with spacing
- **Next**: `component_design.md` - Apply spacing to components

## Using the Reference Files

### When to Read Each Reference

**`./references/spacing-system-taskflow.md`** — Read when you need detailed guidance on spacing system taskflow aspects of this skill.
