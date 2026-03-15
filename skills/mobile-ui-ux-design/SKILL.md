---
name: mobile-ui-ux-design
description: "Design intuitive, accessible mobile user interfaces following platform guidelines (Material Design, Human Interface Guidelines), responsive layouts, and user-centered design principles. Use for: designing mobile UI/UX, creating wireframes and prototypes, implementing responsive layouts, ensuring accessibility, following iOS HIG and Android Material Design, designing for different screen sizes, implementing gestures and animations, conducting usability testing, and optimizing user flows."
---

# Mobile UI/UX Design

Design intuitive, accessible, and beautiful mobile user interfaces following platform guidelines and user-centered design principles.

## Overview

Mobile UI/UX design focuses on creating user interfaces that are intuitive, accessible, and delightful to use. This skill covers design principles, platform guidelines (Material Design for Android, Human Interface Guidelines for iOS), responsive design, accessibility, user research, prototyping, and usability testing.

## Design Principles

### Core Principles

| Principle | Description |
|-----------|-------------|
| **Clarity** | UI should be easy to understand at a glance |
| **Consistency** | Similar elements behave similarly |
| **Feedback** | Provide immediate response to user actions |
| **Efficiency** | Minimize steps to complete tasks |
| **Forgiveness** | Allow undo, prevent errors |
| **Accessibility** | Usable by everyone, including people with disabilities |

### Mobile-Specific Considerations

**Thumb Zone:** Design for one-handed use. Place primary actions within easy thumb reach (bottom third of screen).

**Touch Targets:** Minimum 44x44 points (iOS) or 48x48 dp (Android) for tappable elements.

**Context of Use:** Users are often distracted, on-the-go. Design for quick, interruptible interactions.

**Screen Real Estate:** Limited space. Prioritize content, use progressive disclosure.

## Platform Guidelines

### iOS Human Interface Guidelines (HIG)

**Key Principles:**
- **Clarity:** Text is legible, icons are precise, adornments are subtle
- **Deference:** Content fills the screen, UI doesn't compete with content
- **Depth:** Visual layers and realistic motion convey hierarchy

**Design Elements:**
- **Navigation:** Tab Bar, Navigation Bar, hierarchical navigation
- **Typography:** San Francisco font, Dynamic Type support
- **Color:** System colors, semantic colors
- **Icons:** SF Symbols (3000+ icons)
- **Spacing:** 8-point grid system

**Components:**
- Navigation Bar, Tab Bar, Toolbars
- Buttons, Segmented Controls, Pickers
- Lists, Tables, Collection Views
- Sheets, Alerts, Action Sheets

### Android Material Design

**Key Principles:**
- **Material as Metaphor:** Inspired by physical materials
- **Bold, Graphic, Intentional:** Deliberate color, imagery, typography
- **Motion Provides Meaning:** Responsive, natural, aware

**Material 3 (Material You):**
- **Dynamic Color:** Adapts to user's wallpaper (Android 12+)
- **Personalization:** User-customizable themes
- **Accessibility:** Enhanced contrast, larger touch targets

**Design Elements:**
- **Typography:** Roboto font, type scale
- **Color:** Primary, Secondary, Tertiary colors with variants
- **Elevation:** Shadows and overlays for depth
- **Shape:** Rounded corners, customizable corner radius
- **Spacing:** 4dp/8dp grid system

**Components:**
- Top App Bar, Bottom Navigation, Navigation Drawer
- Buttons (Filled, Outlined, Text), FAB
- Cards, Lists, Chips
- Dialogs, Snackbars, Bottom Sheets

## Responsive Design

### Screen Sizes and Densities

**iOS:**
- iPhone: 375-430 points width
- iPad: 768-1024 points width
- Dynamic Type: Support text scaling

**Android:**
- Phones: 360-420 dp width
- Tablets: 600-840 dp width
- Foldables: Variable widths
- Density buckets: mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi

### Adaptive Layouts

**Breakpoints:**
- Compact: < 600dp (phones)
- Medium: 600-840dp (tablets portrait, foldables)
- Expanded: > 840dp (tablets landscape, desktops)

**Techniques:**
- Flexible grids
- Responsive typography
- Adaptive navigation (tabs → drawer on larger screens)
- Multi-pane layouts on tablets

## Accessibility

### WCAG 2.1 Guidelines

**Perceivable:**
- Provide text alternatives for images
- Ensure sufficient color contrast (4.5:1 for text)
- Support text resizing
- Don't rely on color alone to convey information

**Operable:**
- All functionality available via keyboard/screen reader
- Provide enough time to read and use content
- Avoid content that causes seizures (flashing)
- Provide clear navigation and focus indicators

**Understandable:**
- Readable text
- Predictable behavior
- Input assistance and error prevention

**Robust:**
- Compatible with assistive technologies

### Platform-Specific Accessibility

**iOS:**
- VoiceOver support
- Dynamic Type
- Reduce Motion
- Increase Contrast
- Accessibility labels and hints

