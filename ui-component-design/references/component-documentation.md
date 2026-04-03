# Component Documentation - UI Component Design

## Introduction

This reference provides comprehensive guidance on documenting UI components for design systems. Use this when writing component documentation, creating specification sheets for developer handoff, building Storybook or documentation sites, or establishing documentation standards for a component library.

---

## Why Component Documentation Matters

### The Documentation Gap

Design systems fail not because of poor components, but because of poor documentation. Without clear docs:

- Developers implement components inconsistently
- Designers use components for unintended purposes
- New team members take weeks to become productive
- The system fragments as teams create local workarounds

### Documentation Audiences

| Audience | What They Need | Format Preference |
|----------|---------------|-------------------|
| **Designers** | Usage guidelines, variants, do/don'ts | Visual examples, Figma links |
| **Developers** | API reference, code examples, props | Code snippets, interactive demos |
| **Product Managers** | When to use, capabilities, limitations | Plain language, comparison tables |
| **QA Engineers** | States, edge cases, accessibility reqs | Checklists, state matrices |
| **New Team Members** | Getting started, patterns, conventions | Tutorials, quick-start guides |

---

## Component Documentation Template

### Section 1: Overview

Every component doc starts with a clear summary:

```markdown
## Button

Buttons trigger actions or navigate to new pages. They communicate 
what happens when the user interacts with them.

### When to Use
- Submitting forms
- Triggering actions (save, delete, create)
- Navigating to a new page when the action is the primary purpose

### When NOT to Use
- Navigating to a new page (use Link instead)
- Toggling between states (use Toggle or Switch)
- Selecting from options (use Radio, Checkbox, or Select)
```

### Section 2: Variants

Document every visual variant with its intended use:

| Variant | Appearance | Usage | Example Context |
|---------|-----------|-------|-----------------|
| **Primary** | Filled background, high contrast | Main action on the page | "Save changes", "Submit" |
| **Secondary** | Outlined, medium contrast | Supporting actions | "Cancel", "Back" |
| **Tertiary/Ghost** | Text-only, minimal styling | Low-priority actions | "Learn more", "Skip" |
| **Destructive** | Red/danger filled | Irreversible or risky actions | "Delete account", "Remove" |
| **Icon-only** | Icon without text label | Space-constrained actions | Close, search, menu toggle |

**Variant Hierarchy Rule**: A view should have at most one Primary button. Multiple actions should use decreasing emphasis: Primary → Secondary → Tertiary.

### Section 3: Sizes

| Size | Height | Padding | Font Size | Icon Size | Use Case |
|------|--------|---------|-----------|-----------|----------|
| **xs** | 28px | 6px 12px | 12px | 14px | Dense tables, inline actions |
| **sm** | 32px | 8px 16px | 13px | 16px | Secondary actions, toolbars |
| **md** | 40px | 10px 20px | 14px | 18px | Default for most contexts |
| **lg** | 48px | 12px 24px | 16px | 20px | Forms, standalone CTAs |
| **xl** | 56px | 14px 32px | 18px | 22px | Hero sections, marketing pages |

### Section 4: States

Document every interactive state with visual specification:

```markdown
### Interactive States

| State | Background | Text Color | Border | Shadow | Cursor |
|-------|-----------|-----------|--------|--------|--------|
| Default | primary-600 | white | none | none | pointer |
| Hover | primary-500 | white | none | sm | pointer |
| Focus | primary-600 | white | none | focus-ring | default |
| Active | primary-700 | white | none | none | pointer |
| Disabled | primary-200 | white/70% | none | none | not-allowed |
| Loading | primary-600 | hidden | none | none | wait |

### Focus Ring Specification
- Style: 2px solid primary-300
- Offset: 2px from component edge
- Border radius: component radius + 2px
- Visible on keyboard focus only (not mouse click)
- Uses :focus-visible, not :focus
```

### Section 5: Props / API Reference

The technical interface documentation:

```markdown
### Props

| Prop | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| `variant` | `'primary' \| 'secondary' \| 'ghost' \| 'destructive'` | `'primary'` | No | Visual style variant |
| `size` | `'xs' \| 'sm' \| 'md' \| 'lg' \| 'xl'` | `'md'` | No | Component size |
| `disabled` | `boolean` | `false` | No | Disables interaction |
| `loading` | `boolean` | `false` | No | Shows loading spinner |
| `fullWidth` | `boolean` | `false` | No | Stretches to container width |
| `leftIcon` | `ReactNode` | `undefined` | No | Icon before label |
| `rightIcon` | `ReactNode` | `undefined` | No | Icon after label |
| `as` | `ElementType` | `'button'` | No | Render as different element |
| `onClick` | `() => void` | `undefined` | No | Click handler |
| `children` | `ReactNode` | — | Yes | Button label content |
```

### Section 6: Code Examples

Provide copy-paste-ready examples for common use cases:

```markdown
### Basic Usage
```jsx
<Button variant="primary" size="md">
  Save Changes
</Button>
```

### With Icons
```jsx
<Button variant="secondary" leftIcon={<PlusIcon />}>
  Add Item
</Button>
```

### Loading State
```jsx
<Button variant="primary" loading={isSubmitting}>
  {isSubmitting ? 'Saving...' : 'Save'}
</Button>
```

### Button Group
```jsx
<ButtonGroup>
  <Button variant="primary">Save</Button>
  <Button variant="secondary">Cancel</Button>
</ButtonGroup>
```

### As Link
```jsx
<Button as="a" href="/dashboard" variant="ghost">
  Go to Dashboard
</Button>
```
```

### Section 7: Accessibility Specifications

