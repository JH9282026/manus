---
name: user-flows-design
description: "Map user journeys and task flows to design intuitive navigation and interaction paths. Use for: creating user flow diagrams, mapping task sequences, identifying decision points, optimizing conversion funnels, and ensuring logical screen-to-screen transitions in web and mobile applications."
---

# User Flows

Map user journeys and task flows to design intuitive navigation and interaction paths.

# Skill: User Flows

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | User Flows |
| **Category** | UX Foundation |
| **Phase** | 2 - UX Foundation |
| **Estimated Time** | 30-60 minutes |
| **Dependencies** | `user_personas.md` |
| **Outputs** | User flow diagrams, journey maps |

## Description
User Flows map the paths users take to accomplish goals within a product. They visualize the steps, decisions, and touchpoints from entry to completion, ensuring designs support efficient, logical task completion.

## When to Use
- After defining user personas
- Before wireframing to plan screen sequences
- When designing new features
- To identify friction points in existing flows
- When optimizing conversion funnels

---

## Instructions for AI Agents
### Step 1: Identify Key Flows

**Prompt to identify flows:**
```
For [PRODUCT] with these personas:
- [Persona 1]: [Primary goal]
- [Persona 2]: [Primary goal]

Identify the essential user flows to design:

1. **Critical Flows** (must work perfectly):
   - [Flow 1]: [What user accomplishes]
   - [Flow 2]: [What user accomplishes]

2. **Important Flows** (high frequency):
   - [Flow 1]: [What user accomplishes]

3. **Supporting Flows** (occasional but necessary):
   - [Flow 1]: [What user accomplishes]
```

### Step 2: Map Flow Structure

**Flow mapping template:**

```markdown

## Flow: [Flow Name]
### Context
- **User**: [Which persona]
- **Goal**: [What they want to accomplish]
- **Entry Point**: [Where they start]
- **Success Criteria**: [What defines completion]

### Flow Diagram

```
[ENTRY] → [Step 1] → [Step 2] → [Decision?]
                                    │
                          ┌────────┴────────┐
                          ▼                  ▼
                     [Path A]           [Path B]
                          │                  │
                          └────────┬────────┘
                                    ▼
                               [SUCCESS]
```

### Detailed Steps

| Step | Screen | User Action | System Response | Notes |
|------|--------|-------------|-----------------|-------|
| 1 | [Screen name] | [What user does] | [What happens] | [Design notes] |
| 2 | [Screen name] | [What user does] | [What happens] | [Design notes] |

### Decision Points
- **[Decision 1]**: [Options available, criteria for each path]

### Error States
- **[Error 1]**: [When it occurs, how to handle]
```

### Step 3: Create Flow Notation

**ASCII flow diagram syntax:**

```
┌─────────┐    Rounded = Screen/Page
│  Screen  │
└─────────┘

┏━━━━━━━━━┓    Double = Entry/Exit point
┃  START  ┃
┗━━━━━━━━━┛

   /\        Diamond = Decision
  /  \
 /    \
 \    /
  \  /
   \/

────▶       Arrow = Flow direction

- - - ▶     Dashed = Optional/alternate path

[⚠️ Error]   Error state
[✓ Done]    Success state
```

### Step 4: Detail Critical Flows

**For each critical flow, document:**

```markdown

## Critical Flow Detail: [Flow Name]
### Happy Path
[Numbered step-by-step for ideal scenario]

1. User arrives at [Entry point] via [Source]
2. User sees [Key elements on screen]
3. User [Takes action]
4. System [Responds with]
5. [Continue until completion]

### Edge Cases
- **[Edge case 1]**: [How handled]
- **[Edge case 2]**: [How handled]

### Error Handling
| Error | Cause | User Message | Recovery Action |
|-------|-------|--------------|----------------|
| [Error 1] | [Why] | [What user sees] | [What they can do] |

### Screen Requirements
This flow requires these screens:
1. **[Screen 1]**: [Primary purpose]
2. **[Screen 2]**: [Primary purpose]

### Metrics to Track
- Completion rate: [Target %]
- Time to complete: [Target time]
- Drop-off points: [Key monitoring points]
```

---

## Example Input/Output
### Example Input

```markdown
**Product**: TaskFlow - SaaS project management
**Personas**: Sarah (Creative Director), Marcus (PM), Jordan (Designer)
**Key task**: Create a new project and assign initial tasks
```

### Example Output

