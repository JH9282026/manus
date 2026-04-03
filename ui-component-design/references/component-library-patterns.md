# Component Library Patterns - UI Component Design

## Introduction

This reference provides comprehensive guidance on designing scalable component libraries using proven architectural patterns. Use this when building a design system from scratch, establishing component taxonomy, implementing atomic design principles, or creating reusable component patterns that scale across products.

---

## Atomic Design Methodology

### Overview

Atomic Design, created by Brad Frost, organizes components into five hierarchical levels based on complexity and composition. This methodology provides a shared language for teams and a clear structure for component libraries.

### The Five Levels

**Level 1: Atoms**
The smallest, indivisible UI elements. They cannot be broken down further without losing meaning.

| Atom | Examples | Properties |
|------|----------|------------|
| Button | Primary, secondary, ghost, icon-only | Size, variant, state, disabled |
| Input | Text, email, password, number | Type, placeholder, state, size |
| Label | Form label, caption, overline | Size, weight, required indicator |
| Icon | System icons, status icons | Size, color, accessibility label |
| Badge | Status badge, count badge | Color, size, content |
| Avatar | User avatar, placeholder | Size, shape, fallback |
| Checkbox | Checked, unchecked, indeterminate | State, disabled, label position |
| Toggle | On/off switch | State, size, label |
| Divider | Horizontal, vertical separator | Orientation, spacing |
| Spinner | Loading indicator | Size, color |

**Level 2: Molecules**
Combinations of atoms that form functional units.

| Molecule | Composed Of | Purpose |
|----------|------------|----------|
| Form Field | Label + Input + Helper Text + Error | Complete input with context |
| Search Bar | Input + Icon Button + Clear button | Search interface |
| Breadcrumb Item | Link + Separator Icon | Navigation waypoint |
| Menu Item | Icon + Label + Badge/Shortcut | Actionable list entry |
| Toast | Icon + Message + Close Button | Transient notification |
| Stat Card | Label + Value + Trend Icon | Single metric display |
| Tab | Icon + Label + Active indicator | Navigation switch |
| Pagination Item | Button (number/arrow) | Page selector |

**Level 3: Organisms**
Complex components that combine molecules into distinct UI sections.

| Organism | Composed Of | Purpose |
|----------|------------|----------|
| Navigation Bar | Logo + Nav Items + Search Bar + Avatar | Global navigation |
| Form Section | Multiple Form Fields + Section Title + Actions | Grouped input collection |
| Data Table | Header Row + Data Rows + Pagination + Filters | Structured data display |
| Card | Image + Title + Description + Actions + Badge | Content container |
| Modal | Overlay + Header + Body + Footer Actions | Focused interaction |
| Sidebar | Nav Groups + User Info + Collapse Toggle | Application navigation |
| Command Palette | Search Input + Results List + Keyboard Hints | Quick action interface |

**Level 4: Templates**
Page-level layouts that arrange organisms into content structures.

- Dashboard Template: Sidebar + Header + Grid of Cards + Data Table
- Settings Template: Sidebar Nav + Form Sections + Save Bar
- List/Detail Template: List Panel + Detail Panel + Action Bar

**Level 5: Pages**
Templates populated with real content. Pages are the final test of the component system — they reveal whether the abstractions hold up with actual data.

---

## Component API Design Patterns

### Props/Variants Architecture

Well-designed component APIs follow predictable patterns:

**Essential Props for Every Component**:

| Prop | Type | Purpose | Example |
|------|------|---------|----------|
| `variant` | enum | Visual style | "primary", "secondary", "ghost" |
| `size` | enum | Dimensional scaling | "sm", "md", "lg" |
| `disabled` | boolean | Interaction blocking | true/false |
| `className` | string | Custom styling escape hatch | "my-custom-class" |
| `children` | node | Content slot | Text, icons, other components |
| `as` | element | Polymorphic rendering | "button", "a", "div" |

**Naming Conventions**:

```
Variant names:   primary, secondary, tertiary, ghost, destructive
Size names:      xs, sm, md (default), lg, xl
State names:     default, hover, focus, active, disabled, loading, error
Slot names:      prefix, suffix, startIcon, endIcon
Event names:     onClick, onChange, onFocus, onBlur, onClose
```

### Composition Patterns

**Pattern 1: Slot-Based Composition**
Components expose named slots for flexible content placement.

```jsx
<Card>
  <Card.Header>Title</Card.Header>
  <Card.Body>Content goes here</Card.Body>
  <Card.Footer>
    <Button>Action</Button>
  </Card.Footer>
</Card>
```

**Pattern 2: Compound Components**
Related components share implicit state through context.

```jsx
<Tabs defaultValue="tab1">
  <Tabs.List>
    <Tabs.Trigger value="tab1">General</Tabs.Trigger>
    <Tabs.Trigger value="tab2">Security</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="tab1">General settings...</Tabs.Content>
  <Tabs.Content value="tab2">Security settings...</Tabs.Content>
</Tabs>
```

**Pattern 3: Render Props / Headless**
Provide behavior without dictating appearance.

```jsx
<Combobox options={options}>
  {({ isOpen, selectedItem, getInputProps }) => (
    <div>
      <input {...getInputProps()} />
      {isOpen && <OptionsList />}
    </div>
  )}
</Combobox>
```

---

## State Management Patterns

### Interactive States Matrix

Every interactive component should define all possible states:

