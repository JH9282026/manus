# Mobile UX & Touch Interactions

Comprehensive guide to mobile user experience patterns, touch interactions, gestures, and navigation design.

---

## Mobile Navigation Patterns

### Bottom Navigation

**Best for**: Primary destinations (3-5 items)

**Pros**:
- Thumb-friendly, always visible
- Follows natural hand position
- Clear indication of current location

**Cons**:
- Limited to 3-5 items
- Takes up screen real estate

**Implementation Tips**:
- Use icons with labels
- Highlight active state clearly
- Keep labels concise (1-2 words)

### Hamburger Menu

**Best for**: Secondary navigation, deep hierarchies

**Pros**:
- Space-efficient
- Familiar pattern
- Accommodates many items

**Cons**:
- Low discoverability
- Extra tap required
- Hidden navigation reduces engagement

### Tab Bar

**Best for**: Content switching within a view

**Pros**:
- Clear, persistent navigation
- Visual indication of sections
- Quick switching

**Cons**:
- Limited flexibility
- May require scrolling on mobile

### Priority+ Navigation

**Best for**: Mixed importance navigation

**Pros**:
- Shows most important items
- Adapts to available space
- Progressive disclosure built-in

**Cons**:
- More complex implementation
- "More" menu still hidden

### Drawer Navigation

**Best for**: Extensive navigation structures

**Pros**:
- Full-height panel for navigation
- Good for many items and deep hierarchies
- Can include user profile, settings

**Cons**:
- Requires action to reveal
- Content obscured when open

---

## Mobile Content Patterns

### Cards

- Contained, scannable content blocks
- Perfect for touch interfaces
- Enable easy reorganization and responsive layouts
- Support swipe actions for quick operations

### Lists

- Efficient for displaying collections
- Support swipe actions (delete, archive)
- Easy to scan vertically

### Carousels

- Horizontal scrolling for related content
- Use sparingly—often overlooked by users
- Always show partial next item as hint
- Provide dot indicators for position

### Accordions

- Collapse and expand content sections
- Reduce visual clutter
- Maintain access to all content
- Use for FAQs, settings, secondary info

### Infinite Scroll

- Continuous content loading as users scroll
- Great for social feeds, discovery content
- Provide orientation cues (sticky headers, scroll position)
- Consider pagination for e-commerce, search results

### Pull-to-Refresh

- Gesture-based content refresh
- Intuitive and satisfying interaction
- Use for time-sensitive content (feeds, messages)
- Provide visual feedback during refresh

---

## Touch Target Guidelines

### Minimum Sizes

| Standard | Minimum | Recommended |
|----------|---------|-------------|
| Apple HIG | 44x44 points | 48x48 points |
| Material Design | 48x48 dp | 56x56 dp |
| WCAG 2.5.5 (AAA) | 44x44 CSS px | — |

### Spacing Requirements

- **Between targets**: 8px minimum
- **Touch area padding**: Can extend beyond visual bounds
- **Critical actions**: Consider 56x56px or larger

### Implementation

```css
.button {
  min-width: 48px;
  min-height: 48px;
  padding: 12px 24px;
}

/* Adequate spacing between targets */
.button + .button {
  margin-left: 8px;
}

/* Invisible touch area extension */
.small-icon {
  position: relative;
}

.small-icon::before {
  content: '';
  position: absolute;
  top: -8px;
  right: -8px;
  bottom: -8px;
  left: -8px;
}
```

---

## Touch Gestures

### Common Gestures

| Gesture | Action | Common Use |
|---------|--------|------------|
| Tap | Single touch | Select, activate buttons/links |
| Double Tap | Two quick taps | Zoom, like (social media) |
| Long Press | Press and hold | Context menu, selection mode |
| Swipe | Quick drag | Navigate, dismiss, reveal actions |
| Pinch | Two-finger zoom | Scale content, images, maps |
| Drag | Press and move | Reorder, scroll, sliders |
| Two-finger scroll | Scroll within element | Maps, embedded content |

### Swipe Actions

| Direction | Common Action |
|-----------|---------------|
| Left | Delete, archive, next |
| Right | Mark read, undo, previous |
| Down | Refresh (pull-to-refresh) |
| Up | Load more, expand |

---

## Gesture Design Best Practices

### Discoverability

- Provide visual hints for gesture-based actions
- Use subtle animations to suggest swipe
- Show partial content to hint at more

### Consistency

- Use standard gesture patterns
- Swipe to dismiss should always work the same
- Match platform conventions (iOS vs Android)

### Reversibility

- Allow users to undo gesture actions
- Provide confirmation for destructive actions
- Show "undo" snackbar after deletions

### Accessibility

- Provide tap alternatives for all gestures
- Never make gestures the only way to access features
- Support assistive technologies

### Avoid Conflicts

- Don't override browser/OS gestures
- Test with edge swipes (browser back)
- Consider keyboard users

---

## Touch vs Mouse Considerations

| Aspect | Touch | Mouse |
|--------|-------|-------|
| Hover states | Not available | Commonly used |
| Target size | Larger (44px+) | Smaller possible |
| Precision | Lower | Higher |
| Gestures | Rich support | Limited |
| Feedback | Touch states, haptics | Hover, cursor changes |

### Design Implications

- Don't hide critical info behind hover
- Replace hover feedback with touch states
- Design for finger, not cursor precision
- Consider touch-and-hold for hover equivalents

---

## Mobile Form Patterns

### Form Best Practices

1. **Single-column layouts** — Forms flow vertically
2. **Large inputs** — 48px height minimum
3. **Appropriate input types** — Trigger correct keyboards
4. **Autocomplete enabled** — Reduce typing effort
5. **Inline validation** — Immediate feedback
6. **Minimal required fields** — Reduce friction

### Input Types

```html
<!-- Email keyboard -->
<input type="email" inputmode="email" autocomplete="email">

<!-- Phone keyboard -->
<input type="tel" inputmode="tel" autocomplete="tel">

<!-- Numeric keyboard -->
<input type="text" inputmode="numeric" pattern="[0-9]*">

<!-- Date picker -->
<input type="date">

<!-- URL keyboard -->
<input type="url" inputmode="url" autocomplete="url">
```

### Form Accessibility

- Associate labels with inputs
- Provide clear error messages
- Use aria-describedby for hints
- Support keyboard navigation

---

## Mobile Search Patterns

### Search Best Practices

- **Prominent search bar** — Easily accessible, often in header
- **Voice search** — Microphone icon for voice input
- **Autocomplete** — Suggestions as users type
- **Recent searches** — Quick access to previous queries
- **Smart filters** — Contextual filtering options

### Search UI Patterns

1. **Persistent search bar** — Always visible in header
2. **Expandable search** — Icon that expands to input
3. **Full-screen search** — Dedicated search screen
4. **Search with filters** — Combined search and filter UI

---

## Thumb Zone Design

### Zone Map

```
+------------------+
|    Hard Zone     |  <- Top 1/3: Rarely used actions
|                  |
+------------------+
|     OK Zone      |  <- Middle: Secondary actions
|                  |
+------------------+
|    Easy Zone     |  <- Bottom 1/3: Primary actions
|                  |
+------------------+
```

### Design Recommendations

| Zone | Action Type | Examples |
|------|-------------|----------|
| Easy (bottom) | Primary, frequent | Navigation, main CTAs |
| OK (middle) | Secondary | Content, scrollable lists |
| Hard (top) | Rare, less critical | Settings, profile, search |

### Implementation

- Bottom navigation bar for primary actions
- Floating action button (FAB) in bottom-right
- Important form submit buttons at bottom
- Pull-up sheets for actions/menus
