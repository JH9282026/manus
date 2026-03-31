# TypeScript Best Practices and Code Quality

## Overview

Writing high-quality TypeScript code requires more than just understanding syntax and features. This guide covers best practices, coding conventions, and quality assurance techniques that lead to maintainable, robust, and professional TypeScript applications.

## Type System Best Practices

### 1. Enable Strict Mode

**Always enable strict mode** in `tsconfig.json`:

```json
{
  "compilerOptions": {
    "strict": true
  }
}
```

This enables:
- `strictNullChecks`
- `strictFunctionTypes`
- `strictBindCallApply`
- `strictPropertyInitialization`
- `noImplicitAny`
- `noImplicitThis`
- `alwaysStrict`

### 2. Avoid `any` Type

**Bad:**
```typescript
function processData(data: any) {
  return data.value; // No type safety
}
```

**Good:**
```typescript
function processData(data: unknown) {
  if (typeof data === 'object' && data !== null && 'value' in data) {
    return (data as { value: any }).value;
  }
  throw new Error('Invalid data');
}

// Or better, with proper typing
interface DataWithValue {
  value: string;
}

function processDataTyped(data: DataWithValue) {
  return data.value; // Type-safe
}
```

### 3. Use Type Inference

**Don't over-annotate** when TypeScript can infer types:

**Bad:**
```typescript
const name: string = "John";
const age: number = 30;
const isActive: boolean = true;

function add(a: number, b: number): number {
  return a + b; // Return type obvious
}
```

**Good:**
```typescript
const name = "John";        // Inferred as string
const age = 30;             // Inferred as number
const isActive = true;      // Inferred as boolean

function add(a: number, b: number) {
  return a + b;             // Return type inferred as number
}
```

**Do annotate** when:
- Function parameters (always)
- Public API return types
- Complex types that aren't obvious
- When you want to enforce a specific type

### 4. Prefer Interfaces for Object Shapes

**Interfaces** for object shapes:
```typescript
interface User {
  id: string;
  name: string;
  email: string;
}
```

**Type aliases** for unions, intersections, and primitives:
```typescript
type ID = string | number;
type Status = 'pending' | 'approved' | 'rejected';
type UserWithTimestamp = User & { timestamp: Date };
```

### 5. Use Readonly and Const Assertions

```typescript
// Readonly properties
interface Config {
  readonly apiUrl: string;
  readonly timeout: number;
}

// Const assertions for literal types
const routes = {
  home: '/',
  about: '/about',
  contact: '/contact'
} as const;

type Route = typeof routes[keyof typeof routes];
// Route = "/" | "/about" | "/contact"

// Readonly arrays
const colors: readonly string[] = ['red', 'green', 'blue'];
// colors.push('yellow'); // Error
```

## Naming Conventions

### Variables and Functions

```typescript
// camelCase for variables and functions
const userName = "John";
const userAge = 30;

function getUserData() {
  return { userName, userAge };
}

function calculateTotalPrice(items: Item[]) {
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

### Classes and Interfaces

```typescript
// PascalCase for classes, interfaces, types, enums
class UserService {
  // ...
}

interface UserData {
  // ...
}

type UserRole = 'admin' | 'user';

enum UserStatus {
  Active,
  Inactive,
  Suspended
}
```

### Constants

```typescript
// UPPER_CASE for global constants
const MAX_RETRY_ATTEMPTS = 3;
const API_BASE_URL = 'https://api.example.com';
const DEFAULT_TIMEOUT = 5000;

// camelCase for local constants
function processData() {
  const maxItems = 100;
  const defaultValue = 0;
}
```

### Private Members

```typescript
class User {
  // Private members with # or private keyword
  #password: string;
  private _internalId: number;

  constructor(password: string) {
    this.#password = password;
    this._internalId = Math.random();
  }
}
```

## Code Organization

### File Structure

```typescript
// 1. Imports (grouped and sorted)
import { readFile } from 'fs/promises';
import path from 'path';

import express from 'express';
import cors from 'cors';

import { UserService } from './services/UserService';
import { Logger } from './utils/Logger';
import type { User, UserRole } from './types';

// 2. Type definitions
interface Config {
  port: number;
  host: string;
}

// 3. Constants
const DEFAULT_PORT = 3000;

// 4. Main code
class Application {
  // ...
}

