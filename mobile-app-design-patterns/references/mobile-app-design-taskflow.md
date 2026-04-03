# Mobile App Design: TaskFlow - Detailed Reference

Detailed reference content for mobile app design.

---

## Mobile App Design: TaskFlow
### Platform Strategy
**Approach**: Platform-native navigation with unified visual identity

---

### iOS Design

#### Task List Screen
```
┌───────────────────────┐
│  ┌───────────────────┐  │  <- Dynamic Island area
├──┴───────────────────┴──┤
│  Tasks                 +  │  <- Nav bar with add
│  My Tasks                 │  <- Large title
├───────────────────────┤
│  [🔍 Search tasks...    ]  │  <- Search bar
├───────────────────────┤
│  TODAY                    │  <- Section header
├───────────────────────┤
│  ○  Review homepage       │
│     Acme • Due today   >  │
├───────────────────────┤
│  ○  Client feedback       │
│     Beta • Due today   >  │
├───────────────────────┤
│  ●  Final assets ✓        │  <- Completed
│     Acme • Completed   >  │
├───────────────────────┤
│  UPCOMING                 │
├───────────────────────┤
│  ○  Sprint planning       │
│     Team • Tomorrow    >  │
│                           │
├───────────────────────┤
│                           │  <- Home indicator
│  🏠    📁    ✅    👤     │  <- Tab bar
│ Home  Proj  Tasks  Me    │
└───────────────────────┘
```

**iOS Specifications**:
- Large title: SF Pro Bold 34pt
- Section header: SF Pro Semibold 13pt, uppercase, Gray-500
- Task title: SF Pro 17pt
- Task meta: SF Pro 15pt, Gray-500
- Tab bar icons: SF Symbols, 25pt
- Row height: 76pt minimum
- Swipe actions: Complete (green), Delete (red)

---

### Android Design

#### Task List Screen
```
┌───────────────────────┐
│  [status bar]            │
├───────────────────────┤
│  ←  My Tasks         🔍  │  <- Top app bar
├───────────────────────┤
│  [Filter chips row]      │  <- Filter chips
│  (All) (Today) (Week)    │
├───────────────────────┤
│  Today                   │
├───────────────────────┤
│  ☐  Review homepage      │
│     Acme • Due today     │
├───────────────────────┤
│  ☐  Client feedback      │
│     Beta • Due today     │
├───────────────────────┤
│  ☑  Final assets         │  <- Completed
│     Acme • Completed     │
├───────────────────────┤
│  Tomorrow                │
├───────────────────────┤
│  ☐  Sprint planning      │
│     Team • Tomorrow      │
│                     ┌───┐│
│                     │ + ││  <- FAB
│                     └───┘│
├───────────────────────┤
│  🏠    📁    ✅    👤    │  <- Bottom nav
│ Home  Proj  Tasks  Me   │
└───────────────────────┘
```

**Android Specifications**:
- Top app bar: Roboto Medium 22sp
- Section header: Roboto Medium 14sp, uppercase
- Task title: Roboto Regular 16sp
- Task meta: Roboto Regular 14sp, on-surface-variant
- FAB: 56dp, Violet-500, + icon
- Bottom nav: 80dp, Material icons
- Row height: 72dp minimum
- Checkbox: Material checkbox 24dp

---

### Platform Comparison

| Element | iOS | Android |
|---------|-----|----------|
| Add task | Nav bar + button | FAB |
| Task completion | Custom circle | Material checkbox |
| Filtering | Scope bar | Filter chips |
| Row disclosure | Chevron > | None (tap row) |
| Search | Collapsing search | Search icon → expand |
| Completed style | Strikethrough | Checkbox filled |
| Swipe actions | Left/Right | Left only |
```

---
