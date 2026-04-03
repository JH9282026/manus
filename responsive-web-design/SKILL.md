---
name: responsive-web-design
description: "Adapt designs across screen sizes and breakpoints using fluid layouts, flexible grids, and responsive strategies. Use for: defining breakpoints, creating mobile-first layouts, adapting typography and spacing for different viewports, designing responsive navigation, and ensuring consistent user experience across desktop, tablet, and mobile devices."
---

# Responsive Design

Adapt designs across screen sizes and breakpoints using fluid layouts, flexible grids, and responsive strategies.

# Skill: Responsive Design

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Responsive Design |
| **Category** | Responsive & Platform Design |
| **Phase** | 4 - Responsive & Platform |
| **Estimated Time** | 45-90 minutes |
| **Dependencies** | `layout_grids.md`, `component_design.md` |
| **Outputs** | Responsive mockups for all breakpoints |

## Description
Responsive Design adapts layouts, components, and interactions to work beautifully across all screen sizes from mobile phones to large desktops. This skill ensures consistent user experience regardless of device.

## When to Use
- After desktop design is complete
- Creating mobile-first implementations
- Auditing existing responsive behavior
- Designing for specific device targets
- Optimizing for touch interactions

---

## Instructions for AI Agents
### Step 1: Define Breakpoint Strategy

**Standard breakpoint system:**

```markdown

## Breakpoints
| Name | Width | Target | Priority |
|------|-------|--------|----------|
| xs | <640px | Small phones | ✓ Design |
| sm | 640px+ | Large phones | |
| md | 768px+ | Tablets portrait | ✓ Design |
| lg | 1024px+ | Tablets landscape, small laptops | |
| xl | 1280px+ | Desktops | ✓ Design |
| 2xl | 1536px+ | Large desktops | |

**Design Priority**: Create mockups for xs, md, xl at minimum.
```

### Step 2: Layout Adaptation Patterns

**Common responsive patterns:**

```markdown
### Pattern: Column Drop
Columns stack vertically as viewport shrinks.

Desktop (3 col): [A] [B] [C]
Tablet (2 col):  [A] [B]
                 [C]
Mobile (1 col):  [A]
                 [B]
                 [C]

### Pattern: Layout Shifter
Layout fundamentally reorganizes.

Desktop: [Sidebar] [      Content      ]
Mobile:  [Header nav icon]
         [Content full width]
         [Bottom tab bar]

### Pattern: Off-Canvas
Navigation hides in drawer.

Desktop: [Full nav] [Content]
Mobile:  [☰] [Content]
         (nav slides in when ☰ tapped)

### Pattern: Content Priority
Less important content hidden on small screens.

Desktop: Show all columns in table
Tablet:  Hide tertiary columns
Mobile:  Card view instead of table
```

### Step 3: Component Responsiveness

**Component adaptation checklist:**

```markdown
### Navigation
| Size | Behavior |
|------|----------|
| Desktop | Full horizontal nav or sidebar |
| Tablet | Collapsed sidebar (icons) or hamburger |
| Mobile | Bottom tab bar + hamburger for overflow |

### Cards
| Size | Behavior |
|------|----------|
| Desktop | Grid (3-4 columns) |
| Tablet | Grid (2 columns) |
| Mobile | Single column, full width |

### Tables
| Size | Behavior |
|------|----------|
| Desktop | Full table with all columns |
| Tablet | Hide tertiary columns |
| Mobile | Convert to card/list view OR horizontal scroll |

### Forms
| Size | Behavior |
|------|----------|
| Desktop | Multi-column forms possible |
| Mobile | Single column, full-width inputs |

### Modals
| Size | Behavior |
|------|----------|
| Desktop | Centered modal with backdrop |
| Mobile | Full-screen or bottom sheet |

### Images
| Size | Behavior |
|------|----------|
| Desktop | Larger, multiple per row |
| Mobile | Full-width, optimized size |
```

### Step 4: Touch Optimization

**Mobile-specific requirements:**

```markdown
### Touch Targets
- Minimum size: 44×44px (iOS) / 48×48dp (Android)
- Minimum spacing: 8px between targets
- Generous padding on buttons

### Touch Interactions
- Replace hover states with tap states
- Add active states (:active) for feedback
- Consider swipe gestures where appropriate
- Bottom-heavy UI for thumb reach

### Form Optimization
- Use appropriate input types (email, tel, number)
- Font size 16px+ to prevent iOS zoom
- Large tap targets for checkboxes/radios
- Sticky submit buttons if form is long

### Content Considerations
- Front-load important content
- Collapse secondary information (accordions)
- Reduce text length for scanning
- Larger line-height for readability
```

---

## Example Input/Output
### Example Input

```markdown
**Project**: TaskFlow dashboard
**Desktop design**: Sidebar + main content with stat cards, task list, project grid
**Key interactions**: Task management, project overview, navigation
```

### Example Output

```markdown

## Prompts Library
### Quick Responsive Conversion
```
Convert this desktop layout to mobile:
[DESKTOP LAYOUT]

Consider:
1. What stacks vertically?
2. What gets hidden/collapsed?
3. How does navigation change?
4. Touch target sizes?
```

### Breakpoint Audit
```
Review responsiveness of [COMPONENT]:

1. Does it work at all breakpoints?
2. Are touch targets adequate on mobile?
3. Is content prioritized correctly?
4. Any awkward intermediate states?
```

---

## Success Criteria
### Minimum Requirements
- [ ] Mobile layout designed
- [ ] Tablet layout designed  
- [ ] Desktop layout designed
- [ ] Navigation adapts appropriately
- [ ] Touch targets meet minimums

### Quality Indicators
- [ ] Smooth transitions between breakpoints
- [ ] Content hierarchy maintained
- [ ] Mobile feels native, not shrunk desktop
- [ ] Performance considered

---

## Related Skills
- **Previous**: `layout_grids.md` - Grid foundations
- **Next**: `mobile_app_design.md` - Native app patterns
- **Related**: `accessibility_review.md` - Mobile accessibility

## Using the Reference Files

### When to Read Each Reference

**`./references/responsive-design-taskflow.md`** — Read when you need detailed guidance on responsive design taskflow aspects of this skill.
