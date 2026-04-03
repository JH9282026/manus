---
name: ui-component-design
description: "Design reusable UI components with consistent states, variants, and interaction patterns for design systems. Use for: creating buttons, forms, cards, navigation elements, modals, designing component libraries, defining interactive states (hover, active, disabled, focus), and building scalable design system foundations."
---

# Component Design

Design reusable UI components with consistent states, variants, and interaction patterns for design systems.

# Skill: Component Design

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Component Design |
| **Category** | Visual Design |
| **Phase** | 3 - Visual Design |
| **Estimated Time** | 60-120 minutes |
| **Dependencies** | `color_palettes.md`, `typography.md`, `spacing_rhythm.md` |
| **Outputs** | Complete UI component library with states and variants |

## Description
Component Design creates reusable, consistent UI building blocks. A well-designed component library ensures visual consistency, speeds up design/development, and maintains quality across all interfaces.

## When to Use
- After foundational design tokens (colors, type, spacing) are defined
- Before designing full pages
- Building a design system
- When UI needs consistency audit
- Creating handoff documentation

---

## Instructions for AI Agents
### Step 1: Identify Component Needs

**Prompt to inventory components:**
```
Based on the wireframes for [PROJECT], list all UI components needed:

**Actions**
- Buttons (primary, secondary, etc.)
- Links
- Icon buttons

**Inputs**
- Text inputs
- Select/dropdowns
- Checkboxes/radios
- Toggles
- Text areas

**Display**
- Cards
- Tables
- Lists
- Badges/tags
- Avatars
- Progress indicators

**Navigation**
- Tabs
- Breadcrumbs
- Pagination
- Menus

**Feedback**
- Alerts/toasts
- Modals
- Tooltips
- Empty states

**Layout**
- Headers
- Sidebars
- Footers
```

### Step 2: Define Component States

**Standard interactive states:**

| State | When | Visual Change |
|-------|------|---------------|
| Default | Normal state | Base appearance |
| Hover | Mouse over | Slight change (lighter/darker, shadow) |
| Focus | Keyboard focus | Visible focus ring |
| Active | Being clicked | Pressed appearance |
| Disabled | Not available | Reduced opacity, no interaction |
| Loading | Processing | Spinner, skeleton |
| Error | Validation failed | Error styling |
| Success | Action completed | Success styling |

### Step 3: Component Specification Template

**For each component, document:**

```markdown

## Component: [Name]
### Description
[What it does and when to use]

### Variants
- **Primary**: [Usage]
- **Secondary**: [Usage]
- **Tertiary/Ghost**: [Usage]

### Sizes
- **Small**: [Dimensions, font size]
- **Medium**: [Dimensions, font size] (default)
- **Large**: [Dimensions, font size]

### States
| State | Background | Text | Border | Other |
|-------|------------|------|--------|-------|
| Default | | | | |
| Hover | | | | |
| Focus | | | | Focus ring |
| Active | | | | |
| Disabled | | | | opacity: 0.5 |

### Anatomy
```
┌─────────────────────────┐
│  [icon]  Label Text  │
└─────────────────────────┘
         │
    padding: 12px 20px
```

### Specifications
| Property | Value |
|----------|-------|
| Height | 40px (medium) |
| Padding | 12px 20px |
| Border radius | 8px |
| Font size | 14px |
| Font weight | 500 |
| Transition | 150ms ease |

### Accessibility
- [ ] Minimum 44px touch target
- [ ] 4.5:1 contrast ratio
- [ ] Visible focus state
- [ ] Disabled state announced
```

### Step 4: Design Core Components

**Essential components to define:**

#### Buttons
```markdown
### Buttons

#### Primary Button
| State | Background | Text | Border |
|-------|------------|------|--------|
| Default | Violet-500 | White | None |
| Hover | Violet-400 | White | None |
| Focus | Violet-500 | White | + focus ring |
| Active | Violet-600 | White | None |
| Disabled | Violet-200 | White | None |

#### Secondary Button
| State | Background | Text | Border |
|-------|------------|------|--------|
| Default | White | Violet-600 | Violet-300 |
| Hover | Violet-50 | Violet-600 | Violet-400 |
| Focus | White | Violet-600 | + focus ring |
| Active | Violet-100 | Violet-700 | Violet-500 |
| Disabled | Gray-50 | Gray-400 | Gray-200 |

#### Ghost Button
| State | Background | Text | Border |
|-------|------------|------|--------|
| Default | Transparent | Violet-600 | None |
| Hover | Violet-50 | Violet-600 | None |
| Focus | Transparent | Violet-600 | + focus ring |
| Active | Violet-100 | Violet-700 | None |
| Disabled | Transparent | Gray-400 | None |

#### Destructive Button
| State | Background | Text | Border |
|-------|------------|------|--------|
| Default | Error-500 | White | None |
| Hover | Error-400 | White | None |

#### Button Sizes
| Size | Height | Padding | Font | Icon |
|------|--------|---------|------|------|
| sm | 32px | 8px 16px | 13px | 16px |
| md | 40px | 10px 20px | 14px | 18px |
| lg | 48px | 12px 24px | 16px | 20px |
```

