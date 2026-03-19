# WCAG 2.2 Guidelines Reference

Comprehensive reference for Web Content Accessibility Guidelines 2.2 success criteria.

## Principle 1: Perceivable

Information and user interface components must be presentable to users in ways they can perceive.

### Guideline 1.1: Text Alternatives

**1.1.1 Non-text Content (A)**
All non-text content has a text alternative that serves the equivalent purpose.

**Implementation:**
- Images: Provide descriptive alt text
- Icons: Use aria-label or visually hidden text
- Decorative images: Use empty alt="" or role="presentation"
- Complex images: Use aria-describedby or long descriptions
- Form inputs: Use associated labels
- CAPTCHA: Provide alternative forms for different senses

**Examples:**
```html
<!-- Informative image -->
<img src="chart.png" alt="Sales increased 45% in Q2 2026">

<!-- Decorative image -->
<img src="border.png" alt="" role="presentation">

<!-- Functional image -->
<button aria-label="Search">
  <img src="search-icon.svg" alt="">
</button>

<!-- Complex image -->
<img src="diagram.png" alt="System architecture" aria-describedby="diagram-desc">
<div id="diagram-desc">
  Detailed description of the system architecture showing...
</div>
```

### Guideline 1.2: Time-based Media

**1.2.1 Audio-only and Video-only (Prerecorded) (A)**
Provide alternatives for prerecorded audio-only and video-only content.

**1.2.2 Captions (Prerecorded) (A)**
Provide captions for all prerecorded audio content in synchronized media.

**1.2.3 Audio Description or Media Alternative (Prerecorded) (A)**
Provide audio description or full text alternative for prerecorded video.

**1.2.4 Captions (Live) (AA)**
Provide captions for all live audio content in synchronized media.

**1.2.5 Audio Description (Prerecorded) (AA)**
Provide audio description for all prerecorded video content.

**Implementation:**
```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions-en.vtt" srclang="en" label="English">
  <track kind="descriptions" src="descriptions-en.vtt" srclang="en">
</video>
```

### Guideline 1.3: Adaptable

**1.3.1 Info and Relationships (A)**
Information, structure, and relationships can be programmatically determined.

**Implementation:**
```html
<!-- Use semantic HTML -->
<h1>Main Heading</h1>
<h2>Subheading</h2>
<ul>
  <li>List item</li>
</ul>

<!-- Proper form labels -->
<label for="name">Name</label>
<input type="text" id="name">

<!-- Table headers -->
<table>
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>John Doe</td>
      <td>john@example.com</td>
    </tr>
  </tbody>
</table>
```

**1.3.2 Meaningful Sequence (A)**
When sequence affects meaning, correct reading sequence can be programmatically determined.

**1.3.3 Sensory Characteristics (A)**
Instructions don't rely solely on sensory characteristics (shape, size, location, sound).

**Bad:** "Click the round button on the right"
**Good:** "Click the Submit button"

**1.3.4 Orientation (AA)**
Content doesn't restrict view to single orientation (portrait/landscape) unless essential.

**1.3.5 Identify Input Purpose (AA)**
The purpose of input fields can be programmatically determined when they collect user information.

**Implementation:**
```html
<input type="text" name="email" autocomplete="email">
<input type="tel" name="phone" autocomplete="tel">
<input type="text" name="address" autocomplete="street-address">
```

### Guideline 1.4: Distinguishable

**1.4.1 Use of Color (A)**
Color is not the only visual means of conveying information.

**Implementation:**
```html
<!-- Bad: Color only -->
<span style="color: red;">Required field</span>

<!-- Good: Color + icon + text -->
<span class="required">
  <svg aria-hidden="true"><!-- asterisk icon --></svg>
  Required field
</span>
```

**1.4.3 Contrast (Minimum) (AA)**
- Normal text: 4.5:1 contrast ratio
- Large text (18pt+ or 14pt+ bold): 3:1 contrast ratio

**1.4.6 Contrast (Enhanced) (AAA)**
- Normal text: 7:1 contrast ratio
- Large text: 4.5:1 contrast ratio

**1.4.10 Reflow (AA)**
Content can be presented without horizontal scrolling at 320 CSS pixels width (equivalent to 400% zoom).

**1.4.11 Non-text Contrast (AA)**
UI components and graphical objects have 3:1 contrast ratio against adjacent colors.

