# Task Completion Interaction - Detailed Reference

Detailed reference content for interaction design.

---

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
