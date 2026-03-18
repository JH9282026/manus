# Spark Streaming

Real-time data processing with Spark Structured Streaming for building scalable, fault-tolerant streaming applications.

## Structured Streaming Overview

Structured Streaming is Spark's high-level API for stream processing, treating streams as unbounded tables with continuous queries.

**Key Concepts:**
- **Input Table** — Unbounded table representing streaming data
- **Query** — Operations on input table (same DataFrame API)
- **Result Table** — Output of query, updated continuously
- **Output Mode** — How to write result table to sink
- **Trigger** — When to process new data
- **Checkpoint** — Fault tolerance and exactly-once semantics

**Advantages over DStreams (legacy API):**
- Unified batch and streaming API (same DataFrame code)
- Automatic optimization with Catalyst
- Event-time processing and watermarking
- Exactly-once semantics
- Better performance

## Creating Streaming DataFrames

### From Kafka

```python
# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "topic1,topic2") \
    .option("startingOffsets", "earliest") \
    .load()

# Kafka DataFrame schema
# root
#  |-- key: binary (nullable = true)
#  |-- value: binary (nullable = true)
#  |-- topic: string (nullable = true)
#  |-- partition: integer (nullable = true)
#  |-- offset: long (nullable = true)
#  |-- timestamp: timestamp (nullable = true)
#  |-- timestampType: integer (nullable = true)

# Parse value as JSON
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

schema = StructType([
    StructField("user_id", StringType()),
    StructField("event_type", StringType()),
    StructField("amount", DoubleType()),
    StructField("timestamp", StringType())
])

parsed_df = df.selectExpr("CAST(value AS STRING) as json") \
    .select(F.from_json("json", schema).alias("data")) \
    .select("data.*")
```

**Kafka Options:**
```python
.option("subscribe", "topic1,topic2")  # Subscribe to topics
.option("subscribePattern", "topic.*")  # Pattern matching
.option("assign", '{"topic1":[0,1],"topic2":[2,3]}')  # Specific partitions
.option("startingOffsets", "earliest")  # earliest, latest, or JSON offset spec
.option("endingOffsets", "latest")  # For batch queries
.option("failOnDataLoss", "false")  # Handle topic deletion
.option("maxOffsetsPerTrigger", "10000")  # Rate limiting
.option("minPartitions", "10")  # Minimum Spark partitions
```

### From Files

```python
# Read from directory (new files detected automatically)
df = spark.readStream \
    .format("json") \
    .schema(schema) \
    .option("maxFilesPerTrigger", 10) \
    .load("s3://bucket/input/")

# CSV
df = spark.readStream \
    .format("csv") \
    .schema(schema) \
    .option("header", "true") \
    .load("hdfs://path/to/csv/")

# Parquet
df = spark.readStream \
    .format("parquet") \
    .schema(schema) \
    .load("s3://bucket/parquet/")
```

### From Socket (Testing Only)

```python
# Read from TCP socket (not for production)
df = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()
```

### From Rate Source (Testing)

```python
# Generate test data
df = spark.readStream \
    .format("rate") \
    .option("rowsPerSecond", 100) \
    .option("numPartitions", 10) \
    .load()

# Schema: timestamp (timestamp), value (long)
```

## Stream Processing Operations

### Transformations

Most DataFrame operations work on streaming DataFrames:

```python
# Selection and filtering
df.select("user_id", "amount") \
  .filter("amount > 100")

# Adding columns
df.withColumn("amount_usd", F.col("amount") * 1.1)

# Joins with static data
static_df = spark.read.parquet("s3://bucket/users/")
df.join(static_df, "user_id")

# Stream-stream joins (with watermarking)
df1.join(df2, 
    expr("""
        df1.user_id = df2.user_id AND
        df1.timestamp >= df2.timestamp AND
        df1.timestamp <= df2.timestamp + interval 1 hour
    """))
```

### Aggregations

```python
# Simple aggregation
df.groupBy("user_id").count()

# Multiple aggregations
df.groupBy("user_id").agg(
    F.sum("amount").alias("total_amount"),
    F.avg("amount").alias("avg_amount"),
    F.count("*").alias("transaction_count")
)

# Aggregation with window
df.groupBy(
    F.window("timestamp", "10 minutes"),
    "user_id"
).agg(F.sum("amount"))
```

