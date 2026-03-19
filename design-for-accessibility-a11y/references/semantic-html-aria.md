# Semantic HTML and ARIA Patterns

## Semantic HTML Fundamentals

Semantic HTML uses elements that clearly describe their meaning and purpose to both browsers and developers. This built-in semantics provides crucial information to assistive technologies like screen readers, enabling them to convey the structure and purpose of content to users.

### Why Semantic HTML Matters

1. **Accessibility**: Screen readers and other assistive technologies rely on semantic structure
2. **SEO**: Search engines better understand content hierarchy and importance
3. **Maintainability**: Code is more readable and easier to maintain
4. **Browser Support**: Native elements have built-in keyboard accessibility and behaviors
5. **Performance**: Native elements are optimized by browsers

### Document Structure Elements

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Semantic HTML Example</title>
</head>
<body>
  <!-- Page header with site-wide navigation -->
  <header role="banner">
    <h1>Site Title</h1>
    <nav role="navigation" aria-label="Main navigation">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <!-- Main content area -->
  <main role="main">
    <!-- Primary article -->
    <article>
      <header>
        <h2>Article Title</h2>
        <p>Published on <time datetime="2026-03-17">March 17, 2026</time></p>
      </header>
      
      <section>
        <h3>Section Heading</h3>
        <p>Section content...</p>
      </section>
      
      <footer>
        <p>Author: John Doe</p>
      </footer>
    </article>

    <!-- Sidebar content -->
    <aside role="complementary">
      <h3>Related Articles</h3>
      <ul>
        <li><a href="/article1">Article 1</a></li>
        <li><a href="/article2">Article 2</a></li>
      </ul>
    </aside>
  </main>

  <!-- Page footer -->
  <footer role="contentinfo">
    <p>&copy; 2026 Company Name</p>
  </footer>
</body>
</html>
```

### Heading Hierarchy

Proper heading structure is critical for navigation and understanding:

```html
<!-- Good: Logical hierarchy -->
<h1>Main Page Title</h1>
  <h2>Section 1</h2>
    <h3>Subsection 1.1</h3>
    <h3>Subsection 1.2</h3>
      <h4>Detail 1.2.1</h4>
  <h2>Section 2</h2>
    <h3>Subsection 2.1</h3>

<!-- Bad: Skipping levels -->
<h1>Main Title</h1>
  <h3>Section</h3> <!-- Skipped h2 -->
  <h2>Another Section</h2> <!-- Out of order -->

<!-- Bad: Using headings for styling -->
<h3 class="small-text">Not actually a heading</h3>
<!-- Use CSS for styling instead -->
<p class="heading-style">Styled paragraph</p>
```

### Lists

```html
<!-- Unordered list -->
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>

<!-- Ordered list -->
<ol>
  <li>First step</li>
  <li>Second step</li>
  <li>Third step</li>
</ol>

<!-- Description list -->
<dl>
  <dt>Term 1</dt>
  <dd>Definition of term 1</dd>
  
  <dt>Term 2</dt>
  <dd>Definition of term 2</dd>
</dl>

<!-- Nested lists -->
<ul>
  <li>Parent item
    <ul>
      <li>Child item 1</li>
      <li>Child item 2</li>
    </ul>
  </li>
</ul>
```

### Tables

```html
<table>
  <caption>Quarterly Sales Report 2025</caption>
  <thead>
    <tr>
      <th scope="col">Quarter</th>
      <th scope="col">Revenue</th>
      <th scope="col">Expenses</th>
      <th scope="col">Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Q1</th>
      <td>$1.2M</td>
      <td>$800K</td>
      <td>$400K</td>
    </tr>
    <tr>
      <th scope="row">Q2</th>
      <td>$1.5M</td>
      <td>$900K</td>
      <td>$600K</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th scope="row">Total</th>
      <td>$2.7M</td>
      <td>$1.7M</td>
      <td>$1.0M</td>
    </tr>
  </tfoot>
