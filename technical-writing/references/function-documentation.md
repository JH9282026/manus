### Function Documentation
Document functions with docstrings:

```python
def process_payment(amount: float, currency: str, customer_id: str) -> dict:
    """
    Process a payment transaction.
    
    Args:
        amount: The payment amount in decimal format.
        currency: Three-letter ISO currency code (e.g., "USD").
        customer_id: The unique customer identifier.
    
    Returns:
        A dictionary containing transaction_id and status.
    
    Raises:
        PaymentError: If the payment cannot be processed.
        InvalidCurrencyError: If the currency code is not supported.
    
    Example:
        >>> process_payment(99.99, "USD", "cust_123")
        {'transaction_id': 'txn_456', 'status': 'completed'}
    """
```
