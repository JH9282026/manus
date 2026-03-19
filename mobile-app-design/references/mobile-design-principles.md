# Mobile Design Principles

## Overview

Mobile design requires different considerations than desktop. Smaller screens, touch interaction, and on-the-go usage demand focused, efficient interfaces.

---

## Mobile-First Thinking

**Start with Mobile**: Design for smallest screen first, then scale up. Forces prioritization of essential content.

**Progressive Enhancement**: Add features and content for larger screens. Mobile gets core experience, desktop gets enhancements.

**Benefits**: 
- Forces focus on essential features
- Easier to add than remove
- Better performance (load only what's needed)
- Aligns with mobile-majority usage

**Process**: 
1. Identify core user tasks
2. Design mobile experience for those tasks
3. Add supporting features for tablet
4. Add enhancements for desktop

---

## Touch Targets and Gestures

**Minimum Touch Target**: 44×44px (Apple), 48×48px (Android). Smaller targets cause errors.

**Spacing**: Minimum 8px between touch targets. Prevents accidental taps.

**Thumb Zone**: Bottom third of screen is easiest to reach with thumb. Place primary actions there.

**Common Gestures**:
- Tap: Primary action
- Double-tap: Zoom (avoid for other actions)
- Long-press: Secondary action, context menu
- Swipe: Navigate, delete, reveal actions
- Pinch: Zoom in/out
- Pull-to-refresh: Reload content

**Gesture Discoverability**: Gestures are invisible. Provide visual hints or tutorials for non-standard gestures.

---

## Mobile Navigation Patterns

**Tab Bar (iOS) / Bottom Navigation (Android)**: 3-5 primary sections. Always visible. Easy thumb access.

**Hamburger Menu**: Hidden menu revealed by icon. Saves space but hides navigation. Use for secondary navigation.

**Top Navigation**: Tabs or segments at top. Good for related content (e.g., inbox categories).

**Gesture Navigation**: Swipe between screens. Invisible but efficient once learned.

**Choosing Pattern**: 
- 3-5 primary sections: Tab bar
- Many sections: Hamburger menu
- Related content: Top tabs
- Linear flow: Gesture navigation

**Avoid**: Too many navigation patterns in one app. Stick to 1-2 patterns for consistency.

---

## Content Prioritization

**One Primary Action**: Each screen should have one clear primary action. Secondary actions should be less prominent.

**Progressive Disclosure**: Show essential information first. Hide details behind taps or expansion.

**Chunking**: Break content into digestible pieces. Use cards, lists, or sections.

**Scrolling vs Pagination**: Scrolling is natural on mobile. Use for continuous content. Pagination for distinct sections.

**Fold Myth**: Users scroll. Don't cram everything above fold. But put most important content first.

---

## Mobile Typography

**Minimum Font Size**: 16px for body text. Smaller text is hard to read on mobile.

**Line Length**: 50-75 characters per line ideal. Mobile screens naturally limit line length.

**Line Height**: 1.4-1.6× font size for body text. Improves readability on small screens.

**Hierarchy**: Use size, weight, and spacing to create clear hierarchy. Color alone isn't enough.

**System Fonts**: iOS San Francisco, Android Roboto. Fast loading, optimized for screens.

**Avoid**: Small text, long paragraphs, low contrast, all caps for long text.

---

## Mobile Performance

**Load Time**: Target 3 seconds or less. Mobile users are impatient and may have slow connections.

**Image Optimization**: Compress images, use appropriate formats (WebP), serve responsive images.

**Lazy Loading**: Load images as user scrolls. Reduces initial load time.

**Minimize Requests**: Combine files, use sprites, inline critical CSS. Each request adds latency.

**Offline Support**: Cache content for offline access. Progressive Web Apps enable offline functionality.

**Testing**: Test on real devices with throttled connections. Emulators don't show real performance.

---
