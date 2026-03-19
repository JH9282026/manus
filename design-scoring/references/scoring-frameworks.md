# Design Scoring Frameworks

## Overview

Design scoring provides objective evaluation criteria for comparing design alternatives, prioritizing improvements, and measuring design quality. Frameworks transform subjective assessments into quantifiable metrics.

---

## Heuristic Evaluation Scoring

**Nielsen's 10 Usability Heuristics**: Rate each heuristic on 0-4 scale:
- 0: No usability problem
- 1: Cosmetic problem only
- 2: Minor usability problem
- 3: Major usability problem
- 4: Usability catastrophe

**Heuristics**:
1. Visibility of system status
2. Match between system and real world
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, and recover from errors
10. Help and documentation

**Scoring**: Sum scores across all heuristics. Lower is better. Prioritize fixing items with highest scores.

---

## System Usability Scale (SUS)

**10-Question Survey**: Users rate agreement on 1-5 scale:
1. I think I would like to use this system frequently
2. I found the system unnecessarily complex
3. I thought the system was easy to use
4. I think I would need support to use this system
5. I found the various functions well integrated
6. I thought there was too much inconsistency
7. I imagine most people would learn this system quickly
8. I found the system very cumbersome to use
9. I felt very confident using the system
10. I needed to learn a lot before I could get going

**Calculation**: 
- For odd items: subtract 1 from score
- For even items: subtract score from 5
- Sum all scores and multiply by 2.5
- Result: 0-100 score (68+ is above average)

**Benefits**: Industry standard, easy to administer, reliable with small sample sizes (5+ users).

---

## Design Quality Scorecard

**Categories and Weights**:
- Visual Design (20%): Aesthetics, hierarchy, consistency
- Usability (30%): Ease of use, learnability, efficiency
- Accessibility (20%): WCAG compliance, inclusive design
- Content (15%): Clarity, tone, information architecture
- Technical (15%): Performance, responsiveness, feasibility

**Scoring Each Category**: Rate 1-5:
- 1: Fails to meet basic standards
- 2: Meets minimum requirements
- 3: Meets standards adequately
- 4: Exceeds standards
- 5: Exceptional, best-in-class

**Calculation**: Multiply each category score by its weight, sum for total score (1-5 scale).

**Usage**: Compare design alternatives, track improvements over iterations, communicate quality to stakeholders.

---

## Comparative Scoring Matrix

**Purpose**: Objectively compare multiple design alternatives against defined criteria.

**Process**:
1. Define evaluation criteria (5-10 items)
2. Assign weight to each criterion (must sum to 100%)
3. Score each design alternative on each criterion (1-5 scale)
4. Multiply scores by weights
5. Sum weighted scores for each alternative
6. Highest score wins

**Example Criteria**:
- Meets user needs (25%)
- Ease of implementation (15%)
- Visual appeal (15%)
- Accessibility (20%)
- Business goal alignment (15%)
- Innovation (10%)

**Benefits**: Removes bias, makes decision rationale transparent, facilitates stakeholder alignment.

---

## Task Success Metrics

**Task Completion Rate**: Percentage of users who successfully complete task. Target: 90%+

**Time on Task**: Average time to complete task. Compare against baseline or competitor.

**Error Rate**: Number of errors per task attempt. Lower is better.

**Efficiency**: Task completion rate divided by time. Higher is better.

**Satisfaction**: Post-task rating (1-5 or 1-7 scale). Target: 4+ on 5-point scale.

**Composite Score**: Combine metrics into single score. Example: (Completion Rate × 0.4) + (Satisfaction × 0.3) + (Efficiency × 0.3)

---

## Accessibility Scoring

**WCAG Conformance Levels**:
- Level A: 30 success criteria (baseline)
- Level AA: 20 additional criteria (target for most projects)
- Level AAA: 28 additional criteria (enhanced)

**Scoring Method**:
- Pass: Meets criterion (1 point)
- Fail: Doesn't meet criterion (0 points)
- N/A: Criterion doesn't apply

**Calculation**: (Passed criteria / Applicable criteria) × 100 = Conformance percentage

**Automated Tool Scores**: axe, WAVE, and Lighthouse provide automated scores. Combine with manual testing for complete picture.

**Severity-Weighted Scoring**: Weight critical issues higher than minor issues for more meaningful score.

---
