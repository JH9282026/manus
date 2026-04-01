---
name: interaction-design
description: "Design interactive behaviors, animations, transitions, and micro-interactions that enhance user experience. Use for: defining interactions, animation specs, hover states, transitions, micro-interactions, and creating delightful user experiences."
---

# Interaction Design

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
## Task Completion Interaction

### Interaction Flow

```
Task Uncompleted:       User Clicks:         Completed State:
┌────────────────┐    ┌────────────────┐    ┌────────────────┐
│ ○ Task name    │    │ ✓ Task name    │    │ ✓ Task name    │
│   Due today   │ →  │   Due today   │ →  │   Completed   │
└────────────────┘    └────────────────┘    └────────────────┘
                        (0-150ms)           (150-300ms)
```

### Checkbox Animation

**Phase 1: Click Response (0-100ms)**
- Checkbox scales down to 0.9 (press feedback)
- Background starts transitioning to Success-500

**Phase 2: Check Mark (100-250ms)**
- Checkbox scales back to 1.0 (spring easing)
- Checkmark draws in (SVG path animation)
- Path animation: left-to-right stroke

**Phase 3: Text Treatment (150-300ms)**
- Task text: Strikethrough animates left-to-right
- Text color: Fades to Gray-400
- Subtle opacity reduction on entire row

**Phase 4: List Update (300-500ms)**
- If "hide completed" is on:
  - Row collapses (height 0, opacity 0)
  - Items below slide up smoothly
- If showing completed:
  - Row moves to completed section (if sorted)

### CSS Implementation

```css
/* Checkbox */
.checkbox {
  transition: transform 100ms ease-out,
              background 150ms ease-out;
}
.checkbox:active {
  transform: scale(0.9);
}
.checkbox.checked {
  background: var(--success-500);
}

/* Checkmark */
.checkmark {
  stroke-dasharray: 20;
  stroke-dashoffset: 20;
  transition: stroke-dashoffset 150ms ease-out;
}
.checkbox.checked .checkmark {
  stroke-dashoffset: 0;
}

/* Task text */
.task-text {
  position: relative;
  transition: color 200ms ease-out;
}
.task-text::after {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  width: 0;
  height: 2px;
  background: var(--gray-400);
  transition: width 200ms ease-out 100ms;
}
.task.completed .task-text {
  color: var(--gray-400);
}
.task.completed .task-text::after {
  width: 100%;
}

/* Row collapse */
.task.removing {
  animation: collapseRow 300ms ease-out forwards;
}
@keyframes collapseRow {
  to {
    height: 0;
    opacity: 0;
    padding: 0;
    margin: 0;
  }
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  .checkbox, .checkmark, .task-text, .task-text::after {
    transition: none;
  }
  .task.removing {
    animation: none;
    display: none;
  }
}
```

### Sound/Haptics (Optional)

| Platform | Feedback |
|----------|----------|
| iOS | Light haptic tap on completion |
| Android | Subtle vibration (if enabled) |
| Web | Optional subtle sound effect |

### Delight Addition (Achievement)

For milestone completions (all daily tasks done):
- Subtle confetti burst from checkbox
- "All done!" toast notification
- Small celebration animation
```

---

## Prompts Library

### Interaction Specification
```
Define the interaction for [COMPONENT/ACTION]:

1. Trigger: What initiates it
2. Animation: What changes and how
3. Timing: Duration and easing
4. Feedback: How user knows it worked
5. Edge cases: Loading, error states
6. Accessibility: Reduced motion alternative
```

### Animation Audit
```
Review these interactions for [PROJECT]:

1. Are all durations under 400ms for UI responses?
2. Is easing appropriate (ease-out for entrances)?
3. Is there feedback for every user action?
4. Do animations serve a purpose?
5. Is reduced motion supported?
```

---

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

## Success Criteria

### Minimum Requirements
- [ ] All interactive elements have feedback
- [ ] Loading states defined
- [ ] Transitions feel smooth
- [ ] Reduced motion supported

### Quality Indicators
- [ ] Animations feel natural and purposeful
- [ ] No jarring or sudden changes
- [ ] Consistent timing throughout
- [ ] Delightful without being distracting

---

## Related Skills

- **Previous**: `component_design.md` - Components to animate
- **Related**: `mobile_app_design.md` - Platform-specific interactions
- **Next**: `design_review.md` - Include interactions in review

## Using the Reference Files

- [./references/design-principles.md](./references/design-principles.md): Design Principles
- [./references/interaction-patterns.md](./references/interaction-patterns.md): Interaction Patterns
- [./references/prototyping-tools.md](./references/prototyping-tools.md): Prototyping Tools
- [./references/usability-testing.md](./references/usability-testing.md): Usability Testing
