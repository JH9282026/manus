# Accessibility Implementation Patterns

Practical code patterns for implementing accessible components and interfaces.

## Accessible Forms

### Basic Form Structure

```html
<form>
  <!-- Text input with label -->
  <div class="form-group">
    <label for="name">Full Name</label>
    <input type="text" 
           id="name" 
           name="name" 
           required 
           aria-required="true"
           autocomplete="name">
  </div>

  <!-- Email input with description -->
  <div class="form-group">
    <label for="email">Email Address</label>
    <input type="email" 
           id="email" 
           name="email" 
           required 
           aria-required="true"
           aria-describedby="email-help"
           autocomplete="email">
    <span id="email-help" class="help-text">
      We'll never share your email with anyone else.
    </span>
  </div>

  <!-- Select with label -->
  <div class="form-group">
    <label for="country">Country</label>
    <select id="country" name="country" autocomplete="country">
      <option value="">Select a country</option>
      <option value="us">United States</option>
      <option value="ca">Canada</option>
      <option value="uk">United Kingdom</option>
    </select>
  </div>

  <!-- Checkbox with label -->
  <div class="form-group">
    <input type="checkbox" 
           id="subscribe" 
           name="subscribe">
    <label for="subscribe">Subscribe to newsletter</label>
  </div>

  <!-- Radio buttons with fieldset -->
  <fieldset>
    <legend>Preferred Contact Method</legend>
    <div>
      <input type="radio" id="contact-email" name="contact" value="email">
      <label for="contact-email">Email</label>
    </div>
    <div>
      <input type="radio" id="contact-phone" name="contact" value="phone">
      <label for="contact-phone">Phone</label>
    </div>
  </fieldset>

  <button type="submit">Submit</button>
</form>
```

### Form Validation with Accessible Error Messages

```html
<form id="signup-form" novalidate>
  <div class="form-group">
    <label for="username">Username</label>
    <input type="text" 
           id="username" 
           name="username" 
           required 
           aria-required="true"
           aria-invalid="false"
           aria-describedby="username-error">
    <span id="username-error" class="error" role="alert" aria-live="polite"></span>
  </div>

  <div class="form-group">
    <label for="password">Password</label>
    <input type="password" 
           id="password" 
           name="password" 
           required 
           aria-required="true"
           aria-invalid="false"
           aria-describedby="password-error password-requirements">
    <span id="password-requirements" class="help-text">
      Must be at least 8 characters with one number and one special character.
    </span>
    <span id="password-error" class="error" role="alert" aria-live="polite"></span>
  </div>

  <button type="submit">Create Account</button>
</form>

<script>
const form = document.getElementById('signup-form');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  
  let isValid = true;
  
  // Validate username
  const username = document.getElementById('username');
  const usernameError = document.getElementById('username-error');
  
  if (username.value.trim() === '') {
    username.setAttribute('aria-invalid', 'true');
    usernameError.textContent = 'Username is required.';
    isValid = false;
  } else if (username.value.length < 3) {
    username.setAttribute('aria-invalid', 'true');
    usernameError.textContent = 'Username must be at least 3 characters.';
    isValid = false;
  } else {
    username.setAttribute('aria-invalid', 'false');
    usernameError.textContent = '';
  }
  
  // Validate password
  const password = document.getElementById('password');
  const passwordError = document.getElementById('password-error');
  const passwordRegex = /^(?=.*\d)(?=.*[!@#$%^&*]).{8,}$/;
  
  if (password.value === '') {
    password.setAttribute('aria-invalid', 'true');
    passwordError.textContent = 'Password is required.';
    isValid = false;
  } else if (!passwordRegex.test(password.value)) {
    password.setAttribute('aria-invalid', 'true');
    passwordError.textContent = 'Password must meet requirements.';
    isValid = false;
  } else {
    password.setAttribute('aria-invalid', 'false');
    passwordError.textContent = '';
  }
  
  if (isValid) {
    // Submit form
    form.submit();
  } else {
    // Focus first error
    const firstError = form.querySelector('[aria-invalid="true"]');
    if (firstError) {
      firstError.focus();
    }
  }
});
</script>
```

