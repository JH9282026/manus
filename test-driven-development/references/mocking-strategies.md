# Mocking Strategies

Techniques for isolating units under test.

## When to Use Mocks

- External API calls
- Database operations
- File system access
- Time-dependent code
- Complex dependencies

## Types of Test Doubles

### Mocks
Verify behavior (method calls, arguments).

### Stubs
Provide predetermined responses.

### Fakes
Working implementations (e.g., in-memory database).

### Spies
Real objects that record interactions.

## Python Example (unittest.mock)

```python
from unittest.mock import Mock, patch

def test_api_call():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'data': 'test'}
        result = fetch_data()
        assert result == {'data': 'test'}
        mock_get.assert_called_once()
```