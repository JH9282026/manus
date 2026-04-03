---
name: design-competitive-analysis
description: "Analyze competitor designs and industry patterns to identify opportunities and establish design benchmarks. Use for: evaluating competitor UX patterns, identifying design gaps, benchmarking visual quality, auditing competitor features, and informing design strategy with competitive insights."
---

# Competitive Analysis

Analyze competitor designs and industry patterns to identify opportunities and establish design benchmarks.

# Skill: Competitive Analysis

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Competitive Analysis |
| **Category** | Research & Inspiration |
| **Phase** | 1 - Research |
| **Estimated Time** | 30-60 minutes |
| **Dependencies** | `design_research.md` |
| **Outputs** | Competitive analysis report, differentiation strategy |

## Description
Competitive Analysis involves systematically examining competitor designs to understand industry standards, identify opportunities for differentiation, and avoid common pitfalls. This skill focuses specifically on design aspects rather than business strategy.

## When to Use
- Starting a new project in an established market
- Redesigning to better compete
- Understanding industry design conventions
- Finding white space for differentiation
- Validating design direction decisions

---

## Instructions for AI Agents
### Step 1: Identify Competitors

**Prompt to identify competitors:**
```
For a [PROJECT TYPE] in the [INDUSTRY] space, identify:

1. **Direct Competitors** (3-5): Same product/service, same audience
2. **Indirect Competitors** (2-3): Different product, same audience OR same product, different audience
3. **Aspirational References** (2-3): Not competitors but gold-standard design examples

For each, provide:
- Company/product name
- Website URL
- Why they're relevant to analyze
```

### Step 2: Visual Design Audit

**For each competitor, analyze:**

```
Analyze the visual design of [COMPETITOR URL]:

## BRAND IDENTITY
- Logo style: [Description]
- Brand personality conveyed: [Adjectives]
- Visual tone: [Professional/Playful/Technical/etc.]

## COLOR PALETTE
- Primary brand color: [Hex]
- Secondary colors: [Hex values]
- Background treatment: [Description]
- How color creates hierarchy: [Analysis]
- Accessibility: [Contrast assessment]

## TYPOGRAPHY
- Heading font: [Family, weights used]
- Body font: [Family, size observed]
- Hierarchy approach: [How they differentiate levels]
- Readability: [Assessment]

## LAYOUT & STRUCTURE
- Homepage structure: [Sections in order]
- Navigation pattern: [Sticky/standard, position, items]
- Content density: [Sparse/balanced/dense]
- Grid usage: [Observations]
- White space usage: [Assessment]

## UI COMPONENTS
- Button styles: [Description]
- Card treatments: [If used]
- Form styling: [If visible]
- Icon style: [Outline/filled/custom]

## IMAGERY & GRAPHICS
- Image style: [Photos/illustrations/abstract]
- Graphic elements: [Gradients/shapes/patterns]
- Screenshot treatment: [How product is shown]

## UNIQUE ELEMENTS
- Standout design features: [What's distinctive]
- Micro-interactions observed: [If any]

## STRENGTHS & WEAKNESSES
- Design strengths: [What works well]
- Design weaknesses: [What could improve]
```

### Step 3: Comparative Matrix

**Create comparison grid:**

```markdown

## Design Comparison Matrix
| Aspect | [Competitor 1] | [Competitor 2] | [Competitor 3] | Opportunity |
|--------|----------------|----------------|----------------|-------------|
| Primary Color | | | | |
| Color Mood | | | | |
| Typography | | | | |
| Layout Style | | | | |
| Visual Density | | | | |
| Imagery Type | | | | |
| Brand Personality | | | | |
| Unique Elements | | | | |
| Mobile Experience | | | | |
| Accessibility | | | | |
```

### Step 4: Identify Patterns & Opportunities

**Prompt for pattern analysis:**
```
Based on the competitive analysis of [COMPETITORS LIST]:

1. **Industry Conventions** (must follow):
   - What design patterns are expected/required?
   - What would confuse users if missing?

2. **Common Approaches** (can follow or differentiate):
   - What do most competitors do similarly?
   - Which of these are best practices vs. just common?

3. **White Space Opportunities** (differentiation):
   - What is NO competitor doing well?
   - What visual territories are unclaimed?
   - How can we stand out while remaining appropriate?

4. **Anti-patterns** (avoid):
   - What mistakes are competitors making?
   - What would our audience dislike?
```

