# Playwright Implementation Guide

Comprehensive guide to implementing Playwright for modern web application testing.

---

## Why Playwright in 2026

Playwright has emerged as the fastest-growing automation framework with:
- **45.1% adoption rate** among QA professionals
- **94% user retention rate** (highest in industry)
- **Direct DevTools Protocol** connection (no WebDriver overhead)
- **True cross-browser support** (Chromium, Firefox, WebKit)
- **Built-in auto-waiting** mechanisms
- **Native parallel execution**
- **Microsoft backing** ensuring long-term viability

---

## Installation and Setup

### Node.js/TypeScript Setup

```bash
# Initialize new project
npm init playwright@latest

# Install Playwright with browsers
npm install -D @playwright/test
npx playwright install

# Install specific browsers only
npx playwright install chromium firefox webkit
```

### Python Setup

```bash
# Install Playwright
pip install playwright pytest-playwright

# Install browsers
playwright install
```

### Configuration (playwright.config.ts)

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
  ],
});
```

---

## Core Concepts

### Auto-Waiting

Playwright automatically waits for elements to be actionable:

```typescript
// No explicit waits needed - Playwright handles it
await page.click('button#submit'); // Waits for button to be visible, enabled, stable
await page.fill('input#email', 'test@example.com'); // Waits for input to be editable
```

### Locator Strategies

```typescript
// Recommended: Use data-testid attributes
await page.locator('[data-testid="login-button"]').click();

// Text-based (resilient to styling changes)
await page.getByRole('button', { name: 'Login' }).click();
await page.getByText('Welcome back').isVisible();

// CSS selectors (use sparingly)
await page.locator('button.primary').click();

// XPath (last resort)
await page.locator('//button[@id="submit"]').click();
```

### Page Object Model

```typescript
// pages/LoginPage.ts
import { Page, Locator } from '@playwright/test';

export class LoginPage {
  readonly page: Page;
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly errorMessage: Locator;

  constructor(page: Page) {
    this.page = page;
    this.emailInput = page.locator('[data-testid="email"]');
    this.passwordInput = page.locator('[data-testid="password"]');
    this.loginButton = page.getByRole('button', { name: 'Login' });
    this.errorMessage = page.locator('.error-message');
  }

  async goto() {
    await this.page.goto('/login');
  }

  async login(email: string, password: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }

  async getErrorMessage() {
    return await this.errorMessage.textContent();
  }
}

// tests/login.spec.ts
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

test('successful login', async ({ page }) => {
  const loginPage = new LoginPage(page);
  await loginPage.goto();
  await loginPage.login('user@example.com', 'password123');
  await expect(page).toHaveURL('/dashboard');
});
```

---

## Advanced Features

### API Testing

```typescript
import { test, expect } from '@playwright/test';

test('API: Create user', async ({ request }) => {
  const response = await request.post('/api/users', {
    data: {
      name: 'John Doe',
      email: 'john@example.com'
    }
  });
  
  expect(response.ok()).toBeTruthy();
  const user = await response.json();
  expect(user.id).toBeDefined();
  expect(user.name).toBe('John Doe');
});

// Combine API and UI testing
test('Create user via API, verify in UI', async ({ request, page }) => {
  // Setup via API (faster)
  const response = await request.post('/api/users', {
    data: { name: 'Jane Doe', email: 'jane@example.com' }
  });
  const user = await response.json();
  
  // Verify in UI
  await page.goto(`/users/${user.id}`);
  await expect(page.locator('h1')).toHaveText('Jane Doe');
});
```

### Network Interception

```typescript
// Mock API responses
test('Mock API response', async ({ page }) => {
  await page.route('**/api/users', route => {
    route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify([{ id: 1, name: 'Mocked User' }])
    });
  });
  
  await page.goto('/users');
  await expect(page.locator('.user-name')).toHaveText('Mocked User');
});

// Abort requests (speed up tests)
test('Block unnecessary resources', async ({ page }) => {
  await page.route('**/*.{png,jpg,jpeg,gif,svg,css}', route => route.abort());
  await page.goto('/dashboard');
});
```

### Parallel Execution

```typescript
// playwright.config.ts
export default defineConfig({
  workers: 4, // Run 4 tests in parallel
  fullyParallel: true,
});

// Run tests in parallel within a file
test.describe.configure({ mode: 'parallel' });

test.describe('Parallel tests', () => {
  test('test 1', async ({ page }) => { /* ... */ });
  test('test 2', async ({ page }) => { /* ... */ });
  test('test 3', async ({ page }) => { /* ... */ });
});
```

### Trace Viewer

```typescript
// Enable tracing
test('with tracing', async ({ page }) => {
  await page.context().tracing.start({ screenshots: true, snapshots: true });
  
  await page.goto('/dashboard');
  await page.click('button#action');
  
  await page.context().tracing.stop({ path: 'trace.zip' });
});

// View trace
// npx playwright show-trace trace.zip
```

### Visual Regression Testing

```typescript
import { test, expect } from '@playwright/test';

test('visual regression', async ({ page }) => {
  await page.goto('/dashboard');
  
  // Full page screenshot comparison
  await expect(page).toHaveScreenshot('dashboard.png');
  
  // Element screenshot comparison
  const header = page.locator('header');
  await expect(header).toHaveScreenshot('header.png');
  
  // With threshold for minor differences
  await expect(page).toHaveScreenshot('dashboard.png', {
    maxDiffPixels: 100
  });
});
```

---

## CI/CD Integration

### GitHub Actions

```yaml
name: Playwright Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    timeout-minutes: 60
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-node@v3
      with:
        node-version: 18
    - name: Install dependencies
      run: npm ci
    - name: Install Playwright Browsers
      run: npx playwright install --with-deps
    - name: Run Playwright tests
      run: npx playwright test
    - uses: actions/upload-artifact@v3
      if: always()
      with:
        name: playwright-report
        path: playwright-report/
        retention-days: 30
