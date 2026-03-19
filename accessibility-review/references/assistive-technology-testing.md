# Assistive Technology Testing

## Overview

Testing with assistive technologies is crucial for understanding real-world accessibility. Screen readers, magnifiers, voice control, and alternative input devices reveal how disabled users actually experience your interface.

---

## Screen Reader Testing

**NVDA (Windows, Free)**: Most popular free screen reader. Download from nvaccess.org. Use NVDA+N for menu, NVDA+Q to quit. Navigate with arrow keys, H for headings, K for links, F for forms.

**JAWS (Windows, Commercial)**: Industry standard enterprise screen reader. Expensive but widely used in corporate environments. Similar navigation to NVDA with some command differences.

**VoiceOver (macOS/iOS, Built-in)**: Apple's screen reader. Activate with Cmd+F5 on Mac, triple-click home on iOS. Use VO keys (Control+Option) for navigation. Rotor gesture on iOS for quick navigation.

**TalkBack (Android, Built-in)**: Google's screen reader. Activate in Settings > Accessibility. Swipe right/left to navigate, double-tap to activate, two-finger swipe to scroll.

---

## Screen Reader Testing Checklist

**Page Structure**: Can users understand page layout? Are landmarks properly identified? Is heading hierarchy logical?

**Navigation**: Can users find and use navigation menus? Are skip links present? Can users navigate by headings, landmarks, and links?

**Forms**: Are all form fields properly labeled? Do error messages make sense? Can users complete forms efficiently?

**Dynamic Content**: Are ARIA live regions announcing updates? Do modals trap focus appropriately? Are loading states communicated?

**Images and Media**: Do images have meaningful alt text? Are decorative images hidden? Do videos have captions and transcripts?

---

## Keyboard Navigation Testing

**Tab Order**: Press Tab to move forward, Shift+Tab to move backward. Verify logical order matching visual layout.

**Focus Indicators**: Ensure visible focus indicators on all interactive elements. Default browser outlines are acceptable but custom indicators should be high contrast.

**Keyboard Traps**: Verify users can escape all components using keyboard alone. Modals should trap focus but allow Escape key to close.

**Shortcuts**: Test common shortcuts like Enter to activate, Space for checkboxes, Arrow keys for radio groups and select elements.

**Skip Links**: Verify skip navigation links appear on focus and jump to main content.

---

## Magnification and Zoom Testing

**Browser Zoom**: Test at 200% zoom (WCAG AA requirement). Verify no horizontal scrolling, all content remains visible, and functionality preserved.

**Text Spacing**: Test with increased text spacing (line height 1.5x, paragraph spacing 2x, letter spacing 0.12x, word spacing 0.16x). Content should remain readable without overlap.

**Screen Magnifiers**: Test with ZoomText (Windows) or built-in magnifiers. Verify focus tracking, smooth scrolling, and readable magnified content.

**Responsive Design**: Verify mobile layouts work well for users who zoom on desktop. Consider mobile-first approach for better zoom compatibility.

---

## Voice Control Testing

**Voice Control (iOS/macOS)**: Test with Apple's Voice Control. Verify all interactive elements have voice-accessible names. Test commands like 'Tap [name]', 'Show numbers', 'Show grid'.

**Voice Access (Android)**: Google's voice control system. Similar testing approach to iOS Voice Control. Verify element labels are speakable.

**Dragon NaturallySpeaking**: Popular third-party voice control. Test form filling, navigation, and command execution.

**Testing Checklist**: Can users navigate without mouse? Are all interactive elements voice-accessible? Do custom controls have appropriate names?

---

## Alternative Input Devices

**Switch Access**: Single or dual switch navigation for users with limited mobility. Test with Android Switch Access or iOS Switch Control.

**Eye Tracking**: Devices like Tobii allow eye-gaze control. Ensure targets are large enough (minimum 44x44px) and well-spaced.

**Mouth Stick/Head Pointer**: Physical pointing devices. Verify keyboard accessibility covers these use cases.

**Sip-and-Puff**: Breath-controlled input. Relies on keyboard accessibility and proper focus management.

---
