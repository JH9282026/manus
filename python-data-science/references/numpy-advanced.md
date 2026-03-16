# NumPy Advanced Techniques

Comprehensive guide to advanced NumPy operations for numerical computing.

---

## Array Indexing and Slicing

### Basic Indexing

```python
import numpy as np

# 1D arrays
arr = np.array([0, 1, 2, 3, 4, 5])
arr[0]  # First element
arr[-1]  # Last element
arr[1:4]  # Elements 1, 2, 3
arr[::2]  # Every other element
arr[::-1]  # Reverse array

# 2D arrays
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_2d[0, 0]  # Element at row 0, column 0
arr_2d[0]  # First row
arr_2d[:, 0]  # First column
arr_2d[0:2, 1:3]  # Subarray
```

### Boolean Indexing

```python
# Create boolean mask
mask = arr > 3
print(mask)  # [False, False, False, False, True, True]

# Use mask to filter
filtered = arr[mask]  # [4, 5]

# Combined conditions
arr[(arr > 2) & (arr < 5)]  # [3, 4]
arr[(arr < 2) | (arr > 4)]  # [0, 1, 5]

# Modify values with boolean indexing
arr[arr > 3] = 0
```

### Fancy Indexing

```python
# Index with arrays
arr = np.array([10, 20, 30, 40, 50])
indices = np.array([0, 2, 4])
arr[indices]  # [10, 30, 50]

# 2D fancy indexing
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
row_indices = np.array([0, 1, 2])
col_indices = np.array([1, 0, 1])
arr_2d[row_indices, col_indices]  # [2, 3, 6]
```

---

## Broadcasting Rules

### Broadcasting Basics

Broadcasting allows operations on arrays of different shapes:

1. If arrays have different dimensions, prepend 1s to the smaller shape
2. Arrays are compatible if dimensions are equal or one of them is 1
3. After broadcasting, each array behaves as if it had the larger shape

```python
# Scalar broadcasting
arr = np.array([1, 2, 3])
arr + 10  # [11, 12, 13]

# 1D to 2D broadcasting
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])
arr_2d + vector  # Adds vector to each row
# [[11, 22, 33],
#  [14, 25, 36]]

# Column vector broadcasting
col_vector = np.array([[10], [20]])
arr_2d + col_vector  # Adds column to each column
# [[11, 12, 13],
#  [24, 25, 26]]
```

### Advanced Broadcasting

```python
# 3D broadcasting
arr_3d = np.random.rand(3, 4, 5)
vector = np.random.rand(5)
result = arr_3d + vector  # Broadcasts across first two dimensions

# Outer product using broadcasting
a = np.array([1, 2, 3])
b = np.array([10, 20, 30, 40])
outer = a[:, np.newaxis] * b
# [[ 10  20  30  40]
#  [ 20  40  60  80]
#  [ 30  60  90 120]]

# Distance matrix
points = np.random.rand(100, 2)
dist_matrix = np.sqrt(((points[:, np.newaxis] - points) ** 2).sum(axis=2))
```

---

## Linear Algebra

### Matrix Operations

```python
# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Element-wise multiplication
A * B

# Matrix multiplication
A @ B  # Python 3.5+
np.dot(A, B)  # Alternative
np.matmul(A, B)  # Alternative

# Transpose
A.T
np.transpose(A)

# Inverse
np.linalg.inv(A)

# Determinant
np.linalg.det(A)

# Trace
np.trace(A)
```

### Solving Linear Systems

```python
# Solve Ax = b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
print(x)  # [2. 3.]

# Least squares solution
A = np.array([[1, 1], [1, 2], [1, 3]])
b = np.array([1, 2, 2])
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
```

### Eigenvalues and Eigenvectors

```python
# Eigendecomposition
A = np.array([[1, 2], [2, 1]])
eigenvalues, eigenvectors = np.linalg.eig(A)

# Singular Value Decomposition (SVD)
U, s, Vt = np.linalg.svd(A)

# Reconstruct matrix
A_reconstructed = U @ np.diag(s) @ Vt
```

---

## Random Number Generation

### Random Sampling

```python
# Set seed for reproducibility
np.random.seed(42)

# Uniform distribution [0, 1)
np.random.rand(3, 3)

# Uniform distribution [low, high)
np.random.uniform(0, 10, size=(3, 3))

# Standard normal distribution
np.random.randn(3, 3)

# Normal distribution with mean and std
np.random.normal(loc=0, scale=1, size=(3, 3))

# Random integers
np.random.randint(0, 10, size=(3, 3))

# Random choice from array
arr = np.array([1, 2, 3, 4, 5])
np.random.choice(arr, size=3, replace=False)

# Shuffle array in-place
np.random.shuffle(arr)

# Permutation (returns shuffled copy)
np.random.permutation(arr)
```

