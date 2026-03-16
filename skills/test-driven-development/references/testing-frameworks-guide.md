# Testing Frameworks Guide

Comprehensive overview of popular testing frameworks.

## Python: pytest

**Installation:**
```bash
pip install pytest
```

**Basic Test:**
```python
def test_addition():
    assert 1 + 1 == 2
```

**Fixtures:**
```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}

def test_with_fixture(sample_data):
    assert sample_data["name"] == "John"
```

## JavaScript: Jest

**Installation:**
```bash
npm install --save-dev jest
```

**Basic Test:**
```javascript
test('adds 1 + 2 to equal 3', () => {
  expect(1 + 2).toBe(3);
});
```

**Mocking:**
```javascript
const mockFn = jest.fn();
mockFn.mockReturnValue(42);
expect(mockFn()).toBe(42);
```

## Java: JUnit 5

**Basic Test:**
```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    @Test
    void testAddition() {
        assertEquals(4, 2 + 2);
    }
}
```