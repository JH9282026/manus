# DataFrames and Datasets

Comprehensive guide to Spark's structured APIs for high-performance data processing with schema enforcement and optimization.

## DataFrame Fundamentals

### What is a DataFrame?

A DataFrame is a distributed collection of data organized into named columns, similar to a table in a relational database or a pandas DataFrame, but with optimizations for distributed processing.

**Key Characteristics:**
- **Schema-based:** Strongly typed columns with defined data types
- **Immutable:** Transformations create new DataFrames
- **Lazy evaluation:** Operations build execution plan, run on action
- **Optimized:** Catalyst optimizer generates efficient physical plans
- **Language-agnostic:** Same performance in Python, Scala, Java, R

### Creating DataFrames

#### From Files

```python
# Parquet (recommended for analytics)
df = spark.read.parquet("s3://bucket/data/")
df = spark.read.parquet("hdfs://path/to/parquet")

# CSV
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df = spark.read.option("header", "true") \
    .option("inferSchema", "true") \
    .option("delimiter", ",") \
    .csv("data.csv")

# JSON
df = spark.read.json("data.json")
df = spark.read.option("multiLine", "true").json("nested.json")

# ORC
df = spark.read.orc("data.orc")

# Avro (requires spark-avro package)
df = spark.read.format("avro").load("data.avro")

# Text files
df = spark.read.text("logs.txt")  # Single column "value"
```

#### From Databases

```python
# JDBC
jdbc_url = "jdbc:postgresql://host:5432/database"
properties = {
    "user": "username",
    "password": "password",
    "driver": "org.postgresql.Driver"
}

df = spark.read.jdbc(url=jdbc_url, table="table_name", properties=properties)

# With query
query = "(SELECT * FROM table WHERE date >= '2024-01-01') AS subquery"
df = spark.read.jdbc(url=jdbc_url, table=query, properties=properties)

# Partitioned read for parallelism
df = spark.read.jdbc(
    url=jdbc_url,
    table="large_table",
    column="id",
    lowerBound=1,
    upperBound=1000000,
    numPartitions=100,
    properties=properties
)
```

#### From Hive

```python
# Enable Hive support
spark = SparkSession.builder.enableHiveSupport().getOrCreate()

# Read Hive table
df = spark.table("database.table_name")
df = spark.sql("SELECT * FROM database.table_name WHERE year = 2024")

# Show databases and tables
spark.sql("SHOW DATABASES").show()
spark.sql("SHOW TABLES IN database").show()
```

#### From RDDs

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# With schema inference
rdd = sc.parallelize([("Alice", 25), ("Bob", 30)])
df = spark.createDataFrame(rdd, ["name", "age"])

# With explicit schema
schema = StructType([
    StructField("name", StringType(), nullable=False),
    StructField("age", IntegerType(), nullable=True)
])
df = spark.createDataFrame(rdd, schema)
```

#### From Python Collections

```python
# From list of tuples
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["name", "age"])

# From list of dictionaries
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]
df = spark.createDataFrame(data)

# From pandas DataFrame
import pandas as pd
pandas_df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
df = spark.createDataFrame(pandas_df)
```

### Schema Definition

#### Explicit Schema

```python
from pyspark.sql.types import *

schema = StructType([
    StructField("id", LongType(), nullable=False),
    StructField("name", StringType(), nullable=False),
    StructField("email", StringType(), nullable=True),
    StructField("age", IntegerType(), nullable=True),
    StructField("salary", DoubleType(), nullable=True),
    StructField("hire_date", DateType(), nullable=True),
    StructField("last_login", TimestampType(), nullable=True),
    StructField("is_active", BooleanType(), nullable=False),
    StructField("tags", ArrayType(StringType()), nullable=True),
    StructField("metadata", MapType(StringType(), StringType()), nullable=True),
    StructField("address", StructType([
        StructField("street", StringType()),
        StructField("city", StringType()),
        StructField("zip", StringType())
    ]), nullable=True)
])

df = spark.read.schema(schema).json("data.json")
```

#### Schema Inference

```python
# Infer schema (requires scanning data)
df = spark.read.option("inferSchema", "true").csv("data.csv")

# View schema
df.printSchema()
df.schema  # Returns StructType

# Schema as DDL string
schema_ddl = "id LONG, name STRING, age INT, salary DOUBLE"
df = spark.read.schema(schema_ddl).csv("data.csv")
```

**Best Practice:** Use explicit schemas in production to avoid inference overhead and ensure data quality.

## DataFrame Operations

### Selection and Projection

```python
from pyspark.sql import functions as F

