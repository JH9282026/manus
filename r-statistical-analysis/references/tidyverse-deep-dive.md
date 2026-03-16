# Tidyverse Deep Dive

Comprehensive guide to advanced data manipulation and transformation using tidyverse packages.

---

## Advanced dplyr Techniques

### Window Functions

Window functions operate on groups of rows and return a value for each row:

```r
# Ranking within groups
data %>%
  group_by(category) %>%
  mutate(
    rank = row_number(desc(sales)),
    percentile = percent_rank(sales),
    cumulative_sales = cumsum(sales)
  )

# Moving averages
data %>%
  arrange(date) %>%
  mutate(
    ma_7day = zoo::rollmean(value, k = 7, fill = NA, align = "right"),
    ma_30day = zoo::rollmean(value, k = 30, fill = NA, align = "right")
  )
```

### Scoped Verbs

Apply operations to multiple columns simultaneously:

```r
# Apply to all columns
data %>% mutate_all(as.character)

# Apply to specific columns by condition
data %>% mutate_if(is.numeric, ~round(., 2))

# Apply to specific columns by name
data %>% mutate_at(vars(starts_with("sales_")), ~. / 1000)

# Modern approach with across()
data %>%
  mutate(across(where(is.numeric), ~round(., 2))) %>%
  mutate(across(starts_with("sales_"), ~. / 1000))
```

### Complex Filtering

```r
# Multiple conditions
data %>%
  filter(
    year >= 2020,
    region %in% c("North", "South"),
    sales > mean(sales, na.rm = TRUE)
  )

# Filter with grouped conditions
data %>%
  group_by(category) %>%
  filter(sales > quantile(sales, 0.75))

# Filter with string matching
data %>%
  filter(
    str_detect(product_name, "Premium"),
    !str_detect(customer_type, "Internal")
  )
```

### Advanced Summarization

```r
# Multiple summary statistics
data %>%
  group_by(region, category) %>%
  summarise(
    n = n(),
    total_sales = sum(sales),
    avg_sales = mean(sales),
    median_sales = median(sales),
    sd_sales = sd(sales),
    min_sales = min(sales),
    max_sales = max(sales),
    q25 = quantile(sales, 0.25),
    q75 = quantile(sales, 0.75),
    .groups = "drop"
  )

# Conditional aggregation
data %>%
  group_by(region) %>%
  summarise(
    total_revenue = sum(sales * price),
    premium_revenue = sum(sales * price * (category == "Premium")),
    premium_pct = premium_revenue / total_revenue
  )
```

### Joins and Relationships

```r
# Inner join - only matching rows
inner_join(sales, customers, by = "customer_id")

# Left join - all rows from left table
left_join(sales, customers, by = "customer_id")

# Right join - all rows from right table
right_join(sales, customers, by = "customer_id")

# Full join - all rows from both tables
full_join(sales, customers, by = "customer_id")

# Anti join - rows in left table without match in right
anti_join(sales, customers, by = "customer_id")

# Semi join - rows in left table with match in right
semi_join(sales, customers, by = "customer_id")

# Join on multiple keys
left_join(sales, products, by = c("product_id", "region"))

# Join with different column names
left_join(sales, customers, by = c("cust_id" = "customer_id"))
```

---

## Advanced tidyr Techniques

### Pivoting Data

```r
# Wide to long format
data_wide %>%
  pivot_longer(
    cols = starts_with("month_"),
    names_to = "month",
    values_to = "sales",
    names_prefix = "month_"
  )

# Long to wide format
data_long %>%
  pivot_wider(
    names_from = category,
    values_from = sales,
    values_fill = 0
  )

# Multiple value columns
data %>%
  pivot_wider(
    names_from = metric,
    values_from = c(value, percentage),
    names_sep = "_"
  )
```

### Handling Missing Data

```r
# Drop rows with any missing values
data %>% drop_na()

# Drop rows with missing values in specific columns
data %>% drop_na(sales, customer_id)

# Fill missing values with specific value
data %>% replace_na(list(sales = 0, region = "Unknown"))

# Fill missing values with previous/next value
data %>%
  arrange(date) %>%
  fill(sales, .direction = "down")  # Forward fill

data %>%
  arrange(date) %>%
  fill(sales, .direction = "up")  # Backward fill
```

### Nesting and Unnesting

```r
# Create nested data frames
nested_data <- data %>%
  group_by(region) %>%
  nest()

# Apply functions to nested data
nested_data %>%
  mutate(
    model = map(data, ~lm(sales ~ price, data = .)),
    predictions = map2(model, data, predict),
    r_squared = map_dbl(model, ~summary(.)$r.squared)
  )

# Unnest results
nested_data %>%
  unnest(cols = c(data))
```

### Separating and Uniting Columns

```r
# Separate one column into multiple
data %>%
  separate(
    col = full_name,
    into = c("first_name", "last_name"),
    sep = " "
  )

# Unite multiple columns into one
data %>%
  unite(
    col = "full_address",
    street, city, state, zip,
    sep = ", "
  )
```

