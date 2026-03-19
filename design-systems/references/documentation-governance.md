# Documentation and Governance

Comprehensive guide to creating design system documentation and establishing effective governance models.

---

## Documentation Fundamentals

### Why Documentation Matters

**Without documentation:**
- Components misused or inconsistently applied
- Designers and developers make conflicting decisions
- Onboarding new team members takes weeks
- Design system adoption stalls

**With documentation:**
- Clear usage guidelines reduce errors
- Faster onboarding (days instead of weeks)
- Self-service reduces support burden on DS team
- Higher adoption and consistency

### Documentation Audiences

**1. Designers**
- Need: Visual examples, usage guidelines, Figma component library
- Format: Visual documentation with do's/don'ts, Figma files

**2. Developers**
- Need: Code examples, API reference, integration guides
- Format: Code snippets, Storybook, technical documentation

**3. Product Managers**
- Need: Component capabilities, when to use, business value
- Format: High-level overviews, use case examples

**4. Content Designers**
- Need: Voice and tone guidelines, microcopy standards
- Format: Writing guidelines, content patterns

**5. Accessibility Specialists**
- Need: WCAG compliance, keyboard navigation, screen reader behavior
- Format: Accessibility specifications, testing guidelines

---

## Documentation Structure

### Essential Documentation Sections

**1. Getting Started**
- What is this design system?
- Who is it for?
- How to install/access
- Quick start guide

**2. Design Principles**
- Core principles guiding the system
- Design philosophy
- Brand values

**3. Design Tokens**
- Color palette
- Typography scale
- Spacing system
- Other tokens (shadows, borders, etc.)

**4. Components**
- Component library (organized by category)
- Usage guidelines for each component
- Code examples
- Accessibility notes

**5. Patterns**
- Common UI patterns (forms, navigation, data display)
- Layout patterns
- Interaction patterns

**6. Content Guidelines**
- Voice and tone
- Writing style
- Microcopy standards

**7. Accessibility**
- Accessibility standards (WCAG level)
- Testing guidelines
- Keyboard navigation

**8. Resources**
- Figma libraries
- Code repositories
- Slack channels
- Office hours

**9. Contribution Guidelines**
- How to propose new components
- How to report issues
- How to contribute code/designs

**10. Changelog**
- Release notes
- Migration guides
- Deprecation notices

---

## Component Documentation Template

For each component, document:

### 1. Overview

**What is this component?**

Brief description (1-2 sentences).

**When to use:**
- Use case 1
- Use case 2
- Use case 3

**When not to use:**
- Anti-pattern 1 (use X instead)
- Anti-pattern 2 (use Y instead)

### 2. Anatomy

Visual diagram labeling component parts:

```
┌─────────────────────────────┐
│ [Icon] Button Text [Badge]  │  ← Button
└─────────────────────────────┘
   ↑        ↑          ↑
  Icon    Label     Badge (optional)
```

### 3. Variants

Visual examples of all variants:

- Primary button
- Secondary button
- Tertiary button
- Destructive button
- Ghost button

**When to use each variant:**
- **Primary:** Main action on page ("Save," "Submit")
- **Secondary:** Secondary actions ("Cancel," "Back")
- **Tertiary:** Low-emphasis actions ("Learn More")
- **Destructive:** Dangerous actions ("Delete," "Remove")
- **Ghost:** Minimal actions in dense UIs

### 4. States

Visual examples of all states:

- Default
- Hover
- Active (pressed)
- Focus (keyboard)
- Disabled
- Loading

### 5. Sizes

Visual examples of all sizes:

- Small (32px height)
- Medium (40px height, default)
- Large (48px height)

### 6. Props/API

Table of all props:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `'primary' \| 'secondary' \| 'tertiary' \| 'destructive' \| 'ghost'` | `'primary'` | Visual style |
| `size` | `'small' \| 'medium' \| 'large'` | `'medium'` | Size |
| `disabled` | `boolean` | `false` | Disabled state |
| `loading` | `boolean` | `false` | Loading state |
| `icon` | `ReactNode` | - | Icon element |
| `onClick` | `() => void` | - | Click handler |

