# NPM Workspaces and Monorepo Management

## Overview

NPM Workspaces, introduced in npm 7, provide built-in support for managing monorepos (multiple packages in a single repository). This feature simplifies dependency management, enables seamless inter-package dependencies, and streamlines development workflows.

## Understanding Monorepos

### What is a Monorepo?

#### Definition
- Single repository containing multiple related packages/projects
- Shared version control
- Unified development workflow
- Common tooling and configuration

#### Benefits
- **Code Sharing**: Easy to share code between packages
- **Atomic Changes**: Single commit across multiple packages
- **Consistent Tooling**: Shared configuration and dependencies
- **Simplified Dependencies**: No need to publish for local development
- **Easier Refactoring**: Change multiple packages together

#### Challenges
- **Complexity**: More complex than single-package repos
- **Build Coordination**: Managing build order
- **Scaling**: Performance with many packages
- **Tooling**: Requires proper tooling support

### Monorepo vs. Polyrepo

| Aspect | Monorepo | Polyrepo |
|--------|----------|----------|
| Repositories | One | Many |
| Code Sharing | Easy | Requires publishing |
| Versioning | Coordinated | Independent |
| Tooling | Shared | Per-repo |
| CI/CD | Complex | Simple |
| Onboarding | Single clone | Multiple clones |

## NPM Workspaces Fundamentals

### What are NPM Workspaces?

#### Definition
- Built-in monorepo support in npm 7+
- Manage multiple packages from single root
- Automatic symlinking of local packages
- Shared dependency management

#### Key Concepts
- **Root Package**: Top-level package.json
- **Workspace**: Individual package within monorepo
- **Hoisting**: Shared dependencies at root
- **Symlinks**: Local packages linked in node_modules

### Setting Up Workspaces

#### Basic Configuration

**Root package.json**:
```json
{
  "name": "my-monorepo",
  "version": "1.0.0",
  "private": true,
  "workspaces": [
    "packages/*",
    "apps/*"
  ]
}
```

**Directory Structure**:
```
my-monorepo/
├── package.json
├── package-lock.json
├── node_modules/
├── packages/
│   ├── package-a/
│   │   ├── package.json
│   │   └── index.js
│   └── package-b/
│       ├── package.json
│       └── index.js
└── apps/
    └── web-app/
        ├── package.json
        └── index.js
```

#### Creating Workspaces

**Method 1: Manual Creation**
```bash
# Create directories
mkdir -p packages/package-a
mkdir -p packages/package-b

# Initialize packages
cd packages/package-a
npm init -y
cd ../package-b
npm init -y
```

**Method 2: Using npm init**
```bash
# From root directory
npm init -w packages/package-a
npm init -w packages/package-b
```

#### Workspace Naming

**Scoped Packages** (Recommended):
```json
{
  "name": "@my-org/package-a",
  "version": "1.0.0"
}
```

**Benefits**:
- Avoid conflicts with npm registry
- Clear ownership
- Consistent naming

## Dependency Management

### Installing Dependencies

#### Root-Level Dependencies

```bash
# Install at root (shared by all workspaces)
npm install eslint --save-dev
```

**Use Cases**:
- Development tools (eslint, prettier)
- Build tools (webpack, rollup)
- Testing frameworks (jest, mocha)

#### Workspace-Specific Dependencies

```bash
# Install in specific workspace
npm install express --workspace=packages/package-a

# Short form
npm install express -w packages/package-a
```

#### Multiple Workspaces

```bash
# Install in multiple workspaces
npm install lodash -w packages/package-a -w packages/package-b

# Install in all workspaces
npm install date-fns --workspaces
```

### Dependency Hoisting

#### How It Works

1. **Common Dependencies**: Installed once at root
2. **Different Versions**: Installed in specific workspace
3. **Optimization**: Reduces disk space and installation time

**Example**:
```
Root node_modules/
├── lodash@4.17.21 (shared by package-a and package-b)
├── @my-org/package-a -> packages/package-a (symlink)
└── @my-org/package-b -> packages/package-b (symlink)

packages/package-a/node_modules/
└── express@4.18.0 (specific to package-a)

packages/package-b/node_modules/
└── express@5.0.0 (different version for package-b)
```

#### Benefits
- Reduced disk space
- Faster installations
- Synchronized versions
- Simplified updates

#### Potential Issues
- Dependency resolution conflicts
- Phantom dependencies (accessing hoisted deps not declared)
- Version mismatches

