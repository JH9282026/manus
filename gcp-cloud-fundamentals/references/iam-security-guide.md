# GCP IAM and Security Guide

Comprehensive guide to GCP IAM and security.

---

## IAM Fundamentals

**Who**: User, service account, group
**Can do what**: Role (collection of permissions)
**On which resource**: Project, folder, organization

---

## Roles

**Primitive roles**: Owner, Editor, Viewer (avoid in production)
**Predefined roles**: Service-specific, curated by Google
**Custom roles**: Fine-grained, user-defined

---

## Service Accounts

**Purpose**: Identity for applications and VMs

**Types**:
- User-managed
- Default service accounts
- Google-managed

**Best practices**:
- Use service accounts for applications
- Grant minimum necessary permissions
- Rotate keys regularly
- Use Workload Identity for GKE

---

## IAM Policies

**Binding**: Associates members with roles

**Conditions**: Context-aware access control

**Organization policies**: Constraints across organization

---

## Security Best Practices

1. Use predefined roles instead of primitive roles
2. Grant roles at smallest scope necessary
3. Use service accounts for applications
4. Enable audit logging
5. Implement organization policies
6. Use VPC Service Controls for data exfiltration protection
7. Enable Security Command Center
8. Implement least privilege principle
9. Regular access reviews
10. Use Cloud KMS for encryption key management
