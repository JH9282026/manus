---
name: user-flow-design
description: "Map user journeys and task flows to visualize steps, decisions, and touchpoints from entry to completion. Use for: designing user flow diagrams, planning screen sequences before wireframing, identifying friction points in existing flows, optimizing conversion funnels, documenting happy paths and error states, and ensuring logical task completion paths."
---

# User Flow Design

Map user journeys and task flows to visualize the steps, decisions, and touchpoints users take to accomplish goals within a product.

## Overview

User Flows map the paths users take to accomplish goals within a product. They visualize the steps, decisions, and touchpoints from entry to completion, ensuring designs support efficient, logical task completion. This skill provides frameworks for identifying critical flows, mapping flow structure, documenting decision points and error states, and deriving screen requirements from flows.

## When to Use

- After defining user personas, before wireframing
- When designing new features or screen sequences
- To identify friction points in existing flows
- When optimizing conversion funnels
- To document happy paths, edge cases, and error handling

## Flow Identification Framework

Organize flows by criticality:

| Priority | Description | Examples |
|----------|-------------|----------|
| **Critical** | Must work perfectly, core value | Sign up, checkout, primary task |
| **Important** | High frequency daily usage | Update status, search, filter |
| **Supporting** | Occasional but necessary | Settings, export, archive |

Alternatively, map flows to the AARRR funnel:
1. **Acquisition** — How users first engage
2. **Activation** — First value moment
3. **Core** — Primary daily usage
4. **Retention** — What brings them back
5. **Revenue** — Upgrade or purchase

## Flow Mapping Structure

For each flow, document:

| Element | Description |
|---------|-------------|
| **User/Persona** | Which persona takes this path |
| **Goal** | What they want to accomplish |
| **Entry Point** | Where they start (URL, button, notification) |
| **Success Criteria** | What defines completion |
| **Steps** | Ordered sequence of screens and actions |
| **Decision Points** | Branching logic with criteria for each path |
| **Error States** | What can go wrong and recovery actions |

### Step Documentation Table

| Step | Screen | User Action | System Response | Notes |
|------|--------|-------------|-----------------|-------|
| 1 | Screen name | What user does | What happens | Design notes |
| 2 | Screen name | What user does | What happens | Design notes |

## Flow Diagram Notation

Use consistent notation for flow diagrams:

| Symbol | Meaning |
|--------|---------|
| Rounded rectangle | Screen or page |
| Double-border rectangle | Entry or exit point |
| Diamond | Decision point |
| Solid arrow | Primary flow direction |
| Dashed arrow | Optional or alternate path |
| ⚠️ marker | Error state |
| ✓ marker | Success state |

## Critical Flow Documentation

For each critical flow, provide:

1. **Happy Path** — Numbered step-by-step for ideal scenario
2. **Edge Cases** — How unusual situations are handled
3. **Error Handling** — Error cause, user message, recovery action
4. **Screen Requirements** — List of screens this flow requires
5. **Metrics to Track** — Completion rate target, time to complete, drop-off monitoring points

## Flow Optimization Checklist

When reviewing an existing flow, check for:

- Unnecessary steps that can be removed
- Decision points that could be eliminated or defaulted
- Places where users might get stuck or abandon
- Opportunities for delight or acceleration
- Keyboard shortcuts or quick actions
- Progressive disclosure to reduce cognitive load

## Best Practices

1. **Map breadth first** — Identify all flows before detailing any single one
2. **Start from the persona's goal**, not from screens
3. **Design for the happy path first**, then handle edge cases
4. **Keep flows as short as possible** — Every step is a potential drop-off
5. **Include re-entry points** — Users may leave and come back
6. **Consider multi-device flows** — Start on mobile, finish on desktop
7. **Validate with real tasks** — Walk through each flow with a scenario

## Using the Reference Files

### When to Read Each Reference

**`./references/flow-mapping-methodology.md`** — Read when planning a flow mapping session, needing detailed templates for flow structure, or requiring ASCII diagram syntax for documenting flows.

**`./references/flow-examples-patterns.md`** — Read when needing concrete examples of user flows (sign-up, project creation, task management) or common flow patterns for SaaS, e-commerce, or mobile apps.

**`./references/flow-optimization-prompts.md`** — Read when optimizing existing flows, conducting flow audits, or needing AI prompts for flow identification, optimization, and error handling design.
