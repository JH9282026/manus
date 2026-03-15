# Docker Production Deployment Guide

Best practices for deploying Docker containers in production.

---

## Health Checks

**Dockerfile**:
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost/health || exit 1
```

**Docker Compose**:
```yaml
services:
  web:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 3s
      retries: 3
```

---

## Resource Limits

```yaml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M
```

---

## Restart Policies

```yaml
services:
  web:
    restart: unless-stopped  # or always, on-failure, no
```

---

## Logging

**Configure logging driver**:
```yaml
services:
  web:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

**Log drivers**: json-file, syslog, journald, gelf, fluentd

---

## Security

**Run as non-root**:
```dockerfile
USER 1001
```

**Read-only filesystem**:
```yaml
services:
  web:
    read_only: true
    tmpfs:
      - /tmp
```

**Drop capabilities**:
```yaml
services:
  web:
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
```

---

## Secrets Management

**Docker secrets** (Swarm):
```yaml
services:
  web:
    secrets:
      - db_password

secrets:
  db_password:
    external: true
```

**Environment variables** (non-Swarm):
- Use .env files (not committed to git)
- Use secret management tools (Vault, AWS Secrets Manager)

---

## Monitoring

**Metrics to monitor**:
- CPU usage
- Memory usage
- Network I/O
- Disk I/O
- Container restarts

**Tools**:
- Prometheus + Grafana
- cAdvisor
- Docker stats
- Cloud provider monitoring

---

## Best Practices Summary

1. Implement health checks
2. Set resource limits
3. Use restart policies
4. Configure logging
5. Run as non-root
6. Use read-only filesystems
7. Manage secrets securely
8. Monitor containers
9. Implement CI/CD
10. Regular security scans
