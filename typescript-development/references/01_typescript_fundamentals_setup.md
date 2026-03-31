# TypeScript Fundamentals and Setup

## Overview

TypeScript is a strongly typed superset of JavaScript that compiles to plain JavaScript. It provides static type-checking, enhanced IDE support, and modern JavaScript features, making it the gold standard for building scalable, maintainable, and robust applications.

## What is TypeScript?

TypeScript extends JavaScript by adding:
- **Static Type System**: Catch errors at compile-time rather than runtime
- **Modern JavaScript Features**: Use latest ECMAScript features with backward compatibility
- **Enhanced IDE Support**: Better autocomplete, refactoring, and navigation
- **Object-Oriented Features**: Interfaces, classes, generics, and more
- **Gradual Adoption**: Can be introduced incrementally into existing JavaScript projects

## Why Use TypeScript?

### 1. Type Safety
- Catch errors during development, not in production
- Prevent common bugs like `undefined is not a function`
- Ensure function parameters and return values match expectations
- Reduce runtime errors significantly

### 2. Better Developer Experience
- Intelligent code completion
- Inline documentation
- Easier refactoring
- Better code navigation
- Improved collaboration through self-documenting code

### 3. Scalability
- Easier to maintain large codebases
- Clear contracts between different parts of the application
- Facilitates team collaboration
- Reduces technical debt

### 4. Modern JavaScript Features
- Use latest ECMAScript features
- Compile to older JavaScript versions for compatibility
- Access to experimental features

### 5. Strong Ecosystem
- First-class support in major frameworks (React, Angular, Vue)
- Extensive type definitions for popular libraries (@types packages)
- Large and active community
- Excellent tooling support

## Installation and Setup

### Prerequisites

- Node.js (version 14 or higher recommended)
- npm or yarn package manager
- Code editor (VS Code recommended for best TypeScript support)

### Installing TypeScript

#### Global Installation
```bash
npm install -g typescript
```

#### Project-Specific Installation (Recommended)
```bash
npm install --save-dev typescript
```

#### Verify Installation
```bash
tsc --version
```

### Project Initialization

#### Create a New TypeScript Project
```bash
mkdir my-typescript-project
cd my-typescript-project
npm init -y
npm install --save-dev typescript
npx tsc --init
```

This creates a `tsconfig.json` file with default configuration.

## TypeScript Configuration (tsconfig.json)

### Essential Configuration

```json
{
  "compilerOptions": {
    // Language and Environment
    "target": "ES2020",                    // ECMAScript target version
    "lib": ["ES2020", "DOM"],             // Standard library to include
    "module": "commonjs",                  // Module system
    
    // Module Resolution
    "moduleResolution": "node",            // How modules are resolved
    "esModuleInterop": true,               // Enables emit interoperability
    "resolveJsonModule": true,             // Allow importing JSON files
    
    // Type Checking - STRICT MODE (ESSENTIAL)
    "strict": true,                        // Enable all strict type checks
    "noImplicitAny": true,                 // Error on expressions with implied 'any'
    "strictNullChecks": true,              // Strict null checking
    "strictFunctionTypes": true,           // Strict function type checking
    "strictBindCallApply": true,           // Strict bind/call/apply methods
    "strictPropertyInitialization": true,  // Ensure class properties are initialized
    "noImplicitThis": true,                // Error on 'this' with implied 'any'
    "alwaysStrict": true,                  // Parse in strict mode
    
    // Additional Checks
    "noUnusedLocals": true,                // Error on unused local variables
    "noUnusedParameters": true,            // Error on unused parameters
    "noImplicitReturns": true,             // Error when not all code paths return
    "noFallthroughCasesInSwitch": true,    // Error on fallthrough cases
    "forceConsistentCasingInFileNames": true, // Ensure consistent casing
    
    // Emit
    "outDir": "./dist",                    // Output directory
    "rootDir": "./src",                    // Root directory of source files
    "declaration": true,                   // Generate .d.ts files
    "sourceMap": true,                     // Generate source maps
    "removeComments": true,                // Remove comments in output
    
    // Interop Constraints
    "skipLibCheck": true                   // Skip type checking of declaration files
  },
  "include": ["src/**/*"],                // Files to include
  "exclude": ["node_modules", "dist"]     // Files to exclude
}
```

### Configuration Presets

#### For Node.js Projects
```json
{
  "extends": "@tsconfig/node16/tsconfig.json",
  "compilerOptions": {
    "outDir": "dist"
  }
}
```

