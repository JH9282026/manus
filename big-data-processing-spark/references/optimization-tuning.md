# Optimization and Tuning

Advanced techniques for optimizing Spark applications for performance, cost, and reliability.

## Performance Diagnosis

### Spark UI Analysis

#### Jobs Tab

**Key Metrics:**
- **Duration** — Total job execution time
- **Stages** — Number of stages (fewer is better)
- **Tasks** — Total tasks across all stages

**Red Flags:**
- Long-running jobs (>expected time)
- Many stages (indicates many shuffles)
- Failed tasks (indicates instability)

#### Stages Tab

**Key Metrics:**
- **Duration** — Stage execution time
- **Input** — Data read from source
- **Output** — Data written to sink
- **Shuffle Read** — Data read from shuffle
- **Shuffle Write** — Data written to shuffle

**Red Flags:**
- **High shuffle sizes** — Indicates expensive data movement
- **Task skew** — Some tasks much longer than others
- **Spill to disk** — Memory pressure, need more memory or partitions
- **High GC time** — Memory pressure, tune JVM settings

**Task Metrics:**
```
Task Duration Distribution:
Min: 100ms
25th: 200ms
50th: 250ms
75th: 300ms
Max: 5000ms  ← PROBLEM: Straggler task (data skew)
```

#### Storage Tab

**Key Metrics:**
- **RDD/DataFrame name** — Cached data identifier
- **Storage Level** — Memory, disk, serialized
- **Size in Memory** — Memory consumed
- **Fraction Cached** — Percentage cached (should be 100%)

**Red Flags:**
- **Fraction < 100%** — Not enough memory, data spilling
- **Large cached data** — May not fit in memory, consider uncaching

#### Executors Tab

**Key Metrics:**
- **Active Tasks** — Currently running tasks
- **Failed Tasks** — Task failures (should be 0)
- **Complete Tasks** — Successfully completed tasks
- **Total GC Time** — Time spent in garbage collection
- **Memory Used** — Current memory usage

**Red Flags:**
- **GC time > 10% of task time** — Memory pressure
- **Failed tasks** — Executor instability, OOM errors
- **Uneven task distribution** — Scheduling issues

#### SQL Tab

**Physical Plan:**
```
== Physical Plan ==
*(2) HashAggregate(keys=[category#10], functions=[sum(amount#11)])
+- Exchange hashpartitioning(category#10, 200)  ← Shuffle
   +- *(1) HashAggregate(keys=[category#10], functions=[partial_sum(amount#11)])
      +- *(1) Project [category#10, amount#11]
         +- *(1) Filter isnotnull(amount#11)  ← Predicate pushdown
            +- *(1) FileScan parquet [category#10,amount#11]  ← Column pruning
```

**Look for:**
- **Exchange** — Shuffle operations (minimize these)
- **BroadcastExchange** — Broadcast joins (good for small tables)
- **Filter** — Predicate pushdown (good, filters early)
- **Project** — Column pruning (good, reads only needed columns)

### Common Performance Issues

#### Data Skew

**Symptoms:**
- Few tasks take much longer than others
- Some executors idle while others busy
- OOM errors on specific tasks

**Diagnosis:**
```python
# Check partition sizes
df.rdd.glom().map(len).collect()

# Check key distribution
df.groupBy("key").count().orderBy(F.desc("count")).show()
```

**Solutions:**
```python
# 1. Salting (add random prefix to skewed keys)
df.withColumn("salted_key", 
    F.concat(F.col("key"), F.lit("_"), (F.rand() * 10).cast("int"))
)

# 2. Broadcast join (if one side is small)
df_large.join(broadcast(df_small), "key")

# 3. Adaptive Query Execution (Spark 3.0+)
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
```

#### Excessive Shuffles

**Symptoms:**
- Many Exchange operations in physical plan
- High shuffle read/write sizes
- Long stage durations

