---
name: "code-review-quality-analysis"
description: "Perform comprehensive automated code review and quality analysis. Use for: security vulnerability detection, performance optimization, code style enforcement, technical debt assessment, pull request reviews, code audits, and actionable improvement recommendations."
---

# Code Review & Quality Analysis

Conduct comprehensive code evaluation across security, performance, maintainability, and style.

## Overview

This skill provides systematic code analysis covering security vulnerabilities, performance bottlenecks, maintainability metrics, and coding standards. Augment human code review with consistent, thorough analysis that catches issues before production.

## Analysis Type Selection

| Context | Primary Focus | Key Checks | Reference |
|---------|---------------|------------|----------|
| Pull request | Security, standards | OWASP, style | `/references/security-analysis.md` |
| Pre-release | Performance, reliability | Load, error handling | `/references/performance-analysis.md` |
| Tech debt audit | Maintainability | Complexity, duplication | `/references/maintainability.md` |
| Due diligence | Comprehensive | All dimensions | `/references/audit-methodology.md` |
| Compliance | Security, licensing | Vulnerabilities, licenses | `/references/security-analysis.md` |

## Core Competencies

### Security Analysis
- Detect injection vulnerabilities (SQL, XSS, SSRF)
- Identify authentication and authorization flaws
- Find data exposure risks
- Check cryptographic implementations
- Scan dependencies for known vulnerabilities

### Performance Analysis
- Identify algorithmic inefficiencies
- Detect memory leaks and resource issues
- Find N+1 query patterns
- Assess caching opportunities
- Evaluate I/O and concurrency patterns

### Maintainability Analysis
- Calculate complexity metrics (cyclomatic, cognitive)
- Detect code duplication
- Assess coupling and cohesion
- Identify code smells and anti-patterns
- Evaluate documentation coverage

### Style and Standards
- Enforce coding conventions
- Check naming patterns
- Validate formatting
- Assess documentation completeness
- Verify test coverage

## Key Deliverables

### Review Reports
- Code Review Report (executive summary + details)
- Security Findings (CWE/OWASP classified)
- Performance Issues (with impact estimates)
- Maintainability Assessment

### Detailed Outputs
- Line-by-line findings with code snippets
- Severity ratings with justification
- Remediation recommendations with examples
- Effort estimates for fixes

### Metrics
- Complexity scores by module
- Test coverage statistics
- Dependency health scores
- Technical debt quantification

## Severity Classification

| Severity | Description | Action |
|----------|-------------|--------|
| Critical | Security breach, data loss | Block deployment |
| High | Significant risk or defect | Fix before release |
| Medium | Quality concern | Fix in sprint |
| Low | Minor improvement | Backlog |
| Info | Best practice suggestion | Consider |

## Language Support

| Language | Static Analysis | Security | Style |
|----------|-----------------|----------|-------|
| Python | Pylint, mypy | Bandit | Black, PEP8 |
| JavaScript/TS | ESLint | SonarJS, npm audit | Prettier |
| Java | PMD, SpotBugs | FindSecBugs | Checkstyle |
| Go | golangci-lint | gosec | gofmt |
| C/C++ | cppcheck | Clang-Tidy | clang-format |

## Using the Reference Files

### When to Read Each Reference

**`/references/security-analysis.md`** — Read when conducting security reviews, checking for vulnerabilities, or preparing for security audits.

**`/references/performance-analysis.md`** — Read when optimizing code performance, identifying bottlenecks, or reviewing algorithmic efficiency.

**`/references/maintainability.md`** — Read when assessing code quality, measuring technical debt, or planning refactoring efforts.

**`/references/audit-methodology.md`** — Read when conducting comprehensive code audits, M&A due diligence, or establishing review processes.
