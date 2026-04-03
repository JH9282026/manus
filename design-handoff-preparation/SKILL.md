---
name: design-handoff-preparation
description: "Prepare developer-ready design deliverables with accurate specifications, assets, and implementation guidance. Use for: creating redline specifications, exporting design assets, generating CSS/token values, preparing icon sprite sheets, writing developer handoff notes, and ensuring seamless design-to-development transitions."
---

# Handoff Preparation

Prepare developer-ready design deliverables with accurate specifications, assets, and implementation guidance.

# Skill: Handoff Preparation

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Handoff Preparation |
| **Category** | Delivery |
| **Phase** | 6 - Delivery |
| **Estimated Time** | 30-60 minutes |
| **Dependencies** | `design_documentation.md`, score ≥9/10 |
| **Outputs** | Developer-ready design package |

## Description
Handoff Preparation creates a complete package for developers including exported assets, specifications, and implementation notes. This ensures smooth translation from design to code.

## When to Use
- Design is finalized (9/10+)
- Documentation is complete
- Ready to begin development
- For sprint planning
- When onboarding new developers

---

## Instructions for AI Agents
### Step 1: Handoff Checklist

**Pre-handoff validation:**

```markdown

## Handoff Readiness Checklist
### Design Quality
- [ ] Design score ≥9/10
- [ ] All screens complete
- [ ] All states designed
- [ ] Responsive versions ready
- [ ] Accessibility verified

### Documentation
- [ ] Design tokens documented
- [ ] Component specs complete
- [ ] Interaction specs defined
- [ ] Pattern guidelines written

### Assets
- [ ] Icons exported (SVG)
- [ ] Images optimized
- [ ] Illustrations prepared
- [ ] Logos in all formats

### Organization
- [ ] Files properly named
- [ ] Layers organized
- [ ] Styles linked to tokens
- [ ] Components properly structured
```

### Step 2: Asset Export

**Asset export specifications:**

```markdown

## Asset Export Guide
### Icons
| Format | Size | Usage |
|--------|------|-------|
| SVG | N/A (scalable) | Primary format |
| PNG @1x | 24px | Fallback |
| PNG @2x | 48px | Retina |
| PNG @3x | 72px | High-DPI |

**Naming Convention**: `icon-[name]-[size].svg`
Examples: `icon-home-24.svg`, `icon-search-20.svg`

### Images
| Format | Quality | Usage |
|--------|---------|-------|
| WebP | 80% | Primary (modern browsers) |
| JPEG | 80% | Fallback |
| PNG | N/A | Transparency needed |

**Naming Convention**: `[type]-[name]-[dimensions].webp`
Examples: `hero-dashboard-1920x1080.webp`, `avatar-placeholder-200x200.png`

### Size Requirements
| Context | Max Width | Max Size |
|---------|-----------|----------|
| Hero images | 1920px | 300KB |
| Card images | 800px | 100KB |
| Thumbnails | 400px | 50KB |
| Avatars | 200px | 30KB |

### Responsive Images
Export at multiple sizes:
- Small: 640px width
- Medium: 1024px width
- Large: 1920px width
```

### Step 3: Implementation Notes

**Developer notes template:**

```markdown

## Implementation Notes
### Priority Order

1. **Phase 1: Foundation** (Week 1)
   - Set up design tokens
   - Configure typography
   - Implement color system
   - Set up spacing scale

2. **Phase 2: Components** (Week 2-3)
   - Build base components
   - Implement states
   - Add accessibility
   - Component testing

3. **Phase 3: Pages** (Week 3-4)
   - Implement layouts
   - Build page templates
   - Responsive testing
   - Cross-browser testing

### Technical Considerations

#### CSS Architecture
- Use CSS custom properties for tokens
- Component-scoped styles
- Mobile-first media queries
- BEM or CSS Modules naming

#### Animation Performance
- Use `transform` and `opacity` only
- Add `will-change` for animated elements
- Respect `prefers-reduced-motion`
- Keep durations under 400ms

#### Accessibility Implementation
- Semantic HTML elements
- ARIA attributes where needed
- Focus management for modals
- Keyboard navigation support

### Known Challenges

| Challenge | Recommendation |
|-----------|---------------|
| [Challenge 1] | [Solution approach] |
| [Challenge 2] | [Solution approach] |

### Questions for Developer

1. [Technical question about implementation]
2. [Framework-specific question]
3. [Performance consideration]
```

### Step 4: Handoff Package Structure

**File organization:**

```markdown

## Handoff Package Structure
```
project-handoff/
├── README.md              # Overview and getting started
├── CHANGELOG.md           # Design version history
│
├── documentation/
│   ├── design-system.md   # Full design system doc
│   ├── components/        # Component specifications
│   │   ├── button.md
│   │   ├── input.md
│   │   └── ...
│   ├── patterns/          # UI patterns
│   └── accessibility.md   # A11y guidelines
│
├── tokens/
│   ├── tokens.json        # Design tokens (JSON)
│   ├── tokens.css         # CSS custom properties
│   ├── tokens.scss        # Sass variables
│   └── tokens.js          # JS constants
│
├── assets/
│   ├── icons/             # SVG icons
│   ├── images/            # Optimized images
│   ├── illustrations/     # Illustration files
│   └── logos/             # Logo variations
│
├── mockups/
│   ├── desktop/           # Desktop screenshots
│   ├── tablet/            # Tablet screenshots
│   └── mobile/            # Mobile screenshots
│
└── source/
    └── [design-tool-files] # Figma links, Sketch files, etc.
```
```

### Step 5: Create README

```markdown
# [Project] Design Handoff

## Quick Start
1. Review `documentation/design-system.md` for full specifications
2. Import tokens from `tokens/tokens.css` into your project
3. Reference component specs in `documentation/components/`
4. Find all assets in `assets/` directory

## Design File Access
- **Figma**: [Link to Figma file]
- **View-only mode**: [Link]
- **Developer mode**: Enabled for measurements

## Token Usage
```css
/* Import tokens */
@import 'tokens/tokens.css';

/* Use in CSS */
.button {
  background: var(--color-primary-500);
  padding: var(--spacing-2) var(--spacing-4);
  border-radius: var(--radius-md);
}
```

## Key Screens
| Screen | Desktop | Mobile | Status |
|--------|---------|--------|--------|
| Dashboard | ✅ | ✅ | Complete |
| Project List | ✅ | ✅ | Complete |
| Task Detail | ✅ | ✅ | Complete |
| Settings | ✅ | ✅ | Complete |

## Questions?
Contact: [Designer contact]
Figma comments: Enabled for questions

## Version History
| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [Date] | Initial handoff |
```

---

## Example Output
### Handoff Summary Document

```markdown
# TaskFlow Design Handoff Summary

## Overview
**Design Score**: 9.2/10
**Handoff Date**: [Date]
**Designer**: [Name]
**Developer Contact**: [Name]

---

## Technical Notes
### Recommended Stack
- CSS: Tailwind CSS or CSS Modules
- Icons: Import as React components
- Animations: Framer Motion or CSS transitions

### Performance Budget
- First Contentful Paint: <1.5s
- Largest Contentful Paint: <2.5s
- Total image payload: <1MB

### Browser Support
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

---

## Using the Reference Files

### When to Read Each Reference

**`./references/communication.md`** — Read when you need detailed guidance on communication aspects of this skill.

**`./references/related-skills.md`** — Read when you need detailed guidance on related skills aspects of this skill.

**`./references/whats-included.md`** — Read when you need detailed guidance on whats included aspects of this skill.
