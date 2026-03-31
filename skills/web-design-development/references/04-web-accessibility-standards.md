# Web Accessibility Standards and Best Practices

## Introduction to Web Accessibility

Web accessibility (a11y) ensures that websites, tools, and technologies are designed and developed so that people with disabilities can use them. This includes people with auditory, cognitive, neurological, physical, speech, and visual disabilities.

### Why Accessibility Matters

1. **Legal Compliance**: ADA, Section 508, AODA, European Accessibility Act
2. **Inclusive Design**: Reaches wider audience (15% of global population)
3. **Better UX**: Improves usability for everyone
4. **SEO Benefits**: Better structure and semantics
5. **Business Value**: Larger market reach, better brand reputation

## WCAG Guidelines

### WCAG 2.1 Principles (POUR)

#### 1. Perceivable

Information and user interface components must be presentable to users in ways they can perceive.

**Text Alternatives**
```html
<!-- Images -->
<img src="logo.png" alt="Company Name Logo">

<!-- Decorative images -->
<img src="decoration.png" alt="" role="presentation">

<!-- Complex images -->
<img src="chart.png" alt="Sales chart" aria-describedby="chart-description">
<div id="chart-description">
  Sales increased from $1M in Q1 to $2.5M in Q4.
</div>

<!-- Icons with text -->
<button>
  <svg aria-hidden="true" focusable="false">...</svg>
  <span>Save</span>
</button>

<!-- Icon-only buttons -->
<button aria-label="Close dialog">
  <svg aria-hidden="true">...</svg>
</button>
```

**Time-Based Media**
```html
<!-- Video with captions and audio description -->
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions-en.vtt" srclang="en" label="English">
  <track kind="descriptions" src="descriptions-en.vtt" srclang="en">
  <track kind="subtitles" src="subtitles-es.vtt" srclang="es" label="Español">
</video>

<!-- Audio with transcript -->
<audio controls>
  <source src="podcast.mp3" type="audio/mpeg">
</audio>
<details>
  <summary>Transcript</summary>
  <p>Full transcript of the audio content...</p>
</details>
```

**Adaptable Content**
```html
<!-- Semantic HTML -->
<article>
  <header>
    <h1>Article Title</h1>
    <p>By <span class="author">John Doe</span></p>
    <time datetime="2024-03-31">March 31, 2024</time>
  </header>
  
  <section>
    <h2>Section Heading</h2>
    <p>Content...</p>
  </section>
  
  <footer>
    <p>Tags: <a href="/tag/web">Web</a></p>
  </footer>
</article>

<!-- Proper heading hierarchy -->
<h1>Main Page Title</h1>
  <h2>Section 1</h2>
    <h3>Subsection 1.1</h3>
    <h3>Subsection 1.2</h3>
  <h2>Section 2</h2>
    <h3>Subsection 2.1</h3>
```

**Distinguishable**
```css
/* Color contrast (WCAG AA: 4.5:1 for normal text, 3:1 for large text) */
.text-on-light {
  color: #212529;           /* 16.1:1 contrast ratio */
  background: #ffffff;
}

.text-on-dark {
  color: #ffffff;           /* 21:1 contrast ratio */
  background: #000000;
}

/* Don't rely on color alone */
.error {
  color: #dc3545;
  border-left: 4px solid #dc3545;
}

.error::before {
  content: "⚠ ";
  font-weight: bold;
}

/* Focus indicators */
a:focus,
button:focus,
input:focus {
  outline: 2px solid #007bff;
  outline-offset: 2px;
}

/* Text spacing */
p {
  line-height: 1.5;         /* At least 1.5 */
  letter-spacing: 0.12em;   /* At least 0.12em */
  word-spacing: 0.16em;     /* At least 0.16em */
}

h1, h2, h3 {
  margin-bottom: 0.5em;     /* At least 0.5em */
}
```

#### 2. Operable

User interface components and navigation must be operable.

**Keyboard Accessible**
```html
<!-- All interactive elements must be keyboard accessible -->
<button onclick="handleClick()">Accessible Button</button>

<!-- Custom interactive elements need tabindex and keyboard handlers -->
<div 
  role="button" 
  tabindex="0"
  onclick="handleClick()"
  onkeydown="handleKeyDown(event)"
>
  Custom Button
</div>

<!-- Skip links -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<nav>...</nav>

<main id="main-content">
  <h1>Main Content</h1>
</main>
```

```css
/* Skip link styling */
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
```

