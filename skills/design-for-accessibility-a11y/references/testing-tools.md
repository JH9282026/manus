# Accessibility Testing Tools

## Overview

Accessibility testing requires a combination of automated tools and manual testing to ensure comprehensive coverage. While automated tools can detect 20-50% of WCAG issues, manual testing with assistive technologies and human judgment is essential for catching the remaining accessibility barriers.

This guide covers the essential tools, techniques, and workflows for testing web accessibility in 2026.

## Automated Testing Tools

### Browser Extensions

**axe DevTools (Deque)**

The industry-standard browser extension for accessibility testing.

```javascript
// Programmatic usage with axe-core
import { axe } from 'axe-core';

axe.run(document, {
  runOnly: {
    type: 'tag',
    values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']
  }
}).then(results => {
  if (results.violations.length > 0) {
    console.error('Accessibility violations:', results.violations);
    
    results.violations.forEach(violation => {
      console.log(`\n${violation.id}: ${violation.description}`);
      console.log(`Impact: ${violation.impact}`);
      console.log(`Help: ${violation.helpUrl}`);
      
      violation.nodes.forEach(node => {
        console.log(`  Element: ${node.html}`);
        console.log(`  Fix: ${node.failureSummary}`);
      });
    });
  } else {
    console.log('No accessibility violations found!');
  }
});
```

**Features:**
- WCAG 2.2 compliance checking
- Detailed violation reports with remediation guidance
- Integration with CI/CD pipelines
- Available for Chrome, Firefox, Edge

**WAVE (WebAIM)**

Visual feedback tool that highlights accessibility issues directly on the page.

**Features:**
- Visual indicators for errors, alerts, and features
- Color contrast analysis
- Structural/semantic information
- Educational resources
- Available as browser extension and online tool

**Lighthouse (Google)**

Built into Chrome DevTools, provides accessibility audits alongside performance and SEO.

```javascript
// Run Lighthouse programmatically
const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');

async function runLighthouse(url) {
  const chrome = await chromeLauncher.launch({chromeFlags: ['--headless']});
  const options = {
    logLevel: 'info',
    output: 'json',
    onlyCategories: ['accessibility'],
    port: chrome.port
  };
  
  const runnerResult = await lighthouse(url, options);
  const accessibilityScore = runnerResult.lhr.categories.accessibility.score * 100;
  
  console.log(`Accessibility Score: ${accessibilityScore}`);
  
  await chrome.kill();
}

runLighthouse('https://example.com');
```

**Accessibility Insights (Microsoft)**

Comprehensive testing toolkit with guided assessments.

**Features:**
- FastPass for quick automated checks
- Assessment mode for comprehensive WCAG testing
- Tab stops visualization
- Color contrast checker
- Available for web and Windows applications

### Command-Line Tools

**Pa11y**

Automated accessibility testing for CI/CD integration.

```javascript
// pa11y configuration
const pa11y = require('pa11y');

async function testAccessibility(url) {
  try {
    const results = await pa11y(url, {
      standard: 'WCAG2AA',
      runners: ['axe', 'htmlcs'],
      includeNotices: true,
      includeWarnings: true,
      chromeLaunchConfig: {
        args: ['--no-sandbox']
      }
    });
    
    console.log(`Issues found: ${results.issues.length}`);
    
    results.issues.forEach(issue => {
      console.log(`\n${issue.type}: ${issue.message}`);
      console.log(`Code: ${issue.code}`);
      console.log(`Selector: ${issue.selector}`);
      console.log(`Context: ${issue.context}`);
    });
    
    return results;
  } catch (error) {
    console.error('Error running pa11y:', error);
  }
}

testAccessibility('https://example.com');
```

**Pa11y CI for multiple pages:**

```json
// .pa11yci.json
{
  "defaults": {
    "standard": "WCAG2AA",
    "runners": ["axe", "htmlcs"],
    "chromeLaunchConfig": {
      "args": ["--no-sandbox"]
    }
  },
  "urls": [
    "https://example.com",
    "https://example.com/about",
    "https://example.com/contact"
  ]
}
```

```bash
# Run pa11y-ci
npx pa11y-ci
```

**axe-core CLI**

```bash
# Install
npm install -g @axe-core/cli

# Run tests
axe https://example.com --tags wcag2a,wcag2aa,wcag21aa,wcag22aa

# Save results
axe https://example.com --save results.json
```

### Integration Testing

**Jest + jest-axe**

```javascript
import { axe, toHaveNoViolations } from 'jest-axe';
import { render } from '@testing-library/react';
import MyComponent from './MyComponent';

expect.extend(toHaveNoViolations);

describe('MyComponent accessibility', () => {
  it('should not have accessibility violations', async () => {
    const { container } = render(<MyComponent />);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });
  
  it('should have proper heading hierarchy', async () => {
    const { container } = render(<MyComponent />);
    const results = await axe(container, {
      rules: {
        'heading-order': { enabled: true }
      }
    });
    expect(results).toHaveNoViolations();
  });
});
```

