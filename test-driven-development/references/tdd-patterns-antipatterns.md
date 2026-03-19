# TDD Patterns and Anti-Patterns

## Patterns (Good Practices)

### 1. Test List
Maintain list of tests to write.

### 2. Fake It Till You Make It
Return hard-coded values initially, generalize later.

### 3. Triangulation
Add multiple test cases to drive generalization.

### 4. Obvious Implementation
If implementation is obvious, write it directly.

## Anti-Patterns (Avoid)

### 1. Testing Implementation Details
Test behavior, not internal structure.

### 2. Fragile Tests
Tests break with minor refactoring.

### 3. Slow Tests
Tests take too long to run.

### 4. Test Interdependence
Tests depend on execution order.

### 5. Excessive Mocking
Mocking everything reduces test value.