---
name: docker-containerization
description: "Master Docker containerization fundamentals including images, containers, Dockerfiles, Docker Compose, networking, volumes, and best practices for building, deploying, and managing containerized applications. Use for: containerizing applications, creating Docker images, writing Dockerfiles, managing containers, implementing multi-container applications with Docker Compose, optimizing image sizes, implementing container security, or preparing applications for Kubernetes deployment."
---

# Docker Containerization

Master Docker fundamentals for building, deploying, and managing containerized applications.

## Overview

Docker is an open platform for developing, shipping, and running applications in isolated containers. Containers package applications with all dependencies, ensuring consistency across environments. This skill covers Docker images, containers, Dockerfiles, Docker Compose, networking, volumes, and production best practices.

## Docker Fundamentals

### Images vs Containers

**Image**: Read-only template with instructions for creating a container
- Built from Dockerfile
- Layered filesystem
- Immutable
- Stored in registries (Docker Hub, private registries)

**Container**: Runnable instance of an image
- Isolated process
- Has own filesystem, networking, process tree
- Ephemeral by default
- Can be started, stopped, deleted

### Docker Architecture

**Docker Client**: CLI tool (`docker` command)

**Docker Daemon**: Background service managing containers

**Docker Registry**: Stores images (Docker Hub, ECR, GCR, ACR)

**Docker Objects**: Images, containers, networks, volumes

## Dockerfile Best Practices

### Multi-Stage Builds

**Purpose**: Reduce image size by separating build and runtime dependencies

```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY package*.json ./
RUN npm install --production
CMD ["node", "dist/index.js"]
```

**Benefits**: 50-90% smaller images, faster deployments, reduced attack surface

### Base Image Selection

**Prefer minimal images**:
- `alpine`: 5 MB base, minimal packages
- `distroless`: No shell, package manager (Google)
- `scratch`: Empty image for static binaries

**Pin versions**:
```dockerfile
# Bad: Uses latest, unpredictable
FROM node:18

# Good: Specific version
FROM node:18.16.0-alpine3.17

# Better: Use digest for immutability
FROM node:18.16.0-alpine3.17@sha256:abc123...
```

### Layer Optimization

**Order matters** (least to most frequently changing):

```dockerfile
FROM python:3.11-slim

# 1. Install system dependencies (rarely change)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 2. Copy dependency files (change occasionally)
COPY requirements.txt .

# 3. Install dependencies (change occasionally)
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy application code (changes frequently)
COPY . .

CMD ["python", "app.py"]
```

**Benefits**: Faster builds (layer caching), smaller images

### Security Best Practices

**Run as non-root user**:
```dockerfile
FROM node:18-alpine

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Set ownership
COPY --chown=nodejs:nodejs . /app

# Switch to non-root user
USER nodejs

CMD ["node", "index.js"]
```

**Use .dockerignore**:
```
node_modules
.git
.env
*.md
tests
```

## Docker Compose

### Multi-Container Applications

**docker-compose.yml**:
```yaml
version: '3.8'

services:
  web:
    build: ./web
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://db:5432/myapp
    depends_on:
      - db
    networks:
      - app-network

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_PASSWORD=secret
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - app-network

volumes:
  db-data:

networks:
  app-network:
    driver: bridge
```

**Commands**:
```bash
docker-compose up -d          # Start services
docker-compose down           # Stop and remove
docker-compose logs -f web    # View logs
docker-compose exec web sh    # Execute command
```

## Networking

### Network Types

**Bridge** (default): Isolated network for containers on same host

**Host**: Container uses host's network (no isolation)

**None**: No networking

**Custom bridge**: User-defined bridge with DNS resolution

### Creating Networks

```bash
# Create custom network
docker network create my-network

# Run containers on network
docker run -d --name web --network my-network nginx
docker run -d --name api --network my-network node:18

# Containers can communicate via name
# web can reach api at http://api:3000
```

## Volumes and Data Persistence

### Volume Types

**Named volumes**: Managed by Docker, best for persistence
```bash
docker volume create my-data
docker run -v my-data:/app/data myapp
```

**Bind mounts**: Mount host directory into container
```bash
docker run -v /host/path:/container/path myapp
```

**tmpfs mounts**: In-memory, temporary data
```bash
docker run --tmpfs /app/temp myapp
```

### Best Practices

- Use named volumes for production data
- Use bind mounts for development (live code reload)
- Never store data in container filesystem (ephemeral)
- Backup volumes regularly

## Container Management

### Lifecycle Commands

```bash
# Build image
docker build -t myapp:1.0 .

# Run container
docker run -d --name myapp -p 8080:80 myapp:1.0

# View running containers
docker ps

# View logs
docker logs -f myapp

# Execute command in container
docker exec -it myapp sh

# Stop container
docker stop myapp

# Remove container
docker rm myapp

# Remove image
docker rmi myapp:1.0
```

### Resource Limits

```bash
# Limit CPU and memory
docker run -d \
  --cpus="1.5" \
  --memory="512m" \
  --memory-swap="1g" \
  myapp
```

## Image Optimization

### Reduce Image Size

1. **Use multi-stage builds**
2. **Choose minimal base images** (alpine, distroless)
3. **Combine RUN commands** to reduce layers
4. **Remove unnecessary files** in same layer
5. **Use .dockerignore**

**Example**:
```dockerfile
# Combine commands to reduce layers
RUN apt-get update && \
    apt-get install -y package && \
    rm -rf /var/lib/apt/lists/*  # Clean up in same layer
```

### Image Scanning

**Scan for vulnerabilities**:
```bash
docker scan myapp:1.0
```

**Use tools**:
- Docker Scout
- Trivy
- Snyk
- Clair

## Production Best Practices

### Health Checks

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
```

### Logging

**Log to stdout/stderr** (Docker captures):
```dockerfile
# Redirect logs to stdout
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log
```

### Environment Variables

```dockerfile
# Set defaults
ENV NODE_ENV=production
ENV PORT=3000

# Override at runtime
docker run -e NODE_ENV=development myapp
```

## Using the Reference Files

**`/references/dockerfile-best-practices.md`** — Read when writing Dockerfiles, optimizing images, or implementing security best practices.

**`/references/docker-compose-guide.md`** — Read when building multi-container applications, configuring services, or managing development environments.

**`/references/docker-networking.md`** — Read when connecting containers, implementing service discovery, or troubleshooting network issues.

**`/references/production-deployment.md`** — Read when deploying to production, implementing health checks, or optimizing for performance and security.

