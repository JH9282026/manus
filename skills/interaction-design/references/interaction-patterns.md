# Interaction Patterns

Comprehensive catalog of proven interaction patterns with usage guidelines, variations, and accessibility considerations.

---

## Navigation Patterns

### Breadcrumbs

**Purpose:** Show user's location in site hierarchy and provide quick navigation to parent levels.

**When to use:**
- Deep content hierarchies (3+ levels)
- E-commerce product categories
- Documentation sites
- Any site where users may enter via search/deep links

**Implementation guidelines:**
- Show full path from home to current page
- Make all levels except current page clickable
- Use ">" or "/" as separators
- Place at top of content area, below main navigation
- Truncate middle levels if path is very long (Home > ... > Parent > Current)

**Accessibility:**
- Use `<nav>` element with `aria-label="Breadcrumb"`
- Use ordered list (`<ol>`) for breadcrumb items
- Mark current page with `aria-current="page"`
- Ensure sufficient color contrast for links

**Anti-patterns:**
- Don't use for flat site structures (2 levels or fewer)
- Don't replace primary navigation with breadcrumbs
- Don't show breadcrumbs on mobile if space is limited (use back button instead)

---

### Tabs

**Purpose:** Organize related content into separate views without leaving the page.

**When to use:**
- Grouping related content (e.g., Profile, Settings, Notifications)
- Switching between different views of same data (e.g., List view, Grid view)
- Multi-step forms where users may need to jump between steps

