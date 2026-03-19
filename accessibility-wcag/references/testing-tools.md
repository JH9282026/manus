# Accessibility Testing Tools

Comprehensive guide to automated and manual accessibility testing tools.

## Automated Testing Tools

### Browser Extensions

#### axe DevTools
**Best for:** In-page accessibility scanning

**Features:**
- Detects WCAG 2.0, 2.1, 2.2 violations
- Highlights issues directly on page
- Provides remediation guidance
- Intelligent Guided Tests for complex issues
- Export reports (PDF, CSV, JSON)

**Installation:**
- Chrome: [Chrome Web Store](https://chrome.google.com/webstore)
- Firefox: [Firefox Add-ons](https://addons.mozilla.org)
- Edge: [Edge Add-ons](https://microsoftedge.microsoft.com/addons)

**Usage:**
1. Open DevTools (F12)
2. Navigate to "axe DevTools" tab
3. Click "Scan ALL of my page"
4. Review issues by severity (Critical, Serious, Moderate, Minor)
5. Click issue for details and remediation guidance

**Pros:**
- Most comprehensive automated testing
- Excellent documentation
- Low false positive rate
- Free tier available

**Cons:**
- Pro features require license
- Can't detect all accessibility issues (manual testing still needed)

#### WAVE (Web Accessibility Evaluation Tool)
**Best for:** Visual feedback on accessibility issues

**Features:**
- Visual indicators overlaid on page
- Color-coded icons for errors, alerts, features
- Contrast checker
- Structure/order view
- No registration required

**Installation:**
- Chrome: [Chrome Web Store](https://chrome.google.com/webstore)
- Firefox: [Firefox Add-ons](https://addons.mozilla.org)
- Edge: [Edge Add-ons](https://microsoftedge.microsoft.com/addons)

**Usage:**
1. Click WAVE extension icon
2. Review icons overlaid on page
3. Click icons for details
4. Use sidebar to filter by type
5. Check "Contrast" tab for color issues

**Pros:**
- Completely free
- Excellent visual feedback
- Easy to understand
- Great for beginners

**Cons:**
- Less detailed than axe DevTools
- Can clutter complex pages

#### Lighthouse
**Best for:** Overall site quality including accessibility

**Features:**
- Built into Chrome DevTools
- Accessibility score (0-100)
- Performance, SEO, best practices audits
- Mobile and desktop testing
- Automated and manual checks

**Usage:**
1. Open Chrome DevTools (F12)
2. Navigate to "Lighthouse" tab
3. Select "Accessibility" category
4. Click "Analyze page load"
5. Review score and specific issues

**Pros:**
- Built into Chrome (no installation)
- Comprehensive site audit
- Clear scoring system
- CI/CD integration available

**Cons:**
- Less detailed than specialized tools
- Focuses on automated checks only

#### IBM Equal Access Accessibility Checker
**Best for:** IBM accessibility requirements

**Features:**
- Checks against WCAG, IBM standards
- Element-level scanning
- Accessibility assessment
- Keyboard checker
- Multi-tab scanning

**Installation:**
- Chrome: [Chrome Web Store](https://chrome.google.com/webstore)
- Firefox: [Firefox Add-ons](https://addons.mozilla.org)

**Pros:**
- Free and open source
- Detailed element inspection
- Good for enterprise compliance

**Cons:**
- Interface less intuitive than competitors
- Smaller user community

### Command-Line Tools

#### Pa11y
**Best for:** CI/CD integration and automated testing

**Installation:**
```bash
npm install -g pa11y
```

**Usage:**
```bash
# Test single page
pa11y https://example.com

# Test with specific standard
pa11y --standard WCAG2AA https://example.com

# Output as JSON
pa11y --reporter json https://example.com > results.json

# Test with authentication
pa11y --header "Cookie: session=abc123" https://example.com

# Screenshot on error
pa11y --screen-capture error.png https://example.com
```

**Configuration file (`.pa11yrc`):**
```json
{
  "standard": "WCAG2AA",
  "timeout": 10000,
  "wait": 1000,
  "chromeLaunchConfig": {
    "args": ["--no-sandbox"]
  },
  "ignore": [
    "WCAG2AA.Principle1.Guideline1_4.1_4_3.G18.Fail"
  ]
}
```

**Pa11y CI (test multiple URLs):**
```bash
npm install -g pa11y-ci
```

**Configuration (`.pa11yci.json`):**
```json
{
  "defaults": {
    "standard": "WCAG2AA",
    "timeout": 10000
  },
  "urls": [
    "https://example.com",
    "https://example.com/about",
    "https://example.com/contact"
  ]
}
```

**Run:**
```bash
pa11y-ci
```

#### axe-core (JavaScript library)
**Best for:** Integration into test suites

**Installation:**
```bash
npm install --save-dev axe-core
```

**Usage with Jest:**
```javascript
import { axe, toHaveNoViolations } from 'jest-axe';
import { render } from '@testing-library/react';
import MyComponent from './MyComponent';

expect.extend(toHaveNoViolations);

test('component should be accessible', async () => {
  const { container } = render(<MyComponent />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

**Usage with Playwright:**
```javascript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('page should be accessible', async ({ page }) => {
  await page.goto('https://example.com');
  
  const accessibilityScanResults = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa'])
    .analyze();
  
  expect(accessibilityScanResults.violations).toEqual([]);
});
```

**Usage with Cypress:**
```javascript
import 'cypress-axe';

describe('Accessibility tests', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.injectAxe();
  });

  it('Has no detectable accessibility violations', () => {
    cy.checkA11y();
  });

  it('Checks specific element', () => {
    cy.checkA11y('.main-content');
  });

  it('Excludes specific elements', () => {
    cy.checkA11y({ exclude: ['.third-party-widget'] });
  });
});
```

### Online Tools

#### WAVE API
**Best for:** Batch testing multiple pages

**Usage:**
```bash
curl "https://wave.webaim.org/api/request?key=YOUR_API_KEY&url=https://example.com"
```

**Response includes:**
- Error count and details
- Alert count and details
- Feature count
- Structural elements
- ARIA usage

#### Google Lighthouse CI
**Best for:** Continuous integration

**Installation:**
```bash
npm install -g @lhci/cli
```

**Configuration (`lighthouserc.json`):**
```json
{
  "ci": {
    "collect": {
      "url": ["http://localhost:3000"],
      "numberOfRuns": 3
    },
    "assert": {
      "assertions": {
        "categories:accessibility": ["error", {"minScore": 0.9}]
      }
    },
    "upload": {
      "target": "temporary-public-storage"
    }
  }
}
```

**Run:**
```bash
lhci autorun
```

## Manual Testing Tools

### Screen Readers

#### NVDA (NonVisual Desktop Access)
**Platform:** Windows (Free)

**Installation:**
- Download from [nvaccess.org](https://www.nvaccess.org)
- Install and restart computer

**Basic Commands:**
- **Start/Stop:** Ctrl + Alt + N
- **Read next line:** Down Arrow
- **Read previous line:** Up Arrow
- **Read next word:** Ctrl + Right Arrow
- **Read next character:** Right Arrow
- **Stop reading:** Ctrl
- **List headings:** Insert + F7
- **List links:** Insert + F7, then Tab
- **Next heading:** H
- **Next link:** K
- **Next form field:** F
- **Next button:** B

**Testing Workflow:**
1. Start NVDA (Ctrl + Alt + N)
2. Navigate to page
3. Use Tab to move through interactive elements
4. Use H to jump between headings
5. Use arrow keys to read content
6. Verify all content is announced correctly
7. Test forms, buttons, and interactive components

#### JAWS (Job Access With Speech)
**Platform:** Windows (Commercial)

**Installation:**
- Purchase from [freedomscientific.com](https://www.freedomscientific.com)
- 40-minute demo mode available

**Basic Commands:**
- **Start/Stop:** Ctrl + Alt + J
- **Read next line:** Down Arrow
- **Read previous line:** Up Arrow
- **List headings:** Insert + F6
- **List links:** Insert + F7
- **Next heading:** H
- **Next link:** Tab
- **Forms mode:** Enter (on form field)
- **Exit forms mode:** Numpad Plus

#### VoiceOver
**Platform:** macOS, iOS (Built-in, Free)

**macOS Activation:**
- **Enable:** Cmd + F5 (or System Preferences > Accessibility > VoiceOver)
- **Quick start:** Cmd + F5

**macOS Basic Commands:**
- **VoiceOver key:** Ctrl + Option (VO)
- **Start reading:** VO + A
- **Stop reading:** Ctrl
- **Next item:** VO + Right Arrow
- **Previous item:** VO + Left Arrow
- **Interact with element:** VO + Shift + Down Arrow
- **Stop interacting:** VO + Shift + Up Arrow
- **Rotor (navigation menu):** VO + U
- **Next heading:** VO + Cmd + H
- **Next link:** VO + Cmd + L

**iOS Activation:**
- Settings > Accessibility > VoiceOver > On
- Or triple-click home/side button (if configured)

**iOS Basic Gestures:**
- **Next item:** Swipe right
- **Previous item:** Swipe left
- **Activate:** Double-tap
- **Rotor:** Rotate two fingers
- **Scroll:** Three-finger swipe

#### TalkBack
**Platform:** Android (Built-in, Free)

**Activation:**
- Settings > Accessibility > TalkBack > On
- Or volume keys shortcut (if configured)

**Basic Gestures:**
- **Next item:** Swipe right
- **Previous item:** Swipe left
- **Activate:** Double-tap
- **Scroll:** Two-finger swipe
- **Reading controls:** Swipe up then right
- **Global context menu:** Swipe down then right
- **Local context menu:** Swipe up then down

### Keyboard Testing

#### Keyboard Navigation Checklist

**Tab Navigation:**
- [ ] All interactive elements reachable via Tab
- [ ] Tab order follows visual layout
- [ ] No keyboard traps (can Tab away from all elements)
- [ ] Skip links work (jump to main content)

**Focus Indicators:**
- [ ] Focus indicator visible on all elements
- [ ] Focus indicator has sufficient contrast (3:1)
- [ ] Focus indicator not obscured by other content

**Keyboard Shortcuts:**
- [ ] Enter activates buttons and links
- [ ] Space activates buttons and toggles checkboxes
- [ ] Arrow keys navigate within components (tabs, menus, sliders)
- [ ] Escape closes dialogs and cancels operations
- [ ] Home/End jump to first/last items

**Custom Components:**
- [ ] Dropdowns: Arrow keys navigate, Enter selects, Escape closes
- [ ] Modals: Focus trapped, Escape closes, focus returns on close
- [ ] Tabs: Arrow keys navigate tabs, Tab moves to panel
- [ ] Sliders: Arrow keys adjust value, Home/End jump to min/max
- [ ] Menus: Arrow keys navigate, Enter activates, Escape closes

#### Browser Developer Tools for Keyboard Testing

**Chrome DevTools:**
1. Open DevTools (F12)
2. Elements tab > Accessibility pane
3. View computed accessibility properties
4. Inspect ARIA attributes
5. View accessibility tree

**Firefox Accessibility Inspector:**
1. Open DevTools (F12)
2. Accessibility tab
3. Enable accessibility features
4. Inspect accessibility tree
5. Check for issues

### Color Contrast Tools

#### WebAIM Contrast Checker
**URL:** https://webaim.org/resources/contrastchecker/

**Features:**
- Enter foreground and background colors
- Shows contrast ratio
- Indicates WCAG AA/AAA pass/fail
- Suggests similar passing colors

#### Colour Contrast Analyser (CCA)
**Platform:** Windows, macOS (Free)

**Download:** [tpgi.com/color-contrast-checker](https://www.tpgi.com/color-contrast-checker/)

**Features:**
- Eyedropper to sample colors from screen
- Real-time contrast ratio calculation
- WCAG 2.0, 2.1, 2.2 compliance indicators
- Color blindness simulator

**Usage:**
1. Open CCA
2. Use eyedropper to select foreground color
3. Use eyedropper to select background color
4. View contrast ratio and pass/fail status

#### Browser Extensions

**WCAG Color Contrast Checker (Chrome)**
- Right-click element > Inspect
- View contrast ratio in DevTools
- Automatic detection of text/background pairs

### Zoom and Reflow Testing

#### Browser Zoom Test

**Procedure:**
1. Set browser zoom to 100%
2. Increase zoom to 200% (Ctrl/Cmd + +)
3. Verify:
   - [ ] No horizontal scrolling
   - [ ] Content reflows properly
   - [ ] All functionality available
   - [ ] Text remains readable
4. Test at 400% for AAA compliance

**Common Issues:**
- Fixed-width containers causing horizontal scroll
- Overlapping content
- Hidden or cut-off text
- Broken layouts

#### Text Spacing Test

**Bookmarklet:**
```javascript
javascript:(function(){var s=document.createElement('style');s.innerHTML='*{line-height:1.5!important;letter-spacing:0.12em!important;word-spacing:0.16em!important;}p{margin-bottom:2em!important;}';document.head.appendChild(s);})();
```

**Procedure:**
1. Create bookmark with above code
2. Navigate to page
3. Click bookmarklet
4. Verify no loss of content or functionality

### Mobile Testing Tools

#### Chrome DevTools Device Emulation

**Usage:**
1. Open DevTools (F12)
2. Click device toolbar icon (Ctrl+Shift+M)
3. Select device or set custom dimensions
4. Test touch targets (minimum 24×24px per WCAG 2.2)
5. Test orientation changes

#### Accessibility Scanner (Android)

**Installation:**
- Download from Google Play Store

**Usage:**
1. Open Accessibility Scanner
2. Grant permissions
3. Navigate to app/page to test
4. Tap floating action button
5. Review suggestions

**Checks:**
- Touch target size
- Clickable items
- Text contrast
- Content labels

## Testing Workflow

### Quick Test (15 minutes)

1. **Automated scan** (5 min)
   - Run axe DevTools or WAVE
   - Note critical and serious issues

2. **Keyboard test** (5 min)
   - Tab through page
   - Verify focus indicators
   - Test interactive components

3. **Screen reader spot check** (5 min)
   - Test main navigation
   - Test one form or interactive component
   - Verify headings and landmarks

### Comprehensive Test (2-4 hours)

1. **Automated testing** (30 min)
   - Run multiple tools (axe, WAVE, Lighthouse)
   - Document all issues
   - Categorize by severity

2. **Keyboard testing** (30 min)
   - Complete keyboard navigation
   - Test all interactive components
   - Verify shortcuts and custom controls

3. **Screen reader testing** (60 min)
   - Test with NVDA or JAWS (Windows)
   - Test with VoiceOver (macOS)
   - Test all major user flows
   - Verify forms, tables, dynamic content

4. **Visual testing** (30 min)
   - Color contrast verification
   - Zoom to 200% and 400%
   - Text spacing test
   - Color blindness simulation

5. **Mobile testing** (30 min)
   - Test on iOS with VoiceOver
   - Test on Android with TalkBack
   - Verify touch target sizes
   - Test orientation changes

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Accessibility Tests

on: [push, pull_request]

jobs:
  a11y:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node
        uses: actions/setup-node@v3
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
        run: |
          npm install -g pa11y-ci
          pa11y-ci
      
      - name: Run Lighthouse
        run: |
          npm install -g @lhci/cli
          lhci autorun
```

### Pre-commit Hook

```bash
#!/bin/sh
# .git/hooks/pre-commit

npm run test:a11y

if [ $? -ne 0 ]; then
  echo "Accessibility tests failed. Commit aborted."
  exit 1
fi
```

## Resources

- **axe DevTools**: https://www.deque.com/axe/devtools/
- **WAVE**: https://wave.webaim.org/
- **Pa11y**: https://pa11y.org/
- **Lighthouse**: https://developers.google.com/web/tools/lighthouse
- **NVDA**: https://www.nvaccess.org/
- **WebAIM**: https://webaim.org/