// 5. Exports
export { Application };
export type { Config };
```

### Module Organization

```
src/
├── types/
│   ├── index.ts          # Re-export all types
│   ├── user.ts
│   └── product.ts
├── services/
│   ├── UserService.ts
│   └── ProductService.ts
├── repositories/
│   ├── UserRepository.ts
│   └── ProductRepository.ts
├── utils/
│   ├── logger.ts
│   └── validators.ts
└── index.ts
```

## Function Best Practices

### 1. Keep Functions Small and Focused

**Bad:**
```typescript
function processUserData(user: any) {
  // Validate
  if (!user.email) throw new Error('Email required');
  if (!user.name) throw new Error('Name required');
  
  // Transform
  const normalized = {
    email: user.email.toLowerCase(),
    name: user.name.trim()
  };
  
  // Save to database
  database.save(normalized);
  
  // Send email
  emailService.send(normalized.email, 'Welcome!');
  
  // Log
  logger.log(`User ${normalized.email} processed`);
}
```

**Good:**
```typescript
function validateUser(user: User): void {
  if (!user.email) throw new ValidationError('Email required');
  if (!user.name) throw new ValidationError('Name required');
}

function normalizeUser(user: User): NormalizedUser {
  return {
    email: user.email.toLowerCase(),
    name: user.name.trim()
  };
}

async function processUserData(user: User): Promise<void> {
  validateUser(user);
  const normalized = normalizeUser(user);
  
  await userRepository.save(normalized);
  await emailService.sendWelcome(normalized.email);
  logger.info(`User ${normalized.email} processed`);
}
```

### 2. Limit Function Parameters

**Bad:**
```typescript
function createUser(
  name: string,
  email: string,
  age: number,
  address: string,
  phone: string,
  role: string
) {
  // ...
}
```

**Good:**
```typescript
interface CreateUserParams {
  name: string;
  email: string;
  age: number;
  address: string;
  phone: string;
  role: UserRole;
}

function createUser(params: CreateUserParams) {
  // ...
}

// Usage
createUser({
  name: 'John',
  email: 'john@example.com',
  age: 30,
  address: '123 Main St',
  phone: '555-0100',
  role: 'user'
});
```

### 3. Avoid Boolean Parameters

**Bad:**
```typescript
function getUsers(includeInactive: boolean) {
  // What does true mean?
}

getUsers(true); // Unclear
```

**Good:**
```typescript
type UserFilter = 'all' | 'active' | 'inactive';

function getUsers(filter: UserFilter = 'active') {
  // Clear intent
}

getUsers('all');      // Clear
getUsers('active');   // Clear
```

### 4. Use Descriptive Names

**Bad:**
```typescript
function proc(d: any) {
  const r = d.map((x: any) => x * 2);
  return r;
}
```

**Good:**
```typescript
function doubleNumbers(numbers: number[]): number[] {
  return numbers.map(num => num * 2);
}
```

## Error Handling

### 1. Use Custom Error Classes

```typescript
class AppError extends Error {
  constructor(
    public message: string,
    public statusCode: number = 500,
    public isOperational: boolean = true
  ) {
    super(message);
    Object.setPrototypeOf(this, AppError.prototype);
    Error.captureStackTrace(this, this.constructor);
  }
}

class ValidationError extends AppError {
  constructor(message: string) {
    super(message, 400);
  }
}

class NotFoundError extends AppError {
  constructor(resource: string) {
    super(`${resource} not found`, 404);
  }
}

class UnauthorizedError extends AppError {
  constructor(message: string = 'Unauthorized') {
    super(message, 401);
  }
}
```

### 2. Handle Errors Appropriately

```typescript
async function getUserById(id: string): Promise<User> {
  try {
    const user = await userRepository.findById(id);
    
    if (!user) {
      throw new NotFoundError('User');
    }
    
    return user;
  } catch (error) {
    if (error instanceof AppError) {
      throw error; // Re-throw operational errors
    }
    
    // Log unexpected errors
    logger.error('Unexpected error in getUserById', error);
    throw new AppError('Failed to retrieve user');
  }
}
```

### 3. Use Result Types for Expected Failures

```typescript
type Result<T, E = Error> = 
  | { success: true; value: T }
  | { success: false; error: E };

function parseJSON<T>(json: string): Result<T> {
  try {
    const value = JSON.parse(json) as T;
    return { success: true, value };
  } catch (error) {
    return { 
      success: false, 
      error: error instanceof Error ? error : new Error('Parse failed')
    };
  }
}

// Usage
const result = parseJSON<User>(jsonString);
if (result.success) {
  console.log(result.value.name);
} else {
  console.error(result.error.message);
}
```

## Async/Await Best Practices

### 1. Always Handle Promise Rejections

```typescript
// Bad
async function fetchData() {
  const data = await fetch('/api/data');
  return data.json();
}

// Good
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    logger.error('Failed to fetch data', error);
    throw error;
  }
}
```

### 2. Use Promise.all for Parallel Operations

```typescript
// Bad - Sequential (slow)
async function getUserData(userId: string) {
  const user = await getUser(userId);
  const posts = await getPosts(userId);
  const comments = await getComments(userId);
  return { user, posts, comments };
}

