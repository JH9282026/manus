---
name: mobile-app-design
description: "Design native mobile app interfaces for iOS and Android following platform guidelines and mobile UX best practices. Use for: mobile app UI, iOS design, Android design, mobile-first design, and platform-specific patterns."
---

# Mobile App Design

## Description

Mobile App Design applies platform-specific patterns and conventions for iOS and Android native apps. This skill ensures apps feel native, respect platform guidelines, and provide familiar user experiences.

## When to Use

- Designing native iOS or Android apps
- Creating cross-platform designs
- Adapting web app for mobile app
- Following Human Interface Guidelines or Material Design
- Designing for touch-first experiences

---

## Instructions for AI Agents

### Step 1: Platform Selection

**Platform comparison:**

| Aspect | iOS (HIG) | Android (Material 3) |
|--------|-----------|---------------------|
| Navigation | Tab bar (bottom) | Nav drawer or bottom nav |
| Back | Swipe right, top-left | System back, top-left |
| Typography | SF Pro | Roboto |
| Buttons | Rounded rectangles | Rounded, ripple effect |
| Modals | Bottom sheets, alerts | Dialogs, bottom sheets |
| Spacing base | 8pt grid | 8dp grid |
| Icons | SF Symbols | Material Icons |

### Step 2: iOS Design Patterns

**Human Interface Guidelines essentials:**

```markdown
## iOS Design Patterns

### Navigation
- **Tab Bar**: 5 items max, always visible
- **Navigation Bar**: Title, back button, actions
- **Large Titles**: Collapsible for hierarchy

### Components

#### Navigation Bar
```
┌───────────────────────┐
│  ← Back     Title    ⋯  │  44pt height
└───────────────────────┘
```

#### Large Title (Collapsed)
```
┌───────────────────────┐
│  ← Back              +  │
│  Large Title           │  34pt bold
└───────────────────────┘
```

#### Tab Bar
```
┌───────────────────────┐
│  🏠     🔍    ➕    👤   │  49pt + safe area
│ Home  Search Add  Profile│
└───────────────────────┘
```

#### Action Sheet
```
┌───────────────────────┐
│  Action One            │
├───────────────────────┤
│  Action Two            │
├───────────────────────┤
│  Destructive (red)     │
├───────────────────────┤
│                        │
│       Cancel           │
└───────────────────────┘
```

### Sizing
| Element | Size |
|---------|------|
| Touch target | 44×44pt minimum |
| Tab bar | 49pt + safe area |
| Nav bar | 44pt + status bar |
| Button height | 44pt |
| Large title | 34pt |
| Body text | 17pt |
| Caption | 12pt |
| Margin | 16pt |

### Safe Areas
- Status bar: ~47pt (varies with notch)
- Home indicator: 34pt
- Design within safe area margins
```

### Step 3: Android Design Patterns

**Material Design 3 essentials:**

```markdown
## Android / Material 3 Patterns

### Navigation
- **Bottom Navigation**: 3-5 items
- **Navigation Drawer**: For many destinations
- **Navigation Rail**: Tablet landscape

### Components

#### Top App Bar
```
┌───────────────────────┐
│  ☰      Title     🔍  ⋮  │  64dp height
└───────────────────────┘
```

#### Bottom Navigation
```
┌───────────────────────┐
│  🏠     🔍     ❤️     👤  │  80dp height
│ Home  Search  Saved Profile│  with labels
└───────────────────────┘
```

#### FAB (Floating Action Button)
```
                     ┌───┐
                     │ + │  56dp
                     └───┘
  16dp from edge, 16dp from bottom nav
```

#### Bottom Sheet
```
┌───────────────────────┐
│        ─────           │  Drag handle
│                        │
│  Sheet Title           │
│                        │
│  Content here          │
│                        │
│  [   Action Button   ] │
└───────────────────────┘
```

### Sizing
| Element | Size |
|---------|------|
| Touch target | 48×48dp minimum |
| Bottom nav | 80dp |
| Top app bar | 64dp |
| FAB | 56dp |
| Button height | 40dp |
| Body text | 16sp |
| Margin | 16dp |
```

### Step 4: Cross-Platform Strategy

**Unified approach:**

```markdown
## Cross-Platform Design Strategy

### Shared Elements
- Core brand identity (colors, fonts where possible)
- Icon style and meaning
- Information architecture
- Core user flows

### Platform-Specific Adaptations

| Element | iOS | Android |
|---------|-----|----------|
| Primary font | SF Pro | Roboto |
| Navigation | Tab bar | Bottom nav |
| Back action | Swipe + button | System back |
| Primary action | Button/nav bar | FAB |
| Alerts | iOS alerts | Material dialogs |
| Toggle | iOS switch | Material switch |
| Selection | Checkmark | Checkbox |

### When to Differ
- Navigation patterns (respect muscle memory)
- System-provided components
- Gesture behaviors
- Typography system

### When to Unify
- Brand expression
- Feature parity
- Visual style
- Interaction concepts
```

