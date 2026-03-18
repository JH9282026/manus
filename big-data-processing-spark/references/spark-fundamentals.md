# Spark Fundamentals

Deep dive into Apache Spark architecture, execution model, and core concepts for distributed data processing.

## Spark Architecture Components

### Driver Program

The driver is the process running the main() function of the application and creating the SparkContext. It performs three key functions:

1. **Program Conversion** — Converts user program into tasks
   - Builds logical DAG of operations
   - Optimizes the DAG (e.g., pipelining transformations)
   - Converts DAG into physical execution plan
   - Breaks plan into stages of tasks

2. **Resource Scheduling** — Negotiates with cluster manager
   - Requests executors from cluster manager
   - Monitors executor health and availability
   - Revokes executors when no longer needed (dynamic allocation)

3. **Task Distribution** — Schedules tasks on executors
   - Assigns tasks based on data locality
   - Tracks task completion and failures
   - Retries failed tasks on different executors
   - Collects results from executors

### Executors

Executors are worker processes that run on cluster nodes:

**Responsibilities:**
- Execute tasks assigned by driver
- Store data in memory or disk for caching
- Return computed results to driver
- Provide metrics (memory usage, task duration, etc.)

**Lifecycle:**
- Launched at application start (or dynamically)
- Run for entire application duration (static allocation)
- Can be added/removed dynamically based on workload
- Terminated when application completes

**Configuration:**
```python
# Static allocation
conf.set("spark.executor.instances", "50")
conf.set("spark.executor.cores", "4")
conf.set("spark.executor.memory", "8g")

# Dynamic allocation
conf.set("spark.dynamicAllocation.enabled", "true")
conf.set("spark.dynamicAllocation.minExecutors", "5")
conf.set("spark.dynamicAllocation.maxExecutors", "100")
conf.set("spark.dynamicAllocation.initialExecutors", "10")
conf.set("spark.dynamicAllocation.executorIdleTimeout", "60s")
```

### Cluster Managers

#### YARN (Hadoop)

**Advantages:**
- Mature, production-tested
- Multi-tenancy with resource queues
- Integration with Hadoop ecosystem
- Fine-grained resource management

**Configuration:**
```bash
spark-submit --master yarn \
  --deploy-mode cluster \
  --queue production \
  --num-executors 50 \
  --executor-cores 4 \
  --executor-memory 8G \
  main.py
```

**YARN Modes:**
- **Cluster Mode** — Driver runs on YARN ApplicationMaster (recommended for production)
- **Client Mode** — Driver runs on client machine (useful for interactive sessions)

#### Kubernetes

**Advantages:**
- Cloud-native, containerized
- Auto-scaling and self-healing
- Multi-cloud portability
- Modern DevOps integration

**Configuration:**
```bash
spark-submit --master k8s://https://k8s-api:6443 \
  --deploy-mode cluster \
  --name spark-job \
  --conf spark.executor.instances=20 \
  --conf spark.kubernetes.container.image=spark:3.5.0 \
  --conf spark.kubernetes.namespace=spark-jobs \
  --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
  main.py
```

**Resource Management:**
```python
conf.set("spark.kubernetes.executor.request.cores", "2")
conf.set("spark.kubernetes.executor.limit.cores", "4")
conf.set("spark.kubernetes.executor.request.memory", "4g")
conf.set("spark.kubernetes.executor.limit.memory", "8g")
```

#### Standalone Mode

**Advantages:**
- Simple setup, no external dependencies
- Good for dedicated Spark clusters
- Easy to get started

**Setup:**
```bash
# Start master
./sbin/start-master.sh

# Start workers
./sbin/start-worker.sh spark://master:7077

# Submit job
spark-submit --master spark://master:7077 \
  --executor-memory 8G \
  --total-executor-cores 100 \
  main.py
```

#### Mesos

**Advantages:**
- Fine-grained resource sharing
- Multi-framework support (Spark, Hadoop, etc.)
- Dynamic resource allocation

**Note:** Less commonly used than YARN/Kubernetes in modern deployments.

## Execution Model

### DAG (Directed Acyclic Graph)

Spark builds a DAG of operations before execution:

1. **Logical Plan** — High-level operations (filter, map, join)
2. **Optimized Logical Plan** — Catalyst optimizer applies rules
3. **Physical Plan** — Concrete execution strategy
4. **Execution** — Tasks run on executors

**Example DAG:**
```
TextFile → Map → Filter → ReduceByKey → Collect
         Stage 1         |  Stage 2
                    Shuffle Boundary
```

### Stages and Tasks

**Stage** — Set of tasks that can run in parallel without shuffle
- Bounded by shuffle operations (groupBy, join, repartition)
- All tasks in a stage process different partitions of same data

