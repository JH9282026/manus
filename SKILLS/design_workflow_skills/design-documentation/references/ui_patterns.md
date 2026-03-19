## UI Patterns

### Form Pattern

**Structure:**
```
┌──────────────────────────────┐
│  Form Title (H2)            │
│  Optional description       │
│                              │
│  [Label]                     │
│  [Input Field          ]    │
│  Helper text                 │
│                              │
│  [Label]                     │
│  [Input Field          ]    │
│                              │
│        [Cancel] [Submit]     │
└──────────────────────────────┘
```

**Spacing:**
- Title to description: 8px
- Description to first field: 24px
- Label to input: 6px
- Input to helper: 4px
- Between fields: 20px
- Fields to buttons: 32px

**Behavior:**
- Validate on blur (first time)
- Validate on change (after error shown)
- Submit focuses first error
- Loading state disables form

### Empty State Pattern

**Structure:**
```
┌──────────────────────────────┐
│                              │
│       ┌──────────┐          │
│       │  🖼️      │          │
│       │ Illo     │          │
│       └──────────┘          │
│                              │
│      No projects yet         │
│                              │
│   Create your first project  │
│   to get started.            │
│                              │
│     [Create Project]         │
│                              │
└──────────────────────────────┘
```

**Content:**
- Illustration: Relevant, friendly, 200-300px
- Title: Short, specific to context
- Description: Action-oriented, 1-2 lines
- CTA: Primary button for main action

### Loading Pattern

**Skeleton Loading:**
- Match layout structure
- Pulse animation: 1.5s, ease-in-out
- Replace entire content area
- No spinners for initial loads

**Inline Loading:**
- Use for actions (button loading)
- Spinner size matches context
- Disable triggering element
- Show "Loading..." text
```

---