### Inter-Package Dependencies

#### Declaring Dependencies

**packages/package-b/package.json**:
```json
{
  "name": "@my-org/package-b",
  "version": "1.0.0",
  "dependencies": {
    "@my-org/package-a": "^1.0.0"
  }
}
```

#### How It Works

1. Run `npm install` at root
2. NPM creates symlinks in root node_modules
3. Packages can import each other as if published

**Usage in Code**:
```javascript
// packages/package-b/index.js
import { someFunction } from '@my-org/package-a';

// No relative imports needed!
// Not: import { someFunction } from '../package-a';
```

#### Benefits
- No relative imports
- Works like published packages
- Easy refactoring
- Type checking works correctly

## Running Scripts

### Workspace-Specific Scripts

#### Single Workspace

```bash
# Run script in specific workspace
npm run build --workspace=packages/package-a

# Short form
npm run build -w packages/package-a
```

#### Multiple Workspaces

```bash
# Run in all workspaces
npm run test --workspaces

# Run in specific workspaces
npm run build -w packages/package-a -w packages/package-b
```

#### Conditional Execution

```bash
# Run only if script exists
npm run build --workspaces --if-present
```

**Use Case**: Not all packages have all scripts

### Root-Level Scripts

**Root package.json**:
```json
{
  "scripts": {
    "build": "npm run build --workspaces",
    "test": "npm run test --workspaces --if-present",
    "lint": "eslint .",
    "clean": "rm -rf packages/*/dist apps/*/dist"
  }
}
```

**Usage**:
```bash
# From root
npm run build
npm test
```

### Script Execution Order

#### Parallel Execution

By default, npm runs scripts in parallel across workspaces.

**Pros**:
- Faster execution
- Better resource utilization

**Cons**:
- No guaranteed order
- May cause issues with dependencies

#### Sequential Execution

For ordered execution, use tools like npm-run-all or custom scripts.

```bash
# Install npm-run-all
npm install --save-dev npm-run-all

# Sequential execution
npm-run-all --serial build:*
```

## TypeScript Integration

### TypeScript Project References

#### Why Use Project References?

- Manage inter-package dependencies
- Incremental compilation
- Proper type checking
- Build order management

### Configuration

#### Root tsconfig.json

```json
{
  "files": [],
  "references": [
    { "path": "./packages/package-a" },
    { "path": "./packages/package-b" },
    { "path": "./apps/web-app" }
  ]
}
```

#### Base tsconfig.base.json

```json
{
  "compilerOptions": {
    "composite": true,
    "declaration": true,
    "declarationMap": true,
    "incremental": true,
    "skipLibCheck": true,
    "noEmitOnError": true,
    "module": "ESNext",
    "moduleResolution": "node",
    "target": "ES2020",
    "lib": ["ES2020"]
  }
}
```

#### Package-Level tsconfig.json

**packages/package-a/tsconfig.json**:
```json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"],
  "references": []
}
```

**packages/package-b/tsconfig.json**:
```json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"],
  "references": [
    { "path": "../package-a" }
  ]
}
```

### Building TypeScript Workspaces

#### Build Command

```bash
# Build all projects in correct order
npx tsc --build

# Clean build
npx tsc --build --clean

# Force rebuild
npx tsc --build --force

# Watch mode
npx tsc --build --watch
```

#### Package Scripts

```json
{
  "scripts": {
    "build": "tsc --build",
    "build:clean": "tsc --build --clean",
    "build:watch": "tsc --build --watch"
  }
}
```

### .gitignore for TypeScript

```gitignore
# TypeScript
*.tsbuildinfo
**/dist/
**/build/

# Dependencies
node_modules/

# Logs
*.log
```

## Advanced Workspace Features

### Workspace Protocol

#### Using workspace: Protocol

```json
{
  "dependencies": {
    "@my-org/package-a": "workspace:*"
  }
}
```

**Benefits**:
- Explicit workspace dependency
- Always uses local version
- Clear intent

**Note**: npm doesn't support `workspace:` protocol natively (pnpm/yarn feature)

### Filtering Workspaces

#### By Name

```bash
# Specific workspace
npm run test -w @my-org/package-a
```

#### By Pattern

```bash
# All packages matching pattern
npm run build -w packages/*
```

### Listing Workspaces

