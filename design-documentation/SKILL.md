---
name: design-documentation
description: "Create comprehensive design documentation including specs, guidelines, and handoff materials for development teams. Use for: developer handoff, design specifications, style guides, component documentation, and ensuring accurate implementation."
---

# Design Documentation

## Description

Design Documentation creates comprehensive specifications that capture all design decisions, enabling consistent implementation and future maintenance. This is the source of truth for developers and stakeholders.

## When to Use

- After design achieves 9/10+ score
- Before developer handoff
- When onboarding new team members
- For design system documentation
- Creating style guides

---

## Instructions for AI Agents

### Step 1: Documentation Structure

**Master documentation outline:**

```markdown
## Design Documentation Structure

### 1. Overview
- Project summary
- Design principles
- Key decisions and rationale

### 2. Design Tokens
- Colors (full palette)
- Typography (scale and styles)
- Spacing (scale)
- Shadows
- Border radii
- Breakpoints
- Animations/transitions

### 3. Components
- Component inventory
- Individual component specs
- States and variants
- Usage guidelines

### 4. Layouts
- Grid system
- Page templates
- Responsive behavior

### 5. Patterns
- Common UI patterns
- Interaction patterns
- Content patterns

### 6. Assets
- Icons
- Illustrations
- Images
- Logos

### 7. Accessibility
- Guidelines
- Compliance checklist
- Implementation notes
```

### Step 2: Design Tokens Documentation

**Token documentation template:**

```markdown
## Design Tokens: [PROJECT]

### Colors

#### Brand Colors

```json
{
  "color": {
    "primary": {
      "50": { "value": "#F5F3FF", "type": "color" },
      "100": { "value": "#EDE9FE", "type": "color" },
      "200": { "value": "#DDD6FE", "type": "color" },
      "300": { "value": "#C4B5FD", "type": "color" },
      "400": { "value": "#A78BFA", "type": "color" },
      "500": { "value": "#8B5CF6", "type": "color" },
      "600": { "value": "#7C3AED", "type": "color" },
      "700": { "value": "#6D28D9", "type": "color" },
      "800": { "value": "#5B21B6", "type": "color" },
      "900": { "value": "#4C1D95", "type": "color" }
    }
  }
}
```

#### Usage

| Token | CSS Variable | Usage |
|-------|--------------|-------|
| primary.500 | --color-primary-500 | Primary buttons, links |
| primary.600 | --color-primary-600 | Hover states |
| primary.100 | --color-primary-100 | Selected backgrounds |

### Typography

```json
{
  "font": {
    "family": {
      "primary": { "value": "'Inter', sans-serif" },
      "mono": { "value": "'JetBrains Mono', monospace" }
    },
    "size": {
      "xs": { "value": "0.75rem" },
      "sm": { "value": "0.875rem" },
      "base": { "value": "1rem" },
      "lg": { "value": "1.125rem" },
      "xl": { "value": "1.25rem" },
      "2xl": { "value": "1.5rem" },
      "3xl": { "value": "1.875rem" },
      "4xl": { "value": "2.25rem" }
    },
    "weight": {
      "normal": { "value": "400" },
      "medium": { "value": "500" },
      "semibold": { "value": "600" },
      "bold": { "value": "700" }
    },
    "lineHeight": {
      "tight": { "value": "1.25" },
      "normal": { "value": "1.5" },
      "relaxed": { "value": "1.75" }
    }
  }
}
```

### Spacing

```json
{
  "spacing": {
    "0": { "value": "0" },
    "1": { "value": "0.25rem" },
    "2": { "value": "0.5rem" },
    "3": { "value": "0.75rem" },
    "4": { "value": "1rem" },
    "5": { "value": "1.25rem" },
    "6": { "value": "1.5rem" },
    "8": { "value": "2rem" },
    "10": { "value": "2.5rem" },

*[See reference files for complete details]*

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

*[See reference files for complete details]*

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

## Table of Contents

1. [Overview](#overview)
2. [Design Principles](#principles)
3. [Design Tokens](#tokens)
4. [Components](#components)
5. [Layouts](#layouts)
6. [Patterns](#patterns)
7. [Assets](#assets)
8. [Accessibility](#accessibility)

---

## 1. Overview

**Product**: TaskFlow - Project management for creative agencies
**Platforms**: Web (responsive), iOS, Android
**Design Lead**: [Name]
**Last Design Review**: [Date] - 9.2/10

### Key Decisions

| Decision | Rationale |
|----------|----------|
| Violet primary color | Differentiates from blue competitors, feels creative |
| Inter typeface | Modern, highly readable, good for dashboards |
| Card-based layouts | Chunks information, scannable |
| Sidebar navigation | Persistent access for dashboard app |

---

## 2. Design Principles

1. **Clarity over cleverness**: Every element should be immediately understandable
2. **Calm productivity**: Reduce visual noise, help users focus
3. **Consistent but flexible**: System that adapts without breaking
4. **Accessible by default**: No user left behind

---

## 3. Design Tokens

[Full token specifications as shown above]

---

## 4. Components

### Component Index

| Category | Components |
|----------|------------|
| Actions | Button, IconButton, Link |
| Inputs | TextField, Select, Checkbox, Radio, Toggle, TextArea |
| Display | Card, Badge, Avatar, Table, List |
| Navigation | Sidebar, Tabs, Breadcrumb, Pagination |
| Feedback | Alert, Toast, Modal, Tooltip, Progress |
| Layout | Header, Footer, Container, Divider |

[Individual component specs follow]

---

## 5. Layouts

### Grid System
- 12 columns
- 24px gutters (desktop), 16px (mobile)
- Max-width: 1200px

### Page Templates
- Dashboard
- List view
- Detail view
- Settings
- Empty state

---

## 6. Patterns

[Pattern documentation as shown above]

---

## 7. Assets

### Icons
- Library: Heroicons
- Sizes: 16, 20, 24, 32px
- Style: Outlined (default), Solid (emphasis)

### Illustrations
- Source: unDraw
- Color: Primary-500 (#8B5CF6)
- Usage: Empty states, onboarding

---

## 8. Accessibility

### Standards
- Target: WCAG 2.1 AA
- Status: Compliant

### Checklist
- [x] Color contrast meets requirements
- [x] Focus states visible
- [x] Keyboard navigation works
- [x] Touch targets ≥44px
- [x] Reduced motion supported
- [x] Screen reader compatible
```

---

## Success Criteria

### Minimum Requirements
- [ ] All tokens documented
- [ ] Key components specified
- [ ] Usage guidelines included
- [ ] Accessibility documented

### Quality Indicators
- [ ] Developers can implement without questions
- [ ] Decisions have rationale
- [ ] Easy to find information
- [ ] Maintained and versioned

---

## Related Skills

- **Previous**: Design achieving 9/10+
- **Next**: `handoff_preparation.md` - Developer-ready assets


## Using the Reference Files

**`/references/design_tokens:_[project]_full.md`** — Design Tokens: [PROJECT] (Full).

**`/references/component:_button_full.md`** — Component: Button (Full).

**`/references/example_output.md`** — Example Output.

