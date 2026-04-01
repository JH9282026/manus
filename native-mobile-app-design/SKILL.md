---
name: "native-mobile-app-design"
description: "Design native mobile applications following iOS Human Interface Guidelines and Android Material Design standards with platform-specific patterns and components. Use for: iOS app design, Android app design, mobile UI design, platform-specific navigation, mobile component libraries, cross-platform design systems."
---

# Native Mobile App Design

Design native mobile applications following iOS and Android platform-specific guidelines and patterns.

## Overview

Create platform-appropriate mobile app designs that leverage native iOS (Human Interface Guidelines) and Android (Material Design) conventions. Cover navigation patterns, typography, components, gestures, and accessibility.

## Platform Comparison

| Aspect | iOS (HIG) | Android (Material Design) |
|--------|-----------|--------------------------|
| Navigation | Tab bar (bottom), back button (top-left) | Bottom nav, hamburger, back (system) |
| Typography | San Francisco | Roboto |
| Icons | SF Symbols | Material Icons |
| Buttons | Rounded rectangles | FAB, text, outlined, contained |
| Lists | Grouped/inset style | Single-line, two-line, three-line |
| Modals | Sheets (bottom), alerts | Bottom sheets, dialogs |
| Gestures | Swipe back, force touch | Swipe, long press |

## Design Token Comparison

| Token | iOS | Android |
|-------|-----|---------|
| Corner radius | 10-14px (cards), 8px (buttons) | 4-16px (shape system) |
| Elevation | Subtle shadows | Defined elevation levels (0-24dp) |
| Spacing grid | 8pt grid | 4dp/8dp grid |
| Min touch target | 44×44pt | 48×48dp |
| Status bar height | 44pt (notch), 20pt (legacy) | 24dp |
| Navigation bar | 44pt | 56-64dp |

## Cross-Platform Strategy

| Approach | When to Use |
|----------|-------------|
| Fully native per platform | Premium UX, platform-specific features |
| Shared design with platform tweaks | Consistent brand, adapted patterns |
| Single design across platforms | Speed to market, limited resources |

## Using the Reference Files

### When to Read Each Reference

**`/references/ios-design-guidelines.md`** — Read when designing for iOS, implementing HIG patterns, or creating iOS-specific components.

**`/references/android-design-guidelines.md`** — Read when designing for Android, implementing Material Design, or creating Android-specific components.
