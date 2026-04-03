# Information Architecture: TaskFlow - Detailed Reference

Detailed reference content for information architecture.

---

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
