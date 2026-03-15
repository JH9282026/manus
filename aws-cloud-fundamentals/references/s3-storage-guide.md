# S3 Storage Guide

Comprehensive guide to Amazon S3 (Simple Storage Service) object storage.

---

## S3 Fundamentals

### Core Concepts

**Buckets**:
- Containers for objects
- Globally unique names (across all AWS accounts)
- Region-specific (data stays in chosen region)
- Flat structure (no true folders, just key prefixes)

**Objects**:
- Files stored in buckets
- Consist of: Key (name), Value (data), Metadata, Version ID
- Max size: 5 TB per object
- Multipart upload required for objects > 5 GB

**Keys**:
- Unique identifier within bucket
- Can include "/" to simulate folder structure
- Example: `documents/2026/report.pdf`

### Durability and Availability

- **Durability**: 99.999999999% (11 nines) — data loss extremely unlikely
- **Availability**: 99.99% (Standard) — service uptime guarantee
- Data replicated across multiple Availability Zones

---

## Storage Classes

### Comparison Table

| Class | Use Case | Availability | Min Storage | Retrieval |
|-------|----------|--------------|-------------|----------|
| **S3 Standard** | Frequently accessed data | 99.99% | None | Instant |
| **S3 Intelligent-Tiering** | Unknown/changing access | 99.9% | None | Instant |
| **S3 Standard-IA** | Infrequent access | 99.9% | 30 days | Instant |
| **S3 One Zone-IA** | Infrequent, non-critical | 99.5% | 30 days | Instant |
| **S3 Glacier Instant** | Archive, instant retrieval | 99.9% | 90 days | Instant |
| **S3 Glacier Flexible** | Archive, minutes-hours | 99.99% | 90 days | 1-5 min or 3-5 hrs |
| **S3 Glacier Deep Archive** | Long-term archive | 99.99% | 180 days | 12-48 hours |

### Selection Guide

**Use S3 Standard when**:
- Data accessed frequently (multiple times per month)
- Low latency required
- Examples: Active website content, mobile apps, big data analytics

**Use S3 Intelligent-Tiering when**:
- Access patterns unknown or unpredictable
- Want automatic cost optimization
- No retrieval fees

**Use S3 Standard-IA when**:
- Data accessed less than once per month
- Need immediate access when required
- Examples: Backups, disaster recovery, long-term storage

**Use S3 Glacier when**:
- Archival storage with rare access
- Compliance or regulatory requirements
- Examples: Medical records, financial archives, media archives

---

## Lifecycle Policies

### Transition Actions

Automatically move objects between storage classes:

```json
{
  "Rules": [{
    "Id": "Archive old logs",
    "Status": "Enabled",
    "Transitions": [
      {
        "Days": 30,
        "StorageClass": "STANDARD_IA"
      },
      {
        "Days": 90,
        "StorageClass": "GLACIER"
      },
      {
        "Days": 365,
        "StorageClass": "DEEP_ARCHIVE"
      }
    ]
  }]
}
```

### Expiration Actions

Automatically delete objects after specified time:

```json
{
  "Rules": [{
    "Id": "Delete old temp files",
    "Status": "Enabled",
    "Expiration": {
      "Days": 7
    },
    "Filter": {
      "Prefix": "temp/"
    }
  }]
}
```

### Best Practices

- Use lifecycle policies to automate cost optimization
- Transition to IA after 30 days of no access
- Archive to Glacier after 90-180 days
- Delete temporary data automatically
- Use filters to apply policies to specific prefixes or tags

---

## Versioning

### How Versioning Works

**Enabled**:
- Every object modification creates new version
- Previous versions retained
- Each version has unique Version ID
- Protects against accidental deletion and overwrites

**Suspended**:
- New objects get null Version ID
- Existing versions retained
- Can re-enable later

**Disabled** (default):
- Only current version exists
- Cannot enable versioning after suspension without deleting bucket

### Version Management

**Listing versions**:
```bash
aws s3api list-object-versions --bucket my-bucket
```

**Retrieving specific version**:
```bash
aws s3api get-object --bucket my-bucket --key file.txt --version-id <version-id> output.txt
```

**Deleting versions**:
- Delete marker placed on current version (soft delete)
- Specify version ID to permanently delete specific version
- Lifecycle policies can delete old versions automatically

### Cost Considerations

- All versions consume storage (charged for each)
- Use lifecycle policies to delete old versions:
  - `NoncurrentVersionExpiration`: Delete after X days
  - `NoncurrentVersionTransitions`: Move to cheaper storage

---

## Security and Access Control

### Bucket Policies

