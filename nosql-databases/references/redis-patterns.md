# Redis Patterns

Common Redis patterns for caching, queues, and real-time data.

## Caching Pattern

```python
def get_with_cache(key, fetch_fn, ttl=300):
    cached = redis.get(key)
    if cached:
        return json.loads(cached)
    
    data = fetch_fn()
    redis.setex(key, ttl, json.dumps(data))
    return data
```

## Distributed Lock

```python
def acquire_lock(lock_name, timeout=10):
    lock_key = f"lock:{lock_name}"
    identifier = str(uuid.uuid4())
    
    if redis.set(lock_key, identifier, nx=True, ex=timeout):
        return identifier
    return None
```

## Rate Limiting

```python
def is_rate_limited(user_id, limit=100, window=60):
    key = f"rate:{user_id}"
    current = redis.incr(key)
    
    if current == 1:
        redis.expire(key, window)
    
    return current > limit
```
