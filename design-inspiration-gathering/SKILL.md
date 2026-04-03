---
name: design-inspiration-gathering
description: "Collect and organize visual design inspiration from curated sources to inform design direction and establish aesthetic benchmarks. Use for: creating moodboards, gathering UI references from Dribbble and Behance, building visual direction decks, analyzing design trends, and establishing creative direction for web and mobile projects."
---

# Inspiration Gathering

Collect and organize visual design inspiration from curated sources to inform design direction and establish aesthetic benchmarks.

# Skill: Inspiration Gathering

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Inspiration Gathering |
| **Category** | Research & Inspiration |
| **Phase** | 1 - Research |
| **Estimated Time** | 45-90 minutes |
| **Dependencies** | `design_research.md` |
| **Outputs** | Curated moodboard, reference collection |

## Description
Inspiration Gathering involves systematically collecting visual references from Dribbble, the web, and user-provided examples to establish a visual direction and inform design decisions. This skill bridges research and visual design, ensuring designs are grounded in proven patterns while remaining original.

## When to Use
- After completing initial design research
- When establishing a new visual direction
- When exploring alternative design approaches
- During iteration when seeking fresh ideas
- When user provides example references to analyze

---

## Instructions for AI Agents
### Step 1: Define Search Strategy

**Prompt to create search plan:**
```
Based on this project context:
- Project type: [TYPE]
- Industry: [INDUSTRY]
- Target audience: [AUDIENCE]
- Design direction: [DIRECTION]

Create a search strategy with:
1. 5-10 specific Dribbble search queries
2. 3-5 general web search queries for inspiration
3. Key visual elements to look for (colors, typography, layouts)
4. Design patterns relevant to this project type
```

### Step 2: Search Dribbble

**Primary Dribbble search queries by project type:**

| Project Type | Search Queries |
|--------------|----------------|
| Landing Page | "landing page", "hero section", "saas landing", "marketing website" |
| Dashboard | "dashboard ui", "admin panel", "analytics dashboard", "data visualization" |
| E-commerce | "e-commerce", "product page", "shopping cart", "checkout flow" |
| Mobile App | "mobile app ui", "ios app", "android ui", "app design" |
| Portfolio | "portfolio website", "creative portfolio", "agency website" |
| SaaS | "saas ui", "web app", "b2b software", "enterprise ux" |

**Dribbble search URLs:**
```
https://dribbble.com/search/[QUERY]
https://dribbble.com/search/[QUERY]/shots?color=[HEX_WITHOUT_HASH]
```

**Prompt for Dribbble analysis:**
```
Search Dribbble for "[QUERY]" and identify:
1. Top 5 visually striking examples
2. Common patterns across results
3. Color trends in this category
4. Typography approaches used
5. Layout patterns that appear frequently
6. Unique elements worth considering

For each top example, note:
- What makes it effective
- Specific elements to potentially adapt
- How it could apply to [PROJECT]
```

### Step 3: Web Search for Inspiration

**Search queries for broader inspiration:**
```
"best [PROJECT TYPE] design 2024"
"[INDUSTRY] website examples"
"award winning [PROJECT TYPE]"
"[PROJECT TYPE] design trends"
"[COMPETITOR] website design analysis"
```

**Inspiration websites to check:**
- Awwwards: https://awwwards.com
- Land-book: https://land-book.com
- Mobbin: https://mobbin.com (for mobile)
- Bestfolios: https://bestfolios.com (for portfolios)
- Saas Landing Page: https://saaslandingpage.com

### Step 4: Analyze User-Provided Examples

**When user provides example URLs or images:**

```
Analyze this design reference: [URL/IMAGE]

Extract and document:

**COLOR ANALYSIS**
- Primary color(s): [hex values]
- Secondary color(s): [hex values]
- Background color(s): [hex values]
- Accent color(s): [hex values]
- Overall palette mood: [warm/cool/neutral/vibrant]

**TYPOGRAPHY ANALYSIS**
- Heading style: [font family if identifiable, characteristics]
- Body text style: [characteristics]
- Hierarchy levels: [how many, how differentiated]
- Special text treatments: [any notable styling]

**LAYOUT ANALYSIS**
- Grid structure: [columns, gutters]
- Content density: [spacious/balanced/dense]
- Key layout patterns: [cards, sections, etc.]
- Navigation style: [description]

**VISUAL ELEMENTS**
- Imagery style: [photos, illustrations, abstract]
- Icon style: [outline, filled, custom]
- Decorative elements: [gradients, shapes, patterns]
- Shadow/depth usage: [flat, subtle depth, pronounced]

**INTERACTION HINTS**
- Hover effects visible: [yes/no, describe]
- Animation suggestions: [based on visual cues]
- Interactive elements: [buttons, forms, etc.]

**KEY TAKEAWAYS**
- What works well: [list 3-5 items]
- What to adapt for our project: [list specifics]
- What to avoid: [any concerns]
```

### Step 5: Compile Moodboard