### 7. Usage Examples

Code examples for common use cases:

```jsx
// Primary button
<Button variant="primary">Save Changes</Button>

// Secondary button with icon
<Button variant="secondary" icon={<ArrowLeft />}>
  Back
</Button>

// Loading state
<Button loading>Saving...</Button>

// Destructive action
<Button variant="destructive">Delete Account</Button>
```

### 8. Accessibility

**Keyboard navigation:**
- Tab to focus
- Enter or Space to activate

**Screen reader:**
- Button text announced
- Loading state announced ("Busy")
- Disabled state announced ("Dimmed, unavailable")

**ARIA attributes:**
- `aria-busy="true"` when loading
- `aria-disabled="true"` when disabled (if using div instead of button)

**Color contrast:**
- Text meets WCAG AA (4.5:1 for normal text)
- Focus indicator meets WCAG AA (3:1 for UI components)

### 9. Best Practices

**Do:**
- ✅ Use primary button for main action
- ✅ Use descriptive button text ("Save Changes" not "Submit")
- ✅ Provide loading state for async actions
- ✅ Disable button during loading to prevent double-submission

**Don't:**
- ❌ Use multiple primary buttons on same page
- ❌ Use button for navigation (use link instead)
- ❌ Disable button without explanation (show error message)
- ❌ Use vague button text ("Click here," "OK")

### 10. Related Components

- **Link** — For navigation
- **Icon Button** — Button with only icon, no text
- **Button Group** — Multiple related buttons

---

## Documentation Tools

### Tool Comparison

| Tool | Type | Pros | Cons | Best For |
|------|------|------|------|----------|
| **Storybook** | Code-based | Interactive, integrates with code, free | Developer-focused, less visual | Developer documentation |
| **Zeroheight** | Visual platform | Beautiful, designer-friendly, Figma sync | Expensive, less code-focused | Designer documentation |
| **Supernova** | Design-to-code | Syncs design and code, comprehensive | Expensive, complex setup | Enterprise teams |
| **Notion** | General docs | Flexible, collaborative, affordable | Not specialized for design systems | Small teams, early stage |
| **Confluence** | General docs | Enterprise features, integrations | Not specialized, can be cluttered | Enterprise teams already using Atlassian |
| **Custom site** | Static site | Full control, free (hosting only) | Requires development, maintenance | Teams with dev resources |

### Storybook (Recommended for Developers)

**Installation:**
```bash
npx storybook init
```

**Component story example:**

```javascript
// Button.stories.jsx
import { Button } from './Button';

export default {
  title: 'Components/Button',
  component: Button,
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'tertiary', 'destructive', 'ghost'],
    },
    size: {
      control: 'select',
      options: ['small', 'medium', 'large'],
    },
  },
};

const Template = (args) => <Button {...args} />;

export const Primary = Template.bind({});
Primary.args = {
  variant: 'primary',
  children: 'Primary Button',
};

export const Secondary = Template.bind({});
Secondary.args = {
  variant: 'secondary',
  children: 'Secondary Button',
};

export const Loading = Template.bind({});
Loading.args = {
  loading: true,
  children: 'Loading...',
};
```

**MDX documentation:**

```mdx
<!-- Button.stories.mdx -->
import { Meta, Story, Canvas, ArgsTable } from '@storybook/addon-docs';
import { Button } from './Button';

<Meta title="Components/Button" component={Button} />

# Button

Buttons trigger actions or navigate to new pages.

## When to use

- Use buttons for actions ("Save," "Delete")
- Use links for navigation ("Learn more," "View details")

## Variants

<Canvas>
  <Story name="Primary">
    <Button variant="primary">Primary</Button>
  </Story>
  <Story name="Secondary">
    <Button variant="secondary">Secondary</Button>
  </Story>
</Canvas>

## Props

<ArgsTable of={Button} />
```

