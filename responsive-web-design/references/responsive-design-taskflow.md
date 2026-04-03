# Responsive Design: TaskFlow - Detailed Reference

Detailed reference content for responsive design.

---

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
