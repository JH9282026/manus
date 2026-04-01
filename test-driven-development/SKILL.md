---
name: test-driven-development
description: "Implement test-driven development (TDD) methodology using red-green-refactor cycles. Use for: writing tests before code, improving code quality and design, reducing bugs, enabling confident refactoring, creating living documentation, integrating with CI/CD pipelines, and adopting Agile development practices."
---

# Test-Driven Development

Write automated tests before code using the red-green-refactor cycle for higher quality, better design, and faster bug detection.

## Overview

Test-Driven Development (TDD) is a software development methodology where tests are written before the production code. This iterative "test-first" approach, formalized by Kent Beck in the late 1990s as part of Extreme Programming, leads to cleaner code, better architecture, and faster bug detection. With 61% of QA teams adopting AI-driven testing and TDD providing the framework for validating AI-generated code, TDD remains essential for modern development.

## The Red-Green-Refactor Cycle

TDD operates on a three-step iterative cycle:

| Phase | Action | Purpose | Duration |
|-------|--------|---------|----------|
| **Red** | Write a failing test | Define expected behavior, create clear target | 2-5 min |
| **Green** | Write minimum code to pass | Achieve working functionality quickly | 5-15 min |
| **Refactor** | Improve code quality | Enhance readability, maintainability, efficiency | 5-10 min |

### Phase Details