# Select columns
df.select("name", "age")
df.select(df.name, df.age)
df.select(df["name"], df["age"])
df.select(F.col("name"), F.col("age"))

# Select with expressions
df.select(
    F.col("name"),
    (F.col("age") + 1).alias("age_next_year"),
    F.upper(F.col("name")).alias("name_upper")
)

# Select all columns plus new ones
df.select("*", (F.col("salary") * 1.1).alias("salary_with_raise"))

# Drop columns
df.drop("column1", "column2")

# Rename columns
df.withColumnRenamed("old_name", "new_name")

# Add/modify columns
df.withColumn("age_group", F.when(F.col("age") < 30, "young").otherwise("senior"))
```

### Filtering

```python
# Simple filters
df.filter(df.age > 25)
df.filter("age > 25")
df.where(df.age > 25)  # Alias for filter

# Multiple conditions
df.filter((df.age > 25) & (df.salary > 50000))
df.filter((df.age < 25) | (df.age > 65))
df.filter(~(df.status == "inactive"))  # NOT

# SQL-style
df.filter("age > 25 AND salary > 50000")

# IN clause
df.filter(df.department.isin(["Engineering", "Sales"]))

# NULL checks
df.filter(df.email.isNotNull())
df.filter(df.phone.isNull())

# String operations
df.filter(df.name.startswith("A"))
df.filter(df.email.endswith("@company.com"))
df.filter(df.name.contains("Smith"))
df.filter(df.name.like("%Smith%"))
df.filter(df.name.rlike("^[A-Z][a-z]+$"))  # Regex
```

### Aggregations

```python
# Simple aggregations
df.count()
df.select(F.sum("salary"), F.avg("age"), F.max("salary"), F.min("age")).show()

# Group by
df.groupBy("department").count()
df.groupBy("department").agg(
    F.sum("salary").alias("total_salary"),
    F.avg("salary").alias("avg_salary"),
    F.count("*").alias("employee_count"),
    F.max("hire_date").alias("latest_hire")
)

# Multiple grouping columns
df.groupBy("department", "location").agg(F.avg("salary"))

# Collect list/set
df.groupBy("department").agg(
    F.collect_list("name").alias("employee_names"),
    F.collect_set("skill").alias("unique_skills")
)

# Count distinct
df.groupBy("department").agg(F.countDistinct("job_title").alias("unique_titles"))

# Approximate count distinct (faster for large data)
df.groupBy("department").agg(F.approx_count_distinct("user_id").alias("approx_users"))
```

### Sorting

```python
# Ascending
df.orderBy("age")
df.orderBy(F.col("age").asc())
df.sort("age")  # Alias for orderBy

# Descending
df.orderBy(F.col("salary").desc())

# Multiple columns
df.orderBy("department", F.col("salary").desc())

# NULL handling
df.orderBy(F.col("age").asc_nulls_first())
df.orderBy(F.col("age").asc_nulls_last())
```

### Joins

```python
# Inner join (default)
df1.join(df2, df1.id == df2.user_id)
df1.join(df2, "common_key")  # Join on column with same name

# Left outer join
df1.join(df2, df1.id == df2.user_id, "left")
df1.join(df2, df1.id == df2.user_id, "left_outer")

# Right outer join
df1.join(df2, df1.id == df2.user_id, "right")

# Full outer join
df1.join(df2, df1.id == df2.user_id, "outer")
df1.join(df2, df1.id == df2.user_id, "full")

# Left semi join (returns rows from left with match in right)
df1.join(df2, df1.id == df2.user_id, "left_semi")

# Left anti join (returns rows from left without match in right)
df1.join(df2, df1.id == df2.user_id, "left_anti")

# Cross join (cartesian product)
df1.crossJoin(df2)

# Multiple join conditions
df1.join(df2, (df1.id == df2.user_id) & (df1.date == df2.date))

# Broadcast join for small tables
from pyspark.sql.functions import broadcast
df_large.join(broadcast(df_small), "key")
```

### Window Functions

```python
from pyspark.sql.window import Window

# Define window specification
window_spec = Window.partitionBy("department").orderBy("salary")

# Ranking functions
df.withColumn("rank", F.rank().over(window_spec))
df.withColumn("dense_rank", F.dense_rank().over(window_spec))
df.withColumn("row_number", F.row_number().over(window_spec))
df.withColumn("percent_rank", F.percent_rank().over(window_spec))

# Analytic functions
df.withColumn("running_total", F.sum("salary").over(window_spec))
df.withColumn("avg_salary_in_dept", F.avg("salary").over(Window.partitionBy("department")))