```bash
# List all workspaces
npm ls --workspaces

# List workspace names
npm ls --workspaces --json | jq -r '.dependencies | keys[]'
```

## Best Practices

### Project Structure

#### Recommended Layout

```
monorepo/
├── package.json (root, private: true)
├── package-lock.json
├── tsconfig.json (root references)
├── tsconfig.base.json (shared config)
├── .gitignore
├── packages/ (libraries)
│   ├── package-a/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   ├── src/
│   │   └── dist/
│   └── package-b/
└── apps/ (applications)
    └── web-app/
        ├── package.json
        ├── tsconfig.json
        └── src/
```

### Naming Conventions

1. **Use Scopes**: `@my-org/package-name`
2. **Consistent Prefixes**: `@my-org/ui-*`, `@my-org/api-*`
3. **Clear Separation**: packages/ for libraries, apps/ for applications

### Dependency Management

1. **Hoist Common Dependencies**: Install shared deps at root
2. **Version Consistency**: Use same versions across workspaces
3. **Minimal Dependencies**: Only install what's needed
4. **Regular Updates**: Keep dependencies up to date

### Scripts and Automation

1. **Root Scripts**: Provide convenience scripts at root
2. **Consistent Naming**: Use same script names across workspaces
3. **Use --if-present**: For optional scripts
4. **Document Scripts**: Add comments in package.json

### Version Control

1. **Commit Lockfile**: Always commit package-lock.json
2. **Ignore Build Outputs**: Add dist/, build/ to .gitignore
3. **Ignore TypeScript Artifacts**: Add *.tsbuildinfo
4. **Review Changes**: Carefully review lockfile changes

## Limitations and Workarounds

### Limitations of NPM Workspaces

#### No Build Introspection
- Cannot visualize dependency graph
- No equivalent to `nx graph`

**Workaround**: Use external tools like Nx or Turborepo

#### No Task Dependencies
- Cannot define task execution order
- Must manually manage build order

**Workaround**: Use npm-run-all or custom scripts

#### No Affected Mechanism
- Cannot run tasks only for changed packages
- Must run tasks for all workspaces

**Workaround**: Use Nx or Turborepo for affected detection

#### Limited Framework Integration
- No native integration with React, Vue, etc.
- Manual configuration required

**Workaround**: Use framework-specific monorepo tools

### Dependency Resolution Issues

#### Phantom Dependencies

**Problem**: Accessing hoisted dependencies not declared

**Solution**:
- Explicitly declare all dependencies
- Use linters to detect phantom deps
- Consider using pnpm (stricter hoisting)

#### Version Conflicts

**Problem**: Different workspaces need different versions

**Solution**:
- Install specific versions in workspace
- Use peer dependencies when appropriate
- Consider version alignment

### Deployment Challenges

#### Shared node_modules

**Problem**: Deploying single package includes all dependencies

**Solutions**:
1. **Build Step**: Bundle package with dependencies
2. **Docker Multi-Stage**: Copy only needed files
3. **Separate Deployment**: Deploy each package independently

**Docker Example**:
```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
COPY packages/package-a packages/package-a
RUN npm ci
RUN npm run build -w packages/package-a

# Production stage
FROM node:18-slim
WORKDIR /app
COPY --from=builder /app/packages/package-a/dist ./dist
COPY --from=builder /app/packages/package-a/package.json ./
RUN npm ci --production
CMD ["node", "dist/index.js"]
```

## Alternative Tools

### When to Consider Alternatives

- Need advanced features (affected, caching)
- Large monorepo (100+ packages)
- Complex build dependencies
- Framework-specific needs

### Popular Alternatives

#### Nx
- Advanced build system
- Affected command
- Computation caching
- Framework integrations

#### Turborepo
- Fast build system
- Remote caching
- Simple configuration
- Good DX

#### Lerna
- Mature monorepo tool
- Version management
- Publishing workflows
- Can work with npm workspaces

#### pnpm Workspaces
- Stricter dependency resolution
- Better disk space efficiency
- Faster installations
- Similar API to npm workspaces

## References

- NPM Workspaces Documentation: https://docs.npmjs.com/cli/v9/using-npm/workspaces
- "NPM Workspaces Monorepo" (Earthly.dev)
- "Setting Up a Monorepo Using NPM Workspaces and TypeScript Project References" (Medium)
- "NPM Workspaces" (YieldCode Blog)
- TypeScript Project References: https://www.typescriptlang.org/docs/handbook/project-references.html
