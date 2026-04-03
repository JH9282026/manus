---
name: design-review-workflow
description: "Systematically evaluate designs against established criteria, user needs, and quality standards to identify strengths and weaknesses. Use for: conducting design critiques, evaluating visual design quality, assessing UX effectiveness, checking consistency and accessibility, generating detailed review reports with scores and recommendations, and validating designs before development handoff."
---

# Design Review Workflow

Systematically evaluate designs against established criteria, user needs, and quality standards to drive iterative improvement.

## Overview

Design Review systematically evaluates designs against established criteria, user needs, and quality standards. It identifies strengths to maintain and weaknesses to address, producing actionable review reports with scores and prioritized recommendations. This skill covers review frameworks, visual inspection checklists, UX evaluation, and structured reporting.

## When to Use

- After completing a design phase
- Before handoff to development
- When iterating toward high quality (9/10 target)
- During design critiques or team reviews
- When validating design decisions against requirements

## Review Dimensions & Weights

| Dimension | Weight | Focus Areas |
|-----------|--------|-------------|
| Visual Design | 25% | Color harmony, typography hierarchy, layout alignment, visual hierarchy, polish |
| User Experience | 25% | Clarity of purpose, intuitive navigation, clear CTAs, logical flows, error handling |
| Consistency | 15% | Component reuse, pattern consistency, spacing consistency, interaction consistency |
| Responsiveness | 15% | Mobile layout quality, breakpoint transitions, touch targets, content priority |
| Accessibility | 10% | Color contrast, focus states, touch targets, screen reader considerations |
| Brand & Polish | 10% | Brand alignment, professional appearance, memorable elements, emotional resonance |

## Visual Inspection Checklist

### First Impression (5-Second Test)
1. Look at the design for 5 seconds
2. Note first impression (positive/negative/neutral)
3. Identify what draws attention first
4. Assess if primary action is clear

### Typography Check
- [ ] Body text readable (16px+ size)
- [ ] Heading hierarchy clear (3+ distinct levels)
- [ ] Line length comfortable (60–75 characters)
- [ ] Line height appropriate (1.5–1.7 for body)
- [ ] Font loading handled correctly

### Color Check
- [ ] Palette feels cohesive
- [ ] Sufficient contrast ratios
- [ ] Color used meaningfully (not just decoratively)
- [ ] Semantic colors correct (green=success, red=error)
- [ ] Works for colorblind users

### Layout Check
- [ ] Grid usage consistent
- [ ] Alignment precise (no off-grid elements)
- [ ] Whitespace intentional and consistent
- [ ] Visual balance achieved
- [ ] Layout guides the eye through content hierarchy

### Component Check
- [ ] All states designed (default, hover, active, disabled, focus, error)
- [ ] Components consistent across screens
- [ ] Interactive elements clearly identifiable
- [ ] Feedback adequate for user actions

## UX Evaluation

### Task Completion
For each key user task verify:
1. User can identify where to start
2. Path to completion is clear
3. Progress is communicated
4. Completion is confirmed

### Cognitive Load
- Information chunked appropriately
- Users not overloaded with options
- Important information prioritized
- Users can focus on one task at a time

### Wayfinding
- Current location is clear (active states, breadcrumbs)
- Users can navigate to any section
- Back paths are available
- Search available for complex navigation

### Error Handling
- Potential errors prevented where possible
- Error messages are helpful and specific
- Users can recover easily
- Data is preserved on errors

## Review Report Structure

```markdown
## Design Review Report

**Project**: [Name] | **Version**: [X] | **Date**: [Date]

### Summary
- **Overall Score**: [X/10]
- **Quality Level**: [Poor/Below Average/Average/Good/Excellent]
- **Ready for**: [Next phase / Iteration / Development]

### Strengths (Keep These)
1. [Strength]: [Why it works]

### Areas for Improvement
1. [Issue]: [Description] | Impact: [High/Med/Low] | Fix: [Recommendation]

### Critical Issues (Must Fix)
1. [Issue]: [Why critical] | Required fix: [Action]

### Detailed Scores
| Category | Score | Notes |
|----------|-------|-------|
| Visual Design | _/10 | |
| User Experience | _/10 | |
| Consistency | _/10 | |
| Responsiveness | _/10 | |
| Accessibility | _/10 | |
| Brand & Polish | _/10 | |

### Recommended Next Steps
1. [Priority action with time estimate]
```

## Scoring Guidelines

| Score | Quality Level | Description |
|-------|--------------|-------------|
| 1–3 | Poor | Major issues, needs significant rework |
| 4–5 | Below Average | Functional but unprofessional |
| 6–7 | Average/Good | Solid foundation, needs refinement |
| 8 | Very Good | Production-ready with minor polish needed |
| 9–10 | Excellent | High quality, professional, delightful |

## Best Practices

1. **Be balanced** — Always identify strengths alongside weaknesses
2. **Be specific** — "Card padding varies (16px, 20px, 24px)" not "spacing is inconsistent"
3. **Be actionable** — Every issue should have a concrete fix recommendation
4. **Prioritize** — Assign impact levels so teams know what to fix first
5. **Include estimates** — Time estimates help with planning iterations
6. **Review screen by screen** — Then synthesize patterns across screens

## Using the Reference Files

### When to Read Each Reference

**`./references/review-checklists-detail.md`** — Read when conducting a thorough design review and needing complete element-by-element checklists for typography, color, layout, and components.

**`./references/review-report-examples.md`** — Read when writing a design review report and needing concrete examples of findings, scores, and screen-by-screen notes.

**`./references/review-prompts-templates.md`** — Read when needing AI prompts for quick reviews, focused reviews (typography-only, UX-only), or comparative design reviews.