## Accessible Modals/Dialogs

### Modal Dialog Pattern

```html
<!-- Trigger button -->
<button id="open-dialog">Open Dialog</button>

<!-- Modal dialog -->
<div id="dialog" 
     role="dialog" 
     aria-labelledby="dialog-title" 
     aria-describedby="dialog-desc"
     aria-modal="true"
     class="dialog"
     hidden>
  <div class="dialog-content">
    <h2 id="dialog-title">Confirm Action</h2>
    <p id="dialog-desc">Are you sure you want to delete this item? This action cannot be undone.</p>
    <div class="dialog-actions">
      <button id="dialog-cancel">Cancel</button>
      <button id="dialog-confirm" class="danger">Delete</button>
    </div>
    <button id="dialog-close" aria-label="Close dialog" class="close-button">
      <svg aria-hidden="true" focusable="false"><!-- X icon --></svg>
    </button>
  </div>
</div>

<div id="dialog-backdrop" class="backdrop" hidden></div>

<script>
class AccessibleDialog {
  constructor(dialogId) {
    this.dialog = document.getElementById(dialogId);
    this.backdrop = document.getElementById('dialog-backdrop');
    this.openButton = document.getElementById('open-dialog');
    this.closeButton = document.getElementById('dialog-close');
    this.cancelButton = document.getElementById('dialog-cancel');
    this.confirmButton = document.getElementById('dialog-confirm');
    this.previousFocus = null;
    
    this.init();
  }
  
  init() {
    this.openButton.addEventListener('click', () => this.open());
    this.closeButton.addEventListener('click', () => this.close());
    this.cancelButton.addEventListener('click', () => this.close());
    this.confirmButton.addEventListener('click', () => this.confirm());
    this.backdrop.addEventListener('click', () => this.close());
    
    this.dialog.addEventListener('keydown', (e) => this.handleKeydown(e));
  }
  
  open() {
    // Save current focus
    this.previousFocus = document.activeElement;
    
    // Show dialog
    this.dialog.removeAttribute('hidden');
    this.backdrop.removeAttribute('hidden');
    
    // Prevent body scroll
    document.body.style.overflow = 'hidden';
    
    // Focus first focusable element (close button)
    this.closeButton.focus();
    
    // Trap focus
    this.trapFocus();
  }
  
  close() {
    // Hide dialog
    this.dialog.setAttribute('hidden', '');
    this.backdrop.setAttribute('hidden', '');
    
    // Restore body scroll
    document.body.style.overflow = '';
    
    // Restore focus
    if (this.previousFocus) {
      this.previousFocus.focus();
    }
  }
  
  confirm() {
    // Handle confirmation
    console.log('Confirmed');
    this.close();
  }
  
  handleKeydown(e) {
    if (e.key === 'Escape') {
      this.close();
    }
  }
  
  trapFocus() {
    const focusableElements = this.dialog.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const firstElement = focusableElements[0];
    const lastElement = focusableElements[focusableElements.length - 1];
    
    this.dialog.addEventListener('keydown', (e) => {
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
}

// Initialize dialog
const dialog = new AccessibleDialog('dialog');
</script>

<style>
.dialog {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1000;
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  width: 90%;
}

.backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 999;
}

[hidden] {
  display: none;
}
</style>
```

## Accessible Navigation

### Skip Links

```html
<a href="#main-content" class="skip-link">Skip to main content</a>
<a href="#navigation" class="skip-link">Skip to navigation</a>

<header>
  <nav id="navigation" role="navigation" aria-label="Main navigation">
    <!-- Navigation content -->
  </nav>
</header>

<main id="main-content" tabindex="-1">
  <!-- Main content -->
</main>

<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
  text-decoration: none;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
</style>
```

### Accessible Dropdown Menu

