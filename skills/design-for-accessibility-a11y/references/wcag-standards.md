# WCAG Standards and Guidelines

## Overview of WCAG

The Web Content Accessibility Guidelines (WCAG) are international standards developed by the World Wide Web Consortium (W3C) Web Accessibility Initiative (WAI) to define how to make web content more accessible to people with disabilities. These guidelines address a comprehensive range of disabilities including visual, auditory, physical, speech, cognitive, language, learning, and neurological impairments.

## WCAG Versions and Evolution

### WCAG 2.0 (December 2008)
The foundational version that established the POUR principles and the A/AA/AAA conformance model.

### WCAG 2.1 (June 2018)
Added 17 new success criteria focusing on:
- Mobile accessibility
- Low vision users
- Cognitive and learning disabilities

### WCAG 2.2 (Current Standard - 2023)
The latest version adds 9 new success criteria addressing:
- Advanced interaction patterns
- Mobile accessibility improvements
- Cognitive usability enhancements
- Small or touch-screen device support

**New Success Criteria in WCAG 2.2:**
1. **2.4.11 Focus Not Obscured (Minimum)** (AA)
2. **2.4.12 Focus Not Obscured (Enhanced)** (AAA)
3. **2.4.13 Focus Appearance** (AAA)
4. **2.5.7 Dragging Movements** (AA)
5. **2.5.8 Target Size (Minimum)** (AA)
6. **3.2.6 Consistent Help** (A)
7. **3.3.7 Redundant Entry** (A)
8. **3.3.8 Accessible Authentication (Minimum)** (AA)
9. **3.3.9 Accessible Authentication (Enhanced)** (AAA)

### WCAG 3.0 (In Development)
The next generation, also known as "W3C Accessibility Guidelines" (formerly "Silver"), aims to:
- Address more disability types
- Provide clearer testing procedures
- Offer more flexible conformance models
- Better support for mobile and emerging technologies

## The POUR Principles

### 1. Perceivable

Information and user interface components must be presentable to users in ways they can perceive.

**Guideline 1.1 - Text Alternatives**
Provide text alternatives for non-text content.

*Success Criterion 1.1.1 Non-text Content (Level A):*
```html
<!-- Images -->
<img src="chart.png" alt="Sales increased 25% in Q4 2025">

<!-- Decorative images -->
<img src="border.png" alt="" role="presentation">

<!-- Functional images -->
<button>
  <img src="search-icon.svg" alt="Search">
</button>

<!-- Complex images -->
<img src="diagram.png" 
     alt="System architecture" 
     aria-describedby="diagram-description">
<div id="diagram-description">
  Detailed description of the architecture...
</div>
```

**Guideline 1.2 - Time-based Media**
Provide alternatives for time-based media.

*Success Criterion 1.2.1 Audio-only and Video-only (Level A):*
```html
<!-- Audio with transcript -->
<audio controls src="podcast.mp3"></audio>
<details>
  <summary>Transcript</summary>
  <p>Full transcript of audio content...</p>
</details>
```

*Success Criterion 1.2.2 Captions (Prerecorded) (Level A):*
```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions-en.vtt" 
         srclang="en" label="English" default>
</video>
```

*Success Criterion 1.2.5 Audio Description (Prerecorded) (Level AA):*
```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="descriptions" src="descriptions.vtt" srclang="en">
</video>
```

**Guideline 1.3 - Adaptable**
Create content that can be presented in different ways without losing information.

*Success Criterion 1.3.1 Info and Relationships (Level A):*
```html
<!-- Proper heading hierarchy -->
<h1>Main Title</h1>
  <h2>Section</h2>
    <h3>Subsection</h3>

<!-- Proper list structure -->
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<!-- Proper table structure -->
<table>
  <caption>Sales Data 2025</caption>
  <thead>
    <tr>
      <th scope="col">Quarter</th>
      <th scope="col">Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Q1</th>
      <td>$1.2M</td>
    </tr>
  </tbody>
</table>
```

*Success Criterion 1.3.4 Orientation (Level AA):*
```css
/* Don't restrict orientation */
/* Allow both portrait and landscape */
@media (orientation: portrait) {
  /* Responsive layout */
}

@media (orientation: landscape) {
  /* Responsive layout */
}
```

