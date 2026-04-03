---
name: information-architecture-design
description: "Structure content and navigation systems to create intuitive information hierarchies. Use for: organizing site maps, designing navigation patterns, structuring content taxonomies, planning menu systems, labeling strategies, and creating findable content architectures for websites and applications."
---

# Information Architecture

Structure content and navigation systems to create intuitive information hierarchies.

# Skill: Information Architecture

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Information Architecture |
| **Category** | UX Foundation |
| **Phase** | 2 - UX Foundation |
| **Estimated Time** | 30-45 minutes |
| **Dependencies** | `user_personas.md`, `user_flows.md` |
| **Outputs** | Site map, navigation structure, content hierarchy |

## Description
Information Architecture (IA) is the structural design of information environments. It involves organizing, labeling, and structuring content so users can find what they need efficiently. Good IA is invisible – users simply find what they expect where they expect it.

## When to Use
- Designing a new website or app structure
- Reorganizing existing navigation
- Planning content strategy
- Before wireframing to establish structure
- When users report difficulty finding content

---

## Instructions for AI Agents
### Step 1: Content Inventory

**Prompt to identify content:**
```
For [PRODUCT/WEBSITE], list all content and features needed:

1. **Pages/Screens**: All unique views users need
2. **Features**: Interactive functionality
3. **Content Types**: Articles, products, user data, etc.
4. **User Actions**: Things users can do
5. **System Info**: Settings, account, help, etc.

Group these into logical categories.
```

### Step 2: Create Site Map

**Site map template:**

```markdown

## Site Map: [PRODUCT]
### Primary Navigation (Always Visible)

```
[PRODUCT]
│
├── Home / Dashboard
│
├── [Section 1]
│   ├── [Subsection 1.1]
│   ├── [Subsection 1.2]
│   └── [Subsection 1.3]
│
├── [Section 2]
│   ├── [Subsection 2.1]
│   └── [Subsection 2.2]
│
├── [Section 3]
│
└── [Section 4]
```

### Secondary Navigation (User Menu / Footer)

```
[User Menu]
├── Account Settings
├── Billing
├── Team Management
└── Log Out

[Footer]
├── About
├── Privacy Policy
├── Terms of Service
└── Contact
```
```

### Step 3: Define Navigation Patterns

**Navigation types to consider:**

| Type | Best For | Example |
|------|----------|--------|
| Top Bar | Primary nav, 4-7 items | Main sections |
| Side Bar | Deep navigation, many items | Dashboard apps |
| Tab Bar | Mobile, 3-5 items | Mobile app main nav |
| Hamburger | Secondary items, mobile overflow | Settings, account |
| Breadcrumbs | Deep hierarchies | E-commerce categories |
| Search | Large content libraries | Documentation, products |

### Step 4: Label Strategy

**Naming principles:**

```markdown

## Navigation Labels
### Principles
1. **User language**: Use words users know, not internal jargon
2. **Specific over generic**: "Pricing" not "Information"
3. **Consistent verb form**: All actions or all nouns
4. **Scannable**: Front-load important words

### Label Audit

| Current Label | User Language | Final Label | Notes |
|---------------|---------------|-------------|-------|
| [Label 1] | [How users say it] | [Final] | [Why] |
```

### Step 5: Content Grouping

**Card sorting simulation prompt:**
```
Imagine [PERSONA] is looking for [CONTENT/FEATURE].
Where would they expect to find it?

Test these groupings:
- Would [Item A] and [Item B] logically be together?
- If looking for [Item C], would they check [Section X]?
- What label best describes [Group of items]?
```

---

## Example Input/Output
### Example Input

```markdown
**Product**: TaskFlow - Project management for creative agencies
**Key Features**: Projects, tasks, team, clients, time tracking, reports
**Personas**: Creative Director, Project Manager, Designer
```

### Example Output

```markdown

## Prompts Library
### Quick IA Generation
```
Create an information architecture for [PRODUCT TYPE] with these features:
[FEATURE LIST]

Include:
1. Site map (tree structure)
2. Primary navigation items (max 7)
3. Secondary navigation (user menu)
4. Mobile navigation strategy
```

### Navigation Audit
```
Review this navigation structure:
[CURRENT NAV]

Evaluate:
1. Is anything missing users would expect?
2. Are items grouped logically?
3. Are labels clear and consistent?
4. Is the depth appropriate (rule of 3 clicks)?
5. Suggested improvements?
```

### Content Hierarchy
```
For [CONTENT TYPE], define the information hierarchy:

1. What's the most important info to show first?
2. What's secondary but still on first view?
3. What can be in "show more" or secondary views?
4. What's rarely needed (settings, advanced)?
```

---

## Success Criteria
### Minimum Requirements
- [ ] Site map covering all content
- [ ] Primary navigation defined (max 7 items)
- [ ] Secondary navigation planned
- [ ] Mobile navigation strategy
- [ ] Clear, consistent labels

### Quality Indicators
- [ ] Any content findable in 3 clicks or less
- [ ] Labels pass the "5-second test" (instantly understood)
- [ ] Navigation serves all personas
- [ ] Consistent patterns throughout
- [ ] Room for future growth

---

## Related Skills
- **Previous**: `user_flows.md` - Understand user journeys
- **Next**: `wireframing.md` - Apply IA to screen layouts
- **Related**: `layout_grids.md` - Grid structure for navigation

## Using the Reference Files

### When to Read Each Reference

**`./references/information-architecture-taskflow.md`** — Read when you need detailed guidance on information architecture taskflow aspects of this skill.
