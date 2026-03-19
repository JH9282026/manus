# React Testing Guide

Comprehensive testing strategies for React applications using modern tools and best practices.

---

## Testing Philosophy

### Testing Trophy

```
       /\
      /  \     E2E Tests (few)
     /    \
    /------\   Integration Tests (more)
   /        \
  /----------\  Unit Tests (many)
 /____________\ Static Analysis (most)
```

**Priorities**:
1. Static Analysis (TypeScript, ESLint)
2. Unit Tests (utilities, hooks)
3. Integration Tests (components, user flows)
4. E2E Tests (critical paths)

## Testing Stack

### Recommended Tools (2026)

- **Test Runner**: Vitest (fast, Vite-compatible)
- **Component Testing**: React Testing Library
- **E2E Testing**: Playwright
- **Mocking**: MSW (Mock Service Worker)
- **Coverage**: Vitest coverage
- **Visual Testing**: Storybook + Chromatic

## Unit Testing

### Testing Utilities

```typescript
// utils/formatCurrency.ts
export function formatCurrency(amount: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
  }).format(amount);
}

// utils/formatCurrency.test.ts
import { describe, it, expect } from 'vitest';
import { formatCurrency } from './formatCurrency';

describe('formatCurrency', () => {
  it('formats positive numbers', () => {
    expect(formatCurrency(1234.56)).toBe('$1,234.56');
  });
  
  it('formats negative numbers', () => {
    expect(formatCurrency(-1234.56)).toBe('-$1,234.56');
  });
  
  it('formats zero', () => {
    expect(formatCurrency(0)).toBe('$0.00');
  });
});
```

### Testing Custom Hooks

```typescript
// hooks/useCounter.ts
import { useState, useCallback } from 'react';

export function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);
  
  const increment = useCallback(() => setCount(c => c + 1), []);
  const decrement = useCallback(() => setCount(c => c - 1), []);
  const reset = useCallback(() => setCount(initialValue), [initialValue]);
  
  return { count, increment, decrement, reset };
}

// hooks/useCounter.test.ts
import { renderHook, act } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { useCounter } from './useCounter';

describe('useCounter', () => {
  it('initializes with default value', () => {
    const { result } = renderHook(() => useCounter());
    expect(result.current.count).toBe(0);
  });
  
  it('initializes with custom value', () => {
    const { result } = renderHook(() => useCounter(10));
    expect(result.current.count).toBe(10);
  });
  
  it('increments count', () => {
    const { result } = renderHook(() => useCounter());
    
    act(() => {
      result.current.increment();
    });
    
    expect(result.current.count).toBe(1);
  });
  
  it('decrements count', () => {
    const { result } = renderHook(() => useCounter(5));
    
    act(() => {
      result.current.decrement();
    });
    
    expect(result.current.count).toBe(4);
  });
  
  it('resets to initial value', () => {
    const { result } = renderHook(() => useCounter(10));
    
    act(() => {
      result.current.increment();
      result.current.increment();
      result.current.reset();
    });
    
    expect(result.current.count).toBe(10);
  });
});
```

## Component Testing

### Basic Component Test

```typescript
// components/Button.tsx
interface ButtonProps {
  onClick: () => void;
  children: React.ReactNode;
  variant?: 'primary' | 'secondary';
}

export function Button({ onClick, children, variant = 'primary' }: ButtonProps) {
  return (
    <button
      className={`btn btn-${variant}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
}

// components/Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { Button } from './Button';