---

## Example Input/Output

### Example Input

```markdown
**Project**: TaskFlow mobile app
**Platforms**: iOS and Android
**Key screens**: Task list, task detail, project overview
**Design tokens**: Violet primary, existing component library
```

### Example Output

```markdown
## Mobile App Design: TaskFlow

### Platform Strategy
**Approach**: Platform-native navigation with unified visual identity

---

### iOS Design

#### Task List Screen
```
┌───────────────────────┐
│  ┌───────────────────┐  │  <- Dynamic Island area
├──┴───────────────────┴──┤
│  Tasks                 +  │  <- Nav bar with add
│  My Tasks                 │  <- Large title
├───────────────────────┤
│  [🔍 Search tasks...    ]  │  <- Search bar
├───────────────────────┤
│  TODAY                    │  <- Section header
├───────────────────────┤
│  ○  Review homepage       │
│     Acme • Due today   >  │
├───────────────────────┤
│  ○  Client feedback       │
│     Beta • Due today   >  │
├───────────────────────┤
│  ●  Final assets ✓        │  <- Completed
│     Acme • Completed   >  │
├───────────────────────┤
│  UPCOMING                 │
├───────────────────────┤
│  ○  Sprint planning       │
│     Team • Tomorrow    >  │
│                           │
├───────────────────────┤
│                           │  <- Home indicator
│  🏠    📁    ✅    👤     │  <- Tab bar
│ Home  Proj  Tasks  Me    │
└───────────────────────┘
```

**iOS Specifications**:
- Large title: SF Pro Bold 34pt
- Section header: SF Pro Semibold 13pt, uppercase, Gray-500
- Task title: SF Pro 17pt
- Task meta: SF Pro 15pt, Gray-500
- Tab bar icons: SF Symbols, 25pt
- Row height: 76pt minimum
- Swipe actions: Complete (green), Delete (red)

---

### Android Design

#### Task List Screen
```
┌───────────────────────┐
│  [status bar]            │
├───────────────────────┤
│  ←  My Tasks         🔍  │  <- Top app bar
├───────────────────────┤
│  [Filter chips row]      │  <- Filter chips
│  (All) (Today) (Week)    │
├───────────────────────┤
│  Today                   │
├───────────────────────┤
│  ☐  Review homepage      │
│     Acme • Due today     │
├───────────────────────┤
│  ☐  Client feedback      │
│     Beta • Due today     │
├───────────────────────┤
│  ☑  Final assets         │  <- Completed
│     Acme • Completed     │
├───────────────────────┤
│  Tomorrow                │
├───────────────────────┤
│  ☐  Sprint planning      │
│     Team • Tomorrow      │
│                     ┌───┐│
│                     │ + ││  <- FAB
│                     └───┘│
├───────────────────────┤
│  🏠    📁    ✅    👤    │  <- Bottom nav
│ Home  Proj  Tasks  Me   │
└───────────────────────┘
```

**Android Specifications**:
- Top app bar: Roboto Medium 22sp
- Section header: Roboto Medium 14sp, uppercase
- Task title: Roboto Regular 16sp
- Task meta: Roboto Regular 14sp, on-surface-variant
- FAB: 56dp, Violet-500, + icon
- Bottom nav: 80dp, Material icons
- Row height: 72dp minimum
- Checkbox: Material checkbox 24dp

---

### Platform Comparison

| Element | iOS | Android |
|---------|-----|----------|
| Add task | Nav bar + button | FAB |
| Task completion | Custom circle | Material checkbox |
| Filtering | Scope bar | Filter chips |
| Row disclosure | Chevron > | None (tap row) |
| Search | Collapsing search | Search icon → expand |
| Completed style | Strikethrough | Checkbox filled |
| Swipe actions | Left/Right | Left only |
```

---

## Resources

### Platform Guidelines
- **iOS**: https://developer.apple.com/design/human-interface-guidelines
- **Android**: https://m3.material.io

### Design Kits
- iOS Design Kit (Figma)
- Material 3 Design Kit (Figma)

---

## Success Criteria

### Minimum Requirements
- [ ] Platform conventions followed
- [ ] Touch targets meet platform minimums
- [ ] Safe areas respected
- [ ] Native navigation patterns used

### Quality Indicators
- [ ] Feels native to each platform
- [ ] Gestures work as expected
- [ ] Visual identity maintained across platforms
- [ ] Accessibility features supported

---

## Related Skills

- **Previous**: `responsive_design.md` - Web responsive foundations
- **Next**: `interaction_design.md` - Micro-interactions
- **Related**: `accessibility_review.md` - Mobile accessibility

## References

- [Ios Android Guidelines](references/ios-android-guidelines.md)
- [Mobile Design Principles](references/mobile-design-principles.md)
- [Mobile Interaction Patterns](references/mobile-interaction-patterns.md)