```html
<nav role="navigation" aria-label="Main navigation">
  <ul class="menu">
    <li>
      <a href="/">Home</a>
    </li>
    <li class="has-submenu">
      <button aria-expanded="false" aria-haspopup="true" id="products-button">
        Products
        <svg aria-hidden="true" focusable="false"><!-- chevron icon --></svg>
      </button>
      <ul class="submenu" aria-labelledby="products-button" hidden>
        <li><a href="/products/software">Software</a></li>
        <li><a href="/products/hardware">Hardware</a></li>
        <li><a href="/products/services">Services</a></li>
      </ul>
    </li>
    <li>
      <a href="/about">About</a>
    </li>
  </ul>
</nav>

<script>
class AccessibleDropdown {
  constructor(button) {
    this.button = button;
    this.menu = button.nextElementSibling;
    this.isOpen = false;
    
    this.init();
  }
  
  init() {
    this.button.addEventListener('click', () => this.toggle());
    this.button.addEventListener('keydown', (e) => this.handleButtonKeydown(e));
    this.menu.addEventListener('keydown', (e) => this.handleMenuKeydown(e));
    
    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!this.button.contains(e.target) && !this.menu.contains(e.target)) {
        this.close();
      }
    });
  }
  
  toggle() {
    this.isOpen ? this.close() : this.open();
  }
  
  open() {
    this.button.setAttribute('aria-expanded', 'true');
    this.menu.removeAttribute('hidden');
    this.isOpen = true;
    
    // Focus first menu item
    const firstItem = this.menu.querySelector('a');
    if (firstItem) {
      firstItem.focus();
    }
  }
  
  close() {
    this.button.setAttribute('aria-expanded', 'false');
    this.menu.setAttribute('hidden', '');
    this.isOpen = false;
  }
  
  handleButtonKeydown(e) {
    switch (e.key) {
      case 'Enter':
      case ' ':
      case 'ArrowDown':
        e.preventDefault();
        this.open();
        break;
      case 'Escape':
        this.close();
        break;
    }
  }
  
  handleMenuKeydown(e) {
    const items = Array.from(this.menu.querySelectorAll('a'));
    const currentIndex = items.indexOf(document.activeElement);
    
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        const nextIndex = (currentIndex + 1) % items.length;
        items[nextIndex].focus();
        break;
      case 'ArrowUp':
        e.preventDefault();
        const prevIndex = (currentIndex - 1 + items.length) % items.length;
        items[prevIndex].focus();
        break;
      case 'Escape':
        this.close();
        this.button.focus();
        break;
      case 'Tab':
        this.close();
        break;
    }
  }
}

// Initialize all dropdowns
document.querySelectorAll('[aria-haspopup="true"]').forEach(button => {
  new AccessibleDropdown(button);
});
</script>
```

## Accessible Tabs

```html
<div class="tabs">
  <div role="tablist" aria-label="Account settings">
    <button role="tab" 
            aria-selected="true" 
            aria-controls="panel-1" 
            id="tab-1"
            tabindex="0">
      Profile
    </button>
    <button role="tab" 
            aria-selected="false" 
            aria-controls="panel-2" 
            id="tab-2"
            tabindex="-1">
      Security
    </button>
    <button role="tab" 
            aria-selected="false" 
            aria-controls="panel-3" 
            id="tab-3"
            tabindex="-1">
      Notifications
    </button>
  </div>
  
  <div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
    <h2>Profile Settings</h2>
    <p>Manage your profile information.</p>
  </div>
  
  <div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
    <h2>Security Settings</h2>
    <p>Manage your password and security preferences.</p>
  </div>
  
  <div role="tabpanel" id="panel-3" aria-labelledby="tab-3" hidden>
    <h2>Notification Settings</h2>
    <p>Manage your notification preferences.</p>
  </div>
</div>

<script>
class AccessibleTabs {
  constructor(container) {
    this.container = container;
    this.tablist = container.querySelector('[role="tablist"]');
    this.tabs = Array.from(this.tablist.querySelectorAll('[role="tab"]'));
    this.panels = Array.from(container.querySelectorAll('[role="tabpanel"]'));
    
    this.init();
  }
  
  init() {
    this.tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => this.selectTab(index));
      tab.addEventListener('keydown', (e) => this.handleKeydown(e, index));
    });
  }
  
  selectTab(index) {
    // Deselect all tabs
    this.tabs.forEach((tab, i) => {
      tab.setAttribute('aria-selected', 'false');
      tab.setAttribute('tabindex', '-1');
      this.panels[i].setAttribute('hidden', '');
    });
    
    // Select target tab
    this.tabs[index].setAttribute('aria-selected', 'true');
    this.tabs[index].setAttribute('tabindex', '0');
    this.tabs[index].focus();
    this.panels[index].removeAttribute('hidden');
  }
  
  handleKeydown(e, currentIndex) {
    let newIndex;
    
    switch (e.key) {
      case 'ArrowLeft':
        e.preventDefault();
        newIndex = (currentIndex - 1 + this.tabs.length) % this.tabs.length;
        this.selectTab(newIndex);
        break;
      case 'ArrowRight':
        e.preventDefault();
        newIndex = (currentIndex + 1) % this.tabs.length;
        this.selectTab(newIndex);
        break;
      case 'Home':
        e.preventDefault();
        this.selectTab(0);
        break;
      case 'End':
        e.preventDefault();
        this.selectTab(this.tabs.length - 1);
        break;
    }
  }
}

// Initialize tabs
document.querySelectorAll('.tabs').forEach(container => {
  new AccessibleTabs(container);
});
</script>
```

