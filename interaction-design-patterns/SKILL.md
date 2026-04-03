---
name: interaction-design-patterns
description: "Design micro-interactions, animations, and state transitions that enhance usability and provide meaningful feedback. Use for: creating hover effects, loading states, transition animations, gesture responses, form validation feedback, and establishing motion design principles that improve user experience without compromising performance."
---

# Interaction Design

Design micro-interactions, animations, and state transitions that enhance usability and provide meaningful feedback.

# Skill: Interaction Design

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Interaction Design |
| **Category** | Responsive & Platform Design |
| **Phase** | 4 - Responsive & Platform |
| **Estimated Time** | 30-60 minutes |
| **Dependencies** | `component_design.md` |
| **Outputs** | Interaction specifications, animation guidelines, micro-interaction definitions |

## Description
Interaction Design defines how users interact with the interface through animations, transitions, micro-interactions, and feedback systems. Good interaction design makes interfaces feel responsive, intuitive, and delightful.

## When to Use
- After component design is complete
- Defining transition behaviors
- Creating loading and feedback patterns
- Adding polish and delight
- Documenting interactive behaviors for development

---

## Instructions for AI Agents
### Step 1: Identify Interaction Points

**Categories of interactions:**

```markdown

## Interaction Inventory
### State Changes
- Button states (hover, active, disabled)
- Input focus states
- Toggle/switch animations
- Checkbox/radio selection

### Navigation
- Page transitions
- Modal open/close
- Drawer slide in/out
- Tab switching

### Feedback
- Form validation
- Success/error messages
- Loading indicators
- Progress feedback

### Data
- List item add/remove
- Drag and drop
- Sort/filter transitions
- Infinite scroll loading

### Delight
- Hover effects
- Scroll-based animations
- Celebration moments
- Empty state animations
```

### Step 2: Define Animation Principles

**Animation values:**

```markdown

## Animation System
### Timing (Duration)

| Type | Duration | Use Case |
|------|----------|----------|
| Instant | 0ms | State toggles (on/off) |
| Fast | 100-150ms | Hovers, button feedback |
| Normal | 200-300ms | Modals, panels, most transitions |
| Slow | 400-500ms | Complex animations, page transitions |
| Deliberate | 500ms+ | Celebrations, attention-grabbing |

### Easing Functions

| Easing | CSS | Use Case |
|--------|-----|----------|
| Ease-out | `cubic-bezier(0, 0, 0.2, 1)` | Elements entering (modals appearing) |
| Ease-in | `cubic-bezier(0.4, 0, 1, 1)` | Elements exiting (modals closing) |
| Ease-in-out | `cubic-bezier(0.4, 0, 0.2, 1)` | Elements moving on screen |
| Spring | `cubic-bezier(0.175, 0.885, 0.32, 1.275)` | Playful, bouncy effects |

### Principles
1. **Purposeful**: Every animation serves a function
2. **Fast**: Never block the user (200-300ms typical)
3. **Natural**: Use physics-based easing
4. **Consistent**: Same animation for same action
5. **Reducible**: Respect reduced motion preferences
```

### Step 3: Component Interactions

**Interaction specifications:**

```markdown

## Button Interactions
### Hover
- Duration: 150ms
- Easing: ease-out
- Changes: Background color shift, subtle scale (1.02)

### Active (Press)
- Duration: 50ms
- Changes: Scale down (0.98), darker background

### Focus
- Duration: 0ms (instant)
- Changes: Focus ring appears

### Loading
- Spinner replaces text
- Button width maintained
- Disabled during loading

---

## Input Interactions
### Focus
- Duration: 150ms
- Border color transition
- Label floats up (if using floating labels)
- Ring/glow appears

### Validation
- Error: Shake animation (subtle, 2-3 shakes)
- Success: Brief green border flash
- Message slides down: 200ms

---

## Modal Interactions
### Open
- Backdrop: Fade in 200ms, ease-out
- Modal: Scale from 0.95 to 1, fade in, 200ms
- Entry: Slightly from bottom (10-20px)

### Close
- Duration: 150ms
- Modal: Fade out, scale to 0.95
- Backdrop: Fade out after modal starts

---

## List Interactions
### Add Item
- New item: Slide down + fade in, 200ms
- Push existing items down smoothly

### Remove Item
- Item: Slide left + fade out, 200ms
- Or: Collapse height smoothly

### Reorder (Drag)
- Dragged item: Subtle shadow, scale 1.02
- Drop zones highlight
- Items shift to make room (200ms)
```

### Step 4: Feedback Patterns

**User feedback interactions:**

```markdown

## Loading States
### Button Loading
```
[  Button  ] -> [◌ Loading...] -> [✓ Done!] -> [  Button  ]
     0ms           100ms          2000ms         3000ms
```

### Skeleton Loading
- Pulsing gradient animation
- 1.5s cycle, ease-in-out
- Match content layout shape

### Progress Bar
- Smooth width transition
- Determinate: Based on actual progress
- Indeterminate: Infinite animation

---

## Notifications/Toasts
### Appear
- Slide in from edge (top/bottom)
- Duration: 200ms, ease-out
- Auto-dismiss: 3-5 seconds

### Progress Timer
- Optional progress bar showing time remaining
- Pause on hover

### Dismiss
- Swipe away OR fade out
- Duration: 150ms

---

## Validation Feedback
### Real-time Validation
- Debounce input: 300-500ms
- Show indicator while validating
- Animate state change (border color)

### Submit Validation
- Scroll to first error
- Shake invalid field (subtle)
- Focus first invalid input
```

### Step 5: Accessibility Considerations

```markdown

## Motion Accessibility
### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.001ms !important;
    transition-duration: 0.001ms !important;
  }
}
```

### Guidelines
- Provide static alternatives
- No flashing content (seizure risk)
- Allow animation disabling in settings
- Essential animations can remain (with caution)

### What to Keep (Reduced Motion)
- Opacity changes (subtle)
- Color changes
- Essential state indicators

### What to Remove
- Position animations
- Scale transforms
- Complex sequences
- Decorative motion
```

---

## Example Input/Output
### Example Input

```markdown
**Project**: TaskFlow
**Focus**: Task completion interaction
**Personality**: Professional but satisfying
```

### Example Output

```markdown

## Resources
### Animation Libraries
- Framer Motion (React)
- GSAP (JavaScript)
- CSS Animations/Transitions
- Lottie (complex animations)

### References
- Material Motion: https://m2.material.io/design/motion/
- iOS Motion: https://developer.apple.com/design/human-interface-guidelines/motion

---

## Related Skills
- **Previous**: `component_design.md` - Components to animate
- **Related**: `mobile_app_design.md` - Platform-specific interactions
- **Next**: `design_review.md` - Include interactions in review

## Using the Reference Files

### When to Read Each Reference

**`./references/prompts-library.md`** — Read when you need detailed guidance on prompts library aspects of this skill.

**`./references/task-completion-interaction.md`** — Read when you need detailed guidance on task completion interaction aspects of this skill.