### Windowing

#### Tumbling Windows

Fixed, non-overlapping time intervals:

```python
# 10-minute tumbling windows
df.groupBy(
    F.window("timestamp", "10 minutes")
).agg(F.sum("amount"))

# Result includes window start and end
# window.start: 2024-01-01 10:00:00
# window.end:   2024-01-01 10:10:00
```

#### Sliding Windows

Overlapping time intervals:

```python
# 10-minute windows, sliding every 5 minutes
df.groupBy(
    F.window("timestamp", "10 minutes", "5 minutes")
).agg(F.sum("amount"))

# Windows:
# 10:00-10:10
# 10:05-10:15
# 10:10-10:20
# ...
```

#### Session Windows

Dynamic windows based on inactivity gaps:

```python
# Session window with 30-minute timeout
df.groupBy(
    F.session_window("timestamp", "30 minutes")
).agg(F.sum("amount"))

# New session starts after 30 minutes of inactivity
```

### Watermarking

Handle late data and limit state size:

```python
# Allow 10 minutes of late data
df.withWatermark("timestamp", "10 minutes") \
  .groupBy(
      F.window("timestamp", "10 minutes"),
      "user_id"
  ).agg(F.sum("amount"))
```

**How Watermarking Works:**
1. Spark tracks maximum event time seen
2. Watermark = max event time - threshold (10 minutes)
3. Data older than watermark is dropped
4. State for windows older than watermark is cleaned up

**Example:**
```
Current time: 10:30
Max event time seen: 10:25
Watermark: 10:25 - 10 minutes = 10:15

Events with timestamp < 10:15 are dropped
Windows ending before 10:15 are finalized and removed from state
```

### Deduplication

```python
# Deduplicate on key
df.dropDuplicates(["user_id", "transaction_id"])

# Deduplicate with watermark (limits state)
df.withWatermark("timestamp", "1 hour") \
  .dropDuplicates(["user_id", "transaction_id"])
```

## Output Modes

### Append Mode

Only new rows added to result table:

```python
query = df.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .start("output/")
```

**Use Cases:**
- Immutable events (logs, clicks)
- No aggregations or only with watermarking
- ETL pipelines

**Restrictions:**
- Cannot use without watermark for aggregations
- Cannot update existing rows

### Complete Mode

Entire result table written every trigger:

```python
query = df.groupBy("category").count() \
    .writeStream \
    .outputMode("complete") \
    .format("memory") \
    .queryName("category_counts") \
    .start()

# Query result table
spark.sql("SELECT * FROM category_counts").show()
```

**Use Cases:**
- Small aggregations (dashboards)
- Real-time analytics
- In-memory sinks

**Restrictions:**
- Only for aggregations
- Result table must fit in memory
- High output volume

### Update Mode

Only updated rows written:

```python
query = df.groupBy("user_id").count() \
    .writeStream \
    .outputMode("update") \
    .format("parquet") \
    .start("output/")
```

**Use Cases:**
- Large aggregations
- Incremental updates
- Upsert to databases

**Restrictions:**
- Only for aggregations
- Requires sink that supports updates (Delta, databases)

## Output Sinks

### File Sink

```python
# Parquet (recommended)
query = df.writeStream \
    .format("parquet") \
    .option("path", "s3://bucket/output/") \
    .option("checkpointLocation", "s3://bucket/checkpoints/") \
    .partitionBy("date") \
    .start()

# JSON
query = df.writeStream \
    .format("json") \
    .option("path", "output/json/") \
    .option("checkpointLocation", "checkpoints/json/") \
    .start()

# CSV
query = df.writeStream \
    .format("csv") \
    .option("path", "output/csv/") \
    .option("checkpointLocation", "checkpoints/csv/") \
    .start()
```

### Kafka Sink

```python
# Write to Kafka
query = df.selectExpr(
    "CAST(user_id AS STRING) AS key",
    "to_json(struct(*)) AS value"
).writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "output_topic") \
    .option("checkpointLocation", "checkpoints/kafka/") \
    .start()
```

