---
name: accessibility-wcag
description: "Design and develop accessible digital products following WCAG 2.2 and ARIA standards. Use for implementing accessibility requirements, conducting WCAG audits, remediating accessibility issues, building inclusive user interfaces, ensuring keyboard navigation, managing screen reader compatibility, creating accessible forms and interactive components, meeting legal compliance requirements (ADA, Section 508), and establishing accessibility testing workflows."
---

# Accessibility & WCAG Compliance

Design and develop inclusive digital experiences that meet WCAG 2.2 standards and serve users of all abilities.

## Overview

Web accessibility ensures that digital products are usable by people with disabilities, including visual, auditory, motor, and cognitive impairments. The Web Content Accessibility Guidelines (WCAG) provide a comprehensive framework for creating accessible content. This skill covers WCAG 2.2 compliance, ARIA implementation, accessibility testing methodologies, remediation strategies, and legal compliance requirements. It emphasizes practical implementation patterns, automated testing integration, and building accessibility into the design and development process from the start.

## WCAG 2.2 Principles & Levels

WCAG is organized around four core principles (POUR) with three conformance levels:

| Principle | Focus | Key Requirements |
|-----------|-------|------------------|
| **Perceivable** | Information must be presentable to users | Text alternatives, captions, adaptable content, distinguishable elements |
| **Operable** | Interface components must be usable | Keyboard access, sufficient time, seizure prevention, navigable |
| **Understandable** | Information and operation must be clear | Readable text, predictable behavior, input assistance |
| **Robust** | Content must work with assistive technologies | Valid markup, name/role/value for components |

### Conformance Levels

**Level A (Minimum)** — Essential accessibility features
- Required for: Basic legal compliance
- Examples: Alt text for images, keyboard navigation, form labels
- Impact: Addresses major barriers but insufficient for full accessibility

**Level AA (Standard)** — Recommended target for most organizations
- Required for: ADA compliance, Section 508, most legal requirements
- Examples: 4.5:1 color contrast, resize text to 200%, consistent navigation
- Impact: Addresses most common barriers, industry standard

**Level AAA (Enhanced)** — Highest level of accessibility
- Required for: Specialized contexts (government, healthcare, education)
- Examples: 7:1 color contrast, sign language interpretation, reading level
- Impact: Maximum accessibility but not always achievable for all content

### WCAG 2.2 New Success Criteria (2023)

**2.4.11 Focus Not Obscured (Minimum)** [AA] — Focused elements must be at least partially visible
**2.4.12 Focus Not Obscured (Enhanced)** [AAA] — Focused elements must be fully visible
**2.4.13 Focus Appearance** [AAA] — Focus indicators must meet minimum size and contrast
**2.5.7 Dragging Movements** [AA] — Provide alternatives to dragging interactions
**2.5.8 Target Size (Minimum)** [AA] — Interactive targets at least 24×24 CSS pixels
**3.2.6 Consistent Help** [A] — Help mechanisms in consistent locations
**3.3.7 Redundant Entry** [A] — Don't require re-entering information
**3.3.8 Accessible Authentication (Minimum)** [AA] — Don't require cognitive function tests
**3.3.9 Accessible Authentication (Enhanced)** [AAA] — No cognitive function tests for authentication

## ARIA Implementation Patterns

Accessible Rich Internet Applications (ARIA) extends HTML semantics for complex interactive components.

### ARIA Roles, States, and Properties

**Landmark Roles** — Define page structure for screen readers
```html
<header role="banner">
<nav role="navigation" aria-label="Main navigation">
<main role="main">
<aside role="complementary">
<footer role="contentinfo">
```

**Widget Roles** — Define interactive components
```html
<div role="button" tabindex="0" aria-pressed="false">
<div role="tab" aria-selected="true" aria-controls="panel-1">
<div role="dialog" aria-labelledby="dialog-title" aria-modal="true">
<div role="alert" aria-live="assertive">
```

**States and Properties** — Communicate component status
```html
aria-expanded="true"          <!-- Disclosure state -->
aria-checked="mixed"          <!-- Checkbox state -->
aria-disabled="true"          <!-- Disabled state -->
aria-hidden="true"            <!-- Hidden from screen readers -->
aria-label="Close dialog"    <!-- Accessible name -->
aria-describedby="help-text" <!-- Additional description -->
aria-live="polite"            <!-- Dynamic content updates -->
aria-atomic="true"            <!-- Announce entire region -->
```

### Common ARIA Patterns

**Accessible Modal Dialog**
```html
<div role="dialog" 
     aria-labelledby="dialog-title" 
     aria-describedby="dialog-desc"
     aria-modal="true">
  <h2 id="dialog-title">Confirm Action</h2>
  <p id="dialog-desc">Are you sure you want to delete this item?</p>
  <button>Cancel</button>
  <button>Delete</button>
</div>
```

