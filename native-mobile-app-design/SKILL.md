---
name: native-mobile-app-design
description: "Design native mobile applications following iOS and Android platform guidelines. Use for: iOS app design (HIG), Android app design (Material Design), mobile navigation patterns, platform-specific UI components, mobile gesture design, adaptive layouts, accessibility on mobile, and platform-appropriate interaction patterns."
---

# Native Mobile App Design

Design native mobile applications that follow iOS Human Interface Guidelines and Android Material Design conventions for intuitive, platform-appropriate user experiences.

## Overview

Native mobile app design requires understanding and respecting platform conventions. iOS and Android users have fundamentally different expectations — from navigation placement to gesture patterns to typography. This skill covers platform-specific design systems, navigation patterns, component usage, gesture design, and accessibility for both iOS and Android.

## Platform Comparison at a Glance

| Element | iOS (HIG) | Android (Material Design 3) | Reference |
|---------|-----------|---------------------------|-----------|
| Navigation | Tab bar (bottom) | Bottom nav bar or nav drawer | `/references/ios-design-guidelines.md` |
| Back navigation | Swipe from left edge | System back button/gesture | `/references/android-design-guidelines.md` |
| Typography | SF Pro (system font) | Roboto or brand font | Platform-specific |
| Button style | Rounded rectangles, text buttons | Contained, outlined, FAB | Platform-specific |
| Primary action | Prominent button or nav bar button | FAB (Floating Action Button) | Platform-specific |
| Alerts | Centered modal dialog | Bottom sheet or dialog | Platform-specific |
| Pull to refresh | Built-in UIRefreshControl | SwipeRefreshLayout | Both platforms |
| Status bar | Translucent, blends with content | System-controlled color | Platform-specific |
| Tab bar position | Bottom (always) | Bottom (preferred) or top | Platform-specific |
| Search | Search bar in nav or pull-down | Search icon in top app bar | Platform-specific |

## iOS Design Framework (HIG)

### Navigation Patterns

| Pattern | Use Case | Components |
|---------|----------|-----------|
| Tab Bar | 3–5 top-level destinations | UITabBarController, SF Symbols icons |
| Navigation Stack | Hierarchical content drill-down | UINavigationController, push/pop |
| Modal | Focused task, interruption | Sheet (partial/full), alert |
| Sidebar | iPad primary navigation | UISplitViewController |

### iOS Component Usage

| Component | When to Use | Specs |
|-----------|-------------|-------|
| Navigation Bar | Top of every screen in a stack | 44pt height, large/small title options |
| Tab Bar | Persistent bottom navigation | 49pt height, max 5 tabs |
| Search Bar | List filtering, content discovery | Expandable from nav bar or inline |
| Segmented Control | 2–5 mutually exclusive views | Pill-style toggle |
| Action Sheet | Multiple actions from context | Bottom sheet with options |
| Alert | Important decisions, confirmations | Centered dialog, 2–3 buttons max |
| SwiftUI Menu | Contextual actions | Long-press or three-dot menu |

### iOS Typography Scale

| Style | Size | Weight | Use |
|-------|------|--------|-----|
| Large Title | 34pt | Bold | Screen titles (first in nav) |
| Title 1 | 28pt | Bold | Section headers |
| Title 2 | 22pt | Bold | Subsections |
| Title 3 | 20pt | Semibold | Card headers |
| Headline | 17pt | Semibold | Emphasis text |
| Body | 17pt | Regular | Main content text |
| Callout | 16pt | Regular | Secondary content |
| Subheadline | 15pt | Regular | Supporting text |
| Footnote | 13pt | Regular | Tertiary info |
| Caption 1 | 12pt | Regular | Labels, metadata |
| Caption 2 | 11pt | Regular | Timestamps |

## Android Design Framework (Material Design 3)

### Navigation Patterns

| Pattern | Use Case | Components |
|---------|----------|-----------|
| Bottom Navigation | 3–5 top-level destinations | NavigationBar (MD3) |
| Navigation Drawer | 6+ destinations or secondary navigation | ModalNavigationDrawer |
| Navigation Rail | Tablet/foldable primary nav | NavigationRail (side rail) |
| Tabs | Switching between related content groups | TabRow, fixed or scrollable |

### Material Design 3 Components