### Statistical Distributions

```python
# Binomial
np.random.binomial(n=10, p=0.5, size=1000)

# Poisson
np.random.poisson(lam=3, size=1000)

# Exponential
np.random.exponential(scale=2, size=1000)

# Beta
np.random.beta(a=2, b=5, size=1000)

# Gamma
np.random.gamma(shape=2, scale=2, size=1000)
```

---

## Universal Functions (ufuncs)

### Mathematical Functions

```python
# Trigonometric
np.sin(arr)
np.cos(arr)
np.tan(arr)
np.arcsin(arr)
np.arccos(arr)
np.arctan(arr)

# Exponential and logarithmic
np.exp(arr)
np.log(arr)  # Natural log
np.log10(arr)  # Base 10
np.log2(arr)  # Base 2

# Power and roots
np.power(arr, 3)
np.sqrt(arr)
np.cbrt(arr)  # Cube root

# Rounding
np.round(arr, decimals=2)
np.floor(arr)
np.ceil(arr)
np.trunc(arr)
```

### Comparison and Logic

```python
# Element-wise comparison
np.greater(arr1, arr2)
np.less(arr1, arr2)
np.equal(arr1, arr2)
np.not_equal(arr1, arr2)

# Logical operations
np.logical_and(arr1 > 0, arr2 > 0)
np.logical_or(arr1 > 0, arr2 > 0)
np.logical_not(arr > 0)

# Any and all
np.any(arr > 0)
np.all(arr > 0)
```

---

## Array Manipulation

### Reshaping

```python
# Reshape
arr = np.arange(12)
arr.reshape(3, 4)
arr.reshape(2, 2, 3)

# Flatten
arr_2d = np.array([[1, 2], [3, 4]])
arr_2d.flatten()  # Returns copy
arr_2d.ravel()  # Returns view if possible

# Transpose
arr_2d.T
np.transpose(arr_2d)

# Swap axes
arr_3d = np.random.rand(2, 3, 4)
np.swapaxes(arr_3d, 0, 2)  # Swap first and third axes
```

### Stacking and Splitting

```python
# Vertical stack (row-wise)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
np.vstack([arr1, arr2])
# [[1, 2, 3],
#  [4, 5, 6]]

# Horizontal stack (column-wise)
np.hstack([arr1, arr2])
# [1, 2, 3, 4, 5, 6]

# Depth stack
np.dstack([arr1, arr2])

# Concatenate along axis
np.concatenate([arr1, arr2], axis=0)

# Split array
arr = np.arange(9)
np.split(arr, 3)  # Split into 3 equal parts
np.array_split(arr, 4)  # Split into 4 parts (allows unequal)
```

### Repeating and Tiling

```python
# Repeat elements
arr = np.array([1, 2, 3])
np.repeat(arr, 3)  # [1, 1, 1, 2, 2, 2, 3, 3, 3]

# Tile array
np.tile(arr, 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
np.tile(arr, (2, 3))  # 2D tiling
```

---

## Performance Optimization

### Vectorization

```python
# Bad: Python loop
result = []
for x in arr:
    result.append(x ** 2)

# Good: Vectorized
result = arr ** 2

# Bad: Iterating over rows
result = []
for row in arr_2d:
    result.append(row.sum())

# Good: Vectorized aggregation
result = arr_2d.sum(axis=1)
```

### Memory Views

```python
# Slicing creates views (no copy)
arr = np.arange(10)
view = arr[2:5]
view[0] = 999  # Modifies original array

# Force copy
copy = arr[2:5].copy()
copy[0] = 999  # Does not modify original

# Check if array owns data
arr.flags['OWNDATA']  # True
view.flags['OWNDATA']  # False
```

### Efficient Aggregations

```python
# Use built-in aggregations
arr.sum()  # Faster than np.sum(arr)
arr.mean()
arr.std()
arr.var()

# Aggregations along axes
arr_2d.sum(axis=0)  # Sum columns
arr_2d.mean(axis=1)  # Mean of rows

# Cumulative operations
np.cumsum(arr)
np.cumprod(arr)
```

---

## Structured Arrays

### Creating Structured Arrays

```python
# Define dtype
dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])

# Create structured array
data = np.array([('Alice', 25, 55.0), ('Bob', 30, 70.5)], dtype=dt)

# Access fields
data['name']
data['age']

# Access individual records
data[0]
data[0]['name']
```

### Record Arrays

```python
# Record arrays allow attribute access
data_rec = data.view(np.recarray)
data_rec.name
data_rec.age
```