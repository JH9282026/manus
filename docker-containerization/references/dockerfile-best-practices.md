# Dockerfile Best Practices

Advanced Dockerfile techniques and optimization strategies.

---

## Multi-Stage Builds

Separate build and runtime dependencies for smaller images.

**Example**:
```dockerfile
FROM golang:1.20 AS builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 go build -o app

FROM alpine:3.18
COPY --from=builder /app/app /app
CMD ["/app"]
```

---

## Layer Caching

Order instructions from least to most frequently changing.

**Optimal order**:
1. Base image
2. System dependencies
3. Application dependencies
4. Application code

---

## Security

**Run as non-root**:
```dockerfile
USER 1001
```

**Scan for vulnerabilities**:
```bash
docker scan image:tag
```

**Use trusted base images**:
- Official images
- Verified publishers
- Minimal images (alpine, distroless)

---

## Size Optimization

**Combine RUN commands**:
```dockerfile
RUN apt-get update && \
    apt-get install -y package && \
    rm -rf /var/lib/apt/lists/*
```

**Use .dockerignore**:
```
.git
node_modules
*.md
tests
```

---

## Best Practices Summary

1. Use multi-stage builds
2. Choose minimal base images
3. Pin image versions
4. Run as non-root user
5. Implement health checks
6. Use .dockerignore
7. Combine RUN commands
8. Clean up in same layer
9. Use COPY instead of ADD
10. Set WORKDIR explicitly