**Task** — Unit of work sent to one executor
- One task per partition
- Tasks in same stage run in parallel across executors

**Example:**
```python
rdd = sc.textFile("data.txt", 100)  # 100 partitions
rdd.map(lambda x: x.upper()) \
   .filter(lambda x: "ERROR" in x) \
   .groupBy(lambda x: x.split()[0]) \
   .count()

# Stage 1: 100 tasks (map + filter on each partition)
# Shuffle boundary at groupBy
# Stage 2: 200 tasks (default shuffle partitions)
```

### Shuffle Operations

Shuffle redistributes data across partitions, requiring network I/O:

**Shuffle-Triggering Operations:**
- `groupBy`, `groupByKey`, `reduceByKey`, `aggregateByKey`
- `join`, `cogroup`
- `repartition`, `coalesce` (with increase)
- `distinct`, `sortBy`, `sortByKey`
- Window functions with `PARTITION BY`

**Shuffle Process:**
1. **Map Side** — Each task writes shuffle data to local disk
2. **Shuffle Files** — Organized by target partition
3. **Reduce Side** — Tasks fetch data from all map tasks
4. **Combine** — Data combined in memory (or spilled to disk)

**Shuffle Configuration:**
```python
# Number of partitions for shuffle operations
conf.set("spark.sql.shuffle.partitions", "400")  # Default 200

# Shuffle behavior
conf.set("spark.shuffle.compress", "true")  # Compress shuffle data
conf.set("spark.shuffle.spill.compress", "true")  # Compress spilled data
conf.set("spark.shuffle.file.buffer", "64k")  # Buffer size for shuffle writes
conf.set("spark.reducer.maxSizeInFlight", "96m")  # Max data fetched per reduce task

# Shuffle service (for dynamic allocation)
conf.set("spark.shuffle.service.enabled", "true")
conf.set("spark.shuffle.service.port", "7337")
```

### Data Locality

Spark tries to schedule tasks close to data:

**Locality Levels (best to worst):**
1. **PROCESS_LOCAL** — Data in same JVM (cached data)
2. **NODE_LOCAL** — Data on same node (e.g., HDFS block)
3. **RACK_LOCAL** — Data on same rack
4. **ANY** — Data anywhere (requires network transfer)

**Locality Wait:**
```python
# How long to wait for better locality before falling back
conf.set("spark.locality.wait", "3s")  # Default 3s
conf.set("spark.locality.wait.node", "3s")
conf.set("spark.locality.wait.process", "3s")
conf.set("spark.locality.wait.rack", "3s")
```

**Improving Locality:**
- Partition data by keys used in joins
- Cache frequently accessed data
- Use broadcast joins for small tables
- Increase locality wait time (trade latency for locality)

## Memory Management

### Unified Memory Model (Spark 1.6+)

Spark uses a unified memory region for execution and storage:

```
+---------------------------+
|    Reserved Memory        |  300MB (fixed)
+---------------------------+
|                           |
|    User Memory            |  (1 - spark.memory.fraction) * (Heap - Reserved)
|                           |  Default: 40% of heap
+---------------------------+
|                           |
|    Unified Memory         |  spark.memory.fraction * (Heap - Reserved)
|                           |  Default: 60% of heap
|  +---------------------+  |
|  | Storage Memory      |  |  spark.memory.storageFraction * Unified
|  | (Cached data)       |  |  Default: 50% of unified (30% of heap)
|  +---------------------+  |
|  | Execution Memory    |  |  Remaining unified memory
|  | (Shuffles, joins)   |  |  Default: 50% of unified (30% of heap)
|  +---------------------+  |
+---------------------------+
```

**Key Properties:**
```python
conf.set("spark.memory.fraction", "0.6")  # Unified memory as fraction of heap
conf.set("spark.memory.storageFraction", "0.5")  # Storage as fraction of unified
```

**Dynamic Borrowing:**
- Execution can borrow from storage if storage is not fully used
- Storage can borrow from execution if execution is not fully used
- Cached data can be evicted if execution needs memory (LRU policy)
- Execution memory cannot be evicted (will spill to disk instead)

### Storage Levels

```python
from pyspark import StorageLevel

# Memory only (deserialized)
df.persist(StorageLevel.MEMORY_ONLY)  # Fast, high memory usage

# Memory only (serialized)
df.persist(StorageLevel.MEMORY_ONLY_SER)  # Slower, lower memory usage

# Memory and disk (deserialized)
df.persist(StorageLevel.MEMORY_AND_DISK)  # Default for cache()

# Memory and disk (serialized)
df.persist(StorageLevel.MEMORY_AND_DISK_SER)  # Best for large datasets

# Disk only
df.persist(StorageLevel.DISK_ONLY)  # Slowest, no memory usage

# Off-heap (requires spark.memory.offHeap.enabled)
df.persist(StorageLevel.OFF_HEAP)  # Avoids GC overhead
```

