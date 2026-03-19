# Icon Design Principles

## Overview

Effective icons are simple, recognizable, and consistent. They communicate meaning quickly and work across sizes and contexts. Good icon design balances clarity with personality.

---

## Clarity and Simplicity

**Reduce to Essence**: Remove all non-essential details. Icon should be recognizable at smallest size (16px).

**Clear Silhouette**: Icon should be identifiable from outline alone. Test by viewing as solid black shape.

**Avoid Ambiguity**: Icon meaning should be immediately clear. If it requires explanation, it's too complex.

**One Concept Per Icon**: Don't try to communicate multiple ideas in one icon. Keep it focused.

**Test at Size**: Always test icons at actual usage size. What works at 512px may fail at 24px.

---

## Consistency and System Thinking

**Visual Style**: All icons in set should share visual language. Same line weight, corner radius, level of detail.

**Grid System**: Use consistent grid (e.g., 24×24px with 2px padding). Ensures optical alignment.

**Stroke Weight**: Maintain consistent stroke width across set. Typically 1.5-2px at base size.

**Corner Radius**: Consistent rounding. Either all sharp, all rounded, or consistent radius value.

**Metaphors**: Use consistent metaphor system. If folder = container, use consistently.

**Perspective**: Stick to one perspective (flat, isometric, or 3/4 view) across entire set.

---

## Optical Adjustment

**Optical vs Mathematical**: Shapes that are mathematically equal may not look equal. Trust your eye.

**Vertical vs Horizontal**: Vertical strokes appear thinner than horizontal. Compensate by making verticals slightly thicker.

**Circles and Squares**: Circle must be slightly larger than square to appear same size.

**Alignment**: Icons should feel centered even if not mathematically centered. Adjust for visual weight.

**Overshoot**: Rounded shapes should extend slightly beyond baseline for optical alignment.

---

## Metaphor and Recognition

**Universal Metaphors**: Use widely recognized symbols. Magnifying glass = search, house = home, gear = settings.

**Cultural Considerations**: Some symbols have different meanings in different cultures. Research target audience.

**Avoid Obsolete Metaphors**: Floppy disk for save is outdated. Consider more timeless alternatives.

**Literal vs Abstract**: Literal icons (picture of thing) are clearer but less flexible. Abstract icons (symbolic) are more versatile but may need learning.

**Test Recognition**: Show icons to users without labels. Can they identify meaning?

---

## Technical Specifications

**Format**: SVG for web (scalable, small file size). PNG for raster needs (multiple sizes).

**Artboard Size**: Design at 24×24px or 32×32px. Scale up for larger sizes, not down.

**Pixel Grid**: Align to pixel grid at base size. Prevents blurry rendering.

**Export Sizes**: Provide multiple sizes (16px, 24px, 32px, 48px, 64px) or single SVG.

**Color**: Design in black first. Color can be applied via CSS/code. Simplifies maintenance.

**Naming**: Use consistent, descriptive names. icon-search.svg, icon-settings.svg, etc.

---

## Accessibility

**Labels**: Icons should always have text labels or ARIA labels. Never rely on icon alone.

**Color**: Don't rely on color alone to convey meaning. Icon shape should communicate.

**Size**: Minimum touch target 44×44px (Apple) or 48×48px (Android). Icon can be smaller but clickable area must meet minimum.

**Contrast**: Ensure sufficient contrast against background (3:1 minimum for UI elements).

**Alternative Text**: Provide alt text for informative icons. Decorative icons should have empty alt attribute.

---
