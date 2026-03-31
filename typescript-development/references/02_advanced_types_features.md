# Advanced TypeScript Types and Features

## Overview

TypeScript's advanced type system enables developers to create highly expressive, type-safe code that catches errors at compile-time and provides excellent IDE support. This guide covers advanced type features that distinguish TypeScript as a powerful tool for enterprise development.

## Generics

### What are Generics?

Generics allow you to write reusable code that can work with different types while maintaining type safety.

### Basic Generic Functions

```typescript
// Without generics - limited reusability
function identityNumber(arg: number): number {
  return arg;
}

function identityString(arg: string): string {
  return arg;
}

// With generics - works with any type
function identity<T>(arg: T): T {
  return arg;
}

const num = identity<number>(42);      // Type: number
const str = identity<string>("hello"); // Type: string
const bool = identity(true);           // Type inferred as boolean
```

### Generic Interfaces

```typescript
interface Box<T> {
  value: T;
}

const numberBox: Box<number> = { value: 42 };
const stringBox: Box<string> = { value: "hello" };

// Generic interface with multiple type parameters
interface Pair<K, V> {
  key: K;
  value: V;
}

const pair: Pair<string, number> = {
  key: "age",
  value: 30
};
```

### Generic Classes

```typescript
class DataStore<T> {
  private data: T[] = [];

  add(item: T): void {
    this.data.push(item);
  }

  get(index: number): T | undefined {
    return this.data[index];
  }

  getAll(): T[] {
    return [...this.data];
  }
}

const numberStore = new DataStore<number>();
numberStore.add(1);
numberStore.add(2);

const userStore = new DataStore<User>();
userStore.add({ id: 1, name: "John" });
```

### Generic Constraints

```typescript
// Constrain generic to types with 'length' property
interface HasLength {
  length: number;
}

function logLength<T extends HasLength>(arg: T): void {
  console.log(arg.length);
}

logLength("hello");        // OK: string has length
logLength([1, 2, 3]);      // OK: array has length
logLength({ length: 10 }); // OK: object has length
// logLength(42);          // Error: number doesn't have length

// Constrain to object keys
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { name: "John", age: 30 };
const name = getProperty(user, "name"); // OK
// const invalid = getProperty(user, "invalid"); // Error
```

## Utility Types

### Partial<T>

Makes all properties optional.

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

function updateUser(id: number, updates: Partial<User>): void {
  // Can update any subset of properties
}

updateUser(1, { name: "Jane" });           // OK
updateUser(2, { email: "jane@example.com" }); // OK
updateUser(3, { name: "Bob", email: "bob@example.com" }); // OK
```

### Required<T>

Makes all properties required.

```typescript
interface Config {
  host?: string;
  port?: number;
  timeout?: number;
}

type RequiredConfig = Required<Config>;

const config: RequiredConfig = {
  host: "localhost",
  port: 3000,
  timeout: 5000  // All properties must be provided
};
```

### Readonly<T>

Makes all properties read-only.

```typescript
interface User {
  id: number;
  name: string;
}

const user: Readonly<User> = {
  id: 1,
  name: "John"
};

// user.name = "Jane"; // Error: Cannot assign to 'name'
```

### Pick<T, K>

Creates a type by picking specific properties.

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

type UserPreview = Pick<User, "id" | "name">;

const preview: UserPreview = {
  id: 1,
  name: "John"
  // email and age not required
};
```

### Omit<T, K>

Creates a type by omitting specific properties.

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  password: string;
}

type PublicUser = Omit<User, "password">;

const publicUser: PublicUser = {
  id: 1,
  name: "John",
  email: "john@example.com"
  // password omitted
};
```

### Record<K, T>

Creates an object type with specific keys and value type.

```typescript
type Role = "admin" | "user" | "guest";

type Permissions = Record<Role, string[]>;

const permissions: Permissions = {
  admin: ["read", "write", "delete"],
  user: ["read", "write"],
  guest: ["read"]
};
```

### ReturnType<T>

Extracts the return type of a function.

```typescript
function createUser() {
  return {
    id: 1,
    name: "John",
    email: "john@example.com"
  };
}

type User = ReturnType<typeof createUser>;
// User is { id: number; name: string; email: string; }
```

## Conditional Types

### Basic Conditional Types

```typescript
type IsString<T> = T extends string ? true : false;

type A = IsString<string>;  // true
type B = IsString<number>;  // false

// Practical example
type NonNullable<T> = T extends null | undefined ? never : T;

type A = NonNullable<string | null>;      // string
type B = NonNullable<number | undefined>; // number
```

### Distributive Conditional Types

```typescript
type ToArray<T> = T extends any ? T[] : never;

type StrOrNumArray = ToArray<string | number>;
// Result: string[] | number[]
```

### Infer Keyword

```typescript
// Extract return type
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

// Extract array element type
type ElementType<T> = T extends (infer E)[] ? E : never;

type NumArray = number[];
type Num = ElementType<NumArray>; // number
```

## Mapped Types

### Basic Mapped Types

```typescript
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};

type Optional<T> = {
  [P in keyof T]?: T[P];
};

