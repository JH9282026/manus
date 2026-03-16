# Pandas Advanced Techniques

Comprehensive guide to advanced Pandas operations for data manipulation and analysis.

---

## Advanced Indexing

### MultiIndex (Hierarchical Indexing)

```python
import pandas as pd
import numpy as np

# Create MultiIndex DataFrame
arrays = [
    ['A', 'A', 'B', 'B'],
    ['one', 'two', 'one', 'two']
]
index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(4, 2), index=index, columns=['data1', 'data2'])

# Access levels
df.loc['A']
df.loc[('A', 'one')]
df.xs('one', level='second')

# Swap levels
df.swaplevel('first', 'second')

# Sort by index
df.sort_index(level='second')
```

### Advanced Selection

```python
# Query method
df.query('age > 30 and salary < 100000')

# isin method
df[df['category'].isin(['A', 'B', 'C'])]

# between method
df[df['value'].between(10, 20)]

# where method (replace values not meeting condition)
df.where(df > 0, -df)

# mask method (opposite of where)
df.mask(df < 0, 0)
```

---

## Time Series Advanced

### Date Ranges and Frequencies

```python
# Create date ranges
pd.date_range('2024-01-01', periods=100, freq='D')  # Daily
pd.date_range('2024-01-01', periods=24, freq='H')  # Hourly
pd.date_range('2024-01-01', periods=12, freq='M')  # Monthly
pd.date_range('2024-01-01', periods=4, freq='Q')  # Quarterly

# Business days
pd.bdate_range('2024-01-01', periods=100)

# Custom frequencies
pd.date_range('2024-01-01', periods=10, freq='2H')  # Every 2 hours
pd.date_range('2024-01-01', periods=10, freq='W-MON')  # Weekly on Monday
```

### Resampling and Rolling

```python
# Downsampling
df.resample('M').sum()  # Monthly sum
df.resample('W').mean()  # Weekly mean
df.resample('Q').agg({'sales': 'sum', 'profit': 'mean'})

# Upsampling
df.resample('D').ffill()  # Forward fill
df.resample('H').interpolate()  # Interpolate

# Rolling windows
df['sales'].rolling(window=7).mean()  # 7-period moving average
df['sales'].rolling(window=7).std()  # 7-period rolling std
df['sales'].rolling(window=7).apply(lambda x: x.max() - x.min())

# Expanding windows
df['sales'].expanding().mean()  # Cumulative mean
df['sales'].expanding().sum()  # Cumulative sum

# Exponentially weighted windows
df['sales'].ewm(span=7).mean()  # EW moving average
```

### Time Zone Handling

```python
# Localize to timezone
df.tz_localize('US/Eastern')

# Convert timezone
df.tz_convert('Europe/London')

# Remove timezone
df.tz_localize(None)
```

---

## GroupBy Advanced

### Multiple Aggregations

```python
# Different aggregations per column
df.groupby('category').agg({
    'sales': ['sum', 'mean', 'count'],
    'profit': ['sum', 'mean'],
    'quantity': 'sum'
})

# Named aggregations
df.groupby('category').agg(
    total_sales=('sales', 'sum'),
    avg_sales=('sales', 'mean'),
    total_profit=('profit', 'sum')
)

# Custom aggregation functions
def range_func(x):
    return x.max() - x.min()

df.groupby('category')['sales'].agg(['mean', 'std', range_func])
```

### Transform and Filter

```python
# Transform (returns same shape as input)
df['sales_normalized'] = df.groupby('category')['sales'].transform(lambda x: (x - x.mean()) / x.std())

# Filter groups
df.groupby('category').filter(lambda x: x['sales'].sum() > 1000)

# Apply (most flexible)
df.groupby('category').apply(lambda x: x.nlargest(3, 'sales'))
```

### Grouping by Multiple Columns

```python
# Multiple grouping columns
df.groupby(['region', 'category'])['sales'].sum()

# Grouping by time periods
df.groupby(pd.Grouper(key='date', freq='M'))['sales'].sum()

# Grouping by bins
df.groupby(pd.cut(df['age'], bins=[0, 18, 35, 50, 100]))['income'].mean()
```

---

## Merging and Joining Advanced

### Complex Merges

```python
# Merge with indicator
pd.merge(df1, df2, on='key', how='outer', indicator=True)

# Merge on index
pd.merge(df1, df2, left_index=True, right_index=True)

# Merge with different column names
pd.merge(df1, df2, left_on='key1', right_on='key2')

# Merge with suffixes
pd.merge(df1, df2, on='key', suffixes=('_left', '_right'))

# Validate merge
pd.merge(df1, df2, on='key', validate='one_to_one')  # Raises error if not 1:1
```

