# NPM Fundamentals and Best Practices

## Overview

NPM (Node Package Manager) is the default package manager for JavaScript and Node.js, providing access to the world's largest software registry. Effective NPM package management requires understanding core concepts, following best practices, and implementing security measures.

## Core Concepts

### What is NPM?

#### Components
- **CLI (Command-Line Interface)**: Tool for interacting with NPM
- **Registry**: Online database of public and private packages (npmjs.org)
- **Package Manager**: Handles installation, updating, and dependency resolution

#### Purpose
- Manage project dependencies
- Share and reuse code
- Version control for packages
- Automate development workflows

### The NPM Ecosystem

#### Public Registry
- Over 2 million packages
- Free and open-source
- Community-driven
- Largest software registry in the world

#### Private Registries
- Organization-specific packages
- Proprietary code
- Access control
- Examples: Verdaccio, npm Enterprise, Artifactory

## Package.json Fundamentals

### Essential Fields

#### Metadata
```json
{
  "name": "my-package",
  "version": "1.0.0",
  "description": "A brief description of the package",
  "keywords": ["javascript", "utility"],
  "author": "Your Name <email@example.com>",
  "license": "MIT"
}
```

#### Entry Points
```json
{
  "main": "index.js",
  "module": "dist/index.esm.js",
  "types": "dist/index.d.ts",
  "bin": {
    "my-cli": "./bin/cli.js"
  }
}
```

#### Scripts
```json
{
  "scripts": {
    "start": "node index.js",
    "test": "jest",
    "build": "webpack",
    "lint": "eslint src/",
    "format": "prettier --write \"src/**/*.js\""
  }
}
```

#### Repository Information
```json
{
  "repository": {
    "type": "git",
    "url": "https://github.com/username/repo.git"
  },
  "bugs": {
    "url": "https://github.com/username/repo/issues"
  },
  "homepage": "https://github.com/username/repo#readme"
}
```

### Private Package Configuration

#### Prevent Accidental Publication
```json
{
  "private": true
}
```

#### Publish Configuration
```json
{
  "publishConfig": {
    "access": "restricted",
    "registry": "https://npm.pkg.github.com"
  }
}
```

### Files Configuration

#### Include Specific Files
```json
{
  "files": [
    "dist/",
    "lib/",
    "README.md",
    "LICENSE"
  ]
}
```

## Scoped Packages

### What are Scopes?

#### Definition
- Namespace for related packages
- Format: `@scope/package-name`
- Tied to organization or user

#### Benefits
- **Organization**: Group related packages
- **Security**: Prevent typosquatting
- **Namespace**: Avoid naming conflicts
- **Access Control**: Manage permissions centrally

### Creating Scoped Packages

#### Initialize with Scope
```bash
npm init --scope=@my-org
```

#### Package.json Example
```json
{
  "name": "@my-org/my-package",
  "version": "1.0.0"
}
```

#### Installing Scoped Packages
```bash
npm install @my-org/my-package
```

### Organizational Scoping Best Practices

1. **Single Scope per Organization**: Use one scope for entire organization
2. **Register on npmjs.org**: Prevent malicious packages
3. **Consistent Naming**: Follow naming conventions
4. **Access Control**: Manage team permissions
5. **Documentation**: Document scope usage

## Semantic Versioning (SemVer)

### Version Format

#### Structure: MAJOR.MINOR.PATCH
- **MAJOR**: Incompatible API changes
- **MINOR**: Backward-compatible functionality
- **PATCH**: Backward-compatible bug fixes

#### Examples
- `1.0.0`: Initial release
- `1.1.0`: New feature added
- `1.1.1`: Bug fix
- `2.0.0`: Breaking change

### Version Ranges

#### Caret (^) - Compatible Updates
```json
{
  "dependencies": {
    "express": "^4.17.1"
  }
}
```
- Allows: `>=4.17.1 <5.0.0`
- Updates: Minor and patch versions

#### Tilde (~) - Patch Updates
```json
{
  "dependencies": {
    "lodash": "~4.17.20"
  }
}
```
- Allows: `>=4.17.20 <4.18.0`
- Updates: Only patch versions

#### Exact Version
```json
{
  "dependencies": {
    "react": "17.0.2"
  }
}
```
- No automatic updates
- Explicit version required