// Good - Parallel (fast)
async function getUserData(userId: string) {
  const [user, posts, comments] = await Promise.all([
    getUser(userId),
    getPosts(userId),
    getComments(userId)
  ]);
  return { user, posts, comments };
}
```

### 3. Handle Partial Failures

```typescript
async function fetchMultipleResources(ids: string[]) {
  const results = await Promise.allSettled(
    ids.map(id => fetchResource(id))
  );
  
  const successful = results
    .filter((r): r is PromiseFulfilledResult<Resource> => r.status === 'fulfilled')
    .map(r => r.value);
  
  const failed = results
    .filter((r): r is PromiseRejectedResult => r.status === 'rejected')
    .map(r => r.reason);
  
  return { successful, failed };
}
```

## Code Quality Tools

### ESLint Configuration

```json
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-requiring-type-checking"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "project": "./tsconfig.json"
  },
  "rules": {
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/explicit-function-return-type": "warn",
    "@typescript-eslint/no-unused-vars": ["error", { 
      "argsIgnorePattern": "^_" 
    }],
    "@typescript-eslint/naming-convention": [
      "error",
      {
        "selector": "interface",
        "format": ["PascalCase"]
      },
      {
        "selector": "typeAlias",
        "format": ["PascalCase"]
      }
    ],
    "no-console": ["warn", { "allow": ["warn", "error"] }]
  }
}
```

### Prettier Configuration

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "arrowParens": "avoid",
  "endOfLine": "lf"
}
```

## Testing Best Practices

### Unit Testing with Jest

```typescript
// user.service.ts
export class UserService {
  constructor(private repository: UserRepository) {}

  async createUser(data: CreateUserDto): Promise<User> {
    const existing = await this.repository.findByEmail(data.email);
    if (existing) {
      throw new ValidationError('Email already exists');
    }
    return this.repository.create(data);
  }
}

// user.service.test.ts
import { UserService } from './user.service';
import { UserRepository } from './user.repository';
import { ValidationError } from './errors';

describe('UserService', () => {
  let service: UserService;
  let repository: jest.Mocked<UserRepository>;

  beforeEach(() => {
    repository = {
      findByEmail: jest.fn(),
      create: jest.fn(),
    } as any;
    service = new UserService(repository);
  });

  describe('createUser', () => {
    it('should create a new user', async () => {
      const userData = { name: 'John', email: 'john@example.com' };
      const createdUser = { id: '1', ...userData };

      repository.findByEmail.mockResolvedValue(null);
      repository.create.mockResolvedValue(createdUser);

      const result = await service.createUser(userData);

      expect(result).toEqual(createdUser);
      expect(repository.findByEmail).toHaveBeenCalledWith(userData.email);
      expect(repository.create).toHaveBeenCalledWith(userData);
    });

    it('should throw ValidationError if email exists', async () => {
      const userData = { name: 'John', email: 'john@example.com' };
      const existingUser = { id: '1', ...userData };

      repository.findByEmail.mockResolvedValue(existingUser);

      await expect(service.createUser(userData))
        .rejects
        .toThrow(ValidationError);
    });
  });
});
```

## Performance Considerations

### 1. Avoid Unnecessary Type Assertions

```typescript
// Bad
const user = data as User;

// Good - use type guards
function isUser(data: unknown): data is User {
  return (
    typeof data === 'object' &&
    data !== null &&
    'id' in data &&
    'name' in data
  );
}

if (isUser(data)) {
  // data is User here
}
```

### 2. Use Const Enums for Performance

```typescript
// Regular enum (generates runtime code)
enum Direction {
  Up,
  Down,
  Left,
  Right
}

// Const enum (inlined at compile time)
const enum Direction {
  Up,
  Down,
  Left,
  Right
}
```

### 3. Optimize Imports

```typescript
// Bad - imports entire library
import _ from 'lodash';

// Good - imports only what's needed
import debounce from 'lodash/debounce';
import throttle from 'lodash/throttle';
```

## Documentation

### JSDoc Comments

```typescript
/**
 * Calculates the total price of items in a cart
 * @param items - Array of cart items
 * @param taxRate - Tax rate as a decimal (e.g., 0.08 for 8%)
 * @returns Total price including tax
 * @throws {ValidationError} If items array is empty
 * @example
 * ```typescript
 * const total = calculateTotal([{ price: 10 }, { price: 20 }], 0.08);
 * console.log(total); // 32.4
 * ```
 */
function calculateTotal(items: CartItem[], taxRate: number): number {
  if (items.length === 0) {
    throw new ValidationError('Cart cannot be empty');
  }
  const subtotal = items.reduce((sum, item) => sum + item.price, 0);
  return subtotal * (1 + taxRate);
}
```

## Conclusion

Writing high-quality TypeScript code requires discipline, attention to detail, and adherence to best practices. By following these guidelines—enabling strict mode, using proper naming conventions, organizing code effectively, handling errors appropriately, and leveraging quality tools—you can create TypeScript applications that are maintainable, robust, and professional. Remember that code is read more often than it's written, so prioritize clarity and consistency.
