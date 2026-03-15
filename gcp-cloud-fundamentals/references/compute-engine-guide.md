# GCP Compute Engine Guide

Comprehensive guide to Google Compute Engine.

---

## Machine Types

### Standard Machine Types

**E2**: Cost-optimized, burstable
**N1**: Balanced, older generation
**N2**: Balanced, newer generation
**N2D**: AMD-based, cost-effective

### Specialized Machine Types

**C2/C2D**: Compute-optimized
**M1/M2/M3**: Memory-optimized
**A2**: GPU-optimized

### Custom Machine Types

Create VMs with custom vCPU and memory configurations.

---

## Pricing Models

**On-Demand**: Pay per second, no commitment

**Preemptible**: Up to 80% discount, 24-hour max runtime

**Committed Use**: 1 or 3 years, up to 57% savings

**Sustained Use**: Automatic discounts for running VMs

---

## Instance Management

### Startup Scripts

Automate VM configuration on boot.

### Instance Templates

Reusable VM configurations for instance groups.

### Managed Instance Groups

Auto-scaling, auto-healing, rolling updates.

---

## Storage Options

**Persistent Disk**: Standard, SSD, balanced
**Local SSD**: High performance, ephemeral
**Cloud Storage**: Object storage

---

## Networking

**VPC**: Isolated network
**Firewall Rules**: Control traffic
**Load Balancing**: Distribute traffic

---

## Best Practices

1. Use preemptible VMs for fault-tolerant workloads
2. Implement auto-scaling for variable loads
3. Use committed use discounts for steady workloads
4. Enable OS Login for secure SSH access
5. Use service accounts with minimum permissions
