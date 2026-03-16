# MongoDB Advanced

Advanced MongoDB queries, aggregations, and optimization.

## Aggregation Pipeline

```javascript
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: {
      _id: "$customer_id",
      total: { $sum: "$amount" },
      count: { $sum: 1 }
  }},
  { $sort: { total: -1 } },
  { $limit: 10 }
])
```

## Indexing Strategies

```javascript
// Compound index
db.posts.createIndex({ author: 1, created_at: -1 })

// Text index
db.posts.createIndex({ title: "text", content: "text" })

// Geospatial index
db.locations.createIndex({ coordinates: "2dsphere" })
```

## Sharding

```javascript
// Enable sharding
sh.enableSharding("mydb")

// Shard collection
sh.shardCollection("mydb.posts", { author_id: 1 })
```
