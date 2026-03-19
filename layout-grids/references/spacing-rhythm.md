# Spacing and Vertical Rhythm

## Overview

Consistent spacing creates visual harmony and improves readability. Spacing systems and vertical rhythm provide structure without being visible to users.

---

## Spacing Scale

**8-Point Grid**: Base unit of 8px. All spacing is multiple of 8 (8, 16, 24, 32, 40, 48, 56, 64).

**Benefits**: 
- Consistent spacing across design
- Easier for developers (no arbitrary values)
- Scales well across devices
- Aligns with common screen resolutions

**4-Point Grid**: More granular. Base unit of 4px. Allows for tighter spacing when needed.

**Custom Scale**: Define your own scale based on project needs. Example: 4, 8, 12, 16, 24, 32, 48, 64, 96.

**Choosing Scale**: 8-point is industry standard. Use 4-point if you need more granularity. Stay consistent.

---

## Applying Spacing

**Component Padding**: Internal spacing within components. Typically 8-16px for small components, 16-24px for larger.

**Component Margins**: Space between components. Typically 16-32px depending on relationship.

**Section Spacing**: Space between major sections. Typically 48-96px. Creates clear separation.

**Micro Spacing**: Space between related elements (icon and label, form label and input). Typically 4-8px.

**Macro Spacing**: Space between unrelated elements. Typically 24-48px.

**Proximity Principle**: Related elements should be closer together than unrelated elements. Spacing communicates relationships.

---

## Vertical Rhythm

**Baseline Grid**: Invisible horizontal grid based on line height. All text aligns to baseline.

**Line Height**: Typically 1.5× font size for body text. Creates comfortable reading rhythm.

**Example**:
- Body text: 16px font, 24px line height (16 × 1.5)
- Heading: 32px font, 40px line height (32 × 1.25)
- All line heights are multiples of 8px

**Benefits**: Creates visual harmony, improves readability, aligns text across columns.

**Implementation**: Set base line height (e.g., 24px). All spacing and heights should be multiples of this value.

---

## Spacing in Responsive Design

**Scale Down on Mobile**: Reduce spacing at smaller breakpoints. 48px section spacing becomes 32px on mobile.

**Maintain Ratios**: If desktop has 2:1 ratio between section and component spacing, maintain that ratio on mobile.

**Minimum Spacing**: Don't go below 8px for component spacing. Maintains touch targets and readability.

**Responsive Scale Example**:
- Desktop: 8, 16, 24, 32, 48, 64, 96
- Tablet: 8, 12, 16, 24, 32, 48, 64
- Mobile: 8, 12, 16, 20, 24, 32, 48

**CSS Variables**: Use CSS custom properties for spacing. Easy to adjust at breakpoints.

---

## Common Spacing Mistakes

**Arbitrary Values**: Using random spacing (13px, 27px) instead of system values. Creates inconsistency.

**Too Tight**: Insufficient spacing makes design feel cramped and hard to read.

**Too Loose**: Excessive spacing wastes screen real estate and breaks visual relationships.

**Inconsistent Application**: Using different spacing for same type of relationship. Confuses users.

**Ignoring Proximity**: Unrelated elements too close, related elements too far. Spacing should communicate relationships.

**Not Testing**: Spacing that works on desktop may be too tight on mobile. Always test at actual sizes.

---

## Spacing Documentation

**Design Tokens**: Document spacing values as design tokens. Makes handoff to development clear.

**Example**:
```
spacing-xs: 4px
spacing-sm: 8px
spacing-md: 16px
spacing-lg: 24px
spacing-xl: 32px
spacing-2xl: 48px
spacing-3xl: 64px
```

**Usage Guidelines**: Document when to use each spacing value. 'Use spacing-md between form fields.'

**Visual Examples**: Show spacing applied in context. Helps designers and developers apply consistently.

**Code Snippets**: Provide CSS/code examples. Reduces implementation errors.

---
