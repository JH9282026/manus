---
name: big-data-processing-spark
description: "Process and analyze massive datasets using Apache Spark distributed computing framework. Use for: large-scale data processing (TB/PB scale), real-time stream processing, machine learning on big data, ETL pipelines, data lake analytics, distributed SQL queries, batch and streaming workloads, cluster computing tasks, and high-performance data transformations."
---

# Big Data Processing with Apache Spark

Process and analyze massive datasets using Apache Spark's distributed computing framework for batch and streaming workloads.

## Overview

Apache Spark is a unified analytics engine for large-scale data processing, providing high-level APIs in Java, Scala, Python, and R. This skill covers Spark architecture, DataFrames/Datasets, streaming, optimization techniques, and production deployment patterns for processing terabyte to petabyte-scale data efficiently across distributed clusters.

## Core Spark Architecture

### Execution Model

| Component | Purpose | Key Characteristics |
|-----------|---------|---------------------|
| **Driver** | Orchestrates execution | Runs main program, creates SparkContext, schedules tasks |
| **Executors** | Execute tasks | Run on worker nodes, store data in memory/disk, report status |
| **Cluster Manager** | Resource allocation | YARN, Mesos, Kubernetes, or Standalone mode |
| **DAG Scheduler** | Optimizes execution | Builds directed acyclic graph, stage optimization |
| **Task Scheduler** | Distributes work | Assigns tasks to executors, handles failures |

### Memory Management

- **Storage Memory**: Cached RDDs, DataFrames, broadcast variables (default 50% of heap)
- **Execution Memory**: Shuffles, joins, sorts, aggregations (default 50% of heap)
- **User Memory**: User data structures, UDFs (remaining heap space)
- **Reserved Memory**: System reserved (300MB default)

### Deployment Modes

**Cluster Mode** — Driver runs on cluster worker node, fully distributed
**Client Mode** — Driver runs on client machine, executors on cluster
**Local Mode** — Single JVM for development/testing (local[*] uses all cores)

## Data Abstractions

### RDD vs DataFrame vs Dataset

| Feature | RDD | DataFrame | Dataset |
|---------|-----|-----------|----------|
| **Type Safety** | Compile-time | Runtime | Compile-time |
| **Optimization** | Manual | Catalyst optimizer | Catalyst optimizer |
| **API Style** | Functional | SQL-like | Type-safe SQL |
| **Performance** | Baseline | 2-10x faster | 2-10x faster |
| **Use Case** | Low-level control | SQL analytics | Type-safe transformations |
| **Language** | All | All | Scala/Java only |

### When to Use Each

**Use DataFrames when:**
- Performing SQL-like operations (filters, aggregations, joins)
- Working with structured/semi-structured data
- Need maximum performance with Catalyst optimization
- Using Python or R (Datasets not available)
- Building ETL pipelines with schema enforcement

**Use Datasets when:**
- Need compile-time type safety (Scala/Java)
- Working with domain objects and case classes
- Want functional programming with optimization benefits
- Require encoder-based serialization performance

**Use RDDs when:**
- Need fine-grained control over partitioning
- Working with unstructured data without schema
- Implementing custom partitioners or low-level operations
- Maintaining legacy code (pre-Spark 2.0)

## Spark SQL and DataFrames

### Creating DataFrames

```python
# From structured files
df = spark.read.parquet("s3://bucket/data/")
df = spark.read.json("hdfs://path/to/json")
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# From databases
df = spark.read.jdbc(url=jdbc_url, table="table_name", properties=props)

# From RDDs with schema
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])
df = spark.createDataFrame(rdd, schema)

# From Hive tables
df = spark.sql("SELECT * FROM hive_table WHERE date >= '2024-01-01'")
```

### Essential DataFrame Operations

```python
# Selection and filtering
df.select("col1", "col2").filter(df.col1 > 100)
df.where((df.status == "active") & (df.amount > 1000))

# Aggregations
df.groupBy("category").agg(
    F.sum("revenue").alias("total_revenue"),
    F.avg("price").alias("avg_price"),
    F.count("*").alias("count")
)

# Window functions
from pyspark.sql.window import Window
window_spec = Window.partitionBy("user_id").orderBy("timestamp")
df.withColumn("row_num", F.row_number().over(window_spec))

# Joins
df1.join(df2, df1.id == df2.user_id, "inner")
df1.join(df2, "common_key", "left_outer")
```

### Performance Patterns

**Predicate Pushdown** — Filter early to reduce data movement
**Column Pruning** — Select only needed columns
**Broadcast Joins** — Use for small tables (<10MB) to avoid shuffles
**Partition Pruning** — Leverage partitioned data sources
**Caching** — Cache intermediate results used multiple times

## Streaming Processing

### Structured Streaming Fundamentals

