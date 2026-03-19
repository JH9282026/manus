# Cassandra Architecture

Distributed architecture and data modeling for Cassandra.

## Consistency Levels

```cql
-- Write consistency
INSERT INTO posts (id, title) VALUES (uuid(), 'Title')
USING CONSISTENCY QUORUM;

-- Read consistency
SELECT * FROM posts WHERE id = ?
USING CONSISTENCY LOCAL_QUORUM;
```

## Data Modeling

```cql
-- Query-first design
CREATE TABLE posts_by_author (
  author_id uuid,
  post_date date,
  post_id timeuuid,
  title text,
  PRIMARY KEY ((author_id, post_date), post_id)
) WITH CLUSTERING ORDER BY (post_id DESC);
```