```javascript
// Keyboard event handling
function handleKeyDown(event) {
  // Enter or Space activates button
  if (event.key === 'Enter' || event.key === ' ') {
    event.preventDefault();
    handleClick();
  }
}

// Trap focus in modal
function trapFocus(element) {
  const focusableElements = element.querySelectorAll(
    'a[href], button, textarea, input, select, [tabindex]:not([tabindex="-1"])'
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

**Enough Time**
```html
<!-- Provide controls for time limits -->
<div role="alert" aria-live="polite">
  <p>Your session will expire in <span id="timer">5:00</span></p>
  <button onclick="extendSession()">Extend Session</button>
</div>

<!-- Pause, stop, hide for moving content -->
<div class="carousel">
  <button aria-label="Pause carousel">⏸</button>
  <button aria-label="Play carousel">▶</button>
</div>
```

**Seizures and Physical Reactions**
```css
/* Avoid flashing content more than 3 times per second */
/* Respect prefers-reduced-motion */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Navigable**
```html
<!-- Descriptive page titles -->
<title>Contact Us - Company Name</title>

<!-- Logical focus order (use natural DOM order) -->
<form>
  <label for="name">Name:</label>
  <input id="name" type="text">
  
  <label for="email">Email:</label>
  <input id="email" type="email">
  
  <button type="submit">Submit</button>
</form>

<!-- Descriptive link text -->
<!-- Bad -->
<a href="/article">Click here</a>

<!-- Good -->
<a href="/article">Read our accessibility guide</a>

<!-- Multiple navigation mechanisms -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>

<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/products">Products</a></li>
    <li aria-current="page">Product Name</li>
  </ol>
</nav>

<!-- Landmarks -->
<header role="banner">...</header>
<nav role="navigation">...</nav>
<main role="main">...</main>
<aside role="complementary">...</aside>
<footer role="contentinfo">...</footer>
```

#### 3. Understandable

Information and operation of user interface must be understandable.

**Readable**
```html
<!-- Language of page -->
<html lang="en">

<!-- Language of parts -->
<p>The French phrase <span lang="fr">Bonjour</span> means hello.</p>

<!-- Abbreviations -->
<abbr title="World Wide Web Consortium">W3C</abbr>

<!-- Definitions -->
<dfn>Accessibility</dfn> means ensuring equal access for people with disabilities.
```

**Predictable**
```html
<!-- Consistent navigation -->
<nav aria-label="Main navigation">
  <!-- Same order on every page -->
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>

<!-- No automatic context changes -->
<!-- Bad: Auto-submit on select -->
<select onchange="this.form.submit()">
  <option>Choose...</option>
</select>

<!-- Good: Explicit submit -->
<select id="country">
  <option>Choose...</option>
</select>
<button type="submit">Go</button>
```

**Input Assistance**
```html
<!-- Labels for form controls -->
<label for="email">Email Address:</label>
<input 
  id="email" 
  type="email" 
  required 
  aria-describedby="email-hint"
>
<span id="email-hint">We'll never share your email.</span>

<!-- Error identification -->
<form>
  <div class="form-group" aria-invalid="true">
    <label for="username">Username:</label>
    <input 
      id="username" 
      type="text" 
      aria-describedby="username-error"
    >
    <span id="username-error" role="alert">
      Username must be at least 3 characters.
    </span>
  </div>
</form>

<!-- Error prevention -->
<form>
  <h2>Review Your Order</h2>
  <dl>
    <dt>Item:</dt>
    <dd>Product Name</dd>
    <dt>Quantity:</dt>
    <dd>2</dd>
    <dt>Total:</dt>
    <dd>$50.00</dd>
  </dl>
  
  <button type="button" onclick="history.back()">Edit Order</button>
  <button type="submit">Confirm Purchase</button>
</form>
```

#### 4. Robust

Content must be robust enough to be interpreted by a wide variety of user agents, including assistive technologies.

**Compatible**
```html
<!-- Valid HTML -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title</title>
</head>
<body>
  <!-- Properly nested and closed elements -->
  <div>
    <p>Content</p>
  </div>
</body>
</html>

<!-- Unique IDs -->
<label for="first-name">First Name:</label>
<input id="first-name" type="text">

<label for="last-name">Last Name:</label>
<input id="last-name" type="text">

<!-- Name, Role, Value for custom components -->
<div 
  role="checkbox" 
  aria-checked="false"
  aria-labelledby="checkbox-label"
  tabindex="0"
>
  <span id="checkbox-label">Accept terms</span>
</div>
```

## ARIA (Accessible Rich Internet Applications)

### ARIA Roles

```html
<!-- Landmark roles -->
<header role="banner">...</header>
<nav role="navigation">...</nav>
<main role="main">...</main>
<aside role="complementary">...</aside>
<footer role="contentinfo">...</footer>
<form role="search">...</form>

<!-- Widget roles -->
<div role="button" tabindex="0">Custom Button</div>
<div role="checkbox" aria-checked="false">Custom Checkbox</div>
<div role="tab" aria-selected="true">Tab 1</div>
<div role="tabpanel">Tab content</div>
<div role="dialog" aria-modal="true">Modal Dialog</div>
<div role="alert">Important message</div>
<div role="status">Status update</div>
```