*Success Criterion 1.3.5 Identify Input Purpose (Level AA):*
```html
<input type="email" 
       name="email" 
       autocomplete="email" 
       id="user-email">

<input type="tel" 
       name="phone" 
       autocomplete="tel" 
       id="user-phone">
```

**Guideline 1.4 - Distinguishable**
Make it easier for users to see and hear content.

*Success Criterion 1.4.3 Contrast (Minimum) (Level AA):*
- Normal text: 4.5:1 contrast ratio
- Large text (18pt+ or 14pt+ bold): 3:1 contrast ratio

```css
/* Good contrast examples */
.text {
  color: #1a1a1a; /* Dark gray */
  background: #ffffff; /* White */
  /* Ratio: 16.1:1 (AAA) */
}

.button {
  color: #ffffff;
  background: #0066cc;
  /* Ratio: 7.3:1 (AAA) */
}
```

*Success Criterion 1.4.10 Reflow (Level AA):*
```css
/* Content reflows without horizontal scrolling at 320px width */
.container {
  max-width: 100%;
  overflow-x: hidden;
}

/* Use responsive units */
body {
  font-size: 1rem;
  line-height: 1.5;
}
```

*Success Criterion 1.4.11 Non-text Contrast (Level AA):*
```css
/* UI components and graphics need 3:1 contrast */
button {
  border: 2px solid #767676; /* 3:1 against white */
  background: #ffffff;
}

.icon {
  fill: #595959; /* 3:1 against white */
}
```

*Success Criterion 1.4.12 Text Spacing (Level AA):*
```css
/* Support user-defined text spacing */
* {
  line-height: 1.5 !important;
  letter-spacing: 0.12em !important;
  word-spacing: 0.16em !important;
}

p {
  margin-bottom: 2em !important;
}
```

### 2. Operable

User interface components and navigation must be operable.

**Guideline 2.1 - Keyboard Accessible**
Make all functionality available from a keyboard.

*Success Criterion 2.1.1 Keyboard (Level A):*
```html
<!-- All interactive elements keyboard accessible -->
<button onclick="submit()">Submit</button>

<!-- Custom interactive element -->
<div role="button" 
     tabindex="0" 
     onclick="action()" 
     onkeydown="handleKey(event)">
  Custom Button
</div>

<script>
function handleKey(event) {
  if (event.key === 'Enter' || event.key === ' ') {
    event.preventDefault();
    action();
  }
}
</script>
```

*Success Criterion 2.1.2 No Keyboard Trap (Level A):*
```javascript
// Ensure users can navigate away from all components
function trapFocus(container) {
  const focusableElements = container.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];
  
  container.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        lastElement.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        firstElement.focus();
      }
    }
    
    // Always allow Escape to exit
    if (e.key === 'Escape') {
      closeModal();
    }
  });
}
```

**Guideline 2.2 - Enough Time**
Provide users enough time to read and use content.

*Success Criterion 2.2.1 Timing Adjustable (Level A):*
```javascript
// Provide controls for time limits
class TimedSession {
  constructor(duration) {
    this.duration = duration;
    this.remaining = duration;
    this.warningThreshold = 60; // 60 seconds
  }
  
  start() {
    this.interval = setInterval(() => {
      this.remaining--;
      
      if (this.remaining === this.warningThreshold) {
        this.showWarning();
      }
      
      if (this.remaining <= 0) {
        this.expire();
      }
    }, 1000);
  }
  
  showWarning() {
    const extend = confirm(
      'Your session will expire in 60 seconds. Extend session?'
    );
    
    if (extend) {
      this.extend();
    }
  }
  
  extend() {
    this.remaining += this.duration;
  }
  
  expire() {
    clearInterval(this.interval);
    // Handle expiration
  }
}
```

**Guideline 2.3 - Seizures and Physical Reactions**
Do not design content that causes seizures or physical reactions.

