---
name: npm-package-management
description: "Manage JavaScript dependencies and monorepos with npm using workspaces, semantic versioning, and package publishing. Master dependency resolution, scripts, and package.json configuration. Use for: installing and managing project dependencies, creating and publishing npm packages, implementing monorepo architecture with workspaces, managing dependency versions and security updates, configuring npm scripts for automation, resolving dependency conflicts, implementing private package registries, and optimizing node_modules with package-lock.json."
---

# npm Package Management

Master JavaScript package management with npm for dependency management, monorepos, and package publishing.

## Overview

npm (Node Package Manager) is the default package manager for Node.js, providing dependency management, package publishing, and workspace support for monorepos. npm 7+ introduces workspaces, improved dependency resolution, automatic peer dependency installation, and enhanced security features.

## Package.json Configuration

### Essential Fields

```json
{
  "name": "my-package",
  "version": "1.0.0",
  "description": "Package description",
  "main": "dist/index.js",
  "module": "dist/index.esm.js",
  "types": "dist/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/index.esm.js",
      "require": "./dist/index.js",
      "types": "./dist/index.d.ts"
    }
  },
  "files": [
    "dist",
    "README.md"
  ],
  "scripts": {
    "build": "tsc",
    "test": "jest",
    "lint": "eslint src",
    "prepublishOnly": "npm run build"
  },
  "keywords": ["javascript", "utility"],
  "author": "Your Name <email@example.com>",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/user/repo.git"
  },
  "bugs": {
    "url": "https://github.com/user/repo/issues"
  },
  "homepage": "https://github.com/user/repo#readme"
}
```

### Dependency Types

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "lodash": "~4.17.21"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "jest": "^29.0.0"
  },
  "peerDependencies": {
    "react": ">=16.8.0"
  },
  "optionalDependencies": {
    "fsevents": "^2.3.2"
  },
  "bundledDependencies": [
    "private-package"
  ]
}
```

## Dependency Management

### Installing Packages

```bash
# Install from package.json
npm install
npm ci  # Clean install (uses package-lock.json)

# Install specific package
npm install lodash
npm install react@18.2.0
npm install --save-dev typescript

# Install globally
npm install -g typescript

# Install from git
npm install user/repo
npm install github:user/repo#branch

# Install from tarball
npm install ./package.tgz
npm install https://example.com/package.tgz
```

### Version Ranges

```json
{
  "dependencies": {
    "exact": "1.2.3",
    "caret": "^1.2.3",      // >=1.2.3 <2.0.0
    "tilde": "~1.2.3",      // >=1.2.3 <1.3.0
    "range": ">=1.2.3 <2.0.0",
    "latest": "*",
    "tag": "latest",
    "git": "git://github.com/user/repo.git"
  }
}
```

### Updating Packages

```bash
# Check outdated packages
npm outdated

# Update packages
npm update
npm update lodash
npm update --save

# Update to latest (ignoring semver)
npm install lodash@latest
```

## npm Workspaces (Monorepo)

### Workspace Configuration

```json
{
  "name": "my-monorepo",
  "private": true,
  "workspaces": [
    "packages/*",
    "apps/*"
  ]
}
```

### Project Structure

```
my-monorepo/
├── package.json
├── package-lock.json
├── packages/
│   ├── package-a/
│   │   └── package.json
│   └── package-b/
│       └── package.json
└── apps/
    └── web/
        └── package.json
```

### Workspace Commands

```bash
# Install all workspace dependencies
npm install

# Run script in specific workspace
npm run build --workspace=package-a
npm run build -w package-a

# Run script in all workspaces
npm run test --workspaces
npm run test --workspaces --if-present

# Add dependency to workspace
npm install lodash --workspace=package-a

# Add local workspace dependency
# In packages/package-b/package.json
{
  "dependencies": {
    "package-a": "*"
  }
}
```

### Workspace Dependencies

```json
{
  "name": "@myorg/package-a",
  "version": "1.0.0",
  "dependencies": {
    "lodash": "^4.17.21"
  }
}