### Delta Lake Sink

```python
# Write to Delta table
query = df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "checkpoints/delta/") \
    .start("s3://bucket/delta/table/")

# Upsert with foreachBatch
def upsert_to_delta(batch_df, batch_id):
    batch_df.write \
        .format("delta") \
        .mode("append") \
        .save("s3://bucket/delta/table/")

query = df.writeStream \
    .foreachBatch(upsert_to_delta) \
    .start()
```

### Console Sink (Testing)

```python
# Print to console
query = df.writeStream \
    .format("console") \
    .outputMode("append") \
    .start()
```

### Memory Sink (Testing)

```python
# Write to in-memory table
query = df.writeStream \
    .format("memory") \
    .queryName("my_table") \
    .outputMode("complete") \
    .start()

# Query table
spark.sql("SELECT * FROM my_table").show()
```

### ForeachBatch Sink

Custom logic for each micro-batch:

```python
def process_batch(batch_df, batch_id):
    # Custom processing
    batch_df.write.jdbc(
        url="jdbc:postgresql://host:5432/db",
        table="output_table",
        mode="append",
        properties={"user": "user", "password": "pass"}
    )

query = df.writeStream \
    .foreachBatch(process_batch) \
    .start()
```

**Use Cases:**
- Write to multiple sinks
- Custom transformations per batch
- Complex business logic
- Integration with external systems

### Foreach Sink

Custom logic for each row:

```python
class MyForeachWriter:
    def open(self, partition_id, epoch_id):
        # Initialize connection
        self.connection = create_connection()
        return True
    
    def process(self, row):
        # Process each row
        self.connection.write(row)
    
    def close(self, error):
        # Close connection
        self.connection.close()

query = df.writeStream \
    .foreach(MyForeachWriter()) \
    .start()
```

## Triggers

Control when to process data:

### Default (Micro-batch)

Process as soon as previous batch completes:

```python
query = df.writeStream \
    .start()  # No trigger specified
```

### Fixed Interval

Process every N seconds:

```python
query = df.writeStream \
    .trigger(processingTime="30 seconds") \
    .start()
```

### One-time

Process all available data and stop:

```python
query = df.writeStream \
    .trigger(once=True) \
    .start()

query.awaitTermination()
```

### Available Now

Process all available data in multiple batches:

```python
query = df.writeStream \
    .trigger(availableNow=True) \
    .start()

query.awaitTermination()
```

### Continuous (Experimental)

Low-latency processing (~1ms):

```python
query = df.writeStream \
    .trigger(continuous="1 second") \
    .start()
```

**Note:** Limited operation support, experimental feature.

## Fault Tolerance and Checkpointing

### Checkpointing

Ensures exactly-once semantics:

```python
query = df.writeStream \
    .option("checkpointLocation", "s3://bucket/checkpoints/my_query/") \
    .start("output/")
```

**Checkpoint Contents:**
- Offset tracking (Kafka offsets, file positions)
- State store (aggregation state)
- Metadata (query configuration)

**Best Practices:**
- Use reliable storage (S3, HDFS)
- One checkpoint location per query
- Don't delete checkpoints (breaks recovery)
- Use different checkpoint locations for different queries

### Recovery

Automatic recovery from failures:

1. **Driver failure** — Restart application, reads from checkpoint
2. **Executor failure** — Tasks retried on different executor
3. **Source failure** — Waits for source to recover
4. **Sink failure** — Retries write operation

### Exactly-Once Semantics

Guaranteed by:
- **Replayable sources** — Kafka, files with offsets
- **Idempotent sinks** — Same output for replayed data
- **Checkpointing** — Tracks processed offsets

## Monitoring and Management

### Query Status

```python
# Get query object
query = df.writeStream.start()

# Query ID
query.id

# Query name
query.name

# Is query active?
query.isActive

# Last progress
query.lastProgress

# Recent progress
query.recentProgress

# Status
query.status

# Exception (if failed)
query.exception()
```

### Progress Reporting