## Accessible Data Tables

### Simple Table

```html
<table>
  <caption>Employee Directory</caption>
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Department</th>
      <th scope="col">Email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Jane Smith</td>
      <td>Engineering</td>
      <td>jane@example.com</td>
    </tr>
    <tr>
      <td>John Doe</td>
      <td>Marketing</td>
      <td>john@example.com</td>
    </tr>
  </tbody>
</table>
```

### Complex Table with Row and Column Headers

```html
<table>
  <caption>Quarterly Sales by Region</caption>
  <thead>
    <tr>
      <th scope="col">Region</th>
      <th scope="col">Q1 2026</th>
      <th scope="col">Q2 2026</th>
      <th scope="col">Q3 2026</th>
      <th scope="col">Q4 2026</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">North America</th>
      <td>$1.2M</td>
      <td>$1.5M</td>
      <td>$1.8M</td>
      <td>$2.1M</td>
    </tr>
    <tr>
      <th scope="row">Europe</th>
      <td>$800K</td>
      <td>$950K</td>
      <td>$1.1M</td>
      <td>$1.3M</td>
    </tr>
    <tr>
      <th scope="row">Asia Pacific</th>
      <td>$600K</td>
      <td>$750K</td>
      <td>$900K</td>
      <td>$1.0M</td>
    </tr>
  </tbody>
</table>
```

## Accessible Notifications

### Toast Notifications

```html
<div id="toast-container" aria-live="polite" aria-atomic="true" class="toast-container"></div>

<button onclick="showToast('Success! Your changes have been saved.', 'success')">Show Success</button>
<button onclick="showToast('Error: Unable to save changes.', 'error')">Show Error</button>

<script>
function showToast(message, type = 'info') {
  const container = document.getElementById('toast-container');
  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.setAttribute('role', type === 'error' ? 'alert' : 'status');
  toast.textContent = message;
  
  container.appendChild(toast);
  
  // Auto-dismiss after 5 seconds
  setTimeout(() => {
    toast.remove();
  }, 5000);
}
</script>

<style>
.toast-container {
  position: fixed;
  top: 1rem;
  right: 1rem;
  z-index: 1000;
}

.toast {
  background: #333;
  color: #fff;
  padding: 1rem;
  margin-bottom: 0.5rem;
  border-radius: 4px;
  min-width: 250px;
}

.toast-success {
  background: #28a745;
}

.toast-error {
  background: #dc3545;
}
</style>
```

## Resources

- **ARIA Authoring Practices Guide**: https://www.w3.org/WAI/ARIA/apg/
- **Inclusive Components**: https://inclusive-components.design/
- **A11y Style Guide**: https://a11y-style-guide.com/
- **Deque University Code Library**: https://dequeuniversity.com/library/
