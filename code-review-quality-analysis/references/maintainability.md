# Code Maintainability

Assess and improve code maintainability through metrics, patterns, and refactoring.

---

## Maintainability Index

### Calculation Components

The maintainability index combines:
- **Halstead volume** — Measures code complexity based on operators and operands
- **Cyclomatic complexity** — Number of independent execution paths
- **Lines of code** — Physical size of the codebase
- **Comment ratio** — Proportion of documentation

### Interpretation Scale

| Score | Rating | Action |
|---|---|---|
| 85-100 | Excellent | Maintain current practices |
| 65-84 | Good | Minor improvements possible |
| 40-64 | Moderate | Targeted refactoring needed |
| 20-39 | Poor | Significant refactoring required |
| 0-19 | Critical | Major rewrite consideration |

---

## SOLID Principles Compliance

| Principle | Check | Violation Indicator |
|---|---|---|
| **S**ingle Responsibility | Does the class/module have one reason to change? | Class doing multiple unrelated things |
| **O**pen/Closed | Can behavior be extended without modifying existing code? | Frequent modifications to existing classes |
| **L**iskov Substitution | Can subtypes replace base types without breaking? | Type-checking in client code |
| **I**nterface Segregation | Are interfaces focused and minimal? | Clients forced to implement unused methods |
| **D**ependency Inversion | Do modules depend on abstractions? | Direct instantiation of concrete dependencies |

---

## Technical Debt Assessment

### Debt Classification

| Type | Description | Interest Rate | Example |
|---|---|---|---|
| Architecture debt | Structural issues limiting scalability | High — compounds rapidly | Monolith needing decomposition |
| Design debt | Poor patterns causing ripple changes | Medium-High | God objects, circular dependencies |
| Code debt | Quality issues increasing bug risk | Medium | Duplicated code, complex functions |
| Test debt | Insufficient coverage, brittle tests | Medium | Missing tests for critical paths |
| Documentation debt | Missing or outdated docs | Low | Undocumented APIs, stale README |
| Infrastructure debt | Outdated tools, manual processes | Medium | No CI/CD, manual deployments |

### Debt Prioritization Matrix

Prioritize remediation by: **Impact × Frequency of Change**
- High impact + frequently changed → Fix immediately
- High impact + rarely changed → Schedule for next quarter
- Low impact + frequently changed → Include in next refactoring sprint
- Low impact + rarely changed → Track but deprioritize

---

## Refactoring Patterns

### Safe Refactoring Steps

1. Ensure comprehensive test coverage before refactoring
2. Make one change at a time, verify tests pass
3. Use automated refactoring tools where available
4. Review each refactoring with the team
5. Document the rationale for significant changes

### Common Refactoring Catalog

| Refactoring | When to Apply | Risk |
|---|---|---|
| Extract Method | Long functions, duplicated logic | Low |
| Extract Class | Class with too many responsibilities | Medium |
| Move Method | Feature envy — method uses another class's data | Low |
| Replace Conditional with Polymorphism | Complex switch/if chains | Medium |
| Introduce Parameter Object | Long parameter lists | Low |
| Replace Magic Number with Constant | Hardcoded values | Low |
| Encapsulate Collection | Exposed internal collections | Low |