#### Form Inputs
```markdown
### Text Input

#### States
| State | Background | Border | Label | Icon |
|-------|------------|--------|-------|------|
| Default | White | Gray-300 | Gray-600 | Gray-400 |
| Hover | White | Gray-400 | Gray-600 | Gray-500 |
| Focus | White | Violet-500 | Violet-600 | Violet-500 |
| Filled | White | Gray-300 | Gray-600 | Gray-600 |
| Error | White | Error-500 | Error-600 | Error-500 |
| Disabled | Gray-50 | Gray-200 | Gray-400 | Gray-300 |

#### Specifications
| Property | Value |
|----------|-------|
| Height | 44px |
| Padding | 12px 16px |
| Border width | 1px |
| Border radius | 8px |
| Font size | 16px (prevents iOS zoom) |
| Placeholder color | Gray-400 |
| Focus ring | 2px Violet-200 offset 2px |

#### Anatomy
```
 Label Text
┌──────────────────────────────┐
│ [icon] Placeholder text... │
└──────────────────────────────┘
 Helper text or error message
```
```

---

## Example Input/Output
### Example Input

```markdown
**Project**: TaskFlow dashboard
**Design tokens**: Violet primary, Slate neutrals, 8px spacing base
**Key components needed**: Buttons, inputs, cards, navigation
```

### Example Output

```markdown

## Component Library: TaskFlow
### Design Tokens Reference
- Primary: Violet-500 (#8B5CF6)
- Border radius: 8px (default), 12px (cards)
- Spacing unit: 8px
- Shadow: 0 1px 3px rgba(0,0,0,0.1)

---

## Input Field
### Text Input

**Visual**
```
 Email Address
┌────────────────────────────┐
│ ✉️  you@example.com       │
└────────────────────────────┘
 We'll never share your email.
```

**States**
| State | Border | Shadow | Icon |
|-------|--------|--------|------|
| Default | Gray-300 | none | Gray-400 |
| Hover | Gray-400 | none | Gray-500 |
| Focus | Violet-500 | ring 2px Violet-100 | Violet-500 |
| Error | Error-500 | ring 2px Error-100 | Error-500 |
| Disabled | Gray-200 | none | Gray-300 |

**Specifications**
```css
.input {
  width: 100%;
  height: 44px;
  padding: 0 12px 0 40px; /* left padding for icon */
  border: 1px solid #CBD5E1;
  border-radius: 8px;
  font-size: 16px;
  color: #334155;
  background: white;
  transition: all 150ms ease;
}
.input:focus {
  border-color: #8B5CF6;
  box-shadow: 0 0 0 3px #EDE9FE;
  outline: none;
}
.input.error {
  border-color: #EF4444;
  box-shadow: 0 0 0 3px #FEE2E2;
}
```

---

## Using the Reference Files

### When to Read Each Reference

**`./references/component-library-patterns.md`** — Read when you need to apply Atomic Design methodology (atoms, molecules, organisms), design component APIs with consistent props and naming, implement composition patterns (slots, compound components, headless), manage interactive states and their combinations, build responsive/adaptive components, or integrate accessibility and design tokens.

**`./references/component-documentation.md`** — Read when you need to write component documentation, create specification sheets for developer handoff, structure Storybook stories, define prop tables and code examples, establish do's/don'ts guidelines, or set up documentation governance and quality metrics.

**`./references/buttons.md`** — Read when you need detailed guidance on buttons aspects of this skill.

**`./references/navigation.md`** — Read when you need detailed guidance on navigation aspects of this skill.

**`./references/prompts-library.md`** — Read when you need detailed guidance on prompts library aspects of this skill.