{
  "name": "@myorg/package-b",
  "version": "1.0.0",
  "dependencies": {
    "@myorg/package-a": "*",
    "lodash": "^4.17.21"
  }
}
```

## npm Scripts

### Common Patterns

```json
{
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "build": "tsc && vite build",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "lint": "eslint src",
    "lint:fix": "eslint src --fix",
    "format": "prettier --write src",
    "clean": "rm -rf dist",
    "prebuild": "npm run clean",
    "postbuild": "npm run test"
  }
}
```

### Lifecycle Scripts

```json
{
  "scripts": {
    "preinstall": "echo 'Before install'",
    "postinstall": "echo 'After install'",
    "prepublishOnly": "npm run build && npm test",
    "prepare": "husky install",
    "preversion": "npm test",
    "version": "npm run build",
    "postversion": "git push && git push --tags"
  }
}
```

### Running Scripts

```bash
# Run script
npm run build
npm run test

# Run with arguments
npm run test -- --watch
npm run build -- --mode production

# Run multiple scripts
npm run clean && npm run build
npm run lint & npm run test  # Parallel
```

## Publishing Packages

### Preparing for Publish

```json
{
  "name": "@myorg/my-package",
  "version": "1.0.0",
  "private": false,
  "publishConfig": {
    "access": "public",
    "registry": "https://registry.npmjs.org/"
  },
  "files": [
    "dist",
    "README.md",
    "LICENSE"
  ]
}
```

### Publishing Workflow

```bash
# Login to npm
npm login

# Check what will be published
npm pack --dry-run

# Publish package
npm publish

# Publish scoped package
npm publish --access public

# Publish to specific tag
npm publish --tag beta

# Unpublish (within 72 hours)
npm unpublish @myorg/package@1.0.0
```

### Semantic Versioning

```bash
# Patch release (1.0.0 -> 1.0.1)
npm version patch

# Minor release (1.0.0 -> 1.1.0)
npm version minor

# Major release (1.0.0 -> 2.0.0)
npm version major

# Prerelease (1.0.0 -> 1.0.1-0)
npm version prerelease

# Custom version
npm version 1.2.3
```

## Security

### Auditing Dependencies

```bash
# Run security audit
npm audit

# Fix vulnerabilities
npm audit fix

# Fix with breaking changes
npm audit fix --force

# View audit report
npm audit --json
```

### Package Lock

```bash
# Generate package-lock.json
npm install

# Update package-lock.json
npm update

# Verify integrity
npm ci
```

## Configuration

### .npmrc File

```ini
# Project .npmrc
registry=https://registry.npmjs.org/
@myorg:registry=https://npm.pkg.github.com/

# Authentication
//registry.npmjs.org/:_authToken=${NPM_TOKEN}

# Settings
save-exact=true
package-lock=true
engine-strict=true
```

### Environment Variables

```bash
# Set registry
export NPM_CONFIG_REGISTRY=https://registry.npmjs.org/

# Set auth token
export NPM_TOKEN=your-token-here

# Use in .npmrc
//registry.npmjs.org/:_authToken=${NPM_TOKEN}
```

## Best Practices

### Dependency Management

```bash
# Use exact versions for applications
npm install --save-exact lodash

# Use ranges for libraries
npm install lodash  # Uses ^

# Audit regularly
npm audit

# Keep dependencies updated
npm outdated
npm update
```

### Package.json

```json
{
  "engines": {
    "node": ">=18.0.0",
    "npm": ">=9.0.0"
  },
  "volta": {
    "node": "18.16.0",
    "npm": "9.5.1"
  }
}
```

## Using the Reference Files

### When to Read Each Reference

**`/references/workspace-patterns.md`** — Read when setting up monorepos, managing workspace dependencies, or implementing shared configurations.

**`/references/publishing-guide.md`** — Read when creating npm packages, configuring package.json for publishing, or managing package versions.

**`/references/security-best-practices.md`** — Read when auditing dependencies, implementing security policies, or managing private packages.

**`/references/troubleshooting.md`** — Read when resolving dependency conflicts, debugging installation issues, or optimizing node_modules.

## References

- [01 Npm Fundamentals Best Practices](references/01_npm_fundamentals_best_practices.md)
- [02 Lockfiles Reproducible Builds](references/02_lockfiles_reproducible_builds.md)
- [03 Security Vulnerability Management](references/03_security_vulnerability_management.md)
- [04 Workspaces Monorepo Management](references/04_workspaces_monorepo_management.md)
