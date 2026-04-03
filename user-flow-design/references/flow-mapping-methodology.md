# Flow Mapping Methodology

Detailed methodology for creating user flow diagrams, including templates, notation systems, and documentation standards.

---

## Flow Mapping Template

Use this structure for every flow:

```markdown
## Flow: [Flow Name]

### Context
- **User**: [Which persona]
- **Goal**: [What they want to accomplish]
- **Entry Point**: [Where they start]
- **Success Criteria**: [What defines completion]

### Happy Path Steps

| Step | Screen | User Action | System Response | Notes |
|------|--------|-------------|-----------------|-------|
| 1 | [Screen] | [Action] | [Response] | [Notes] |
| 2 | [Screen] | [Action] | [Response] | [Notes] |

### Decision Points
- **[Decision 1]**: [Options available, criteria for each path]

### Error States
| Error | Cause | User Message | Recovery Action |
|-------|-------|--------------|----------------|
| [Error 1] | [Why] | [What user sees] | [What they can do] |

### Screen Requirements
1. **[Screen 1]**: [Primary purpose]
2. **[Screen 2]**: [Primary purpose]

### Metrics
- Completion rate target: [X%]
- Time to complete: [Target]
- Key drop-off points: [Where to monitor]
```

---

## ASCII Flow Diagram Syntax

Standard notation for text-based flow diagrams:

```
┌─────────┐    Rounded rectangle = Screen/Page
│  Screen  │
└─────────┘

┏━━━━━━━━━┓    Double border = Entry/Exit point
┃  START  ┃
┗━━━━━━━━━┛

   /\        Diamond = Decision point
  /  \
 /    \
 \    /
  \  /
   \/

────▶       Solid arrow = Flow direction

- - - ▶     Dashed arrow = Optional/alternate path

[⚠️ Error]   Error state
[✓ Done]    Success state
```

---

## Critical Flow Detail Template

For flows rated as "Critical", expand documentation to include:

### Happy Path
Numbered step-by-step for the ideal scenario:
1. User arrives at [Entry point] via [Source]
2. User sees [Key elements on screen]
3. User [Takes action]
4. System [Responds with]
5. Continue until completion

### Edge Cases
- **Existing account on sign-up**: Show "Already have account? Log in"
- **Slow connection**: Show progress indicators per step
- **Abandonment mid-flow**: Email reminder after 24h
- **Skip optional steps**: Allow skipping to core experience

### Error Handling Table

| Error | Cause | User Message | Recovery Action |
|-------|-------|--------------|----------------|
| Invalid email | Typo in email field | "Please enter a valid email" | Highlight field, focus cursor |
| Server timeout | Network issue | "Something went wrong. Try again." | Retry button, preserve data |
| Duplicate entry | Already exists | "This already exists. View it?" | Link to existing item |

### Screen Requirements Derived from Flow
List every screen this flow touches, with primary purpose:
1. **Sign Up Modal**: Email, password, terms
2. **Workspace Setup**: Company name, optional logo
3. **Role Selection**: 3 clear role cards
4. **Dashboard**: First-run experience with guided tour

### Metrics to Track
- **Completion rate**: Target 80%+ for critical flows
- **Time to complete**: Under 3 minutes for onboarding
- **Drop-off points**: Monitor each step transition
- **Recovery rate**: % of users who hit errors and still complete

---

## Flow Inventory Organization

Organize all identified flows into a master inventory:

### By Priority
- **Critical Flows** (must work perfectly): Sign up, core task, checkout
- **Important Flows** (high frequency): Update, search, invite
- **Supporting Flows** (occasional): Settings, export, archive

### By Funnel Stage (AARRR)
1. **Acquisition**: Landing → Sign up
2. **Activation**: Sign up → First value moment
3. **Core Usage**: Daily primary tasks
4. **Retention**: Notifications → Re-engagement
5. **Revenue**: Free → Paid upgrade

---

## Multi-Device Flow Considerations

When flows span devices:
- Document handoff points (e.g., "email link opens on mobile")
- Ensure state persistence across devices
- Design for the smallest screen at each step
- Consider QR codes or magic links for device transitions
