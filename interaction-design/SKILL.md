---
name: interaction-design
description: "Design intuitive, engaging user interactions for digital products through systematic application of interaction design principles, patterns, prototyping methodologies, and usability testing. Use for creating interaction flows, selecting and implementing design patterns, building prototypes (low to high fidelity), conducting usability tests, designing microinteractions, optimizing user control and feedback mechanisms, ensuring accessibility in interactions, and establishing interaction design systems for products and teams."
---

# Interaction Design

Create engaging, intuitive user experiences through systematic interaction design principles, patterns, prototyping, and testing.

## Overview

Interaction design focuses on creating meaningful relationships between users and digital products through carefully crafted behaviors, feedback mechanisms, and interaction patterns. This skill provides frameworks for applying core interaction principles, selecting appropriate patterns, prototyping at various fidelity levels, and validating designs through usability testing. It covers the complete interaction design process from conceptualization through validation, emphasizing user-centricity, consistency, and accessibility.

## Core Interaction Design Principles

Seven fundamental principles guide all interaction design decisions:

| Principle | Definition | Application Example |
|-----------|------------|---------------------|
| **User-Centricity** | Design based on user needs, not assumptions | Google Docs AI suggests changes rather than auto-applying them, giving users control |
| **Consistency** | Predictable patterns across touchpoints | Google Workspace maintains shared visual language and behaviors across all apps |
| **Hierarchy** | Structure information to guide attention | AI summaries appear at top of content, prioritizing most important information first |
| **Context** | Adapt to user's situation and environment | Google Maps changes interface for driving vs. walking, prioritizing relevant information |
| **User Control** | Provide freedom and easy error recovery | Undo/cancel options, "emergency exits" for all critical actions |
| **Accessibility** | Usable by widest possible audience | Sufficient color contrast, keyboard navigation, screen reader support |
| **Usability** | Easy to learn, efficient, memorable | Core tasks completable without training or documentation |

### Principle Application Strategy

**For new features:**
1. Start with user-centricity — validate the need through research
2. Apply consistency — reuse existing patterns where possible
3. Establish hierarchy — determine information priority
4. Consider context — identify usage scenarios and constraints
5. Ensure user control — add undo/cancel for all actions
6. Verify accessibility — test with assistive technologies
7. Validate usability — test with representative users

**For AI-powered products:**
- Suggest actions rather than executing automatically
- Clearly structure AI outputs to avoid overwhelming users
- Provide transparency about AI decision-making
- Allow users to override or refine AI suggestions

## Interaction Pattern Selection

Choose patterns based on user goals and context:

| User Goal | Recommended Pattern | When to Use |
|-----------|---------------------|-------------|
| Navigate hierarchy | Breadcrumbs, tree navigation | Deep content structures (3+ levels) |
| Complete multi-step process | Wizard, stepper, progress indicator | Onboarding, checkout, complex forms |
| Provide input | Forms, inline editing, natural language | Data entry, content creation |
| Discover content | Cards, infinite scroll, filters | Content-heavy applications, feeds |
| Take quick action | Floating action button, quick actions menu | Mobile apps, frequent tasks |
| Receive feedback | Toast notifications, inline validation | Confirmations, errors, status updates |
| Explore options | Tabs, accordions, progressive disclosure | Organizing related content |
| Manipulate objects | Drag-and-drop, gestures, direct manipulation | Visual editors, dashboards |

### Pattern Combination Guidelines

- **Don't mix competing patterns** — Use either tabs OR accordions for content organization, not both
- **Layer patterns hierarchically** — Breadcrumbs for navigation + tabs for content organization works well
- **Consider mobile constraints** — Hover states don't work on touch devices; use tap-and-hold or alternative patterns
- **Test pattern recognition** — Users should understand the pattern without instruction

## Prototyping Strategy

Match prototype fidelity to your validation goals:

### Fidelity Selection Matrix

| Stage | Fidelity Level | Prototype Type | Purpose | Time Investment |
|-------|----------------|----------------|---------|------------------|
| **Concept validation** | Low | Paper sketches, wireframes | Test core flows and structure | 1-4 hours |
| **Flow validation** | Low-Mid | Clickable wireframes | Validate navigation and information architecture | 4-8 hours |
| **Interaction validation** | Mid | Interactive wireframes | Test specific interaction patterns | 1-2 days |
| **Visual validation** | Mid-High | Styled prototypes | Validate visual design and branding | 2-3 days |
| **Usability validation** | High | Functional prototypes | Test complete user experience | 3-5 days |
| **Stakeholder presentation** | High | Polished prototypes | Communicate vision and secure buy-in | 3-5 days |
| **Developer handoff** | High | Functional prototypes with specs | Provide implementation reference | 5+ days |

### Prototype Type Selection

**Horizontal prototypes** — Broad interactivity across many features with limited depth
- Use when: Demonstrating overall product vision, stakeholder presentations
- Advantage: Shows complete user journey
- Limitation: Shallow interaction depth

**Vertical prototypes** — Deep interactivity within few key features
- Use when: Testing complex interactions, validating technical feasibility
- Advantage: Realistic interaction behavior
- Limitation: Limited feature coverage

**Hybrid approach** (recommended for most projects):
1. Start with horizontal low-fidelity prototype for overall flow
2. Create vertical high-fidelity prototypes for complex interactions
3. Combine insights to build final product

