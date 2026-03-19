# TDD Cycle Deep Dive

Detailed exploration of the red-green-refactor cycle.

## Red Phase

Write a failing test that defines desired behavior.

**Steps:**
1. Identify next small feature
2. Write test that exercises feature
3. Run test (should fail)
4. Verify failure message is clear

**Example (Python):**
```python
def test_calculate_total_with_tax():
    calculator = PriceCalculator()
    total = calculator.calculate_total(100, tax_rate=0.1)
    assert total == 110.0
```

## Green Phase

Write minimum code to pass the test.

**Implementation:**
```python
class PriceCalculator:
    def calculate_total(self, amount, tax_rate):
        return amount + (amount * tax_rate)
```

## Refactor Phase

Improve code quality while keeping tests green.

**Refactoring:**
```python
class PriceCalculator:
    def calculate_total(self, amount: float, tax_rate: float) -> float:
        """Calculate total price including tax."""
        tax_amount = self._calculate_tax(amount, tax_rate)
        return amount + tax_amount
    
    def _calculate_tax(self, amount: float, rate: float) -> float:
        return amount * rate
```