### ARIA Properties and States

```html
<!-- Labels and descriptions -->
<button aria-label="Close dialog">×</button>
<input aria-labelledby="label-id" aria-describedby="hint-id">

<!-- States -->
<button aria-pressed="true">Bold</button>
<div role="checkbox" aria-checked="mixed">Select All</div>
<button aria-expanded="false" aria-controls="menu">Menu</button>
<input aria-invalid="true" aria-errormessage="error-id">
<div aria-hidden="true">Hidden from screen readers</div>
<div aria-live="polite">Dynamic content</div>
<div aria-atomic="true">Read entire region on change</div>

<!-- Relationships -->
<div role="tablist">
  <button role="tab" aria-controls="panel-1" aria-selected="true">Tab 1</button>
  <button role="tab" aria-controls="panel-2" aria-selected="false">Tab 2</button>
</div>
<div role="tabpanel" id="panel-1">Content 1</div>
<div role="tabpanel" id="panel-2" hidden>Content 2</div>
```

### Live Regions

```html
<!-- Polite: Announce when user is idle -->
<div aria-live="polite" aria-atomic="true">
  <p>3 new messages</p>
</div>

<!-- Assertive: Announce immediately -->
<div aria-live="assertive" role="alert">
  <p>Error: Form submission failed</p>
</div>

<!-- Status updates -->
<div role="status" aria-live="polite">
  <p>Saving...</p>
</div>
```

## Accessible Components

### Modal Dialog

```html
<div 
  role="dialog" 
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-description"
  class="modal"
>
  <h2 id="dialog-title">Confirm Action</h2>
  <p id="dialog-description">Are you sure you want to proceed?</p>
  
  <button onclick="confirmAction()">Confirm</button>
  <button onclick="closeDialog()">Cancel</button>
</div>
```

```javascript
function openDialog() {
  const dialog = document.querySelector('.modal');
  const previousFocus = document.activeElement;
  
  dialog.style.display = 'block';
  dialog.querySelector('button').focus();
  trapFocus(dialog);
  
  // Return focus on close
  dialog.addEventListener('close', () => {
    previousFocus.focus();
  });
}
```

### Accordion

```html
<div class="accordion">
  <h3>
    <button 
      aria-expanded="false"
      aria-controls="section1"
      id="accordion1"
    >
      Section 1
    </button>
  </h3>
  <div id="section1" role="region" aria-labelledby="accordion1" hidden>
    <p>Content for section 1</p>
  </div>
</div>
```

### Tabs

```html
<div class="tabs">
  <div role="tablist" aria-label="Sample Tabs">
    <button role="tab" aria-selected="true" aria-controls="panel-1" id="tab-1">
      Tab 1
    </button>
    <button role="tab" aria-selected="false" aria-controls="panel-2" id="tab-2">
      Tab 2
    </button>
  </div>
  
  <div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
    <p>Content 1</p>
  </div>
  
  <div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
    <p>Content 2</p>
  </div>
</div>
```

## Testing Accessibility

### Automated Testing Tools

```javascript
// axe-core
import { axe } from 'axe-core';

axe.run(document, (err, results) => {
  if (err) throw err;
  console.log(results.violations);
});

// Pa11y
const pa11y = require('pa11y');

pa11y('https://example.com').then(results => {
  console.log(results.issues);
});
```

### Manual Testing Checklist

1. ✅ Keyboard navigation (Tab, Shift+Tab, Enter, Space, Arrow keys)
2. ✅ Screen reader testing (NVDA, JAWS, VoiceOver)
3. ✅ Color contrast (4.5:1 for normal text, 3:1 for large text)
4. ✅ Zoom to 200% without loss of functionality
5. ✅ Forms have labels and error messages
6. ✅ Images have alt text
7. ✅ Videos have captions
8. ✅ Headings are in logical order
9. ✅ Focus indicators are visible
10. ✅ No keyboard traps

## Conclusion

Web accessibility is not optional—it's a fundamental requirement for inclusive web development. Key principles:

1. **Semantic HTML**: Use proper elements for their intended purpose
2. **Keyboard Access**: All functionality available via keyboard
3. **ARIA**: Enhance semantics when HTML isn't enough
4. **Testing**: Combine automated tools with manual testing
5. **Continuous**: Accessibility is an ongoing process

By following WCAG guidelines and implementing these best practices, you create websites that are usable by everyone, regardless of ability.