*Success Criterion 2.3.1 Three Flashes or Below Threshold (Level A):*
```javascript
// Avoid flashing more than 3 times per second
function safeFlash(element, duration) {
  const maxFlashesPerSecond = 3;
  const minInterval = 1000 / maxFlashesPerSecond; // 333ms
  
  let flashes = 0;
  const interval = setInterval(() => {
    element.classList.toggle('flash');
    flashes++;
    
    if (flashes >= 6) { // 3 full cycles
      clearInterval(interval);
    }
  }, minInterval);
}
```

**Guideline 2.4 - Navigable**
Provide ways to help users navigate, find content, and determine where they are.

*Success Criterion 2.4.1 Bypass Blocks (Level A):*
```html
<!-- Skip to main content link -->
<a href="#main-content" class="skip-link">
  Skip to main content
</a>

<style>
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
</style>
```

*Success Criterion 2.4.3 Focus Order (Level A):*
```html
<!-- Logical tab order -->
<form>
  <label for="name">Name</label>
  <input type="text" id="name" tabindex="1">
  
  <label for="email">Email</label>
  <input type="email" id="email" tabindex="2">
  
  <button type="submit" tabindex="3">Submit</button>
</form>
```

*Success Criterion 2.4.7 Focus Visible (Level AA):*
```css
/* Visible focus indicator */
:focus-visible {
  outline: 3px solid #4A90E2;
  outline-offset: 2px;
}

/* Don't remove focus outline without replacement */
:focus:not(:focus-visible) {
  outline: none;
}
```

**Guideline 2.5 - Input Modalities**
Make it easier for users to operate functionality through various inputs.

*Success Criterion 2.5.1 Pointer Gestures (Level A):*
```javascript
// Provide alternatives to complex gestures
class AccessibleSlider {
  constructor(element) {
    this.element = element;
    this.setupTouchHandlers();
    this.setupButtonControls(); // Alternative to swiping
  }
  
  setupButtonControls() {
    const prevBtn = document.createElement('button');
    prevBtn.textContent = 'Previous';
    prevBtn.onclick = () => this.previous();
    
    const nextBtn = document.createElement('button');
    nextBtn.textContent = 'Next';
    nextBtn.onclick = () => this.next();
    
    this.element.appendChild(prevBtn);
    this.element.appendChild(nextBtn);
  }
}
```

*Success Criterion 2.5.2 Pointer Cancellation (Level A):*
```javascript
// Execute on mouseup/touchend, not mousedown/touchstart
button.addEventListener('mouseup', (e) => {
  performAction();
});

// Allow cancellation
button.addEventListener('mousedown', (e) => {
  button.classList.add('pressed');
});

button.addEventListener('mouseleave', (e) => {
  button.classList.remove('pressed');
  // Action cancelled if mouse leaves before release
});
```

*Success Criterion 2.5.3 Label in Name (Level A):*
```html
<!-- Visible label matches accessible name -->
<button aria-label="Search products">Search</button>
<!-- Better: -->
<button>Search</button>
```

*Success Criterion 2.5.5 Target Size (Level AAA):*
```css
/* Touch targets at least 44x44 pixels */
button, a {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 16px;
}
```

*Success Criterion 2.5.8 Target Size (Minimum) (Level AA - WCAG 2.2):*
```css
/* Minimum 24x24 pixels for targets */
.icon-button {
  min-width: 24px;
  min-height: 24px;
}
```

### 3. Understandable

Information and operation of the user interface must be understandable.

**Guideline 3.1 - Readable**
Make text content readable and understandable.

*Success Criterion 3.1.1 Language of Page (Level A):*
```html
<html lang="en">
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <p>English content...</p>
    <p lang="es">Contenido en español...</p>
  </body>
</html>
```

**Guideline 3.2 - Predictable**
Make web pages appear and operate in predictable ways.

*Success Criterion 3.2.1 On Focus (Level A):*
```javascript
// Don't trigger actions on focus alone
input.addEventListener('focus', () => {
  // OK: Show help text
  helpText.style.display = 'block';
});

// Bad: Don't submit on focus
input.addEventListener('focus', () => {
  form.submit(); // Unexpected behavior
});
```

