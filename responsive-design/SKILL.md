---
name: responsive-design
description: "Create designs that adapt seamlessly across devices and screen sizes using responsive design principles. Use for: multi-device design, breakpoint planning, fluid layouts, mobile-first approach, and cross-platform consistency."
---

# Responsive Design

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
## Responsive Design: TaskFlow

### Breakpoint Definitions

| Breakpoint | Width | Grid | Sidebar |
|------------|-------|------|--------|
| Mobile | <768px | 4-col | Hidden |
| Tablet | 768-1023px | 8-col | Collapsed (64px) |
| Desktop | 1024px+ | 12-col | Full (240px) |

---

### Dashboard - Desktop (1280px)

```
┌──────────┬───────────────────────────────────────────────┐
│          │  Search                        🔔 Avatar  │
│  Logo    ├───────────────────────────────────────────────┤
├──────────┤  Welcome, Sarah                              │
│          │                                               │
│ ▶ Dash   ├──────────────┬──────────────┬───────────────┤
│   Projects│  Stat Card  │  Stat Card  │  Stat Card   │
│   Tasks  │     12      │    5 due   │    2 risk   │
│   Team   ├──────────────┴──────────────┴───────────────┤
│   Time   │                                               │
│          │  My Tasks Today                              │
│──────────│  ☐ Task one                                   │
│          │  ☐ Task two                                   │
│ [+ New]  │                                               │
│          ├───────────────────────────────────────────────┤
│          │  Projects                                     │
│          │  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐     │
│          │  │ Proj1 │ │ Proj2 │ │ Proj3 │ │ Proj4 │     │
│          │  └───────┘ └───────┘ └───────┘ └───────┘     │
└──────────┴───────────────────────────────────────────────┘

Sidebar: 240px fixed
Content: Fluid with 12-col grid
Project cards: 4 per row (3 columns each)
```

---

### Dashboard - Tablet (768px)

```
┌─────┬─────────────────────────────────┐
│     │  Search              🔔 AV  │
│ 🏠  ├─────────────────────────────────┤
│ 📁  │  Hi, Sarah                        │
│ ✅  │                                  │
│ 👥  ├──────────┬──────────┬──────────┤
│ ⏱  │  12 Proj │  5 Due   │  2 Risk  │
│     ├──────────┴──────────┴──────────┤
│     │                                  │
│  +  │  My Tasks                        │
│     │  ☐ Task one                      │
│     │  ☐ Task two                      │
│     │                                  │
│     ├─────────────────────────────────┤
│     │  Projects                        │
│     │  ┌────────┐ ┌────────┐          │
│     │  │ Proj1  │ │ Proj2  │          │
│     │  └────────┘ └────────┘          │
└─────┴─────────────────────────────────┘

Sidebar: 64px (icons only, tooltips on hover)
Labels: Hidden, shown on hover/focus
Project cards: 2 per row
```

---

### Dashboard - Mobile (375px)

```
┌───────────────────────┐
│  [☰] TaskFlow   🔍  🔔  │
├───────────────────────┤
│                       │
│  Hi, Sarah            │
│                       │
│  ┌─────┬─────┬─────┐  │
│  │ 12  │  5  │  2  │  │  <- Compact stats
│  │Proj │ Due │Risk │  │
│  └─────┴─────┴─────┘  │
│                       │
│  My Tasks (5)         │
│  ┌───────────────────┐  │
│  │ ☐ Task one       │  │
│  │   Acme • Due today │  │
│  └───────────────────┘  │
│  ┌───────────────────┐  │
│  │ ☐ Task two       │  │
│  │   Beta • Due today │  │
│  └───────────────────┘  │
│                       │
│  Projects             │
│  ┌───────────────────┐  │
│  │ Acme Rebrand  🟡  │  │  <- Full-width cards
│  └───────────────────┘  │
│                       │
├───────────────────────┤
│  🏠    📁   (➕)  ✅   ⋮  │  <- Bottom tab bar
└───────────────────────┘

Sidebar: Replaced by hamburger menu
Navigation: Bottom tab bar (5 items max)
Project cards: Full width, stacked
Stats: Horizontal compact row
```

---

### Adaptation Details

#### Navigation
| Element | Desktop | Tablet | Mobile |
|---------|---------|--------|--------|
| Sidebar | Full 240px | Icons 64px | Hidden |
| Top bar | Search + avatar | Same | Hamburger + search |
| Quick add | Sidebar button | Icon | FAB in tab bar |
| Nav overflow | Always visible | Visible | In hamburger |

#### Content
| Element | Desktop | Tablet | Mobile |
|---------|---------|--------|--------|
| Stat cards | 3 across | 3 across | 3 compact inline |
| Task list | Table-like rows | Same | Card-style |
| Project grid | 4 columns | 2 columns | 1 column |
| Page padding | 32px | 24px | 16px |

#### Interactions
| Interaction | Desktop | Mobile |
|-------------|---------|--------|
| Hover states | ✓ | Remove (use active) |
| Task checkbox | Click | Larger tap target |
| Project card | Click to open | Tap to open |
| Sidebar toggle | N/A | Hamburger tap |
| Quick actions | Hover reveal | Swipe or menu |

---

### Mobile-Specific Optimizations

1. **Touch Targets**
   - All buttons: minimum 44px height
   - Checkboxes: 44px tap target (larger than visual)
   - Nav items: 48px minimum

2. **Thumb Zone**
   - Primary actions at bottom (tab bar)
   - FAB for "add" action
   - Pull-to-refresh for updates

3. **Forms**
   - Full-width inputs
   - 16px font size (prevent iOS zoom)
   - Fixed submit button at bottom

4. **Performance**
   - Lazy load project cards
   - Skeleton loading states
   - Optimized images
```

---

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

- [./references/breakpoints-media-queries.md](./references/breakpoints-media-queries.md): Breakpoints Media Queries
- [./references/mobile-navigation-patterns.md](./references/mobile-navigation-patterns.md): Mobile Navigation Patterns
- [./references/responsive-images-media.md](./references/responsive-images-media.md): Responsive Images Media
- [./references/responsive-layout-fundamentals.md](./references/responsive-layout-fundamentals.md): Responsive Layout Fundamentals