**1.4.12 Text Spacing (AA)**
No loss of content or functionality when users adjust:
- Line height to 1.5× font size
- Paragraph spacing to 2× font size
- Letter spacing to 0.12× font size
- Word spacing to 0.16× font size

**1.4.13 Content on Hover or Focus (AA)**
Content that appears on hover/focus is dismissible, hoverable, and persistent.

## Principle 2: Operable

User interface components and navigation must be operable.

### Guideline 2.1: Keyboard Accessible

**2.1.1 Keyboard (A)**
All functionality is available via keyboard.

**2.1.2 No Keyboard Trap (A)**
Keyboard focus can be moved away from any component using only keyboard.

**2.1.4 Character Key Shortcuts (A)**
If single-character shortcuts exist, they can be turned off, remapped, or are only active when component has focus.

**Implementation:**
```javascript
// Provide keyboard support for custom components
button.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault();
    button.click();
  }
});

// Avoid keyboard traps
function trapFocus(container) {
  const focusable = container.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const first = focusable[0];
  const last = focusable[focusable.length - 1];

  container.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeDialog();
    }
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
  });
}
```

### Guideline 2.2: Enough Time

**2.2.1 Timing Adjustable (A)**
Users can turn off, adjust, or extend time limits.

**2.2.2 Pause, Stop, Hide (A)**
Moving, blinking, or auto-updating content can be paused, stopped, or hidden.

### Guideline 2.3: Seizures and Physical Reactions

**2.3.1 Three Flashes or Below Threshold (A)**
Content doesn't flash more than three times per second.

### Guideline 2.4: Navigable

**2.4.1 Bypass Blocks (A)**
Mechanism to skip repeated content blocks.

**Implementation:**
```html
<a href="#main-content" class="skip-link">Skip to main content</a>
<nav><!-- navigation --></nav>
<main id="main-content"><!-- content --></main>
```

**2.4.2 Page Titled (A)**
Web pages have descriptive titles.

**2.4.3 Focus Order (A)**
Focusable components receive focus in an order that preserves meaning.

**2.4.4 Link Purpose (In Context) (A)**
Purpose of each link can be determined from link text or context.

**Bad:** "Click here" | "Read more" | "Learn more"
**Good:** "Read our accessibility policy" | "Learn more about WCAG 2.2"

**2.4.5 Multiple Ways (AA)**
More than one way to locate a page (e.g., search, sitemap, navigation).

**2.4.6 Headings and Labels (AA)**
Headings and labels describe topic or purpose.

**2.4.7 Focus Visible (AA)**
Keyboard focus indicator is visible.

**2.4.11 Focus Not Obscured (Minimum) (AA)** [NEW in 2.2]
When component receives focus, it's not entirely hidden by author-created content.

**2.4.13 Focus Appearance (AAA)** [NEW in 2.2]
Focus indicator has minimum area and contrast.

### Guideline 2.5: Input Modalities

**2.5.1 Pointer Gestures (A)**
Functionality that uses multipoint or path-based gestures has single-pointer alternative.

**2.5.2 Pointer Cancellation (A)**
For single-pointer functionality, at least one is true:
- No down-event
- Abort or undo
- Up reversal
- Essential

**2.5.3 Label in Name (A)**
For UI components with labels, the accessible name contains the visible text.

**2.5.4 Motion Actuation (A)**
Functionality triggered by device motion can be operated by UI components and motion can be disabled.

**2.5.7 Dragging Movements (AA)** [NEW in 2.2]
Functionality that uses dragging has single-pointer alternative without dragging.

**Implementation:**
```javascript
// Provide alternative to drag-and-drop
// Option 1: Keyboard controls
item.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowUp') moveUp(item);
  if (e.key === 'ArrowDown') moveDown(item);
});

// Option 2: Cut/paste buttons
<button onclick="moveUp(item)">Move Up</button>
<button onclick="moveDown(item)">Move Down</button>
```

**2.5.8 Target Size (Minimum) (AA)** [NEW in 2.2]
Target size is at least 24×24 CSS pixels, except when:
- Spacing: Target has sufficient spacing
- Inline: Target is in a sentence or block of text
- User agent control: Size determined by user agent
- Essential: Particular presentation is essential