```markdown

## User Flows: TaskFlow
### Flow Inventory

#### Critical Flows (Must be excellent)
1. **Sign Up / Onboarding** - New user to first value
2. **Create Project** - Starting a new client project
3. **Create & Assign Task** - Core daily action
4. **Check Project Status** - Dashboard overview

#### Important Flows
5. **Invite Team Member** - Growing the team
6. **Update Task Status** - Daily micro-interaction
7. **View My Tasks** - Individual focus

#### Supporting Flows
8. **Archive Project** - Cleanup
9. **Export Report** - Client deliverable
10. **Manage Settings** - Configuration

---

## Critical Flow 1: User Sign Up & Onboarding
### Context
- **User**: Sarah (Creative Director) - Decision maker trying the product
- **Goal**: Sign up and understand if TaskFlow fits agency needs
- **Entry Point**: Landing page CTA "Start Free Trial"
- **Success Criteria**: First project created with at least 2 tasks

### Flow Diagram

```
┏━━━━━━━━━━━━━━━┓
┃ Landing Page   ┃
┃ Click "Start"  ┃
┗━━━━━━━┫━━━━━━━┛
        │
        ▼
┌───────────────┐
│  Sign Up Form  │
│  Email + Pass  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ Workspace Name │
│ (Agency name)  │
└───────┬───────┘
        │
        ▼
┌───────────────┐     ┌───────────────┐
│ Role Selection │───▶│ Optional:     │
│ (What you do)  │     │ Invite Team   │
└───────┬───────┘     └───────┬───────┘
        │                      │
        └──────────┬───────────┘
                   │
                   ▼
        ┌────────────────┐
        │ First Project   │
        │ Template Select │
        └───────┬────────┘
                │
                ▼
        ┌────────────────┐
        │ Guided Tour     │
        │ Create 1st Task │
        └───────┬────────┘
                │
                ▼
        ┏━━━━━━━━━━━━━━━━┓
        ┃  ✓ SUCCESS     ┃
        ┃ Dashboard View ┃
        ┗━━━━━━━━━━━━━━━━┛
```

### Detailed Steps

| Step | Screen | User Action | System Response | Design Notes |
|------|--------|-------------|-----------------|-------------|
| 1 | Landing | Click "Start Free Trial" | Show signup form | Prominent CTA |
| 2 | Signup | Enter email, password | Validate, create account | Social login option |
| 3 | Workspace | Enter agency name | Create workspace | Pre-fill if from email domain |
| 4 | Role | Select role from 3 options | Customize initial view | Creative Director / PM / Designer |
| 5 | Invite | Optionally add team emails | Queue invites | Skip option prominent |
| 6 | Template | Choose project template | Create sample project | "Start blank" option |
| 7 | Tour | Follow guided task creation | Highlight features | Can dismiss anytime |
| 8 | Dashboard | View completed setup | Show project with tasks | Celebration moment! |

### Edge Cases
- **Existing email**: Show "Already have account? Log in" link
- **Slow connection**: Show progress indicators per step
- **Abandonment**: Email reminder after 24h if incomplete
- **Skip everything**: Allow skipping to empty dashboard

### Screens Required
1. **Sign Up Modal**: Email, password, terms
2. **Workspace Setup**: Company name, optional logo
3. **Role Selection**: 3 clear role cards
4. **Team Invite**: Email input with skip option
5. **Template Picker**: Visual template cards
6. **Guided Tour Overlay**: Step-by-step tooltips

---

## Success Criteria
### Minimum Requirements
- [ ] Critical flows identified and mapped
- [ ] Happy path documented for each
- [ ] Decision points clearly marked
- [ ] Error states considered
- [ ] Screen list derived from flows

### Quality Indicators
- [ ] Flows are efficient (minimal steps)
- [ ] Clear entry and exit points
- [ ] Consistent patterns across flows
- [ ] Personas can complete their goals
- [ ] Accessibility considered in flow design

---

## Related Skills
- **Previous**: `user_personas.md` - Know who flows are for
- **Next**: `information_architecture.md` - Structure the navigation
- **Next**: `wireframing.md` - Sketch the screens identified

## Using the Reference Files

### When to Read Each Reference

**`./references/critical-flow-2-create-project.md`** — Read when you need detailed guidance on critical flow 2 create project aspects of this skill.

**`./references/prompts-library.md`** — Read when you need detailed guidance on prompts library aspects of this skill.