#### For React Projects
```json
{
  "extends": "@tsconfig/react/tsconfig.json",
  "compilerOptions": {
    "jsx": "react-jsx"
  }
}
```

## Basic TypeScript Syntax

### Type Annotations

```typescript
// Variables
let name: string = "John";
let age: number = 30;
let isActive: boolean = true;

// Arrays
let numbers: number[] = [1, 2, 3];
let names: Array<string> = ["Alice", "Bob"];

// Objects
let user: { name: string; age: number } = {
  name: "John",
  age: 30
};

// Functions
function greet(name: string): string {
  return `Hello, ${name}!`;
}

const add = (a: number, b: number): number => a + b;
```

### Type Inference

```typescript
// TypeScript infers types when possible
let message = "Hello"; // inferred as string
let count = 42;        // inferred as number

function multiply(a: number, b: number) {
  return a * b;        // return type inferred as number
}
```

### Interfaces

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  age?: number;        // Optional property
  readonly createdAt: Date; // Read-only property
}

const user: User = {
  id: 1,
  name: "John Doe",
  email: "john@example.com",
  createdAt: new Date()
};
```

### Type Aliases

```typescript
type ID = string | number;
type Status = "pending" | "approved" | "rejected";

type User = {
  id: ID;
  name: string;
  status: Status;
};
```

### Union and Intersection Types

```typescript
// Union Types
type StringOrNumber = string | number;

function printId(id: StringOrNumber) {
  console.log(`ID: ${id}`);
}

// Intersection Types
type Person = { name: string };
type Employee = { employeeId: number };
type Staff = Person & Employee;

const staff: Staff = {
  name: "John",
  employeeId: 12345
};
```

## Compiling TypeScript

### Basic Compilation

```bash
# Compile a single file
tsc index.ts

# Compile all files in project
tsc

# Watch mode (recompile on changes)
tsc --watch
```

### Using npm Scripts

Add to `package.json`:

```json
{
  "scripts": {
    "build": "tsc",
    "watch": "tsc --watch",
    "start": "node dist/index.js"
  }
}
```

Run with:
```bash
npm run build
npm run watch
npm start
```

## Development Tools

### VS Code Extensions

1. **ESLint**: Linting for TypeScript
2. **Prettier**: Code formatting
3. **TypeScript Importer**: Auto-import suggestions
4. **Path Intellisense**: Autocomplete for file paths

### ESLint Configuration

Install dependencies:
```bash
npm install --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
```

Create `.eslintrc.json`:
```json
{
  "parser": "@typescript-eslint/parser",
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended"
  ],
  "plugins": ["@typescript-eslint"],
  "env": {
    "node": true,
    "es6": true
  },
  "rules": {
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/explicit-function-return-type": "warn"
  }
}
```

### Prettier Configuration

Install:
```bash
npm install --save-dev prettier
```

Create `.prettierrc`:
```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2
}
```

## Project Structure

### Recommended Structure

```
my-typescript-project/
├── src/
│   ├── index.ts
│   ├── types/
│   │   └── index.ts
│   ├── utils/
│   │   └── helpers.ts
│   └── models/
│       └── User.ts
├── dist/              # Compiled output
├── tests/
│   └── index.test.ts
├── node_modules/
├── .eslintrc.json
├── .prettierrc
├── tsconfig.json
├── package.json
└── README.md
```

## Common Pitfalls and Solutions

### 1. Using `any` Type
**Problem**: Defeats the purpose of TypeScript
**Solution**: Use specific types or `unknown` for truly unknown types

### 2. Ignoring Strict Mode
**Problem**: Misses many type-safety benefits
**Solution**: Always enable `"strict": true` in tsconfig.json

### 3. Not Using Type Inference
**Problem**: Verbose, redundant code
**Solution**: Let TypeScript infer types when obvious

### 4. Incorrect Module Resolution
**Problem**: Import errors
**Solution**: Configure `moduleResolution` and `baseUrl` properly

## Next Steps

After mastering the fundamentals:
1. Learn advanced types (generics, conditional types, mapped types)
2. Explore utility types (Partial, Pick, Omit, etc.)
3. Study design patterns in TypeScript
4. Integrate with frameworks (React, Node.js, etc.)
5. Learn testing with TypeScript (Jest, Mocha)

## Conclusion

TypeScript provides a robust foundation for building scalable applications. Proper setup with strict mode enabled, good tooling configuration, and understanding of basic syntax are essential first steps. The investment in learning TypeScript pays dividends in code quality, maintainability, and developer productivity.