**Android:**
- TalkBack support
- Font scaling
- Touch target sizes (48dp minimum)
- Content descriptions
- Accessibility actions

## User Research and Testing

### Research Methods

| Method | Purpose | When to Use |
|--------|---------|-------------|
| **User Interviews** | Understand needs, pain points | Early discovery |
| **Surveys** | Quantitative data, large sample | Validate assumptions |
| **Usability Testing** | Observe users completing tasks | Validate designs |
| **A/B Testing** | Compare design variants | Optimize conversions |
| **Analytics** | Understand user behavior | Ongoing optimization |

### Usability Testing

**Process:**
1. Define goals and tasks
2. Recruit representative users
3. Prepare test scenarios
4. Observe users (think-aloud protocol)
5. Collect feedback
6. Analyze results
7. Iterate design

**Metrics:**
- Task completion rate
- Time on task
- Error rate
- Satisfaction (SUS, NPS)

## Design Process

### 1. Research and Discovery

- Understand users (personas, user journeys)
- Analyze competitors
- Define requirements
- Identify constraints

### 2. Information Architecture

- Content inventory
- Card sorting
- Site maps
- User flows

### 3. Wireframing

- Low-fidelity sketches
- Focus on layout and structure
- Iterate quickly
- Tools: Figma, Sketch, Adobe XD, Balsamiq

### 4. Prototyping

- Interactive prototypes
- Test user flows
- Validate interactions
- Tools: Figma, Framer, Principle, ProtoPie

### 5. Visual Design

- Apply brand identity
- Choose color palette
- Define typography
- Create design system
- Design high-fidelity mockups

### 6. Handoff to Development

- Design specifications
- Assets export (SVG, PNG @1x, @2x, @3x)
- Annotations for interactions
- Design system documentation

## Design Patterns

### Navigation Patterns

| Pattern | Use Case |
|---------|----------|
| **Tab Bar** | 3-5 top-level sections |
| **Navigation Drawer** | Many sections, less frequent access |
| **Bottom Navigation** | 3-5 primary destinations (Android) |
| **Hierarchical** | Drill-down navigation |
| **Modal** | Temporary, focused tasks |

### Content Patterns

- **Cards:** Grouped, related content
- **Lists:** Scannable, uniform items
- **Grids:** Visual content (photos, products)
- **Feed:** Infinite scroll, chronological/algorithmic

### Input Patterns

- **Forms:** Structured data entry
- **Search:** Find specific content
- **Filters:** Refine results
- **Pickers:** Select from predefined options

## Gestures and Interactions

### Common Gestures

| Gesture | Action |
|---------|--------|
| **Tap** | Select, activate |
| **Double Tap** | Zoom, like |
| **Long Press** | Context menu, drag mode |
| **Swipe** | Navigate, delete, reveal actions |
| **Pinch** | Zoom in/out |
| **Drag** | Reorder, move |
| **Pull to Refresh** | Reload content |

### Micro-Interactions

- Button press states
- Loading indicators
- Success/error feedback
- Skeleton screens
- Transitions between screens

## Animation

### Purposes

- **Feedback:** Confirm actions
- **Guidance:** Direct attention
- **Continuity:** Smooth transitions
- **Delight:** Enhance experience

### Principles

- **Duration:** 200-400ms for most animations
- **Easing:** Natural motion (ease-in-out)
- **Purpose:** Every animation should have a reason
- **Performance:** 60fps, avoid jank

## Design Systems

### Components

- **Foundations:** Colors, typography, spacing, icons
- **Components:** Buttons, inputs, cards, etc.
- **Patterns:** Navigation, forms, data display
- **Guidelines:** Usage, accessibility, best practices

### Benefits

- Consistency across app
- Faster design and development
- Easier maintenance
- Scalability

### Tools

- Figma (design system libraries)
- Storybook (component documentation)
- Zeroheight (design system documentation)

## Best Practices

1. **Follow Platform Guidelines:** Users expect platform-native behavior
2. **Design for Accessibility:** From the start, not as an afterthought
3. **Test with Real Users:** Assumptions ≠ reality
4. **Iterate Based on Feedback:** Design is never "done"
5. **Optimize for Performance:** Fast apps feel better
6. **Provide Clear Feedback:** Users should always know what's happening
7. **Minimize Cognitive Load:** Don't make users think
8. **Design for Errors:** Prevent errors, provide clear recovery
9. **Use Familiar Patterns:** Don't reinvent the wheel
10. **Test on Real Devices:** Simulators don't capture everything

## Using the Reference Files

**`/references/platform-guidelines.md`** — Read when implementing platform-specific designs, understanding iOS HIG or Material Design components.

**`/references/accessibility-checklist.md`** — Read when ensuring accessibility compliance, implementing screen reader support, or testing with assistive technologies.

**`/references/design-patterns-library.md`** — Read when choosing navigation patterns, implementing common UI patterns, or solving specific design problems.

**`/references/prototyping-tools.md`** — Read when creating prototypes, choosing design tools, or setting up design-to-development workflows.
