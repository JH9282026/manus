# CI/CD TDD Integration

Integrating TDD into continuous integration pipelines.

## GitHub Actions Example

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - run: pip install -r requirements.txt
    - run: pytest --cov=src tests/
    - run: coverage report --fail-under=80
```

## Quality Gates

1. **All tests must pass**
2. **Code coverage ≥ 80%**
3. **No critical security vulnerabilities**
4. **Code style compliance**

## Best Practices

- Run tests on every commit
- Fast feedback (<5 min)
- Parallel test execution
- Clear failure reporting
- Block merges on test failures