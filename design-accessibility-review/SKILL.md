---
name: design-accessibility-review
description: "Evaluate designs for WCAG compliance and inclusive design principles to ensure accessibility for all users. Use for: checking color contrast ratios, verifying keyboard navigation, auditing screen reader compatibility, testing touch target sizes, evaluating cognitive accessibility, and creating VPAT documentation for design deliverables."
---

# Accessibility Review

Evaluate designs for WCAG compliance and inclusive design principles to ensure accessibility for all users.

# Skill: Accessibility Review

## Overview
| Attribute | Value |
|-----------|-------|
| **Skill Name** | Accessibility Review |
| **Category** | Review & Iteration |
| **Phase** | 5 - Review & Iteration |
| **Estimated Time** | 30-45 minutes |
| **Dependencies** | `component_design.md`, `color_palettes.md` |
| **Outputs** | Accessibility audit report with compliance status |

## Description
Accessibility Review ensures designs meet WCAG guidelines and are usable by people with disabilities. This includes checking color contrast, keyboard navigation, screen reader compatibility, and more.

## When to Use
- During design review phase
- Before development handoff
- When accessibility is a project requirement
- To meet legal/compliance standards
- As part of quality assurance

**Target**: WCAG 2.1 AA compliance (minimum)

---

## Instructions for AI Agents
### Step 1: Color Contrast Check

**WCAG contrast requirements:**

| Text Type | Minimum Ratio | WCAG Level |
|-----------|---------------|------------|
| Normal text (<18px) | 4.5:1 | AA |
| Large text (≥18px bold, ≥24px) | 3:1 | AA |
| UI components & graphics | 3:1 | AA |
| Normal text | 7:1 | AAA |
| Large text | 4.5:1 | AAA |

**Audit template:**

```markdown

## Color Contrast Audit
### Text Combinations

| Foreground | Background | Ratio | Size | Required | Pass? |
|------------|------------|-------|------|----------|-------|
| [Color] | [Color] | [X:1] | Body | 4.5:1 | ✅/❌ |
| [Color] | [Color] | [X:1] | Heading | 3:1 | ✅/❌ |
| [Color] | [Color] | [X:1] | Caption | 4.5:1 | ✅/❌ |

### Interactive Elements

| Element | State | Foreground | Background | Ratio | Pass? |
|---------|-------|------------|------------|-------|-------|
| Button | Default | | | | |
| Button | Hover | | | | |
| Button | Disabled | | | | |
| Link | Default | | | | |
| Input | Focus | | | | |

### Issues Found

1. **[Issue]**: [Color combo] fails with [ratio]
   - Fix: [Recommended color adjustment]
```

### Step 2: Keyboard Navigation

**Keyboard accessibility checklist:**

```markdown

## Keyboard Navigation Audit
### Focus Management

- [ ] All interactive elements focusable via Tab
- [ ] Focus order is logical (left-to-right, top-to-bottom)
- [ ] Focus visible on all elements
- [ ] Focus trapped appropriately in modals
- [ ] Focus returned after modal closes

### Focus Indicators

| Element | Focus Style | Visible? | Contrast? |
|---------|-------------|----------|----------|
| Button | [Style] | ✅/❌ | ✅/❌ |
| Link | [Style] | ✅/❌ | ✅/❌ |
| Input | [Style] | ✅/❌ | ✅/❌ |
| Card (if clickable) | [Style] | ✅/❌ | ✅/❌ |
| Nav item | [Style] | ✅/❌ | ✅/❌ |

### Keyboard Interactions

| Component | Expected Keys | Designed? |
|-----------|--------------|----------|
| Button | Enter, Space | ✅/❌ |
| Link | Enter | ✅/❌ |
| Dropdown | Arrow keys, Enter, Esc | ✅/❌ |
| Modal | Esc to close, Tab trapped | ✅/❌ |
| Tabs | Arrow keys between tabs | ✅/❌ |
| Checkbox | Space | ✅/❌ |
```

### Step 3: Touch Target Size

**Minimum touch targets:**