```python
# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "topic1,topic2") \
    .load()

# Process stream
processed = df.selectExpr("CAST(value AS STRING)") \
    .select(F.from_json(F.col("value"), schema).alias("data")) \
    .select("data.*") \
    .groupBy(F.window("timestamp", "10 minutes"), "category") \
    .agg(F.sum("amount").alias("total"))

# Write to sink
query = processed.writeStream \
    .outputMode("update") \
    .format("parquet") \
    .option("path", "s3://output/") \
    .option("checkpointLocation", "s3://checkpoints/") \
    .trigger(processingTime="30 seconds") \
    .start()

query.awaitTermination()
```

### Output Modes

| Mode | Behavior | Use Case |
|------|----------|----------|
| **Append** | Only new rows | Immutable events, logs |
| **Complete** | Entire result table | Small aggregations, dashboards |
| **Update** | Changed rows only | Large aggregations, incremental updates |

### Windowing Operations

**Tumbling Windows** — Fixed, non-overlapping intervals (e.g., every 10 minutes)
**Sliding Windows** — Overlapping intervals (e.g., 10-minute window, 5-minute slide)
**Session Windows** — Dynamic windows based on inactivity gaps

## Optimization Techniques

### Partitioning Strategies

```python
# Repartition for parallelism
df.repartition(200)  # Increase partitions for more parallelism
df.repartition("date", "region")  # Partition by columns

# Coalesce to reduce partitions (no shuffle)
df.coalesce(10)  # Reduce partitions efficiently

# Write with partitioning
df.write.partitionBy("year", "month").parquet("output/")
```

### Caching and Persistence

```python
# Cache in memory
df.cache()  # MEMORY_AND_DISK by default

# Explicit storage levels
from pyspark import StorageLevel
df.persist(StorageLevel.MEMORY_ONLY)
df.persist(StorageLevel.MEMORY_AND_DISK_SER)  # Serialized, saves memory
df.persist(StorageLevel.DISK_ONLY)

# Unpersist when done
df.unpersist()
```

### Broadcast Variables

```python
# Broadcast small lookup tables
lookup_dict = {"A": 1, "B": 2, "C": 3}
broadcast_var = spark.sparkContext.broadcast(lookup_dict)

# Use in UDF
def map_value(key):
    return broadcast_var.value.get(key, 0)

map_udf = F.udf(map_value, IntegerType())
df.withColumn("mapped", map_udf(F.col("key")))

# Broadcast join (automatic for small DataFrames)
from pyspark.sql.functions import broadcast
df_large.join(broadcast(df_small), "key")
```

### Avoiding Shuffles

**Shuffle-Heavy Operations:**
- `groupBy`, `join`, `repartition`, `distinct`, `sortBy`
- Window functions with `PARTITION BY`
- `reduceByKey`, `aggregateByKey` (RDD operations)

**Shuffle Reduction Strategies:**
- Use broadcast joins for small tables
- Pre-partition data by join keys
- Use `mapPartitions` instead of `map` for batch processing
- Combine operations to minimize shuffle stages
- Increase `spark.sql.shuffle.partitions` for large shuffles (default 200)

## Configuration Tuning

### Memory Configuration

```python
conf = SparkConf() \
    .set("spark.executor.memory", "8g") \
    .set("spark.executor.cores", "4") \
    .set("spark.executor.instances", "50") \
    .set("spark.driver.memory", "4g") \
    .set("spark.memory.fraction", "0.8")  # 80% for execution/storage \
    .set("spark.memory.storageFraction", "0.3")  # 30% of above for storage
```

### Shuffle Configuration

```python
conf.set("spark.sql.shuffle.partitions", "400")  # Default 200, increase for large data
conf.set("spark.shuffle.compress", "true")
conf.set("spark.shuffle.spill.compress", "true")
conf.set("spark.shuffle.file.buffer", "64k")  # Increase for better I/O
```

### Serialization

```python
# Use Kryo for better performance
conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
conf.set("spark.kryo.registrationRequired", "false")
conf.set("spark.kryoserializer.buffer.max", "512m")
```

### Dynamic Allocation

```python
conf.set("spark.dynamicAllocation.enabled", "true")
conf.set("spark.dynamicAllocation.minExecutors", "5")
conf.set("spark.dynamicAllocation.maxExecutors", "100")
conf.set("spark.dynamicAllocation.initialExecutors", "10")
```

## Data Formats and Storage

### Format Comparison

| Format | Compression | Schema Evolution | Splittable | Best For |
|--------|-------------|------------------|------------|----------|
| **Parquet** | Excellent | Yes | Yes | Analytics, columnar queries |
| **ORC** | Excellent | Yes | Yes | Hive integration, ACID |
| **Avro** | Good | Yes | Yes | Row-based, schema evolution |
| **JSON** | Poor | Flexible | No | Semi-structured, human-readable |
| **CSV** | Poor | No | Yes | Simple data, legacy systems |
| **Delta Lake** | Excellent | Yes | Yes | ACID, time travel, upserts |

### Recommended Format: Parquet

