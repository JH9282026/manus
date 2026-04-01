---
name: kubernetes-orchestration
description: "Master Kubernetes container orchestration including architecture, core resources (Pods, Deployments, Services, ConfigMaps, Secrets), networking, storage, scaling, security with RBAC, and production best practices. Use for: deploying containerized applications, managing Kubernetes clusters, implementing auto-scaling, configuring service discovery, managing persistent storage, implementing security policies, troubleshooting Kubernetes issues, or preparing for CKA/CKAD certifications."
---

# Kubernetes Orchestration

Master Kubernetes for container orchestration, deployment, and management at scale.

## Overview

Kubernetes (K8s) is an open-source container orchestration platform that automates deployment, scaling, and management of containerized applications. This skill covers Kubernetes architecture, core resources (Pods, Deployments, Services), networking, storage, security, and production best practices.

## Kubernetes Architecture

### Control Plane Components

**kube-apiserver**: API server, front-end for control plane

**etcd**: Key-value store for cluster data

**kube-scheduler**: Assigns Pods to Nodes

**kube-controller-manager**: Runs controller processes

**cloud-controller-manager**: Cloud-specific control logic

### Node Components

**kubelet**: Agent running on each node

**kube-proxy**: Network proxy on each node

**Container runtime**: Docker, containerd, CRI-O

## Core Resources

### Pods

**Smallest deployable unit** in Kubernetes

**Characteristics**:
- One or more containers
- Shared network namespace
- Shared storage volumes
- Ephemeral (not self-healing)

**Example**:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
    image: nginx:1.24
    ports:
    - containerPort: 80
```

### Deployments

**Manage ReplicaSets** for declarative updates

**Features**:
- Rolling updates
- Rollback capability
- Scaling
- Self-healing

**Example**:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.24
        ports:
        - containerPort: 80
```

### Services

**Expose applications** running on Pods

**Types**:
- **ClusterIP**: Internal cluster access (default)
- **NodePort**: Expose on each Node's IP
- **LoadBalancer**: Cloud provider load balancer
- **ExternalName**: DNS CNAME record

**Example**:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: LoadBalancer
```

## Configuration Management

### ConfigMaps

**Store non-sensitive configuration**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  database_url: "postgresql://db:5432/myapp"
  log_level: "info"
```

**Use in Pod**:
```yaml
env:
- name: DATABASE_URL
  valueFrom:
    configMapKeyRef:
      name: app-config
      key: database_url
```

### Secrets

**Store sensitive data** (base64 encoded)

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  password: cGFzc3dvcmQxMjM=  # base64 encoded
```

## Storage

### Volumes

**Persistent storage** for Pods

**Types**:
- emptyDir: Temporary, Pod lifetime
- hostPath: Node filesystem
- persistentVolumeClaim: Persistent storage

### PersistentVolumes (PV) and PersistentVolumeClaims (PVC)

**PV**: Cluster-level storage resource

**PVC**: Request for storage by user

**Example**:
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: standard
```

## Networking

### Pod Networking

**Every Pod gets unique IP**

**Pods can communicate** without NAT

**Network policies** control traffic

### Ingress

**HTTP/HTTPS routing** to Services

**Features**:
- Path-based routing
- Host-based routing
- TLS termination
- Load balancing

**Example**:
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
spec:
  rules:
  - host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nginx-service
            port:
              number: 80
```

## Scaling and Auto-Scaling

### Manual Scaling

```bash
kubectl scale deployment nginx-deployment --replicas=5
```

### Horizontal Pod Autoscaler (HPA)

**Auto-scale based on metrics**

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

## Security

### RBAC (Role-Based Access Control)

**Control access** to Kubernetes API

**Components**:
- Role/ClusterRole: Define permissions
- RoleBinding/ClusterRoleBinding: Assign permissions

### Pod Security

**Security contexts**:
- Run as non-root
- Read-only root filesystem
- Drop capabilities

**Example**:
```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  readOnlyRootFilesystem: true
  capabilities:
    drop:
    - ALL
```

## Best Practices

1. Use Deployments, not bare Pods
2. Implement resource requests and limits
3. Use liveness and readiness probes
4. Implement RBAC
5. Use namespaces for isolation
6. Tag images with specific versions
7. Use ConfigMaps and Secrets
8. Implement network policies
9. Monitor with Prometheus and Grafana
10. Use Helm for package management

## Using the Reference Files

**`/references/pods-deployments-guide.md`** — Read when creating Pods, Deployments, or implementing rolling updates.

**`/references/services-networking-guide.md`** — Read when exposing applications, configuring Ingress, or implementing network policies.

**`/references/storage-guide.md`** — Read when implementing persistent storage, configuring volumes, or managing StatefulSets.

**`/references/security-best-practices.md`** — Read when implementing RBAC, securing Pods, or managing secrets.

## References

- [Pods Deployments Guide](references/pods-deployments-guide.md)
- [Security Best Practices](references/security-best-practices.md)
- [Services Networking Guide](references/services-networking-guide.md)
- [Storage Guide](references/storage-guide.md)
