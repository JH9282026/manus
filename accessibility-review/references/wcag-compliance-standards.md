# WCAG Compliance Standards

## Overview

Web Content Accessibility Guidelines (WCAG) provide the foundation for digital accessibility. Understanding compliance levels and success criteria is essential for conducting thorough accessibility reviews.

---

## WCAG 2.1 Levels

**Level A (Minimum)**: Basic web accessibility features that must be present. Includes text alternatives for non-text content, keyboard accessibility, sufficient time to read content, and no content that causes seizures.

**Level AA (Mid-range)**: Addresses the biggest barriers for disabled users. Includes color contrast requirements (4.5:1 for normal text), resize text up to 200%, multiple ways to find pages, and visible focus indicators.

**Level AAA (Highest)**: Enhanced accessibility for specialized audiences. Includes sign language interpretation, extended audio descriptions, and 7:1 contrast ratios.

---

## Four Principles (POUR)

**Perceivable**: Information must be presentable to users in ways they can perceive. Provide text alternatives, captions, adaptable content, and distinguishable foreground/background.

**Operable**: Interface components must be operable. Ensure keyboard accessibility, sufficient time, no seizure-inducing content, and navigable structure.

**Understandable**: Information and operation must be understandable. Make text readable, pages appear and operate predictably, and help users avoid/correct mistakes.

**Robust**: Content must be robust enough for interpretation by assistive technologies. Maximize compatibility with current and future tools.

---

## Success Criteria Categories

**Perceivable**: 1.1 Text Alternatives, 1.2 Time-based Media, 1.3 Adaptable, 1.4 Distinguishable

**Operable**: 2.1 Keyboard Accessible, 2.2 Enough Time, 2.3 Seizures, 2.4 Navigable, 2.5 Input Modalities

**Understandable**: 3.1 Readable, 3.2 Predictable, 3.3 Input Assistance

**Robust**: 4.1 Compatible

---

## Common Compliance Issues

**Color Contrast**: Text and background combinations failing 4.5:1 ratio. Test with contrast checkers and provide sufficient luminosity differences.

**Missing Alt Text**: Images without descriptive alternatives. Every informative image needs meaningful alt text; decorative images should have empty alt attributes.

**Keyboard Traps**: Users unable to navigate away using keyboard alone. Ensure all interactive elements are keyboard accessible with visible focus.

**Form Labels**: Input fields without associated labels. Every form control needs a programmatically associated label element.

**Heading Structure**: Skipped heading levels or improper hierarchy. Use h1-h6 in logical order without skipping levels.

---

## Testing Methodology

**Automated Testing**: Use tools like axe, WAVE, or Lighthouse for initial scans. Automated tools catch ~30-40% of issues.

**Manual Testing**: Keyboard navigation, screen reader testing, zoom testing, and color contrast verification. Essential for comprehensive coverage.

**Assistive Technology Testing**: Test with NVDA, JAWS, VoiceOver, and TalkBack. Real-world usage reveals issues automated tools miss.

**User Testing**: Include people with disabilities in testing. Their lived experience provides invaluable insights.

---