**Benefits:**
- Interactive component playground
- Auto-generated props table
- Visual regression testing (with Chromatic)
- Accessibility testing (with a11y addon)

### Zeroheight (Recommended for Designers)

**Features:**
- Figma sync (components, styles, variables)
- Beautiful visual documentation
- Version control
- Custom branding

**Structure:**

```
Design System
├── Getting Started
│   ├── Introduction
│   ├── Installation
│   └── Quick Start
├── Foundations
│   ├── Colors
│   ├── Typography
│   ├── Spacing
│   └── Iconography
├── Components
│   ├── Button
│   ├── Input
│   ├── Card
│   └── ...
├── Patterns
│   ├── Forms
│   ├── Navigation
│   └── Data Display
└── Resources
    ├── Figma Libraries
    ├── Code Repository
    └── Support
```

**Best practices:**
- Sync Figma components automatically
- Add usage guidelines and examples
- Include do's and don'ts with visuals
- Link to Storybook for code examples

---

## Governance Models

### Governance Model Comparison

| Model | Structure | Decision Making | Contribution | Best For |
|-------|-----------|-----------------|--------------|----------|
| **Centralized (top-down)** | DS team controls all | DS team decides | DS team only | Small teams, strict brand |
| **Centralized (service)** | DS team serves feature teams | DS team decides with input | Feature teams request, DS builds | Medium teams, diverse needs |
| **Federated** | Multiple teams manage | Consensus across teams | All teams contribute | Small orgs, early stage |
| **Hybrid** | Central team + contributions | DS team approves contributions | Feature teams can contribute | Growing teams |
| **Distributed** | Specialized roles | Collaborative, clear boundaries | All teams contribute within guardrails | Large teams, enterprise |

### Distributed Governance Model (Recommended)

**Three pillars:**

**1. Design System Team**
- **Responsibility:** Core components, primitives, tokens, documentation
- **Goal:** Cover 80% of use cases
- **Size:** 2-5 people (designers + developers)
- **Focus:** Quality, consistency, accessibility, performance

**2. Framework Team**
- **Responsibility:** Implementation across products, technical support
- **Goal:** Ensure design standards met in production
- **Size:** 1-3 people (senior developers)
- **Focus:** Code quality, integration, developer experience

**3. Feature Teams**
- **Responsibility:** Product features using DS components
- **Goal:** Build features quickly
- **Freedom:** Extend system with local libraries when needed
- **Contribution:** Propose components for core system

**Benefits:**
- No bottlenecks (feature teams not blocked)
- High collaboration
- Innovation within guardrails
- Core system stays focused

### Contribution Process

**For new components:**

**Step 1: Proposal**

Feature team submits proposal:

```markdown
## Component Proposal: Data Table

**Proposed by:** Product Team A
**Date:** 2026-03-15

**Use case:**
We need to display large datasets (100+ rows) with sorting, filtering, and pagination.

**Frequency:**
- Used in 5 product areas
- ~20 instances across products

**Alternatives considered:**
- Simple table (doesn't support sorting/filtering)
- Card grid (not suitable for large datasets)

**Proposed API:**
<DataTable
  data={data}
  columns={columns}
  sortable
  filterable
  pagination
/>

**Mockups:**
[Figma link]
```

**Step 2: Review**

DS team evaluates:

- ✅ **Generalizability:** Used by multiple teams? (Yes, 5 product areas)
- ✅ **Frequency:** Common enough for core system? (Yes, 20 instances)
- ✅ **Alignment:** Fits system principles? (Yes)
- ⚠️ **Complexity:** Can we build and maintain this? (High complexity, but valuable)

**Step 3: Decision**

**Options:**

**A. Accept into core system**
- DS team builds and maintains
- Available to all teams
- Documented and tested

**B. Defer to local library**
- Feature team builds in their product
- Shared across their product only
- Revisit for core system later if usage grows

**C. Reject**
- Use existing components
- Explain why it doesn't fit