#### Range
```json
{
  "dependencies": {
    "webpack": ">=5.0.0 <6.0.0"
  }
}
```

### Pre-release Versions

#### Format
- `1.0.0-alpha`
- `1.0.0-beta.1`
- `1.0.0-rc.2`

#### Benefits
- Clear development stage
- Immutable identifiers
- Prevent confusion
- Testing and validation

#### Best Practices
- Use standardized identifiers (alpha, beta, rc)
- Integrate with CI/CD
- Avoid custom distribution tags
- Document pre-release purpose

## Package Installation

### Installation Commands

#### Install All Dependencies
```bash
npm install
# or
npm i
```

#### Install Production Dependency
```bash
npm install express
npm install express --save-prod
npm install express -S
```

#### Install Development Dependency
```bash
npm install jest --save-dev
npm install jest -D
```

#### Install Optional Dependency
```bash
npm install fsevents --save-optional
npm install fsevents -O
```

#### Install Global Package
```bash
npm install -g typescript
```

#### Install Specific Version
```bash
npm install react@17.0.2
```

### Installation Flags

#### Production Only
```bash
npm install --production
# or
NODE_ENV=production npm install
```

#### Clean Install (CI)
```bash
npm ci
```
- Uses lockfile exclusively
- Deletes node_modules first
- Faster and more reliable for CI/CD

#### Ignore Scripts
```bash
npm install --ignore-scripts
```
- Prevents lifecycle script execution
- Security measure

## Package Scripts

### Common Scripts

#### Lifecycle Scripts
```json
{
  "scripts": {
    "preinstall": "echo 'Before install'",
    "postinstall": "echo 'After install'",
    "prepublish": "npm run build",
    "prepare": "npm run build",
    "pretest": "npm run lint",
    "test": "jest",
    "posttest": "echo 'Tests complete'"
  }
}
```

#### Custom Scripts
```json
{
  "scripts": {
    "dev": "nodemon index.js",
    "build": "webpack --mode production",
    "clean": "rm -rf dist/",
    "deploy": "npm run build && npm run upload"
  }
}
```

### Running Scripts

#### Execute Script
```bash
npm run build
# or for start/test
npm start
npm test
```

#### Pass Arguments
```bash
npm run test -- --coverage
```

#### Run Multiple Scripts
```bash
npm run clean && npm run build
```

### Script Best Practices

1. **Clear Naming**: Use descriptive script names
2. **Documentation**: Comment complex scripts
3. **Composability**: Break into smaller scripts
4. **Cross-Platform**: Use cross-platform tools (cross-env, rimraf)
5. **Error Handling**: Fail fast on errors

## NPM Configuration

### .npmrc File

#### Project-Level (.npmrc in project root)
```
registry=https://registry.npmjs.org/
save-exact=true
engine-strict=true
```

#### User-Level (~/.npmrc)
```
init-author-name=Your Name
init-author-email=email@example.com
init-license=MIT
```

#### Common Configurations
```
# Use specific registry
registry=https://npm.pkg.github.com

# Scoped registry
@my-org:registry=https://npm.pkg.github.com

# Authentication token
//npm.pkg.github.com/:_authToken=${NPM_TOKEN}

# Save exact versions
save-exact=true

# Ignore scripts
ignore-scripts=true

# Strict engine checking
engine-strict=true
```

### Environment Variables

#### NPM_TOKEN
```bash
export NPM_TOKEN=your_token_here
```

#### NODE_ENV
```bash
export NODE_ENV=production
```

## Best Practices for Package Management

### Package Selection

#### Evaluation Criteria
1. **Popularity**: Weekly downloads, GitHub stars
2. **Maintenance**: Recent updates, active issues
3. **Security**: Known vulnerabilities, security score
4. **Size**: Bundle size (use BundlePhobia)
5. **Documentation**: Clear README, examples
6. **Dependencies**: Number and quality of dependencies
7. **License**: Compatible with your project
8. **Community**: Active contributors, support

#### Security Vetting
- Check package name carefully (typosquatting)
- Use OpenSSF Security Scorecards
- Review deps.dev for dependency analysis
- Run `npm audit` before installing
- Verify package publisher

### Dependency Management

#### Dependencies vs. DevDependencies