```python
# Write with compression
df.write.mode("overwrite") \
    .option("compression", "snappy") \
    .partitionBy("year", "month") \
    .parquet("s3://bucket/data/")

# Read with predicate pushdown
df = spark.read.parquet("s3://bucket/data/") \
    .filter("year = 2024 AND month >= 6")
```

### Delta Lake for ACID Transactions

```python
from delta.tables import DeltaTable

# Write Delta table
df.write.format("delta").mode("overwrite").save("/delta/table")

# Upsert (merge)
delta_table = DeltaTable.forPath(spark, "/delta/table")
delta_table.alias("target").merge(
    updates.alias("source"),
    "target.id = source.id"
).whenMatchedUpdateAll() \
 .whenNotMatchedInsertAll() \
 .execute()

# Time travel
df = spark.read.format("delta").option("versionAsOf", 5).load("/delta/table")
df = spark.read.format("delta").option("timestampAsOf", "2024-01-01").load("/delta/table")
```

## Machine Learning with MLlib

### Pipeline Example

```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler, StringIndexer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Feature engineering
indexer = StringIndexer(inputCol="category", outputCol="category_idx")
assembler = VectorAssembler(
    inputCols=["feature1", "feature2", "category_idx"],
    outputCol="features"
)
scaler = StandardScaler(inputCol="features", outputCol="scaled_features")

# Model
rf = RandomForestClassifier(
    featuresCol="scaled_features",
    labelCol="label",
    numTrees=100,
    maxDepth=10
)

# Pipeline
pipeline = Pipeline(stages=[indexer, assembler, scaler, rf])
model = pipeline.fit(train_df)

# Predictions
predictions = model.transform(test_df)

# Evaluation
evaluator = BinaryClassificationEvaluator(labelCol="label", metricName="areaUnderROC")
auc = evaluator.evaluate(predictions)
```

### Distributed Hyperparameter Tuning

```python
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

param_grid = ParamGridBuilder() \
    .addGrid(rf.numTrees, [50, 100, 200]) \
    .addGrid(rf.maxDepth, [5, 10, 15]) \
    .build()

cv = CrossValidator(
    estimator=pipeline,
    estimatorParamMaps=param_grid,
    evaluator=evaluator,
    numFolds=3,
    parallelism=4
)

cv_model = cv.fit(train_df)
best_model = cv_model.bestModel
```

## Production Deployment

### Job Submission

```bash
# Submit to YARN cluster
spark-submit \
  --master yarn \
  --deploy-mode cluster \
  --num-executors 50 \
  --executor-cores 4 \
  --executor-memory 8G \
  --driver-memory 4G \
  --conf spark.sql.shuffle.partitions=400 \
  --conf spark.dynamicAllocation.enabled=true \
  --py-files dependencies.zip \
  --files config.yaml \
  main.py

# Submit to Kubernetes
spark-submit \
  --master k8s://https://k8s-api:6443 \
  --deploy-mode cluster \
  --name spark-job \
  --conf spark.executor.instances=20 \
  --conf spark.kubernetes.container.image=spark:3.5.0 \
  --conf spark.kubernetes.namespace=spark-jobs \
  main.py
```

### Monitoring and Debugging

**Spark UI** — Access at `http://driver:4040` for live jobs
- Jobs, stages, tasks breakdown
- Storage tab for cached data
- Executors tab for resource usage
- SQL tab for query plans

**History Server** — Review completed applications
```bash
spark-submit --conf spark.eventLog.enabled=true \
             --conf spark.eventLog.dir=hdfs://logs/spark
```

**Key Metrics to Monitor:**
- Task duration and skew (identify stragglers)
- Shuffle read/write sizes (optimize shuffles)
- GC time (tune memory if >10% of task time)
- Spill to disk (increase memory or partitions)
- Data locality (PROCESS_LOCAL > NODE_LOCAL > RACK_LOCAL)

### Error Handling

```python
# Graceful error handling in transformations
def safe_transform(row):
    try:
        return process(row)
    except Exception as e:
        return None  # or log error

df.rdd.map(safe_transform).filter(lambda x: x is not None).toDF()

# Checkpoint for fault tolerance
spark.sparkContext.setCheckpointDir("hdfs://checkpoints/")

---

**Note:** This file was automatically condensed to meet the 500-line requirement. Additional content has been moved to the references/ folder.

## Using the Reference Files

- [./references/dataframes-datasets.md](./references/dataframes-datasets.md): Dataframes Datasets
- [./references/optimization-tuning.md](./references/optimization-tuning.md): Optimization Tuning
- [./references/spark-fundamentals.md](./references/spark-fundamentals.md): Spark Fundamentals
- [./references/spark-streaming.md](./references/spark-streaming.md): Spark Streaming

## References

- [Dataframes Datasets](references/dataframes-datasets.md)
- [Optimization Tuning](references/optimization-tuning.md)
- [Spark Fundamentals](references/spark-fundamentals.md)
- [Spark Streaming](references/spark-streaming.md)
