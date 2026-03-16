# Test Architecture Patterns

Design patterns and architectural approaches for scalable, maintainable test automation frameworks.

---

## Page Object Model (POM)

### Classic POM

**Concept:** Encapsulate page elements and actions in dedicated classes.

**Benefits:**
- Centralized element locators
- Reusable page actions
- Easy maintenance
- Clear separation of concerns

**Implementation:**

```typescript
// pages/BasePage.ts
export class BasePage {
  constructor(protected page: Page) {}
  
  async navigate(path: string) {
    await this.page.goto(path);
  }
  
  async waitForElement(locator: string) {
    await this.page.waitForSelector(locator);
  }
}

// pages/LoginPage.ts
import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';

export class LoginPage extends BasePage {
  private readonly emailInput: Locator;
  private readonly passwordInput: Locator;
  private readonly loginButton: Locator;
  private readonly errorMessage: Locator;
  
  constructor(page: Page) {
    super(page);
    this.emailInput = page.locator('[data-testid="email"]');
    this.passwordInput = page.locator('[data-testid="password"]');
    this.loginButton = page.locator('[data-testid="login-button"]');
    this.errorMessage = page.locator('.error-message');
  }
  
  async goto() {
    await this.navigate('/login');
  }
  
  async login(email: string, password: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }
  
  async getErrorText(): Promise<string> {
    return await this.errorMessage.textContent() || '';
  }
  
  async isErrorVisible(): Promise<boolean> {
    return await this.errorMessage.isVisible();
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

## Component Object Model

**Concept:** Break pages into reusable components.

```typescript
// components/Header.ts
export class Header {
  private readonly userMenu: Locator;
  private readonly logoutButton: Locator;
  
  constructor(private page: Page) {
    this.userMenu = page.locator('[data-testid="user-menu"]');
    this.logoutButton = page.locator('[data-testid="logout"]');
  }
  
  async logout() {
    await this.userMenu.click();
    await this.logoutButton.click();
  }
}

// pages/DashboardPage.ts
import { Header } from '../components/Header';

export class DashboardPage {
  readonly header: Header;
  
  constructor(private page: Page) {
    this.header = new Header(page);
  }
  
  async goto() {
    await this.page.goto('/dashboard');
  }
}

// Usage
const dashboard = new DashboardPage(page);
await dashboard.goto();
await dashboard.header.logout();
```

---

## Screenplay Pattern

**Concept:** Focus on user interactions and tasks rather than page structure.

```typescript
// actors/User.ts
export class User {
  constructor(private page: Page) {}
  
  async attemptsTo(...tasks: Task[]) {
    for (const task of tasks) {
      await task.performAs(this);
    }
  }
  
  getPage(): Page {
    return this.page;
  }
}

// tasks/Login.ts
export class Login implements Task {
  constructor(
    private email: string,
    private password: string
  ) {}
  
  async performAs(actor: User) {
    const page = actor.getPage();
    await page.goto('/login');
    await page.fill('[data-testid="email"]', this.email);
    await page.fill('[data-testid="password"]', this.password);
    await page.click('[data-testid="login-button"]');
  }
}

// tasks/CreatePost.ts
export class CreatePost implements Task {
  constructor(private title: string, private content: string) {}
  
  async performAs(actor: User) {
    const page = actor.getPage();
    await page.click('[data-testid="new-post"]');
    await page.fill('[data-testid="title"]', this.title);
    await page.fill('[data-testid="content"]', this.content);
    await page.click('[data-testid="publish"]');
  }
}

// Usage
const user = new User(page);
await user.attemptsTo(
  new Login('user@example.com', 'password'),
  new CreatePost('My Title', 'My Content')
);
```

---

## Builder Pattern for Test Data

```typescript
// builders/UserBuilder.ts
export class UserBuilder {
  private user: Partial<User> = {};
  
  withEmail(email: string): this {
    this.user.email = email;
    return this;
  }
  