```python
# Print progress every trigger
query = df.writeStream \
    .foreachBatch(lambda batch_df, batch_id: 
        print(f"Batch {batch_id}: {batch_df.count()} rows")
    ) \
    .start()

# Access progress programmatically
progress = query.lastProgress
print(f"Input rows: {progress['numInputRows']}")
print(f"Processing time: {progress['durationMs']['triggerExecution']}ms")
```

### Stream Manager

```python
# List active queries
spark.streams.active

# Get query by ID
query = spark.streams.get(query_id)

# Stop all queries
for query in spark.streams.active:
    query.stop()

# Await termination
query.awaitTermination()  # Block until query stops
query.awaitTermination(timeout=60)  # Timeout in seconds
```

### Metrics

```python
# Enable metrics
spark.conf.set("spark.sql.streaming.metricsEnabled", "true")

# Access metrics
progress = query.lastProgress
metrics = {
    "input_rows": progress["numInputRows"],
    "processing_time_ms": progress["durationMs"]["triggerExecution"],
    "input_rate": progress["inputRowsPerSecond"],
    "processing_rate": progress["processedRowsPerSecond"],
    "batch_id": progress["batchId"],
    "timestamp": progress["timestamp"]
}
```

## Advanced Patterns

### Stream-Stream Joins

```python
# Inner join with time constraints
df1.withWatermark("timestamp", "10 minutes") \
   .join(
       df2.withWatermark("timestamp", "10 minutes"),
       expr("""
           df1.user_id = df2.user_id AND
           df1.timestamp >= df2.timestamp AND
           df1.timestamp <= df2.timestamp + interval 5 minutes
       """)
   )

# Left outer join
df1.withWatermark("timestamp", "10 minutes") \
   .join(
       df2.withWatermark("timestamp", "10 minutes"),
       expr("..."),
       "left_outer"
   )
```

### Stateful Operations

```python
from pyspark.sql.streaming import GroupState, GroupStateTimeout

def update_state(key, values, state):
    # Get current state
    current_count = state.get() if state.exists else 0
    
    # Update state
    new_count = current_count + sum(values)
    state.update(new_count)
    
    # Return result
    return (key, new_count)

query = df.groupByKey(lambda x: x.user_id) \
    .mapGroupsWithState(update_state, GroupStateTimeout.NoTimeout) \
    .writeStream \
    .start()
```

### Multiple Queries

```python
# Read once, write to multiple sinks
input_df = spark.readStream.format("kafka").load()

# Query 1: Aggregation to Delta
query1 = input_df.groupBy("category").count() \
    .writeStream \
    .format("delta") \
    .option("checkpointLocation", "checkpoints/query1/") \
    .start("output/aggregated/")

# Query 2: Raw data to Parquet
query2 = input_df.writeStream \
    .format("parquet") \
    .option("checkpointLocation", "checkpoints/query2/") \
    .start("output/raw/")

# Wait for both
spark.streams.awaitAnyTermination()
```

## Performance Tuning

### Shuffle Partitions

```python
# Reduce for low-throughput streams
spark.conf.set("spark.sql.shuffle.partitions", "10")  # Default 200
```

### State Store

```python
# Configure state store
spark.conf.set("spark.sql.streaming.stateStore.providerClass", 
               "org.apache.spark.sql.execution.streaming.state.HDFSBackedStateStoreProvider")
```

### Trigger Interval

```python
# Balance latency vs throughput
query = df.writeStream \
    .trigger(processingTime="10 seconds") \
    .start()
```

### Watermark Tuning

```python
# Shorter watermark = less state, more late data dropped
df.withWatermark("timestamp", "5 minutes")

# Longer watermark = more state, fewer late data dropped
df.withWatermark("timestamp", "1 hour")
```

## Best Practices

1. **Always use checkpointing** — Required for fault tolerance
2. **Set watermarks for aggregations** — Limits state size
3. **Monitor query progress** — Track input rate, processing time
4. **Use appropriate output mode** — Append for events, update for aggregations
5. **Tune shuffle partitions** — Reduce for low-throughput streams
6. **Test with rate source** — Validate logic before production
7. **Handle late data** — Set watermark based on business requirements
8. **Use Delta Lake** — ACID transactions, schema evolution, time travel
9. **Partition output data** — Improves query performance
10. **Monitor state size** — Prevent unbounded state growth