**Cypress + cypress-axe**

```javascript
// cypress/support/commands.js
import 'cypress-axe';

// cypress/e2e/accessibility.cy.js
describe('Accessibility tests', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.injectAxe();
  });
  
  it('Has no detectable accessibility violations on load', () => {
    cy.checkA11y();
  });
  
  it('Has no accessibility violations after interaction', () => {
    cy.get('button').click();
    cy.checkA11y();
  });
  
  it('Checks specific element', () => {
    cy.checkA11y('.main-content');
  });
  
  it('Excludes specific elements', () => {
    cy.checkA11y(null, {
      exclude: [['.third-party-widget']]
    });
  });
  
  it('Tests specific rules', () => {
    cy.checkA11y(null, {
      runOnly: {
        type: 'tag',
        values: ['wcag2a', 'wcag2aa']
      }
    });
  });
});
```

**Playwright + @axe-core/playwright**

```javascript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Accessibility tests', () => {
  test('should not have accessibility violations', async ({ page }) => {
    await page.goto('https://example.com');
    
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'])
      .analyze();
    
    expect(accessibilityScanResults.violations).toEqual([]);
  });
  
  test('should not have violations after interaction', async ({ page }) => {
    await page.goto('https://example.com');
    await page.click('button');
    
    const accessibilityScanResults = await new AxeBuilder({ page })
      .analyze();
    
    expect(accessibilityScanResults.violations).toEqual([]);
  });
});
```

## Manual Testing Tools

### Screen Readers

**NVDA (Windows - Free)**

```
Common NVDA Commands:
- NVDA + Down Arrow: Read next line
- NVDA + Up Arrow: Read previous line
- H: Next heading
- Shift + H: Previous heading
- 1-6: Jump to heading level
- K: Next link
- Shift + K: Previous link
- F: Next form field
- B: Next button
- T: Next table
- NVDA + F7: Elements list
- Insert + Space: Toggle browse/focus mode
```

**JAWS (Windows - Commercial)**

```
Common JAWS Commands:
- Down Arrow: Read next line
- Up Arrow: Read previous line
- H: Next heading
- Shift + H: Previous heading
- T: Next table
- Ctrl: Stop reading
- Insert + F5: Form fields list
- Insert + F6: Headings list
- Insert + F7: Links list
```

**VoiceOver (macOS/iOS - Built-in)**

```
macOS VoiceOver Commands:
- VO + A: Start reading
- VO + Right Arrow: Next item
- VO + Left Arrow: Previous item
- VO + Command + H: Next heading
- VO + Command + Shift + H: Previous heading
- VO + Command + L: Next link
- VO + U: Rotor (navigation menu)
- VO + Space: Activate item

iOS VoiceOver Gestures:
- Swipe right: Next item
- Swipe left: Previous item
- Double tap: Activate
- Two-finger swipe up: Read all from top
- Rotor: Rotate two fingers
```

**TalkBack (Android - Built-in)**

```
TalkBack Gestures:
- Swipe right: Next item
- Swipe left: Previous item
- Double tap: Activate
- Swipe down then right: Read from top
- Swipe up then down: Reading controls menu
```

### Browser Developer Tools

**Chrome DevTools Accessibility Features**

```javascript
// Accessibility tree inspection
// DevTools > Elements > Accessibility pane

// Emulate vision deficiencies
// DevTools > Rendering > Emulate vision deficiencies
// - Blurred vision
// - Protanopia (red-blind)
// - Deuteranopia (green-blind)
// - Tritanopia (blue-blind)
// - Achromatopsia (total color blindness)

// CSS Overview for contrast issues
// DevTools > CSS Overview > Capture overview
// Shows all contrast issues on the page
```

**Firefox Accessibility Inspector**

```
Features:
- Accessibility tree view
- Check for issues (contrast, keyboard, text labels)
- Simulate color vision deficiencies
- Show tabbing order
- Highlight accessibility issues
```

### Color Contrast Tools

**WebAIM Contrast Checker**

```javascript
// Calculate contrast ratio
function getContrastRatio(color1, color2) {
  const l1 = getRelativeLuminance(color1);
  const l2 = getRelativeLuminance(color2);
  
  const lighter = Math.max(l1, l2);
  const darker = Math.min(l1, l2);
  
  return (lighter + 0.05) / (darker + 0.05);
}

function getRelativeLuminance(rgb) {
  const [r, g, b] = rgb.map(val => {
    val = val / 255;
    return val <= 0.03928 
      ? val / 12.92 
      : Math.pow((val + 0.055) / 1.055, 2.4);
  });
  
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

// Check if contrast meets WCAG requirements
function meetsWCAG(ratio, level, isLargeText) {
  if (level === 'AA') {
    return isLargeText ? ratio >= 3 : ratio >= 4.5;
  } else if (level === 'AAA') {
    return isLargeText ? ratio >= 4.5 : ratio >= 7;
  }
  return false;
}

// Usage
const ratio = getContrastRatio([0, 102, 204], [255, 255, 255]);
console.log(`Contrast ratio: ${ratio.toFixed(2)}:1`);
console.log(`Meets WCAG AA: ${meetsWCAG(ratio, 'AA', false)}`);
```

