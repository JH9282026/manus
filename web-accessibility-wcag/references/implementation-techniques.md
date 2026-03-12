# Implementation Techniques

Detailed reference content for web-accessibility-wcag.

---

## ARIA (Accessible Rich Internet Applications)

### What is ARIA

WAI-ARIA (Web Accessibility Initiative - Accessible Rich Internet Applications) is a specification that defines ways to make web content and applications more accessible to people with disabilities. ARIA provides semantic information about widgets, structures, and behaviors that enhance accessibility when native HTML semantics are insufficient.

### ARIA Roles

**Landmark Roles**: Define regions of the page for navigation. Include `banner`, `navigation`, `main`, `complementary`, `contentinfo`, `search`, `form`, and `region`. These help screen reader users navigate quickly to major sections.

**Widget Roles**: Define interactive components. Include `button`, `checkbox`, `dialog`, `listbox`, `menu`, `menuitem`, `progressbar`, `slider`, `tab`, `tabpanel`, `textbox`, `tree`, and many more.

**Document Structure Roles**: Define structural elements. Include `article`, `heading`, `list`, `listitem`, `table`, `row`, `cell`, `img`, and `separator`.

**Live Region Roles**: Define areas that update dynamically. Include `alert`, `log`, `marquee`, `status`, and `timer`. These announce changes to assistive technology users.

### ARIA Properties

**aria-label**: Provides an accessible name for an element when visible text is not available. Use for icons, unlabeled inputs, or elements where the visible label is insufficient.

**aria-labelledby**: References the ID of another element that provides the accessible name. Useful when the label is visible but not programmatically associated.

**aria-describedby**: References elements that provide additional descriptions or instructions. Useful for form fields with help text or error messages.

**aria-hidden**: Hides content from assistive technologies while keeping it visually present. Use for decorative elements, duplicated content, or off-screen content.

**aria-live**: Announces dynamic content changes. Values include `polite` (waits for pause), `assertive` (interrupts immediately), and `off` (no announcements).

### ARIA States

**aria-expanded**: Indicates whether a collapsible element is expanded or collapsed. Use for accordions, menus, and disclosure widgets.

**aria-selected**: Indicates the current selection state in widgets like tabs, listboxes, and trees.

**aria-checked**: Indicates the checked state for checkboxes, radio buttons, and toggle switches. Supports `true`, `false`, and `mixed` values.

**aria-disabled**: Indicates that an element is disabled and not interactive. The element remains focusable and visible but non-functional.

### ARIA Best Practices

**Use Semantic HTML First**: ARIA should supplement, not replace, proper HTML semantics. A native `<button>` is always preferable to `<div role="button">`.

**Don't Override Native Semantics**: Avoid adding ARIA roles that conflict with an element's implicit role. Don't add `role="button"` to an `<a>` element.

**Test with Screen Readers**: ARIA implementations must be tested with actual assistive technologies. Browser support and screen reader behavior can vary significantly.

---

---

## Keyboard Navigation

### Keyboard Accessibility Importance

Keyboard accessibility is fundamental because many assistive technologies translate input into keyboard commands. Users with motor disabilities, visual impairments, and those who prefer keyboard navigation all depend on complete keyboard operability.

### Keyboard Navigation Requirements

**All Functionality Keyboard Accessible**: Every interactive element and action must be achievable using only a keyboard. This includes navigation, form submission, media controls, and custom widgets.

**Logical Tab Order**: Focus must move through interactive elements in a logical sequence that follows the visual layout. Tab order should progress left to right, top to bottom in most languages.

**Visible Focus Indicators**: A visible outline or highlight must indicate which element has keyboard focus. Default browser focus styles should not be removed without providing equally visible alternatives.

**Skip Links**: Allow users to bypass repetitive content like navigation menus. Skip links should be the first focusable element on the page and become visible when focused.

### Focus Management

**Focus Order**: Manage focus order using proper DOM structure rather than tabindex values greater than 0. Use `tabindex="0"` to add elements to tab order and `tabindex="-1"` for programmatically focusable elements.

**Focus Trapping**: Modal dialogs and overlays should trap focus within the dialog until closed. This prevents users from accidentally tabbing to content behind the modal.

**Focus Restoration**: When closing modals or completing interactions, return focus to the triggering element or a logical next location. Users should never be left in an unexpected focus position.

**Focus Styles**: Ensure focus indicators have sufficient contrast (3:1 ratio against adjacent colors) and are large enough to be clearly visible. WCAG 2.2 requires a minimum focus indicator area.

### Keyboard Shortcuts

**Standard Shortcuts**: Support standard keyboard patterns like Tab for navigation, Enter/Space for activation, Arrow keys for widget navigation, and Escape for dismissal.

**Custom Shortcuts**: Document custom shortcuts and ensure they don't conflict with browser or assistive technology shortcuts. Provide alternatives for users who cannot use shortcuts.

**Avoid Conflicts**: Single character shortcuts (letters, numbers, punctuation) can interfere with screen reader commands. WCAG 2.1 requires these to be remappable or only active on focus.

---

---

## Accessible Navigation

### Navigation Structure

**Consistent Navigation**: Navigation should appear in the same location and order across pages. Users should be able to predict where to find navigation elements.

**Multiple Ways to Navigate**: Provide multiple ways to find content: navigation menus, site search, sitemaps, and breadcrumbs.

**Skip Links**: Allow users to skip repetitive navigation and jump directly to main content.

**Breadcrumbs**: Show users their location in the site hierarchy and provide alternative navigation paths.

### Menu Accessibility

**Keyboard Navigation**: Menus must be fully operable via keyboard. Use arrow keys for navigation within menus and Tab to exit.

**ARIA Roles**: Use appropriate ARIA roles (`navigation`, `menu`, `menuitem`, `menubar`) for complex navigation patterns.

**Focus Management**: Manage focus within dropdown menus. Return focus to the trigger element when menus close.

**Mobile Menus**: Mobile navigation patterns (hamburger menus, slide-outs) must be keyboard accessible and properly announced.

### Link Accessibility

**Descriptive Link Text**: Link text should clearly describe the destination. Avoid generic text like "click here" or "read more."

**Link Purpose**: Link purpose should be determinable from the link text alone or from surrounding context.

**External Links**: Indicate when links open new windows or navigate to external sites. Warn users before their context changes.

### Page Structure

**Landmarks**: Use HTML5 landmarks and ARIA landmark roles to define page regions. Screen reader users navigate by landmarks.

**Heading Hierarchy**: Use headings in logical order without skipping levels. Start with one `<h1>` and use subsequent levels for subsections.

---