</table>
```

### Forms

```html
<form action="/submit" method="post">
  <!-- Text input with label -->
  <label for="username">Username</label>
  <input type="text" id="username" name="username" required>

  <!-- Email with description -->
  <label for="email">Email Address</label>
  <input type="email" id="email" name="email" 
         aria-describedby="email-hint" required>
  <span id="email-hint" class="hint">We'll never share your email</span>

  <!-- Password with requirements -->
  <label for="password">Password</label>
  <input type="password" id="password" name="password" 
         aria-describedby="password-requirements" required>
  <div id="password-requirements">
    <ul>
      <li>At least 8 characters</li>
      <li>Include a number</li>
      <li>Include a special character</li>
    </ul>
  </div>

  <!-- Radio buttons -->
  <fieldset>
    <legend>Subscription Type</legend>
    <label>
      <input type="radio" name="subscription" value="free" checked>
      Free
    </label>
    <label>
      <input type="radio" name="subscription" value="premium">
      Premium
    </label>
  </fieldset>

  <!-- Checkboxes -->
  <fieldset>
    <legend>Interests</legend>
    <label>
      <input type="checkbox" name="interests" value="tech">
      Technology
    </label>
    <label>
      <input type="checkbox" name="interests" value="design">
      Design
    </label>
  </fieldset>

  <!-- Select dropdown -->
  <label for="country">Country</label>
  <select id="country" name="country">
    <option value="">Select a country</option>
    <option value="us">United States</option>
    <option value="uk">United Kingdom</option>
    <option value="ca">Canada</option>
  </select>

  <!-- Textarea -->
  <label for="message">Message</label>
  <textarea id="message" name="message" rows="5"></textarea>

  <!-- Submit button -->
  <button type="submit">Submit</button>
</form>
```

## ARIA (Accessible Rich Internet Applications)

### The First Rule of ARIA

**"If you can use a native HTML element or attribute with the semantics and behavior you require already built in, instead of re-purposing an element and adding an ARIA role, state or property to make it accessible, then do so."**

```html
<!-- Good: Native button -->
<button>Click me</button>

<!-- Bad: Div as button -->
<div role="button" tabindex="0" onclick="handleClick()" 
     onkeydown="handleKeyPress(event)">
  Click me
</div>
```

### ARIA Roles

Roles define what an element is or does.

**Landmark Roles:**
```html
<header role="banner">Site header</header>
<nav role="navigation">Navigation</nav>
<main role="main">Main content</main>
<aside role="complementary">Sidebar</aside>
<footer role="contentinfo">Footer</footer>
<form role="search">Search form</form>
<section role="region" aria-labelledby="region-title">
  <h2 id="region-title">Region Title</h2>
</section>
```

**Widget Roles:**
```html
<!-- Button -->
<div role="button" tabindex="0">Custom Button</div>

<!-- Checkbox -->
<div role="checkbox" aria-checked="false" tabindex="0">Option</div>

<!-- Tab interface -->
<div role="tablist">
  <button role="tab" aria-selected="true" aria-controls="panel1">Tab 1</button>
  <button role="tab" aria-selected="false" aria-controls="panel2">Tab 2</button>
</div>
<div role="tabpanel" id="panel1">Panel 1 content</div>
<div role="tabpanel" id="panel2" hidden>Panel 2 content</div>

<!-- Dialog -->
<div role="dialog" aria-labelledby="dialog-title" aria-modal="true">
  <h2 id="dialog-title">Dialog Title</h2>
  <p>Dialog content</p>
  <button>Close</button>
</div>
```

### ARIA States and Properties

**Labeling and Describing:**
```html
<!-- aria-label: Provides accessible name -->
<button aria-label="Close dialog">
  <svg><!-- X icon --></svg>
</button>

<!-- aria-labelledby: References element(s) for name -->
<div role="dialog" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm Action</h2>
</div>

<!-- aria-describedby: Additional description -->
<input type="password" 
       aria-describedby="password-requirements">
<div id="password-requirements">
  Must be at least 8 characters
</div>
```

**Widget States:**
```html
<!-- aria-expanded: Expandable elements -->
<button aria-expanded="false" aria-controls="menu">
  Menu
</button>
<ul id="menu" hidden>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<!-- aria-checked: Checkbox/radio state -->
<div role="checkbox" aria-checked="true">Selected</div>

