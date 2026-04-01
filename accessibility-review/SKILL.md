---
name: accessibility-review
description: "Review and improve design accessibility for WCAG compliance, screen readers, keyboard navigation, and inclusive design. Use for: accessibility audits, WCAG compliance checks, inclusive design reviews, disability accommodation, and ensuring designs work for all users."
---

# Accessibility Review

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
## Accessibility Audit: TaskFlow

**Standard**: WCAG 2.1 AA
**Overall Status**: ⚠️ Partially Compliant (3 issues to fix)

---

### Color Contrast Audit

#### Text Combinations

| Foreground | Background | Ratio | Required | Status |
|------------|------------|-------|----------|--------|
| Slate-900 #0F172A | White | 15.3:1 | 4.5:1 | ✅ Pass |
| Slate-700 #334155 | White | 8.6:1 | 4.5:1 | ✅ Pass |
| Slate-500 #64748B | White | 4.6:1 | 4.5:1 | ✅ Pass |
| Slate-400 #94A3B8 | White | 2.9:1 | 4.5:1 | ❌ **Fail** |
| White | Violet-500 #8B5CF6 | 4.9:1 | 4.5:1 | ✅ Pass |
| White | Amber-500 #F59E0B | 2.1:1 | 4.5:1 | ❌ **Fail** |

#### Issues Found

1. **Slate-400 placeholder text** fails at 2.9:1
   - Current: #94A3B8 on white
   - Fix: Use Slate-500 #64748B for placeholders
   - Impact: Low (placeholder only)

2. **White on Amber buttons** fails at 2.1:1
   - Current: White text on Amber-500
   - Fix: Use Slate-900 text on Amber buttons
   - Impact: Medium (affects warning buttons)

---

### Keyboard Navigation Audit

#### Focus Management: ✅ Good

| Check | Status | Notes |
|-------|--------|-------|
| All elements focusable | ✅ | |
| Logical focus order | ✅ | |
| Focus visible | ⚠️ | Needs enhancement |
| Modal focus trap | ✅ | |
| Focus return | ✅ | |

#### Focus Indicator Issue

**Current**: Default browser outline (inconsistent, sometimes invisible)
**Required**: Visible focus indicator with 3:1 contrast

**Recommended Fix**:
```css
:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px var(--violet-200);
}
```

---

### Touch Target Audit

| Element | Size | Required | Status |
|---------|------|----------|--------|
| Primary button | 40×H | 44px | ✅ |
| Small button | 32×H | 44px | ❌ **Fail** |
| Checkbox | 18×18 | 44px | ❌ **Fail** (visual) |
| Checkbox tap area | 44×44 | 44px | ✅ (if padded) |
| Nav item | 40×40 | 44px | ⚠️ Marginal |
| Close button | 24×24 | 44px | ❌ **Fail** |

#### Issues Found

1. **Small buttons** visual size 32px
   - Fix: Increase to 36px minimum, ensure 44px tap area with padding

2. **Modal close button** only 24px
   - Fix: Increase to 44px tap target (can keep visual at 24px with padding)

---

### Screen Reader Considerations

| Check | Status | Notes |
|-------|--------|-------|
| Heading hierarchy | ✅ | h1 → h2 → h3 correct |
| Landmarks | ⚠️ | Need main, nav defined |
| Alt text strategy | ✅ | Documented |
| Form labels | ✅ | All inputs labeled |
| Error announcements | ⚠️ | Need aria-live regions |

---

### Additional Checks

| Check | Status | Notes |
|-------|--------|-------|
| Reduced motion | ❌ | Not implemented |
| Color independence | ✅ | Icons accompany colors |
| Text resize 200% | ✅ | Layout holds |
| Max line width | ✅ | 75 characters |

---

### Summary

#### ❌ Must Fix (3 issues)

1. **Slate-400 contrast**: Change placeholder text to Slate-500
2. **Amber button text**: Use dark text on Amber backgrounds
3. **Reduced motion**: Add @media query support

#### ⚠️ Should Fix (4 issues)

1. **Focus states**: Enhance visibility with consistent style
2. **Touch targets**: Ensure all targets ≥44px
3. **Landmarks**: Add role="main", role="navigation"
4. **Error announcements**: Add aria-live regions

#### ✅ Compliant

- Text contrast (primary combinations)
- Keyboard navigation flow
- Heading structure
- Form labeling
- Color independence
- Text resizing

---

### Recommended Fixes

```css
/* 1. Fix placeholder contrast */
::placeholder {
  color: #64748B; /* Slate-500 */
}

/* 2. Amber button text */
.btn-amber {
  color: #0F172A; /* Slate-900 */
}

/* 3. Reduced motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.001ms !important;
    transition-duration: 0.001ms !important;
  }
}

/* 4. Focus states */
:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px #DDD6FE;
}

/* 5. Touch target padding */
.icon-button {
  padding: 10px;
  /* Visual: 24px icon, Total: 44px */
}
```

---

### Compliance Status

| Level | Status |
|-------|--------|
| WCAG 2.1 A | ✅ Pass |
| WCAG 2.1 AA | ⚠️ Pass after fixes |
| WCAG 2.1 AAA | ❌ Not targeted |
```

---

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

- [./references/accessibility-audit-process.md](./references/accessibility-audit-process.md): Accessibility Audit Process
- [./references/aria-best-practices.md](./references/aria-best-practices.md): Aria Best Practices
- [./references/assistive-technology-testing.md](./references/assistive-technology-testing.md): Assistive Technology Testing
- [./references/wcag-compliance-standards.md](./references/wcag-compliance-standards.md): Wcag Compliance Standards
