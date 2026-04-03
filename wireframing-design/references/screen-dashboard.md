# Screen: Dashboard - Detailed Reference

Detailed reference content for wireframing.

---

## Screen: Dashboard
### Purpose
Provide at-a-glance overview of all projects and personal tasks. Help Sarah quickly identify projects needing attention without diving into details.

### Desktop Wireframe

```
┌───────────┬─────────────────────────────────────────────────┐
│           │  [🔍 Search or jump to... ⌘K]          🔔  ┌─┐ │
│  TaskFlow │                                        │AV│ │
├───────────┼──────────────────────────────────────└─┘──────┤
│           │                                                   │
│  🏠 Dash   │  Good morning, Sarah           Friday, Mar 5     │
│           │                                                   │
│  📁 Proj   ├───────────────┬───────────────┬───────────────┤
│           │  ACTIVE PROJ  │  TASKS DUE    │  AT RISK       │
│  ✅ Tasks  │     12       │    5 today   │     2          │
│           │               │               │  🟡 Acme, 🔴 Foo  │
│  👥 Team   ├───────────────┴───────────────┴───────────────┤
│           │                                                   │
│  🏬 Client │  MY TASKS TODAY (5)                [View All →]  │
│           │                                                   │
│  ⏱ Time   │  ☐ Review homepage mockups     Acme • Due today  │
│           │  ☐ Client feedback call         Beta • Due today  │
│  📊 Report │  ☐ Approve final assets        Acme • Due today  │
│           │  ☐ Sprint planning             Team • Due today  │
│           │  ☐ Review contractor work      Misc • Due today  │
│  ───────  │                                                   │
│           ├─────────────────────────────────────────────────┤
│           │                                                   │
│  [+ New]  │  ACTIVE PROJECTS (12)              [View All →]  │
│           │                                                   │
│           │  ┌────────────┐ ┌────────────┐ ┌────────────┐  │
│           │  │ Acme       │ │ Beta       │ │ Gamma      │  │
│           │  │ Rebrand    │ │ Website    │ │ App Design │  │
│           │  │            │ │            │ │            │  │
│           │  │ 🟡 4 tasks  │ │ 🟢 On track │ │ 🟢 On track │  │
│           │  │ Due Fri    │ │ Due Mar 15 │ │ Due Mar 20 │  │
│           │  └────────────┘ └────────────┘ └────────────┘  │
│           │                                                   │
└───────────┴─────────────────────────────────────────────────┘
```

### Annotations

1. **Global Search** (Top bar)
   - Purpose: Quick access to any project, task, or person
   - Behavior: Cmd+K opens command palette style search
   - Shows recent items, quick actions, and search results

2. **Stat Cards** (Top row)
   - Purpose: At-a-glance health metrics
   - "At Risk" is clickable - shows projects needing attention
   - Color-coded: green = good, yellow = warning, red = alert

3. **My Tasks Today**
   - Purpose: Personal task list for the day
   - Behavior: Checkboxes for quick completion
   - Click task to open detail panel (slide-in)
   - "View All" goes to full task list

4. **Active Projects Grid**
   - Purpose: Quick access to current projects
   - Shows: Project name, client, status, next deadline
   - Color indicator matches project health
   - Click card to open project

### Mobile Wireframe

```
┌───────────────────────┐
│  ☰  TaskFlow    🔍  🔔  │
├───────────────────────┤
│                       │
│  Morning, Sarah       │
│                       │
│  ┌───────┬───────┬─────┐  │
│  │  12   │   5   │  2  │  │  <- Compact stats
│  │ Proj  │ Tasks │ Risk│  │
│  └───────┴───────┴─────┘  │
│                       │
│  Today (5)   [See all]│
│                       │
│  ☐ Review mockups     │
│    Acme • Due today   │
│  ───────────────────  │
│  ☐ Client call        │
│    Beta • Due today   │
│  ───────────────────  │
│  ☐ Approve assets     │
│    Acme • Due today   │
│                       │
│  Projects    [See all]│
│  ┌───────────────────┐  │
│  │ Acme Rebrand  🟡   │  │
│  └───────────────────┘  │
│                       │
├───────────────────────┤
│  🏠   📁  (➕)  ✅   ⋮   │  <- Tab bar
└───────────────────────┘
```

### Responsive Notes
- **Desktop (1200px+)**: Full sidebar, 3-column project grid
- **Tablet (768-1199px)**: Collapsible sidebar, 2-column grid
- **Mobile (<768px)**: Bottom tabs, single column, compact stats

### Open Questions
- [ ] Should "At Risk" show inline list or link to filtered view?
- [ ] How many projects to show before "View All"?
- [ ] Include time tracking widget on dashboard?
```

---