JSON-based access policies attached to buckets:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "PublicReadGetObject",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::my-bucket/*"
  }]
}
```

**Use for**:
- Grant public access to specific objects
- Cross-account access
- Enforce encryption
- Restrict access by IP address

### IAM Policies

Attached to users, groups, or roles:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "s3:GetObject",
      "s3:PutObject"
    ],
    "Resource": "arn:aws:s3:::my-bucket/user-uploads/*"
  }]
}
```

**Use for**: User-specific or role-specific permissions

### Access Control Lists (ACLs)

**Legacy method** (bucket policies preferred):
- Canned ACLs: private, public-read, public-read-write
- Granular permissions for specific AWS accounts

**Recommendation**: Disable ACLs and use bucket policies instead.

### Block Public Access

**Four settings** (enabled by default for new buckets):
1. Block public access granted through new ACLs
2. Block public access granted through any ACLs
3. Block public access granted through new bucket policies
4. Block public and cross-account access through any bucket policies

**Best Practice**: Keep all enabled unless you specifically need public access.

---

## Encryption

### Server-Side Encryption (SSE)

**SSE-S3** (default):
- AWS-managed keys
- AES-256 encryption
- No additional cost
- Simplest option

**SSE-KMS**:
- AWS Key Management Service
- Customer-managed keys
- Audit trail via CloudTrail
- Additional KMS costs
- Rotation and access control

**SSE-C**:
- Customer-provided keys
- You manage encryption keys
- AWS performs encryption/decryption
- Must provide key with every request

### Client-Side Encryption

- Encrypt data before uploading to S3
- You manage encryption process and keys
- AWS stores encrypted data only
- Use AWS Encryption SDK or third-party tools

### Encryption in Transit

- Use HTTPS endpoints (SSL/TLS)
- Enforce with bucket policy:

```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:*",
  "Resource": "arn:aws:s3:::my-bucket/*",
  "Condition": {
    "Bool": {
      "aws:SecureTransport": "false"
    }
  }
}
```

---

## Static Website Hosting

### Configuration Steps

1. **Enable static website hosting**:
   - Specify index document (e.g., `index.html`)
   - Optional error document (e.g., `404.html`)

2. **Upload website files**:
   ```bash
   aws s3 sync ./website s3://my-bucket/
   ```

3. **Set bucket policy for public read**:
   ```json
   {
     "Effect": "Allow",
     "Principal": "*",
     "Action": "s3:GetObject",
     "Resource": "arn:aws:s3:::my-bucket/*"
   }
   ```

4. **Access website**:
   - URL: `http://my-bucket.s3-website-us-east-1.amazonaws.com`

### Best Practices

- Use CloudFront for HTTPS, custom domain, caching, and global distribution
- Enable versioning for rollback capability
- Use Route 53 for custom domain (e.g., `www.example.com`)
- Compress files (gzip) to reduce transfer costs
- Set appropriate Cache-Control headers

---

## Performance Optimization

### Transfer Acceleration

- Uses CloudFront edge locations for faster uploads
- Optimizes long-distance transfers
- Additional cost per GB transferred
- Enable per bucket

**Use when**: Uploading from geographically distant locations

### Multipart Upload

**Benefits**:
- Required for objects > 5 GB
- Recommended for objects > 100 MB
- Parallel uploads for faster transfer
- Resume failed uploads
- Upload while creating object

**Process**:
1. Initiate multipart upload
2. Upload parts (5 MB to 5 GB each)
3. Complete multipart upload (S3 assembles parts)

### Request Rate Performance

**Limits**:
- 3,500 PUT/COPY/POST/DELETE requests per second per prefix
- 5,500 GET/HEAD requests per second per prefix

**Optimization**:
- Use multiple prefixes to scale horizontally
- Example: Instead of `logs/2026-03-15-001.log`, use `logs/a/2026-03-15-001.log`, `logs/b/2026-03-15-002.log`

### Caching with CloudFront

- Reduce latency for global users
- Reduce load on S3
- Lower data transfer costs (CloudFront cheaper than S3 egress)
- HTTPS support
- Custom domain names

---

## Cost Optimization

### Pricing Components

1. **Storage**: Per GB per month (varies by class)
2. **Requests**: GET, PUT, COPY, POST, LIST
3. **Data Transfer**: Egress to internet (ingress free)
4. **Management**: Lifecycle, analytics, inventory

### Optimization Strategies

1. **Use appropriate storage class**:
   - Standard-IA for infrequent access (50% cheaper storage)
   - Glacier for archives (80%+ cheaper)
   - Intelligent-Tiering for unknown patterns

2. **Implement lifecycle policies**:
   - Automatic transitions to cheaper classes
   - Delete old versions and incomplete multipart uploads

3. **Reduce request costs**:
   - Use CloudFront caching
   - Batch operations when possible
   - Use S3 Select to retrieve subset of data

4. **Optimize data transfer**:
   - Use CloudFront (cheaper egress)
   - Transfer Acceleration for uploads
   - VPC endpoints for free transfer from EC2

5. **Monitor with S3 Storage Lens**:
   - Identify optimization opportunities
   - Track usage trends
   - Analyze access patterns

---

## Advanced Features

### S3 Select and Glacier Select

- Retrieve subset of data using SQL queries
- Reduce data transfer and processing costs
- Up to 400% faster and 80% cheaper than retrieving full object

```sql
SELECT * FROM s3object s WHERE s."Age" > 30
```

### S3 Batch Operations

- Perform operations on billions of objects
- Copy, tag, restore from Glacier, invoke Lambda
- Track progress and generate completion reports

### S3 Object Lock

- Write-once-read-many (WORM) model
- Prevent object deletion or modification
- Compliance and governance modes
- Use for: Regulatory compliance, legal holds

### S3 Replication

**Cross-Region Replication (CRR)**:
- Replicate objects to different region
- Compliance, lower latency, disaster recovery

**Same-Region Replication (SRR)**:
- Replicate within same region
- Aggregate logs, live replication between accounts

**Requirements**:
- Versioning enabled on source and destination
- IAM role with replication permissions
- Can replicate encrypted objects, delete markers, and metadata