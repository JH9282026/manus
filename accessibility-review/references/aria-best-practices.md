# ARIA Best Practices

## Overview

Accessible Rich Internet Applications (ARIA) provides semantic information to assistive technologies when native HTML is insufficient. However, ARIA should be used judiciously—the first rule of ARIA is don't use ARIA if native HTML works.

---

## ARIA First Rule

**Use Native HTML First**: Native HTML elements have built-in accessibility. Use `<button>` instead of `<div role='button'>`, `<nav>` instead of `<div role='navigation'>`.

**When ARIA is Needed**: Custom widgets without HTML equivalents (tree views, complex tabs), dynamic content updates (live regions), enhanced semantics for complex applications.

**ARIA Doesn't Fix Everything**: ARIA only affects semantics, not behavior. You must still implement keyboard navigation, focus management, and visual styling.

---

## ARIA Roles

**Landmark Roles**: `banner`, `navigation`, `main`, `complementary`, `contentinfo`, `search`, `form`. Use HTML5 equivalents when possible (`<nav>`, `<main>`, `<aside>`).

**Widget Roles**: `button`, `checkbox`, `tab`, `tabpanel`, `dialog`, `menu`, `menuitem`, `tree`, `treeitem`. Require keyboard interaction implementation.

**Document Structure Roles**: `article`, `heading`, `list`, `listitem`, `table`, `row`, `cell`. Usually better to use native HTML.

**Live Region Roles**: `alert`, `status`, `log`, `marquee`, `timer`. Announce dynamic content changes to screen readers.

---

## ARIA States and Properties

**aria-label**: Provides accessible name when visible label isn't present. Example: `<button aria-label='Close dialog'>×</button>`

**aria-labelledby**: References element(s) that label the current element. Example: `<div role='dialog' aria-labelledby='dialog-title'>`

**aria-describedby**: References element(s) that describe the current element. Example: `<input aria-describedby='password-requirements'>`

**aria-hidden**: Hides content from assistive technologies. Use for decorative or redundant content. Example: `<span aria-hidden='true'>★</span>`

**aria-expanded**: Indicates if collapsible content is expanded. Example: `<button aria-expanded='false' aria-controls='menu'>`

**aria-selected**: Indicates selection state in tabs, options, or rows. Example: `<div role='tab' aria-selected='true'>`

**aria-checked**: Indicates checkbox or radio state. Example: `<div role='checkbox' aria-checked='true'>`

**aria-disabled**: Indicates disabled state. Example: `<button aria-disabled='true'>`

---

## Live Regions

**aria-live='polite'**: Announces changes when user is idle. Use for non-critical updates like status messages.

**aria-live='assertive'**: Announces changes immediately, interrupting current speech. Use sparingly for critical alerts.

**aria-atomic**: Indicates if entire region should be announced or just changes. `aria-atomic='true'` announces entire region.

**role='alert'**: Equivalent to `aria-live='assertive' aria-atomic='true'`. Use for important messages.

**role='status'**: Equivalent to `aria-live='polite' aria-atomic='true'`. Use for status updates.

**Implementation Tips**: Create live region on page load (not dynamically), update content via JavaScript, keep announcements concise.

---

## Common ARIA Patterns

**Modal Dialog**: `role='dialog'`, `aria-modal='true'`, `aria-labelledby` for title, trap focus, close with Escape.

**Tabs**: `role='tablist'` on container, `role='tab'` on tabs, `role='tabpanel'` on panels, `aria-selected` on active tab, arrow key navigation.

**Accordion**: `<button>` for headers with `aria-expanded`, `aria-controls` pointing to panel, unique IDs for association.

**Dropdown Menu**: `role='menu'` on container, `role='menuitem'` on items, arrow key navigation, Escape to close, focus management.

**Combobox**: `role='combobox'`, `aria-expanded`, `aria-controls` pointing to listbox, `aria-activedescendant` for virtual focus.

---

## ARIA Pitfalls to Avoid

**Overusing ARIA**: Don't add ARIA to elements that already have native semantics. `<button role='button'>` is redundant.

**Conflicting Roles**: Don't override native semantics incorrectly. `<button role='heading'>` breaks button functionality.

**Missing Keyboard Support**: ARIA roles require keyboard implementation. `role='button'` needs Enter/Space handlers.

**Incorrect State Management**: Update ARIA states when UI changes. Forgetting to toggle `aria-expanded` confuses users.

**Empty Labels**: `aria-label=''` or `aria-labelledby` pointing to empty element provides no information.

**Hiding Focusable Content**: Don't use `aria-hidden='true'` on focusable elements. Creates keyboard traps.

---
