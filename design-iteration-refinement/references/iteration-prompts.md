# Iteration Prompts

AI prompts for planning iterations, implementing changes, and validating improvements.

---

## Iteration Planning Prompt

```
Plan iteration from [CURRENT SCORE] to [TARGET SCORE]:

Given these issues:
[ISSUE LIST]

Create:
1. Priority matrix (impact vs. effort)
2. Scope for this iteration
3. What to defer to next iteration
4. Expected score impact per category
```

---

## Change Implementation Prompt

```
Implement this design change:
- Issue: [ISSUE]
- Goal: [DESIRED OUTCOME]

Provide:
1. Before state (current values)
2. After state (detailed spec)
3. CSS or design token changes needed
4. Verification criteria (how to confirm it's fixed)
```

---

## Iteration Review Prompt

```
Review iteration V[X] → V[X+1]:

1. Were all planned changes made?
2. What improved?
3. Any regressions introduced?
4. Ready for re-scoring?
5. Remaining work estimate to reach target?
```

---

## Regression Check Prompt

```
After making these changes:
[LIST OF CHANGES]

Check for regressions:
1. Do all previously-identified strengths still hold?
2. Are there new inconsistencies?
3. Did any responsive behavior break?
4. Are transitions and animations still smooth?
5. Does the overall design still feel cohesive?
```

---

## Score Projection Prompt

```
Given the current design at [SCORE]/10 with these changes planned:
[CHANGE LIST]

Project the expected score after implementation:
- Visual Design: [current] → [expected]
- UX: [current] → [expected]
- Consistency: [current] → [expected]
- Responsiveness: [current] → [expected]
- Accessibility: [current] → [expected]
- Brand & Polish: [current] → [expected]

Overall projected score: [X]/10
Remaining gap to 9/10: [X] points
```
