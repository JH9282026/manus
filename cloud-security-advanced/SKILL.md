---
name: cloud-security-advanced
description: "Master advanced cloud security including IAM, encryption, compliance, and zero-trust architecture. Use for: implementing cloud security best practices, designing IAM policies, managing encryption at rest and in transit, ensuring compliance (SOC2, HIPAA, GDPR), implementing zero-trust architecture, securing cloud infrastructure, threat detection, incident response, and security automation."
---

# Cloud Security Advanced

Master advanced cloud security practices, zero-trust architecture, and compliance frameworks.

## Overview

Cloud security requires a comprehensive approach covering identity and access management, data encryption, network security, compliance, and threat detection. This skill covers advanced security patterns for AWS, Azure, and GCP, with focus on zero-trust principles and automation.

## Security Pillars

| Pillar | Focus | Key Services |
|--------|-------|--------------|
| Identity & Access | Authentication, authorization | IAM, SSO, MFA |
| Data Protection | Encryption, key management | KMS, encryption |
| Infrastructure | Network security, isolation | VPC, security groups |
| Detection | Monitoring, logging | CloudTrail, GuardDuty |
| Incident Response | Automation, remediation | Lambda, Security Hub |
| Compliance | Standards, auditing | Config, Audit Manager |

## IAM Best Practices

### Least Privilege Principle

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-bucket/user-data/${aws:username}/*"
    }
  ]
}
```

### Role-Based Access Control

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "unique-external-id"
        }
      }
    }
  ]
}
```

### Service Control Policies (SCPs)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "ec2:RunInstances"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "ec2:Region": ["us-east-1", "us-west-2"]
        }
      }
    }
  ]
}
```

## Encryption

### At Rest

```python
# S3 Server-Side Encryption
s3.put_object(
    Bucket='my-bucket',
    Key='file.txt',
    Body=data,
    ServerSideEncryption='aws:kms',
    SSEKMSKeyId='arn:aws:kms:region:account:key/key-id'
)

# DynamoDB Encryption
table = dynamodb.create_table(
    TableName='SecureTable',
    SSESpecification={
        'Enabled': True,
        'SSEType': 'KMS',
        'KMSMasterKeyId': 'key-id'
    }
)
```

### In Transit

```python
# Enforce HTTPS
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
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
    ]
}
```

## Network Security

### VPC Design

```yaml
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      EnableDnsSupport: true
  
  PublicSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.1.0/24
      MapPublicIpOnLaunch: true
  
  PrivateSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.2.0/24
  
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Application security group
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0
```

### Zero-Trust Architecture

```python
# Verify every request
def verify_request(event):
    # 1. Verify identity
    token = event['headers'].get('Authorization')
    user = verify_jwt(token)
    
    # 2. Verify device
    device_id = event['headers'].get('X-Device-ID')
    if not is_trusted_device(device_id):
        raise Exception('Untrusted device')
    
    # 3. Verify context
    ip = event['requestContext']['identity']['sourceIp']
    if not is_allowed_ip(ip):
        raise Exception('Unauthorized IP')
    
    # 4. Verify resource access
    if not has_permission(user, event['resource']):
        raise Exception('Insufficient permissions')
    
    return user
```

## Compliance

### SOC 2

- Access controls
- Encryption
- Logging and monitoring
- Incident response
- Change management

### HIPAA

```python
# PHI encryption
def encrypt_phi(data):
    kms = boto3.client('kms')
    response = kms.encrypt(
        KeyId='arn:aws:kms:region:account:key/key-id',
        Plaintext=json.dumps(data)
    )
    return response['CiphertextBlob']

# Audit logging
def log_phi_access(user, resource):
    cloudtrail.log_event({
        'eventName': 'PHIAccess',
        'user': user,
        'resource': resource,
        'timestamp': datetime.now().isoformat()
    })
```

### GDPR

```python
# Data retention
def enforce_retention_policy():
    # Delete data older than retention period
    cutoff_date = datetime.now() - timedelta(days=365)
    
    table.scan(
        FilterExpression='created_at < :cutoff',
        ExpressionAttributeValues={':cutoff': cutoff_date}
    )

# Right to be forgotten
def delete_user_data(user_id):
    # Delete from all systems
    dynamodb.delete_item(Key={'user_id': user_id})
    s3.delete_objects(Prefix=f'users/{user_id}/')
    # Log deletion
    audit_log.record('UserDataDeleted', user_id)
```

## Threat Detection

### GuardDuty Integration

```python
def handle_guardduty_finding(event, context):
    finding = event['detail']
    severity = finding['severity']
    
    if severity >= 7:
        # High severity - immediate action
        isolate_instance(finding['resource']['instanceDetails']['instanceId'])
        notify_security_team(finding)
    elif severity >= 4:
        # Medium severity - investigate
        create_investigation_ticket(finding)
```

### Security Hub

```python
import boto3

securityhub = boto3.client('securityhub')

def report_security_finding(title, description, severity):
    securityhub.batch_import_findings(
        Findings=[{
            'SchemaVersion': '2018-10-08',
            'Id': f'custom-finding-{uuid.uuid4()}',
            'ProductArn': 'arn:aws:securityhub:region:account:product/account/default',
            'GeneratorId': 'custom-scanner',
            'AwsAccountId': 'account-id',
            'Types': ['Software and Configuration Checks'],
            'CreatedAt': datetime.now().isoformat(),
            'UpdatedAt': datetime.now().isoformat(),
            'Severity': {'Label': severity},
            'Title': title,
            'Description': description
        }]
    )
```

## Incident Response

### Automated Remediation

```python
def auto_remediate(event, context):
    finding_type = event['detail']['type']
    
    if finding_type == 'UnauthorizedAccess:EC2/SSHBruteForce':
        # Block IP in security group
        instance_id = event['detail']['resource']['instanceDetails']['instanceId']
        attacker_ip = event['detail']['service']['action']['networkConnectionAction']['remoteIpDetails']['ipAddressV4']
        
        block_ip(instance_id, attacker_ip)
        notify_team(f'Blocked {attacker_ip} due to SSH brute force')
    
    elif finding_type == 'UnauthorizedAccess:IAMUser/MaliciousIPCaller':
        # Disable compromised user
        user_name = event['detail']['resource']['accessKeyDetails']['userName']
        disable_user(user_name)
        rotate_credentials(user_name)
```

## Security Automation

### Config Rules

```python
# Custom Config rule
def evaluate_compliance(event, context):
    config = boto3.client('config')
    
    # Check if S3 buckets have encryption
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    
    evaluations = []
    for bucket in buckets:
        try:
            encryption = s3.get_bucket_encryption(Bucket=bucket['Name'])
            compliance = 'COMPLIANT'
        except:
            compliance = 'NON_COMPLIANT'
        
        evaluations.append({
            'ComplianceResourceType': 'AWS::S3::Bucket',
            'ComplianceResourceId': bucket['Name'],
            'ComplianceType': compliance,
            'OrderingTimestamp': datetime.now()
        })
    
    config.put_evaluations(
        Evaluations=evaluations,
        ResultToken=event['resultToken']
    )
```

## Using the Reference Files

### When to Read Each Reference

**`/references/iam-advanced.md`** — Read when designing complex IAM policies, implementing cross-account access, or managing service roles.

**`/references/compliance-frameworks.md`** — Read when implementing SOC2, HIPAA, GDPR, or other compliance requirements.

**`/references/zero-trust-implementation.md`** — Read when implementing zero-trust architecture, device trust, or context-aware access.
