---
name: design-documentation-specs
description: "Create comprehensive design specifications and documentation that capture all design decisions for implementation. Use for: writing design specs, documenting component behavior, creating style guides, specifying interaction patterns, recording design rationale, and producing design system documentation for development teams."
---

# Design Documentation

Create comprehensive design specifications and documentation that capture all design decisions for implementation.

# Skill: Design Documentation

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Design Documentation |
| **Category** | Delivery |
| **Phase** | 6 - Delivery |
| **Estimated Time** | 60-90 minutes |
| **Dependencies** | All design phases complete, score ≥9/10 |
| **Outputs** | Complete design specification document |

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
    "12": { "value": "3rem" },
    "16": { "value": "4rem" }
  }
}
```

### Effects

```json
{
  "shadow": {
    "sm": { "value": "0 1px 2px rgba(0,0,0,0.05)" },
    "md": { "value": "0 4px 6px rgba(0,0,0,0.07)" },
    "lg": { "value": "0 10px 15px rgba(0,0,0,0.1)" },
    "xl": { "value": "0 20px 25px rgba(0,0,0,0.15)" }
  },
  "radius": {
    "sm": { "value": "4px" },
    "md": { "value": "8px" },
    "lg": { "value": "12px" },
    "xl": { "value": "16px" },
    "full": { "value": "9999px" }
  },
  "transition": {
    "fast": { "value": "150ms ease-out" },
    "normal": { "value": "200ms ease-out" },
    "slow": { "value": "300ms ease-out" }
  }
}
```
```

### Step 3: Component Documentation

**Component spec template:**

```markdown

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

## Example Output
### Complete Documentation Package

```markdown
# TaskFlow Design Documentation

Version: 1.0
Last Updated: [Date]
Design Score: 9.2/10

## 2. Design Principles
1. **Clarity over cleverness**: Every element should be immediately understandable
2. **Calm productivity**: Reduce visual noise, help users focus
3. **Consistent but flexible**: System that adapts without breaking
4. **Accessible by default**: No user left behind

---

## Using the Reference Files

### When to Read Each Reference

**`./references/4-components.md`** — Read when you need detailed guidance on 4 components aspects of this skill.

**`./references/7-assets.md`** — Read when you need detailed guidance on 7 assets aspects of this skill.

**`./references/component-button.md`** — Read when you need detailed guidance on component button aspects of this skill.

**`./references/related-skills.md`** — Read when you need detailed guidance on related skills aspects of this skill.

**`./references/table-of-contents.md`** — Read when you need detailed guidance on table of contents aspects of this skill.
