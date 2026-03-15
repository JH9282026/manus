# IAM Security Guide

Comprehensive guide to AWS Identity and Access Management (IAM).

---

## IAM Fundamentals

### Core Components

**Users**:
- Individual identities for people or applications
- Long-term credentials (password and/or access keys)
- Can belong to multiple groups
- Maximum 5,000 users per AWS account

**Groups**:
- Collections of users
- Attach policies to groups instead of individual users
- Users inherit group permissions
- Cannot nest groups

**Roles**:
- Temporary credentials for services or federated users
- No long-term credentials
- Assumed by users, applications, or AWS services
- Can be assumed cross-account

**Policies**:
- JSON documents defining permissions
- Attached to users, groups, or roles
- Evaluated together to determine final permissions

### Identity vs Resource-Based Policies

**Identity-based policies**:
- Attached to IAM users, groups, or roles
- Define what the identity can do
- Example: User policy allowing S3 access

**Resource-based policies**:
- Attached to resources (S3 buckets, SQS queues, etc.)
- Define who can access the resource
- Example: S3 bucket policy allowing public read

---

## Policy Structure

### JSON Policy Syntax

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadAccess",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-bucket",
        "arn:aws:s3:::my-bucket/*"
      ],
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        }
      }
    }
  ]
}
```

### Policy Elements

**Version**: Policy language version (always use "2012-10-17")

**Statement**: Array of individual permission statements

**Sid**: Optional statement identifier

**Effect**: "Allow" or "Deny"

**Principal**: Who the policy applies to (resource-based policies only)

**Action**: AWS service actions (e.g., "s3:GetObject", "ec2:StartInstances")

**Resource**: ARN of resources the actions apply to

**Condition**: Optional conditions for when policy applies

### Wildcards and Variables

**Wildcards**:
```json
"Action": "s3:*"  // All S3 actions
"Resource": "arn:aws:s3:::my-bucket/*"  // All objects in bucket
```

**Policy Variables**:
```json
"Resource": "arn:aws:s3:::my-bucket/${aws:username}/*"
```

Common variables:
- `${aws:username}`: IAM user name
- `${aws:userid}`: Unique user ID
- `${aws:PrincipalTag/tag-key}`: Tag value from principal

---

## Least Privilege Principle

### Implementation Strategy

1. **Start with minimum permissions**: Begin with no access, add only what's needed
2. **Use AWS managed policies as templates**: Review and customize
3. **Grant permissions incrementally**: Add permissions as requirements emerge
4. **Review regularly**: Remove unused permissions
5. **Use Access Analyzer**: Identify unused permissions

### Permission Boundaries

**Purpose**: Set maximum permissions a user or role can have

**Use cases**:
- Delegate permission management safely
- Prevent privilege escalation
- Enforce organizational standards

**Example**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*",
        "ec2:*",
        "rds:*"
      ],
      "Resource": "*"
    }
  ]
}
```

User can only use services within boundary, even if granted broader permissions.

---

## AWS Managed vs Customer Managed Policies

### AWS Managed Policies

**Characteristics**:
- Created and maintained by AWS
- Automatically updated for new services
- Cannot be modified
- Shared across all AWS accounts

**Common policies**:
- `AdministratorAccess`: Full access to all services
- `PowerUserAccess`: Full access except IAM
- `ReadOnlyAccess`: Read-only access to all services
- `SecurityAudit`: Permissions for security auditing

**Use when**: Policy matches your needs exactly, want automatic updates

### Customer Managed Policies

**Characteristics**:
- Created and maintained by you
- Full control over permissions
- Can version and rollback
- Reusable across users, groups, and roles

**Use when**: Need custom permissions, want version control

### Inline Policies

**Characteristics**:
- Embedded directly in user, group, or role
- 1:1 relationship with identity
- Deleted when identity is deleted

**Use when**: Ensuring permissions are never accidentally attached to wrong identity

---

## Cross-Account Access

### Use Cases

- Centralized logging account
- Shared services (CI/CD, monitoring)
- Third-party access (auditors, vendors)
- Multi-account organization structure

### Implementation

**Account A (Trusting Account)**:
1. Create IAM role with trust policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT-B-ID:root"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

2. Attach permissions policy to role

**Account B (Trusted Account)**:
1. Grant users permission to assume role:
```json
{
  "Effect": "Allow",
  "Action": "sts:AssumeRole",
  "Resource": "arn:aws:iam::ACCOUNT-A-ID:role/CrossAccountRole"
}
```

2. Users assume role:
```bash
aws sts assume-role --role-arn arn:aws:iam::ACCOUNT-A-ID:role/CrossAccountRole --role-session-name session1
```

### External ID for Third-Party Access

**Problem**: Confused deputy problem (third-party could access wrong customer account)

**Solution**: Require external ID in trust policy:
```json
{
  "Condition": {
    "StringEquals": {
      "sts:ExternalId": "unique-external-id-12345"
    }
  }
}
```