### Prototyping Best Practices

- **Start low, go high** — Begin with low-fidelity for rapid iteration, increase fidelity as design solidifies
- **Test early, test often** — 5 users can reveal 85% of usability issues
- **Match fidelity to audience** — Stakeholders often need higher fidelity than development teams
- **Prototype only what you need to learn** — Don't build complete flows if testing one interaction
- **Use real content when possible** — Lorem ipsum hides content design issues
- **Include error states** — Test how users recover from mistakes

## Microinteractions and Feedback

Microinteractions provide crucial feedback and enhance perceived responsiveness:

### Essential Microinteraction Types

| Interaction Type | Purpose | Implementation Guidelines |
|------------------|---------|---------------------------|
| **Button states** | Confirm interaction registered | Hover (desktop), pressed, disabled, loading states |
| **Loading indicators** | Manage expectations during waits | <1s: none needed; 1-5s: spinner; 5s+: progress bar with estimate |
| **Transitions** | Maintain spatial context | 200-300ms for most transitions; faster feels jarring, slower feels sluggish |
| **Validation feedback** | Guide correct input | Inline validation as user types (for errors) or on blur (for success) |
| **Success confirmations** | Acknowledge completion | Toast notifications (3-5s), checkmark animations, state changes |
| **Error messages** | Enable recovery | Specific, actionable, near the error source |
| **Skeleton screens** | Reduce perceived wait time | Show content structure while loading actual data |

### Feedback Timing Guidelines

- **Immediate (<100ms)** — Direct manipulation (drag, scroll, type)
- **Responsive (100-300ms)** — Button clicks, navigation, simple actions
- **Acknowledged (300ms-1s)** — Form submissions, saves, simple processing
- **Progress indicated (1s+)** — Complex operations, uploads, searches

## Accessibility in Interaction Design

Build accessibility into interactions from the start:

### Critical Accessibility Requirements

| Requirement | Implementation | Testing Method |
|-------------|----------------|----------------|
| **Keyboard navigation** | All interactive elements accessible via Tab, Enter, Space, Arrow keys | Navigate entire interface without mouse |
| **Focus indicators** | Visible focus state on all interactive elements (3:1 contrast minimum) | Tab through interface, verify visible focus |
| **Screen reader support** | Proper ARIA labels, roles, and live regions | Test with NVDA (Windows) or VoiceOver (Mac/iOS) |
| **Color contrast** | 4.5:1 for normal text, 3:1 for large text and UI components | Use WebAIM Contrast Checker |
| **Touch targets** | Minimum 44×44px for mobile, 24×24px for desktop | Test on actual devices |
| **Motion sensitivity** | Respect prefers-reduced-motion setting | Disable animations when user preference set |
| **Error identification** | Don't rely on color alone; use icons and text | View interface in grayscale |

### Accessibility Testing Workflow

1. **Automated testing** — Run axe DevTools or WAVE on prototypes
2. **Keyboard testing** — Navigate without mouse, verify all functionality accessible
3. **Screen reader testing** — Test with NVDA/VoiceOver, verify logical reading order
4. **Contrast testing** — Check all text and interactive elements meet WCAG AA standards
5. **User testing** — Include users with disabilities in usability testing

## Emerging Interaction Paradigms

### Multimodal Interfaces

Combine voice, touch, gesture, and traditional inputs:

- **Design for mode switching** — Users should easily transition between input methods
- **Provide redundancy** — Critical actions available through multiple modalities
- **Consider context** — Voice works poorly in noisy environments; touch works poorly with gloves
- **Maintain consistency** — Same action should produce same result regardless of input method

### AI-Augmented Interactions

- **Suggestion over automation** — Let users review and approve AI actions
- **Explainability** — Show why AI made specific recommendations
- **Graceful degradation** — Provide manual alternatives when AI fails
- **Progressive disclosure** — Don't overwhelm with all AI capabilities at once

### Immersive Environments (VR/AR)

- **Spatial navigation** — Design for 3D space, not 2D screens
- **Depth perception** — Use depth cues for hierarchy and focus
- **Comfort considerations** — Avoid rapid movements that cause motion sickness
- **Physical constraints** — Consider user's physical space and movement limitations

## Using the Reference Files

### When to Read Each Reference

**`/references/design-principles.md`** — Read when establishing interaction design foundations for a new product, making principle-based design decisions, resolving design conflicts, or training team members on interaction design fundamentals. Contains deep dives into each principle with application frameworks and decision trees.

**`/references/interaction-patterns.md`** — Read when selecting patterns for specific user tasks, designing navigation systems, creating input mechanisms, or building pattern libraries. Provides comprehensive pattern catalog with usage guidelines, variations, accessibility considerations, and anti-patterns to avoid.

**`/references/prototyping-tools.md`** — Read when choosing prototyping tools for your workflow, setting up prototyping processes, or evaluating tool capabilities for specific project needs. Covers tool comparisons, feature matrices, integration capabilities, and workflow recommendations for different team structures.

**`/references/usability-testing.md`** — Read when planning usability tests, recruiting participants, facilitating test sessions, analyzing results, or establishing continuous testing practices. Includes test protocols, participant screening criteria, facilitation techniques, analysis frameworks, and reporting templates.