**Red Phase:**
- Write test for small, specific functionality
- Test must fail (proving feature doesn't exist yet)
- Clarifies requirements and acceptance criteria
- Creates executable specification

**Green Phase:**
- Write simplest code to make test pass
- Don't focus on elegance initially
- Goal: green test as fast as possible
- Validates understanding of requirements

**Refactor Phase:**
- Improve code structure and quality
- Remove duplication
- Enhance readability
- All tests must continue passing
- Safety net against regressions

## TDD Approaches

### Inside-Out (Bottom-Up)

Start with smallest components, build outward.

**Best for:**
- APIs and libraries
- Complex algorithms
- Backend services
- Beginners learning TDD

**Process:**
1. Test individual functions/methods
2. Test classes
3. Test module interactions
4. Test system integration

### Outside-In (Top-Down)

Start from user perspective, work inward.

**Best for:**
- User interfaces
- Customer-facing features
- Full-stack applications
- Behavior-driven development

**Process:**
1. Write acceptance test (user story)
2. Identify required components
3. Test and implement each component
4. Integration emerges naturally

## When to Use TDD

### Ideal Scenarios

| Scenario | Why TDD Helps |
|----------|---------------|
| Complex business logic | Continuous validation of intricate rules |
| Long-term projects | Maintainability and evolution over time |
| Quality-critical systems | Reliability and security paramount |
| Team learning | Improves design skills and collaboration |
| Legacy system updates | Safety net against breaking changes |
| Regulatory compliance | Documentation and traceability |

### When to Skip TDD

- **Prototypes** — Requirements uncertain, rapid changes expected
- **Simple CRUD** — Straightforward operations, low complexity
- **Tight deadlines** — Upfront investment may seem slow (though saves time long-term)
- **Exploratory coding** — Learning new technology or approach
- **Throwaway code** — One-time scripts or temporary solutions

## Key Benefits

### 1. Enhanced Code Quality
- Modular, loosely coupled design
- Testable code from the start
- Cleaner interfaces
- Reduced technical debt

### 2. Faster Bug Detection
- Bugs caught within minutes
- Immediate feedback loop
- Pinpoint exact location of issues
- Reduced debugging time by 40-60%

### 3. Better Architecture
- Forces consideration of code usage
- Encourages SOLID principles
- Simpler, more maintainable designs
- Clear separation of concerns

### 4. Increased Confidence
- Comprehensive test suite as safety net
- Refactor without fear
- Deploy with confidence
- Reduced regression bugs by 70%+

### 5. Living Documentation
- Tests illustrate expected behavior
- Always up-to-date
- Onboarding tool for new team members
- Executable specifications

### 6. CI/CD Enablement
- Automated test suite crucial for pipelines
- Frequent deployments with confidence
- Fast feedback on code changes
- Quality gates enforcement

## Best Practices

### Test Design

1. **One Behavior Per Test**
   - Single, focused assertion
   - Clear test purpose
   - Easy to understand failures

2. **Clear, Descriptive Names**
   - Describe what is being tested
   - Include expected outcome
   - Example: `test_login_with_invalid_credentials_returns_error`

3. **AAA Pattern**
   - **Arrange:** Set up test data and conditions
   - **Act:** Execute the code being tested
   - **Assert:** Verify expected outcome

4. **Independent Tests**
   - No shared state between tests
   - Run in any order
   - Isolated test data

5. **Fast Execution**
   - Keep tests lightweight
   - Avoid external dependencies in unit tests
   - Use mocks/fakes for speed
   - Target: <5 seconds for full unit test suite

### Code Practices

1. **Write Minimal Code**
   - Only enough to pass current test
   - Avoid over-engineering
   - Let tests drive design

2. **Refactor Regularly**
   - After each green phase
   - Treat test code like production code
   - Remove duplication
   - Improve naming

3. **Test Behavior, Not Implementation**
   - Focus on *what* code does
   - Not *how* it does it
   - Reduces brittle tests
   - Enables refactoring

4. **Use Test Doubles Appropriately**
   - Mocks for behavior verification
   - Stubs for state setup
   - Fakes for complex dependencies
   - Spies for interaction tracking

## Common Challenges and Solutions

### Challenge: Initial Learning Curve
**Solutions:**
- Start with simple functions
- Pair programming with experienced TDD practitioners
- Practice katas (coding exercises)
- Attend TDD workshops

### Challenge: Perceived Time Investment
**Reality:**
- Slower initially, faster overall
- Reduces debugging time by 40-60%
- Prevents costly bugs in production
- Enables faster feature development long-term

### Challenge: Test Maintenance
**Solutions:**
- Regular refactoring of test code
- Remove obsolete tests
- Keep tests simple and focused
- Use Page Object Model for UI tests

### Challenge: Complex Tests
**Solutions:**
- Break into smaller tests
- Use test helpers and fixtures
- Leverage test data builders
- Focus on one behavior per test

### Challenge: Slow Test Execution
**Solutions:**
- Parallel test execution
- Avoid external dependencies
- Use in-memory databases
- Implement smart test selection

## Tools and Frameworks

### Unit Testing Frameworks

| Language | Framework | Key Features |
|----------|-----------|--------------|
| Java | JUnit, TestNG | Annotations, parameterized tests, test suites |
| Python | pytest, unittest | Fixtures, parametrize, mocking |
| JavaScript | Jest, Mocha | Snapshot testing, async support, mocking |
| C# | NUnit, xUnit | Attributes, theories, parallel execution |
| Ruby | RSpec, Minitest | BDD syntax, shared examples |

### Mocking Libraries

- **Mockito** (Java) — Behavior verification, argument matchers
- **unittest.mock** (Python) — Built-in, flexible mocking
- **Sinon.js** (JavaScript) — Spies, stubs, mocks
- **Moq** (C#) — LINQ-based, fluent API

### CI/CD Integration

- **GitHub Actions** — Native GitHub integration
- **GitLab CI** — Built-in pipelines
- **Jenkins** — Flexible, extensible
- **CircleCI** — Fast, cloud-based

### Code Coverage Tools

- **JaCoCo** (Java) — Bytecode instrumentation
- **Coverage.py** (Python) — Statement and branch coverage
- **Istanbul/nyc** (JavaScript) — Comprehensive coverage reports
- **Coverlet** (C#) — Cross-platform coverage

## Metrics and Standards

| Metric | Target | Purpose |
|--------|--------|---------|
| Code Coverage | 80%+ | Ensure adequate test coverage |
| Test Execution Time | <5 min for unit tests | Fast feedback loop |
| Test-to-Code Ratio | 1:1 to 2:1 | Adequate test investment |
| Test Pass Rate | 100% on main branch | Maintain code quality |
| Defect Escape Rate | <5% | Measure test effectiveness |

## TDD with Modern Development

### Agile and Scrum
- Breaks user stories into testable tasks
- Supports sprint goals with quality
- Enables continuous delivery
- Facilitates team collaboration

### DevOps
- Automated testing in deployment pipeline
- Confidence for frequent releases
- Reduced rollback rates
- Faster mean time to recovery (MTTR)

### AI-Assisted Development
- Tests define expected behavior for AI
- Validate AI-generated code
- AI can accelerate test generation
- TDD provides framework for AI code validation

## Using the Reference Files

### When to Read Each Reference

**`/references/tdd-cycle-deep-dive.md`** — Read when implementing TDD for the first time, understanding the red-green-refactor cycle in detail, or training team members.

**`/references/testing-frameworks-guide.md`** — Read when selecting testing frameworks, setting up test infrastructure, or migrating between frameworks.

**`/references/mocking-strategies.md`** — Read when dealing with external dependencies, implementing test doubles, or isolating units for testing.

**`/references/tdd-patterns-antipatterns.md`** — Read when improving test quality, avoiding common pitfalls, or establishing team standards.

**`/references/ci-cd-tdd-integration.md`** — Read when integrating TDD into CI/CD pipelines, setting up automated testing, or establishing quality gates.

## References

- [Ci Cd Tdd Integration](references/ci-cd-tdd-integration.md)
- [Mocking Strategies](references/mocking-strategies.md)
- [Tdd Cycle Deep Dive](references/tdd-cycle-deep-dive.md)
- [Tdd Patterns Antipatterns](references/tdd-patterns-antipatterns.md)
- [Testing Frameworks Guide](references/testing-frameworks-guide.md)
