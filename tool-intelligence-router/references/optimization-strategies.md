# Optimization Strategies

Detailed reference content for tool-intelligence-router.

---

## Appendix D: Performance Benchmarks

### Expected Latency Targets

| Operation | Target Latency | Maximum Acceptable |
|-----------|---------------|-------------------|
| Intent extraction | <20ms | 50ms |
| Category filtering | <10ms | 30ms |
| Semantic similarity search | <30ms | 100ms |
| Multi-criteria scoring (5 tools) | <50ms | 150ms |
| Parameter mapping | <15ms | 50ms |
| Total selection cycle | <150ms | 400ms |

### Scalability Guidelines

| Tool Inventory Size | Indexing Strategy | Expected Selection Time |
|--------------------|-------------------|------------------------|
| <100 tools | In-memory linear scan | <50ms |
| 100-500 tools | In-memory vector index | <100ms |
| 500-2000 tools | Approximate NN (HNSW) | <150ms |
| 2000+ tools | Distributed vector DB | <200ms |

### Cache Configuration Recommendations

```json
{
  "cache_settings": {
    "tool_metadata_ttl_hours": 24,
    "embedding_cache_ttl_hours": 168,
    "selection_result_ttl_minutes": 5,
    "user_preference_cache_ttl_hours": 1,
    "max_cache_size_mb": 512
  }
}
```

---