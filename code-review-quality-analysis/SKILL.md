---
name: "code-review-quality-analysis"
description: "Perform comprehensive automated code review and quality analysis across multiple dimensions. Use for: security vulnerability detection (OWASP, CWE), performance optimization, code style enforcement, technical debt assessment, pull request reviews, architecture evaluation, test coverage analysis, and actionable improvement recommendations."
---

# Code Review & Quality Analysis

Perform systematic, multi-dimensional code analysis covering security, performance, maintainability, and standards compliance.

## Overview

Evaluate source code across security, performance, maintainability, and style dimensions. Detect vulnerabilities (OWASP Top 10, CWE), identify performance bottlenecks, measure complexity metrics, enforce coding standards, assess test coverage, and generate prioritized, actionable improvement recommendations.

## Analysis Scope Selection

| Review Type | Depth | Time | Best For |
|---|---|---|---|
| Quick scan | Surface-level issues, linting | Minutes | Pre-commit checks, small changes |
| Standard review | Security + style + basic performance | 30-60 min | Pull request reviews |
| Deep analysis | All dimensions + architecture | 2-4 hours | Release readiness, audits |
| Focused audit | Single dimension deep-dive | 1-2 hours | Security audit, performance tuning |

## Security Analysis Framework

### OWASP Top 10 Checklist

| Vulnerability | Detection Pattern | Severity |
|---|---|---|
| A01: Broken Access Control | Missing auth checks, IDOR, path traversal | Critical |
| A02: Cryptographic Failures | Weak algorithms, hardcoded secrets, plaintext storage | Critical |
| A03: Injection | Unsanitized input in SQL, OS, LDAP commands | Critical |
| A04: Insecure Design | Missing threat modeling, unsafe business logic | High |
| A05: Security Misconfiguration | Default credentials, verbose errors, open ports | High |
| A06: Vulnerable Components | Outdated dependencies with known CVEs | High |
| A07: Auth Failures | Weak passwords, missing MFA, session issues | High |
| A08: Data Integrity Failures | Insecure deserialization, unsigned updates | Medium |
| A09: Logging Failures | Missing audit logs, log injection, PII in logs | Medium |
| A10: SSRF | Unvalidated URL fetching, internal network access | High |

## Code Quality Metrics

### Complexity Metrics

| Metric | Tool | Threshold | Action |
|---|---|---|---|
| Cyclomatic complexity | ESLint, pylint, SonarQube | ≤10 per function | Refactor above threshold |
| Cognitive complexity | SonarQube | ≤15 per function | Simplify logic flow |
| Lines per function | Linter | ≤50 lines | Extract helper functions |
| Lines per file | Linter | ≤300 lines | Split into modules |
| Nesting depth | Linter | ≤4 levels | Use early returns, extract |
| Duplication | SonarQube, jscpd | <5% codebase | Extract shared code |

### Code Smell Categories

| Category | Examples | Refactoring Approach |
|---|---|---|
| Bloaters | Long methods, large classes, long parameter lists | Extract method/class, parameter objects |
| OOP abusers | Switch statements, refused bequest, parallel inheritance | Polymorphism, composition |
| Change preventers | Divergent change, shotgun surgery | Single responsibility, encapsulation |
| Dispensables | Dead code, speculative generality, comments as deodorant | Delete unused code, clarify intent |
| Couplers | Feature envy, inappropriate intimacy, message chains | Move method, delegate, encapsulate |

## Review Output Format

Structure every code review report as:

1. **Executive summary** — Overall health score (A-F), critical issues count, risk assessment
2. **Critical findings** — Security vulnerabilities, data loss risks, breaking changes
3. **Major findings** — Performance issues, significant maintainability problems
4. **Minor findings** — Style violations, naming improvements, documentation gaps
5. **Positive observations** — Well-written patterns worth highlighting
6. **Recommendations** — Prioritized action items with effort estimates

## Test Coverage Assessment

| Coverage Type | Minimum Target | Ideal Target |
|---|---|---|
| Line coverage | 70% | 85%+ |
| Branch coverage | 60% | 75%+ |
| Function coverage | 80% | 90%+ |
| Integration test coverage | Key paths covered | All API endpoints |
| E2E test coverage | Critical user flows | Happy + error paths |

## Using the Reference Files

**`/references/security-analysis.md`** — Read when performing security-focused reviews, checking OWASP compliance, or auditing authentication and authorization patterns.

**`/references/performance-analysis.md`** — Read when analyzing runtime performance, identifying bottlenecks, or optimizing algorithms and queries.

**`/references/maintainability.md`** — Read when assessing code quality metrics, evaluating architecture, or planning technical debt remediation.

**`/references/audit-methodology.md`** — Read when conducting formal code audits, establishing review processes, or building review checklists for teams.

## Reference Files

This skill includes the following detailed reference materials:

- [Audit Methodology](./references/audit-methodology.md)
- [Maintainability](./references/maintainability.md)
- [Performance Analysis](./references/performance-analysis.md)
- [Security Analysis](./references/security-analysis.md)