**dependencies**: Required for production
```json
{
  "dependencies": {
    "express": "^4.17.1",
    "mongoose": "^6.0.0"
  }
}
```

**devDependencies**: Only for development
```json
{
  "devDependencies": {
    "jest": "^27.0.0",
    "eslint": "^8.0.0",
    "webpack": "^5.0.0"
  }
}
```

#### PeerDependencies

**Purpose**: Specify expected host dependencies
```json
{
  "peerDependencies": {
    "react": "^17.0.0 || ^18.0.0"
  }
}
```

**Use Cases**:
- Plugin systems
- Framework extensions
- Shared dependencies

### Avoiding Git Packages

#### Risks
- Less control over updates
- Potential breaking changes
- No version guarantees
- Harder to audit

#### When Necessary
- Pin to specific commit/tag
```json
{
  "dependencies": {
    "my-package": "git+https://github.com/user/repo.git#v1.0.0"
  }
}
```

### Regular Maintenance

#### Update Dependencies
```bash
# Check outdated packages
npm outdated

# Update to latest within semver range
npm update

# Update specific package
npm update express

# Update to latest (ignoring semver)
npm install express@latest
```

#### Automated Updates
- **Dependabot**: GitHub's automated dependency updates
- **Renovate**: Configurable dependency update bot
- **npm-check-updates**: CLI tool for updating package.json

#### Audit and Fix
```bash
# Audit for vulnerabilities
npm audit

# Automatically fix vulnerabilities
npm audit fix

# Force fix (may introduce breaking changes)
npm audit fix --force
```

## Publishing Packages

### Preparation

#### Pre-publish Checklist
1. ✅ Update version in package.json
2. ✅ Update CHANGELOG.md
3. ✅ Run tests
4. ✅ Build distribution files
5. ✅ Review files to be published
6. ✅ Check .npmignore or files field
7. ✅ Verify README.md
8. ✅ Update documentation

#### Dry Run
```bash
npm publish --dry-run
```

### Publishing

#### Login to NPM
```bash
npm login
```

#### Publish Package
```bash
# Public package
npm publish

# Scoped public package
npm publish --access public

# Private package
npm publish --access restricted
```

#### Publish with Tag
```bash
npm publish --tag beta
```

### Post-publish

#### Verify Publication
```bash
npm view @my-org/my-package
```

#### Create Git Tag
```bash
git tag v1.0.0
git push origin v1.0.0
```

## Security Best Practices

### Prevent Secret Leakage

#### .gitignore
```
node_modules/
.env
.npmrc
*.log
```

#### .npmignore
```
.git/
.env
test/
*.test.js
.github/
```

#### Use files Field
```json
{
  "files": [
    "dist/",
    "lib/"
  ]
}
```

### Enable Two-Factor Authentication

```bash
npm profile enable-2fa auth-and-writes
```

### Token Management

#### Create Token
```bash
npm token create
```

#### List Tokens
```bash
npm token list
```

#### Revoke Token
```bash
npm token revoke <token_id>
```

### CI/CD Security

#### Least Privilege
- Use read-only tokens when possible
- Limit token scope
- Rotate tokens regularly

#### GitHub Actions Example
```yaml
name: Publish
on:
  release:
    types: [created]
jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
          registry-url: 'https://registry.npmjs.org'
      - run: npm ci
      - run: npm test
      - run: npm publish
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

## Common Issues and Solutions

### Permission Errors

#### Problem
```
EPERM: operation not permitted
```

#### Solutions
- Don't use sudo with npm
- Fix npm permissions
- Use nvm (Node Version Manager)

### Dependency Conflicts

#### Problem
```
EERROR: unable to resolve dependency tree
```

#### Solutions
```bash
# Use legacy peer deps
npm install --legacy-peer-deps

# Force install
npm install --force

# Update conflicting packages
npm update
```

### Cache Issues

#### Clear Cache
```bash
npm cache clean --force
```

#### Verify Cache
```bash
npm cache verify
```

## References

- NPM Official Documentation: https://docs.npmjs.com/
- "Best Practices for Your Organization's NPM Packages" (Inedo)
- "Guide to Managing NPM Packages in package.json" (Medium)
- "NPM Best Practices" (RisingStack)
- Semantic Versioning Specification: https://semver.org/
