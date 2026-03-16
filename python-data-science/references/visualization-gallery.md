# Visualization Gallery

Comprehensive examples of data visualizations using Matplotlib, Seaborn, and Plotly.

---

## Matplotlib Examples

### Line Plots

```python
import matplotlib.pyplot as plt
import numpy as np

# Basic line plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', linewidth=2)
plt.plot(x, y2, label='cos(x)', linewidth=2, linestyle='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trigonometric Functions')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### Scatter Plots

```python
# Scatter with color mapping
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.colorbar(label='Color Value')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Color and Size Mapping')
plt.show()
```

### Bar Charts

```python
# Grouped bar chart
categories = ['A', 'B', 'C', 'D']
values1 = [23, 45, 56, 78]
values2 = [34, 56, 67, 89]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width/2, values1, width, label='Group 1')
ax.bar(x + width/2, values2, width, label='Group 2')

ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Grouped Bar Chart')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
plt.show()
```

---

## Seaborn Examples

### Distribution Plots

```python
import seaborn as sns
import pandas as pd

# Load example dataset
tips = sns.load_dataset('tips')

# Histogram with KDE
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x='total_bill', kde=True, bins=30)
plt.title('Distribution of Total Bill')
plt.show()

# Multiple distributions
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x='total_bill', hue='time', kde=True, bins=30)
plt.title('Distribution by Time')
plt.show()
```

### Relationship Plots

```python
# Scatter plot with regression
plt.figure(figsize=(10, 6))
sns.regplot(data=tips, x='total_bill', y='tip')
plt.title('Total Bill vs Tip')
plt.show()

# Joint plot
sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg', height=8)
plt.show()

# Pair plot
sns.pairplot(tips, hue='time')
plt.show()
```

### Categorical Plots

```python
# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='total_bill', hue='time')
plt.title('Total Bill by Day and Time')
plt.show()

# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=tips, x='day', y='total_bill', hue='time', split=True)
plt.title('Distribution by Day and Time')
plt.show()
```

---

## Plotly Examples

### Interactive Line Plot

```python
import plotly.graph_objects as go

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='sin(x)'))
fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='cos(x)'))

fig.update_layout(
    title='Interactive Trigonometric Functions',
    xaxis_title='X',
    yaxis_title='Y',
    hovermode='x unified'
)

fig.show()
```

### 3D Scatter Plot

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_length',
                    color='species', size='petal_width', hover_data=['species'])
fig.show()
```
