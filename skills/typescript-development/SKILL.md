---
name: typescript-development
description: "Write type-safe JavaScript applications with TypeScript using advanced types, generics, utility types, and design patterns. Master type inference, conditional types, mapped types, template literal types, and branded types. Use for: adding static type checking to JavaScript projects, creating reusable generic components and functions, implementing type-safe APIs and data models, preventing runtime errors through compile-time validation, building scalable enterprise applications, integrating with React/Node.js/frameworks, and leveraging TypeScript's powerful type system for better developer experience and code maintainability."
---

# TypeScript Development

Write type-safe, scalable JavaScript applications using TypeScript's powerful type system and advanced features.

## Overview

TypeScript is a strongly-typed superset of JavaScript that compiles to plain JavaScript. It provides static type checking, enhanced IDE support, better refactoring capabilities, and improved code maintainability. TypeScript 5+ introduces decorators, const type parameters, and improved type inference.

## Type System Fundamentals

### Basic Types

```typescript
// Primitives
let name: string = "John";
let age: number = 30;
let isActive: boolean = true;
let nothing: null = null;
let notDefined: undefined = undefined;

// Arrays
let numbers: number[] = [1, 2, 3];
let strings: Array<string> = ["a", "b", "c"];

// Tuples
let tuple: [string, number] = ["hello", 42];

// Enums
enum Color {
  Red,
  Green,
  Blue
}
let color: Color = Color.Red;

// Any (avoid when possible)
let anything: any = "could be anything";

// Unknown (safer than any)
let userInput: unknown;
if (typeof userInput === "string") {
  console.log(userInput.toUpperCase());
}

// Never (functions that never return)
function throwError(message: string): never {
  throw new Error(message);
}
```

### Type Inference

TypeScript automatically infers types when possible:

```typescript
let inferredString = "hello"; // Type: string
let inferredNumber = 42; // Type: number
let inferredArray = [1, 2, 3]; // Type: number[]

function add(a: number, b: number) {
  return a + b; // Return type inferred as number
}
```

### Union and Intersection Types

```typescript
// Union: value can be one of several types
type StringOrNumber = string | number;
let value: StringOrNumber = "hello";
value = 42; // Also valid

// Intersection: combines multiple types
type Person = { name: string };
type Employee = { employeeId: number };
type Staff = Person & Employee;

const staff: Staff = {
  name: "John",
  employeeId: 123
};
```

## Advanced Type Manipulation

### Conditional Types

```typescript
type IsString<T> = T extends string ? true : false;

type A = IsString<string>; // true
type B = IsString<number>; // false

// Extract array element type
type ElementType<T> = T extends (infer U)[] ? U : never;
type NumType = ElementType<number[]>; // number
```

### Mapped Types

```typescript
// Make all properties optional
type Partial<T> = {
  [P in keyof T]?: T[P];
};

// Make all properties readonly
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};

// Custom mapped type
type Stringify<T> = {
  [P in keyof T]: string;
};

interface User {
  name: string;
  age: number;
}

type StringUser = Stringify<User>;
// { name: string; age: string }
```

### Template Literal Types

```typescript
type EventName = "click" | "focus" | "blur";
type EventHandler = \`on\${Capitalize<EventName>}\`;
// "onClick" | "onFocus" | "onBlur"

type HTTPMethod = "GET" | "POST" | "PUT" | "DELETE";
type Endpoint = \`/api/\${string}\`;
type APIRoute = \`\${HTTPMethod} \${Endpoint}\`;
// "GET /api/users" | "POST /api/users" | etc.
```

## Generics

### Generic Functions

```typescript
function identity<T>(arg: T): T {
  return arg;
}

let output1 = identity<string>("hello");
let output2 = identity(42); // Type inferred

function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const person = { name: "John", age: 30 };
const name = getProperty(person, "name"); // Type: string
```

### Generic Interfaces and Classes

```typescript
interface Repository<T> {
  getById(id: string): Promise<T>;
  getAll(): Promise<T[]>;
  create(item: T): Promise<T>;
  update(id: string, item: T): Promise<T>;
  delete(id: string): Promise<void>;
}

class UserRepository implements Repository<User> {
  async getById(id: string): Promise<User> {
    // Implementation
  }
  // ... other methods
}

// Generic class
class Box<T> {
  private value: T;
  
  constructor(value: T) {
    this.value = value;
  }
  
  getValue(): T {
    return this.value;
  }
}
```

### Generic Constraints

```typescript
interface Lengthwise {
  length: number;
}

function logLength<T extends Lengthwise>(arg: T): T {
  console.log(arg.length);
  return arg;
}

logLength("hello"); // OK
logLength([1, 2, 3]); // OK
logLength({ length: 10, value: 3 }); // OK
// logLength(3); // Error: number doesn't have length
```