# Lead and lag
df.withColumn("next_salary", F.lead("salary", 1).over(window_spec))
df.withColumn("prev_salary", F.lag("salary", 1).over(window_spec))

# First and last
df.withColumn("first_in_dept", F.first("name").over(window_spec))
df.withColumn("last_in_dept", F.last("name").over(window_spec))

# Window with frame specification
window_frame = Window.partitionBy("user_id") \
    .orderBy("timestamp") \
    .rowsBetween(-2, 0)  # Current row and 2 preceding rows

df.withColumn("moving_avg", F.avg("value").over(window_frame))

# Range-based window (value-based, not row-based)
window_range = Window.partitionBy("user_id") \
    .orderBy("timestamp") \
    .rangeBetween(-86400, 0)  # Last 24 hours (in seconds)

df.withColumn("daily_sum", F.sum("amount").over(window_range))
```

### Pivot and Unpivot

```python
# Pivot (wide format)
df.groupBy("year").pivot("department").sum("salary")

# Pivot with specific values (more efficient)
df.groupBy("year").pivot("department", ["Engineering", "Sales", "Marketing"]).sum("salary")

# Unpivot (long format) - using stack
df.selectExpr(
    "id",
    "stack(3, 'Q1', Q1, 'Q2', Q2, 'Q3', Q3) as (quarter, revenue)"
)
```

### Union and Intersection

```python
# Union (includes duplicates)
df1.union(df2)

# Union by name (matches columns by name, not position)
df1.unionByName(df2)

# Union with missing columns (fills with NULL)
df1.unionByName(df2, allowMissingColumns=True)

# Distinct union (removes duplicates)
df1.union(df2).distinct()

# Intersection
df1.intersect(df2)

# Except (rows in df1 but not in df2)
df1.subtract(df2)
df1.exceptAll(df2)  # Keeps duplicates
```

## Built-in Functions

### String Functions

```python
# Case conversion
df.withColumn("upper", F.upper("name"))
df.withColumn("lower", F.lower("name"))
df.withColumn("initcap", F.initcap("name"))  # Title case

# Trimming
df.withColumn("trimmed", F.trim("name"))
df.withColumn("ltrimmed", F.ltrim("name"))
df.withColumn("rtrimmed", F.rtrim("name"))

# Substring
df.withColumn("first_3", F.substring("name", 1, 3))

# Concatenation
df.withColumn("full_name", F.concat("first_name", F.lit(" "), "last_name"))
df.withColumn("full_name", F.concat_ws(" ", "first_name", "last_name"))

# Replace
df.withColumn("cleaned", F.regexp_replace("text", "[^a-zA-Z0-9]", ""))

# Split
df.withColumn("words", F.split("sentence", " "))

# Length
df.withColumn("name_length", F.length("name"))

# Padding
df.withColumn("padded", F.lpad("id", 10, "0"))
df.withColumn("padded", F.rpad("id", 10, "0"))
```

### Date and Time Functions

```python
# Current date/time
df.withColumn("current_date", F.current_date())
df.withColumn("current_timestamp", F.current_timestamp())

# Extract components
df.withColumn("year", F.year("date"))
df.withColumn("month", F.month("date"))
df.withColumn("day", F.dayofmonth("date"))
df.withColumn("hour", F.hour("timestamp"))
df.withColumn("minute", F.minute("timestamp"))
df.withColumn("second", F.second("timestamp"))
df.withColumn("day_of_week", F.dayofweek("date"))  # 1=Sunday
df.withColumn("day_of_year", F.dayofyear("date"))
df.withColumn("week_of_year", F.weekofyear("date"))

# Date arithmetic
df.withColumn("next_week", F.date_add("date", 7))
df.withColumn("last_month", F.add_months("date", -1))
df.withColumn("days_diff", F.datediff("end_date", "start_date"))
df.withColumn("months_diff", F.months_between("end_date", "start_date"))

# Truncate
df.withColumn("month_start", F.trunc("date", "month"))
df.withColumn("year_start", F.trunc("date", "year"))
df.withColumn("hour_start", F.date_trunc("hour", "timestamp"))

# Formatting
df.withColumn("formatted", F.date_format("date", "yyyy-MM-dd"))

# Parsing
df.withColumn("parsed", F.to_date("date_string", "yyyy-MM-dd"))
df.withColumn("parsed_ts", F.to_timestamp("ts_string", "yyyy-MM-dd HH:mm:ss"))