```markdown
### Accessibility

#### ARIA Requirements
- Buttons use native `<button>` element (no `<div>` with role="button")
- Toggle buttons include `aria-pressed` state
- Loading buttons include `aria-busy="true"` and `aria-live="polite"`
- Icon-only buttons require `aria-label` describing the action
- Disabled buttons use native `disabled` attribute (not `aria-disabled`)

#### Keyboard Navigation
| Key | Action |
|-----|--------|
| `Tab` | Focus the button |
| `Enter` | Activate the button |
| `Space` | Activate the button |

#### Screen Reader Announcements
- Default: Reads button label text
- Loading: Announces "Loading" via aria-busy
- Disabled: Announces "dimmed" or "unavailable"
- Icon-only: Reads aria-label value

#### Minimum Requirements
- [ ] Touch target ≥ 44×44px on mobile
- [ ] Color contrast ≥ 4.5:1 for button text
- [ ] Focus indicator ≥ 3:1 contrast against adjacent colors
- [ ] Does not rely on color alone for state changes
```

### Section 8: Do's and Don'ts

Visual guidelines that prevent misuse:

```markdown
### Do
✓ Use sentence case for button labels ("Save changes", not "SAVE CHANGES")
✓ Start labels with a verb ("Create", "Delete", "Download")
✓ Keep labels concise (1-3 words ideally)
✓ Use Primary for the single most important action on the page
✓ Pair Destructive buttons with a confirmation dialog
✓ Include aria-label on icon-only buttons

### Don't
✗ Don't use more than one Primary button per view
✗ Don't use generic labels ("Click here", "Submit")
✗ Don't disable buttons without explaining why
✗ Don't use buttons for navigation (use Links)
✗ Don't make buttons look like links or vice versa
✗ Don't nest interactive elements inside buttons
```

---

## Documentation Tools and Platforms

### Storybook

The industry standard for component documentation:

**Key features for documentation**:
- **Stories**: Interactive examples for each variant and state
- **Controls**: Live prop editing in the browser
- **Docs page**: Auto-generated from JSDoc comments + MDX
- **Accessibility addon**: Built-in a11y testing per story
- **Design addon**: Embed Figma frames alongside code

**Story structure best practice**:
```
Button/
├── Overview (MDX documentation page)
├── Playground (interactive controls)
├── Variants/
│   ├── Primary
│   ├── Secondary
│   ├── Ghost
│   └── Destructive
├── Sizes/
│   ├── Small
│   ├── Medium
│   └── Large
├── States/
│   ├── Disabled
│   ├── Loading
│   └── With Icons
└── Accessibility
```

---

## Specification Sheets for Handoff

### What a Spec Sheet Includes

A component spec sheet bridges design and development:

```markdown
## Button Component Spec

### Dimensions
- Height: 40px (md default)
- Min-width: 80px
- Max-width: none (fits content)
- Border-radius: 8px
- Icon size: 18px
- Icon-to-label gap: 8px

### Spacing
- Horizontal padding: 20px
- Vertical padding: 10px
- Button group gap: 8px
- Margin from adjacent elements: 16px minimum

### Typography
- Font family: Inter
- Font size: 14px
- Font weight: 500 (Medium)
- Line height: 20px
- Letter spacing: 0.01em
- Text transform: none

### Colors (Light Theme)
- Primary bg: #2563EB
- Primary hover bg: #3B82F6
- Primary active bg: #1D4ED8
- Primary text: #FFFFFF
- Focus ring: #93C5FD, 2px, offset 2px

### Animation
- Transition property: background-color, box-shadow, transform
- Duration: 150ms
- Easing: ease-in-out
- Active scale: transform: scale(0.98)
```

### Design Token Mapping

Link every spec value to a design token:

| Property | Value | Token |
|----------|-------|-------|
| Background | #2563EB | `color.primary.600` |
| Text color | #FFFFFF | `color.white` |
| Font size | 14px | `fontSize.sm` |
| Font weight | 500 | `fontWeight.medium` |
| Border radius | 8px | `radius.md` |
| Padding-x | 20px | `space.5` |
| Padding-y | 10px | `space.2.5` |
| Transition | 150ms | `duration.fast` |

---

## Documentation Quality Checklist

Use this checklist to evaluate documentation completeness:

```
□ Overview: Clear description of what the component does
□ When to use / when not to use: Decision guidance
□ Variants: All variants documented with intended usage
□ Sizes: All sizes with dimensions and use cases
□ States: Complete state matrix with visual specs
□ Props/API: Every prop documented with type, default, description
□ Code examples: Copy-paste snippets for common patterns
□ Accessibility: ARIA requirements, keyboard nav, screen reader behavior
□ Do's and Don'ts: Clear usage guidelines with visual examples
□ Responsive behavior: How the component adapts across breakpoints
□ Related components: Links to similar or complementary components
□ Design tokens: Every value mapped to a token name
□ Figma link: Reference to the source design file
□ Changelog: Version history of significant changes
```

---

## Maintaining Documentation

### Documentation as Code

Treat docs like code — version controlled, reviewed, and tested:

- Store documentation alongside component code (co-location)
- Include doc updates in component PR reviews
- Auto-generate prop tables from TypeScript types
- Run visual regression tests on documentation examples
- Set up CI checks that fail if a component lacks documentation

---

## Key Takeaways

1. Documentation is as important as the components themselves — without it, adoption fails
2. Write for multiple audiences: designers, developers, PMs, and QA
3. Every component needs: overview, variants, states, props, code examples, and accessibility specs
4. Use Storybook for interactive documentation; supplement with written guidelines
5. Spec sheets bridge design and development with precise measurements and token mappings
6. Treat documentation as code — co-locate, version, review, and test it
7. Measure documentation effectiveness through adoption rates and support ticket trends
