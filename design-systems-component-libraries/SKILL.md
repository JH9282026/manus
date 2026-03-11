---
name: "design-systems-component-libraries"
description: "Create and maintain design systems and component libraries for consistent, scalable UI/UX development. Use for: building design token systems, creating component libraries with atomic design, establishing design governance, implementing systems like Material Design or Carbon, managing design-to-code workflows, documenting components with Storybook, and scaling design across teams and products."
---

# Design Systems & Component Libraries

Create, maintain, and scale design systems that ensure UI consistency, development efficiency, and brand coherence across products and teams.

## Overview

Provide frameworks for building complete design systems including visual foundations, component libraries, documentation, governance, and tooling. Cover atomic design methodology, design tokens, accessibility integration, and cross-platform consistency.

## Design System Maturity Levels

| Level | Components | Documentation | Governance | Adoption |
|---|---|---|---|---|
| Style Guide | Colors, type, icons | Static docs | None | Informal |
| Component Library | Reusable UI components | Usage examples | Light review | Voluntary |
| Design System | Tokens + components + patterns | Interactive docs | Contribution process | Required |
| Design Platform | Full ecosystem + tools | Self-service docs | Dedicated team | Embedded |

## Atomic Design Hierarchy

| Level | Description | Examples |
|---|---|---|
| Atoms | Basic building blocks | Button, input, label, icon |
| Molecules | Simple component groups | Search bar (input + button), form field (label + input) |
| Organisms | Complex UI sections | Header (logo + nav + search), card grid |
| Templates | Page-level layouts | Blog layout, dashboard layout |
| Pages | Specific instances | Homepage, settings page |

## Design Token Architecture

Organize tokens in three tiers:
1. **Global tokens**: Raw values (color hex, pixel sizes)
2. **Alias tokens**: Semantic mappings (color-primary, spacing-md)
3. **Component tokens**: Specific usage (button-background-primary)

### Token Categories

| Category | Examples | Format |
|---|---|---|
| Color | Primary, secondary, semantic, neutral | Hex, HSL |
| Typography | Font family, size scale, weight, line height | px, rem |
| Spacing | Padding, margin, gap scale | px, rem |
| Border | Width, radius, style | px |
| Shadow | Elevation levels | CSS shadow |
| Motion | Duration, easing curves | ms, cubic-bezier |
| Breakpoints | Mobile, tablet, desktop, wide | px |

## Component Documentation Checklist

For each component, document:
- [ ] Component name and description
- [ ] Visual examples of all variants and states
- [ ] Props/API specification
- [ ] Usage guidelines (when to use / when not to use)
- [ ] Accessibility requirements (ARIA, keyboard, screen reader)
- [ ] Code examples (React, Vue, or framework-specific)
- [ ] Design file links (Figma, Sketch)

## Using the Reference Files

### When to Read Each Reference

**`/references/building-component-libraries.md`** — Read when creating new components, defining component APIs, or implementing atomic design patterns in code.

**`/references/governance-and-scaling.md`** — Read when establishing contribution processes, managing versioning, rolling out the design system across teams, or handling internationalization.