# Unix timestamp
df.withColumn("unix_ts", F.unix_timestamp("timestamp"))
df.withColumn("from_unix", F.from_unixtime("unix_ts"))
```

### Math Functions

```python
# Basic operations
df.withColumn("rounded", F.round("value", 2))
df.withColumn("ceiling", F.ceil("value"))
df.withColumn("floor", F.floor("value"))
df.withColumn("absolute", F.abs("value"))

# Trigonometric
df.withColumn("sine", F.sin("angle"))
df.withColumn("cosine", F.cos("angle"))
df.withColumn("tangent", F.tan("angle"))

# Exponential and logarithmic
df.withColumn("exp", F.exp("value"))
df.withColumn("log", F.log("value"))
df.withColumn("log10", F.log10("value"))
df.withColumn("sqrt", F.sqrt("value"))
df.withColumn("power", F.pow("base", "exponent"))

# Random
df.withColumn("random", F.rand())  # Uniform [0, 1)
df.withColumn("random_normal", F.randn())  # Standard normal
```

### Conditional Functions

```python
# When/otherwise (if-then-else)
df.withColumn("category",
    F.when(F.col("age") < 18, "minor")
     .when(F.col("age") < 65, "adult")
     .otherwise("senior")
)

# Coalesce (first non-null value)
df.withColumn("email", F.coalesce("work_email", "personal_email", F.lit("no_email")))

# Null handling
df.withColumn("filled", F.coalesce("value", F.lit(0)))
df.na.fill({"age": 0, "name": "unknown"})
df.na.drop()  # Drop rows with any NULL
df.na.drop(subset=["email"])  # Drop rows with NULL in specific columns
```

### Array and Map Functions

```python
# Array operations
df.withColumn("array", F.array("col1", "col2", "col3"))
df.withColumn("array_size", F.size("array_col"))
df.withColumn("first_element", F.element_at("array_col", 1))  # 1-indexed
df.withColumn("contains", F.array_contains("array_col", "value"))
df.withColumn("sorted", F.array_sort("array_col"))
df.withColumn("distinct", F.array_distinct("array_col"))
df.withColumn("joined", F.array_join("array_col", ","))

# Explode (array to rows)
df.withColumn("item", F.explode("array_col"))
df.withColumn("item", F.explode_outer("array_col"))  # Keeps NULL arrays

# Map operations
df.withColumn("map", F.create_map("key1", "value1", "key2", "value2"))
df.withColumn("value", F.element_at("map_col", "key"))
df.withColumn("keys", F.map_keys("map_col"))
df.withColumn("values", F.map_values("map_col"))

# Explode map (map to rows)
df.select("id", F.explode("map_col").alias("key", "value"))
```

### JSON Functions

```python
# Parse JSON string
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("name", StringType()),
    StructField("age", IntegerType())
])

df.withColumn("parsed", F.from_json("json_string", schema))
df.withColumn("name", F.get_json_object("json_string", "$.name"))

# Convert to JSON string
df.withColumn("json", F.to_json(F.struct("col1", "col2")))

# Extract from nested JSON
df.withColumn("nested_value", F.col("parsed.name"))
```

## User-Defined Functions (UDFs)

### Python UDFs

```python
from pyspark.sql.types import StringType, IntegerType

# Define UDF
def categorize_age(age):
    if age < 18:
        return "minor"
    elif age < 65:
        return "adult"
    else:
        return "senior"

# Register UDF
categorize_udf = F.udf(categorize_age, StringType())

# Use UDF
df.withColumn("category", categorize_udf("age"))

# Decorator syntax
@F.udf(returnType=StringType())
def categorize_age_v2(age):
    if age < 18:
        return "minor"
    elif age < 65:
        return "adult"
    else:
        return "senior"

df.withColumn("category", categorize_age_v2("age"))
```

**Performance Note:** Python UDFs are slow due to serialization overhead. Use built-in functions when possible.

### Pandas UDFs (Vectorized)

Faster than regular Python UDFs:

```python
import pandas as pd
from pyspark.sql.functions import pandas_udf

# Scalar Pandas UDF
@pandas_udf(StringType())
def categorize_age_pandas(ages: pd.Series) -> pd.Series:
    return ages.apply(lambda age:
        "minor" if age < 18 else "adult" if age < 65 else "senior"
    )

df.withColumn("category", categorize_age_pandas("age"))

# Grouped map Pandas UDF
schema = "id long, name string, avg_salary double"

@pandas_udf(schema, F.PandasUDFType.GROUPED_MAP)
def normalize_salary(pdf):
    pdf["avg_salary"] = pdf["salary"] / pdf["salary"].mean()
    return pdf

