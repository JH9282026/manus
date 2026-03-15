# Services and Networking Guide

## Service Types
- ClusterIP: Internal only
- NodePort: Expose on node IP
- LoadBalancer: Cloud LB
- ExternalName: DNS alias

## Ingress
- HTTP/HTTPS routing
- Path and host-based routing
- TLS termination

## Network Policies
- Control Pod-to-Pod traffic
- Namespace isolation
- Egress and ingress rules

## Best Practices
1. Use ClusterIP for internal services
2. Implement Ingress for HTTP/HTTPS
3. Use Network Policies for security
4. Configure DNS properly