**Accessible Tab Interface**
```html
<div role="tablist" aria-label="Account settings">
  <button role="tab" aria-selected="true" aria-controls="panel-1" id="tab-1">
    Profile
  </button>
  <button role="tab" aria-selected="false" aria-controls="panel-2" id="tab-2">
    Security
  </button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Profile content -->
</div>
```

**Accessible Form with Validation**
```html
<form>
  <label for="email">Email Address</label>
  <input type="email" 
         id="email" 
         aria-required="true"
         aria-invalid="true"
         aria-describedby="email-error">
  <span id="email-error" role="alert">Please enter a valid email address</span>
</form>
```

## Keyboard Navigation Requirements

All interactive elements must be keyboard accessible without requiring a mouse.

### Focus Management

**Tab Order** — Logical sequence matching visual layout
- Use semantic HTML elements (button, a, input) for natural tab order
- Use `tabindex="0"` to add custom elements to tab order
- Use `tabindex="-1"` for programmatic focus (modals, error messages)
- Never use `tabindex` values greater than 0 (creates unpredictable order)

**Focus Indicators** — Visible indication of focused element
```css
/* WCAG 2.2 AA compliant focus indicator */
:focus-visible {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}

/* Enhanced focus indicator (AAA) */
:focus-visible {
  outline: 3px solid #0066cc;
  outline-offset: 3px;
  box-shadow: 0 0 0 5px rgba(0, 102, 204, 0.2);
}
```

**Focus Trapping** — Contain focus within modals and dialogs
```javascript
function trapFocus(element) {
  const focusableElements = element.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  element.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        lastElement.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        firstElement.focus();
      }
    }
  });
}
```

### Keyboard Shortcuts

**Standard Keyboard Patterns**
- **Tab** — Move focus forward
- **Shift+Tab** — Move focus backward
- **Enter/Space** — Activate buttons and links
- **Arrow keys** — Navigate within components (tabs, menus, sliders)
- **Escape** — Close dialogs, cancel operations
- **Home/End** — Jump to first/last item in lists

**Custom Keyboard Shortcuts**
```javascript
// Provide visible documentation and avoid conflicts
document.addEventListener('keydown', (e) => {
  // Use modifier keys to avoid conflicts
  if (e.ctrlKey && e.key === 'k') {
    e.preventDefault();
    openSearchDialog();
  }
});
```

## Screen Reader Compatibility

Optimize content for screen readers (JAWS, NVDA, VoiceOver, TalkBack).

### Semantic HTML

**Use native elements for built-in accessibility**
```html
<!-- Good: Semantic HTML -->
<button>Submit</button>
<a href="/about">About Us</a>
<nav><ul><li><a href="/">Home</a></li></ul></nav>

<!-- Bad: Requires extensive ARIA -->
<div onclick="submit()">Submit</div>
<span onclick="navigate()">About Us</span>
<div><div><div onclick="navigate()">Home</div></div></div>
```

### Alternative Text Strategies

**Informative Images**
```html
<img src="chart.png" alt="Sales increased 45% from Q1 to Q2 2026">
```

**Decorative Images**
```html
<img src="decorative-border.png" alt="" role="presentation">
```

**Complex Images**
```html
<figure>
  <img src="org-chart.png" alt="Company organizational structure" 
       aria-describedby="org-description">
  <figcaption id="org-description">
    The CEO reports to the Board. Three VPs (Engineering, Sales, Operations) 
    report to the CEO. Each VP manages 3-5 department heads.
  </figcaption>
</figure>
```

**Functional Images (Icons)**
```html
<button aria-label="Close dialog">
  <svg aria-hidden="true" focusable="false"><!-- X icon --></svg>
</button>
```

### Live Regions for Dynamic Content

```html
<!-- Polite announcements (non-urgent) -->
<div aria-live="polite" aria-atomic="true">
  5 new messages
</div>

<!-- Assertive announcements (urgent) -->
<div role="alert" aria-live="assertive">
  Error: Payment failed. Please try again.
</div>

<!-- Status updates -->
<div role="status" aria-live="polite">
  Saving... Saved successfully.
</div>
```

## Color Contrast & Visual Design

Ensure sufficient contrast and don't rely solely on color to convey information.

### Contrast Ratios (WCAG 2.2)

**Level AA Requirements**
- Normal text (< 24px): 4.5:1 minimum
- Large text (≥ 24px or ≥ 19px bold): 3:1 minimum
- UI components and graphics: 3:1 minimum

**Level AAA Requirements**
- Normal text: 7:1 minimum
- Large text: 4.5:1 minimum

**Contrast Calculation**
```javascript
// Calculate relative luminance
function getLuminance(r, g, b) {
  const [rs, gs, bs] = [r, g, b].map(c => {
    c = c / 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
}

// Calculate contrast ratio
function getContrastRatio(rgb1, rgb2) {
  const lum1 = getLuminance(...rgb1);
  const lum2 = getLuminance(...rgb2);
  const lighter = Math.max(lum1, lum2);
  const darker = Math.min(lum1, lum2);
  return (lighter + 0.05) / (darker + 0.05);
}
```

