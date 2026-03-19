# Data Governance for Revenue Operations

Comprehensive frameworks for establishing data standards, ensuring data quality, and implementing governance policies across the revenue technology stack.

---

## Data Governance Fundamentals

### Definition and Purpose

Data governance is the framework of policies, processes, and standards that ensure data is accurate, consistent, secure, and used appropriately across the organization.

**Core Objectives**:
1. **Data Quality**: Ensure accuracy, completeness, and consistency
2. **Data Security**: Protect sensitive information and comply with regulations
3. **Data Accessibility**: Enable appropriate access while maintaining control
4. **Data Standardization**: Create common definitions and formats
5. **Data Accountability**: Establish clear ownership and responsibility

### Business Impact

**Poor Data Governance Consequences**:
- Inaccurate forecasts and reporting
- Wasted sales and marketing efforts
- Poor customer experiences
- Compliance violations and fines
- Lost revenue opportunities
- Inefficient operations

**Strong Data Governance Benefits**:
- Improved decision-making
- Increased operational efficiency
- Better customer insights
- Regulatory compliance
- Enhanced trust in data
- Faster time to insights

## Data Governance Framework

### Governance Structure

**Data Governance Council**
- **Composition**: CRO, VP Sales, VP Marketing, VP Customer Success, CFO, RevOps Leader
- **Responsibilities**: Set data strategy, approve policies, resolve escalations
- **Cadence**: Quarterly meetings

**Data Stewardship Team**
- **Composition**: RevOps Manager, Sales Ops, Marketing Ops, CS Ops, Data Analyst
- **Responsibilities**: Implement policies, manage data quality, provide training
- **Cadence**: Monthly meetings, ongoing operational work

**Data Owners**
- **By Domain**: Each department owns specific data domains
  - Marketing: Campaigns, leads, marketing attribution
  - Sales: Opportunities, accounts, quotes
  - Customer Success: Health scores, renewals, support tickets
  - Finance: Revenue, invoices, payments
- **Responsibilities**: Define standards, ensure quality, approve access

**Data Users**
- **All Revenue Team Members**: Sales reps, marketers, CSMs
- **Responsibilities**: Follow data entry standards, maintain quality, report issues

### Governance Policies

**Data Quality Policy**
- Minimum data quality standards (accuracy, completeness, timeliness)
- Data validation and cleansing procedures
- Quality metrics and monitoring
- Remediation processes for quality issues

**Data Security and Privacy Policy**
- Access control principles (least privilege, role-based)
- Data classification (public, internal, confidential, restricted)
- Encryption and protection requirements
- Compliance with regulations (GDPR, CCPA, etc.)

**Data Retention and Archival Policy**
- Retention periods by data type
- Archival procedures and storage
- Deletion and purging processes
- Legal hold and e-discovery procedures

**Data Integration and Sharing Policy**
- Approved integration methods and tools
- Data sharing agreements and protocols
- API usage and rate limiting
- Third-party data handling

## Data Quality Management

### Data Quality Dimensions

**Accuracy**
- **Definition**: Data correctly represents reality
- **Measurement**: % of records with accurate values
- **Target**: >95% accuracy for critical fields
- **Example**: Email addresses are valid and deliverable

**Completeness**
- **Definition**: All required data is present
- **Measurement**: % of records with all required fields populated
- **Target**: >90% completeness for required fields
- **Example**: All opportunities have close date, amount, and stage

**Consistency**
- **Definition**: Data is uniform across systems and time
- **Measurement**: % of records matching across integrated systems
- **Target**: >98% consistency for synchronized fields
- **Example**: Account name is identical in CRM and marketing automation

**Timeliness**
- **Definition**: Data is up-to-date and available when needed
- **Measurement**: Average age of data, sync frequency
- **Target**: Real-time or <15 minutes for critical data
- **Example**: Opportunity stage changes reflected in reports within 15 minutes

**Validity**
- **Definition**: Data conforms to defined formats and rules
- **Measurement**: % of records passing validation rules
- **Target**: >99% validity for structured fields
- **Example**: Phone numbers match standard format, states use approved codes

**Uniqueness**
- **Definition**: No duplicate records exist
- **Measurement**: % of records that are unique
- **Target**: <1% duplicate rate
- **Example**: Each account exists only once in CRM

### Data Quality Metrics

**Overall Data Quality Score**
```
DQ Score = (Accuracy × 0.3) + (Completeness × 0.25) + (Consistency × 0.2) + 
           (Timeliness × 0.15) + (Validity × 0.05) + (Uniqueness × 0.05)
```

**Critical Field Completeness**
| Object | Critical Fields | Target Completeness |
|--------|----------------|--------------------|
| **Lead** | Name, Email, Company, Source | 95% |
| **Account** | Name, Industry, Employee Count, Revenue | 90% |
| **Contact** | Name, Email, Title, Account | 95% |
| **Opportunity** | Name, Amount, Close Date, Stage, Owner | 98% |

**Duplicate Rates**
- Leads: <2%
- Contacts: <1%
- Accounts: <0.5%
- Opportunities: <0.1%

