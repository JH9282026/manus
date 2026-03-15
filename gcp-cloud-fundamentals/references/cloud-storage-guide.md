# GCP Cloud Storage Guide

Comprehensive guide to Google Cloud Storage.

---

## Storage Classes

**Standard**: Frequently accessed data
**Nearline**: Once per month access
**Coldline**: Once per quarter access
**Archive**: Once per year access

---

## Lifecycle Management

Automate transitions between storage classes and deletions.

**Example**:
- Move to Nearline after 30 days
- Move to Coldline after 90 days
- Delete after 365 days

---

## Access Control

**Uniform bucket-level access**: IAM only (recommended)
**Fine-grained access**: IAM + ACLs
**Signed URLs**: Time-limited access

---

## Versioning

Enable versioning to protect against accidental deletions and overwrites.

---

## Encryption

**Encryption at rest**: Automatic with Google-managed keys
**Customer-managed keys**: Use Cloud KMS
**Customer-supplied keys**: You manage keys

---

## Best Practices

1. Use appropriate storage class for access patterns
2. Implement lifecycle policies for cost optimization
3. Enable versioning for critical data
4. Use uniform bucket-level access
5. Encrypt sensitive data with customer-managed keys