**When to Cache:**
- Dataset used multiple times in same application
- Iterative algorithms (ML training)
- Interactive queries on same data
- Expensive transformations reused downstream

**When NOT to Cache:**
- Data used only once
- Data larger than cluster memory
- Simple transformations (cheaper to recompute)

### Off-Heap Memory

Store data outside JVM heap to avoid GC overhead:

```python
conf.set("spark.memory.offHeap.enabled", "true")
conf.set("spark.memory.offHeap.size", "4g")  # Per executor
```

**Advantages:**
- Reduced GC pressure
- More predictable performance
- Can exceed JVM heap limits

**Disadvantages:**
- Serialization overhead
- More complex memory management
- Requires explicit configuration

## Spark Session and Context

### SparkSession (Spark 2.0+)

Unified entry point for Spark functionality:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .master("yarn") \
    .config("spark.executor.memory", "8g") \
    .config("spark.sql.shuffle.partitions", "400") \
    .enableHiveSupport() \
    .getOrCreate()

# Access underlying contexts
sc = spark.sparkContext  # SparkContext for RDDs
sqlContext = spark.sqlContext  # SQLContext (deprecated, use spark directly)
```

### SparkContext (Legacy)

Low-level API for RDD operations:

```python
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("MyApp").setMaster("local[*]")
sc = SparkContext(conf=conf)

# RDD operations
rdd = sc.textFile("data.txt")
result = rdd.map(lambda x: x.upper()).collect()

sc.stop()
```

**Note:** Use SparkSession for new applications. SparkContext is maintained for backward compatibility.

## Deployment Modes

### Local Mode

Runs Spark in single JVM for development/testing:

```python
# Local with 1 thread
spark = SparkSession.builder.master("local").getOrCreate()

# Local with N threads
spark = SparkSession.builder.master("local[4]").getOrCreate()

# Local with all available cores
spark = SparkSession.builder.master("local[*]").getOrCreate()
```

**Use Cases:**
- Development and debugging
- Unit testing
- Small datasets that fit in memory
- Learning Spark

### Client Mode

Driver runs on client machine, executors on cluster:

```bash
spark-submit --master yarn \
  --deploy-mode client \
  --executor-memory 8G \
  --num-executors 50 \
  main.py
```

**Advantages:**
- Interactive feedback (driver output visible)
- Easy debugging
- Good for notebooks (Jupyter, Zeppelin)

**Disadvantages:**
- Client machine must stay connected
- Network latency between client and cluster
- Client becomes bottleneck for large results

### Cluster Mode

Driver runs on cluster worker node:

```bash
spark-submit --master yarn \
  --deploy-mode cluster \
  --executor-memory 8G \
  --num-executors 50 \
  main.py
```

**Advantages:**
- Fully distributed (no client dependency)
- Better for production jobs
- Driver close to executors (low latency)
- Client can disconnect after submission

**Disadvantages:**
- No interactive output (check logs)
- Harder to debug
- Requires log aggregation for monitoring

## Application Lifecycle

### Initialization

1. **Driver starts** — Runs main() function
2. **SparkSession created** — Initializes Spark environment
3. **Cluster manager contacted** — Requests executors
4. **Executors launched** — On worker nodes
5. **Driver registers executors** — Tracks available resources

### Execution

1. **User code runs** — Defines transformations and actions
2. **DAG built** — Logical plan created
3. **DAG optimized** — Catalyst optimizer applies rules
4. **Physical plan generated** — Concrete execution strategy
5. **Stages created** — Divided at shuffle boundaries
6. **Tasks scheduled** — Assigned to executors based on locality
7. **Tasks executed** — On executor JVMs
8. **Results collected** — Sent back to driver

### Termination

1. **Application completes** — All actions finished
2. **Driver stops SparkSession** — `spark.stop()`
3. **Executors terminated** — Resources released
4. **Cluster manager notified** — Application removed

### Fault Tolerance

**Task Failures:**
- Task retried on different executor (up to 4 times by default)
- If task fails 4 times, stage fails
- If stage fails 4 times, job fails

**Executor Failures:**
- Lost executors replaced by cluster manager
- Tasks on lost executor rescheduled
- Cached data on lost executor recomputed

**Driver Failures:**
- Application fails (no automatic recovery)
- Use checkpointing for long-running streaming jobs
- Consider external orchestration (Airflow, Oozie)

**Configuration:**
```python
conf.set("spark.task.maxFailures", "4")  # Task retry limit
conf.set("spark.stage.maxConsecutiveAttempts", "4")  # Stage retry limit
conf.set("spark.blacklist.enabled", "true")  # Blacklist bad executors
```

## Monitoring and Debugging

### Spark UI

Web interface at `http://driver:4040` (increments if port busy):