| State | Trigger | Visual Change | Behavioral Change |
|-------|---------|---------------|-------------------|
| Default | Initial render | Base appearance | Fully interactive |
| Hover | Mouse enters | Background/color shift | Cursor changes |
| Focus | Tab or click | Focus ring visible | Keyboard accessible |
| Active | Mouse down / keypress | Pressed appearance | Action pending |
| Disabled | disabled prop | Reduced opacity (0.5) | No interaction, no focus |
| Loading | Async operation | Spinner replaces content | Interaction blocked |
| Error | Validation failure | Error border/color | Error message shown |
| Success | Operation complete | Success styling | Temporary, auto-clears |
| Selected | User selection | Highlighted state | Toggle behavior |
| Expanded | Disclosure toggle | Content revealed | Aria-expanded true |

### State Combinations

Some states can coexist; others are exclusive:

```
Valid combinations:
  ✓ Hover + Focus (mouse over focused element)
  ✓ Focus + Error (focused input with validation error)
  ✓ Selected + Hover (hovering over selected item)
  ✓ Loading + Disabled (loading automatically disables)

Mutually exclusive:
  ✗ Disabled + Hover (disabled elements have no hover)
  ✗ Disabled + Focus (disabled elements are not focusable)
  ✗ Loading + Error (can't be loading and errored simultaneously)
```

---

## Responsive Component Patterns

### Adaptive Components

Components that change structure (not just size) based on available space:

| Component | Desktop | Tablet | Mobile |
|-----------|---------|--------|--------|
| Navigation | Horizontal nav bar | Horizontal with overflow | Hamburger menu |
| Data Table | Full columns visible | Horizontal scroll | Card list view |
| Form Layout | Multi-column grid | Two-column | Single column stack |
| Modal | Centered overlay | Centered overlay | Full-screen sheet |
| Tabs | Horizontal tab bar | Scrollable tabs | Dropdown select |
| Pagination | Full number range | Simplified (prev/next + current) | Prev/Next only |

### Container-Aware Components

```css
.card {
  container-type: inline-size;
}

/* Stack layout when container is narrow */
@container (max-width: 300px) {
  .card-content {
    flex-direction: column;
  }
  .card-image {
    width: 100%;
    aspect-ratio: 16/9;
  }
}

/* Horizontal layout when container is wide */
@container (min-width: 301px) {
  .card-content {
    flex-direction: row;
  }
  .card-image {
    width: 200px;
  }
}
```

---

## Accessibility Patterns

### ARIA Roles and Patterns

| Component | ARIA Role | Key Attributes | Keyboard |
|-----------|-----------|---------------|----------|
| Button | button | aria-pressed, aria-expanded | Enter, Space |
| Modal | dialog | aria-modal, aria-labelledby | Escape to close, focus trap |
| Tabs | tablist + tab + tabpanel | aria-selected, aria-controls | Arrow keys, Home/End |
| Dropdown | listbox + option | aria-expanded, aria-activedescendant | Arrow keys, Enter, Escape |
| Accordion | region | aria-expanded, aria-controls | Enter/Space, Arrow keys |
| Toast | alert or status | role="alert", aria-live="polite" | Auto-dismiss, dismissible |
| Breadcrumb | navigation | aria-label="Breadcrumb", aria-current | Standard link navigation |
| Toggle | switch | aria-checked | Space to toggle |

### Focus Management Rules

1. **Focus order**: Tab order follows visual reading order (top-left to bottom-right in LTR)
2. **Focus trapping**: Modals, drawers, and popovers trap focus within their boundary
3. **Focus restoration**: When a modal closes, focus returns to the trigger element
4. **Skip links**: Provide "Skip to main content" for keyboard users
5. **Focus indicators**: Visible focus ring on every focusable element (3:1 contrast minimum)

---

## Design Token Integration

### Component Token Structure

Each component maps to design tokens at multiple levels:

```json
{
  "component": {
    "button": {
      "primary": {
        "bg": { "value": "{color.primary.600}" },
        "bg-hover": { "value": "{color.primary.500}" },
        "bg-active": { "value": "{color.primary.700}" },
        "text": { "value": "{color.white}" },
        "border-radius": { "value": "{radius.md}" },
        "padding-x": { "value": "{space.4}" },
        "padding-y": { "value": "{space.2}" },
        "font-size": { "value": "{fontSize.sm}" },
        "font-weight": { "value": "{fontWeight.medium}" }
      }
    }
  }
}
```

### Theming Through Token Swapping

Component libraries support theming by swapping token sets:

- **Brand A tokens**: Blue primary, rounded corners, Inter font
- **Brand B tokens**: Green primary, sharp corners, DM Sans font
- **Dark mode tokens**: Inverted backgrounds, adjusted colors

Same components, different visual identity — achieved by changing token values, not component code.

---

## Reference Component Libraries

| Library | Architecture | Key Innovation |
|---------|-------------|----------------|
| **Radix UI** | Headless primitives | Unstyled, accessible by default |
| **shadcn/ui** | Copy-paste components | Full ownership, Tailwind + Radix |
| **Chakra UI** | Styled system | Style props, design tokens built-in |
| **Ant Design** | Enterprise components | Comprehensive, opinionated |
| **Material UI** | Google Material Design | Theming engine, wide adoption |
| **Headless UI** | Headless + Tailwind | Minimal, behavior-only |
| **Mantine** | Full-featured hooks + components | Built-in hooks library, TypeScript |

---

## Key Takeaways

1. Atomic Design provides a shared vocabulary for component complexity levels
2. Design component APIs with consistent prop naming (variant, size, disabled)
3. Use compound/slot patterns for flexible composition without prop explosion
4. Define all interactive states upfront — including combinations and exclusions
5. Build adaptive components that change structure, not just scale, across breakpoints
6. Accessibility is not optional — bake ARIA roles and keyboard support into every component
7. Design tokens enable theming and brand customization without touching component code
