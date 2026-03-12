# Android Design Guidelines (Material Design)

## Navigation Patterns

### Bottom Navigation
- 3-5 destinations
- Icons + text labels
- Active destination highlighted
- Badge support for notifications
- Scrolls away on content scroll (optional)

### Navigation Drawer
- Full-height panel from left edge
- User account section at top
- Grouped navigation items
- Used for 5+ destinations
- Hamburger icon trigger

### Top App Bar
- Title left-aligned
- Navigation icon (hamburger or back)
- Action icons right-aligned (1-3)
- Can collapse on scroll

---

## Typography (Roboto)

| Style | Size | Weight | Tracking |
|-------|------|--------|----------|
| Display Large | 57sp | Regular | -0.25 |
| Display Medium | 45sp | Regular | 0 |
| Display Small | 36sp | Regular | 0 |
| Headline Large | 32sp | Regular | 0 |
| Headline Medium | 28sp | Regular | 0 |
| Headline Small | 24sp | Regular | 0 |
| Title Large | 22sp | Regular | 0 |
| Title Medium | 16sp | Medium | 0.15 |
| Title Small | 14sp | Medium | 0.1 |
| Body Large | 16sp | Regular | 0.5 |
| Body Medium | 14sp | Regular | 0.25 |
| Body Small | 12sp | Regular | 0.4 |
| Label Large | 14sp | Medium | 0.1 |
| Label Medium | 12sp | Medium | 0.5 |
| Label Small | 11sp | Medium | 0.5 |

---

## Material Design Components

### Floating Action Button (FAB)
- Primary action for screen
- 56dp standard, 40dp mini
- Bottom-right positioning (typical)
- One per screen maximum
- Use for creation, sharing, navigation

### Cards
- Corner radius: 12dp (Material 3)
- Elevation: 1dp default
- Content padding: 16dp
- Types: elevated, filled, outlined

### Bottom Sheets
- **Standard**: Persistent, part of layout
- **Modal**: Overlays content, scrim behind
- Swipe down to dismiss
- Peek height + full expansion
- Used for supplementary content

### Chips
| Type | Use |
|------|-----|
| Assist | Smart suggestions |
| Filter | Refine content |
| Input | User entries, tags |
| Suggestion | Dynamic recommendations |

---

## Material 3 (Material You)

### Dynamic Color
- Extract color from user's wallpaper
- Generate harmonized color scheme
- Tonal palettes with 13 tonal values
- Maintain WCAG contrast requirements
- Provide fallback static colors

### Shape System
| Category | Corner Radius |
|----------|--------------|
| Extra Small | 4dp |
| Small | 8dp |
| Medium | 12dp |
| Large | 16dp |
| Extra Large | 28dp |
| Full | 50% (circular) |

---

## Android Accessibility

- TalkBack support for all elements
- `contentDescription` on images and icons
- Minimum 48×48dp touch targets
- Color contrast ≥4.5:1 for text
- Support font scaling up to 200%
- Focus order matches visual layout
