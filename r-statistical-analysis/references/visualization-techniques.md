# Visualization Techniques

Comprehensive guide to creating effective data visualizations in R using ggplot2 and related packages.

---

## ggplot2 Fundamentals

### Grammar of Graphics

ggplot2 builds plots in layers:

1. **Data**: The dataset to visualize
2. **Aesthetics**: Mapping of variables to visual properties (x, y, color, size, etc.)
3. **Geometries**: The type of plot (points, lines, bars, etc.)
4. **Statistics**: Statistical transformations (binning, smoothing, etc.)
5. **Scales**: Control how aesthetics map to values
6. **Coordinates**: The coordinate system
7. **Facets**: Subplots based on variables
8. **Themes**: Overall visual appearance

### Basic Template

```r
ggplot(data = df, aes(x = var1, y = var2)) +
  geom_point() +
  labs(title = "Title", x = "X Label", y = "Y Label") +
  theme_minimal()
```

---

## Common Plot Types

### Scatter Plots

```r
# Basic scatter plot
ggplot(df, aes(x = x, y = y)) +
  geom_point()

# With color by group
ggplot(df, aes(x = x, y = y, color = group)) +
  geom_point(size = 3, alpha = 0.7)

# With size mapping
ggplot(df, aes(x = x, y = y, size = value, color = group)) +
  geom_point(alpha = 0.6)

# With trend line
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  geom_smooth(method = "lm", se = TRUE)

# With LOESS smoothing
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  geom_smooth(method = "loess", span = 0.3)
```

### Line Plots

```r
# Basic line plot
ggplot(df, aes(x = date, y = value)) +
  geom_line()

# Multiple lines by group
ggplot(df, aes(x = date, y = value, color = group)) +
  geom_line(size = 1)

# With points
ggplot(df, aes(x = date, y = value)) +
  geom_line() +
  geom_point()

# With confidence interval
ggplot(df, aes(x = date, y = value)) +
  geom_line() +
  geom_ribbon(aes(ymin = lower, ymax = upper), alpha = 0.3)
```

### Bar Charts

```r
# Basic bar chart
ggplot(df, aes(x = category, y = value)) +
  geom_col()

# Grouped bars
ggplot(df, aes(x = category, y = value, fill = group)) +
  geom_col(position = "dodge")

# Stacked bars
ggplot(df, aes(x = category, y = value, fill = group)) +
  geom_col(position = "stack")

# Percentage stacked
ggplot(df, aes(x = category, y = value, fill = group)) +
  geom_col(position = "fill") +
  scale_y_continuous(labels = scales::percent)

# Horizontal bars
ggplot(df, aes(x = value, y = reorder(category, value))) +
  geom_col() +
  labs(y = "Category")
```

### Histograms and Density Plots

```r
# Histogram
ggplot(df, aes(x = value)) +
  geom_histogram(bins = 30, fill = "steelblue", color = "white")

# Density plot
ggplot(df, aes(x = value)) +
  geom_density(fill = "steelblue", alpha = 0.5)

# Multiple densities
ggplot(df, aes(x = value, fill = group)) +
  geom_density(alpha = 0.5)

# Histogram with density overlay
ggplot(df, aes(x = value)) +
  geom_histogram(aes(y = ..density..), bins = 30, fill = "steelblue", alpha = 0.5) +
  geom_density(color = "red", size = 1)
```

### Box Plots and Violin Plots

```r
# Box plot
ggplot(df, aes(x = group, y = value)) +
  geom_boxplot()

# Box plot with points
ggplot(df, aes(x = group, y = value)) +
  geom_boxplot(outlier.shape = NA) +
  geom_jitter(width = 0.2, alpha = 0.3)

# Violin plot
ggplot(df, aes(x = group, y = value)) +
  geom_violin()

# Violin with box plot inside
ggplot(df, aes(x = group, y = value)) +
  geom_violin() +
  geom_boxplot(width = 0.1)
```

### Heatmaps

```r
# Basic heatmap
ggplot(df, aes(x = x_var, y = y_var, fill = value)) +
  geom_tile() +
  scale_fill_gradient(low = "white", high = "red")

# Diverging color scale
ggplot(df, aes(x = x_var, y = y_var, fill = value)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", mid = "white", high = "red", midpoint = 0)

# With text labels
ggplot(df, aes(x = x_var, y = y_var, fill = value)) +
  geom_tile() +
  geom_text(aes(label = round(value, 2))) +
  scale_fill_gradient(low = "white", high = "red")
```

---

## Advanced Customization

### Color Scales

```r
# Manual colors
ggplot(df, aes(x = x, y = y, color = group)) +
  geom_point() +
  scale_color_manual(values = c("red", "blue", "green"))

# ColorBrewer palettes
ggplot(df, aes(x = x, y = y, color = group)) +
  geom_point() +
  scale_color_brewer(palette = "Set1")

# Viridis (colorblind-friendly)
ggplot(df, aes(x = x, y = y, color = value)) +
  geom_point() +
  scale_color_viridis_c()

# Custom gradient
ggplot(df, aes(x = x, y = y, color = value)) +
  geom_point() +
  scale_color_gradient(low = "yellow", high = "red")
```

### Axis Customization