df.groupBy("department").apply(normalize_salary)
```

## Performance Optimization

### Catalyst Optimizer

Spark's query optimizer automatically:
- **Predicate pushdown** — Filters applied early
- **Column pruning** — Only needed columns read
- **Constant folding** — Compile-time expression evaluation
- **Join reordering** — Optimal join order
- **Projection pushdown** — Minimize data read from storage

**View execution plan:**
```python
df.explain()  # Physical plan
df.explain(True)  # Logical and physical plans
df.explain("extended")  # All plans
df.explain("formatted")  # Pretty-printed
```

### Caching Strategies

```python
# Cache when DataFrame used multiple times
df.cache()  # MEMORY_AND_DISK
df.persist(StorageLevel.MEMORY_ONLY_SER)  # Serialized, saves memory

# Check cached data
spark.catalog.isCached("table_name")

# Uncache
df.unpersist()
spark.catalog.clearCache()
```

**When to cache:**
- Iterative algorithms (ML training)
- Interactive queries on same data
- Expensive transformations reused downstream
- Branching workflows (multiple actions on same DataFrame)

### Broadcast Joins

For small tables (<10MB):

```python
from pyspark.sql.functions import broadcast

# Automatic broadcast (if table < spark.sql.autoBroadcastJoinThreshold)
df_large.join(df_small, "key")

# Explicit broadcast
df_large.join(broadcast(df_small), "key")

# Configure threshold (default 10MB)
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 20 * 1024 * 1024)  # 20MB
```

### Partition Tuning

```python
# Check current partitions
df.rdd.getNumPartitions()

# Repartition (full shuffle)
df.repartition(200)
df.repartition("date", "region")  # Hash partitioning by columns

# Coalesce (reduce partitions without shuffle)
df.coalesce(10)

# Configure shuffle partitions
spark.conf.set("spark.sql.shuffle.partitions", "400")  # Default 200
```

**Guidelines:**
- Target 128MB-1GB per partition
- Use 2-3x number of cores for parallelism
- Increase shuffle partitions for large aggregations/joins
- Use coalesce before writing to reduce small files

### Avoiding Shuffles

**Shuffle-heavy operations:**
- `groupBy`, `join`, `repartition`, `distinct`, `sortBy`

**Strategies:**
- Use broadcast joins for small tables
- Pre-partition data by join keys
- Use `reduceByKey` instead of `groupByKey` (RDDs)
- Combine operations to minimize shuffle stages

## Datasets (Scala/Java)

Type-safe API with compile-time checking:

```scala
// Define case class
case class Person(name: String, age: Int, salary: Double)

// Create Dataset
val ds: Dataset[Person] = spark.read.json("people.json").as[Person]

// Type-safe operations
ds.filter(_.age > 25)
ds.map(p => p.copy(salary = p.salary * 1.1))
ds.groupByKey(_.age).count()

// Convert to DataFrame
val df: DataFrame = ds.toDF()

// Convert DataFrame to Dataset
val ds2: Dataset[Person] = df.as[Person]
```

**Advantages over DataFrames:**
- Compile-time type safety
- Better IDE support (autocomplete, refactoring)
- Encoder-based serialization (faster than Java serialization)

**Disadvantages:**
- Only available in Scala/Java (not Python/R)
- Slightly more verbose
- Less flexible than DataFrames for ad-hoc queries

## Best Practices

### Schema Management

1. **Use explicit schemas in production** — Avoid inference overhead
2. **Validate data quality** — Check for NULLs, types, ranges
3. **Version schemas** — Track changes over time
4. **Use schema evolution** — Parquet/Delta support adding columns

### Code Organization

```python
# Modular transformations
def clean_data(df):
    return df.filter("status = 'active'").na.drop()

def enrich_data(df):
    return df.withColumn("full_name", F.concat("first_name", F.lit(" "), "last_name"))

def aggregate_data(df):
    return df.groupBy("department").agg(F.sum("salary"))

# Pipeline
result = aggregate_data(enrich_data(clean_data(df)))
```

### Testing

```python
import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[*]").getOrCreate()

def test_transformation(spark):
    # Arrange
    input_data = [("Alice", 25), ("Bob", 30)]
    df = spark.createDataFrame(input_data, ["name", "age"])
    
    # Act
    result = df.filter("age > 25")
    
    # Assert
    assert result.count() == 1
    assert result.first()["name"] == "Bob"
```

### Monitoring

- Use Spark UI to identify bottlenecks
- Monitor shuffle read/write sizes
- Check for data skew (uneven partition sizes)
- Track GC time (should be <10% of task time)
- Monitor spill to disk (indicates memory pressure)