describe('Button', () => {
  it('renders children', () => {
    render(<Button onClick={() => {}}>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });
  
  it('calls onClick when clicked', () => {
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    
    fireEvent.click(screen.getByText('Click me'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
  
  it('applies variant class', () => {
    render(<Button onClick={() => {}} variant="secondary">Click me</Button>);
    expect(screen.getByText('Click me')).toHaveClass('btn-secondary');
  });
});
```

### Testing User Interactions

```typescript
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('form submission', async () => {
  const user = userEvent.setup();
  const handleSubmit = vi.fn();
  
  render(<LoginForm onSubmit={handleSubmit} />);
  
  await user.type(screen.getByLabelText('Email'), 'user@example.com');
  await user.type(screen.getByLabelText('Password'), 'password123');
  await user.click(screen.getByRole('button', { name: 'Login' }));
  
  await waitFor(() => {
    expect(handleSubmit).toHaveBeenCalledWith({
      email: 'user@example.com',
      password: 'password123',
    });
  });
});
```

### Testing Async Components

```typescript
test('loads and displays user data', async () => {
  render(<UserProfile userId="123" />);
  
  // Initially shows loading
  expect(screen.getByText('Loading...')).toBeInTheDocument();
  
  // Wait for data to load
  const userName = await screen.findByText('John Doe');
  expect(userName).toBeInTheDocument();
  
  // Loading indicator should be gone
  expect(screen.queryByText('Loading...')).not.toBeInTheDocument();
});
```

### Testing with Context

```typescript
import { render, screen } from '@testing-library/react';
import { ThemeProvider } from '@/contexts/ThemeContext';

function renderWithTheme(ui: React.ReactElement, theme = 'light') {
  return render(
    <ThemeProvider initialTheme={theme}>
      {ui}
    </ThemeProvider>
  );
}

test('renders with dark theme', () => {
  renderWithTheme(<ThemedButton />, 'dark');
  expect(screen.getByRole('button')).toHaveClass('dark-theme');
});
```

## Mocking

### Mocking API Calls with MSW

```typescript
// mocks/handlers.ts
import { http, HttpResponse } from 'msw';

export const handlers = [
  http.get('/api/users', () => {
    return HttpResponse.json([
      { id: 1, name: 'John Doe' },
      { id: 2, name: 'Jane Smith' },
    ]);
  }),
  
  http.post('/api/users', async ({ request }) => {
    const newUser = await request.json();
    return HttpResponse.json(
      { id: 3, ...newUser },
      { status: 201 }
    );
  }),
];

// mocks/server.ts
import { setupServer } from 'msw/node';
import { handlers } from './handlers';

export const server = setupServer(...handlers);

// vitest.setup.ts
import { beforeAll, afterEach, afterAll } from 'vitest';
import { server } from './mocks/server';

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

### Using MSW in Tests

```typescript
import { server } from '@/mocks/server';
import { http, HttpResponse } from 'msw';

test('handles server error', async () => {
  server.use(
    http.get('/api/users', () => {
      return HttpResponse.json(
        { message: 'Server error' },
        { status: 500 }
      );
    })
  );
  
  render(<UserList />);
  
  expect(await screen.findByText('Error loading users')).toBeInTheDocument();
});
```

### Mocking Modules

```typescript
import { vi } from 'vitest';

// Mock entire module
vi.mock('@/lib/analytics', () => ({
  trackEvent: vi.fn(),
  trackPageView: vi.fn(),
}));

// Mock specific function
vi.mock('@/lib/api', async () => {
  const actual = await vi.importActual('@/lib/api');
  return {
    ...actual,
    fetchUser: vi.fn(() => Promise.resolve({ id: 1, name: 'Test User' })),
  };
});
```

## Integration Testing

### Testing User Flows

```typescript
test('complete checkout flow', async () => {
  const user = userEvent.setup();
  
  render(<App />);
  
  // Add item to cart
  await user.click(screen.getByText('Add to Cart'));
  expect(screen.getByText('1 item in cart')).toBeInTheDocument();
  
  // Go to checkout
  await user.click(screen.getByText('Checkout'));
  expect(screen.getByText('Checkout')).toBeInTheDocument();
  
  // Fill shipping info
  await user.type(screen.getByLabelText('Name'), 'John Doe');
  await user.type(screen.getByLabelText('Address'), '123 Main St');
  
  // Submit order
  await user.click(screen.getByText('Place Order'));
  
  // Verify success
  expect(await screen.findByText('Order confirmed')).toBeInTheDocument();
});
```

### Testing Routing

```typescript
import { MemoryRouter } from 'react-router-dom';

function renderWithRouter(ui: React.ReactElement, { route = '/' } = {}) {
  return render(
    <MemoryRouter initialEntries={[route]}>
      {ui}
    </MemoryRouter>
  );
}

test('navigates to user profile', async () => {
  const user = userEvent.setup();
  
  renderWithRouter(<App />, { route: '/users' });
  
  await user.click(screen.getByText('John Doe'));
  
  expect(screen.getByText('User Profile')).toBeInTheDocument();
  expect(window.location.pathname).toBe('/users/1');
});
```

## E2E Testing with Playwright

### Basic E2E Test

```typescript
import { test, expect } from '@playwright/test';

test('user can login', async ({ page }) => {
  await page.goto('http://localhost:3000');
  
  await page.fill('input[name="email"]', 'user@example.com');
  await page.fill('input[name="password"]', 'password123');
  await page.click('button[type="submit"]');
  
  await expect(page.locator('text=Welcome back')).toBeVisible();
});
```

### Testing with Authentication

```typescript
import { test as base } from '@playwright/test';

const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    await page.goto('http://localhost:3000/login');
    await page.fill('input[name="email"]', 'user@example.com');
    await page.fill('input[name="password"]', 'password123');
    await page.click('button[type="submit"]');
    await page.waitForURL('**/dashboard');
    await use(page);
  },
});

test('authenticated user can access dashboard', async ({ authenticatedPage }) => {
  await expect(authenticatedPage.locator('h1')).toHaveText('Dashboard');
});
```

## Snapshot Testing

```typescript
import { render } from '@testing-library/react';

test('Button matches snapshot', () => {
  const { container } = render(
    <Button variant="primary">Click me</Button>
  );
  expect(container.firstChild).toMatchSnapshot();
});
```

**Note**: Use snapshots sparingly. Prefer explicit assertions.

## Testing Best Practices

### Query Priority

1. **getByRole**: Most accessible
2. **getByLabelText**: For form fields
3. **getByPlaceholderText**: If no label
4. **getByText**: For non-interactive elements
5. **getByTestId**: Last resort

```typescript
// ✅ Good
screen.getByRole('button', { name: 'Submit' });
screen.getByLabelText('Email');

// ❌ Avoid
screen.getByTestId('submit-button');
```

### Async Utilities

- **findBy**: Wait for element to appear
- **waitFor**: Wait for assertion to pass
- **waitForElementToBeRemoved**: Wait for element to disappear

```typescript
// Wait for element
const element = await screen.findByText('Loaded');

// Wait for assertion
await waitFor(() => {
  expect(screen.getByText('Success')).toBeInTheDocument();
});

// Wait for removal
await waitForElementToBeRemoved(() => screen.queryByText('Loading'));
```

### Avoid Implementation Details

```typescript
// ❌ Bad - testing implementation
expect(component.state.count).toBe(1);

// ✅ Good - testing behavior
expect(screen.getByText('Count: 1')).toBeInTheDocument();
```

## Coverage

### Running Coverage

```bash
vitest --coverage
```

### Coverage Thresholds

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html', 'lcov'],
      lines: 80,
      functions: 80,
      branches: 80,
      statements: 80,
    },
  },
});
```

**Note**: 100% coverage doesn't guarantee bug-free code. Focus on testing critical paths.
