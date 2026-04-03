# Critical Flow 2: Create Project - Detailed Reference

Detailed reference content for user flows.

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
