# Maintainability Analysis

## Complexity Metrics

### Cyclomatic Complexity
Measures independent paths through code.

| Score | Risk | Action |
|-------|------|--------|
| 1-10 | Low | Acceptable |
| 11-20 | Moderate | Review |
| 21-50 | High | Refactor |
| 50+ | Very High | Priority refactor |

### Cognitive Complexity
Measures how difficult code is to understand.

Factors:
- Nesting depth
- Control flow breaks
- Boolean complexity
- Recursive calls

---

## Code Duplication

### Detection Methods
- Exact clone detection
- Parameterized clone detection
- Semantic similarity analysis

### Duplication Thresholds

| Duplication | Assessment |
|-------------|------------|
| <3% | Good |
| 3-5% | Acceptable |
| 5-10% | Concern |
| >10% | Action required |

---

## Code Smells

### Common Code Smells

| Smell | Description | Refactoring |
|-------|-------------|-------------|
| Long Method | >20 lines | Extract Method |
| Long Parameter List | >4 params | Introduce Object |
| Large Class | >500 lines | Extract Class |
| Feature Envy | Uses other class data | Move Method |
| Data Clumps | Repeated data groups | Extract Class |
| Primitive Obsession | Primitives over objects | Introduce Domain Object |
| Switch Statements | Complex conditionals | Replace with Polymorphism |
| Parallel Inheritance | Paired class hierarchies | Merge Hierarchies |

---

## Design Principles

### SOLID Violations

| Principle | Violation Sign | Check |
|-----------|----------------|-------|
| Single Responsibility | Class does many things | One reason to change |
| Open/Closed | Modifying for extension | Extend, don't modify |
| Liskov Substitution | Subtype breaks parent contract | Substitutability |
| Interface Segregation | Fat interfaces | Focused interfaces |
| Dependency Inversion | High-level depends on low-level | Depend on abstractions |

---

## Documentation Quality

### Documentation Checklist
- [ ] Module/class docstrings
- [ ] Public method documentation
- [ ] Complex logic comments
- [ ] API documentation
- [ ] README completeness
- [ ] Architecture decision records

### Comment Quality
- Explain why, not what
- Keep comments current
- Remove dead/misleading comments
- Use self-documenting code

---

## Test Quality

### Coverage Targets

| Coverage Type | Target |
|---------------|--------|
| Statement | 80%+ |
| Branch | 70%+ |
| Function | 90%+ |
| Critical paths | 100% |

### Test Quality Indicators
- Meaningful assertions
- Test isolation
- Edge case coverage
- Readable test names
- Appropriate mocking