### Step 5: Differentiation Strategy

**Create actionable differentiation plan:**

```markdown

## Differentiation Strategy
### Where to Conform
[Design elements where following conventions is important for usability]

1. [Convention 1]: Why it matters
2. [Convention 2]: Why it matters

### Where to Differentiate
[Opportunities to stand out]

1. **[Differentiation 1]**
   - What competitors do: [X]
   - What we'll do: [Y]
   - Why it's better: [Reason]

2. **[Differentiation 2]**
   - What competitors do: [X]
   - What we'll do: [Y]
   - Why it's better: [Reason]

### Signature Elements
[Unique design elements that will become recognizable]

1. [Element]: [Description and reasoning]
```

---

## Example Input/Output
### Example Input

```markdown
**Project**: TaskFlow - SaaS project management for creative agencies
**Competitors provided**: Monday.com, Asana, Notion
**Additional to research**: Similar sized competitors in creative space
```

### Example Output

```markdown

## Prompts Library
### Quick Competitor Scan
```
Provide a 2-minute visual assessment of [URL]:
- First impression (3 words)
- Primary color
- Overall style (modern/dated, minimal/busy, premium/casual)
- One strength, one weakness
- Relevance to [OUR PROJECT]
```

### Color Comparison
```
Compare the color strategies of [COMPETITOR 1], [COMPETITOR 2], [COMPETITOR 3]:
1. Primary brand colors
2. How they differ from each other
3. What mood each creates
4. Gap in the color landscape we could fill
```

### UX Pattern Analysis
```
Analyze the [SPECIFIC FLOW: onboarding/checkout/signup] of [COMPETITOR]:
1. Steps involved
2. Design patterns used
3. What works well
4. Friction points
5. How we could improve on this
```

### Differentiation Brainstorm
```
Given that [COMPETITORS] all do [COMMON APPROACH], brainstorm 5 ways we could differentiate while maintaining usability:

1. [Alternative approach]
2. [Alternative approach]
...

For each, rate: Innovation (1-5), Risk (1-5), Feasibility (1-5)
```

---

## Resources
### Tools for Competitive Analysis
- **SimilarWeb**: Traffic and audience insights
- **BuiltWith**: Technology stack detection
- **Wayback Machine**: Historical design evolution
- **Chrome DevTools**: Inspect fonts, colors, spacing

### Analysis Frameworks
- Feature comparison matrix
- Visual design audit checklist
- UX heuristic evaluation

---

## Success Criteria
### Minimum Requirements
- [ ] 3-5 competitors analyzed
- [ ] Visual design elements documented
- [ ] Comparison matrix created
- [ ] Differentiation opportunities identified
- [ ] Clear direction on what to follow vs. differentiate

### Quality Indicators
- [ ] Analysis is objective, not just opinion
- [ ] Specific, actionable insights extracted
- [ ] Differentiation strategy is achievable
- [ ] Balance between convention and innovation
- [ ] Competitor weaknesses identified tactfully

---

## Common Pitfalls
1. **Copying competitors**: Analyze to differentiate, not duplicate
2. **Only looking at leaders**: Smaller competitors may have innovations
3. **Ignoring indirect competitors**: Cross-industry inspiration is valuable
4. **Surface-level analysis**: Dig into WHY designs work, not just WHAT
5. **Analysis paralysis**: Set a time limit, then move forward
6. **Being different for its own sake**: Differentiation must serve users

---

## Related Skills
- **Previous**: `design_research.md` - Understand project context first
- **Previous**: `inspiration_gathering.md` - Broader inspiration beyond competitors
- **Next**: `user_personas.md` - Define who we're designing for
- **Next**: `color_palettes.md` - Apply competitive color insights

## Using the Reference Files

### When to Read Each Reference

**`./references/competitive-design-analysis-taskflow.md`** — Read when you need detailed guidance on competitive design analysis taskflow aspects of this skill.