<!-- aria-selected: Selection state -->
<div role="option" aria-selected="true">Option 1</div>

<!-- aria-pressed: Toggle button state -->
<button aria-pressed="false">Toggle</button>

<!-- aria-hidden: Hide from assistive tech -->
<span aria-hidden="true" class="icon">★</span>
<span class="sr-only">Favorite</span>

<!-- aria-disabled: Disabled state -->
<button aria-disabled="true">Disabled Button</button>

<!-- aria-invalid: Validation state -->
<input type="email" aria-invalid="true" 
       aria-describedby="email-error">
<span id="email-error" role="alert">Invalid email</span>
```

**Relationships:**
```html
<!-- aria-controls: Element controls another -->
<button aria-controls="panel" aria-expanded="false">
  Show Panel
</button>
<div id="panel" hidden>Panel content</div>

<!-- aria-owns: Defines parent-child relationship -->
<div role="listbox" aria-owns="option1 option2">
  <div role="option" id="option1">Option 1</div>
</div>
<div role="option" id="option2">Option 2</div>

<!-- aria-activedescendant: Focus management -->
<div role="combobox" aria-activedescendant="option-2">
  <input type="text">
  <ul role="listbox">
    <li role="option" id="option-1">Option 1</li>
    <li role="option" id="option-2">Option 2</li>
  </ul>
</div>
```

**Live Regions:**
```html
<!-- aria-live: Announce dynamic changes -->
<div aria-live="polite" aria-atomic="true">
  <!-- Updates announced when user is idle -->
</div>

<div aria-live="assertive">
  <!-- Updates announced immediately -->
</div>

<!-- role="alert": Equivalent to aria-live="assertive" -->
<div role="alert">
  Error: Form submission failed
</div>

<!-- role="status": Equivalent to aria-live="polite" -->
<div role="status">
  5 items added to cart
</div>

<!-- aria-atomic: Announce entire region or just changes -->
<div aria-live="polite" aria-atomic="true">
  <!-- Entire content announced -->
</div>

<!-- aria-relevant: What changes to announce -->
<div aria-live="polite" aria-relevant="additions removals">
  <!-- Announce additions and removals, not text changes -->
</div>
```

## Common ARIA Patterns

### Accordion

```html
<div class="accordion">
  <h3>
    <button aria-expanded="false" 
            aria-controls="section1" 
            id="accordion1">
      Section 1
    </button>
  </h3>
  <div id="section1" 
       role="region" 
       aria-labelledby="accordion1" 
       hidden>
    <p>Content for section 1</p>
  </div>

  <h3>
    <button aria-expanded="false" 
            aria-controls="section2" 
            id="accordion2">
      Section 2
    </button>
  </h3>
  <div id="section2" 
       role="region" 
       aria-labelledby="accordion2" 
       hidden>
    <p>Content for section 2</p>
  </div>
</div>

<script>
const buttons = document.querySelectorAll('.accordion button');

buttons.forEach(button => {
  button.addEventListener('click', () => {
    const expanded = button.getAttribute('aria-expanded') === 'true';
    const panel = document.getElementById(button.getAttribute('aria-controls'));
    
    button.setAttribute('aria-expanded', !expanded);
    panel.hidden = expanded;
  });
});
</script>
```

### Modal Dialog

```html
<button onclick="openDialog()">Open Dialog</button>

<div role="dialog" 
     aria-labelledby="dialog-title" 
     aria-describedby="dialog-desc"
     aria-modal="true"
     class="dialog"
     hidden>
  <h2 id="dialog-title">Confirm Action</h2>
  <p id="dialog-desc">Are you sure you want to proceed?</p>
  
  <button onclick="confirmAction()">Confirm</button>
  <button onclick="closeDialog()">Cancel</button>
</div>

<script>
let previousFocus;

function openDialog() {
  const dialog = document.querySelector('[role="dialog"]');
  previousFocus = document.activeElement;
  
  dialog.hidden = false;
  dialog.querySelector('button').focus();
  
  document.addEventListener('keydown', handleDialogKeydown);
}

