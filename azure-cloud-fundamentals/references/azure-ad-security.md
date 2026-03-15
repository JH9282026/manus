# Azure Active Directory and Security Guide

Comprehensive guide to Azure AD and security best practices.

---

## Azure Active Directory Fundamentals

### What is Azure AD?

**Cloud-based identity and access management service**:
- Authentication and authorization
- Single Sign-On (SSO)
- Multi-Factor Authentication (MFA)
- Conditional Access
- Identity protection

**Differences from Windows Server AD**:
- Cloud-based (not on-premises)
- REST API (not LDAP)
- HTTP/HTTPS (not Kerberos)
- Flat structure (not OU-based)

### Azure AD Editions

| Feature | Free | Premium P1 | Premium P2 |
|---------|------|------------|------------|
| **Users** | 500,000 | Unlimited | Unlimited |
| **SSO** | 10 apps | Unlimited | Unlimited |
| **MFA** | ✓ | ✓ | ✓ |
| **Conditional Access** | ✗ | ✓ | ✓ |
| **Identity Protection** | ✗ | ✗ | ✓ |
| **Privileged Identity Management** | ✗ | ✗ | ✓ |
| **Access Reviews** | ✗ | ✓ | ✓ |

---

## Identity Management

### Users and Groups

**User types**:
- **Cloud identities**: Created in Azure AD
- **Synchronized identities**: Synced from on-premises AD
- **Guest users**: External users (B2B)

**Group types**:
- **Security groups**: Manage access to resources
- **Microsoft 365 groups**: Collaboration (mailbox, SharePoint, Teams)

**Group assignment**:
- **Assigned**: Manually add members
- **Dynamic**: Automatically add based on attributes

**Best practices**:
- Use groups for access management
- Implement naming conventions
- Use dynamic groups for automation
- Regular access reviews

### Administrative Units

**Purpose**: Delegate administration for subset of users/groups

**Use cases**:
- Geographic delegation
- Department-based administration
- Restrict admin scope

---

## Authentication

### Multi-Factor Authentication (MFA)

**Verification methods**:
- Microsoft Authenticator app
- SMS text message
- Voice call
- OATH hardware tokens

**Deployment options**:
- **Per-user MFA**: Enable for specific users
- **Conditional Access**: Context-aware MFA
- **Security defaults**: MFA for all users (recommended for small orgs)

**Best practices**:
- Require MFA for all users
- Use Microsoft Authenticator app (most secure)
- Implement Conditional Access for flexibility
- Exclude emergency access accounts

### Passwordless Authentication

**Methods**:
- **Windows Hello for Business**: Biometric or PIN
- **FIDO2 security keys**: Hardware keys
- **Microsoft Authenticator app**: Phone sign-in

**Benefits**:
- Improved security (no password to steal)
- Better user experience
- Reduced helpdesk costs

### Self-Service Password Reset (SSPR)

**Features**:
- Users reset own passwords
- Reduce helpdesk calls
- Configurable authentication methods
- Password writeback to on-premises AD

**Requirements**:
- Azure AD Premium P1 or P2
- Licensed users
- Registered authentication methods

---

## Authorization

### Role-Based Access Control (RBAC)

**Built-in roles**:
- **Owner**: Full access including access management
- **Contributor**: Full access except access management
- **Reader**: View all resources
- **User Access Administrator**: Manage user access

**Scope levels**:
- Management group
- Subscription
- Resource group
- Resource

**Custom roles**:
- Define specific permissions
- JSON-based definition
- Reusable across scopes

**Best practices**:
- Use built-in roles when possible
- Assign roles at appropriate scope
- Use groups for role assignments
- Regular access reviews
- Principle of least privilege

### Privileged Identity Management (PIM)

**Features**:
- Just-in-time privileged access
- Time-bound access
- Approval workflows
- Access reviews
- Audit logs

**Use cases**:
- Reduce standing admin access
- Require justification for elevation
- Implement approval process
- Audit privileged access

**Eligible vs Active**:
- **Eligible**: Can activate role when needed
- **Active**: Role is always active

---

## Conditional Access

### How It Works

**Signal → Decision → Enforcement**

**Signals**:
- User or group membership
- IP location
- Device platform
- Application
- Real-time risk detection

**Decisions**:
- Allow access
- Block access
- Grant access with conditions

**Enforcement**:
- Require MFA
- Require compliant device
- Require hybrid Azure AD joined device
- Require approved client app
- Require app protection policy

### Common Policies

**Require MFA for admins**:
- Signal: Admin roles
- Decision: Grant access
- Enforcement: Require MFA

**Block legacy authentication**:
- Signal: Legacy authentication protocols
- Decision: Block access

**Require compliant device**:
- Signal: All users
- Decision: Grant access
- Enforcement: Require device compliance

**Risk-based access**:
- Signal: Sign-in risk or user risk
- Decision: Grant access
- Enforcement: Require MFA or password change

### Best Practices

1. Start with report-only mode
2. Test with pilot group
3. Exclude emergency access accounts
4. Implement baseline policies first
5. Monitor sign-in logs
6. Use named locations for trusted IPs

---

## Identity Protection

### Risk Detections

