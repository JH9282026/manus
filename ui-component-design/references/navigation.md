# Navigation - Detailed Reference

Detailed reference content for component design.

---

## Navigation
### Sidebar Nav Item

**States**
```
Default:    [icon] Projects        <- Gray-600 text
Hover:      [■■■■■■■■■■■]          <- Gray-100 bg
Active:     [🟣 Projects 🟣]        <- Violet-50 bg, Violet-600 text
```

| State | Background | Text | Icon | Indicator |
|-------|------------|------|------|----------|
| Default | Transparent | Gray-600 | Gray-400 | None |
| Hover | Gray-100 | Gray-700 | Gray-500 | None |
| Active | Violet-50 | Violet-700 | Violet-500 | Left bar Violet-500 |
| Disabled | Transparent | Gray-300 | Gray-200 | None |

```css
.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px;
  border-radius: 8px;
  color: #475569;
  text-decoration: none;
  transition: all 150ms ease;
}
.nav-item:hover {
  background: #F1F5F9;
  color: #334155;
}
.nav-item.active {
  background: #F5F3FF;
  color: #6D28D9;
}
.nav-item.active::before {
  content: '';
  position: absolute;
  left: 0;
  width: 3px;
  height: 24px;
  background: #8B5CF6;
  border-radius: 0 2px 2px 0;
}
```

---

## Badges & Tags
### Status Badge

**Variants**
| Status | Background | Text | Icon |
|--------|------------|------|------|
| Success | #D1FAE5 | #065F46 | ✓ |
| Warning | #FEF3C7 | #92400E | ! |
| Error | #FEE2E2 | #991B1B | × |
| Info | #DBEAFE | #1E40AF | i |
| Neutral | #F1F5F9 | #475569 | |
| Purple | #EDE9FE | #5B21B6 | |

```css
.badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 500;
}
.badge-success {
  background: #D1FAE5;
  color: #065F46;
}
```

---

## Component Checklist
- [ ] Buttons (Primary, Secondary, Ghost, Destructive)
- [ ] Input fields (Text, Email, Password, Search)
- [ ] Select/Dropdown
- [ ] Checkbox & Radio
- [ ] Toggle/Switch
- [ ] Cards (Default, Interactive, Selected)
- [ ] Badges/Tags
- [ ] Avatar (with sizes)
- [ ] Table (with sorting)
- [ ] Modal/Dialog
- [ ] Toast notifications
- [ ] Tooltip
- [ ] Navigation items
- [ ] Tabs
- [ ] Breadcrumbs
- [ ] Pagination
- [ ] Empty states
- [ ] Loading states (Spinner, Skeleton)
```

---