**Solutions:**
```python
# 1. Reduce shuffle partitions for small data
spark.conf.set("spark.sql.shuffle.partitions", "50")  # Default 200

# 2. Combine operations to minimize shuffles
# Bad: Multiple shuffles
df.groupBy("key1").count().groupBy("key2").sum("count")

# Good: Single shuffle
df.groupBy("key1", "key2").count()

# 3. Pre-partition data by join keys
df.write.partitionBy("join_key").parquet("output/")
```

#### Memory Pressure

**Symptoms:**
- High GC time (>10% of task time)
- Spill to disk
- OOM errors

**Solutions:**
```python
# 1. Increase executor memory
conf.set("spark.executor.memory", "16g")  # Was 8g

# 2. Increase memory fraction
conf.set("spark.memory.fraction", "0.8")  # Default 0.6

# 3. Use serialized storage
df.persist(StorageLevel.MEMORY_AND_DISK_SER)

# 4. Increase partitions (smaller tasks)
df.repartition(400)

# 5. Uncache unused data
df.unpersist()
```

#### Small Files Problem

**Symptoms:**
- Many small output files
- Slow reads (many file open operations)
- High metadata overhead

**Solutions:**
```python
# 1. Coalesce before writing
df.coalesce(10).write.parquet("output/")

# 2. Repartition by partition columns
df.repartition("date").write.partitionBy("date").parquet("output/")

# 3. Configure max records per file
spark.conf.set("spark.sql.files.maxRecordsPerFile", 1000000)

# 4. Use Delta Lake auto-optimize
df.write.format("delta") \
    .option("optimizeWrite", "true") \
    .save("output/")
```

## Configuration Tuning

### Memory Configuration

#### Executor Memory

```python
# Total executor memory
conf.set("spark.executor.memory", "16g")

# Off-heap memory (for caching)
conf.set("spark.memory.offHeap.enabled", "true")
conf.set("spark.memory.offHeap.size", "4g")

# Memory overhead (for non-JVM memory)
conf.set("spark.executor.memoryOverhead", "2g")  # Or 10% of executor memory
```

**Total Executor Memory = executor.memory + memoryOverhead + offHeap.size**

#### Memory Fractions

```python
# Unified memory (execution + storage)
conf.set("spark.memory.fraction", "0.6")  # Default, 60% of heap

# Storage fraction (of unified memory)
conf.set("spark.memory.storageFraction", "0.5")  # Default, 50% of unified

# Example with 16GB executor memory:
# Unified: 16GB * 0.6 = 9.6GB
# Storage: 9.6GB * 0.5 = 4.8GB
# Execution: 9.6GB * 0.5 = 4.8GB
# User: 16GB * 0.4 = 6.4GB
```

#### Driver Memory

```python
# Driver memory (for collect, broadcast)
conf.set("spark.driver.memory", "4g")

# Driver memory overhead
conf.set("spark.driver.memoryOverhead", "512m")

# Max result size (for collect)
conf.set("spark.driver.maxResultSize", "2g")  # Default 1g
```

### Parallelism Configuration

#### Executor Configuration

```python
# Number of executors
conf.set("spark.executor.instances", "50")

# Cores per executor (4-5 recommended)
conf.set("spark.executor.cores", "5")

# Total parallelism = instances * cores = 50 * 5 = 250
```

**Sizing Guidelines:**
- **Cores per executor:** 4-5 (diminishing returns beyond 5)
- **Memory per executor:** 8-64GB (avoid >64GB due to GC)
- **Executors per node:** Leave 1 core and 1GB for OS

#### Partition Configuration

```python
# Default parallelism (for RDD operations)
conf.set("spark.default.parallelism", "200")

# Shuffle partitions (for DataFrame operations)
conf.set("spark.sql.shuffle.partitions", "200")

# Target partition size
conf.set("spark.sql.files.maxPartitionBytes", "134217728")  # 128MB

# Adaptive Query Execution (Spark 3.0+)
conf.set("spark.sql.adaptive.enabled", "true")
conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
conf.set("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")  # 128MB
```

### Shuffle Configuration

