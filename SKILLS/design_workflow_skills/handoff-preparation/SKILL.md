---
name: handoff-preparation
description: "Prepare design files, assets, and documentation for smooth handoff to development teams. Use for: developer handoff, asset export, design file organization, creating redlines, and ensuring implementation accuracy."
---

# Handoff Preparation

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

## What's Included

### Documentation
- [x] Design system documentation (100+ pages)
- [x] Component specifications (15 components)
- [x] Pattern library (8 patterns)
- [x] Accessibility guidelines

### Design Tokens
- [x] Colors (primary, neutral, semantic)
- [x] Typography (10 styles)
- [x] Spacing (12 steps)
- [x] Effects (shadows, radii, transitions)

### Assets
- [x] 48 icons (SVG)
- [x] 12 illustrations (SVG)
- [x] Placeholder images
- [x] Logo files (4 variations)

### Screens
- [x] Dashboard (desktop, tablet, mobile)
- [x] Project views (4 screens)
- [x] Task management (3 screens)
- [x] Settings (2 screens)
- [x] Empty states (4 variations)
- [x] Error states (3 variations)

---

## Implementation Priority

### Sprint 1: Foundation
- [ ] Set up design tokens
- [ ] Typography styles
- [ ] Color system
- [ ] Base layout (grid, container)

### Sprint 2: Core Components
- [ ] Buttons (all variants)
- [ ] Form inputs
- [ ] Cards
- [ ] Navigation

### Sprint 3: Features
- [ ] Dashboard layout
- [ ] Task list/detail
- [ ] Project views

### Sprint 4: Polish
- [ ] Animations/transitions
- [ ] Empty states
- [ ] Error handling
- [ ] Mobile refinement

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

## Files Delivered

| File | Format | Location |
|------|--------|----------|
| Design tokens | JSON, CSS, SCSS | `/tokens/` |
| Icons | SVG | `/assets/icons/` |
| Illustrations | SVG | `/assets/illustrations/` |
| Component docs | Markdown | `/documentation/components/` |
| Screen mockups | PNG | `/mockups/` |
| Figma file | Link | [URL] |

---

## Communication

**For Questions**:
- Comment in Figma (design questions)
- Slack: #project-taskflow (general)
- Email: [designer@email.com] (urgent)

**Review Process**:
1. Developer implements component
2. Designer reviews in staging
3. Feedback via Figma comments
4. Iterate until approved

---

## Sign-off

Design handoff is complete and ready for development.

- [ ] Designer: [Name] - [Date]
- [ ] Developer: [Name] - [Date]
- [ ] PM: [Name] - [Date]
```

---

## Success Criteria

### Minimum Requirements
- [ ] All assets exported and organized
- [ ] Tokens in usable format
- [ ] Documentation accessible
- [ ] Implementation notes provided

### Quality Indicators
- [ ] Developers can start without questions
- [ ] Assets properly optimized
- [ ] Clear priority order
- [ ] Handoff package complete

---

## Related Skills

- **Previous**: `design_documentation.md` - Create specs first
- **Related**: All design skills contribute to handoff
- **Next**: Development begins!

---

## Handoff Complete 🎉

Congratulations! Your design workflow is complete:

1. ✅ Research & Inspiration
2. ✅ UX Foundation
3. ✅ Visual Design
4. ✅ Responsive & Platform
5. ✅ Review & Iteration (9/10+ achieved)
6. ✅ Delivery

The design is now ready for implementation!
