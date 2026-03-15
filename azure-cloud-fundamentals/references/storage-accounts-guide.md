# Azure Storage Accounts Guide

Comprehensive guide to Azure Storage services.

---

## Storage Account Fundamentals

### Account Types

| Type | Services | Performance | Use Case |
|------|----------|-------------|----------|
| **Standard general-purpose v2** | Blob, File, Queue, Table | Standard | Most scenarios |
| **Premium block blobs** | Blob only | Premium | High transaction rates |
| **Premium file shares** | File only | Premium | Enterprise file shares |
| **Premium page blobs** | Page blobs only | Premium | VM disks |

### Performance Tiers

**Standard**: HDD-backed, lower cost, good for most workloads

**Premium**: SSD-backed, low latency, high throughput, higher cost

### Replication Options

| Option | Copies | Availability | Use Case |
|--------|--------|--------------|----------|
| **LRS** | 3 in single datacenter | 99.999999999% | Cost-sensitive, non-critical |
| **ZRS** | 3 across availability zones | 99.9999999999% | High availability in region |
| **GRS** | 6 (3 primary + 3 secondary region) | 99.99999999999999% | Disaster recovery |
| **GZRS** | 6 (ZRS primary + LRS secondary) | 99.99999999999999% | Maximum availability + DR |
| **RA-GRS** | GRS + read access to secondary | 99.99999999999999% | Read access during outage |
| **RA-GZRS** | GZRS + read access to secondary | 99.99999999999999% | Maximum availability + read DR |

---

## Blob Storage

### Blob Types

**Block Blobs**:
- Optimized for uploading large amounts of data
- Up to 190.7 TiB per blob
- Ideal for documents, media files, backups

**Append Blobs**:
- Optimized for append operations
- Ideal for logging scenarios
- Up to 195 GiB per blob

**Page Blobs**:
- Optimized for random read/write operations
- Up to 8 TiB per blob
- Used for VM disks

### Access Tiers

| Tier | Availability | Storage Cost | Access Cost | Use Case |
|------|--------------|--------------|-------------|----------|
| **Hot** | 99.9% | Highest | Lowest | Frequently accessed |
| **Cool** | 99% | Lower | Higher | Infrequent access, 30+ days |
| **Archive** | N/A (offline) | Lowest | Highest | Rarely accessed, 180+ days |

**Tier transitions**:
- Hot ↔ Cool: Instant
- Hot/Cool → Archive: Instant
- Archive → Hot/Cool: Hours (rehydration required)

### Lifecycle Management

**Automate tier transitions and deletions**:

```json
{
  "rules": [{
    "name": "archiveOldData",
    "type": "Lifecycle",
    "definition": {
      "filters": {
        "blobTypes": ["blockBlob"],
        "prefixMatch": ["logs/"]
      },
      "actions": {
        "baseBlob": {
          "tierToCool": {"daysAfterModificationGreaterThan": 30},
          "tierToArchive": {"daysAfterModificationGreaterThan": 90},
          "delete": {"daysAfterModificationGreaterThan": 365}
        }
      }
    }
  }]
}
```

---

## File Storage

### Azure Files

**Features**:
- SMB 3.0 and NFS 4.1 protocols
- Fully managed file shares
- Concurrent access from cloud and on-premises
- Up to 100 TiB per share (standard), 5 TiB (premium)

**Use cases**:
- Lift-and-shift applications
- Shared application data
- Development and debugging
- Container persistent volumes

### File Sync

**Azure File Sync**:
- Sync on-premises file servers with Azure Files
- Cloud tiering (cache frequently accessed files locally)
- Multi-site sync
- Disaster recovery

**Benefits**:
- Centralize file shares in Azure
- Reduce on-premises storage costs
- Maintain local performance
- Backup and disaster recovery

---

## Queue Storage

### Characteristics

- Message queue for asynchronous communication
- Messages up to 64 KB
- Queue can contain millions of messages
- TTL up to 7 days (infinite with -1)

### Use Cases

- Decouple application components
- Load leveling
- Asynchronous processing
- Communication between web and worker roles

### Operations

**Add message**:
```bash
az storage message put \
  --queue-name myqueue \
  --content "Hello, World!" \
  --account-name mystorageaccount
```

**Get messages**:
```bash
az storage message get \
  --queue-name myqueue \
  --num-messages 10 \
  --account-name mystorageaccount
```