## Utility Types

### Built-in Utilities

```typescript
interface User {
  id: string;
  name: string;
  email: string;
  age: number;
}

// Partial - all properties optional
type PartialUser = Partial<User>;

// Required - all properties required
type RequiredUser = Required<PartialUser>;

// Pick - select specific properties
type UserPreview = Pick<User, "id" | "name">;

// Omit - exclude specific properties
type UserWithoutId = Omit<User, "id">;

// Record - create object type with specific keys
type UserRoles = Record<string, "admin" | "user" | "guest">;

// ReturnType - extract function return type
function getUser() {
  return { id: "1", name: "John" };
}
type User = ReturnType<typeof getUser>;

// Parameters - extract function parameter types
function createUser(name: string, age: number) {}
type CreateUserParams = Parameters<typeof createUser>;
// [string, number]

// Awaited - unwrap Promise type
type Response = Awaited<Promise<User>>;
// User
```

## Type Guards and Narrowing

### typeof Guards

```typescript
function processValue(value: string | number) {
  if (typeof value === "string") {
    return value.toUpperCase(); // Type: string
  } else {
    return value.toFixed(2); // Type: number
  }
}
```

### instanceof Guards

```typescript
class Dog {
  bark() {}
}

class Cat {
  meow() {}
}

function makeSound(animal: Dog | Cat) {
  if (animal instanceof Dog) {
    animal.bark();
  } else {
    animal.meow();
  }
}
```

### Custom Type Guards

```typescript
interface Fish {
  swim(): void;
}

interface Bird {
  fly(): void;
}

function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}

function move(pet: Fish | Bird) {
  if (isFish(pet)) {
    pet.swim();
  } else {
    pet.fly();
  }
}
```

### Discriminated Unions

```typescript
interface Circle {
  kind: "circle";
  radius: number;
}

interface Square {
  kind: "square";
  sideLength: number;
}

interface Triangle {
  kind: "triangle";
  base: number;
  height: number;
}

type Shape = Circle | Square | Triangle;

function getArea(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.sideLength ** 2;
    case "triangle":
      return (shape.base * shape.height) / 2;
    default:
      const _exhaustive: never = shape;
      return _exhaustive;
  }
}
```

## Configuration (tsconfig.json)

### Essential Compiler Options

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "exactOptionalPropertyTypes": true,
    
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    
    "outDir": "./dist",
    "rootDir": "./src",
    
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## Integration with Frameworks

### React with TypeScript

```typescript
import { FC, useState, useEffect } from 'react';

interface Props {
  userId: string;
  onUpdate?: (user: User) => void;
}

const UserProfile: FC<Props> = ({ userId, onUpdate }) => {
  const [user, setUser] = useState<User | null>(null);
  
  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId]);
  
  if (!user) return <div>Loading...</div>;
  
  return <div>{user.name}</div>;
};
```

### Node.js with TypeScript

```typescript
import express, { Request, Response, NextFunction } from 'express';

const app = express();

interface CustomRequest extends Request {
  user?: User;
}

app.get('/api/users/:id', async (req: Request<{ id: string }>, res: Response) => {
  const user = await getUserById(req.params.id);
  res.json(user);
});

app.listen(3000);
```

## Best Practices

### Prefer Type Inference

```typescript
// ❌ Redundant type annotation
const name: string = "John";

// ✅ Let TypeScript infer
const name = "John";
```

### Use Const Assertions

```typescript
// ❌ Type: string[]
const colors = ["red", "green", "blue"];

// ✅ Type: readonly ["red", "green", "blue"]
const colors = ["red", "green", "blue"] as const;
```

### Avoid Any

```typescript
// ❌ Loses type safety
function process(data: any) {}

// ✅ Use unknown and narrow
function process(data: unknown) {
  if (typeof data === "string") {
    console.log(data.toUpperCase());
  }
}
```

### Use Branded Types for Type Safety

```typescript
type UserId = string & { readonly brand: unique symbol };
type ProductId = string & { readonly brand: unique symbol };

function getUserById(id: UserId) {}
function getProductById(id: ProductId) {}

const userId = "user-123" as UserId;
const productId = "product-456" as ProductId;

getUserById(userId); // OK
// getUserById(productId); // Error!
```

## Using the Reference Files

### When to Read Each Reference

**`/references/advanced-types.md`** — Read when implementing conditional types, mapped types, template literals, or complex type transformations.

**`/references/generics-patterns.md`** — Read when creating reusable generic functions, classes, or implementing type-safe APIs.

**`/references/integration-guide.md`** — Read when integrating TypeScript with React, Node.js, Express, or other frameworks.

**`/references/migration-guide.md`** — Read when converting JavaScript projects to TypeScript or upgrading TypeScript versions.