---

## Service Roles and Instance Profiles

### EC2 Instance Roles

**Benefits**:
- No need to store credentials on EC2
- Automatic credential rotation
- Temporary credentials via instance metadata

**Setup**:
1. Create IAM role with EC2 trust policy
2. Attach permissions policies
3. Attach role to EC2 instance (at launch or later)

**Access credentials from instance**:
```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE-NAME
```

### Lambda Execution Roles

**Required permissions**:
- CloudWatch Logs (for logging)
- Service-specific permissions (S3, DynamoDB, etc.)

**Example**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

---

## MFA and Security Best Practices

### Multi-Factor Authentication

**Types**:
- Virtual MFA (Google Authenticator, Authy)
- Hardware MFA (YubiKey, Gemalto)
- SMS MFA (not recommended for root)

**Enforce MFA with policy**:
```json
{
  "Effect": "Deny",
  "Action": "*",
  "Resource": "*",
  "Condition": {
    "BoolIfExists": {
      "aws:MultiFactorAuthPresent": "false"
    }
  }
}
```

### Root Account Security

1. **Enable MFA**: Use hardware MFA for maximum security
2. **Delete access keys**: Root should never have programmatic access
3. **Use only for account management**: Billing, account closure, support plan changes
4. **Create admin IAM user**: Use for daily administrative tasks
5. **Secure root email**: Use distribution list, enable MFA on email

### Access Key Management

**Best practices**:
- Rotate access keys regularly (every 90 days)
- Delete unused keys
- Never commit keys to code repositories
- Use IAM roles instead of keys when possible
- Monitor key usage with CloudTrail

**Rotation process**:
1. Create second access key
2. Update applications to use new key
3. Test thoroughly
4. Deactivate old key
5. Monitor for errors
6. Delete old key

---

## IAM Access Analyzer

### Features

**Findings**:
- Resources shared with external entities
- Unused access (permissions granted but never used)
- Public and cross-account access

**Supported resources**:
- S3 buckets
- IAM roles
- KMS keys
- Lambda functions
- SQS queues
- Secrets Manager secrets

### Implementation

1. Enable Access Analyzer in each region
2. Define zone of trust (account or organization)
3. Review findings
4. Archive false positives
5. Remediate actual issues

---

## Policy Evaluation Logic

### Decision Flow

1. **Default Deny**: All requests denied by default
2. **Evaluate all policies**: Identity-based, resource-based, SCPs, permission boundaries
3. **Explicit Deny**: Any explicit deny overrides all allows
4. **Explicit Allow**: If no deny, check for explicit allow
5. **Final Decision**: Allow if explicit allow and no deny, otherwise deny

### Policy Types Priority

1. **Explicit Deny**: Highest priority (cannot be overridden)
2. **Service Control Policies (SCPs)**: Organization-level restrictions
3. **Permission Boundaries**: Maximum permissions for identity
4. **Identity-based policies**: User, group, or role policies
5. **Resource-based policies**: Bucket policies, etc.

---

## Troubleshooting Permissions

### Common Issues

**Access Denied**:
1. Check identity-based policies
2. Check resource-based policies
3. Check SCPs (if using AWS Organizations)
4. Check permission boundaries
5. Verify MFA if required
6. Check IP restrictions in conditions

**Tools**:
- **IAM Policy Simulator**: Test policies before deployment
- **CloudTrail**: Review API calls and errors
- **Access Advisor**: See when services were last accessed
- **Access Analyzer**: Identify unused permissions

### Policy Simulator

**Use cases**:
- Test new policies before attaching
- Troubleshoot access denied errors
- Verify policy changes

**Access**: IAM Console → Policy Simulator or CLI:
```bash
aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::ACCOUNT:user/USERNAME --action-names s3:GetObject --resource-arns arn:aws:s3:::my-bucket/file.txt
```

---

## Compliance and Auditing

### CloudTrail Integration

**Log all IAM actions**:
- User creation/deletion
- Policy changes
- Role assumptions
- Access key usage
- Console sign-ins

**Key events to monitor**:
- Root account usage
- Failed authentication attempts
- Policy modifications
- Unusual API calls

### IAM Credential Report

**Generate report**:
```bash
aws iam generate-credential-report
aws iam get-credential-report
```

**Information included**:
- All users in account
- Password last used
- Access keys and last rotation
- MFA status
- Last activity

**Use for**: Security audits, compliance reporting, identifying inactive users

### Best Practices Summary

1. Enable MFA for all users, especially root and admins
2. Use groups to assign permissions, not individual users
3. Grant least privilege
4. Use IAM roles for applications running on EC2
5. Rotate credentials regularly
6. Remove unnecessary credentials
7. Use policy conditions for extra security
8. Monitor activity with CloudTrail
9. Use Access Analyzer to identify external access
10. Regularly review and remove unused permissions
