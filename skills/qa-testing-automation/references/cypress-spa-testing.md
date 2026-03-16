# Cypress SPA Testing Guide

Comprehensive guide to testing Single Page Applications with Cypress.

---

## Why Cypress for SPAs

Cypress excels at testing modern JavaScript SPAs due to:
- **Runs in browser event loop** — Direct access to application code
- **Real-time reloading** — See changes instantly
- **Time-travel debugging** — Step through test execution
- **Automatic waiting** — No manual waits needed
- **Network stubbing** — Control API responses
- **Component testing** — Test React/Vue/Angular components in isolation

---

## Installation and Setup

```bash
# Install Cypress
npm install --save-dev cypress

# Open Cypress
npx cypress open

# Run headless
npx cypress run
```

### Configuration (cypress.config.js)

```javascript
const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://localhost:3000',
    viewportWidth: 1280,
    viewportHeight: 720,
    video: false,
    screenshotOnRunFailure: true,
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
  component: {
    devServer: {
      framework: 'react',
      bundler: 'vite',
    },
  },
});
```

---

## E2E Testing Patterns

### Basic Test Structure

```javascript
describe('Login Flow', () => {
  beforeEach(() => {
    cy.visit('/login');
  });

  it('should login successfully with valid credentials', () => {
    cy.get('[data-testid="email"]').type('user@example.com');
    cy.get('[data-testid="password"]').type('password123');
    cy.get('[data-testid="login-button"]').click();
    
    cy.url().should('include', '/dashboard');
    cy.get('[data-testid="user-name"]').should('contain', 'John Doe');
  });

  it('should show error with invalid credentials', () => {
    cy.get('[data-testid="email"]').type('invalid@example.com');
    cy.get('[data-testid="password"]').type('wrongpassword');
    cy.get('[data-testid="login-button"]').click();
    
    cy.get('.error-message').should('be.visible')
      .and('contain', 'Invalid credentials');
  });
});
```

### Custom Commands

```javascript
// cypress/support/commands.js
Cypress.Commands.add('login', (email, password) => {
  cy.session([email, password], () => {
    cy.visit('/login');
    cy.get('[data-testid="email"]').type(email);
    cy.get('[data-testid="password"]').type(password);
    cy.get('[data-testid="login-button"]').click();
    cy.url().should('include', '/dashboard');
  });
});

Cypress.Commands.add('createUser', (userData) => {
  return cy.request('POST', '/api/users', userData);
});

// Usage in tests
cy.login('user@example.com', 'password123');
cy.visit('/dashboard');
```

---

## Network Interception

### Stubbing API Responses

```javascript
it('should display mocked user data', () => {
  cy.intercept('GET', '/api/user', {
    statusCode: 200,
    body: {
      id: 1,
      name: 'Mocked User',
      email: 'mocked@example.com'
    }
  }).as('getUser');

  cy.visit('/profile');
  cy.wait('@getUser');
  
  cy.get('[data-testid="user-name"]').should('contain', 'Mocked User');
});
```

### Waiting for API Calls

```javascript
it('should wait for API response', () => {
  cy.intercept('POST', '/api/users').as('createUser');
  
  cy.get('[data-testid="create-user-button"]').click();
  cy.wait('@createUser').its('response.statusCode').should('eq', 201);
  
  cy.get('.success-message').should('be.visible');
});
```

### Modifying Requests

```javascript
cy.intercept('POST', '/api/users', (req) => {
  req.body.createdBy = 'test-automation';
  req.continue();
});
```

---

## Component Testing

### React Component Test

```javascript
// Button.cy.jsx
import Button from './Button';

describe('Button Component', () => {
  it('should render with text', () => {
    cy.mount(<Button>Click Me</Button>);
    cy.get('button').should('contain', 'Click Me');
  });

  it('should call onClick handler', () => {
    const onClickSpy = cy.spy().as('onClickSpy');
    cy.mount(<Button onClick={onClickSpy}>Click Me</Button>);
    
    cy.get('button').click();
    cy.get('@onClickSpy').should('have.been.calledOnce');
  });

  it('should be disabled when prop is set', () => {
    cy.mount(<Button disabled>Click Me</Button>);
    cy.get('button').should('be.disabled');
  });
});
```

### Vue Component Test

```javascript
// UserCard.cy.js
import UserCard from './UserCard.vue';

describe('UserCard Component', () => {
  it('should display user information', () => {
    const user = {
      name: 'John Doe',
      email: 'john@example.com',
      role: 'Admin'
    };
    
    cy.mount(UserCard, {
      props: { user }
    });
    
    cy.get('[data-testid="user-name"]').should('contain', 'John Doe');
    cy.get('[data-testid="user-email"]').should('contain', 'john@example.com');
    cy.get('[data-testid="user-role"]').should('contain', 'Admin');
  });
});
```

---

## Advanced Patterns

### Page Object Pattern

```javascript
// cypress/support/pages/LoginPage.js
export class LoginPage {
  visit() {
    cy.visit('/login');
  }

  fillEmail(email) {
    cy.get('[data-testid="email"]').type(email);
    return this;
  }

  fillPassword(password) {
    cy.get('[data-testid="password"]').type(password);
    return this;
  }

  submit() {
    cy.get('[data-testid="login-button"]').click();
  }

  getErrorMessage() {
    return cy.get('.error-message');
  }
}

// Usage
import { LoginPage } from '../support/pages/LoginPage';

it('should login', () => {
  const loginPage = new LoginPage();
  loginPage.visit();
  loginPage
    .fillEmail('user@example.com')
    .fillPassword('password123')
    .submit();
  
  cy.url().should('include', '/dashboard');
});
```

### Fixtures for Test Data

```javascript
// cypress/fixtures/users.json
{
  "validUser": {
    "email": "user@example.com",
    "password": "password123"
  },
  "adminUser": {
    "email": "admin@example.com",
    "password": "admin123"
  }
}

// Test
it('should login with fixture data', () => {
  cy.fixture('users').then((users) => {
    cy.login(users.validUser.email, users.validUser.password);
  });
});
```

---

## Best Practices

### 1. Use data-testid Attributes

```html
<!-- Good -->
<button data-testid="submit-button">Submit</button>

<!-- Avoid -->
<button class="btn btn-primary">Submit</button>
```

### 2. Avoid Hard-Coded Waits

```javascript
// ❌ Bad
cy.wait(3000);
cy.get('.element').click();

// ✅ Good
cy.get('.element').should('be.visible').click();
```

### 3. Use Aliases for Clarity

```javascript
cy.get('[data-testid="user-list"]').as('userList');
cy.get('@userList').should('have.length', 5);
```

### 4. Keep Tests Independent

```javascript
// ❌ Bad: Tests depend on each other
it('creates user', () => { /* ... */ });
it('edits user', () => { /* assumes user exists */ });

// ✅ Good: Each test is independent
it('edits user', () => {
  cy.createUser({ name: 'Test User' }); // Setup
  // Test editing
});
```

---

## CI/CD Integration

### GitHub Actions

```yaml
name: Cypress Tests

on: [push, pull_request]

jobs:
  cypress-run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: cypress-io/github-action@v5
        with:
          build: npm run build
          start: npm start
          wait-on: 'http://localhost:3000'
          browser: chrome
      - uses: actions/upload-artifact@v3
        if: failure()
        with:
          name: cypress-screenshots
          path: cypress/screenshots
```

### Docker

```dockerfile
FROM cypress/included:12.0.0

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

CMD ["npx", "cypress", "run"]
```