## Principle 3: Understandable

Information and operation of user interface must be understandable.

### Guideline 3.1: Readable

**3.1.1 Language of Page (A)**
Default language of page can be programmatically determined.

**Implementation:**
```html
<html lang="en">
```

**3.1.2 Language of Parts (AA)**
Language of each passage can be programmatically determined.

```html
<p>The French phrase <span lang="fr">c'est la vie</span> means "that's life."</p>
```

### Guideline 3.2: Predictable

**3.2.1 On Focus (A)**
Receiving focus doesn't initiate change of context.

**3.2.2 On Input (A)**
Changing setting doesn't automatically cause change of context unless user is warned.

**3.2.3 Consistent Navigation (AA)**
Repeated navigation mechanisms occur in same relative order.

**3.2.4 Consistent Identification (AA)**
Components with same functionality are identified consistently.

**3.2.6 Consistent Help (A)** [NEW in 2.2]
Help mechanisms appear in same relative order across pages.

### Guideline 3.3: Input Assistance

**3.3.1 Error Identification (A)**
Errors are identified and described in text.

**3.3.2 Labels or Instructions (A)**
Labels or instructions provided when content requires user input.

**3.3.3 Error Suggestion (AA)**
Suggestions provided when input error is detected (if known).

**3.3.4 Error Prevention (Legal, Financial, Data) (AA)**
For pages causing legal commitments or financial transactions, submissions are reversible, checked, or confirmed.

**3.3.7 Redundant Entry (A)** [NEW in 2.2]
Information previously entered is auto-populated or available for selection.

**3.3.8 Accessible Authentication (Minimum) (AA)** [NEW in 2.2]
Cognitive function test not required for authentication unless alternative provided or mechanism assists.

**Implementation:**
```html
<!-- Support password managers -->
<input type="password" autocomplete="current-password">

<!-- Provide alternative to CAPTCHA -->
<p>Alternative: Email us at support@example.com to verify your account</p>
```

## Principle 4: Robust

Content must be robust enough to be interpreted by assistive technologies.

### Guideline 4.1: Compatible

**4.1.2 Name, Role, Value (A)**
For all UI components, name and role can be programmatically determined; states, properties, and values can be programmatically set.

**Implementation:**
```html
<!-- Custom checkbox -->
<div role="checkbox" 
     aria-checked="false" 
     aria-labelledby="label-id"
     tabindex="0">
</div>
<span id="label-id">Accept terms</span>

<!-- Custom slider -->
<div role="slider" 
     aria-valuemin="0" 
     aria-valuemax="100" 
     aria-valuenow="50"
     aria-label="Volume"
     tabindex="0">
</div>
```

**4.1.3 Status Messages (AA)**
Status messages can be programmatically determined through role or properties.

```html
<div role="status" aria-live="polite">Item added to cart</div>
<div role="alert" aria-live="assertive">Error: Payment failed</div>
```

## WCAG 2.2 Summary by Level

### Level A (30 criteria)
Minimum level of accessibility. Addresses major barriers.

### Level AA (20 additional criteria)
Recommended target. Addresses most common barriers. Required for ADA, Section 508.

### Level AAA (28 additional criteria)
Highest level. Not always achievable for all content. Required for specialized contexts.

## Quick Reference Checklist

**Every Page Must Have:**
- [ ] Valid HTML with proper structure
- [ ] Page title describing content
- [ ] Language attribute on html element
- [ ] Sufficient color contrast (4.5:1 for text)
- [ ] Keyboard accessible (all functionality)
- [ ] Visible focus indicators
- [ ] Skip navigation link
- [ ] Descriptive link text
- [ ] Form labels for all inputs
- [ ] Alt text for all images
- [ ] Proper heading hierarchy (h1, h2, h3...)
- [ ] ARIA roles/attributes for custom components
- [ ] No keyboard traps
- [ ] Content reflows at 200% zoom
- [ ] Error messages are clear and helpful

## Resources

- **Official WCAG 2.2**: https://www.w3.org/TR/WCAG22/
- **Quick Reference**: https://www.w3.org/WAI/WCAG22/quickref/
- **Understanding WCAG 2.2**: https://www.w3.org/WAI/WCAG22/Understanding/
- **Techniques**: https://www.w3.org/WAI/WCAG22/Techniques/