**Jobs Tab:**
- Active, completed, failed jobs
- Job duration and stage breakdown
- Click job to see stages

**Stages Tab:**
- Stage duration and task metrics
- Task distribution and skew
- Input/output/shuffle sizes
- Click stage to see tasks

**Storage Tab:**
- Cached RDDs/DataFrames
- Memory usage per partition
- Storage level and fraction cached

**Executors Tab:**
- Active executors and resources
- Task metrics per executor
- GC time and memory usage
- Logs and thread dumps

**SQL Tab:**
- DataFrame/SQL query plans
- Physical plan visualization
- Execution time breakdown

### History Server

View completed applications:

```bash
# Enable event logging
spark-submit --conf spark.eventLog.enabled=true \
             --conf spark.eventLog.dir=hdfs://logs/spark \
             main.py

# Start history server
./sbin/start-history-server.sh \
  --properties-file conf/spark-defaults.conf
```

**Configuration:**
```python
conf.set("spark.eventLog.enabled", "true")
conf.set("spark.eventLog.dir", "hdfs://logs/spark")
conf.set("spark.history.fs.logDirectory", "hdfs://logs/spark")
conf.set("spark.history.ui.port", "18080")
```

### Logging

**Configure log4j:**
```properties
# conf/log4j.properties
log4j.rootCategory=WARN, console
log4j.logger.org.apache.spark=INFO
log4j.logger.org.apache.spark.sql=DEBUG
```

**In code:**
```python
log4j = spark.sparkContext._jvm.org.apache.log4j
logger = log4j.LogManager.getLogger(__name__)
logger.info("Starting job")
logger.warn("Potential issue detected")
```

### Metrics

Expose metrics to external systems:

```python
conf.set("spark.metrics.conf", "metrics.properties")
```

**metrics.properties:**
```properties
*.sink.graphite.class=org.apache.spark.metrics.sink.GraphiteSink
*.sink.graphite.host=graphite.example.com
*.sink.graphite.port=2003
*.sink.graphite.period=10
*.sink.graphite.prefix=spark
```

**Supported Sinks:**
- Graphite
- Prometheus
- JMX
- CSV files
- Console

## Best Practices

### Resource Allocation

**Executor Sizing:**
- **Cores per executor:** 4-5 (diminishing returns beyond 5)
- **Memory per executor:** 8-64GB (avoid >64GB due to GC overhead)
- **Executors per node:** Leave 1 core and 1GB for OS/daemons

**Example for 10-node cluster (16 cores, 64GB RAM per node):**
```python
# Leave 1 core and 1GB per node for OS
# Usable: 15 cores, 63GB per node

# Option 1: 3 executors per node, 5 cores each
conf.set("spark.executor.instances", "30")  # 3 * 10 nodes
conf.set("spark.executor.cores", "5")
conf.set("spark.executor.memory", "19g")  # 63GB / 3 executors

# Option 2: 2 executors per node, 7 cores each
conf.set("spark.executor.instances", "20")  # 2 * 10 nodes
conf.set("spark.executor.cores", "7")
conf.set("spark.executor.memory", "28g")  # 63GB / 2 executors
```

### Partition Sizing

**Target:** 128MB - 1GB per partition

**Too few partitions:**
- Underutilized cluster
- Large tasks (memory pressure, long duration)
- Limited parallelism

**Too many partitions:**
- Task scheduling overhead
- Small tasks (inefficient)
- Excessive shuffle files

**Calculation:**
```python
# For 1TB input data, target 128MB partitions
num_partitions = 1024 * 1024 / 128  # 8192 partitions

# For 50 executors with 5 cores each
parallelism = 50 * 5  # 250
num_partitions = parallelism * 2  # 500 (2-3x parallelism)
```

### Configuration Templates

**Small Job (<100GB):**
```python
conf.set("spark.executor.instances", "10")
conf.set("spark.executor.cores", "4")
conf.set("spark.executor.memory", "8g")
conf.set("spark.sql.shuffle.partitions", "100")
```

**Medium Job (100GB-1TB):**
```python
conf.set("spark.executor.instances", "50")
conf.set("spark.executor.cores", "5")
conf.set("spark.executor.memory", "16g")
conf.set("spark.sql.shuffle.partitions", "400")
conf.set("spark.dynamicAllocation.enabled", "true")
```

**Large Job (>1TB):**
```python
conf.set("spark.executor.instances", "100")
conf.set("spark.executor.cores", "5")
conf.set("spark.executor.memory", "32g")
conf.set("spark.sql.shuffle.partitions", "1000")
conf.set("spark.dynamicAllocation.enabled", "true")
conf.set("spark.dynamicAllocation.maxExecutors", "200")
conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
```