```r
# Axis limits
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  xlim(0, 100) +
  ylim(0, 50)

# Axis breaks
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  scale_x_continuous(breaks = seq(0, 100, 10)) +
  scale_y_continuous(breaks = seq(0, 50, 5))

# Log scale
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  scale_x_log10() +
  scale_y_log10()

# Custom labels
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  scale_x_continuous(labels = scales::comma) +
  scale_y_continuous(labels = scales::dollar)

# Date axis
ggplot(df, aes(x = date, y = value)) +
  geom_line() +
  scale_x_date(date_breaks = "1 month", date_labels = "%b %Y")
```

### Faceting

```r
# Facet wrap (one variable)
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  facet_wrap(~category)

# Facet wrap with custom layout
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  facet_wrap(~category, ncol = 3)

# Facet grid (two variables)
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  facet_grid(rows = vars(var1), cols = vars(var2))

# Free scales
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  facet_wrap(~category, scales = "free")
```

### Themes

```r
# Built-in themes
ggplot(df, aes(x = x, y = y)) + geom_point() + theme_minimal()
ggplot(df, aes(x = x, y = y)) + geom_point() + theme_classic()
ggplot(df, aes(x = x, y = y)) + geom_point() + theme_bw()
ggplot(df, aes(x = x, y = y)) + geom_point() + theme_dark()

# Custom theme elements
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    axis.title = element_text(size = 12),
    axis.text = element_text(size = 10),
    legend.position = "bottom",
    panel.grid.minor = element_blank()
  )

# Remove legend
ggplot(df, aes(x = x, y = y, color = group)) +
  geom_point() +
  theme(legend.position = "none")
```

### Labels and Annotations

```r
# Labels
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  labs(
    title = "Main Title",
    subtitle = "Subtitle text",
    caption = "Source: Data source",
    x = "X Axis Label",
    y = "Y Axis Label",
    color = "Legend Title"
  )

# Text annotations
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  annotate("text", x = 50, y = 30, label = "Important point", size = 5)

# Arrow annotations
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  annotate("segment", x = 40, xend = 50, y = 25, yend = 30,
           arrow = arrow(length = unit(0.3, "cm")))

# Rectangle annotations
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  annotate("rect", xmin = 40, xmax = 60, ymin = 20, ymax = 40,
           alpha = 0.2, fill = "red")
```

---

## Interactive Visualizations

### plotly

```r
library(plotly)

# Convert ggplot to plotly
p <- ggplot(df, aes(x = x, y = y, color = group)) +
  geom_point()
ggplotly(p)

# Native plotly
plot_ly(df, x = ~x, y = ~y, color = ~group, type = "scatter", mode = "markers")

# 3D scatter plot
plot_ly(df, x = ~x, y = ~y, z = ~z, color = ~group, type = "scatter3d", mode = "markers")
```

### ggiraph

```r
library(ggiraph)

# Interactive points with tooltips
p <- ggplot(df, aes(x = x, y = y, tooltip = label, data_id = id)) +
  geom_point_interactive(size = 3)

girafe(ggobj = p)
```

---

## Publication-Quality Graphics

### High-Resolution Export

```r
# Save as PNG
ggsave("plot.png", width = 8, height = 6, dpi = 300)

# Save as PDF (vector)
ggsave("plot.pdf", width = 8, height = 6)

# Save as SVG (vector)
ggsave("plot.svg", width = 8, height = 6)

# Save as TIFF
ggsave("plot.tiff", width = 8, height = 6, dpi = 300, compression = "lzw")
```

### Custom Theme for Publications

```r
theme_publication <- function(base_size = 12) {
  theme_bw(base_size = base_size) +
    theme(
      plot.title = element_text(size = base_size + 2, face = "bold", hjust = 0.5),
      axis.title = element_text(size = base_size),
      axis.text = element_text(size = base_size - 1),
      legend.title = element_text(size = base_size, face = "bold"),
      legend.text = element_text(size = base_size - 1),
      legend.position = "bottom",
      panel.grid.minor = element_blank(),
      strip.background = element_rect(fill = "white", color = "black"),
      strip.text = element_text(size = base_size, face = "bold")
    )
}

# Use custom theme
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  theme_publication()
```

---

## Specialized Visualizations

### Correlation Matrices

```r
library(corrplot)

# Calculate correlation matrix
cor_matrix <- cor(df[, numeric_columns])

# Visualize
corrplot(cor_matrix, method = "circle", type = "upper", order = "hclust")

# With ggplot2
library(reshape2)
cor_melted <- melt(cor_matrix)
ggplot(cor_melted, aes(Var1, Var2, fill = value)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", mid = "white", high = "red", midpoint = 0) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```

### Network Graphs

```r
library(igraph)
library(ggraph)

# Create network
graph <- graph_from_data_frame(edges_df, vertices = nodes_df)

# Plot with ggraph
ggraph(graph, layout = "fr") +
  geom_edge_link(aes(alpha = weight)) +
  geom_node_point(aes(size = degree, color = group)) +
  geom_node_text(aes(label = name), repel = TRUE) +
  theme_graph()
```

### Geographic Maps

```r
library(maps)
library(sf)

# Basic map
world <- map_data("world")
ggplot(world, aes(x = long, y = lat, group = group)) +
  geom_polygon(fill = "lightgray", color = "white") +
  coord_fixed(1.3)

# Choropleth map
ggplot(world, aes(x = long, y = lat, group = group, fill = value)) +
  geom_polygon(color = "white") +
  scale_fill_viridis_c() +
  coord_fixed(1.3)
```