**Data Age**
- Contact information: <6 months old
- Account firmographics: <12 months old
- Opportunity data: Real-time

### Data Quality Processes

**Prevention (Proactive)**

**1. Data Entry Standards**
- Required fields at point of entry
- Validation rules and picklists
- Format requirements (phone, email, etc.)
- Default values where appropriate

**2. User Training**
- Data entry best practices
- Importance of data quality
- How to use CRM and tools correctly
- Regular refresher training

**3. Automation**
- Auto-populate fields from enrichment sources
- Workflow rules to enforce standards
- Duplicate prevention rules
- Data validation on save

**Detection (Monitoring)**

**1. Data Quality Dashboards**
- Real-time quality metrics by object and field
- Trend analysis over time
- Quality by user, team, or source
- Alerts for quality degradation

**2. Regular Audits**
- Weekly: Critical field completeness
- Monthly: Comprehensive quality review
- Quarterly: Deep-dive analysis and remediation planning

**3. Automated Monitoring**
- Scheduled data quality jobs
- Exception reports for quality violations
- Alerts for critical issues

**Correction (Remediation)**

**1. Data Cleansing**
- Standardize formats (phone, address, etc.)
- Fill missing values from enrichment sources
- Correct invalid or inaccurate data
- Remove or merge duplicates

**2. Enrichment**
- Append missing firmographic data
- Update contact information
- Add technographic or intent data
- Enhance with third-party sources

**3. Deduplication**
- Identify duplicate records
- Determine master record
- Merge duplicates preserving data
- Prevent future duplicates

## Data Standardization

### Master Data Management

**Account Data Standards**

**Account Name**
- Use legal entity name (not DBA or abbreviation)
- Standardize suffixes (Inc., LLC, Ltd., Corp.)
- Remove extraneous characters (periods, commas)
- Capitalize properly

**Industry**
- Use standardized industry taxonomy (e.g., NAICS, SIC)
- Limit to approved picklist values
- Map custom values to standard taxonomy

**Address**
- Use standard format (street, city, state, zip, country)
- Validate against postal databases
- Standardize abbreviations (St., Ave., Blvd.)
- Include country code for international

**Contact Data Standards**

**Name**
- Separate first and last name fields
- Capitalize properly (not all caps or all lowercase)
- Remove titles (Mr., Mrs., Dr.) from name fields
- Store titles in separate field

**Email**
- Validate format (contains @, valid domain)
- Check deliverability where possible
- Standardize to lowercase
- Flag role-based emails (info@, sales@)

**Phone**
- Use standard format: +[country code] ([area code]) [number]
- Example: +1 (555) 123-4567
- Remove extensions from main number field
- Store mobile, work, and home separately

**Opportunity Data Standards**

**Opportunity Name**
- Format: [Account Name] - [Product/Solution] - [Close Date]
- Example: Acme Corp - Enterprise Platform - Q1 2026
- Consistent naming enables reporting and analysis

**Amount**
- Use Annual Contract Value (ACV) for subscriptions
- Use Total Contract Value (TCV) for multi-year deals
- Exclude services or one-time fees (track separately)
- Round to nearest dollar (no cents)

**Close Date**
- Use last day of month for monthly targets
- Use last day of quarter for quarterly targets
- Update within 48 hours of change
- Require justification for date changes

### Picklist Management

**Picklist Governance**
- Limit picklist values to essential options
- Require approval for new values
- Regularly review and retire unused values
- Provide clear definitions for each value

**Common Picklists**

**Lead Source**
- Website
- Referral
- Event
- Paid Advertising
- Content Download
- Webinar
- Partner
- Sales Prospecting

**Opportunity Stage**
- Qualification
- Discovery
- Proposal
- Negotiation
- Closed Won
- Closed Lost

**Industry**
- Technology
- Financial Services
- Healthcare
- Manufacturing
- Retail
- Professional Services
- (Use standard taxonomy)

**Lead Status**
- New
- Contacted
- Qualified
- Unqualified
- Converted

## Data Security and Privacy

### Data Classification

**Public**
- Definition: Information that can be freely shared
- Examples: Marketing content, public pricing, press releases
- Controls: None required

**Internal**
- Definition: Information for internal use only
- Examples: Internal processes, non-sensitive customer data
- Controls: Require authentication, limit to employees

**Confidential**
- Definition: Sensitive business information
- Examples: Financial data, strategic plans, customer contracts
- Controls: Role-based access, encryption, audit logging

**Restricted**
- Definition: Highly sensitive information with legal/regulatory requirements
- Examples: PII, payment card data, health information
- Controls: Strict access controls, encryption, compliance monitoring

### Access Control

**Principles**

**Least Privilege**
- Users have minimum access needed for their role
- Default to no access, grant as needed
- Regular access reviews and recertification

**Role-Based Access Control (RBAC)**
- Define roles with specific permissions
- Assign users to roles based on job function
- Standardize access by role

**Separation of Duties**
- No single user has end-to-end control of critical processes
- Example: User who creates quote cannot approve it

**Access Control Matrix**