---

## Table Storage

### Characteristics

- NoSQL key-value store
- Schema-less design
- Partition key + row key for indexing
- Up to 500 TiB per table

### Use Cases

- Flexible datasets (user data, device information)
- Web applications requiring flexible schema
- Address books, metadata

### Comparison with Cosmos DB

| Feature | Table Storage | Cosmos DB Table API |
|---------|---------------|---------------------|
| **Latency** | < 10 ms | < 10 ms (99th percentile) |
| **Throughput** | Up to 20,000 ops/sec | Unlimited |
| **Global distribution** | No | Yes |
| **Indexing** | Partition + row key only | All properties |
| **Cost** | Lower | Higher |

**Use Table Storage when**: Cost-sensitive, simple key-value access

**Use Cosmos DB when**: Need global distribution, low latency, complex queries

---

## Security

### Authentication

**Shared Key**: Account name + access key (full access)

**Shared Access Signature (SAS)**:
- Delegated access with specific permissions
- Time-bound
- Can be revoked

**SAS types**:
- **Account SAS**: Access to multiple services
- **Service SAS**: Access to specific service
- **User delegation SAS**: Secured with Azure AD credentials (most secure)

**Azure AD integration**:
- Use Azure AD identities for access
- RBAC for fine-grained permissions
- No need to manage access keys

### Encryption

**Encryption at rest**:
- Automatic with Microsoft-managed keys
- Customer-managed keys in Key Vault
- Infrastructure encryption (double encryption)

**Encryption in transit**:
- HTTPS required by default
- SMB 3.0 encryption for File shares

### Network Security

**Firewalls and virtual networks**:
- Restrict access to specific VNets
- Allow specific public IP ranges
- Service endpoints and private endpoints

**Private endpoints**:
- Access storage over private IP in VNet
- No public internet exposure
- Integrated with Private DNS

---

## Performance Optimization

### Blob Storage Performance

**Partitioning**:
- Partition key is blob name
- Distribute load across multiple partitions
- Use random prefixes for high-throughput scenarios

**Concurrency**:
- Parallel uploads/downloads
- Use Azure Storage SDK for optimal performance
- Adjust block size for large files

**CDN integration**:
- Cache frequently accessed blobs
- Reduce latency for global users
- Lower egress costs

### File Storage Performance

**Premium file shares**:
- Provisioned IOPS and throughput
- Up to 100,000 IOPS per share
- Up to 10 GiB/s throughput

**Standard file shares**:
- Burst IOPS based on share size
- Up to 10,000 IOPS per share
- Up to 300 MiB/s throughput

---

## Cost Optimization

### Strategies

1. **Use appropriate access tier**:
   - Hot for frequently accessed data
   - Cool for infrequent access (30+ days)
   - Archive for long-term storage (180+ days)

2. **Implement lifecycle policies**:
   - Automatic tier transitions
   - Delete old data

3. **Choose right replication**:
   - LRS for non-critical data
   - GRS only when disaster recovery needed

4. **Monitor and optimize**:
   - Use Azure Storage Analytics
   - Identify unused storage
   - Delete old snapshots and versions

5. **Use reserved capacity**:
   - 1-year or 3-year commitment
   - Up to 38% savings on Blob and File storage

---

## Monitoring and Diagnostics

### Storage Analytics

**Metrics**:
- Capacity metrics (blob storage only)
- Transaction metrics (all services)
- Hourly and minute-level aggregation

**Logs**:
- Authenticated and anonymous requests
- Success and failure details
- Stored in $logs container

### Azure Monitor Integration

**Metrics**:
- Availability
- Latency (E2E and server)
- Transactions
- Ingress/egress

**Alerts**:
- Set thresholds for metrics
- Email, SMS, webhook notifications
- Integration with Action Groups

---

## Best Practices

1. **Use Azure AD authentication** instead of shared keys
2. **Enable soft delete** for blobs and file shares
3. **Implement lifecycle policies** for cost optimization
4. **Use private endpoints** for sensitive data
5. **Enable versioning** for critical data
6. **Monitor with Azure Monitor** and set up alerts
7. **Use SAS tokens** with minimal permissions and short expiration
8. **Enable encryption** with customer-managed keys for compliance
9. **Implement geo-redundancy** for critical data
10. **Tag storage accounts** for cost allocation