| Component | When to Use | Variants |
|-----------|-------------|----------|
| Top App Bar | Screen title, navigation, actions | Center-aligned, small, medium, large |
| FAB | Primary action on screen | Regular, small, large, extended |
| Bottom Sheet | Secondary content or actions | Standard, modal |
| Snackbar | Brief feedback messages | With or without action |
| Chip | Filters, selections, input tags | Assist, filter, input, suggestion |
| Card | Container for related content | Elevated, filled, outlined |
| Dialog | Critical decisions | Basic, full-screen |
| Search Bar | Content discovery | In top app bar or standalone |

### Material Design 3 Typography

| Style | Size | Weight | Use |
|-------|------|--------|-----|
| Display Large | 57sp | Regular | Hero headlines |
| Display Medium | 45sp | Regular | Large display text |
| Display Small | 36sp | Regular | Smaller display |
| Headline Large | 32sp | Regular | Screen titles |
| Headline Medium | 28sp | Regular | Section headers |
| Title Large | 22sp | Regular | Top app bar |
| Title Medium | 16sp | Medium | Card headers |
| Body Large | 16sp | Regular | Main text |
| Body Medium | 14sp | Regular | Secondary text |
| Label Large | 14sp | Medium | Button text |
| Label Medium | 12sp | Medium | Nav labels |

## Cross-Platform Design Decisions

| Decision | iOS Approach | Android Approach | When to Diverge |
|----------|-------------|-----------------|-----------------|
| Back button | Don't show — use swipe gesture | Show in top app bar | Always platform-specific |
| Primary action | Text button in nav bar | FAB | Follow platform convention |
| List actions | Swipe-to-reveal | Long-press context menu | Follow platform convention |
| Settings | Separate settings screen | Settings in nav drawer or dedicated screen | Either platform |
| Onboarding | Page-based walkthrough | Same or skip entirely | Can share approach |
| Pull to refresh | Standard pull-down | Same pattern | Can share approach |
| Share | Share sheet (system) | Share sheet (system) | System-handled on both |

## Touch Target & Spacing

| Element | iOS Minimum | Android Minimum | Recommended |
|---------|------------|-----------------|-------------|
| Touch target | 44×44pt | 48×48dp | 48×48 on both |
| Button padding | 8pt | 8dp | 12+ for primary actions |
| List row height | 44pt minimum | 48dp minimum | 56–72 for content-rich rows |
| Icon size (nav) | 25×25pt (SF Symbols) | 24×24dp (Material Icons) | Platform standard |
| Text input height | 44pt | 56dp | Platform standard |
| Bottom spacing (safe area) | Respect home indicator (34pt) | Respect gesture nav bar | Always account for system UI |

## Gesture Design

| Gesture | iOS | Android | Use Case |
|---------|-----|---------|----------|
| Tap | Universal | Universal | Primary interaction |
| Swipe left/right | Delete, actions on list items | Navigate between tabs | Context-dependent |
| Swipe from left edge | Back navigation | Back navigation (system) | Platform-handled |
| Long press | Context menu, preview | Context menu | Secondary actions |
| Pull down | Refresh, search | Refresh | Update content |
| Pinch | Zoom in/out | Zoom in/out | Images, maps |
| Double tap | Zoom, like | Zoom | Context-dependent |

## Accessibility Requirements

| Requirement | iOS Implementation | Android Implementation |
|------------|-------------------|----------------------|
| Screen reader | VoiceOver labels on all interactive elements | TalkBack contentDescription |
| Dynamic type | Support all Dynamic Type sizes | Support font scaling (sp units) |
| Color contrast | 4.5:1 minimum for text | 4.5:1 minimum for text |
| Touch targets | 44×44pt minimum | 48×48dp minimum |
| Reduce Motion | Respect UIAccessibility.isReduceMotionEnabled | Respect ANIMATOR_DURATION_SCALE |
| Dark mode | Support light/dark appearance | Support Material You dark theme |

## Best Practices

- **Follow platform conventions** — iOS users expect tab bars at the bottom; Android users expect navigation drawers or bottom nav
- **Use system fonts** — SF Pro on iOS, Roboto on Android look "right" and support Dynamic Type
- **Design for one-handed use** — place critical actions in the thumb zone (bottom 40% of screen)
- **Test on real devices** — simulators miss performance issues, haptics, and gesture nuances
- **Support both light and dark mode** — it's expected on both platforms in 2026
- **Respect the safe area** — never place interactive elements behind notches, home indicators, or system bars

## Using the Reference Files

**`/references/ios-design-guidelines.md`** — Read when designing for iOS. Covers HIG principles, SF Symbols, navigation patterns, component usage, and iOS-specific interaction design.

**`/references/android-design-guidelines.md`** — Read when designing for Android. Covers Material Design 3, component library, navigation patterns, typography system, and Android-specific patterns.
