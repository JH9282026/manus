---
name: react-frontend-development
description: "Build modern, scalable React applications using functional components, hooks, and the Composition API. Master state management, component architecture, performance optimization, and integration with frameworks like Next.js. Use for: creating interactive UIs, implementing complex state logic with hooks, optimizing rendering performance, building reusable component libraries, integrating with TypeScript, managing side effects, implementing routing and data fetching patterns, and following React 2026 best practices."
---

# React Frontend Development

Build production-ready React applications using modern patterns, hooks, and performance optimization techniques.

## Overview

React is a declarative, component-based JavaScript library for building user interfaces. This skill covers React 18+ features including functional components, hooks, Server Components, Suspense, and integration with modern frameworks. Focus on scalable architecture, type safety with TypeScript, and performance optimization for production applications.

## Modern React Stack (2026)

| Use Case | Recommended Approach | Alternative |
|----------|---------------------|-------------|
| New production app | Next.js 15 with App Router | Remix, Vite + React Router |
| SPA without SSR | Vite + React Router | Create React App (deprecated) |
| Build tool | Vite, Turbopack | Webpack 5 |
| State management (complex) | Zustand, Jotai | Redux Toolkit, Context + useReducer |
| Forms | React Hook Form | Formik, native controlled components |
| Data fetching | TanStack Query, SWR | Native fetch in useEffect |
| Styling | Tailwind CSS, CSS Modules | Styled Components, Emotion |
| Type safety | TypeScript | PropTypes (legacy) |

## Component Architecture

### Functional Components (Preferred)

Use functional components with hooks for all new development:

```typescript
import { useState, useEffect } from 'react';

interface UserProfileProps {
  userId: string;
}

export function UserProfile({ userId }: UserProfileProps) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUser(userId).then(data => {
      setUser(data);
      setLoading(false);
    });
  }, [userId]);

  if (loading) return <Spinner />;
  return <div>{user.name}</div>;
}
```

### Component Organization

- **Presentational Components**: Pure UI components receiving props
- **Container Components**: Handle logic, state, and data fetching
- **Custom Hooks**: Extract reusable stateful logic
- **Compound Components**: Related components working together

## Essential Hooks Patterns

### State Management

**useState** - Local component state:
```typescript
const [count, setCount] = useState(0);
// Functional updates for derived state
setCount(prev => prev + 1);
// Lazy initialization for expensive computations
const [state, setState] = useState(() => computeExpensiveValue());
```

**useReducer** - Complex state logic:
```typescript
const [state, dispatch] = useReducer(reducer, initialState);
```

**useContext** - Share state without prop drilling:
```typescript
const theme = useContext(ThemeContext);
```

### Side Effects

**useEffect** - Synchronize with external systems:
```typescript
useEffect(() => {
  const subscription = api.subscribe(userId);
  return () => subscription.unsubscribe(); // Cleanup
}, [userId]); // Dependencies
```

**Rules for useEffect**:
- Include all dependencies in the dependency array
- Return cleanup functions for subscriptions/timers
- Separate unrelated effects into multiple useEffect calls
- Avoid overuse - prefer loaders or Server Components for data fetching

### Performance Optimization

**useMemo** - Memoize expensive calculations:
```typescript
const sortedItems = useMemo(() => 
  items.sort((a, b) => a.value - b.value),
  [items]
);
```

**useCallback** - Memoize callback functions:
```typescript
const handleClick = useCallback(() => {
  doSomething(value);
}, [value]);
```

**Note**: React Compiler (v1.0+) automates memoization - use sparingly.

### Refs and DOM Access

**useRef** - Persist values without re-renders:
```typescript
const inputRef = useRef<HTMLInputElement>(null);
const previousValue = useRef(value);
```

## Custom Hooks

Extract reusable logic into custom hooks:

```typescript
function useFetch<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    let cancelled = false;
    fetch(url)
      .then(res => res.json())
      .then(data => !cancelled && setData(data))
      .catch(err => !cancelled && setError(err))
      .finally(() => !cancelled && setLoading(false));
    return () => { cancelled = true; };
  }, [url]);

  return { data, loading, error };
}
```

## State Management Strategies

### Local State
Use `useState` or `useReducer` for component-specific state.

### Lifted State
Lift state to common ancestor when multiple components need access.

### Context API
For global state (theme, auth, locale) without external libraries:
```typescript
const AuthContext = createContext<AuthState | null>(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  return (
    <AuthContext.Provider value={{ user, setUser }}>
      {children}
    </AuthContext.Provider>
  );
}
```

### External Libraries
- **Zustand**: Minimal, unopinionated state management
- **Jotai**: Atomic state management
- **Redux Toolkit**: For complex, enterprise applications
- **TanStack Query**: Server state management

## Performance Best Practices

### Rendering Optimization

1. **React.memo** - Prevent unnecessary re-renders:
```typescript
const MemoizedComponent = React.memo(ExpensiveComponent);
```

2. **Code Splitting** - Lazy load components:
```typescript
const LazyComponent = lazy(() => import('./HeavyComponent'));

<Suspense fallback={<Loading />}>
  <LazyComponent />
</Suspense>
```

3. **Virtualization** - Render large lists efficiently:
```typescript
import { FixedSizeList } from 'react-window';
```

### Avoid Common Pitfalls

- Don't create components inside render functions
- Don't mutate state directly - use setState
- Don't use index as key for dynamic lists
- Avoid inline object/array creation in JSX props
- Don't call hooks conditionally or in loops

## TypeScript Integration

### Component Props
```typescript
interface ButtonProps {
  variant: 'primary' | 'secondary';
  onClick: () => void;
  children: React.ReactNode;
  disabled?: boolean;
}

export function Button({ variant, onClick, children, disabled }: ButtonProps) {
  return <button onClick={onClick} disabled={disabled}>{children}</button>;
}
```

### Generic Components
```typescript
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return <>{items.map(renderItem)}</>;
}
```

## Testing Strategies

- **Unit Tests**: Test hooks and utilities with Vitest
- **Component Tests**: Use React Testing Library
- **Integration Tests**: Test user flows with Playwright
- **Visual Regression**: Storybook + Chromatic

## Framework Integration

### Next.js App Router
- Server Components by default (no client JS)
- Client Components with `"use client"` directive
- Server Actions for mutations
- Streaming with Suspense

### Vite + React Router
- Fast dev server with HMR
- File-based or code-based routing
- Data loaders and actions

## Using the Reference Files

### When to Read Each Reference

**`/references/hooks-advanced-patterns.md`** — Read when implementing complex state logic, creating custom hooks, or optimizing performance with memoization.

**`/references/component-patterns.md`** — Read when designing reusable component APIs, implementing compound components, or structuring large applications.

**`/references/performance-optimization.md`** — Read when diagnosing rendering issues, optimizing bundle size, or implementing code splitting strategies.

**`/references/server-components.md`** — Read when working with Next.js App Router, implementing Server Components, or understanding the client/server boundary.

**`/references/testing-guide.md`** — Read when setting up testing infrastructure, writing component tests, or implementing CI/CD pipelines.

**`/references/migration-guide.md`** — Read when upgrading from class components to hooks, migrating from CRA to Vite, or adopting new React features.