---

## Advanced purrr Techniques

### Functional Programming with map()

```r
# Apply function to each element
list_of_dfs %>% map(nrow)

# Return specific type
list_of_dfs %>% map_int(nrow)  # Integer vector
list_of_dfs %>% map_dbl(~mean(.$sales))  # Double vector
list_of_dfs %>% map_chr(~class(.)[1])  # Character vector
list_of_dfs %>% map_lgl(~any(is.na(.)))  # Logical vector

# Map with multiple arguments
map2(list1, list2, ~.x + .y)
pmap(list(a, b, c), function(x, y, z) x + y + z)
```

### Error Handling

```r
# Safely handle errors
safe_log <- safely(log)
results <- map(values, safe_log)

# Extract successful results
results %>% map("result") %>% compact()

# Extract errors
results %>% map("error") %>% compact()

# Use possibly() for default values on error
possible_log <- possibly(log, otherwise = NA)
map_dbl(values, possible_log)
```

### Reducing and Accumulating

```r
# Reduce list to single value
list_of_dfs %>% reduce(bind_rows)

# Accumulate intermediate results
accumulate(1:10, `+`)  # Cumulative sum

# Custom reduction
list_of_dfs %>%
  reduce(~left_join(.x, .y, by = "id"))
```

---

## String Manipulation with stringr

### Pattern Matching

```r
# Detect patterns
str_detect(strings, "pattern")
str_which(strings, "pattern")  # Return indices
str_subset(strings, "pattern")  # Return matching strings

# Extract patterns
str_extract(strings, "\\d+")  # First match
str_extract_all(strings, "\\d+")  # All matches

# Replace patterns
str_replace(strings, "old", "new")  # First occurrence
str_replace_all(strings, "old", "new")  # All occurrences

# Remove patterns
str_remove(strings, "pattern")
str_remove_all(strings, "pattern")
```

### String Transformation

```r
# Case conversion
str_to_upper(strings)
str_to_lower(strings)
str_to_title(strings)

# Trimming whitespace
str_trim(strings)  # Both sides
str_trim(strings, side = "left")
str_trim(strings, side = "right")

# Padding
str_pad(strings, width = 10, side = "left", pad = "0")

# Truncating
str_trunc(strings, width = 20, side = "right", ellipsis = "...")
```

### String Splitting and Combining

```r
# Split strings
str_split(strings, pattern = ",")
str_split_fixed(strings, pattern = ",", n = 3)  # Fixed number of pieces

# Combine strings
str_c("Hello", "World", sep = " ")
str_glue("The value is {value}")
```

---

## Date and Time with lubridate

### Parsing Dates

```r
# Parse common formats
ymd("2024-03-15")
mdy("03/15/2024")
dmy("15-03-2024")
ymd_hms("2024-03-15 14:30:00")

# Parse with time zones
ymd_hms("2024-03-15 14:30:00", tz = "America/New_York")
```

### Extracting Components

```r
# Extract date components
year(date)
month(date)
day(date)
wday(date, label = TRUE)  # Day of week
quarter(date)

# Extract time components
hour(datetime)
minute(datetime)
second(datetime)
```

### Date Arithmetic

```r
# Add/subtract periods
date + days(7)
date + months(3)
date + years(1)

# Calculate differences
interval(start_date, end_date) / days(1)  # Days between
interval(start_date, end_date) / months(1)  # Months between

# Round dates
floor_date(date, "month")
ceiling_date(date, "month")
round_date(date, "month")
```

### Time Zones

```r
# Convert time zones
with_tz(datetime, "America/Los_Angeles")
force_tz(datetime, "America/Los_Angeles")

# List available time zones
OlsonNames()
```

---

## Performance Optimization

### Using data.table for Large Data

```r
library(data.table)

# Convert to data.table
dt <- as.data.table(df)

# Fast aggregation
dt[, .(total_sales = sum(sales)), by = region]

# Fast filtering and updating
dt[sales > 1000, status := "high"]

# Chaining operations
dt[year >= 2020][, .(avg_sales = mean(sales)), by = .(region, category)]
```

### Vectorization

```r
# Avoid loops - use vectorized operations
# Bad
result <- numeric(length(x))
for (i in seq_along(x)) {
  result[i] <- x[i] * 2
}

# Good
result <- x * 2

# Use apply family for complex operations
lapply(list_data, function(x) mean(x$value))
sapply(list_data, function(x) mean(x$value))
```

### Efficient Data Import

```r
# Use readr for speed
data <- read_csv("large_file.csv")

# Use data.table::fread for very large files
data <- fread("very_large_file.csv")

# Read only needed columns
data <- read_csv("file.csv", col_select = c(id, sales, date))

# Read in chunks
read_csv_chunked(
  "huge_file.csv",
  callback = DataFrameCallback$new(function(x, pos) {
    # Process chunk
  }),
  chunk_size = 10000
)
```