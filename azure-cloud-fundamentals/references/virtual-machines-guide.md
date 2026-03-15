# Azure Virtual Machines Guide

Comprehensive guide to Azure Virtual Machines (VMs).

---

## VM Basics

### VM Series and Sizes

**General Purpose (B, D, DC series)**:
- B-series: Burstable, cost-effective for variable workloads
- D-series: Balanced CPU-to-memory ratio
- DC-series: Confidential computing with Intel SGX

**Compute Optimized (F series)**:
- High CPU-to-memory ratio
- Batch processing, web servers, analytics

**Memory Optimized (E, M series)**:
- High memory-to-CPU ratio
- Relational databases, in-memory analytics
- M-series: Up to 4 TB RAM

**Storage Optimized (L series)**:
- High disk throughput and IOPS
- NoSQL databases, data warehousing

**GPU (N series)**:
- Graphics rendering, deep learning
- NC, ND, NV series for different GPU workloads

### Sizing Strategy

**Naming convention**: `Standard_D4s_v5`
- Standard: Pricing tier
- D: Series (general purpose)
- 4: vCPUs
- s: Premium storage support
- v5: Generation

**Selection process**:
1. Identify workload requirements (CPU, memory, storage, network)
2. Choose appropriate series
3. Select size based on performance needs
4. Monitor and adjust based on actual usage

---

## Availability and Scalability

### Availability Sets

**Purpose**: Protect against hardware failures within a datacenter

**Concepts**:
- **Fault Domains**: Physical server racks (max 3)
- **Update Domains**: Logical groups for planned maintenance (max 20)

**SLA**: 99.95% for VMs in availability set

**Use when**: Single-region deployment, need protection from hardware failures

### Availability Zones

**Purpose**: Protect against datacenter failures

**Characteristics**:
- Physically separate datacenters within region
- Independent power, cooling, networking
- Minimum 3 zones per enabled region

**SLA**: 99.99% for VMs across zones

**Use when**: Need highest availability, can tolerate cross-zone latency

### Virtual Machine Scale Sets (VMSS)

**Features**:
- Auto-scaling based on metrics or schedule
- Load balancer integration
- Automatic OS updates
- Up to 1,000 VM instances (3,000 with single placement group disabled)

**Scaling policies**:
- Metric-based (CPU, memory, custom metrics)
- Schedule-based (business hours, known traffic patterns)
- Manual scaling

**Use cases**:
- Web applications with variable traffic
- Batch processing
- Microservices
- Containerized applications

---

## Storage Configuration

### Managed Disks

**Types**:

| Type | IOPS | Throughput | Use Case |
|------|------|------------|----------|
| **Ultra Disk** | 160,000 | 4,000 MB/s | IO-intensive workloads |
| **Premium SSD v2** | 80,000 | 1,200 MB/s | Production workloads |
| **Premium SSD** | 20,000 | 900 MB/s | Production, latency-sensitive |
| **Standard SSD** | 6,000 | 750 MB/s | Web servers, dev/test |
| **Standard HDD** | 2,000 | 500 MB/s | Backup, non-critical |

**Best practices**:
- Use Premium SSD for production workloads
- Enable host caching for read-heavy workloads
- Use separate disks for OS and data
- Implement disk encryption
- Take regular snapshots

### Disk Caching

**Options**:
- **None**: No caching (write-heavy workloads)
- **ReadOnly**: Cache reads (read-heavy workloads)
- **ReadWrite**: Cache reads and writes (general purpose)

**Recommendations**:
- OS disk: ReadWrite
- Data disk (database): None or ReadOnly
- Data disk (general): ReadWrite

---

## Networking

### Network Interfaces

**Features**:
- Multiple NICs per VM (size-dependent)
- Accelerated networking (SR-IOV)
- Public and private IP addresses
- NSG association

**Accelerated Networking**:
- Up to 30 Gbps network throughput
- Lower latency and jitter
- Reduced CPU utilization
- Enable for network-intensive workloads

### Load Balancing

**Azure Load Balancer**:
- Layer 4 (TCP/UDP)
- Public and internal load balancers
- Health probes
- Outbound rules for SNAT

**Application Gateway**:
- Layer 7 (HTTP/HTTPS)
- URL-based routing
- SSL termination
- Web Application Firewall (WAF)
- Autoscaling

---

## Security

### Azure Disk Encryption

**Features**:
- BitLocker (Windows) or dm-crypt (Linux)
- Encryption keys in Azure Key Vault
- Encrypt OS and data disks

**Implementation**:
```bash
az vm encryption enable \
  --resource-group myResourceGroup \
  --name myVM \
  --disk-encryption-keyvault myKeyVault
```

### Network Security

**Network Security Groups (NSGs)**:
- Inbound and outbound rules
- Priority-based evaluation (100-4096)
- Allow or deny traffic
- Associate with subnet or NIC

