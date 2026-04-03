---
name: design-iteration-workflow
description: "Implement targeted design improvements based on review feedback and scoring results to systematically elevate quality. Use for: prioritizing design fixes, applying visual refinements, improving UX issues, iterating toward quality targets, managing revision cycles, and systematically addressing feedback from design reviews."
---

# Design Iteration

Implement targeted design improvements based on review feedback and scoring results to systematically elevate quality.

# Skill: Design Iteration

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Design Iteration |
| **Category** | Review & Iteration |
| **Phase** | 5 - Review & Iteration |
| **Estimated Time** | Varies by scope |
| **Dependencies** | `design_review.md`, `design_scoring.md` |
| **Outputs** | Improved design version |

## Description
Design Iteration is the systematic process of improving designs based on review findings and score gaps. This skill ensures each iteration moves closer to the 9/10 quality target through focused, prioritized changes.

## When to Use
- After design review identifies issues
- When score is below 9/10
- To address specific feedback
- During refinement phase
- Before final handoff

---

## Instructions for AI Agents
### Step 1: Prioritize Issues

**Impact/Effort matrix:**

```markdown

## Issue Prioritization
### High Impact, Low Effort (Do First) 🟢
[Issues that significantly improve quality with minimal work]

1. [Issue]: [Impact description] | Effort: [X hours]
2. [Issue]: [Impact description] | Effort: [X hours]

### High Impact, High Effort (Schedule) 🟡
[Issues that are important but require significant work]

1. [Issue]: [Impact description] | Effort: [X hours]

### Low Impact, Low Effort (Quick Wins) 🟢
[Small improvements that polish the design]

1. [Issue]: [Impact description] | Effort: [X hours]

### Low Impact, High Effort (Defer) 🔴
[Consider if worth the effort, may skip]

1. [Issue]: [Impact description] | Effort: [X hours]
```

### Step 2: Plan Iteration

**Iteration plan template:**

```markdown

## Iteration Plan: V[X] → V[X+1]
### Goal
Move from [current score] to [target score]

### Scope
**In Scope**:
- [Change 1]
- [Change 2]
- [Change 3]

**Out of Scope** (next iteration):
- [Deferred item 1]
- [Deferred item 2]

### Checklist

#### Visual Design Improvements
- [ ] [Specific change 1]
- [ ] [Specific change 2]

#### UX Improvements
- [ ] [Specific change 1]
- [ ] [Specific change 2]

#### Consistency Fixes
- [ ] [Specific change 1]
- [ ] [Specific change 2]

#### Accessibility Fixes
- [ ] [Specific change 1]

### Expected Outcome
- Score improvement: +[X] points
- Target score: [X]/10
```

### Step 3: Execute Changes

**For each change, document:**

```markdown

## Change Log: V[X]
### Change 1: [Title]
**Category**: [Visual/UX/Consistency/Accessibility/Brand]
**Issue**: [What was wrong]
**Solution**: [What was changed]
**Before**: [Description or reference]
**After**: [Description or reference]

### Change 2: [Title]
...
```

### Step 4: Validate Changes

**Post-iteration checklist:**

```markdown

## Iteration Validation
### Issue Resolution
- [ ] Issue 1: Verified fixed
- [ ] Issue 2: Verified fixed
- [ ] Issue 3: Verified fixed

### No Regressions
- [ ] Previous strengths maintained
- [ ] No new issues introduced
- [ ] Consistency not broken

### Quality Check
- [ ] Quick visual scan passes
- [ ] Primary flows still work
- [ ] Responsive behavior intact

### Ready for Re-scoring
- [ ] All planned changes complete
- [ ] Documentation updated
- [ ] Ready for `design_scoring.md`
```

---

## Example Input/Output
### Example Input

```markdown
**Current Version**: TaskFlow v2
**Current Score**: 7.74/10
**Target**: 9.0/10
**Key Issues from Review**:
1. Typography line-height too tight
2. Shadow inconsistencies
3. Focus states need enhancement
4. Mobile task list needs refinement
5. Empty states lack personality
```

### Example Output

```markdown

## Prompts Library
### Iteration Planning
```
Plan iteration from [CURRENT SCORE] to [TARGET SCORE]:

Given these issues:
[ISSUE LIST]

Create:
1. Priority matrix
2. Scope for this iteration
3. What to defer
4. Expected score impact
```

### Change Implementation
```
Implement this design change:
- Issue: [ISSUE]
- Goal: [DESIRED OUTCOME]

Provide:
1. Before state
2. After state (detailed spec)
3. CSS/design token changes
4. Verification criteria
```

### Iteration Review
```
Review iteration V[X] → V[X+1]:

1. Were all planned changes made?
2. What improved?
3. Any regressions?
4. Ready for re-scoring?
5. Remaining work estimate?
```

---

## Success Criteria
### Minimum Requirements
- [ ] High-impact issues addressed
- [ ] Changes documented
- [ ] No regressions introduced
- [ ] Ready for re-scoring

### Quality Indicators
- [ ] Score improved as expected
- [ ] Changes align with design system
- [ ] Iteration moves toward 9/10
- [ ] Sustainable pace (not rushed)

---

## Related Skills
- **Previous**: `design_scoring.md` - Know what to improve
- **Next**: `design_review.md` - Validate improvements
- **Loop**: Continue until 9/10 achieved

## Using the Reference Files

### When to Read Each Reference

**`./references/iteration-plan-taskflow-v2-v3.md`** — Read when you need detailed guidance on iteration plan taskflow v2 v3 aspects of this skill.
