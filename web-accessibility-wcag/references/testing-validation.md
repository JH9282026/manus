# Testing Validation

Detailed reference content for web-accessibility-wcag.

---

## Accessibility Testing

### Manual Testing

**Keyboard Navigation**: Navigate the entire site using only keyboard. Verify all functionality is accessible and focus is always visible.

**Screen Reader Testing**: Test with at least one screen reader. Navigate by headings, landmarks, and links. Verify all content is announced correctly.

**Color Contrast**: Check all text and interactive element contrast ratios against backgrounds.

**Zoom Testing**: Test at 200% zoom. Verify content reflows and remains usable without horizontal scrolling.

### Automated Testing Tools

**axe DevTools**: Browser extension providing automated accessibility testing with clear violation reporting.

**WAVE**: Web-based and browser extension tool that visualizes accessibility issues directly on pages.

**Lighthouse**: Built into Chrome DevTools, provides accessibility audits as part of page quality analysis.

**Pa11y**: Command-line tool for automated accessibility testing, suitable for CI/CD integration.

### User Testing

**Testing with People with Disabilities**: The most valuable accessibility testing involves actual users with disabilities using their preferred assistive technologies.

**Diverse User Groups**: Include users with various disabilities, technology setups, and experience levels.

**Real-World Scenarios**: Test with realistic tasks and content, not just technical compliance.

---