**Example rules**:
- Allow SSH from specific IP: Priority 100
- Allow HTTP from internet: Priority 110
- Deny all inbound: Priority 4096 (default)

### Azure Bastion

**Purpose**: Secure RDP/SSH access without public IPs

**Benefits**:
- No need for public IPs on VMs
- Protection against port scanning
- Integrated with Azure Portal
- No client software required

---

## Monitoring and Diagnostics

### Boot Diagnostics

**Features**:
- Screenshot of VM console
- Serial console access
- Troubleshoot boot issues

**Enable**:
```bash
az vm boot-diagnostics enable \
  --resource-group myResourceGroup \
  --name myVM \
  --storage https://mystorageaccount.blob.core.windows.net/
```

### Azure Monitor

**VM Insights**:
- Performance monitoring
- Dependency mapping
- Health diagnostics
- Log Analytics integration

**Metrics**:
- CPU percentage
- Network in/out
- Disk read/write operations
- Available memory (requires agent)

### Diagnostic Extension

**Collects**:
- Performance counters
- Event logs
- Crash dumps
- Application logs

**Sends to**:
- Azure Storage
- Event Hubs
- Application Insights

---

## Cost Optimization

### Reserved Instances

**Savings**: Up to 72% vs pay-as-you-go

**Terms**: 1-year or 3-year

**Flexibility**:
- Instance size flexibility within series
- Region flexibility (with some restrictions)
- Can exchange or cancel (with fees)

### Spot VMs

**Savings**: Up to 90% vs pay-as-you-go

**Characteristics**:
- Can be evicted with 30-second notice
- Eviction policies: Deallocate or Delete
- Max price setting

**Use cases**:
- Batch processing
- Dev/test environments
- Stateless workloads
- Fault-tolerant applications

### Azure Hybrid Benefit

**Savings**: Up to 85% on Windows VMs, up to 40% on SQL Server

**Requirements**:
- Active Software Assurance
- Windows Server or SQL Server licenses

**Applies to**:
- Windows Server VMs
- SQL Server on VMs
- Azure SQL Database

---

## Automation

### Azure CLI

**Common commands**:
```bash
# Create VM
az vm create \
  --resource-group myResourceGroup \
  --name myVM \
  --image UbuntuLTS \
  --size Standard_D2s_v3 \
  --admin-username azureuser \
  --generate-ssh-keys

# Start/Stop VM
az vm start --resource-group myResourceGroup --name myVM
az vm stop --resource-group myResourceGroup --name myVM

# Resize VM
az vm resize \
  --resource-group myResourceGroup \
  --name myVM \
  --size Standard_D4s_v3
```

### PowerShell

**Common cmdlets**:
```powershell
# Create VM
New-AzVM `
  -ResourceGroupName "myResourceGroup" `
  -Name "myVM" `
  -Location "East US" `
  -Size "Standard_D2s_v3" `
  -Image "Win2019Datacenter"

# Get VM status
Get-AzVM -ResourceGroupName "myResourceGroup" -Name "myVM" -Status

# Update VM
Update-AzVM -ResourceGroupName "myResourceGroup" -VM $vm
```

### Custom Script Extension

**Purpose**: Run scripts on VMs during or after deployment

**Use cases**:
- Install software
- Configure applications
- Join domain
- Download files

**Example**:
```bash
az vm extension set \
  --resource-group myResourceGroup \
  --vm-name myVM \
  --name customScript \
  --publisher Microsoft.Azure.Extensions \
  --settings '{"fileUris": ["https://example.com/script.sh"],"commandToExecute": "./script.sh"}'
```

---

## Backup and Disaster Recovery

### Azure Backup

**Features**:
- Application-consistent backups
- Incremental backups
- Long-term retention
- Encryption at rest and in transit

**Backup policies**:
- Frequency: Daily or weekly
- Retention: Days, weeks, months, years
- Instant restore snapshots

**Recovery**:
- Full VM restore
- File-level restore
- Cross-region restore

### Azure Site Recovery

**Capabilities**:
- VM replication to secondary region
- Orchestrated failover and failback
- Recovery plans with automation
- Test failover without impact

**RPO**: Typically 5 minutes

**RTO**: Depends on recovery plan, typically < 2 hours

---

## Best Practices Summary

1. **Use managed disks** for all VMs
2. **Enable accelerated networking** for network-intensive workloads
3. **Implement availability sets or zones** for production workloads
4. **Use Azure Bastion** instead of public IPs for management
5. **Enable disk encryption** for sensitive data
6. **Implement auto-scaling** for variable workloads
7. **Use Reserved Instances** for predictable workloads
8. **Enable Azure Backup** for all production VMs
9. **Monitor with Azure Monitor** and set up alerts
10. **Tag all resources** for cost allocation and management