### Color-Independent Design

**Don't rely on color alone**
```html
<!-- Bad: Color only -->
<span style="color: red;">Error</span>
<span style="color: green;">Success</span>

<!-- Good: Color + icon + text -->
<span class="error">
  <svg aria-hidden="true"><!-- Error icon --></svg>
  Error: Invalid input
</span>
<span class="success">
  <svg aria-hidden="true"><!-- Check icon --></svg>
  Success: Saved
</span>
```

## Accessibility Testing Workflow

Integrate accessibility testing throughout the development lifecycle.

### Automated Testing Tools

**axe DevTools** — Browser extension for in-page testing
- Install: Chrome/Firefox/Edge extension
- Use: Analyze page, review issues by severity
- Integration: axe-core library for CI/CD

**Lighthouse** — Built into Chrome DevTools
- Run: DevTools > Lighthouse > Accessibility
- Provides: Score, specific issues, guidance

**Pa11y** — Command-line testing tool
```bash
npm install -g pa11y
pa11y https://example.com
```

**axe-core Integration (Jest)**
```javascript
import { axe, toHaveNoViolations } from 'jest-axe';
expect.extend(toHaveNoViolations);

test('page should be accessible', async () => {
  const { container } = render(<MyComponent />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

### Manual Testing Procedures

**Keyboard Navigation Test**
1. Unplug mouse or don't use trackpad
2. Tab through entire page
3. Verify all interactive elements are reachable
4. Verify focus indicators are visible
5. Test all keyboard shortcuts and interactions

**Screen Reader Test**
- **Windows**: NVDA (free) or JAWS
- **macOS**: VoiceOver (built-in, Cmd+F5)
- **iOS**: VoiceOver (Settings > Accessibility)
- **Android**: TalkBack (Settings > Accessibility)

**Zoom and Reflow Test**
1. Zoom to 200% (browser zoom)
2. Verify content reflows (no horizontal scrolling)
3. Verify all functionality remains available
4. Test at 400% for AAA compliance

**Color Contrast Test**
- Use browser extensions (e.g., WCAG Color Contrast Checker)
- Test all text, icons, and UI components
- Test in different color modes (light/dark)

### Testing Checklist

**Every Release**
- [ ] Run automated accessibility scan (axe, Lighthouse)
- [ ] Keyboard navigation test
- [ ] Screen reader spot check (major flows)
- [ ] Color contrast verification
- [ ] Form validation and error handling

**Quarterly Comprehensive Audit**
- [ ] Full screen reader testing (NVDA, JAWS, VoiceOver)
- [ ] Mobile screen reader testing (TalkBack, VoiceOver)
- [ ] Zoom and reflow testing (200%, 400%)
- [ ] Cognitive accessibility review
- [ ] Third-party accessibility audit (if budget allows)

## Legal Compliance Requirements

Understand accessibility laws and compliance obligations.

### Key Regulations

**ADA (Americans with Disabilities Act)** — United States
- Applies to: Public accommodations, commercial facilities
- Standard: WCAG 2.1 Level AA (court precedent)
- Enforcement: Department of Justice, private lawsuits

**Section 508** — United States federal agencies
- Applies to: Federal government websites and technology
- Standard: WCAG 2.0 Level AA (updated to 2.1 in practice)
- Enforcement: Access Board, agency compliance officers

**EAA (European Accessibility Act)** — European Union
- Applies to: Products and services (effective June 2025)
- Standard: EN 301 549 (aligned with WCAG 2.1 Level AA)
- Enforcement: Member state authorities

**AODA (Accessibility for Ontarians with Disabilities Act)** — Ontario, Canada
- Applies to: Public and private sector organizations
- Standard: WCAG 2.0 Level AA
- Enforcement: Accessibility Directorate of Ontario

### Compliance Documentation

**VPAT (Voluntary Product Accessibility Template)**
- Purpose: Document WCAG/Section 508 conformance
- Format: Standardized template (ITI VPAT 2.5)
- Use: Procurement, vendor evaluation, transparency

**Accessibility Statement**
```markdown
# Accessibility Statement

[Company] is committed to ensuring digital accessibility for people with disabilities.
We continually improve the user experience for everyone and apply relevant accessibility standards.

## Conformance Status
We aim to conform to WCAG 2.2 Level AA standards.

## Feedback
We welcome feedback on the accessibility of [product]. Please contact us at accessibility@company.com.

## Date
This statement was last updated on [date].
```

## Remediation Strategies

---

**Note:** This file was automatically condensed to meet the 500-line requirement. Additional content has been moved to the references/ folder.

## References

- [Compliance Documentation](references/compliance-documentation.md)
- [Implementation Patterns](references/implementation-patterns.md)
- [Testing Tools](references/testing-tools.md)
- [Wcag Guidelines](references/wcag-guidelines.md)