function closeDialog() {
  const dialog = document.querySelector('[role="dialog"]');
  dialog.hidden = true;
  
  document.removeEventListener('keydown', handleDialogKeydown);
  previousFocus.focus();
}

function handleDialogKeydown(event) {
  if (event.key === 'Escape') {
    closeDialog();
  }
  
  // Trap focus within dialog
  const dialog = document.querySelector('[role="dialog"]');
  const focusableElements = dialog.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];
  
  if (event.key === 'Tab') {
    if (event.shiftKey && document.activeElement === firstElement) {
      event.preventDefault();
      lastElement.focus();
    } else if (!event.shiftKey && document.activeElement === lastElement) {
      event.preventDefault();
      firstElement.focus();
    }
  }
}
</script>
```

### Tabs

```html
<div class="tabs">
  <div role="tablist" aria-label="Sample Tabs">
    <button role="tab" 
            aria-selected="true" 
            aria-controls="panel-1" 
            id="tab-1" 
            tabindex="0">
      Tab 1
    </button>
    <button role="tab" 
            aria-selected="false" 
            aria-controls="panel-2" 
            id="tab-2" 
            tabindex="-1">
      Tab 2
    </button>
    <button role="tab" 
            aria-selected="false" 
            aria-controls="panel-3" 
            id="tab-3" 
            tabindex="-1">
      Tab 3
    </button>
  </div>

  <div role="tabpanel" 
       id="panel-1" 
       aria-labelledby="tab-1" 
       tabindex="0">
    <p>Panel 1 content</p>
  </div>
  <div role="tabpanel" 
       id="panel-2" 
       aria-labelledby="tab-2" 
       tabindex="0" 
       hidden>
    <p>Panel 2 content</p>
  </div>
  <div role="tabpanel" 
       id="panel-3" 
       aria-labelledby="tab-3" 
       tabindex="0" 
       hidden>
    <p>Panel 3 content</p>
  </div>
</div>

<script>
class TabPanel {
  constructor(container) {
    this.container = container;
    this.tabs = container.querySelectorAll('[role="tab"]');
    this.panels = container.querySelectorAll('[role="tabpanel"]');
    
    this.tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => this.selectTab(index));
      tab.addEventListener('keydown', (e) => this.handleKeydown(e, index));
    });
  }
  
  selectTab(index) {
    this.tabs.forEach((tab, i) => {
      const selected = i === index;
      tab.setAttribute('aria-selected', selected);
      tab.tabIndex = selected ? 0 : -1;
      this.panels[i].hidden = !selected;
    });
    
    this.tabs[index].focus();
  }
  
  handleKeydown(event, index) {
    let newIndex = index;
    
    switch(event.key) {
      case 'ArrowRight':
        newIndex = (index + 1) % this.tabs.length;
        break;
      case 'ArrowLeft':
        newIndex = (index - 1 + this.tabs.length) % this.tabs.length;
        break;
      case 'Home':
        newIndex = 0;
        break;
      case 'End':
        newIndex = this.tabs.length - 1;
        break;
      default:
        return;
    }
    
    event.preventDefault();
    this.selectTab(newIndex);
  }
}

new TabPanel(document.querySelector('.tabs'));
</script>
```

## Best Practices

### Do's

1. **Use native HTML elements when possible**
2. **Provide accessible names for all interactive elements**
3. **Maintain logical heading hierarchy**
4. **Associate labels with form inputs**
5. **Use ARIA to enhance, not replace, semantics**
6. **Test with actual assistive technologies**

### Don'ts

1. **Don't override native semantics unnecessarily**
2. **Don't use `aria-hidden` on focusable elements**
3. **Don't use `role="presentation"` on interactive elements**
4. **Don't create keyboard traps**
5. **Don't rely solely on ARIA without testing**

## Conclusion

Semantic HTML provides the foundation for accessible web content, while ARIA enhances complex interactions and dynamic content. Together, they enable assistive technologies to convey meaning, structure, and functionality to all users. The key is using native HTML whenever possible and applying ARIA thoughtfully to fill gaps where HTML alone is insufficient.
