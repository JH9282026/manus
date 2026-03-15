# GCP Networking Guide

Comprehensive guide to GCP networking.

---

## VPC Fundamentals

**Global resource**: Spans all regions
**Subnets**: Regional, can span zones
**Auto mode**: Automatic subnet creation
**Custom mode**: Manual subnet creation (recommended)

---

## Firewall Rules

**Characteristics**:
- Stateful
- Applied to instances via tags or service accounts
- Priority-based (0-65535, lower = higher priority)

**Components**:
- Direction (ingress/egress)
- Priority
- Action (allow/deny)
- Target (tags, service accounts, all instances)
- Source/Destination
- Protocol and ports

---

## Load Balancing

**Global Load Balancers**:
- HTTP(S) Load Balancer
- SSL Proxy Load Balancer
- TCP Proxy Load Balancer

**Regional Load Balancers**:
- Internal TCP/UDP Load Balancer
- Network Load Balancer

---

## Cloud VPN

**Classic VPN**: 99.9% SLA, static routing
**HA VPN**: 99.99% SLA, dynamic routing (recommended)

---

## Cloud Interconnect

**Dedicated Interconnect**: 10 Gbps or 100 Gbps
**Partner Interconnect**: 50 Mbps to 50 Gbps

---

## Best Practices

1. Use custom mode VPCs for production
2. Implement least privilege firewall rules
3. Use service accounts for firewall targets
4. Enable VPC Flow Logs for troubleshooting
5. Use Cloud NAT for private instance internet access
