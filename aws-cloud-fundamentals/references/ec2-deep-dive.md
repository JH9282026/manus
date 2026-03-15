# EC2 Deep Dive

Comprehensive guide to Amazon EC2 (Elastic Compute Cloud) virtual servers.

---

## Instance Types and Selection

### Instance Families

**General Purpose (T, M series)**
- **T3/T3a/T4g**: Burstable performance, cost-effective for variable workloads
- **M5/M6i/M7g**: Balanced compute, memory, networking for most applications
- **Use for**: Web servers, development environments, small databases

**Compute Optimized (C series)**
- **C5/C6i/C7g**: High-performance processors
- **Use for**: Batch processing, media transcoding, high-performance web servers, scientific modeling

**Memory Optimized (R, X series)**
- **R5/R6i/R7g**: High memory-to-CPU ratio
- **X1e/X2**: Extreme memory (up to 4 TB RAM)
- **Use for**: In-memory databases, real-time big data analytics, high-performance databases

**Storage Optimized (I, D series)**
- **I3/I4i**: NVMe SSD instance storage, high IOPS
- **D2/D3**: Dense HDD storage
- **Use for**: NoSQL databases, data warehousing, distributed file systems

**Accelerated Computing (P, G, F series)**
- **P3/P4**: GPU instances for machine learning
- **G4/G5**: Graphics-intensive applications
- **F1**: FPGA instances for custom hardware acceleration

### Instance Sizing

**Naming Convention**: `m5.2xlarge`
- **m**: Family (general purpose)
- **5**: Generation
- **2xlarge**: Size (nano, micro, small, medium, large, xlarge, 2xlarge, etc.)

**Sizing Strategy**:
1. Start with a reasonable estimate based on workload
2. Monitor CloudWatch metrics (CPU, memory, network)
3. Right-size after collecting usage data
4. Use AWS Compute Optimizer for recommendations

---

## Storage Options

### EBS (Elastic Block Store)

**Volume Types**:

| Type | IOPS | Throughput | Use Case |
|------|------|------------|----------|
| **gp3** | 3,000-16,000 | 125-1,000 MB/s | General purpose, cost-effective |
| **gp2** | 100-16,000 (burst) | 128-250 MB/s | Legacy general purpose |
| **io2** | 64,000+ | 1,000+ MB/s | Mission-critical, high IOPS |
| **st1** | 500 | 500 MB/s | Throughput-optimized, big data |
| **sc1** | 250 | 250 MB/s | Cold storage, infrequent access |

**Best Practices**:
- Use gp3 for most workloads (better price/performance than gp2)
- Enable encryption by default
- Take regular snapshots for backups
- Delete unused volumes to save costs
- Use lifecycle policies to automate snapshot management

### Instance Store

**Characteristics**:
- Ephemeral storage (data lost on stop/terminate)
- Physically attached to host (very high IOPS)
- No additional cost (included with instance)
- Cannot be detached or attached to another instance

**Use for**: Temporary data, caches, buffers, scratch data

---

## Networking Configuration

### Elastic Network Interfaces (ENI)

**Features**:
- Virtual network card attached to EC2 instance
- Has private IP, optional public IP, Elastic IP
- Can attach multiple ENIs to single instance
- Can move ENI between instances

**Use cases**:
- Create management network separate from data network
- Low-budget high-availability solution
- Licensing tied to MAC address

### IP Addressing

**Private IP**:
- Assigned from VPC subnet range
- Persists for instance lifetime
- Used for internal communication

**Public IP**:
- Assigned from AWS pool
- Changes on stop/start
- Free when instance is running

**Elastic IP**:
- Static public IP you own
- Can reassign to different instances
- Charged when not attached to running instance
- Limited to 5 per region (can request increase)

### Security Groups

**Firewall Rules**:
- Stateful (return traffic automatically allowed)
- Allow rules only (no deny rules)
- Evaluated as a whole (not in order)
- Can reference other security groups

**Best Practices**:
- Use descriptive names and descriptions
- Restrict SSH/RDP to specific IPs (not 0.0.0.0/0)
- Create separate security groups for different tiers (web, app, database)
- Use security group references instead of IP addresses
- Regularly audit and remove unused rules

---

## Auto Scaling

### Auto Scaling Groups (ASG)

**Components**:
1. **Launch Template**: Defines instance configuration (AMI, instance type, security groups)
2. **Scaling Policies**: Rules for when to scale in/out
3. **Health Checks**: EC2 or ELB health checks
4. **Desired/Min/Max Capacity**: Control instance count

**Scaling Policies**:

**Target Tracking**:
- Maintain specific metric (e.g., 50% CPU utilization)
- Simplest to configure
- AWS automatically creates CloudWatch alarms

**Step Scaling**:
- Scale based on CloudWatch alarm thresholds
- Different scaling amounts for different thresholds
- More control than target tracking

**Scheduled Scaling**:
- Scale at specific times (e.g., business hours)
- Predictable traffic patterns

**Predictive Scaling**:
- Uses machine learning to forecast traffic
- Automatically schedules scaling actions

### Load Balancing

**Application Load Balancer (ALB)**:
- Layer 7 (HTTP/HTTPS)
- Path-based and host-based routing
- WebSocket and HTTP/2 support
- Best for web applications

**Network Load Balancer (NLB)**:
- Layer 4 (TCP/UDP)
- Ultra-low latency, millions of requests/second
- Static IP support
- Best for extreme performance

**Gateway Load Balancer (GWLB)**:
- Layer 3 (IP packets)
- Deploy third-party virtual appliances
- Best for firewalls, IDS/IPS

---

## AMI Management

### Amazon Machine Images

**Types**:
- **AWS-provided**: Amazon Linux, Ubuntu, Windows Server
- **Marketplace**: Pre-configured third-party images
- **Community**: User-shared public images
- **Custom**: Your own images

**Creating Custom AMIs**:
1. Launch and configure EC2 instance
2. Install applications and dependencies
3. Create AMI from running or stopped instance
4. AMI includes EBS snapshots of all volumes
5. Launch new instances from AMI

**Best Practices**:
- Automate AMI creation with Packer or EC2 Image Builder
- Tag AMIs with version, date, purpose
- Deregister old AMIs and delete associated snapshots
- Copy AMIs to other regions for disaster recovery
- Encrypt AMIs containing sensitive data

---

## Cost Optimization

### Pricing Models

**On-Demand**:
- Pay per hour/second
- No commitment
- Most expensive
- Use for: Unpredictable workloads, short-term needs

**Reserved Instances (RI)**:
- 1-year or 3-year commitment
- Up to 75% savings
- Standard (specific instance type) or Convertible (can change type)
- Use for: Steady-state workloads

**Savings Plans**:
- 1-year or 3-year commitment to $ amount/hour
- Up to 72% savings
- More flexible than RIs (applies across instance families)
- Use for: Consistent compute usage

**Spot Instances**:
- Bid on unused capacity
- Up to 90% savings
- Can be interrupted with 2-minute warning
- Use for: Fault-tolerant, flexible workloads (batch, big data, CI/CD)

**Dedicated Hosts**:
- Physical server dedicated to your use
- Compliance requirements, licensing
- Most expensive option

### Optimization Strategies

1. **Right-sizing**: Use AWS Compute Optimizer recommendations
2. **Scheduling**: Stop non-production instances outside business hours
3. **Spot for dev/test**: Use Spot Instances for development environments
4. **Reserved capacity**: Purchase RIs or Savings Plans for baseline
5. **Monitor idle resources**: Delete stopped instances, unused EBS volumes
6. **Use newer generations**: Newer instance types offer better price/performance

---

## Monitoring and Troubleshooting

### CloudWatch Metrics

**Default Metrics** (5-minute intervals):
- CPUUtilization
- NetworkIn/NetworkOut
- DiskReadOps/DiskWriteOps
- StatusCheckFailed

**Detailed Monitoring** (1-minute intervals):
- Enable for faster auto-scaling response
- Additional cost

**Custom Metrics**:
- Memory utilization (not included by default)
- Disk space utilization
- Application-specific metrics
- Use CloudWatch Agent to collect

### Status Checks

**System Status Check**:
- AWS infrastructure issues
- Network connectivity, system power, hardware
- Resolution: Stop and start instance (moves to new host)

**Instance Status Check**:
- Instance-level issues
- Failed system checks, incorrect networking, corrupted file system
- Resolution: Reboot instance or modify configuration

### Common Issues

**Cannot connect via SSH/RDP**:
- Check security group allows port 22/3389 from your IP
- Verify instance has public IP or Elastic IP
- Check Network ACL rules
- Verify key pair is correct
- Check instance is running

**Instance immediately terminates**:
- EBS volume limit reached
- EBS snapshot is corrupt
- Root EBS volume is encrypted and you lack KMS permissions
- Instance store-backed AMI missing required part

**Performance issues**:
- Check CloudWatch metrics for bottlenecks
- Verify instance type is appropriate for workload
- Check for CPU credit exhaustion (T-series instances)
- Review disk IOPS and throughput
- Analyze network performance