```python
# Shuffle compression
conf.set("spark.shuffle.compress", "true")  # Default
conf.set("spark.shuffle.spill.compress", "true")  # Default

# Shuffle file buffer
conf.set("spark.shuffle.file.buffer", "64k")  # Default 32k, increase for better I/O

# Reducer max size in flight
conf.set("spark.reducer.maxSizeInFlight", "96m")  # Default 48m

# Shuffle service (for dynamic allocation)
conf.set("spark.shuffle.service.enabled", "true")
conf.set("spark.shuffle.service.port", "7337")

# Sort-based shuffle (default)
conf.set("spark.shuffle.manager", "sort")
```

### Serialization Configuration

```python
# Use Kryo serialization (faster than Java)
conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")

# Kryo buffer size
conf.set("spark.kryoserializer.buffer", "64k")  # Default
conf.set("spark.kryoserializer.buffer.max", "512m")  # Default 64m

# Register classes for better performance
conf.set("spark.kryo.registrationRequired", "false")  # Set true for strict mode
```

### I/O Configuration

```python
# Compression codec
conf.set("spark.sql.parquet.compression.codec", "snappy")  # snappy, gzip, lzo, zstd

# Parquet settings
conf.set("spark.sql.parquet.mergeSchema", "false")  # Disable for performance
conf.set("spark.sql.parquet.filterPushdown", "true")  # Enable predicate pushdown

# File source settings
conf.set("spark.sql.files.maxPartitionBytes", "134217728")  # 128MB
conf.set("spark.sql.files.openCostInBytes", "4194304")  # 4MB
```

### Dynamic Allocation

```python
# Enable dynamic allocation
conf.set("spark.dynamicAllocation.enabled", "true")

# Executor limits
conf.set("spark.dynamicAllocation.minExecutors", "5")
conf.set("spark.dynamicAllocation.maxExecutors", "100")
conf.set("spark.dynamicAllocation.initialExecutors", "10")

# Scaling behavior
conf.set("spark.dynamicAllocation.executorIdleTimeout", "60s")
conf.set("spark.dynamicAllocation.cachedExecutorIdleTimeout", "infinity")
conf.set("spark.dynamicAllocation.schedulerBacklogTimeout", "1s")
conf.set("spark.dynamicAllocation.sustainedSchedulerBacklogTimeout", "1s")
```

## Adaptive Query Execution (AQE)

Spark 3.0+ feature for runtime optimization:

```python
# Enable AQE
spark.conf.set("spark.sql.adaptive.enabled", "true")

# Coalesce partitions (reduce shuffle partitions)
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.advisoryPartitionSizeInBytes", "134217728")  # 128MB

# Skew join optimization
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.skewedPartitionFactor", "5")
spark.conf.set("spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes", "268435456")  # 256MB

# Dynamic join strategy
spark.conf.set("spark.sql.adaptive.localShuffleReader.enabled", "true")
```

**Benefits:**
- Automatically reduces shuffle partitions
- Handles data skew in joins
- Converts sort-merge join to broadcast join at runtime
- Optimizes based on runtime statistics

## Advanced Optimization Techniques

### Bucketing

Pre-partition data by join keys:

```python
# Write bucketed table
df.write \
    .bucketBy(100, "user_id") \
    .sortBy("timestamp") \
    .saveAsTable("bucketed_table")

# Read and join (no shuffle needed)
df1 = spark.table("bucketed_table")
df2 = spark.table("another_bucketed_table")
result = df1.join(df2, "user_id")  # No shuffle!
```

**Benefits:**
- Eliminates shuffle for joins on bucketed columns
- Faster aggregations on bucketed columns
- Better data locality

**Considerations:**
- Only works with Hive tables
- Requires same number of buckets for join optimization
- Adds overhead to writes

### Z-Ordering (Delta Lake)

Co-locate related data:

```python
from delta.tables import DeltaTable

# Optimize with Z-ordering
DeltaTable.forPath(spark, "delta/table") \
    .optimize() \
    .executeZOrderBy("user_id", "date")
```