**Color Oracle**

Desktop application that simulates color blindness in real-time.

### Keyboard Testing

**Manual Keyboard Testing Checklist:**

```javascript
// Automated keyboard navigation test
class KeyboardNavigationTester {
  constructor() {
    this.focusableElements = [];
    this.currentIndex = 0;
  }
  
  findFocusableElements() {
    this.focusableElements = Array.from(
      document.querySelectorAll(
        'a[href], button:not([disabled]), input:not([disabled]), ' +
        'select:not([disabled]), textarea:not([disabled]), ' +
        '[tabindex]:not([tabindex="-1"])'
      )
    );
    return this.focusableElements;
  }
  
  testTabOrder() {
    const elements = this.findFocusableElements();
    const results = [];
    
    elements.forEach((el, index) => {
      const tabIndex = el.tabIndex;
      const isVisible = this.isVisible(el);
      const hasFocusIndicator = this.hasFocusIndicator(el);
      
      results.push({
        element: el,
        index,
        tabIndex,
        isVisible,
        hasFocusIndicator,
        issues: []
      });
      
      if (!isVisible) {
        results[index].issues.push('Element not visible but focusable');
      }
      
      if (!hasFocusIndicator) {
        results[index].issues.push('No visible focus indicator');
      }
    });
    
    return results;
  }
  
  isVisible(el) {
    const style = window.getComputedStyle(el);
    return style.display !== 'none' && 
           style.visibility !== 'hidden' && 
           style.opacity !== '0';
  }
  
  hasFocusIndicator(el) {
    el.focus();
    const style = window.getComputedStyle(el);
    return style.outline !== 'none' && style.outlineWidth !== '0px';
  }
}

const tester = new KeyboardNavigationTester();
const results = tester.testTabOrder();
console.table(results);
```

## Testing Workflow

### Comprehensive Testing Checklist

```markdown
## Automated Testing
- [ ] Run axe DevTools on all pages
- [ ] Run Lighthouse accessibility audit
- [ ] Check WAVE for visual feedback
- [ ] Run Pa11y in CI/CD pipeline
- [ ] Review automated test results

## Keyboard Testing
- [ ] Tab through all interactive elements
- [ ] Verify logical tab order
- [ ] Check visible focus indicators
- [ ] Test keyboard shortcuts
- [ ] Verify no keyboard traps
- [ ] Test skip links

## Screen Reader Testing
- [ ] Test with NVDA (Windows)
- [ ] Test with JAWS (Windows)
- [ ] Test with VoiceOver (macOS/iOS)
- [ ] Test with TalkBack (Android)
- [ ] Verify all content announced
- [ ] Check landmark navigation
- [ ] Verify form labels
- [ ] Test dynamic content updates

## Visual Testing
- [ ] Check color contrast (4.5:1 minimum)
- [ ] Test at 200% zoom
- [ ] Verify no information by color alone
- [ ] Test with vision deficiency simulations
- [ ] Check text spacing adjustability
- [ ] Verify responsive design

## Content Testing
- [ ] Verify heading hierarchy
- [ ] Check alt text for images
- [ ] Verify captions for videos
- [ ] Check transcripts for audio
- [ ] Verify form error messages
- [ ] Check link text clarity

## Interaction Testing
- [ ] Test all forms
- [ ] Verify error handling
- [ ] Test modals and dialogs
- [ ] Check accordions and tabs
- [ ] Test carousels and sliders
- [ ] Verify drag-and-drop alternatives
```

### CI/CD Integration

```yaml
# GitHub Actions example
name: Accessibility Tests

on: [push, pull_request]

jobs:
  a11y:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Node
        uses: actions/setup-node@v2
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build
        run: npm run build
      
      - name: Start server
        run: npm start &
        
      - name: Wait for server
        run: npx wait-on http://localhost:3000
      
      - name: Run Pa11y
        run: npx pa11y-ci
      
      - name: Run axe
        run: npx @axe-core/cli http://localhost:3000
      
      - name: Upload results
        if: failure()
        uses: actions/upload-artifact@v2
        with:
          name: accessibility-results
          path: pa11y-results/
```

## Conclusion

Effective accessibility testing combines automated tools for quick detection of common issues with manual testing using assistive technologies for comprehensive coverage. Integrating accessibility testing into development workflows ensures issues are caught early, reducing remediation costs and improving the overall quality of digital experiences.

The key is establishing a consistent testing process that includes automated checks in CI/CD, regular manual testing with screen readers and keyboards, and periodic comprehensive audits to ensure ongoing compliance and usability for all users.