type Nullable<T> = {
  [P in keyof T]: T[P] | null;
};
```

### Advanced Mapped Types

```typescript
// Add prefix to all keys
type Prefixed<T, P extends string> = {
  [K in keyof T as `${P}${string & K}`]: T[K];
};

interface User {
  name: string;
  age: number;
}

type PrefixedUser = Prefixed<User, "user_">;
// { user_name: string; user_age: number; }

// Filter properties by type
type FilterByType<T, U> = {
  [K in keyof T as T[K] extends U ? K : never]: T[K];
};

interface Mixed {
  name: string;
  age: number;
  active: boolean;
  count: number;
}

type OnlyNumbers = FilterByType<Mixed, number>;
// { age: number; count: number; }
```

## Template Literal Types

### Basic Template Literals

```typescript
type Greeting = `Hello ${string}`;

const greeting1: Greeting = "Hello World";  // OK
const greeting2: Greeting = "Hi World";     // Error

// Combining literal types
type HTTPMethod = "GET" | "POST" | "PUT" | "DELETE";
type Endpoint = "users" | "posts" | "comments";

type APIRoute = `/${Endpoint}`;
// "/users" | "/posts" | "/comments"

type APICall = `${HTTPMethod} ${APIRoute}`;
// "GET /users" | "POST /users" | ... (12 combinations)
```

### Practical Applications

```typescript
// Type-safe event system
type EventName = "click" | "focus" | "blur";
type EventHandler = `on${Capitalize<EventName>}`;
// "onClick" | "onFocus" | "onBlur"

// CSS properties
type CSSProperty = "color" | "background" | "border";
type CSSVariable = `--${CSSProperty}`;
// "--color" | "--background" | "--border"

// API endpoints with parameters
type Endpoint = `api/${'users' | 'posts' | 'comments'}`;
type EndpointWithId = `${Endpoint}/${number}`;
```

## The `satisfies` Operator

### Type Checking Without Widening

```typescript
type Color = "red" | "green" | "blue" | { r: number; g: number; b: number };

const palette = {
  primary: "red",
  secondary: { r: 0, g: 255, b: 0 },
  accent: "blue"
} satisfies Record<string, Color>;

// Type is preserved precisely
palette.primary.toUpperCase(); // OK - knows it's a string
palette.secondary.g;           // OK - knows it's an object

// Without satisfies, would need type assertion or lose precision
```

## `as const` Assertions

### Literal Type Inference

```typescript
// Without as const
const config1 = {
  host: "localhost",  // Type: string
  port: 3000          // Type: number
};

// With as const
const config2 = {
  host: "localhost",  // Type: "localhost"
  port: 3000          // Type: 3000
} as const;

// Array example
const colors1 = ["red", "green", "blue"];  // Type: string[]
const colors2 = ["red", "green", "blue"] as const;  // Type: readonly ["red", "green", "blue"]
```

## Type Guards

### Built-in Type Guards

```typescript
function process(value: string | number) {
  if (typeof value === "string") {
    // TypeScript knows value is string here
    console.log(value.toUpperCase());
  } else {
    // TypeScript knows value is number here
    console.log(value.toFixed(2));
  }
}
```

### Custom Type Guards

```typescript
interface User {
  type: "user";
  name: string;
}

interface Admin {
  type: "admin";
  name: string;
  permissions: string[];
}

type Person = User | Admin;

// Type predicate
function isAdmin(person: Person): person is Admin {
  return person.type === "admin";
}

function greet(person: Person) {
  if (isAdmin(person)) {
    // TypeScript knows person is Admin here
    console.log(person.permissions);
  } else {
    // TypeScript knows person is User here
    console.log(person.name);
  }
}
```

## Discriminated Unions

```typescript
interface Success {
  status: "success";
  data: any;
}

interface Error {
  status: "error";
  message: string;
}

interface Loading {
  status: "loading";
}

type Result = Success | Error | Loading;

function handleResult(result: Result) {
  switch (result.status) {
    case "success":
      console.log(result.data);    // TypeScript knows it's Success
      break;
    case "error":
      console.log(result.message); // TypeScript knows it's Error
      break;
    case "loading":
      console.log("Loading...");   // TypeScript knows it's Loading
      break;
  }
}
```

## Best Practices

1. **Use Generics for Reusability**: Create flexible, type-safe functions and classes
2. **Leverage Utility Types**: Don't reinvent the wheel; use built-in utilities
3. **Prefer `unknown` over `any`**: Requires explicit type checking
4. **Use Template Literals**: Create type-safe string patterns
5. **Employ `satisfies`**: Check types without losing precision
6. **Apply `as const`**: Preserve literal types when needed
7. **Create Custom Type Guards**: Improve type narrowing
8. **Use Discriminated Unions**: Make state management type-safe

## Conclusion

Mastering advanced TypeScript types enables you to build highly expressive, type-safe applications. These features allow you to encode business logic and constraints directly in the type system, catching errors at compile-time and providing excellent developer experience through IDE support. The investment in learning these advanced features pays significant dividends in code quality and maintainability.