**Implementation guidelines:**
- Limit to 3-7 tabs (more becomes overwhelming)
- Make active tab visually distinct (underline, background color, or border)
- Keep tab labels short (1-2 words)
- Maintain state when switching tabs (don't lose user input)
- Consider horizontal scrolling for mobile if many tabs

**Variations:**
- **Horizontal tabs** — Standard, placed above content
- **Vertical tabs** — Better for many tabs or long labels, placed to left of content
- **Pill tabs** — Rounded, button-like appearance
- **Underline tabs** — Minimal style with underline indicating active tab

**Accessibility:**
- Use `role="tablist"` on container, `role="tab"` on tab buttons, `role="tabpanel"` on content
- Implement keyboard navigation (Arrow keys to switch tabs, Tab to move to content)
- Use `aria-selected="true"` on active tab
- Use `aria-controls` to link tab to its panel
- Ensure tab panels have `tabindex="0"` for keyboard focus

**Anti-patterns:**
- Don't use tabs for sequential processes (use stepper/wizard instead)
- Don't hide critical information in non-default tabs
- Don't use tabs and accordions together (competing patterns)
- Don't auto-rotate tabs (users lose context)

---

### Hamburger Menu

**Purpose:** Collapse navigation into icon to save screen space, primarily on mobile.

**When to use:**
- Mobile responsive designs with many navigation items
- Secondary navigation that's not always needed
- Utility navigation (settings, help, account)

**Implementation guidelines:**
- Use recognizable three-line icon (≡)
- Place in top-left or top-right corner (consistent with platform conventions)
- Animate menu opening/closing for continuity
- Include close button (X) in open menu
- Dim background when menu is open (focus attention)
- Prevent body scroll when menu is open

**Accessibility:**
- Use `<button>` element, not `<div>` or `<a>`
- Include accessible label: `aria-label="Main menu"`
- Update `aria-expanded` state (true/false) when toggling
- Trap keyboard focus within open menu
- Close menu on Escape key
- Return focus to menu button when closing

**Anti-patterns:**
- Don't hide primary navigation on desktop (hamburger menus reduce discoverability)
- Don't use for only 2-3 navigation items (just show them)
- Don't use without label on desktop ("Menu" text improves clarity)
- Don't use for critical actions (e.g., "Buy now" button)

**Alternatives to consider:**
- **Priority+ navigation** — Show as many items as fit, collapse rest into "More" menu
- **Tab bar** — Bottom navigation for 3-5 primary sections (mobile apps)
- **Drawer navigation** — Persistent drawer on tablet/desktop, collapsible on mobile

---

## Input Patterns

### Inline Editing

**Purpose:** Allow users to edit content directly in place without switching to edit mode.

**When to use:**
- Editing single fields (names, titles, descriptions)
- Spreadsheet-like interfaces
- Content management systems
- Dashboards where users frequently update values

**Implementation guidelines:**
- Show edit affordance on hover (pencil icon, underline, or highlight)
- Click to activate edit mode (field becomes input)
- Save on blur or Enter key
- Cancel on Escape key
- Show loading state while saving
- Provide clear feedback on save success/failure

**Variations:**
- **Click to edit** — Click text to activate input field
- **Always editable** — Field always looks like input (e.g., spreadsheets)
- **Edit button** — Explicit button to enter edit mode

**Accessibility:**
- Ensure edit affordance is keyboard accessible (Tab to focus, Enter to edit)
- Announce state changes to screen readers ("Editing [field name]")
- Provide visible focus indicators
- Support standard keyboard shortcuts (Enter to save, Escape to cancel)

**Anti-patterns:**
- Don't use for long-form content (use dedicated edit page)
- Don't auto-save without confirmation for critical data
- Don't make it unclear what's editable (provide visual cues)
- Don't lose user input on accidental blur (confirm before discarding)

---

### Autocomplete / Typeahead

**Purpose:** Suggest completions as user types to speed input and reduce errors.

**When to use:**
- Search inputs
- Address fields
- Tag/category selection
- Any input with predictable values

**Implementation guidelines:**
- Show suggestions after 2-3 characters typed
- Limit to 5-10 suggestions (more is overwhelming)
- Highlight matching portion of suggestion
- Allow keyboard navigation (Arrow keys to select, Enter to choose)
- Allow typing custom value if no match
- Debounce API calls (wait 200-300ms after last keystroke)

**Accessibility:**
- Use `role="combobox"` on input
- Use `aria-autocomplete="list"` to indicate autocomplete behavior
- Use `aria-expanded` to indicate dropdown state
- Use `aria-activedescendant` to indicate highlighted suggestion
- Announce number of suggestions to screen readers

**Anti-patterns:**
- Don't show suggestions too early (after 1 character is often too noisy)
- Don't auto-select first suggestion (users may not notice and submit wrong value)
- Don't require selection from suggestions (allow custom input)
- Don't make suggestions too slow (>500ms feels unresponsive)

---

### Multi-Step Forms (Wizard)

**Purpose:** Break complex forms into manageable steps to reduce cognitive load.

**When to use:**
- Onboarding flows
- Checkout processes
- Complex configuration
- Any form with 10+ fields

**Implementation guidelines:**
- Show progress indicator (step 2 of 5)
- Allow navigation to previous steps (Back button)
- Save progress between steps (don't lose user input)
- Validate each step before proceeding
- Provide summary/review step before final submission
- Make "Next" button prominent, "Back" button secondary

**Step organization strategies:**
- **Logical grouping** — Group related fields (Personal info → Address → Payment)
- **Progressive disclosure** — Ask simple questions first, complex later
- **Conditional steps** — Skip irrelevant steps based on previous answers

**Accessibility:**
- Use `aria-label` to describe current step ("Step 2 of 5: Shipping address")
- Ensure progress indicator is accessible to screen readers
- Maintain logical tab order within each step
- Announce step changes to screen readers

**Anti-patterns:**
- Don't use for short forms (3-5 fields can be single page)
- Don't make steps too granular (1 field per step is tedious)
- Don't hide progress indicator (users need to know how much is left)
- Don't prevent going back (users may need to correct earlier input)

---

## Feedback Patterns

### Toast Notifications

**Purpose:** Provide brief, non-intrusive feedback about system actions.

**When to use:**
- Confirming actions ("Message sent," "Item added to cart")
- Non-critical errors ("Connection lost, retrying...")
- Undo opportunities ("Email deleted" with Undo button)

**Implementation guidelines:**
- Display for 3-5 seconds (longer for messages with actions)
- Position consistently (usually bottom-center or top-right)
- Stack multiple toasts vertically
- Allow manual dismissal (X button)
- Don't auto-dismiss if toast contains action button
- Animate in/out smoothly

**Variations:**
- **Success toast** — Green, checkmark icon
- **Error toast** — Red, error icon, longer duration
- **Info toast** — Blue, info icon
- **Warning toast** — Yellow/orange, warning icon

**Accessibility:**
- Use `role="status"` for non-critical messages (polite announcement)
- Use `role="alert"` for errors (immediate announcement)
- Ensure sufficient color contrast
- Don't rely on color alone (use icons and text)
- Ensure toast is keyboard accessible if it contains actions

**Anti-patterns:**
- Don't use for critical errors (use modal dialog instead)
- Don't show too many toasts at once (queue them)
- Don't auto-dismiss error messages (users need time to read)
- Don't use for information that requires action (use modal or inline message)

---

### Loading Indicators

**Purpose:** Communicate that system is processing and manage user expectations.

**When to use:**
- Any operation taking >1 second
- Page loads, form submissions, data fetching

**Implementation guidelines:**

**By duration:**
- **<1 second** — No indicator needed (feels instant)
- **1-5 seconds** — Spinner or indeterminate progress bar
- **5-10 seconds** — Determinate progress bar with percentage
- **10+ seconds** — Progress bar with time estimate and cancel option

**By context:**
- **Full page load** — Skeleton screen (shows content structure while loading)
- **Button action** — Replace button text with spinner, disable button
- **Inline content** — Small spinner in content area
- **Background process** — Subtle indicator in header/footer

**Accessibility:**
- Use `aria-live="polite"` for loading announcements
- Use `aria-busy="true"` on loading container
- Provide text alternative for visual spinners ("Loading...")
- Announce completion to screen readers

**Anti-patterns:**
- Don't show spinner for <1 second operations (causes flicker)
- Don't use indeterminate progress for long operations (users need estimate)
- Don't block entire interface for background operations
- Don't use animated GIFs (use CSS/SVG animations for better performance)

---

### Skeleton Screens

**Purpose:** Reduce perceived loading time by showing content structure while data loads.

**When to use:**
- Initial page loads
- Infinite scroll loading more content
- Card-based layouts (feeds, grids)

**Implementation guidelines:**
- Match skeleton to actual content layout
- Use subtle animation (shimmer effect)
- Show skeleton for text, images, and UI elements
- Replace skeleton with real content progressively (as it loads)
- Use neutral colors (light gray)

**Accessibility:**
- Use `aria-busy="true"` on skeleton container
- Announce when content finishes loading
- Ensure skeleton doesn't interfere with screen reader navigation

**Anti-patterns:**
- Don't use for very fast loads (<500ms)
- Don't make skeleton too detailed (simple shapes are better)
- Don't show skeleton indefinitely (fall back to error state if load fails)

---

## Content Patterns

### Infinite Scroll

**Purpose:** Load more content automatically as user scrolls, creating seamless browsing.

**When to use:**
- Social media feeds
- Image galleries
- Search results (when users are exploring, not seeking specific item)

**Implementation guidelines:**
- Load next page when user is ~80% down current content
- Show loading indicator while fetching
- Maintain scroll position if user navigates away and returns
- Provide "Back to top" button after scrolling significantly
- Consider hybrid approach: load 2-3 pages automatically, then show "Load more" button

**Accessibility:**
- Announce new content loading to screen readers
- Ensure keyboard users can access all loaded content
- Provide alternative navigation (search, filters) for finding specific content

**Anti-patterns:**
- Don't use when users need to reach footer (footer becomes unreachable)
- Don't use for goal-oriented tasks (e.g., finding specific product)
- Don't lose user's place when they navigate back
- Don't load indefinitely without performance consideration (DOM becomes huge)

**Alternative: Pagination**

Use pagination when:
- Users need to reach footer
- Users are looking for specific item (want to remember "it was on page 3")
- SEO is important (search engines can index individual pages)
- Performance is concern (limit DOM size)

---

### Cards

**Purpose:** Group related information into scannable, actionable containers.

**When to use:**
- Displaying collections of heterogeneous content
- Dashboards
- Product listings
- News feeds

**Implementation guidelines:**
- Keep cards consistent in structure (same elements in same positions)
- Make entire card clickable if it leads to detail page
- Use clear visual hierarchy within card (image → title → description → actions)
- Provide adequate spacing between cards
- Consider responsive grid (1 column mobile, 2-3 columns tablet, 3-4 columns desktop)

**Card anatomy:**
- **Header** — Title, subtitle, metadata (date, author)
- **Media** — Image, video, or icon
- **Content** — Description, preview text
- **Actions** — Buttons or links (primary action prominent)

**Accessibility:**
- Use semantic HTML (`<article>` for card container)
- Ensure card title is proper heading level
- Make card keyboard accessible (Tab to focus, Enter to activate)
- Provide sufficient color contrast for all text
- Don't rely on hover states (not available on touch devices)

**Anti-patterns:**
- Don't make cards too small (hard to read and interact)
- Don't put too much information in card (use card as preview, detail page for full info)
- Don't use cards for single-item display (cards are for collections)
- Don't make cards inconsistent sizes without good reason (creates visual chaos)

---

### Accordions

**Purpose:** Collapse content into sections to reduce page length and cognitive load.

**When to use:**
- FAQs
- Settings panels with many options
- Mobile navigation
- Any long page with distinct sections

**Implementation guidelines:**
- Use clear, descriptive section headers
- Indicate expanded/collapsed state (chevron icon)
- Allow multiple sections open simultaneously (unless mutually exclusive)
- Animate expansion/collapse smoothly
- Consider starting with first section expanded

**Accessibility:**
- Use `<button>` for accordion headers
- Use `aria-expanded` to indicate state (true/false)
- Use `aria-controls` to link header to content panel
- Ensure keyboard navigation works (Tab to header, Enter/Space to toggle)
- Use proper heading levels for accordion headers

**Anti-patterns:**
- Don't hide critical information in collapsed sections
- Don't use for short content (if everything fits on screen, don't collapse)
- Don't auto-collapse sections when user opens another (unless mutually exclusive)
- Don't use accordions and tabs together (competing patterns)

---

## Action Patterns

### Floating Action Button (FAB)

**Purpose:** Provide quick access to primary action from anywhere on screen.

**When to use:**
- Mobile apps with one clear primary action
- Actions that apply across multiple screens (e.g., "Compose" in email app)
- Actions users perform frequently

**Implementation guidelines:**
- Use for single, primary action only
- Position in bottom-right corner (right-handed users) or bottom-center
- Use icon that clearly represents action
- Consider adding text label on first use or on long-press
- Animate on scroll (hide when scrolling down, show when scrolling up)
- Ensure FAB doesn't cover important content

**Variations:**
- **Single FAB** — One action (most common)
- **Speed dial FAB** — Expands to show 2-4 related actions
- **Extended FAB** — Includes icon + text label

**Accessibility:**
- Use `<button>` element
- Provide accessible label: `aria-label="Compose new message"`
- Ensure sufficient size (minimum 56×56px)
- Ensure sufficient color contrast with background
- Make keyboard accessible

**Anti-patterns:**
- Don't use for multiple primary actions (creates confusion)
- Don't use on desktop (desktop has more space for traditional buttons)
- Don't use for destructive actions (FAB should be positive action)
- Don't hide FAB permanently on scroll (users may need it)

---

### Drag and Drop

**Purpose:** Allow direct manipulation of objects for reordering, organizing, or transferring.

**When to use:**
- Reordering lists (priorities, playlists)
- Organizing items into categories (kanban boards)
- File uploads
- Visual editors (design tools, page builders)

**Implementation guidelines:**
- Show drag handle or make entire item draggable
- Provide visual feedback during drag (item follows cursor, semi-transparent)
- Highlight valid drop zones
- Show preview of where item will be dropped
- Animate item to final position on drop
- Provide undo for drag-and-drop actions

**Accessibility:**
- Provide keyboard alternative (arrow keys to reorder, or move up/down buttons)
- Announce drag-and-drop actions to screen readers
- Ensure drag handle is keyboard accessible
- Use `aria-grabbed` and `aria-dropeffect` (deprecated but still useful)

**Anti-patterns:**
- Don't make drag-and-drop the only way to perform action (provide alternative)
- Don't use for small touch targets (hard to drag on mobile)
- Don't allow dropping in invalid locations without clear feedback
- Don't use for long-distance dragging (provide shortcuts or multi-select)

---

### Swipe Actions

**Purpose:** Reveal contextual actions by swiping on list items (mobile pattern).

**When to use:**
- Mobile email apps (swipe to delete/archive)
- Mobile messaging apps (swipe to reply)
- Any mobile list where items have 1-3 common actions

**Implementation guidelines:**
- Reveal actions on horizontal swipe
- Use different swipe distances for different actions (short swipe = archive, long swipe = delete)
- Provide visual feedback (action icon appears as user swipes)
- Allow user to cancel by swiping back
- Consider left vs. right swipe for different actions
- Provide alternative access to actions (long-press menu or explicit buttons)

**Accessibility:**
- Provide alternative way to access swipe actions (buttons, menu)
- Announce available actions to screen readers
- Consider users with motor impairments (swipe may be difficult)

**Anti-patterns:**
- Don't use on desktop (no swipe gesture)
- Don't hide critical actions behind swipe (not discoverable)
- Don't use for more than 2-3 actions per direction (overwhelming)
- Don't make swipe actions inconsistent across app

---

## Modal Patterns

### Modal Dialogs

**Purpose:** Focus user attention on critical task or information by blocking background content.

**When to use:**
- Confirming destructive actions
- Collecting required information before proceeding
- Displaying critical alerts or errors
- Short, focused tasks that interrupt main workflow

**Implementation guidelines:**
- Dim background (overlay) to focus attention on modal
- Prevent interaction with background content
- Provide clear close mechanism (X button, Cancel button, Escape key, click outside)
- Trap keyboard focus within modal
- Return focus to trigger element when closing
- Prevent body scroll when modal is open

**Accessibility:**
- Use `role="dialog"` or `role="alertdialog"` (for critical alerts)
- Use `aria-modal="true"` to indicate modal behavior
- Use `aria-labelledby` to reference modal title
- Use `aria-describedby` to reference modal description
- Trap keyboard focus (Tab cycles through modal elements only)
- Close on Escape key
- Return focus to trigger element on close

**Anti-patterns:**
- Don't use for non-critical information (use inline or toast instead)
- Don't use for long forms (use dedicated page instead)
- Don't auto-open modals on page load (annoying, reduces accessibility)
- Don't stack modals (modal opening another modal is confusing)
- Don't make modals too large (should feel like dialog, not new page)

---

### Bottom Sheets (Mobile)

**Purpose:** Display contextual content or actions from bottom of screen (mobile pattern).

**When to use:**
- Mobile action menus (share, edit, delete)
- Mobile filters and sorting options
- Mobile forms (shorter than full screen)
- Contextual information that doesn't require full attention

**Implementation guidelines:**
- Slide up from bottom of screen
- Dim background slightly
- Allow dismissal by swiping down or tapping background
- Consider three heights: peek (showing header), half-screen, full-screen
- Make draggable (user can adjust height)

**Accessibility:**
- Use `role="dialog"`
- Trap focus within bottom sheet when open
- Provide close button for keyboard users
- Announce opening to screen readers

**Anti-patterns:**
- Don't use on desktop (use modal or dropdown instead)
- Don't use for critical alerts (use modal dialog)
- Don't make bottom sheet too tall (defeats purpose of partial overlay)

---

## Search Patterns

### Search with Filters

**Purpose:** Help users narrow large result sets to find specific items.

**When to use:**
- E-commerce product search
- Content libraries (documents, images, videos)
- Data tables with many rows
- Any search with >50 potential results

**Implementation guidelines:**
- Place filters in left sidebar (desktop) or collapsible panel (mobile)
- Show number of results for each filter option
- Allow multiple filter selections within category (checkboxes)
- Show active filters clearly with ability to remove individually
- Update results in real-time as filters change (or provide "Apply" button)
- Provide "Clear all filters" option
- Maintain filter state in URL (allows sharing filtered results)

**Filter organization:**
- Order filters by importance/usage frequency
- Group related filters into sections
- Consider progressive disclosure for many filters (show top 5, "Show more" for rest)

**Accessibility:**
- Use `<fieldset>` and `<legend>` for filter groups
- Announce result count changes to screen readers
- Ensure all filters keyboard accessible
- Provide clear labels for all filter options

**Anti-patterns:**
- Don't hide filters completely on mobile (make collapsible, not invisible)
- Don't apply filters automatically if it causes slow page reloads (provide "Apply" button)
- Don't show filters with 0 results without indication
- Don't make users scroll through hundreds of filter options (use search within filters)

---

This comprehensive pattern library provides proven solutions for common interaction design challenges. Always test patterns with your specific users and context, as effectiveness can vary based on audience and use case.
