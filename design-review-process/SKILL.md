---
name: design-review-process
description: "Conduct systematic design evaluations using structured criteria to identify issues and ensure quality standards. Use for: running design critiques, evaluating visual consistency, checking UX heuristics, performing design audits, facilitating peer reviews, and ensuring designs meet professional quality thresholds before delivery."
---

# Design Review

Conduct systematic design evaluations using structured criteria to identify issues and ensure quality standards.

# Skill: Design Review

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Design Review |
| **Category** | Review & Iteration |
| **Phase** | 5 - Review & Iteration |
| **Estimated Time** | 30-45 minutes |
| **Dependencies** | All design phases |
| **Outputs** | Detailed review report with findings and recommendations |

## Description
Design Review systematically evaluates designs against established criteria, user needs, and quality standards. This skill identifies strengths to maintain and weaknesses to address, driving the iterative improvement process.

## When to Use
- After completing a design phase
- Before handoff to development
- When iterating toward 9/10 quality
- During design critiques
- When validating design decisions

---

## Instructions for AI Agents
### Step 1: Establish Review Framework

**Review dimensions:**

```markdown

## Review Checklist
### 1. Visual Design (25%)
- [ ] Color harmony and contrast
- [ ] Typography hierarchy and readability
- [ ] Layout alignment and grid usage
- [ ] Visual hierarchy effectiveness
- [ ] Polish and attention to detail

### 2. User Experience (25%)
- [ ] Clarity of purpose on each screen
- [ ] Intuitive navigation
- [ ] Clear call-to-actions
- [ ] Logical user flows
- [ ] Error prevention and handling

### 3. Consistency (15%)
- [ ] Component reuse
- [ ] Pattern consistency
- [ ] Spacing consistency
- [ ] Interaction consistency

### 4. Responsiveness (15%)
- [ ] Mobile layout quality
- [ ] Breakpoint transitions
- [ ] Touch target sizes
- [ ] Content priority on small screens

### 5. Accessibility (10%)
- [ ] Color contrast compliance
- [ ] Focus states
- [ ] Touch targets
- [ ] Screen reader considerations

### 6. Brand & Polish (10%)
- [ ] Brand alignment
- [ ] Professional appearance
- [ ] Memorable elements
- [ ] Emotional resonance
```

### Step 2: Conduct Visual Inspection

**Systematic review process:**

```markdown

## Visual Inspection Checklist
### Overall Impression
1. Take 5 seconds to look at the design
2. Note first impression (positive/negative/neutral)
3. Identify what draws attention first
4. Assess if primary action is clear

### Element-by-Element Review

#### Typography
- [ ] Is body text readable (16px+)?
- [ ] Is heading hierarchy clear (3+ levels)?
- [ ] Is line length comfortable (60-75 chars)?
- [ ] Is line height appropriate (1.5-1.7 for body)?
- [ ] Are fonts loading correctly?

#### Color
- [ ] Does palette feel cohesive?
- [ ] Is there sufficient contrast?
- [ ] Is color used meaningfully (not decoratively)?
- [ ] Are semantic colors correct (green=success)?
- [ ] Would it work for colorblind users?

#### Layout
- [ ] Is grid usage consistent?
- [ ] Is alignment precise?
- [ ] Is whitespace intentional?
- [ ] Is visual balance achieved?
- [ ] Does layout guide the eye?

#### Components
- [ ] Are all states designed?
- [ ] Are components consistent?
- [ ] Are interactive elements clear?
- [ ] Is feedback adequate?
```

### Step 3: UX Evaluation

**User-centered review:**

```markdown

## UX Evaluation
### Task Completion
For each key user task:
1. Can user identify where to start?
2. Is the path to completion clear?
3. Is progress communicated?
4. Is completion confirmed?

### Cognitive Load
- Is information chunked appropriately?
- Are users overloaded with options?
- Is important info prioritized?
- Can users focus on one task?

### Wayfinding
- Is current location clear?
- Can users navigate to any section?
- Are breadcrumbs/back paths available?
- Is search available if needed?

### Error Handling
- Are potential errors prevented?
- Are error messages helpful?
- Can users recover easily?
- Is data preserved on errors?
```

### Step 4: Document Findings

**Review report template:**

```markdown

## Design Review Report
**Project**: [Name]
**Date**: [Date]
**Reviewer**: [AI Agent/Name]
**Design Version**: [Version number]

---

### Summary

**Overall Score**: [X/10]
**Quality Level**: [Poor/Below Average/Average/Good/Excellent]
**Ready for**: [Next phase / Iteration / Development]

### Key Findings

#### Strengths (Keep These)
1. **[Strength 1]**: [Why it works well]
2. **[Strength 2]**: [Why it works well]
3. **[Strength 3]**: [Why it works well]

#### Areas for Improvement (Address These)
1. **[Issue 1]**: [Description]
   - Impact: [High/Medium/Low]
   - Fix: [Recommendation]
   
2. **[Issue 2]**: [Description]
   - Impact: [High/Medium/Low]
   - Fix: [Recommendation]

#### Critical Issues (Must Fix)
1. **[Critical Issue]**: [Description]
   - Why critical: [Reason]
   - Required fix: [Action]

---

### Detailed Scores

| Category | Score | Notes |
|----------|-------|-------|
| Visual Design | _/10 | |
| User Experience | _/10 | |
| Consistency | _/10 | |
| Responsiveness | _/10 | |
| Accessibility | _/10 | |
| Brand & Polish | _/10 | |

---

### Screen-by-Screen Notes

#### [Screen 1 Name]
- **What's working**: [Notes]
- **Issues**: [Notes]
- **Suggestions**: [Notes]

#### [Screen 2 Name]
- **What's working**: [Notes]
- **Issues**: [Notes]
- **Suggestions**: [Notes]

---

### Recommended Next Steps

1. [ ] [Priority action 1]
2. [ ] [Priority action 2]
3. [ ] [Priority action 3]

### Timeline Estimate
- Critical fixes: [X hours]
- Improvements: [X hours]
- Polish: [X hours]
```

---

## Example Input/Output
### Example Input

```markdown
**Design**: TaskFlow Dashboard v1
**Screens**: Dashboard, Project List, Task Detail
**Stage**: First draft visual design
```

### Example Output

```markdown

## Prompts Library
### Quick Review
```
Provide a rapid design review of [DESIGN/SCREEN]:

1. First impression (1-10)
2. Top 3 strengths
3. Top 3 issues
4. Most critical fix needed
5. Estimated quality level
```

### Focused Review
```
Review [DESIGN] specifically for [ASPECT]:
- Typography / Color / Layout / UX / Accessibility

Provide:
1. Current state assessment
2. Specific issues found
3. Recommended fixes
4. Priority level
```

### Comparative Review
```
Compare [DESIGN A] vs [DESIGN B]:

1. Which is stronger overall?
2. What does A do better?
3. What does B do better?
4. Recommended elements to combine
```

---

## Related Skills
- **Next**: `design_scoring.md` - Apply rubric for objective score
- **Next**: `design_iteration.md` - Act on review findings
- **Related**: `accessibility_review.md` - Deep accessibility review

## Using the Reference Files

### When to Read Each Reference

**`./references/design-review-report-taskflow-dashboard-v1.md`** — Read when you need detailed guidance on design review report taskflow dashboard v1 aspects of this skill.

**`./references/success-criteria.md`** — Read when you need detailed guidance on success criteria aspects of this skill.
