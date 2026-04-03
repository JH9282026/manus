# Review Prompts & Templates

AI prompts for conducting different types of design reviews.

---

## Quick Review Prompt

```
Provide a rapid design review of [DESIGN/SCREEN]:

1. First impression (1-10)
2. Top 3 strengths
3. Top 3 issues
4. Most critical fix needed
5. Estimated quality level
```

---

## Focused Review Prompt

```
Review [DESIGN] specifically for [ASPECT]:
- Typography / Color / Layout / UX / Accessibility

Provide:
1. Current state assessment
2. Specific issues found
3. Recommended fixes
4. Priority level for each fix
```

---

## Comparative Review Prompt

```
Compare [DESIGN A] vs [DESIGN B]:

1. Which is stronger overall?
2. What does A do better?
3. What does B do better?
4. Recommended elements to combine
5. Which is closer to production-ready?
```

---

## Accessibility-Focused Review

```
Conduct an accessibility review of [DESIGN]:

1. Color contrast compliance (WCAG AA)
2. Touch target sizes (44px minimum)
3. Focus state visibility
4. Screen reader considerations
5. Keyboard navigation order
6. Information not dependent on color alone
```

---

## Pre-Handoff Review

```
Review [DESIGN] for development handoff readiness:

1. Are all states designed (default, hover, active, disabled, error, loading, empty)?
2. Are responsive breakpoints specified?
3. Are spacing values on the design system scale?
4. Are interactions and transitions documented?
5. Are edge cases handled (long text, missing data, slow loading)?
6. Is the design technically feasible?
```

---

## Review Report Template

```markdown
## Design Review Report

**Project**: [Name]
**Date**: [Date]
**Version**: [X]
**Reviewer**: [Name/AI]

### Summary
**Overall Score**: [X/10]
**Quality Level**: [Poor/Below Average/Average/Good/Excellent]
**Ready for**: [Next phase / Iteration / Development]

### Key Findings

#### Strengths
1. [Strength 1]: [Why it works]
2. [Strength 2]: [Why it works]

#### Improvements Needed
1. [Issue 1]: [Description] | Impact: [H/M/L] | Fix: [Action]
2. [Issue 2]: [Description] | Impact: [H/M/L] | Fix: [Action]

#### Critical Issues
1. [Critical 1]: [Description] | Fix: [Action] | Estimate: [Hours]

### Scores
| Category | Score | Notes |
|----------|-------|-------|
| Visual Design | /10 | |
| UX | /10 | |
| Consistency | /10 | |
| Responsiveness | /10 | |
| Accessibility | /10 | |
| Brand & Polish | /10 | |

### Next Steps
1. [Action with estimate]
2. [Action with estimate]
```