**Benefits:**
- Faster filters on Z-ordered columns
- Better data skipping
- Improved query performance

### Bloom Filters (Delta Lake)

Skip files without matching values:

```python
# Create table with bloom filter
spark.sql("""
    CREATE TABLE users (
        user_id STRING,
        name STRING,
        email STRING
    )
    USING DELTA
    TBLPROPERTIES (
        'delta.bloomFilter.user_id' = 'true',
        'delta.bloomFilter.fpp' = '0.01'
    )
""")
```

**Benefits:**
- Faster point lookups
- Reduced data scanning
- Low overhead

### Partition Pruning

Leverage partitioned data:

```python
# Write partitioned data
df.write.partitionBy("year", "month").parquet("data/")

# Read with partition filter (only reads relevant partitions)
df = spark.read.parquet("data/") \
    .filter("year = 2024 AND month >= 6")
```

**Best Practices:**
- Partition by low-cardinality columns (date, region)
- Avoid over-partitioning (<1000 partitions)
- Target 128MB-1GB per partition
- Use partition filters in queries

### Predicate Pushdown

Push filters to data source:

```python
# Filter pushed to Parquet reader
df = spark.read.parquet("data/") \
    .filter("amount > 1000")  # Only reads matching row groups

# Filter pushed to database
df = spark.read.jdbc(url, "table", properties=props) \
    .filter("status = 'active'")  # Executed as SQL WHERE clause
```

**Supported Sources:**
- Parquet, ORC (row group filtering)
- JDBC (SQL WHERE clause)
- Hive (partition pruning)
- Delta Lake (file skipping)

### Column Pruning

Read only needed columns:

```python
# Only reads 'name' and 'age' columns from Parquet
df = spark.read.parquet("data/").select("name", "age")

# Bad: Reads all columns then selects
df = spark.read.parquet("data/")
df.select("name", "age")  # Still reads all columns!
```

**Best Practice:** Select columns immediately after reading.

## Caching Strategies

### When to Cache

```python
# Good: Reused multiple times
df.cache()
df.filter("status = 'active'").count()
df.filter("status = 'inactive'").count()
df.groupBy("category").count().show()

# Bad: Used only once
df.cache()
df.count()  # Waste of memory
```

### Storage Levels

```python
from pyspark import StorageLevel

# Memory only (fastest, highest memory usage)
df.persist(StorageLevel.MEMORY_ONLY)

# Memory only, serialized (slower, lower memory usage)
df.persist(StorageLevel.MEMORY_ONLY_SER)

# Memory and disk (default for cache())
df.persist(StorageLevel.MEMORY_AND_DISK)

# Memory and disk, serialized (best for large datasets)
df.persist(StorageLevel.MEMORY_AND_DISK_SER)

# Disk only (slowest, no memory usage)
df.persist(StorageLevel.DISK_ONLY)
```

### Cache Management

```python
# Check if cached
spark.catalog.isCached("table_name")

# Uncache specific DataFrame
df.unpersist()

# Clear all cache
spark.catalog.clearCache()

# Refresh cache (if source data changed)
spark.catalog.refreshTable("table_name")
```

## Monitoring and Profiling

### Metrics Collection

```python
# Enable metrics
spark.conf.set("spark.sql.streaming.metricsEnabled", "true")

# Custom metrics
from pyspark import AccumulatorParam

records_processed = spark.sparkContext.accumulator(0)

def process_partition(iterator):
    count = 0
    for record in iterator:
        # Process record
        count += 1
    records_processed.add(count)
    return iterator

df.rdd.mapPartitions(process_partition).count()
print(f"Records processed: {records_processed.value}")
```

### Logging

```python
# Configure logging
log4j = spark.sparkContext._jvm.org.apache.log4j
logger = log4j.LogManager.getLogger(__name__)

logger.info("Starting job")
logger.warn("Potential issue")
logger.error("Error occurred")
```

### Profiling

