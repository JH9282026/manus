---
name: information-architecture
description: "Structure and organize content, navigation, and information hierarchies for intuitive user experiences. Use for: site mapping, content organization, navigation design, taxonomy creation, and structuring complex information."
---

# Information Architecture

## Description

Information Architecture (IA) is the structural design of information environments. It involves organizing, labeling, and structuring content so users can find what they need efficiently. Good IA is invisible – users simply find what they expect where they expect it.

## When to Use

- Designing a new website or app structure
- Reorganizing existing navigation
- Planning content strategy
- Before wireframing to establish structure
- When users report difficulty finding content

---

## Instructions for AI Agents

### Step 1: Content Inventory

**Prompt to identify content:**
```
For [PRODUCT/WEBSITE], list all content and features needed:

1. **Pages/Screens**: All unique views users need
2. **Features**: Interactive functionality
3. **Content Types**: Articles, products, user data, etc.
4. **User Actions**: Things users can do
5. **System Info**: Settings, account, help, etc.

Group these into logical categories.
```

### Step 2: Create Site Map

**Site map template:**

```markdown
## Site Map: [PRODUCT]

### Primary Navigation (Always Visible)

```
[PRODUCT]
│
├── Home / Dashboard
│
├── [Section 1]
│   ├── [Subsection 1.1]
│   ├── [Subsection 1.2]
│   └── [Subsection 1.3]
│
├── [Section 2]
│   ├── [Subsection 2.1]
│   └── [Subsection 2.2]
│
├── [Section 3]
│
└── [Section 4]
```

### Secondary Navigation (User Menu / Footer)

```
[User Menu]
├── Account Settings
├── Billing
├── Team Management
└── Log Out

[Footer]
├── About
├── Privacy Policy
├── Terms of Service
└── Contact
```
```

### Step 3: Define Navigation Patterns

**Navigation types to consider:**

| Type | Best For | Example |
|------|----------|--------|
| Top Bar | Primary nav, 4-7 items | Main sections |
| Side Bar | Deep navigation, many items | Dashboard apps |
| Tab Bar | Mobile, 3-5 items | Mobile app main nav |
| Hamburger | Secondary items, mobile overflow | Settings, account |
| Breadcrumbs | Deep hierarchies | E-commerce categories |
| Search | Large content libraries | Documentation, products |

### Step 4: Label Strategy

**Naming principles:**

```markdown
## Navigation Labels

### Principles
1. **User language**: Use words users know, not internal jargon
2. **Specific over generic**: "Pricing" not "Information"
3. **Consistent verb form**: All actions or all nouns
4. **Scannable**: Front-load important words

### Label Audit

| Current Label | User Language | Final Label | Notes |
|---------------|---------------|-------------|-------|
| [Label 1] | [How users say it] | [Final] | [Why] |
```

### Step 5: Content Grouping

**Card sorting simulation prompt:**
```
Imagine [PERSONA] is looking for [CONTENT/FEATURE].
Where would they expect to find it?

Test these groupings:
- Would [Item A] and [Item B] logically be together?
- If looking for [Item C], would they check [Section X]?
- What label best describes [Group of items]?
```

---

## Example Input/Output

### Example Input

```markdown
**Product**: TaskFlow - Project management for creative agencies
**Key Features**: Projects, tasks, team, clients, time tracking, reports
**Personas**: Creative Director, Project Manager, Designer
```

### Example Output

```markdown
## Information Architecture: TaskFlow

### Content Inventory

#### Core Content
- Projects (list, detail, archive)
- Tasks (list, detail, my tasks)
- Team members (list, profiles)
- Clients (list, detail)
- Time entries
- Reports (project, team, client)

#### User Content
- Profile
- Settings (personal, workspace)
- Notifications

#### Supporting
- Help/Documentation
- What's New
- Keyboard shortcuts

---

### Site Map

```
TaskFlow App
│
├── 🏠 Dashboard (Home)
│   ├── Overview widgets
│   ├── Recent projects
│   └── My tasks due today
│
├── 📁 Projects
│   ├── All Projects (list view)
│   ├── [Project Name] (detail)
│   │   ├── Overview
│   │   ├── Tasks (list/board/timeline)
│   │   ├── Files
│   │   ├── Time Log
│   │   └── Settings
│   └── Archived Projects
│
├── ✅ My Tasks
│   ├── Today
│   ├── Upcoming
│   ├── Completed
│   └── [Task Detail] (modal)
│
├── 👥 Team
│   ├── All Members
│   ├── [Member Profile]
│   ├── Workload View
│   └── Invite Members
│
├── 🏬 Clients
│   ├── All Clients
│   └── [Client Detail]
│       ├── Projects
│       ├── Contacts
│       └── Billing Info
│
├── ⏱️ Time
│   ├── My Time (personal log)
│   ├── Team Time (if manager)
│   └── Time Reports
│
└── 📊 Reports
    ├── Project Reports
    ├── Team Reports
    └── Client Reports

---

