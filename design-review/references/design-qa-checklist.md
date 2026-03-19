# Design QA Checklist

## Overview

Design QA ensures designs are complete, consistent, and ready for development. A thorough checklist catches issues before handoff, reducing back-and-forth and implementation errors.

---

## Visual Consistency

**Typography**: 
- All text uses defined styles from design system
- Font sizes, weights, and line heights are consistent
- No rogue text styles or one-off sizes
- Hierarchy is clear and consistent across screens

**Colors**: 
- All colors are from defined palette
- No hex codes that aren't in the design system
- Color usage is consistent (e.g., primary button always same blue)
- Sufficient contrast ratios (4.5:1 for text, 3:1 for UI elements)

**Spacing**: 
- Consistent spacing scale used throughout (e.g., 4px, 8px, 16px, 24px)
- No arbitrary spacing values
- Padding and margins follow system rules
- Alignment is precise (not 'close enough')

---

## Component Consistency

**States**: Every interactive component has all necessary states:
- Default
- Hover
- Active/Pressed
- Focus
- Disabled
- Loading (if applicable)
- Error (for form inputs)

**Variants**: All component variants are documented:
- Sizes (small, medium, large)
- Types (primary, secondary, tertiary buttons)
- Configurations (with/without icons, etc.)

**Usage**: Components are used consistently:
- Same component for same purpose across all screens
- No reinventing components that already exist
- Proper component instances, not detached copies

---

## Content and Copy

**Completeness**: 
- No lorem ipsum or placeholder text
- All labels, buttons, and messages have final copy
- Error messages are written and designed
- Empty states have content and visuals

**Consistency**: 
- Terminology is consistent (don't call it 'account' in one place and 'profile' in another)
- Tone and voice match brand guidelines
- Button labels follow consistent pattern (verb-first, e.g., 'Save changes')

**Accuracy**: 
- Copy is grammatically correct
- No typos or spelling errors
- Technical terms are used correctly

---

## Responsive Behavior

**Breakpoints**: Designs exist for all target breakpoints:
- Mobile (320px, 375px, 414px)
- Tablet (768px, 1024px)
- Desktop (1280px, 1440px, 1920px)

**Adaptation**: Clear how design adapts between breakpoints:
- Navigation changes (hamburger menu on mobile)
- Grid adjustments (3 columns to 1 column)
- Content reflow and stacking order
- Image scaling and cropping

**Edge Cases**: Considered how design handles:
- Very long text (names, addresses, etc.)
- Very short text
- Missing content (no profile photo, etc.)
- Large amounts of content (long lists, etc.)

---

## Interaction and Flow

**User Flows**: 
- All user paths are designed (happy path and error paths)
- No dead ends or missing screens
- Back/cancel actions are clear
- Success and error states are designed

**Transitions**: 
- Specified how screens connect (slide, fade, etc.)
- Loading states are designed
- Skeleton screens or spinners for slow operations
- Micro-interactions are documented

**Feedback**: 
- User actions have clear feedback (button press, form submission, etc.)
- Error messages are helpful and actionable
- Success confirmations are present
- Progress indicators for multi-step processes

---

## Accessibility

**Color Contrast**: 
- Text meets WCAG AA standards (4.5:1 for normal, 3:1 for large)
- UI elements meet 3:1 contrast requirement
- Don't rely on color alone to convey information

**Focus States**: 
- All interactive elements have visible focus indicators
- Focus order is logical
- Skip links are present for keyboard navigation

**Alt Text**: 
- All informative images have alt text specified
- Decorative images marked as decorative
- Icons have accessible labels

**Structure**: 
- Heading hierarchy is logical (h1, h2, h3, no skipping)
- Form inputs have associated labels
- Buttons have descriptive text (not just icons)

---

## Handoff Readiness

**Specifications**: 
- Spacing values are clearly marked
- Font sizes and weights are specified
- Colors are labeled with names or hex codes
- Component states are documented

**Assets**: 
- All icons are exported in required formats
- Images are optimized and in correct formats
- Asset naming follows conventions
- All necessary sizes/resolutions are provided

**Documentation**: 
- Interaction notes are included
- Edge cases are documented
- Any special requirements are noted
- Links to design system or component library

**Developer Access**: 
- Developers have view access to design files
- Prototype links are shared
- Design system is accessible
- Point of contact is clear for questions

---