```python
import time

# Time execution
start = time.time()
df.count()
end = time.time()
print(f"Execution time: {end - start:.2f}s")

# Profile with explain
df.explain("cost")  # Show cost-based optimization
df.explain("formatted")  # Pretty-printed plan
```

## Cost Optimization

### Spot Instances (AWS)

```python
# Use spot instances for executors
conf.set("spark.executor.instances", "50")
conf.set("spark.executor.memory", "8g")
conf.set("spark.executor.cores", "4")

# Configure spot instance behavior
conf.set("spark.dynamicAllocation.enabled", "true")
conf.set("spark.dynamicAllocation.maxExecutors", "100")
```

**Best Practices:**
- Use on-demand for driver
- Use spot for executors
- Enable dynamic allocation
- Set appropriate max executors

### Autoscaling

```python
# Enable autoscaling
conf.set("spark.dynamicAllocation.enabled", "true")
conf.set("spark.dynamicAllocation.minExecutors", "5")
conf.set("spark.dynamicAllocation.maxExecutors", "100")
conf.set("spark.dynamicAllocation.initialExecutors", "10")
```

### Resource Optimization

```python
# Right-size executors
# Bad: Over-provisioned
conf.set("spark.executor.memory", "64g")  # Too much, GC overhead
conf.set("spark.executor.cores", "16")  # Too many, diminishing returns

# Good: Optimal sizing
conf.set("spark.executor.memory", "16g")
conf.set("spark.executor.cores", "5")
```

## Configuration Templates

### Small Job (<100GB)

```python
conf = SparkConf() \
    .set("spark.executor.instances", "10") \
    .set("spark.executor.cores", "4") \
    .set("spark.executor.memory", "8g") \
    .set("spark.sql.shuffle.partitions", "100") \
    .set("spark.default.parallelism", "40")
```

### Medium Job (100GB-1TB)

```python
conf = SparkConf() \
    .set("spark.executor.instances", "50") \
    .set("spark.executor.cores", "5") \
    .set("spark.executor.memory", "16g") \
    .set("spark.sql.shuffle.partitions", "400") \
    .set("spark.default.parallelism", "250") \
    .set("spark.dynamicAllocation.enabled", "true") \
    .set("spark.dynamicAllocation.maxExecutors", "100") \
    .set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
```

### Large Job (>1TB)

```python
conf = SparkConf() \
    .set("spark.executor.instances", "100") \
    .set("spark.executor.cores", "5") \
    .set("spark.executor.memory", "32g") \
    .set("spark.executor.memoryOverhead", "4g") \
    .set("spark.sql.shuffle.partitions", "1000") \
    .set("spark.default.parallelism", "500") \
    .set("spark.dynamicAllocation.enabled", "true") \
    .set("spark.dynamicAllocation.maxExecutors", "200") \
    .set("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .set("spark.sql.adaptive.enabled", "true") \
    .set("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .set("spark.sql.adaptive.skewJoin.enabled", "true") \
    .set("spark.memory.offHeap.enabled", "true") \
    .set("spark.memory.offHeap.size", "8g")
```

## Troubleshooting Guide

### OOM Errors

**Symptoms:** `java.lang.OutOfMemoryError`

**Solutions:**
1. Increase executor memory
2. Increase number of partitions
3. Use serialized storage
4. Reduce cached data
5. Enable off-heap memory

### Slow Jobs

**Symptoms:** Jobs taking longer than expected

**Solutions:**
1. Check for data skew
2. Reduce shuffles
3. Increase parallelism
4. Cache reused data
5. Use broadcast joins

### Task Failures

**Symptoms:** Tasks failing and retrying

**Solutions:**
1. Check executor logs
2. Increase task memory
3. Handle bad data
4. Increase task retry limit
5. Blacklist bad executors

### Shuffle Errors

**Symptoms:** `FetchFailedException`, shuffle read errors

**Solutions:**
1. Increase shuffle timeout
2. Enable shuffle service
3. Reduce shuffle partition size
4. Check network connectivity
5. Increase shuffle retry limit
