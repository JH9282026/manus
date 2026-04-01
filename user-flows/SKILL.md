---
name: user-flows
description: "Map user journeys, task flows, and interaction paths through products to optimize user experience. Use for: journey mapping, flow diagrams, task analysis, identifying pain points, and optimizing user paths."
---

# User Flows

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

## Critical Flow 2: Create Project

### Context
- **User**: Sarah (Creative Director) or Marcus (PM)
- **Goal**: Set up a new client project quickly
- **Entry Point**: Dashboard "+ New Project" button
- **Success Criteria**: Project created with name, client, and at least one task

### Flow Diagram

```
┏━━━━━━━━━━━━━━━┓
┃ Dashboard      ┃
┃ "+ New Project"┃
┗━━━━━━━┫━━━━━━━┛
        │
        ▼
┌───────────────┐
│ Project Modal  │
│ Name + Client  │
└───────┬───────┘
        │
        ▼
     Template?
      /      \
    Yes       No
    /           \
   ▼             ▼
┌─────────┐  ┌─────────┐
│ Template │  │  Blank   │
│  Picker  │  │ Project  │
└────┬────┘  └────┬────┘
     │              │
     └──────┬──────┘
            │
            ▼
    ┏━━━━━━━━━━━━━┓
    ┃ Project View ┃
    ┃   Created!   ┃
    ┗━━━━━━━━━━━━━┛
```

### Key Design Considerations
- **Minimal required fields**: Name only is required; client optional
- **Template vs. blank**: Equal prominence, no wrong choice
- **Fast path**: Keyboard shortcut Cmd+N from anywhere
- **Immediate entry**: Modal, not separate page (stay in context)

---

## Critical Flow 3: Create & Assign Task

### Context  
- **User**: Marcus (PM) primary, Sarah secondary
- **Goal**: Create task and assign to team member
- **Entry Point**: Within project view, "+ Add Task"
- **Success Criteria**: Task created with title, assignee, due date

### Flow Diagram (Inline Creation)

```
┌───────────────────────┐
│ Project Task List    │
│                      │
│ [Task 1]             │
│ [Task 2]             │
│ [+ Add Task] ◀──────│─── Click or press Enter
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Inline Task Editor    │
│                       │
│ [Task title input___] │
│ @assign  #date  ...   │
└───────────┬───────────┘
            │
            ▼ Type title, press Enter
┌───────────────────────┐
│ ✓ Task Created        │
│ Click to add details  │
└───────────────────────┘
```

### Quick Actions (Slash Commands)
- Type `/assign @name` - Assign to team member
- Type `/due Friday` - Set due date with natural language
- Type `/priority high` - Set priority
- Press `Tab` - Move through fields quickly

---

## Flow Summary Map

```
                    ┌─────────────┐
                    │  SIGN UP   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  ONBOARD   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
┌─────────────────▶│  DASHBOARD  │◀─────────────────┐
│                  └───┬───┬─────┘                  │
│                      │   │                      │
│              ┌───────┘   └───────┐              │
│              ▼               ▼              │
│       ┌────────────┐  ┌────────────┐       │
│       │  CREATE    │  │  MY TASKS  │       │
│       │  PROJECT   │  │            │       │
│       └──────┬─────┘  └──────┬─────┘       │
│              │               │              │
│              ▼               ▼              │
│       ┌────────────┐  ┌────────────┐       │
│       │  PROJECT   │  │  TASK      │       │
└───────│  VIEW      │─▶│  DETAIL    │───────┘
        └────────────┘  └────────────┘
              │
              ▼
        ┌────────────┐
        │  CREATE    │
        │  TASK      │
        └────────────┘
```
```

---

## Prompts Library

### Flow Identification
```
For [PRODUCT] identify all user flows organized by:
1. Acquisition (how users first engage)
2. Activation (first value moment)
3. Core (primary daily usage)
4. Retention (what brings them back)
5. Revenue (upgrade/purchase)

For each, rate importance: Critical / Important / Nice-to-have
```

### Flow Optimization
```
Review this user flow:
[FLOW DESCRIPTION]

Identify:
1. Unnecessary steps to remove
2. Decision points that could be eliminated
3. Places where users might get stuck
4. Opportunities for delight
5. Keyboard shortcuts or accelerators
```

### Error Flow
```
For the [FLOW NAME] flow, design error handling:
1. What can go wrong at each step?
2. What error message should users see?
3. How can they recover?
4. Should any errors be prevented vs. handled?
```

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

- [./references/01_user_flow_fundamentals.md](./references/01_user_flow_fundamentals.md): 01 User Flow Fundamentals
- [./references/02_creating_user_flow_diagrams.md](./references/02_creating_user_flow_diagrams.md): 02 Creating User Flow Diagrams
- [./references/03_user_flow_optimization.md](./references/03_user_flow_optimization.md): 03 User Flow Optimization
- [./references/04_user_flows_vs_journey_maps.md](./references/04_user_flows_vs_journey_maps.md): 04 User Flows Vs Journey Maps
- [./references/05_user_flow_best_practices.md](./references/05_user_flow_best_practices.md): 05 User Flow Best Practices
