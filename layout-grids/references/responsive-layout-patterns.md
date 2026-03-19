# Responsive Layout Patterns

## Overview

Responsive layouts adapt to different screen sizes and devices. Common patterns provide proven solutions for handling content across breakpoints.

---

## Column Drop Pattern

**Behavior**: Multi-column layout stacks into fewer columns as screen narrows. Eventually becomes single column on mobile.

**Example**: 
- Desktop: 3 columns side-by-side
- Tablet: 2 columns, third drops below
- Mobile: 1 column, all stacked

**Use Cases**: Content-heavy sites, blogs, news sites, dashboards.

**Implementation**: Use CSS Grid or Flexbox with media queries. Adjust column spans at breakpoints.

**Advantages**: Simple, predictable, works for most content types.

**Considerations**: Decide which column drops first. Usually least important content.

---

## Mostly Fluid Pattern

**Behavior**: Grid-based layout that adjusts column widths fluidly. Margins increase on large screens, columns stack on small screens.

**Example**:
- Large desktop: 12-column grid with wide margins
- Desktop: 12-column grid with normal margins
- Tablet: 8-column grid
- Mobile: Single column

**Use Cases**: Most websites, flexible content, varied content types.

**Implementation**: Fluid grid with max-width container. Columns adjust proportionally.

**Advantages**: Flexible, efficient use of space, smooth transitions.

**Considerations**: Test at all sizes, not just breakpoints. Ensure content works at in-between sizes.

---

## Layout Shifter Pattern

**Behavior**: Significant layout changes at breakpoints. Not just stacking, but complete reorganization.

**Example**:
- Desktop: Sidebar left, content center, widgets right
- Tablet: Content top, sidebar and widgets below in 2 columns
- Mobile: Content, sidebar, widgets all stacked

**Use Cases**: Complex applications, dashboards, sites with distinct content areas.

**Implementation**: CSS Grid with template areas. Redefine grid at each breakpoint.

**Advantages**: Optimized layout for each screen size. Maximum flexibility.

**Considerations**: More complex to implement. Ensure content order makes sense at all sizes.

---

## Off Canvas Pattern

**Behavior**: Secondary content (navigation, filters) hidden off-screen on small devices. Revealed via menu button or swipe.

**Example**: 
- Desktop: Navigation visible in sidebar
- Mobile: Navigation hidden, hamburger menu reveals it

**Use Cases**: Navigation-heavy sites, e-commerce filters, mobile apps.

**Implementation**: Position navigation off-screen with CSS. Toggle visibility with JavaScript.

**Advantages**: Maximizes content area on small screens. Familiar pattern to users.

**Considerations**: Ensure menu button is obvious. Provide way to close menu. Consider accessibility.

---

## Tiny Tweaks Pattern

**Behavior**: Minimal changes across breakpoints. Mostly font size and spacing adjustments.

**Example**: Single-column layout at all sizes. Just adjust font sizes, spacing, and image sizes.

**Use Cases**: Simple sites, landing pages, articles, mobile-first designs.

**Implementation**: Fluid typography and spacing. Minimal media queries.

**Advantages**: Simple to implement and maintain. Consistent experience across devices.

**Considerations**: Works best for simple layouts. May not be optimal for complex content.

---

## Responsive Tables

**Problem**: Tables don't fit on small screens. Horizontal scrolling is poor UX.

**Solutions**:

**1. Horizontal Scroll**: Allow table to scroll horizontally. Simple but not ideal.

**2. Collapse to List**: Each row becomes a card on mobile. Labels repeat for each row.

**3. Hide Columns**: Hide less important columns on small screens. Provide way to show all data.

**4. Flip Axis**: Rotate table so columns become rows. Works for small tables.

**5. Chart Instead**: Replace table with chart on mobile. Better for data visualization.

**Choosing Solution**: Depends on data importance, table complexity, and user needs.

---
