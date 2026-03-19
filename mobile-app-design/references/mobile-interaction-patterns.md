# Mobile Interaction Patterns

## Overview

Mobile interaction patterns are proven solutions for common design problems. Using established patterns creates familiar, intuitive experiences.

---

## Onboarding Patterns

**Carousel/Tutorial**: Swipeable screens explaining key features. Keep to 3-5 screens max.

**Progressive Onboarding**: Teach features in context as user encounters them. Less overwhelming.

**Account Creation**: 
- Option 1: Create account upfront (high friction but captures users)
- Option 2: Guest access, prompt to create account later (low friction)
- Option 3: Social sign-in (fastest, but privacy concerns)

**Permissions**: Request permissions in context when needed, not all upfront. Explain why you need each permission.

**Best Practices**: 
- Show value before asking for commitment
- Make it skippable
- Keep it brief
- Use visuals, not just text

---

## Form Patterns

**Input Types**: Use appropriate keyboard for input type (email, phone, number, URL). Reduces errors and speeds entry.

**Autofill**: Support autofill for common fields (name, email, address, payment). Dramatically speeds up forms.

**Inline Validation**: Validate as user types or on blur. Immediate feedback prevents errors.

**Error Handling**: 
- Show errors inline, near the field
- Explain what's wrong and how to fix it
- Don't clear field on error (frustrating)

**Multi-Step Forms**: 
- Show progress indicator
- Allow back navigation
- Save progress
- Keep each step focused (one topic per step)

**Smart Defaults**: Pre-fill fields when possible. Reduces user effort.

---

## Search Patterns

**Search Box Placement**: Top of screen, always accessible. Tap to expand or navigate to search screen.

**Auto-complete**: Suggest queries as user types. Speeds search and aids discovery.

**Recent Searches**: Show recent searches when search box is tapped. Quick access to common searches.

**Filters**: 
- Chips for active filters (easy to remove)
- Filter button opens sheet with all filter options
- Show number of active filters on button

**Results**: 
- Show number of results
- Highlight search terms
- Provide sorting options
- Handle zero results gracefully (suggestions, alternatives)

**Voice Search**: Microphone icon in search box. Useful for hands-free or difficult-to-type queries.

---

## List and Feed Patterns

**Infinite Scroll**: Load more content as user scrolls. Good for continuous feeds (social media, news).

**Pull-to-Refresh**: Pull down to reload content. Standard pattern, users expect it.

**Swipe Actions**: Swipe left/right to reveal actions (delete, archive, etc.). Efficient but needs visual hints.

**Empty States**: 
- Explain why list is empty
- Provide action to add content
- Use illustration or icon
- Make it encouraging, not discouraging

**Loading States**: 
- Skeleton screens (show content structure while loading)
- Spinners for short waits
- Progress bars for longer operations

**Pagination**: Load more button or automatic loading. Infinite scroll is more common on mobile.

---

## Navigation Patterns

**Tabs**: 3-5 primary sections. Always visible at bottom (iOS) or top (Android).

**Hamburger Menu**: Hidden menu for secondary navigation. Tap icon to reveal.

**Drill-Down**: Tap to go deeper into hierarchy. Back button to return. Common for settings, categories.

**Modal**: Full-screen overlay for focused task. Close button or swipe down to dismiss.

**Bottom Sheet**: Partial overlay from bottom. For actions, options, or supplementary content.

**Breadcrumbs**: Rare on mobile (space constraints). Use navigation bar title and back button instead.

---

## Feedback and Confirmation

**Toast/Snackbar**: Brief message at bottom of screen. Confirms action, shows status. Auto-dismisses.

**Alert/Dialog**: Modal message requiring user response. Use sparingly (interrupts flow).

**Inline Messages**: Show success/error message in context. Less disruptive than modal.

**Loading Indicators**: 
- Spinner for indeterminate wait
- Progress bar for determinate wait
- Skeleton screen for content loading

**Haptic Feedback**: Subtle vibration confirms action. Use for important actions (payment, delete).

**Animation**: Smooth transitions provide feedback. Button press, screen transition, etc.

---
