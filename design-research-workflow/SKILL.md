---
name: design-research-workflow
description: "Conduct foundational design research to understand project context, user needs, business goals, and constraints before visual design begins. Use for: starting new design projects, gathering requirements, creating research briefs, defining target audiences, establishing success metrics, and grounding design decisions in evidence rather than assumptions."
---

# Design Research

Conduct foundational design research to understand project context, user needs, business goals, and constraints before visual design begins.

# Skill: Design Research

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Design Research |
| **Category** | Research & Inspiration |
| **Phase** | 1 - Research |
| **Estimated Time** | 30-60 minutes |
| **Dependencies** | None (starting point) |
| **Outputs** | Research brief, requirements document |

## Description
Design Research is the foundational skill for understanding project context, user needs, business goals, and constraints before any visual design begins. This skill ensures all subsequent design decisions are grounded in real understanding rather than assumptions.

## When to Use
- Starting any new design project
- Redesigning existing products
- Launching new features
- Pivoting design direction
- When requirements are unclear

---

## Instructions for AI Agents
### Step 1: Gather Project Requirements

**Prompt to extract requirements:**
```
Analyze the following project brief and extract:
1. Primary business goals (what success looks like)
2. Target audience description
3. Key features/functionality needed
4. Brand guidelines or constraints
5. Technical constraints (platforms, frameworks)
6. Timeline and budget considerations
7. Competitive landscape
8. Success metrics

Project brief: [INSERT BRIEF]
```

**Required information to collect:**

| Category | Questions to Answer |
|----------|--------------------|
| Business | What problem are we solving? What are the business objectives? |
| Users | Who will use this? What are their needs? |
| Scope | What pages/screens/features are needed? |
| Brand | Are there existing brand guidelines? Colors? Fonts? |
| Platform | Web only? Mobile app? Both? |
| Timeline | When is this needed? Are there milestones? |
| Competitors | Who are the main competitors? |

### Step 2: Analyze Target Audience

**Prompt for audience analysis:**
```
Based on the target audience of [AUDIENCE DESCRIPTION], identify:
1. Demographics (age, location, profession)
2. Technical proficiency level
3. Device preferences (mobile-first vs desktop)
4. Key pain points and motivations
5. Design expectations based on their industry
6. Accessibility considerations
```

### Step 3: Define Design Direction

**Prompt for design direction:**
```
Based on the following project requirements and audience:
[INSERT REQUIREMENTS AND AUDIENCE INFO]

Recommend:
1. Visual style direction (modern/minimal, bold/playful, corporate/professional, etc.)
2. Color mood (warm, cool, neutral, vibrant)
3. Typography character (elegant, friendly, technical, authoritative)
4. Layout approach (dense information, spacious, card-based, etc.)
5. Interaction level (simple, animated, highly interactive)

Provide reasoning for each recommendation.
```

### Step 4: Document Constraints

**Categories of constraints to identify:**

- **Technical**: Browser support, framework limitations, performance requirements
- **Brand**: Existing colors, fonts, logo usage rules
- **Content**: Text length limits, image availability, localization needs
- **Accessibility**: WCAG level required (AA minimum)
- **Legal**: Privacy policies, terms display requirements, cookie consent

---

## Example Input/Output
### Example Input

```markdown
**Project Brief:**
We need a landing page for our new SaaS product "TaskFlow" - a project 
management tool for small creative agencies. Target audience is creative 
directors and project managers at agencies with 5-20 employees. They're 
tech-savvy but time-poor. We want to feel modern and premium but approachable. 
We have a logo but no brand guidelines yet. Competitors include Monday.com, 
Asana, and Notion. Launch in 6 weeks.
```

### Example Output

```markdown

## Using the Reference Files

### When to Read Each Reference

**`./references/detailed-guidelines.md`** — Read when you need detailed guidance on detailed guidelines aspects of this skill.
