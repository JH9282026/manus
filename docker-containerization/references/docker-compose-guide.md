# Docker Compose Guide

Comprehensive guide to Docker Compose for multi-container applications.

---

## Compose File Structure

```yaml
version: '3.8'

services:
  service-name:
    build: ./path
    image: image:tag
    ports:
      - "host:container"
    environment:
      - KEY=value
    volumes:
      - volume-name:/path
    networks:
      - network-name
    depends_on:
      - other-service

volumes:
  volume-name:

networks:
  network-name:
```

---

## Service Configuration

**Build from Dockerfile**:
```yaml
services:
  web:
    build:
      context: ./web
      dockerfile: Dockerfile.prod
      args:
        - NODE_ENV=production
```

**Use existing image**:
```yaml
services:
  db:
    image: postgres:15-alpine
```

---

## Environment Variables

**Inline**:
```yaml
environment:
  - DATABASE_URL=postgresql://db:5432/myapp
```

**From file**:
```yaml
env_file:
  - .env
```

---

## Volumes

**Named volume**:
```yaml
volumes:
  - db-data:/var/lib/postgresql/data
```

**Bind mount**:
```yaml
volumes:
  - ./src:/app/src
```

---

## Networking

**Default**: All services on same network

**Custom networks**:
```yaml
networks:
  frontend:
  backend:

services:
  web:
    networks:
      - frontend
  api:
    networks:
      - frontend
      - backend
  db:
    networks:
      - backend
```

---

## Commands

```bash
docker-compose up -d              # Start
docker-compose down               # Stop and remove
docker-compose ps                 # List services
docker-compose logs -f service    # View logs
docker-compose exec service sh    # Execute command
docker-compose build              # Build images
docker-compose pull               # Pull images
```

---

## Best Practices

1. Use version 3.8 or later
2. Define health checks
3. Use named volumes for data
4. Implement proper networking
5. Use environment files for secrets
6. Define resource limits
7. Use depends_on for startup order
8. Implement restart policies
