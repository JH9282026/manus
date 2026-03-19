# Grid Systems Fundamentals

## Overview

Grid systems provide structure and consistency to layouts. They create visual rhythm, align elements, and make responsive design more manageable. Good grids are invisible but essential.

---

## Types of Grids

**Manuscript Grid**: Single column of text. Simplest grid. Used for documents, long-form reading.

**Column Grid**: Multiple vertical columns. Most common for web design. Flexible and versatile.

**Modular Grid**: Columns and rows creating modules. Used for complex layouts with varied content types.

**Hierarchical Grid**: Custom grid based on content needs. More organic, less rigid. Requires more skill.

**Baseline Grid**: Horizontal grid based on line height. Ensures vertical rhythm. Common in print, less common in web.

**Choosing Grid Type**: Consider content variety, design complexity, and responsive needs.

---

## Column Grid Anatomy

**Columns**: Vertical divisions of the page. Typically 12 columns for web (divisible by 2, 3, 4, 6).

**Gutters**: Space between columns. Typically 20-30px for web. Provides breathing room.

**Margins**: Space on left and right edges. Prevents content from touching screen edges.

**Rows**: Horizontal divisions. Less common in web (infinite scroll) but useful for defining sections.

**Modules**: Intersection of columns and rows in modular grid. Creates consistent units.

**Example - 12-Column Grid**:
- Container width: 1200px
- Columns: 12
- Column width: 70px
- Gutter: 30px
- Margins: 15px each side

---

## Common Grid Configurations

**12-Column Grid**: Most versatile. Divides evenly by 2, 3, 4, 6. Industry standard.

**8-Column Grid**: Simpler, good for content-focused sites. Divides by 2, 4.

**16-Column Grid**: More granular control. Good for complex layouts.

**Responsive Breakpoints**:
- Mobile: 4 columns (320-767px)
- Tablet: 8 columns (768-1023px)
- Desktop: 12 columns (1024px+)

**Fluid vs Fixed**: 
- Fluid: Columns scale with viewport. More flexible.
- Fixed: Columns stay same width. More predictable.
- Hybrid: Fixed up to max width, then centered.

---

## Using Grids in Design

**Alignment**: Align elements to column edges or gutters. Creates visual order.

**Spanning**: Elements can span multiple columns. Heading spans 12 columns, body text spans 8.

**Nesting**: Grids within grids. Divide a 6-column section into 2 columns of 3.

**Breaking the Grid**: Intentional breaks create emphasis. Use sparingly for impact.

**Whitespace**: Don't fill every column. Empty columns create breathing room.

**Consistency**: Use same grid across all pages. Maintains visual coherence.

---

## Responsive Grid Behavior

**Stacking**: On mobile, columns stack vertically. 3-column layout becomes 1 column.

**Reordering**: Change order of elements at different breakpoints. Important content first on mobile.

**Hiding**: Hide less important content on small screens. Reduces clutter.

**Resizing**: Adjust column spans at breakpoints. 4-column element becomes 6 columns on tablet, 12 on mobile.

**Margin Adjustment**: Reduce margins on small screens to maximize content area.

**Testing**: Always test layouts at actual breakpoints. Don't assume it will work.

---

## Grid Tools and Frameworks

**CSS Grid**: Native CSS grid system. Powerful and flexible. Modern browser support.

**Flexbox**: One-dimensional layout. Good for components and simple layouts.

**Bootstrap Grid**: 12-column responsive grid. Easy to use, widely adopted.

**Tailwind CSS**: Utility-first CSS with grid classes. Flexible and customizable.

**Design Tool Grids**: Figma, Sketch, Adobe XD have built-in grid systems. Use during design phase.

**Grid Generators**: Tools like Grid Calculator, Gridlover help calculate grid math.

---
