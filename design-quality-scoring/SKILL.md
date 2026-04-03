---
name: design-quality-scoring
description: "Apply rubric-based scoring to objectively measure design quality across visual, UX, and technical dimensions. Use for: scoring designs against quality rubrics, measuring visual aesthetics, evaluating usability heuristics, assessing accessibility compliance, benchmarking design progress, and ensuring designs achieve 9/10+ quality thresholds."
---

# Design Scoring

Apply rubric-based scoring to objectively measure design quality across visual, UX, and technical dimensions.

# Skill: Design Scoring

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Design Scoring |
| **Category** | Review & Iteration |
| **Phase** | 5 - Review & Iteration |
| **Estimated Time** | 15-20 minutes |
| **Dependencies** | `design_review.md`, `design_rubric.md` |
| **Outputs** | Objective score with breakdown, gap analysis |

## Description
Design Scoring applies the comprehensive rubric to objectively measure design quality on a 1-10 scale. This enables tracking progress across iterations and provides clear targets for improvement.

## When to Use
- After each design iteration
- To measure progress toward 9/10 goal
- During design reviews
- To identify specific weak areas
- Before declaring design "complete"

**Critical Rule**: All designs must achieve **9/10 or higher** before delivery.

---

## Instructions for AI Agents
### Step 1: Prepare for Scoring

**Pre-scoring checklist:**
```markdown
Before scoring, confirm:
- [ ] Design is complete enough to evaluate
- [ ] All key screens are available
- [ ] Responsive versions exist (or can be inferred)
- [ ] Component states are defined
- [ ] Have access to rubric criteria
```

### Step 2: Apply Rubric Categories

**Score each category (1-10):**

```markdown

## Scoring Worksheet
### Category 1: Visual Aesthetics (25% weight)

#### 1.1 Color Usage (5%)
Score: _/10
Rationale: 

#### 1.2 Typography (5%)
Score: _/10
Rationale: 

#### 1.3 Layout & Composition (5%)
Score: _/10
Rationale: 

#### 1.4 Visual Hierarchy (5%)
Score: _/10
Rationale: 

#### 1.5 Polish & Detail (5%)
Score: _/10
Rationale: 

**Category Score**: (avg of above) = _/10

---

### Category 2: User Experience (25% weight)

#### 2.1 Usability (10%)
Score: _/10
Rationale: 

#### 2.2 Information Architecture (5%)
Score: _/10
Rationale: 

#### 2.3 User Flow (5%)
Score: _/10
Rationale: 

#### 2.4 Content Clarity (5%)
Score: _/10
Rationale: 

**Category Score**: _/10

---

### Category 3: Consistency & Systems (15% weight)

#### 3.1 Design System Adherence (5%)
Score: _/10
Rationale: 

#### 3.2 Component Consistency (5%)
Score: _/10
Rationale: 

#### 3.3 Spacing & Rhythm (5%)
Score: _/10
Rationale: 

**Category Score**: _/10

---

### Category 4: Responsiveness (15% weight)

#### 4.1 Mobile Design (5%)
Score: _/10
Rationale: 

#### 4.2 Tablet/Desktop Adaptation (5%)
Score: _/10
Rationale: 

#### 4.3 Cross-Platform Consistency (5%)
Score: _/10
Rationale: 

**Category Score**: _/10

---

### Category 5: Accessibility (10% weight)

#### 5.1 Color Accessibility (4%)
Score: _/10
Rationale: 

#### 5.2 Interactive Accessibility (3%)
Score: _/10
Rationale: 

#### 5.3 Content Accessibility (3%)
Score: _/10
Rationale: 

**Category Score**: _/10

---

### Category 6: Brand & Identity (10% weight)

#### 6.1 Brand Expression (5%)
Score: _/10
Rationale: 

#### 6.2 Emotional Design (5%)
Score: _/10
Rationale: 

**Category Score**: _/10
```

### Step 3: Calculate Final Score

**Weighted calculation:**

```markdown

## Final Score Calculation
| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| Visual Aesthetics | _/10 | × 0.25 | = _ |
| User Experience | _/10 | × 0.25 | = _ |
| Consistency | _/10 | × 0.15 | = _ |
| Responsiveness | _/10 | × 0.15 | = _ |
| Accessibility | _/10 | × 0.10 | = _ |
| Brand & Identity | _/10 | × 0.10 | = _ |
| **FINAL SCORE** | | | **_/10** |

### Quality Level
| Score Range | Level | Action |
|-------------|-------|--------|
| 9.0-10.0 | ✅ Excellent | Ready for delivery |
| 8.0-8.9 | Good | Minor polish needed |
| 7.0-7.9 | Average | Focused improvements |
| 6.0-6.9 | Below Average | Significant revision |
| <6.0 | Poor | Major rework required |

**Current Level**: [Level]
**Ready for Delivery**: [Yes/No]
```

### Step 4: Gap Analysis

**Identify improvement path:**

```markdown

## Gap Analysis
### Current State
- **Score**: [X/10]
- **Target**: 9.0/10
- **Gap**: [Y points]

### Weakest Categories (Focus Here)

1. **[Category with lowest score]**: [Score]/10
   - Why it's low: [Explanation]
   - To reach 9: [Specific improvements needed]
   - Estimated effort: [Hours]

2. **[Second lowest category]**: [Score]/10
   - Why it's low: [Explanation]
   - To reach 9: [Specific improvements needed]
   - Estimated effort: [Hours]

### Strongest Categories (Maintain)

1. **[Highest category]**: [Score]/10
   - Keep: [What's working]
   - Avoid: [What could reduce this]

### Impact Analysis

To reach 9.0:
- If we improve [Category 1] from [X] to 9: Final = [new score]
- If we improve [Category 2] from [X] to 9: Final = [new score]
- Most efficient path: [Which categories to focus on]
```

---

## Example Input/Output
### Example Input

```markdown
**Design**: TaskFlow Dashboard v2
**Context**: Second iteration after addressing critical issues
```

### Example Output

```markdown

## Prompts Library
### Quick Score
```
Score this design quickly (1-10):
[DESIGN]

Provide:
- Overall score with one-line rationale
- Strongest category
- Weakest category
- One action to improve most
```

### Category Deep-Dive
```
Score [DESIGN] deeply on [CATEGORY]:

For each subcategory:
1. Score (1-10)
2. Evidence/rationale
3. Specific improvement to reach 9
```

### Progress Comparison
```
Compare scores between [VERSION 1] and [VERSION 2]:

1. Score comparison table
2. Improvements made
3. Regressions (if any)
4. Remaining work to 9/10
```

---

## Success Criteria
### Minimum Requirements
- [ ] All categories scored
- [ ] Final weighted score calculated
- [ ] Rationale provided for each score
- [ ] Gap to 9/10 identified

### Quality Indicators
- [ ] Scores are calibrated consistently
- [ ] Rationale is specific, not vague
- [ ] Path to improvement is clear
- [ ] Effort estimates included

---

## Using the Reference Files

### When to Read Each Reference

**`./references/design-score-card-taskflow-v2.md`** — Read when you need detailed guidance on design score card taskflow v2 aspects of this skill.

**`./references/related-skills.md`** — Read when you need detailed guidance on related skills aspects of this skill.
