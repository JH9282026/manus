# Accessibility Audit Process

## Overview

A systematic accessibility audit identifies barriers and provides actionable remediation guidance. Combining automated tools, manual testing, and assistive technology evaluation ensures comprehensive coverage.

---

## Audit Planning

**Define Scope**: Identify pages, user flows, and components to audit. Prioritize high-traffic pages and critical user journeys.

**Select Standards**: Typically WCAG 2.1 Level AA for most projects. Government sites may require Section 508 compliance.

**Assemble Tools**: Automated scanners (axe, WAVE, Lighthouse), screen readers (NVDA, JAWS, VoiceOver), browser extensions, color contrast analyzers.

**Create Checklist**: Document specific success criteria to evaluate. Use WCAG Quick Reference as foundation.

---

## Automated Testing Phase

**Initial Scan**: Run automated tools on all pages in scope. Tools like axe DevTools, WAVE, or Lighthouse catch common issues quickly.

**Document Findings**: Record all automated findings with severity levels. Note that automated tools only catch 30-40% of issues.

**Categorize Issues**: Group by WCAG principle (Perceivable, Operable, Understandable, Robust) and severity (Critical, Serious, Moderate, Minor).

**Recommended Tools**:
- axe DevTools: Comprehensive, accurate, integrates with browsers
- WAVE: Visual feedback, good for learning
- Lighthouse: Built into Chrome, good for quick scans
- Pa11y: Command-line tool for CI/CD integration

---

## Manual Testing Phase

**Keyboard Navigation**: Tab through entire interface. Verify logical order, visible focus, no keyboard traps, and all functionality accessible.

**Screen Reader Testing**: Test with at least two screen readers (e.g., NVDA + VoiceOver). Verify page structure, navigation, forms, and dynamic content.

**Visual Inspection**: Check color contrast, text sizing, responsive behavior, and visual indicators. Use browser zoom to test at 200%.

**Content Review**: Verify heading hierarchy, link text clarity, alt text quality, and form label associations.

**Interactive Components**: Test modals, dropdowns, tabs, accordions, and custom widgets for keyboard access and screen reader announcements.

---

## Reporting Structure

**Executive Summary**: High-level overview of findings, compliance level, and priority recommendations. Include overall score or grade.

**Detailed Findings**: Each issue should include:
- Issue description and location
- WCAG success criterion violated
- Severity level (Critical/Serious/Moderate/Minor)
- User impact explanation
- Remediation guidance with code examples
- Screenshots or screen recordings

**Prioritization Matrix**: Organize issues by severity and effort. Quick wins (high impact, low effort) should be addressed first.

**Remediation Roadmap**: Phased approach with timelines. Critical issues first, then serious, then moderate/minor.

---

## Issue Severity Levels

**Critical**: Blocks access for disabled users. Examples: missing alt text on essential images, keyboard traps, forms without labels. Fix immediately.

**Serious**: Major barriers causing significant difficulty. Examples: poor color contrast, missing skip links, improper heading hierarchy. Fix within sprint.

**Moderate**: Noticeable barriers but workarounds exist. Examples: redundant links, minor contrast issues, missing ARIA labels. Fix within quarter.

**Minor**: Best practice violations with minimal user impact. Examples: missing lang attribute, non-descriptive link text in low-priority areas. Fix when convenient.

---

## Remediation Verification

**Re-test Fixed Issues**: Verify each remediation actually resolves the issue. Test with same tools and methods used in initial audit.

**Regression Testing**: Ensure fixes don't introduce new issues. Run full automated scan after major changes.

**User Validation**: If possible, have disabled users test remediated features. Real-world validation is invaluable.

**Documentation**: Update audit report with remediation status. Track progress and maintain accessibility documentation for future reference.

---