**Decision:** Accept (high value, multiple teams need it)

**Step 4: Implementation**

DS team builds component:

1. Design in Figma
2. Build in code
3. Write documentation
4. Accessibility testing
5. Visual regression testing
6. Release and announce

**Timeline:** 2-4 weeks

### Versioning and Release Process

**Semantic versioning:**

- **MAJOR (1.0.0 → 2.0.0)** — Breaking changes
- **MINOR (1.0.0 → 1.1.0)** — New features (backward compatible)
- **PATCH (1.0.0 → 1.0.1)** — Bug fixes

**Release cadence:**

- **Patch releases:** As needed (bug fixes)
- **Minor releases:** Every 2-4 weeks (new features)
- **Major releases:** Every 6-12 months (breaking changes)

**Release process:**

1. **Code freeze** — No new features, only bug fixes
2. **Testing** — Visual regression, accessibility, manual testing
3. **Documentation** — Update docs, write changelog
4. **Release** — Publish to npm, update Figma libraries
5. **Announcement** — Slack, email, changelog page
6. **Support** — Monitor for issues, provide migration help

**Changelog example:**

```markdown
# Changelog

## [2.0.0] - 2026-03-15

### Breaking Changes

- **Button:** Removed `type` prop (use `variant` instead)
- **Card:** Renamed `image` prop to `media`

### Migration Guide

**Button:**
```jsx
// Before
<Button type="primary">Click</Button>

// After
<Button variant="primary">Click</Button>
```

**Card:**
```jsx
// Before
<Card image={<img src="..." />} />

// After
<Card media={<img src="..." />} />
```

### Added

- **DataTable:** New component for displaying large datasets
- **Button:** New `loading` prop for async actions

### Fixed

- **Input:** Fixed focus ring not visible in dark mode
- **Modal:** Fixed scroll lock not working on iOS

## [1.5.0] - 2026-03-01

### Added

- **Button:** New `icon` prop
- **Modal:** New `size` prop (small, medium, large)

### Fixed

- **Dropdown:** Fixed keyboard navigation
```

---

## Measuring Success

### Adoption Metrics

**Component usage:**
- % of product using design system components
- Number of component instances
- Coverage by component type

**Tracking:**
```javascript
// Add data attribute to components
<Button data-ds-component="button" data-ds-version="2.0.0">
  Click me
</Button>

// Analytics
const dsComponents = document.querySelectorAll('[data-ds-component]');
console.log(`${dsComponents.length} DS components on page`);
```

### Efficiency Metrics

**Time savings:**
- Time to build new feature (before vs. after DS)
- Time to onboard new designer/developer

**Consistency:**
- Design QA issues (before vs. after DS)
- Accessibility issues (before vs. after DS)

**Velocity:**
- Features shipped per quarter
- Design-to-development handoff time

### Satisfaction Metrics

**User surveys:**
- Designer satisfaction (1-5 scale)
- Developer satisfaction (1-5 scale)
- Ease of use (1-5 scale)

**Qualitative feedback:**
- What's working well?
- What needs improvement?
- What's missing?

---

## Governance Best Practices

### 1. Clear Ownership

- Designate DS team lead
- Define roles and responsibilities
- Establish decision-making authority

### 2. Regular Communication

- Weekly DS team sync
- Monthly all-hands (share updates with all teams)
- Office hours (open Q&A for users)
- Slack channel for support

### 3. Transparent Roadmap

- Public roadmap (what's coming next)
- Prioritization criteria (how decisions are made)
- Request process (how to propose new components)

### 4. Feedback Loops

- Quarterly user surveys
- Regular user interviews
- Analytics on component usage
- GitHub issues for bug reports and feature requests

### 5. Continuous Improvement

- Retrospectives after major releases
- Iterate on processes
- Celebrate wins
- Learn from failures

---

Effective documentation and governance are what transform a component library into a true design system. Invest in both to maximize adoption, consistency, and team efficiency.