[User Menu - Top Right]
├── My Profile
├── Preferences
├── Workspace Settings (admin only)
├── Billing (admin only)
├── Help & Support
└── Log Out

[Quick Actions - Persistent]
├── + New Project
├── + New Task
└── 🔍 Search (Cmd+K)

[Notifications - Bell Icon]
├── All Notifications
└── Settings
```

---

### Navigation Design

#### Desktop: Sidebar Navigation

```
┌────────────────────────────────────────────────┐
│  ┌─────────┐  [Search]           [🔔] [Avatar]│
│  │TaskFlow │                                 │
├──┴──────────┼───────────────────────────────────┤
│  Dashboard  │                                 │
│  Projects   │       MAIN CONTENT AREA        │
│  My Tasks   │                                 │
│  Team       │                                 │
│  Clients    │                                 │
│  Time       │                                 │
│  Reports    │                                 │
│             │                                 │
│  ────────── │                                 │
│  [+ New]    │                                 │
└─────────────┴───────────────────────────────────┘
```

**Rationale**: Sidebar provides:
- Persistent visibility of all sections
- Room for expansion (sub-items)
- Familiar pattern for SaaS dashboards
- Space for quick actions

#### Mobile: Tab Bar + Hamburger

```
┌─────────────────────────┐
│  [☰] TaskFlow  [🔔][👤] │  <- Top bar with hamburger
├─────────────────────────┤
│                         │
│                         │
│    MAIN CONTENT AREA    │
│                         │
│                         │
├─────────────────────────┤
│ [🏠]  [📁]  [+]  [✅]  [⋮] │  <- Bottom tab bar
│ Home  Proj  New Tasks More │
└─────────────────────────┘

Tab Bar Items:
1. Home (Dashboard)
2. Projects
3. + (Quick Add - FAB style)
4. Tasks (My Tasks)
5. More (Team, Clients, Time, Reports, Settings)
```

**Rationale**: 
- 5 items max for thumb reach
- Most used features in tabs
- Less used in "More" menu
- Prominent "Add" action

---

### Label Decisions

| Feature | Rejected Labels | Chosen Label | Reason |
|---------|-----------------|--------------|--------|
| Main overview | Home, Overview | Dashboard | Industry standard for SaaS |
| Task list | To-dos, Activities | My Tasks | Clear ownership, familiar |
| Time tracking | Timesheets, Hours | Time | Short, clear, modern |
| People section | Members, Users | Team | Warmer, agency-appropriate |
| Analytics | Analytics, Insights | Reports | Action-oriented, familiar |

---

### Navigation by Persona

| Persona | Primary Nav Path | Key Actions |
|---------|------------------|-------------|
| Sarah (Director) | Dashboard → Projects → Reports | Check status, review progress |
| Marcus (PM) | My Tasks → Projects → Team | Manage tasks, check workload |
| Jordan (Designer) | My Tasks → [Task] | See assignments, update status |

---

### Search & Findability

**Global Search (Cmd+K)**
- Search projects by name
- Search tasks by title
- Search team members
- Search clients
- Quick actions ("Create project", "Invite member")

**Filters by Section**
- Projects: Status, Client, Date range
- Tasks: Assignee, Due date, Priority, Status
- Team: Role, Availability
- Time: Date range, Project, Person
```

---

## Prompts Library

### Quick IA Generation
```
Create an information architecture for [PRODUCT TYPE] with these features:
[FEATURE LIST]

Include:
1. Site map (tree structure)
2. Primary navigation items (max 7)
3. Secondary navigation (user menu)
4. Mobile navigation strategy
```

### Navigation Audit
```
Review this navigation structure:
[CURRENT NAV]

Evaluate:
1. Is anything missing users would expect?
2. Are items grouped logically?
3. Are labels clear and consistent?
4. Is the depth appropriate (rule of 3 clicks)?
5. Suggested improvements?
```

### Content Hierarchy
```
For [CONTENT TYPE], define the information hierarchy:

1. What's the most important info to show first?
2. What's secondary but still on first view?
3. What can be in "show more" or secondary views?
4. What's rarely needed (settings, advanced)?
```

---

## Success Criteria

### Minimum Requirements
- [ ] Site map covering all content
- [ ] Primary navigation defined (max 7 items)
- [ ] Secondary navigation planned
- [ ] Mobile navigation strategy
- [ ] Clear, consistent labels

### Quality Indicators
- [ ] Any content findable in 3 clicks or less
- [ ] Labels pass the "5-second test" (instantly understood)
- [ ] Navigation serves all personas
- [ ] Consistent patterns throughout
- [ ] Room for future growth

---

## Related Skills

- **Previous**: `user_flows.md` - Understand user journeys
- **Next**: `wireframing.md` - Apply IA to screen layouts
- **Related**: `layout_grids.md` - Grid structure for navigation

## References

- [Content Strategy Ia](references/content-strategy-ia.md)
- [Ia Principles Methods](references/ia-principles-methods.md)
- [Site Mapping Flows](references/site-mapping-flows.md)