### Concatenation Options

```python
# Concatenate with keys
pd.concat([df1, df2], keys=['first', 'second'])

# Ignore index
pd.concat([df1, df2], ignore_index=True)

# Only keep common columns
pd.concat([df1, df2], join='inner')

# Verify integrity
pd.concat([df1, df2], verify_integrity=True)  # Raises error on duplicate indices
```

---

## Performance Optimization

### Efficient Data Types

```python
# Convert to category for low-cardinality strings
df['category'] = df['category'].astype('category')

# Downcast numeric types
df['int_col'] = pd.to_numeric(df['int_col'], downcast='integer')
df['float_col'] = pd.to_numeric(df['float_col'], downcast='float')

# Use sparse for mostly-null data
df['sparse_col'] = df['sparse_col'].astype(pd.SparseDtype('float', fill_value=0))
```

### Chunking Large Files

```python
# Read in chunks
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Process chunk
    processed = chunk[chunk['value'] > 0]
    chunks.append(processed)

result = pd.concat(chunks, ignore_index=True)
```

### Vectorized String Operations

```python
# Use .str accessor for vectorized string operations
df['name'].str.lower()
df['name'].str.contains('pattern')
df['name'].str.replace('old', 'new')
df['name'].str.split(',')
df['name'].str.extract(r'(\d+)')
```

---

## Missing Data Handling

### Advanced Imputation

```python
# Forward fill
df.fillna(method='ffill')

# Backward fill
df.fillna(method='bfill')

# Interpolate
df.interpolate(method='linear')
df.interpolate(method='polynomial', order=2)
df.interpolate(method='time')  # For time series

# Fill with group mean
df['value'] = df.groupby('category')['value'].transform(lambda x: x.fillna(x.mean()))
```

### Detecting Missing Patterns

```python
# Count missing values
df.isnull().sum()

# Percentage missing
df.isnull().mean() * 100

# Missing value heatmap
import seaborn as sns
sns.heatmap(df.isnull(), cbar=False)
```

---

## Pivot Tables and Crosstabs

### Advanced Pivot Tables

```python
# Basic pivot
pd.pivot_table(df, values='sales', index='region', columns='category', aggfunc='sum')

# Multiple aggregations
pd.pivot_table(df, values='sales', index='region', columns='category', 
               aggfunc=['sum', 'mean', 'count'])

# Multiple values
pd.pivot_table(df, values=['sales', 'profit'], index='region', columns='category', aggfunc='sum')

# With margins (totals)
pd.pivot_table(df, values='sales', index='region', columns='category', aggfunc='sum', margins=True)

# Fill missing values
pd.pivot_table(df, values='sales', index='region', columns='category', aggfunc='sum', fill_value=0)
```

### Crosstabs

```python
# Frequency table
pd.crosstab(df['category'], df['region'])

# With percentages
pd.crosstab(df['category'], df['region'], normalize='all')  # Overall percentage
pd.crosstab(df['category'], df['region'], normalize='index')  # Row percentage
pd.crosstab(df['category'], df['region'], normalize='columns')  # Column percentage

# With aggregation
pd.crosstab(df['category'], df['region'], values=df['sales'], aggfunc='sum')
```

---

## Window Functions

### Ranking

```python
# Rank within entire DataFrame
df['rank'] = df['sales'].rank()

# Rank within groups
df['rank'] = df.groupby('category')['sales'].rank()

# Different ranking methods
df['rank_min'] = df['sales'].rank(method='min')  # Ties get minimum rank
df['rank_dense'] = df['sales'].rank(method='dense')  # No gaps in ranks
df['rank_pct'] = df['sales'].rank(pct=True)  # Percentile ranks
```

### Cumulative Operations

```python
# Cumulative sum
df['cumsum'] = df.groupby('category')['sales'].cumsum()

# Cumulative max
df['cummax'] = df.groupby('category')['sales'].cummax()

# Cumulative product
df['cumprod'] = df.groupby('category')['sales'].cumprod()
```

### Shifting and Lagging

```python
# Lag (previous value)
df['sales_lag1'] = df.groupby('category')['sales'].shift(1)
df['sales_lag2'] = df.groupby('category')['sales'].shift(2)

# Lead (next value)
df['sales_lead1'] = df.groupby('category')['sales'].shift(-1)

# Difference
df['sales_diff'] = df.groupby('category')['sales'].diff()

# Percentage change
df['sales_pct_change'] = df.groupby('category')['sales'].pct_change()
```