| Role | Leads | Accounts | Opportunities | Reports | Admin |
|------|-------|----------|---------------|---------|-------|
| **Sales Rep** | Own records | Own accounts | Own opps | Standard | No |
| **Sales Manager** | Team records | Team accounts | Team opps | Custom | No |
| **Marketing** | All leads | Read all | Read all | Standard | No |
| **Customer Success** | No access | Own accounts | Read all | Standard | No |
| **RevOps** | All records | All records | All records | All | Yes |
| **Executive** | Read all | Read all | Read all | All | No |

### Compliance

**GDPR (General Data Protection Regulation)**

**Key Requirements**:
- Lawful basis for processing personal data
- Consent management and documentation
- Right to access, rectify, and erase data
- Data portability
- Privacy by design and default
- Data breach notification (72 hours)

**Implementation**:
- Consent tracking in CRM
- Data subject request workflows
- Data retention and deletion policies
- Privacy impact assessments
- Data processing agreements with vendors

**CCPA (California Consumer Privacy Act)**

**Key Requirements**:
- Right to know what data is collected
- Right to delete personal information
- Right to opt-out of data sale
- Non-discrimination for exercising rights

**Implementation**:
- Privacy policy updates
- "Do Not Sell" mechanisms
- Consumer request portal
- Data inventory and mapping

**Other Regulations**
- **HIPAA**: Healthcare data (if applicable)
- **PCI DSS**: Payment card data (if processing payments)
- **SOC 2**: Security and availability controls
- **ISO 27001**: Information security management

## Data Integration Governance

### Integration Standards

**Approved Integration Methods**
1. **Native Integrations**: Vendor-provided, supported integrations
2. **API Integrations**: RESTful APIs with proper authentication
3. **iPaaS Platforms**: Approved platforms (Zapier, Workato, Mulesoft)
4. **ETL Tools**: Data warehouse integrations (Fivetran, Stitch)

**Prohibited Methods**
- Screen scraping or web automation
- Shared login credentials
- Unsecured file transfers
- Unapproved third-party tools

### Integration Approval Process

**Step 1: Request Submission**
- Business justification and use case
- Source and target systems
- Data fields to be integrated
- Frequency and volume

**Step 2: Security Review**
- Data classification and sensitivity
- Authentication and authorization method
- Encryption in transit and at rest
- Compliance implications

**Step 3: Technical Review**
- Integration method and architecture
- Error handling and monitoring
- Performance and scalability
- Maintenance and support plan

**Step 4: Approval and Implementation**
- Data Governance Council approval
- Implementation by approved team
- Testing and validation
- Documentation and training

### Integration Monitoring

**Health Metrics**
- Integration success rate (target: >99%)
- Average sync time
- Error rate and types
- Data volume and growth

**Alerts**
- Integration failures
- Sync delays exceeding SLA
- Data quality issues
- Unusual volume or patterns

**Regular Reviews**
- Weekly: Error log review and resolution
- Monthly: Performance and health metrics
- Quarterly: Integration audit and optimization

## Data Stewardship

### Roles and Responsibilities

**Chief Data Steward (RevOps Leader)**
- Overall accountability for data governance
- Chair Data Governance Council
- Approve policies and standards
- Resolve escalations

**Data Domain Stewards**
- Own specific data domains (accounts, opportunities, etc.)
- Define standards and rules for their domain
- Monitor quality and compliance
- Approve access requests

**Data Quality Analysts**
- Monitor data quality metrics
- Perform data cleansing and enrichment
- Investigate and resolve quality issues
- Generate quality reports

**System Administrators**
- Implement technical controls (validation rules, workflows)
- Manage user access and permissions
- Configure integrations and data flows
- Maintain system documentation

**End Users**
- Follow data entry standards
- Maintain data quality in daily work
- Report data issues
- Complete data governance training

### Training and Enablement

**New Hire Onboarding**
- Data governance overview and importance
- Data entry standards and best practices
- System training (CRM, tools)
- Compliance and security requirements

**Ongoing Training**
- Quarterly refresher sessions
- Updates on policy or standard changes
- Best practice sharing
- Quality improvement workshops

**Resources**
- Data governance handbook
- Quick reference guides
- Video tutorials
- Help desk and support

## Continuous Improvement

### Governance Maturity Model

**Level 1: Ad Hoc**
- No formal governance
- Inconsistent data quality
- Reactive problem-solving

**Level 2: Developing**
- Basic policies and standards
- Some data quality monitoring
- Informal stewardship

**Level 3: Defined**
- Documented governance framework
- Regular quality monitoring and reporting
- Formal stewardship roles

**Level 4: Managed**
- Proactive quality management
- Automated monitoring and remediation
- Strong compliance and security

**Level 5: Optimized**
- Continuous improvement culture
- Predictive quality management
- Data governance as competitive advantage

### Metrics and KPIs

**Governance Effectiveness**
- Data quality score trend
- Policy compliance rate
- Time to resolve data issues
- User satisfaction with data

**Operational Efficiency**
- Time spent on data cleanup
- Cost of data quality issues
- Automation rate for data processes

**Business Impact**
- Forecast accuracy improvement
- Revenue impact of data quality
- Customer satisfaction correlation
- Compliance audit results
