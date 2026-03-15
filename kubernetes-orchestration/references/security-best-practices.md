# Kubernetes Security Best Practices

## RBAC
- Least privilege principle
- Use Roles and RoleBindings
- Audit access regularly

## Pod Security
- Run as non-root
- Read-only root filesystem
- Drop unnecessary capabilities
- Use security contexts

## Network Security
- Implement Network Policies
- Use TLS for all communication
- Restrict egress traffic

## Secrets Management
- Use Secrets for sensitive data
- Encrypt Secrets at rest
- Use external secret managers (Vault, etc.)
- Rotate secrets regularly

## Best Practices
1. Enable RBAC
2. Use Pod Security Standards
3. Implement Network Policies
4. Scan images for vulnerabilities
5. Enable audit logging
6. Use namespaces for isolation
7. Limit resource usage
8. Monitor security events
