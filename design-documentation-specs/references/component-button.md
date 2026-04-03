# Component: Button - Detailed Reference

Detailed reference content for design documentation.

---

## Component: Button
### Description
Buttons trigger actions or navigate users. Use the appropriate variant based on action importance.

### Variants

| Variant | Usage | Visual |
|---------|-------|--------|
| Primary | Main actions, CTAs | Filled, primary color |
| Secondary | Alternative actions | Outlined |
| Ghost | Tertiary actions | Text only |
| Destructive | Delete, remove | Red filled |

### Sizes

| Size | Height | Padding | Font | Icon |
|------|--------|---------|------|------|
| sm | 32px | 8px 12px | 13px | 16px |
| md | 40px | 10px 16px | 14px | 18px |
| lg | 48px | 12px 24px | 16px | 20px |

### States

#### Primary Button

| State | Background | Text | Border | Other |
|-------|------------|------|--------|-------|
| Default | primary-500 | white | none | |
| Hover | primary-400 | white | none | translateY(-1px) |
| Focus | primary-500 | white | none | ring: 3px primary-200 |
| Active | primary-600 | white | none | scale(0.98) |
| Disabled | primary-200 | white | none | opacity: 0.6 |
| Loading | primary-500 | -- | none | spinner |

### Anatomy

```
┌────────────────────────────┐
│   padding: 10px 16px       │
│                            │
│   [Icon 18px]  [Text 14px] │
│       gap: 8px             │
│                            │
└────────────────────────────┘
        border-radius: 8px
```

### CSS Specification

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-2);
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-medium);
  transition: var(--transition-fast);
  cursor: pointer;
}

.btn-md {
  height: 40px;
  padding: 10px 16px;
  font-size: 14px;
}

.btn-primary {
  background: var(--color-primary-500);
  color: white;
  border: none;
}

.btn-primary:hover {
  background: var(--color-primary-400);
  transform: translateY(-1px);
}

.btn-primary:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px var(--color-primary-200);
}

.btn-primary:active {
  background: var(--color-primary-600);
  transform: scale(0.98);
}

.btn-primary:disabled {
  background: var(--color-primary-200);
  opacity: 0.6;
  cursor: not-allowed;
}
```

### Accessibility

- Minimum touch target: 44×44px
- Contrast ratio: 4.5:1 (text on background)
- Focus state: Visible ring
- Disabled: aria-disabled="true"
- Loading: aria-busy="true", spinner aria-label="Loading"

### Usage Guidelines

**Do:**
- Use Primary for main page action
- Use consistent sizing within context
- Include loading state for async actions
- Use icons to reinforce meaning

**Don't:**
- Don't use multiple Primary buttons in one view
- Don't disable without clear reason
- Don't use Ghost for important actions
- Don't mix sizes in same button group
```

### Step 4: Pattern Documentation

```markdown