**Moodboard organization structure:**

```markdown

## Inspiration Moodboard for [PROJECT]
### Overall Direction
[2-3 sentences describing the visual direction]

### Color References
| Source | Palette | Application |
|--------|---------|-------------|
| [Reference 1] | [Colors] | [How to use] |
| [Reference 2] | [Colors] | [How to use] |

### Typography References
| Source | Style | Application |
|--------|-------|-------------|
| [Reference 1] | [Description] | [How to use] |
| [Reference 2] | [Description] | [How to use] |

### Layout References
| Source | Pattern | Application |
|--------|---------|-------------|
| [Reference 1] | [Description] | [How to use] |
| [Reference 2] | [Description] | [How to use] |

### Component References
| Component | Reference | Notes |
|-----------|-----------|-------|
| Hero section | [Source] | [Notes] |
| Cards | [Source] | [Notes] |
| Navigation | [Source] | [Notes] |
| Footer | [Source] | [Notes] |

### Unique Elements to Consider
1. [Element 1 from Reference X]
2. [Element 2 from Reference Y]
3. [Element 3 from Reference Z]
```

---

## Example Input/Output
### Example Input

```markdown
**Project**: TaskFlow - SaaS project management for creative agencies
**Direction**: Modern, minimal, premium but approachable
**User Example**: "I like the look of Linear.app and the warmth of Notion"
```

### Example Output

```markdown

## Inspiration Moodboard: TaskFlow
### Search Strategy Used
1. Dribbble: "saas dashboard", "project management ui", "minimal dashboard"
2. Dribbble: "creative agency website", "modern web app"
3. Web: "best saas landing pages 2024", "linear app design"
4. Direct: Linear.app, Notion.so analysis

### Overall Visual Direction
Clean, sophisticated minimal design with subtle warmth. Emphasis on white 
space, precise typography, and functional elegance. Small delightful 
details (micro-interactions, subtle gradients) add personality without 
clutter. The aesthetic should feel premium and calm - a tool that reduces 
stress, not adds to it.

### Reference Analysis

#### Linear.app Analysis
**Colors**:
- Background: #FFFFFF, #F7F7F8
- Primary: #5E6AD2 (purple)
- Text: #1D1D1F, #6B6B6F
- Accents: Subtle gradients

**Typography**:
- Sans-serif throughout (Inter-like)
- Tight letter-spacing in headings
- Clean hierarchy with size contrast

**What to adapt**:
- Precision in spacing and alignment
- Subtle gradient accents
- Minimal but effective use of color
- Command palette aesthetic

#### Notion.so Analysis
**Colors**:
- Background: #FFFFFF
- Warm accents: Soft peach, tan
- Text: Near-black, gray levels

**Typography**:
- Mix of serif (headings) and sans-serif
- Friendly, readable

**What to adapt**:
- Warmth and approachability
- Playful illustrations
- Inviting empty states

### Color Direction (Combining References)
| Role | Color | Hex | Reference |
|------|-------|-----|----------|
| Background | White | #FFFFFF | Both |
| Surface | Light Gray | #F8F9FA | Linear |
| Primary | Warm Purple | #8B5CF6 | Linear+warm |
| Text Primary | Near Black | #1A1A1A | Linear |
| Text Secondary | Gray | #6B7280 | Both |
| Accent Warm | Soft Amber | #F59E0B | Notion warmth |

### Typography Direction
- Headings: Inter or Satoshi (geometric, modern)
- Body: Inter (proven readability)
- Consider: Slight warmth in weights, not too mechanical

### Layout Patterns to Follow
1. **Hero**: Large typography, subtle illustration, clear CTA (Linear style)
2. **Features**: Card grid with icons, generous padding
3. **Screenshots**: Floating with subtle shadow, perspective
4. **Pricing**: Simple table, highlight recommended

### Components to Design
| Component | Reference Style | Notes |
|-----------|-----------------|-------|
| Navigation | Linear - minimal, right-aligned CTA | |
| Hero | Linear + illustration warmth | |
| Feature cards | Notion - warm, icon-led | |
| Testimonials | Linear - minimal, photo + quote | |
| Footer | Simple, organized columns | |

### Unique Elements Worth Including
1. **Floating UI preview** (Linear style) - shows product without full screenshot
2. **Warm gradient accent** - subtle, adds life to minimal design
3. **Playful illustrations** (Notion style) - humanizes the product
4. **Keyboard shortcut hints** - appeals to power users

### Anti-patterns to Avoid
- Too cold/clinical (pure Linear without warmth)
- Too playful/casual (would undermine premium feel)
- Dense information (overwhelming for target audience)
- Generic stock photos (contradicts creative agency audience)
```

---

## Using the Reference Files

### When to Read Each Reference

**`./references/common-pitfalls.md`** — Read when you need detailed guidance on common pitfalls aspects of this skill.

**`./references/prompts-library.md`** — Read when you need detailed guidance on prompts library aspects of this skill.