```

### Docker

```dockerfile
FROM mcr.microsoft.com/playwright:v1.40.0-focal

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

CMD ["npx", "playwright", "test"]
```

---

## Best Practices

### 1. Use Data-TestId Attributes

```html
<!-- HTML -->
<button data-testid="submit-button" class="btn btn-primary">Submit</button>

<!-- Test -->
await page.locator('[data-testid="submit-button"]').click();
```

### 2. Leverage Auto-Waiting

```typescript
// ❌ Bad: Unnecessary explicit waits
await page.waitForTimeout(3000);
await page.click('button');

// ✅ Good: Let Playwright handle waiting
await page.click('button'); // Automatically waits for button to be actionable
```

### 3. Use Fixtures for Setup

```typescript
import { test as base } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

type MyFixtures = {
  authenticatedPage: Page;
};

const test = base.extend<MyFixtures>({
  authenticatedPage: async ({ page }, use) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login('user@example.com', 'password');
    await use(page);
  },
});

test('access protected page', async ({ authenticatedPage }) => {
  await authenticatedPage.goto('/protected');
  // Already logged in
});
```

### 4. Implement Retry Logic

```typescript
// playwright.config.ts
export default defineConfig({
  retries: process.env.CI ? 2 : 0, // Retry failed tests in CI
});

// Per-test retry
test('flaky test', async ({ page }) => {
  test.info().annotations.push({ type: 'issue', description: 'Known flaky test' });
  // Test code
});
```

### 5. Organize Tests Logically

```
tests/
├── auth/
│   ├── login.spec.ts
│   ├── logout.spec.ts
│   └── registration.spec.ts
├── dashboard/
│   ├── overview.spec.ts
│   └── widgets.spec.ts
├── api/
│   ├── users.spec.ts
│   └── products.spec.ts
└── fixtures/
    └── authenticated.ts
```

---

## Performance Optimization

### 1. Parallel Execution

```bash
# Run tests in parallel across 4 workers
npx playwright test --workers=4

# Run specific project
npx playwright test --project=chromium
```

### 2. Sharding for CI

```bash
# Split tests across multiple machines
npx playwright test --shard=1/3  # Machine 1
npx playwright test --shard=2/3  # Machine 2
npx playwright test --shard=3/3  # Machine 3
```

### 3. Reuse Authentication State

```typescript
// global-setup.ts
import { chromium, FullConfig } from '@playwright/test';

async function globalSetup(config: FullConfig) {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('http://localhost:3000/login');
  await page.fill('[data-testid="email"]', 'user@example.com');
  await page.fill('[data-testid="password"]', 'password');
  await page.click('[data-testid="login-button"]');
  await page.context().storageState({ path: 'auth.json' });
  await browser.close();
}

export default globalSetup;

// playwright.config.ts
export default defineConfig({
  globalSetup: require.resolve('./global-setup'),
  use: {
    storageState: 'auth.json',
  },
});
```

---

## Debugging

### 1. Headed Mode

```bash
npx playwright test --headed
```

### 2. Debug Mode

```bash
npx playwright test --debug
```

### 3. Playwright Inspector

```typescript
await page.pause(); // Opens Playwright Inspector
```

### 4. Console Logs

```typescript
page.on('console', msg => console.log('PAGE LOG:', msg.text()));
```

---

## Migration from Selenium

### Key Differences

| Feature | Selenium | Playwright |
|---------|----------|------------|
| Architecture | WebDriver (client-server) | DevTools Protocol (direct) |
| Auto-waiting | Manual (explicit/implicit waits) | Built-in |
| Browser support | All major browsers | Chromium, Firefox, WebKit |
| Speed | Slower (network overhead) | Faster (direct connection) |
| API testing | External libraries needed | Built-in |
| Parallel execution | Selenium Grid required | Native support |

### Migration Steps

1. **Install Playwright** alongside Selenium
2. **Convert one test file** as proof-of-concept
3. **Update locators** to use Playwright syntax
4. **Remove explicit waits** (leverage auto-waiting)
5. **Migrate gradually** (file by file or feature by feature)
6. **Update CI/CD pipelines** once migration complete

### Example Conversion

```python
# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://example.com')
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
element.click()

# Playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://example.com')
    page.click('#submit')  # Auto-waits for element to be clickable
    browser.close()
```

---

## Common Pitfalls

### 1. Over-reliance on CSS Selectors

```typescript
// ❌ Fragile: Breaks with styling changes
await page.locator('div.container > ul > li:nth-child(2) > a').click();

// ✅ Robust: Uses semantic locators
await page.getByRole('link', { name: 'Dashboard' }).click();
```

### 2. Not Using Page Object Model

```typescript
// ❌ Bad: Duplicated locators across tests
test('test 1', async ({ page }) => {
  await page.locator('[data-testid="email"]').fill('user@example.com');
});

test('test 2', async ({ page }) => {
  await page.locator('[data-testid="email"]').fill('admin@example.com');
});

// ✅ Good: Centralized in Page Object
class LoginPage {
  readonly emailInput = this.page.locator('[data-testid="email"]');
  // ...
}
```

### 3. Ignoring Test Isolation

```typescript
// ❌ Bad: Tests depend on each other
test('create user', async ({ page }) => {
  // Creates user with ID 123
});

test('edit user', async ({ page }) => {
  // Assumes user 123 exists from previous test
});

// ✅ Good: Each test is independent
test('edit user', async ({ page, request }) => {
  // Create user via API first
  const user = await request.post('/api/users', { data: { name: 'Test' } });
  // Now edit the user
});
```