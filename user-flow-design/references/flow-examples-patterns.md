# Flow Examples & Patterns

Concrete user flow examples and common patterns for reference when designing flows.

---

## Example: SaaS Sign Up & Onboarding Flow

### Context
- **User**: Decision maker trying the product
- **Goal**: Sign up and understand if product fits needs
- **Entry**: Landing page CTA "Start Free Trial"
- **Success**: First project created with tasks

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
│ Workspace Setup│
│ (Company name) │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ Role Selection │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ First Project  │
│ Template Select│
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ Guided Tour    │
│ Create 1st Task│
└───────┬───────┘
        │
        ▼
┏━━━━━━━━━━━━━━━━┓
┃  ✓ SUCCESS     ┃
┃ Dashboard View ┃
┗━━━━━━━━━━━━━━━━┛
```

### Step Detail

| Step | Screen | User Action | System Response | Notes |
|------|--------|-------------|-----------------|-------|
| 1 | Landing | Click "Start Free Trial" | Show signup form | Prominent CTA |
| 2 | Signup | Enter email, password | Validate, create account | Social login option |
| 3 | Workspace | Enter company name | Create workspace | Pre-fill from email domain |
| 4 | Role | Select role from options | Customize initial view | 3 clear role cards |
| 5 | Template | Choose project template | Create sample project | "Start blank" option |
| 6 | Tour | Follow guided task creation | Highlight features | Can dismiss anytime |
| 7 | Dashboard | View completed setup | Show project with tasks | Celebration moment |

---

## Example: Create & Assign Task (Inline)

```
┌───────────────────────┐
│ Project Task List      │
│                        │
│ [Task 1]               │
│ [Task 2]               │
│ [+ Add Task] ◀─── Click or Enter
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Inline Task Editor     │
│ [Task title input___]  │
│ @assign  #date  ...    │
└───────────┬───────────┘
            │ Type title, press Enter
            ▼
┌───────────────────────┐
│ ✓ Task Created         │
│ Click to add details   │
└───────────────────────┘
```

### Quick Actions
- `/assign @name` — Assign to team member
- `/due Friday` — Set due date with natural language
- `/priority high` — Set priority
- `Tab` — Move through fields

---

## Common Flow Patterns

### Progressive Disclosure Pattern
Reveal complexity gradually:
1. Show minimal required fields first
2. Offer "Advanced options" expandable
3. Auto-detect and pre-fill where possible

### Wizard Pattern
Guide through multi-step process:
1. Clear step indicator (Step 2 of 4)
2. Back button always available
3. Save progress automatically
4. Allow skipping optional steps

### Inline Creation Pattern
Create without leaving context:
1. Click "+ Add" in the list
2. Inline form appears in place
3. Enter minimum required info
4. Press Enter to create, Escape to cancel

### Search-then-Act Pattern
1. Type to search/filter
2. Results update in real-time
3. Select item from results
4. Take action on selected item

### Confirmation Pattern
For destructive or irreversible actions:
1. User initiates action
2. System shows confirmation with consequences
3. Require explicit confirmation (type name, check box)
4. Provide undo option when possible

---

## Flow Summary Map Example

```
                    ┌─────────────┐
                    │  SIGN UP    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  ONBOARD    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
┌─────────────────▶│  DASHBOARD  │◀────────────────┐
│                  └───┬───┬─────┘                 │
│              ┌───────┘   └───────┐               │
│              ▼                   ▼               │
│       ┌────────────┐      ┌────────────┐         │
│       │  CREATE    │      │  MY TASKS  │         │
│       │  PROJECT   │      │            │         │
│       └──────┬─────┘      └──────┬─────┘         │
│              ▼                   ▼               │
│       ┌────────────┐      ┌────────────┐         │
└───────│  PROJECT   │─────▶│  TASK      │─────────┘
        │  VIEW      │      │  DETAIL    │
        └────────────┘      └────────────┘
```

This map shows how all flows interconnect, helping identify navigation requirements and re-entry points.
