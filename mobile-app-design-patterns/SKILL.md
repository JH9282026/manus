---
name: mobile-app-design-patterns
description: "Design native mobile app interfaces following iOS and Android platform conventions and interaction patterns. Use for: applying iOS Human Interface Guidelines and Material Design principles, designing touch-friendly interfaces, creating native navigation patterns, handling mobile gestures, and optimizing for platform-specific UX expectations."
---

# Mobile App Design

Design native mobile app interfaces following iOS and Android platform conventions and interaction patterns.

# Skill: Mobile App Design

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Mobile App Design |
| **Category** | Responsive & Platform Design |
| **Phase** | 4 - Responsive & Platform |
| **Estimated Time** | 60-90 minutes |
| **Dependencies** | `component_design.md`, `responsive_design.md` |
| **Outputs** | Mobile app screens following platform conventions |

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

## Using the Reference Files

### When to Read Each Reference

**`./references/mobile-app-design-taskflow.md`** — Read when you need detailed guidance on mobile app design taskflow aspects of this skill.