  withPassword(password: string): this {
    this.user.password = password;
    return this;
  }
  
  withRole(role: string): this {
    this.user.role = role;
    return this;
  }
  
  build(): User {
    return {
      email: this.user.email || 'default@example.com',
      password: this.user.password || 'password123',
      role: this.user.role || 'user',
      ...this.user
    } as User;
  }
}

// Usage
const adminUser = new UserBuilder()
  .withEmail('admin@example.com')
  .withRole('admin')
  .build();

const testUser = new UserBuilder()
  .withEmail('test@example.com')
  .build();
```

---

## Factory Pattern

```typescript
// factories/PageFactory.ts
export class PageFactory {
  static createPage(pageName: string, page: Page): any {
    switch (pageName) {
      case 'login':
        return new LoginPage(page);
      case 'dashboard':
        return new DashboardPage(page);
      case 'profile':
        return new ProfilePage(page);
      default:
        throw new Error(`Unknown page: ${pageName}`);
    }
  }
}

// Usage
const loginPage = PageFactory.createPage('login', page);
```

---

## Fixture Pattern

```typescript
// fixtures/authenticatedUser.ts
import { test as base } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

type AuthenticatedFixture = {
  authenticatedPage: Page;
};

export const test = base.extend<AuthenticatedFixture>({
  authenticatedPage: async ({ page }, use) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login('user@example.com', 'password');
    await use(page);
  },
});

// Usage
import { test } from '../fixtures/authenticatedUser';

test('access protected resource', async ({ authenticatedPage }) => {
  await authenticatedPage.goto('/protected');
  // Already authenticated
});
```

---

## Data-Driven Testing

### CSV-Based

```typescript
import { parse } from 'csv-parse/sync';
import fs from 'fs';

const testData = parse(fs.readFileSync('testdata.csv'), {
  columns: true,
  skip_empty_lines: true
});

for (const data of testData) {
  test(`login with ${data.email}`, async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login(data.email, data.password);
    
    if (data.shouldSucceed === 'true') {
      await expect(page).toHaveURL('/dashboard');
    } else {
      await expect(loginPage.isErrorVisible()).resolves.toBe(true);
    }
  });
}
```

### JSON-Based

```typescript
import testData from './testdata.json';

for (const scenario of testData.loginScenarios) {
  test(scenario.description, async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login(scenario.email, scenario.password);
    
    await expect(page).toHaveURL(scenario.expectedUrl);
  });
}
```

---

## Layered Architecture

```
test-automation/
├── tests/                  # Test specifications
│   ├── e2e/
│   ├── integration/
│   └── unit/
├── pages/                  # Page Objects
│   ├── BasePage.ts
│   ├── LoginPage.ts
│   └── DashboardPage.ts
├── components/             # Reusable components
│   ├── Header.ts
│   └── Footer.ts
├── fixtures/               # Test fixtures
│   └── authenticatedUser.ts
├── utils/                  # Utility functions
│   ├── dateHelpers.ts
│   └── stringHelpers.ts
├── data/                   # Test data
│   ├── users.json
│   └── products.csv
├── config/                 # Configuration
│   ├── environments.ts
│   └── testConfig.ts
└── playwright.config.ts
```

---

## Best Practices

### 1. Single Responsibility
Each page object should represent one page or component.

### 2. DRY (Don't Repeat Yourself)
Extract common functionality into base classes or utilities.

### 3. Encapsulation
Hide implementation details; expose only necessary methods.

### 4. Naming Conventions
- Page Objects: `LoginPage`, `DashboardPage`
- Methods: `login()`, `clickSubmit()`, `getErrorMessage()`
- Locators: `emailInput`, `submitButton`

### 5. Return Types
- Navigation methods return new page objects
- Action methods return void or the same page object (fluent)
- Query methods return data (string, boolean, etc.)

### 6. Avoid Test Logic in Page Objects
Page objects should contain actions and queries, not assertions.