*Success Criterion 3.2.4 Consistent Identification (Level AA):*
```html
<!-- Use consistent labels and icons -->
<button aria-label="Search">
  <svg><!-- search icon --></svg>
</button>

<!-- Same icon and label throughout site -->
<button aria-label="Search">
  <svg><!-- same search icon --></svg>
</button>
```

**Guideline 3.3 - Input Assistance**
Help users avoid and correct mistakes.

*Success Criterion 3.3.1 Error Identification (Level A):*
```html
<label for="email">Email</label>
<input type="email" id="email" 
       aria-invalid="true" 
       aria-describedby="email-error">
<span id="email-error" role="alert">
  Please enter a valid email address
</span>
```

*Success Criterion 3.3.2 Labels or Instructions (Level A):*
```html
<label for="password">Password</label>
<input type="password" id="password" 
       aria-describedby="password-requirements">
<div id="password-requirements">
  Password must be at least 8 characters and include
  a number and special character
</div>
```

*Success Criterion 3.3.3 Error Suggestion (Level AA):*
```html
<label for="date">Date of Birth</label>
<input type="date" id="date" 
       aria-invalid="true" 
       aria-describedby="date-error">
<span id="date-error" role="alert">
  Invalid date format. Please use MM/DD/YYYY (e.g., 01/15/1990)
</span>
```

*Success Criterion 3.3.7 Redundant Entry (Level A - WCAG 2.2):*
```javascript
// Auto-fill previously entered information
function autoFillShipping() {
  if (document.getElementById('same-as-billing').checked) {
    document.getElementById('shipping-address').value = 
      document.getElementById('billing-address').value;
  }
}
```

*Success Criterion 3.3.8 Accessible Authentication (Level AA - WCAG 2.2):*
```html
<!-- Don't require cognitive function tests -->
<!-- Bad: CAPTCHA requiring puzzle solving -->

<!-- Good: Alternative authentication -->
<form>
  <label for="email">Email</label>
  <input type="email" id="email" autocomplete="email">
  
  <label for="password">Password</label>
  <input type="password" id="password" autocomplete="current-password">
  
  <!-- Or use passwordless authentication -->
  <button type="button" onclick="sendMagicLink()">Email me a login link</button>
</form>
```

### 4. Robust

Content must be robust enough to be interpreted by a wide variety of user agents, including assistive technologies.

**Guideline 4.1 - Compatible**
Maximize compatibility with current and future user agents, including assistive technologies.

*Success Criterion 4.1.2 Name, Role, Value (Level A):*
```html
<!-- Native elements have built-in name, role, value -->
<button>Submit</button>

<!-- Custom elements need ARIA -->
<div role="button" 
     tabindex="0" 
     aria-pressed="false"
     onclick="toggle()">
  Toggle
</div>
```

*Success Criterion 4.1.3 Status Messages (Level AA):*
```html
<!-- Announce status changes -->
<div role="status" aria-live="polite" aria-atomic="true">
  <!-- Dynamically updated status -->
</div>

<div role="alert" aria-live="assertive">
  <!-- Important alerts -->
</div>

<script>
function updateStatus(message) {
  document.querySelector('[role="status"]').textContent = message;
}

updateStatus('5 items added to cart');
</script>
```

## Conformance Levels

### Level A (Minimum)
Essential accessibility features that, if not met, make content impossible for some users to access.

### Level AA (Standard)
Addresses major barriers and is the recommended target for most organizations. Required by many laws and regulations.

### Level AAA (Enhanced)
Highest level of accessibility. Not recommended as a general policy for entire sites due to difficulty of meeting all criteria for all content.

## Testing for WCAG Compliance

### Automated Testing
```javascript
// Using axe-core
import { axe } from 'axe-core';

axe.run({
  runOnly: {
    type: 'tag',
    values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa']
  }
}).then(results => {
  console.log('Violations:', results.violations);
});
```

### Manual Testing
1. Keyboard navigation
2. Screen reader testing
3. Color contrast verification
4. Content zoom to 200%
5. Form validation
6. Multimedia alternatives

## Conclusion

WCAG provides comprehensive, testable criteria for web accessibility. Understanding and implementing these standards ensures digital content is accessible to the widest possible audience, meeting legal requirements while improving usability for all users.
