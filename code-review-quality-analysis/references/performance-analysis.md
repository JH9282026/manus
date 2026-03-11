# Performance Analysis

## Algorithmic Analysis

### Big O Assessment

| Complexity | Example | Concern Level |
|------------|---------|---------------|
| O(1) | Hash lookup | None |
| O(log n) | Binary search | None |
| O(n) | Linear scan | Monitor |
| O(n log n) | Good sort | Monitor |
| O(n²) | Nested loops | Review |
| O(2ⁿ) | Exponential | Critical |

### Common Issues
- Nested loops over large datasets
- Repeated expensive computations
- Inefficient data structures
- Missing indexing in lookups
- Redundant iterations

---

## Database Performance

### N+1 Query Detection
```python
# N+1 Problem (1 + N queries)
for order in orders:
    customer = order.customer  # Query per order

# Solution (2 queries)
orders = Order.select().prefetch(Customer)
```

### Query Optimization
- Missing indexes
- SELECT * usage
- Unbounded queries
- Join optimization
- Query caching opportunities

---

## Memory Analysis

### Memory Leak Patterns
- Unreleased resources
- Growing collections
- Circular references
- Event listener accumulation
- Cache without eviction

### Memory Optimization
- Object pooling
- Lazy loading
- Streaming large data
- Proper resource cleanup
- Memory-efficient data structures

---

## Concurrency Issues

### Race Conditions
- Shared mutable state
- Missing synchronization
- Non-atomic operations
- Time-of-check to time-of-use (TOCTOU)

### Deadlock Patterns
- Circular lock dependencies
- Inconsistent lock ordering
- Nested locks
- Resource starvation

---

## I/O Optimization

### File Operations
- Buffered I/O
- Batch processing
- Async file operations
- Memory-mapped files

### Network Operations
- Connection pooling
- Request batching
- Async/await patterns
- Timeout configuration
- Retry with backoff

---

## Caching Opportunities

### Cache Candidates
- Expensive computations
- Repeated database queries
- External API responses
- Configuration data
- Session data

### Caching Strategies

| Strategy | Use Case |
|----------|----------|
| Cache-aside | General purpose |
| Read-through | Transparent caching |
| Write-through | Data consistency |
| Write-behind | Write performance |