| Platform | Minimum Size | Recommended |
|----------|--------------|-------------|
| iOS | 44×44pt | 48×48pt |
| Android | 48×48dp | 48×48dp |
| WCAG 2.2 | 24×24px | 44×44px |

**Audit template:**

```markdown

## Touch Target Audit
| Element | Current Size | Platform Min | Pass? | Fix |
|---------|--------------|--------------|-------|-----|
| Button (sm) | [size] | 44px | ✅/❌ | |
| Checkbox | [size] | 44px | ✅/❌ | |
| Link | [size] | 44px | ✅/❌ | |
| Close button | [size] | 44px | ✅/❌ | |
| Nav item | [size] | 44px | ✅/❌ | |
```

### Step 4: Screen Reader Considerations

**Design checklist for screen readers:**

```markdown

## Screen Reader Compatibility
### Content Structure

- [ ] Heading hierarchy logical (h1 → h2 → h3)
- [ ] Landmarks defined (main, nav, header, footer)
- [ ] Lists used for list content
- [ ] Tables have headers defined

### Images & Icons

| Image Type | Alt Text Strategy | Example |
|------------|-------------------|----------|
| Decorative | Empty alt="" | Background patterns |
| Informative | Descriptive text | Photos, charts |
| Functional | Action description | "Search", "Close" |
| Icons (with label) | aria-hidden="true" | Button with icon+text |
| Icons (alone) | aria-label="[action]" | Icon-only button |

### Dynamic Content

- [ ] Loading states announced (aria-live)
- [ ] Error messages linked to inputs
- [ ] Form validation announced
- [ ] Modal focus announced

### Forms

| Field | Label | Error Handling | Required Indicator |
|-------|-------|----------------|-------------------|
| [Field 1] | Visible label | aria-describedby | aria-required |
```

### Step 5: Additional Checks

```markdown

## Additional Accessibility Checks
### Motion & Animation

- [ ] Animations respect prefers-reduced-motion
- [ ] No flashing content (3 flashes/second max)
- [ ] Essential animations have alternatives
- [ ] Auto-playing content can be paused

### Color Independence

- [ ] Information not conveyed by color alone
- [ ] Error states have icon + color
- [ ] Links distinguishable (underline or icon)
- [ ] Charts have patterns, not just colors

### Text & Readability

- [ ] Text resizable to 200% without breaking
- [ ] Line height at least 1.5 for body
- [ ] Paragraph width max 80 characters
- [ ] Text not fully justified

### Interactive Elements

- [ ] Error identification: Clear what's wrong
- [ ] Error suggestion: Help fixing errors
- [ ] Consistent navigation across pages
- [ ] Consistent identification of UI elements
```

---

## Example Input/Output
### Example Input

```markdown
**Design**: TaskFlow Dashboard
**Target**: WCAG 2.1 AA
**Key areas**: Color system, interactive components
```

### Example Output

```markdown

## Resources
### Testing Tools
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- axe DevTools: https://deque.com/axe/
- WAVE: https://wave.webaim.org
- Stark (Figma plugin): https://getstark.co

### Guidelines
- WCAG 2.1: https://www.w3.org/WAI/WCAG21/quickref/
- A11y Project Checklist: https://a11yproject.com/checklist/

---

## Success Criteria
### Minimum Requirements
- [ ] WCAG 2.1 AA compliance
- [ ] All contrast ratios pass
- [ ] Keyboard navigation works
- [ ] Touch targets adequate

### Quality Indicators
- [ ] Exceeds minimums where possible
- [ ] Clear documentation for developers
- [ ] Reduced motion supported
- [ ] Screen reader tested

---

## Related Skills
- **Previous**: `color_palettes.md` - Define accessible colors from start
- **Related**: `design_review.md` - Include accessibility in review
- **Next**: `design_iteration.md` - Fix accessibility issues

## Using the Reference Files

### When to Read Each Reference

**`./references/accessibility-audit-taskflow.md`** — Read when you need detailed guidance on accessibility audit taskflow aspects of this skill.
