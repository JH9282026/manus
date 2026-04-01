---
name: competitive-analysis
description: "Analyze competitor designs, features, and user experiences to identify opportunities and best practices. Use for: market research, competitor benchmarking, feature comparison, identifying design gaps, and understanding industry standards."
---

# Competitive Analysis

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

## Competitive Design Analysis: TaskFlow

### Competitors Analyzed

| Type | Company | URL | Relevance |
|------|---------|-----|------------|
| Direct | Monday.com | monday.com | Market leader, visual approach |
| Direct | Asana | asana.com | Enterprise-focused competitor |
| Direct | Notion | notion.so | Creative/startup favorite |
| Indirect | Linear | linear.app | Premium SaaS benchmark |
| Aspirational | Stripe | stripe.com | Gold standard SaaS design |

---

### Detailed Analysis

#### Monday.com

**Brand & Tone**: Energetic, colorful, approachable, slightly playful

**Colors**:
- Primary: Multiple bright colors (brand rainbow)
- Heavy use of gradients
- White backgrounds with colorful accents
- Can feel overwhelming

**Typography**:
- Poppins for headings (rounded, friendly)
- Clean sans-serif body
- Good hierarchy but busy

**Layout**:
- Dense with many elements
- Heavy use of illustrations and graphics
- Floating product screenshots
- Lots of social proof

**Strengths**:
- Memorable brand colors
- Clear feature communication
- Effective use of animation

**Weaknesses**:
- Can feel visually overwhelming
- Not "premium" feeling
- Busy layout may not suit focused users

---

#### Asana

**Brand & Tone**: Professional, established, slightly corporate

**Colors**:
- Primary: Coral/salmon (#F06A6A)
- Purple secondary
- Clean white backgrounds
- More muted than Monday

**Typography**:
- Clean sans-serif throughout
- Professional hierarchy
- Good readability

**Layout**:
- More spacious than Monday
- Clear sections
- Professional photography

**Strengths**:
- Professional credibility
- Clear information hierarchy
- Enterprise-appropriate

**Weaknesses**:
- Can feel somewhat cold
- Less personality than others
- Photography feels generic

---

#### Notion

**Brand & Tone**: Warm, friendly, creative, flexible

**Colors**:
- Minimal palette: black, white, beige/cream accents
- Warm neutral tones
- Soft, inviting

**Typography**:
- Mix of serif (marketing) and sans-serif (UI)
- Friendly and readable
- Good personality

**Layout**:
- Very spacious
- Generous whitespace
- Playful illustrations
- Template-focused showcasing

**Strengths**:
- Strong personality
- Feels creative and flexible
- Illustrations are memorable
- Appeals to creative users

**Weaknesses**:
- Can seem too casual for enterprise
- Template-heavy may not show all features
- "All-in-one" positioning can confuse

---

#### Linear (Aspirational)

**Brand & Tone**: Premium, precise, developer-focused, minimal

**Colors**:
- Purple primary (#5E6AD2)
- Dark mode emphasis
- Subtle gradients
- Extremely refined palette

**Typography**:
- Inter or custom sans-serif
- Tight tracking on headings
- Minimalist hierarchy

**Layout**:
- Extremely clean
- Generous whitespace
- Product-focused
- No clutter

**Strengths**:
- Premium feel unmatched
- Focus and simplicity
- Appeals to discerning users
- Unique visual language

**Weaknesses**:
- Could feel cold to some
- Not warm or approachable
- Assumes technical audience

---

### Comparison Matrix

| Aspect | Monday | Asana | Notion | Linear | Opportunity |
|--------|--------|-------|--------|--------|-------------|
| Primary Color | Rainbow | Coral | Black | Purple | Warm purple - premium but approachable |
| Visual Density | High | Medium | Low | Very Low | Low-medium: clean but informative |
| Personality | Playful | Corporate | Creative | Precise | Creative + Premium |
| Imagery | Illustrations | Photos | Illustrations | Product UI | Custom illustrations + product |
| Whitespace | Limited | Moderate | Generous | Extensive | Generous - breathing room |
| Target Feel | Fun | Professional | Flexible | Expert | Capable + Welcoming |

---

### Key Patterns & Opportunities

#### Industry Conventions (Follow)
1. **Navigation**: Top nav with clear CTA (Sign up/Try free)
2. **Hero**: Bold headline + product visual + CTA
3. **Social proof**: Logos, testimonials, user counts
4. **Feature sections**: Clear benefit-focused messaging
5. **Pricing page**: Comparison table format

#### Common Approaches (Evaluate)
1. **Heavy illustration use** - Could differentiate with restraint
2. **Product screenshots everywhere** - Could be more selective
3. **Feature overload** - Could focus on fewer, better presented

#### White Space Opportunities (Differentiate)

1. **Premium minimalism + warmth**
   - Gap: Monday/Asana aren't premium; Linear isn't warm; Notion isn't SaaS-feeling
   - Opportunity: Linear's precision + Notion's warmth

2. **Creative agency specific**
   - Gap: All are general-purpose tools
   - Opportunity: Design for creative workflow specifically

3. **Calm aesthetic**
   - Gap: Most competitors are visually busy or cold
   - Opportunity: "The calm project management tool"

4. **Interaction quality**
   - Gap: Most have standard interactions
   - Opportunity: Delightful micro-interactions like Linear

---

### Differentiation Strategy for TaskFlow

#### Where to Conform
1. **Top navigation structure**: Expected pattern, don't innovate here
2. **Hero section format**: Proven effective, adapt don't reinvent
3. **Pricing table format**: Users expect comparability
4. **CTA button prominence**: Essential for conversion

#### Where to Differentiate

1. **Color: Warm premium purple**
   - Competitors: Bright/corporate (Monday/Asana) or minimal (Notion/Linear)
   - Our approach: Purple (#8B5CF6) with warm amber accents
   - Why: Premium feel with creative warmth, unclaimed territory

2. **Density: Intentional breathing room**
   - Competitors: Busy (Monday) or very minimal (Linear)
   - Our approach: Generous whitespace but informative
   - Why: Respects creative professionals' aesthetic sensibilities

3. **Personality: Creative professional**
   - Competitors: Playful OR corporate OR tech-focused
   - Our approach: Sophisticated but friendly
   - Why: Matches creative agency culture

4. **Imagery: Curated custom illustration + real product**
   - Competitors: Generic illustrations or none
   - Our approach: Custom illustrations that feel creative, real product UI
   - Why: Appeals to design-savvy audience

#### Signature Elements

1. **Warm gradient accents**: Subtle purple-to-amber gradients as signature
2. **Creative tool aesthetic**: UI elements that feel like creative software
3. **Animation quality**: Smooth, purposeful micro-interactions
4. **Agency-specific visuals**: Imagery of creative work, not generic business
```

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

**`/references/example_input_output.md`** — Read when you need detailed example input/output.

**`/references/prompts_library.md`** — Read when you need detailed prompts library.

**`/references/resources.md`** — Read when you need detailed resources.

## References

- [Example Input Output](references/example_input_output.md)
- [Prompts Library](references/prompts_library.md)
- [Resources](references/resources.md)