**Sign-in risks**:
- Atypical travel
- Anonymous IP address
- Malware-linked IP address
- Unfamiliar sign-in properties
- Password spray
- Azure AD threat intelligence

**User risks**:
- Leaked credentials
- Azure AD threat intelligence

### Risk-Based Policies

**Sign-in risk policy**:
- Low, medium, high risk thresholds
- Require MFA for medium/high risk
- Block high-risk sign-ins

**User risk policy**:
- Require password change for high-risk users
- Block access until risk remediated

### Remediation

**Self-remediation**:
- MFA challenge
- Secure password change

**Admin remediation**:
- Confirm user compromised
- Dismiss user risk
- Reset password

---

## Application Management

### Enterprise Applications

**Types**:
- **Gallery apps**: Pre-integrated SaaS apps
- **Non-gallery apps**: Custom SAML/OIDC apps
- **On-premises apps**: Published via Application Proxy

**SSO methods**:
- SAML
- OpenID Connect
- Password-based
- Linked

**User assignment**:
- Require user assignment
- Assign users and groups
- Self-service access

### App Registrations

**Purpose**: Register custom applications

**Authentication**:
- OAuth 2.0
- OpenID Connect
- SAML

**Permissions**:
- **Delegated**: User context
- **Application**: App context (daemon apps)

**Consent**:
- User consent
- Admin consent
- Tenant-wide admin consent

---

## B2B and B2C

### Azure AD B2B

**Purpose**: Collaborate with external users

**Features**:
- Invite external users as guests
- SSO to Azure AD apps
- MFA and Conditional Access
- No need for separate identity system

**Use cases**:
- Partner collaboration
- Vendor access
- Temporary contractors

### Azure AD B2C

**Purpose**: Customer identity and access management

**Features**:
- Customizable sign-up/sign-in
- Social identity providers (Google, Facebook, etc.)
- Custom policies
- Scalable (millions of users)

**Use cases**:
- Customer-facing applications
- Mobile apps
- Web applications

---

## Hybrid Identity

### Azure AD Connect

**Purpose**: Synchronize on-premises AD with Azure AD

**Sync methods**:
- **Password hash synchronization**: Hash of password synced
- **Pass-through authentication**: Authenticate against on-premises AD
- **Federation**: ADFS or third-party federation

**Features**:
- User and group sync
- Password writeback
- Device writeback
- Attribute filtering

**Best practices**:
- Use password hash sync (most resilient)
- Enable password writeback for SSPR
- Implement staging server for high availability
- Monitor sync health

---

## Security Best Practices

### Identity Security

1. **Enable MFA for all users**
2. **Implement Conditional Access policies**
3. **Use passwordless authentication**
4. **Enable Identity Protection**
5. **Implement PIM for privileged roles**
6. **Regular access reviews**
7. **Block legacy authentication**
8. **Monitor sign-in logs**

### Application Security

1. **Use managed identities** for Azure resources
2. **Implement least privilege** for app permissions
3. **Require admin consent** for sensitive permissions
4. **Use certificate credentials** instead of client secrets
5. **Rotate secrets regularly**
6. **Monitor app sign-ins**

### Device Security

1. **Require device compliance**
2. **Implement Conditional Access** for device-based policies
3. **Use Intune** for device management
4. **Enable BitLocker** for Windows devices
5. **Implement mobile application management (MAM)**

---

## Monitoring and Reporting

### Sign-in Logs

**Information**:
- User, application, location
- Success or failure
- MFA details
- Conditional Access results
- Device information

**Use cases**:
- Troubleshoot sign-in issues
- Audit user activity
- Detect suspicious activity

### Audit Logs

**Activities**:
- User and group management
- Application management
- Role assignments
- Policy changes

**Retention**:
- Free: 7 days
- Premium: 30 days
- Export to Log Analytics for longer retention

### Workbooks

**Pre-built workbooks**:
- Sign-ins
- Conditional Access
- Identity Protection
- Usage and insights

**Custom workbooks**:
- Combine multiple data sources
- Visualize trends
- Share with team

---

## Compliance and Governance

### Access Reviews

**Purpose**: Regularly review and certify access

**Review types**:
- Group membership
- Application access
- Azure AD role assignments
- Azure resource role assignments

**Reviewers**:
- Resource owners
- Selected users
- Self-review

**Automation**:
- Auto-apply results
- Remove access if not reviewed

### Entitlement Management

**Purpose**: Automate access request workflows

**Features**:
- Access packages
- Approval workflows
- Time-bound access
- Access reviews
- Separation of duties

**Use cases**:
- Onboarding/offboarding
- Project-based access
- Guest access management

---

## Emergency Access Accounts

### Purpose

**Break-glass accounts** for emergency access when:
- Conditional Access misconfiguration
- MFA service outage
- Admin account lockout

### Configuration

**Requirements**:
- Cloud-only accounts (not synced)
- Global Administrator role
- Strong, unique passwords (stored securely)
- Excluded from Conditional Access policies
- Excluded from MFA
- Monitored for any usage

**Best practices**:
- Create at least 2 accounts
- Store passwords in physical safe
- Alert on any usage
- Regular testing
- Document procedures
