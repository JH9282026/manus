# iOS and Android Design Guidelines

## Overview

iOS and Android have distinct design languages and conventions. Following platform guidelines creates familiar, intuitive experiences for users.

---

## iOS Human Interface Guidelines

**Design Principles**:
- Clarity: Text is legible, icons are precise, functionality is obvious
- Deference: Content fills screen, subtle UI elements
- Depth: Layers and motion provide hierarchy and vitality

**Navigation**: 
- Tab Bar: 3-5 primary destinations at bottom
- Navigation Bar: Top bar with title and navigation controls
- Modal: Full-screen overlay for focused tasks

**Components**:
- SF Symbols: System icon set, over 3,000 icons
- Buttons: Filled, tinted, plain styles
- Lists: Inset or plain styles
- Sheets: Bottom sheets for actions and options

**Typography**: San Francisco font, Dynamic Type for accessibility

**Spacing**: 8-point grid, generous whitespace

**Gestures**: Swipe back, pull-to-refresh, long-press for context menus

---

## Material Design (Android)

**Design Principles**:
- Material is the metaphor: Inspired by paper and ink
- Bold, graphic, intentional: Deliberate color, imagery, typography
- Motion provides meaning: Responsive, natural, aware

**Navigation**:
- Bottom Navigation: 3-5 primary destinations
- Navigation Drawer: Side menu for many destinations
- Top App Bar: Title, navigation, and actions

**Components**:
- Material Icons: System icon set
- Buttons: Filled, outlined, text styles
- Cards: Elevated containers for content
- FAB: Floating Action Button for primary action

**Typography**: Roboto font, type scale for hierarchy

**Spacing**: 8dp grid, elevation for depth

**Motion**: Meaningful transitions, responsive interactions

---

## Key Differences

**Navigation**:
- iOS: Tab bar at bottom, back button top-left
- Android: Bottom navigation or drawer, back button system-level

**Actions**:
- iOS: Actions in navigation bar or sheets
- Android: FAB for primary action, overflow menu for others

**Modals**:
- iOS: Full-screen or page sheet
- Android: Bottom sheets or dialogs

**Icons**:
- iOS: Outlined style, SF Symbols
- Android: Filled style, Material Icons

**Typography**:
- iOS: San Francisco, larger default sizes
- Android: Roboto, smaller default sizes

**Gestures**:
- iOS: Swipe from left edge to go back
- Android: System back button (gesture or button)

---

## Cross-Platform Considerations

**Shared Design System**: Create components that adapt to platform conventions. Same content, platform-appropriate presentation.

**Platform-Specific Builds**: Design separately for iOS and Android. More work but better platform fit.

**Hybrid Approach**: Core experience is shared, platform-specific patterns for navigation and key interactions.

**Testing**: Test on both platforms. What works on iOS may feel wrong on Android and vice versa.

**User Expectations**: Users expect platform conventions. Breaking them causes confusion and frustration.

---

## Accessibility on Mobile

**Dynamic Type (iOS)**: Support user-selected text sizes. Test at largest sizes.

**Font Scaling (Android)**: Similar to Dynamic Type. Ensure layouts adapt to larger text.

**VoiceOver (iOS) / TalkBack (Android)**: Screen readers. Ensure all elements have labels.

**Touch Targets**: Minimum 44×44px (iOS), 48×48px (Android). Larger is better.

**Color Contrast**: 4.5:1 for text, 3:1 for UI elements. Test in bright sunlight.

**Reduce Motion**: Respect user preference for reduced motion. Provide alternatives to animations.

---

## Platform Resources

**iOS**:
- Human Interface Guidelines: developer.apple.com/design
- SF Symbols: developer.apple.com/sf-symbols
- Design Resources: Figma, Sketch templates

**Android**:
- Material Design: material.io
- Material Icons: fonts.google.com/icons
- Design Resources: Figma, Adobe XD kits

**Both**:
- Platform-specific UI kits for design tools
- Official documentation and best practices
- Regular updates with new OS versions

---
