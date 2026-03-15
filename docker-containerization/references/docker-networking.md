# Docker Networking Guide

Comprehensive guide to Docker networking.

---

## Network Drivers

**Bridge**: Default, isolated network on single host

**Host**: Container uses host network stack

**None**: No networking

**Overlay**: Multi-host networking (Swarm)

**Macvlan**: Assign MAC address to container

---

## Bridge Networks

**Default bridge**: All containers can communicate

**Custom bridge**: User-defined, DNS resolution

**Create custom bridge**:
```bash
docker network create my-network
```

**Run container on network**:
```bash
docker run --network my-network nginx
```

---

## Service Discovery

**DNS resolution** (custom bridge networks):
```bash
# Container 'web' can reach 'api' at http://api:3000
docker run --name api --network my-net api-image
docker run --name web --network my-net web-image
```

---

## Port Mapping

**Publish ports**:
```bash
docker run -p 8080:80 nginx  # Host:Container
```

**Publish all exposed ports**:
```bash
docker run -P nginx
```

---

## Network Inspection

```bash
docker network ls                    # List networks
docker network inspect my-network    # Inspect network
docker network connect my-net web    # Connect container
docker network disconnect my-net web # Disconnect
```

---

## Best Practices

1. Use custom bridge networks for production
2. Implement network segmentation
3. Use DNS names instead of IP addresses
4. Limit port exposure
5. Use overlay networks for multi-host
6. Implement network policies
7. Monitor network traffic
