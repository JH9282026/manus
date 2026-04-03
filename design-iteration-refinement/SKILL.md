---
name: design-iteration-refinement
description: "Systematically improve designs based on review findings and score gaps through prioritized, focused changes. Use for: planning design iterations after reviews, prioritizing fixes by impact and effort, executing targeted design improvements, validating changes don't introduce regressions, tracking score progression toward quality targets, and managing the iteration loop from review to re-scoring."
---

# Design Iteration & Refinement

Systematically improve designs based on review findings and score gaps through prioritized, focused changes.

## Overview

Design Iteration is the systematic process of improving designs based on review findings and score gaps. This skill ensures each iteration moves closer to the quality target (typically 9/10) through focused, prioritized changes. It covers issue prioritization, iteration planning, change execution, and validation.

## When to Use

- After design review identifies issues
- When design score is below the target (e.g., below 9/10)
- To address specific feedback from stakeholders
- During refinement phase before handoff
- When iterating between review and scoring cycles

## Impact/Effort Priority Matrix

| Quadrant | Impact | Effort | Action |
|----------|--------|--------|--------|
| **Do First** 🟢 | High | Low | Significant quality improvement with minimal work |
| **Schedule** 🟡 | High | High | Important but requires significant work |
| **Quick Wins** 🟢 | Low | Low | Small polish improvements |
| **Defer** 🟠 | Low | High | Consider if worth the effort, may skip |

Always address **Do First** items in the current iteration. Schedule **High Impact, High Effort** items if time allows. Batch **Quick Wins** together. Defer or eliminate low-value high-effort work.

## Iteration Plan Template

```markdown
## Iteration Plan: V[X] → V[X+1]

### Goal
Move from [current score] to [target score]

### In Scope (This Iteration)
- [Change 1] | Expected impact: +[X] | Effort: [Xh]
- [Change 2] | Expected impact: +[X] | Effort: [Xh]
- [Change 3] | Expected impact: +[X] | Effort: [Xh]

### Out of Scope (Next Iteration)
- [Deferred item 1]
- [Deferred item 2]

### Expected Outcome
- Score improvement: +[X] points
- Target score: [X]/10
```

## Change Documentation

For each change, document:

| Field | Description |
|-------|-------------|
| **Title** | Short descriptive name |
| **Category** | Visual / UX / Consistency / Accessibility / Brand |
| **Issue** | What was wrong |
| **Solution** | What was changed |
| **Before** | Previous state (values, specs) |
| **After** | New state (values, specs) |
| **Impact** | Expected score improvement |

## Common Iteration Categories

### Typography Fixes
- Adjust line-heights (body: 1.5→1.6, headings: 1.1→1.2–1.3)
- Increase heading size differentiation
- Fix line length (target 60–75 characters)

### Shadow & Border Standardization
- Define shadow scale: sm, md, lg
- Apply consistently to all elevated elements
- Standardize border-radius across component types

### Focus State Enhancement
- Add visible focus ring (e.g., 3px colored outline)
- Ensure all interactive elements have focus states
- Test keyboard navigation order

### Mobile Refinement
- Increase touch targets to 48px minimum
- Add swipe actions for common operations
- Implement pull-to-refresh where appropriate
- Redesign navigation for thumb-zone accessibility

### Empty & Loading States
- Design skeleton loaders for content areas
- Add illustrations and CTAs to empty states
- Design error states with recovery actions

## Validation Checklist

After completing iteration changes:

### Issue Resolution
- [ ] Each planned issue is verified fixed
- [ ] Fix addresses the root cause, not just symptoms

### No Regressions
- [ ] Previous strengths are maintained
- [ ] No new issues introduced by changes
- [ ] Consistency not broken across screens

### Quality Check
- [ ] Quick visual scan passes (5-second test)
- [ ] Primary flows still work correctly
- [ ] Responsive behavior intact at all breakpoints

### Ready for Re-scoring
- [ ] All planned changes complete
- [ ] Documentation updated with changes
- [ ] Ready for next review/scoring cycle

## Iteration Cadence

| Iteration | Focus | Target Score |
|-----------|-------|--------------|
| V1 → V2 | Critical fixes (loading, mobile nav, focus) | 7.5/10 |
| V2 → V3 | Important improvements (hierarchy, spacing, indicators) | 8.5/10 |
| V3 → V4 | Polish (micro-interactions, edge cases, accessibility) | 9.0/10 |

Each iteration should be scoped to 4–8 hours of work maximum. Smaller, frequent iterations are better than large infrequent ones.

## Best Practices

1. **Fix the highest-impact issues first** — Don't polish details while critical issues remain
2. **One iteration, one focus** — Don't try to fix everything at once
3. **Document before/after** — Makes review of changes clear and reversible
4. **Re-score after each iteration** — Track progress quantitatively
5. **Don't over-iterate** — Diminishing returns after 3–4 iterations; ship and learn
6. **Preserve what works** — Don't break strengths while fixing weaknesses

## Using the Reference Files

### When to Read Each Reference

**`./references/iteration-planning-examples.md`** — Read when planning a specific iteration, needing concrete examples of before/after changes, or tracking expected score impact across categories.

**`./references/change-implementation-patterns.md`** — Read when implementing specific design changes (typography, shadows, focus states, mobile) and needing detailed CSS specifications and design token updates.

**`./references/iteration-prompts.md`** — Read when needing AI prompts for iteration planning, change implementation, or post-iteration validation.
