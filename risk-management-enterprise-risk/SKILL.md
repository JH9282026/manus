---
name: risk-management-enterprise-risk
description: The Risk Management & Enterprise Risk skill empowers AI agents to deliver comprehensive enterprise risk management (ERM) capabilities, from risk identification and assessment through mitigation strategy development and ongoing risk monitoring.
---

---
name: Risk Management & Enterprise Risk
description: Comprehensive enterprise risk management skill enabling risk assessment, mitigation strategy development, compliance management, and business continuity planning to protect organizational value and enable informed risk-taking.
---

# Risk Management & Enterprise Risk

## Skill Description and Purpose

The Risk Management & Enterprise Risk skill empowers AI agents to deliver comprehensive enterprise risk management (ERM) capabilities, from risk identification and assessment through mitigation strategy development and ongoing risk monitoring. This skill encompasses the complete risk management lifecycle aligned with leading frameworks including COSO ERM, ISO 31000, and industry-specific standards.

This skill is essential for organizations seeking to establish robust risk governance, protect against threats to strategic objectives, ensure regulatory compliance, and enable informed risk-taking that supports business growth. The skill enables autonomous risk assessment, development of risk treatment strategies, implementation of control frameworks, and creation of risk-aware organizational cultures.

**Core Competency Areas:**
- **Risk Assessment Frameworks**: COSO ERM 2017, ISO 31000:2018, and industry-specific frameworks implementation and customization
- **Risk Identification and Analysis**: Risk universe development, inherent and residual risk assessment, scenario analysis, and risk quantification
- **Risk Mitigation Strategies and Controls**: Control design, risk treatment options (accept, avoid, transfer, mitigate), and control effectiveness evaluation
- **Compliance Management and Regulatory Risk**: Regulatory landscape mapping, compliance program design, and regulatory change management
- **Business Continuity Planning (BCP) and Disaster Recovery**: BIA development, continuity strategy, DR planning, and crisis management
- **Risk Monitoring and Reporting**: Key Risk Indicators (KRIs), risk dashboards, board reporting, and emerging risk surveillance
- **Enterprise Risk Management (ERM) Frameworks**: ERM program design, risk appetite frameworks, and integrated risk management
- **Risk Appetite and Tolerance Setting**: Risk appetite statements, tolerance thresholds, and cascading risk limits
- **Operational, Financial, Strategic, and Reputational Risk**: Multi-dimensional risk assessment across risk categories
- **Risk Culture and Governance**: Three lines of defense model, risk committee structures, and risk awareness programs

**When to Use This Skill:**
Deploy this skill when establishing ERM programs, conducting risk assessments, developing business continuity plans, designing compliance frameworks, creating risk governance structures, implementing risk monitoring systems, or building risk-aware organizational cultures.

## Required Inputs/Parameters

### Strategic Context Inputs
| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `organization_profile` | JSON object | Company size, industry, geographic scope, regulatory environment, and business model | Yes |
| `strategic_objectives` | Document/JSON | Corporate strategy, growth plans, and strategic priorities | Yes |
| `risk_governance_structure` | Document | Current risk committee structure, roles, and reporting lines | Recommended |
| `regulatory_requirements` | JSON/Document | Applicable regulations, industry standards, and compliance obligations | Yes |

### Risk Data Inputs
| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `risk_register` | Structured data | Existing risk inventory, assessments, and control mappings | Conditional |
| `incident_history` | CSV/JSON | Historical risk events, losses, and near-misses | Recommended |
| `control_inventory` | Structured data | Current controls, ownership, and effectiveness assessments | Conditional |
| `audit_findings` | Document collection | Internal and external audit reports and findings | Recommended |
| `insurance_coverage` | Structured data | Current insurance policies, limits, and coverage gaps | Conditional |

### Assessment Parameters
| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `risk_categories` | Array | Strategic, operational, financial, compliance, and reputational risk focus areas | Yes |
| `assessment_methodology` | String | Qualitative, semi-quantitative, or quantitative risk assessment approach | Yes |
| `risk_appetite_level` | Scale (1-10) | Organization's general tolerance for risk | Yes |
| `time_horizon` | String | Near-term (1 year), medium-term (1-3 years), or long-term (3-5 years) | Yes |

## Expected Outputs/Deliverables

### Framework and Governance Deliverables
1. **Enterprise Risk Management Framework** (40-60 pages)
   - ERM vision, mission, and objectives
   - Risk management policy and standards
   - Risk governance structure and accountabilities
   - Three lines of defense model implementation
   - Risk assessment methodology and criteria
   - Risk appetite framework and statements
   - Risk reporting architecture
   - ERM maturity roadmap

2. **Risk Appetite Framework**
   - Risk appetite statement (board-approved)
   - Risk tolerance levels by category
   - Key Risk Indicators with thresholds
   - Escalation triggers and protocols
   - Risk limit cascade methodology
   - Appetite monitoring and reporting
   - Annual review and refresh process

### Risk Assessment Deliverables
3. **Enterprise Risk Assessment**
   - Risk universe and taxonomy
   - Top enterprise risks (typically 10-20)
   - Risk assessment heat maps
   - Inherent and residual risk ratings
   - Control effectiveness assessments
   - Risk ownership assignments
   - Risk interconnection analysis
   - Emerging risk identification

4. **Risk Register and Treatment Plans**
   - Comprehensive risk register database
   - Risk descriptions and impact scenarios
   - Likelihood and impact assessments
   - Control mapping and gap analysis
   - Risk treatment recommendations
   - Action plans with timelines
   - Risk monitoring indicators
   - Progress tracking mechanism

### Business Continuity Deliverables
5. **Business Continuity Program**
   - Business Impact Analysis (BIA)
   - Critical process identification
   - Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)
   - Continuity strategy options analysis
   - Business Continuity Plans by function
   - Crisis management framework
   - Communication protocols
   - Testing and exercise program

6. **Disaster Recovery Plan**
   - IT disaster recovery strategy
   - System recovery priorities
   - Technical recovery procedures
   - Data backup and restoration processes
   - Alternative site strategies
   - Vendor dependencies and contacts
   - DR testing schedule and procedures
   - Plan maintenance requirements

### Compliance and Reporting Deliverables
7. **Compliance Management Framework**
   - Regulatory landscape mapping
   - Compliance obligation inventory
   - Control framework alignment (SOX, GDPR, etc.)
   - Compliance monitoring program
   - Policy management framework
   - Training and awareness program
   - Regulatory change management process
   - Compliance reporting and attestation

8. **Risk Reporting Package**
   - Board risk report template
   - Executive risk dashboard
   - Key Risk Indicator scorecard
   - Risk trend analysis
   - Emerging risk briefings
   - Incident and loss reporting
   - Regulatory compliance status
   - Risk culture metrics

### Quality Standards
- All frameworks aligned with recognized standards (COSO, ISO 31000)
- Risk assessments validated through stakeholder workshops
- Quantitative analysis with documented assumptions
- Action plans with clear ownership and timelines
- Board-ready reporting formats
- Integration with strategic planning processes

## Example Use Cases

### Use Case 1: ERM Program Implementation
**Scenario**: A mid-market company ($2B revenue) with informal risk management practices needs to establish a formal ERM program to satisfy board governance requirements and support growth strategy.

**Application**: The skill conducts risk maturity assessment against COSO ERM framework, designs risk governance structure with board risk committee charter, develops risk appetite framework aligned with strategic objectives, creates enterprise risk assessment methodology, facilitates top-down risk identification with executive team, builds risk register with 75 risks across 5 categories, establishes KRI framework with 25 key indicators, implements risk reporting cadence, and delivers comprehensive ERM program achieving desired maturity within 18 months.

### Use Case 2: Financial Services Regulatory Compliance
**Scenario**: A regional bank needs to enhance its risk management and compliance framework to address regulatory expectations (OCC/Fed) and recent examination findings.

**Application**: The skill maps regulatory requirements across OCC Heightened Standards, Federal Reserve guidance, and state regulations, conducts gap assessment against current practices, designs enhanced risk assessment methodology incorporating forward-looking risk identification, develops stress testing integration with enterprise risk, creates compliance monitoring program with automated controls testing, implements three lines of defense model with clear accountabilities, builds regulatory examination management process, and delivers enhanced risk framework achieving successful regulatory examination with no significant findings.

### Use Case 3: Business Continuity Program Development
**Scenario**: A healthcare system with 15 hospitals and 500+ clinics needs comprehensive business continuity program to address patient safety, regulatory requirements, and operational resilience.

**Application**: The skill conducts Business Impact Analysis across all facilities and functions, identifies critical processes affecting patient care and safety, establishes RTOs and RPOs aligned with clinical and regulatory requirements, develops continuity strategies for clinical, IT, and administrative functions, creates facility-specific business continuity plans, designs crisis management and incident command structure, implements pandemic and mass casualty protocols, establishes testing and exercise program, and delivers enterprise BCP program with annual exercise achieving 95% plan activation readiness.

### Use Case 4: Cyber Risk Integration into ERM
**Scenario**: A technology company needs to integrate cyber risk into its enterprise risk framework following board concerns about increasing cyber threats and potential business impact.

**Application**: The skill conducts cyber risk assessment using NIST CSF and FAIR methodology, quantifies top cyber risks in financial terms, integrates cyber risks into enterprise risk register with consistent rating methodology, develops cyber risk appetite statement and tolerance levels, establishes cyber KRIs aligned with enterprise risk reporting, creates cyber incident escalation and communication protocols, implements cyber risk scenario analysis for strategic planning, and delivers integrated cyber-ERM framework enabling informed investment decisions and board-level cyber risk oversight.

### Use Case 5: Third-Party Risk Management Program
**Scenario**: A pharmaceutical company with 3,000+ suppliers and service providers needs enhanced third-party risk management following regulatory observations and supply chain disruptions.

**Application**: The skill develops third-party risk taxonomy covering operational, compliance, cybersecurity, and financial risks, creates vendor segmentation methodology based on criticality and risk exposure, designs tiered due diligence requirements by risk level, establishes ongoing monitoring program with automated alerts, implements contract risk requirements and SLA monitoring, builds fourth-party (sub-contractor) visibility framework, creates concentration risk analysis and mitigation strategies, and delivers TPRM program achieving regulatory compliance and reducing third-party risk events by 40%.

## Prerequisites or Dependencies

### Knowledge Prerequisites
- Enterprise risk management frameworks (COSO, ISO 31000)
- Risk assessment methodologies (qualitative and quantitative)
- Internal control frameworks (COSO IC, COBIT)
- Business continuity planning standards (ISO 22301)
- Regulatory compliance requirements (industry-specific)
- Insurance and risk transfer mechanisms
- Corporate governance principles

### Data and System Requirements
- Access to GRC (Governance, Risk, Compliance) platforms
- Historical incident and loss data
- Audit reports and findings
- Control documentation and test results
- Business process documentation
- Financial and operational performance data
- Regulatory requirements databases

### Tool Dependencies
- GRC platforms (ServiceNow, Archer, MetricStream)
- Risk assessment and quantification tools
- Business continuity planning software
- Compliance management systems
- Data analysis and visualization tools
- Survey and workshop facilitation tools
- Document management systems

### Stakeholder Access Requirements
- Board and risk committee for governance and appetite
- Executive leadership for risk ownership
- Business unit leaders for risk identification
- Internal audit for assurance coordination
- Legal and compliance for regulatory requirements
- IT for cybersecurity and DR planning
- Finance for insurance and financial risk

### Integration Dependencies
- Strategic planning for risk-informed decision making
- Internal audit for coordinated assurance
- Finance for insurance and financial risk management
- IT for technology risk and DR integration
- HR for operational risk and culture
- Legal for regulatory and contractual risk
- Communications for crisis management

### Environmental Considerations
- Industry-specific regulatory landscape
- Geographic risk factors and jurisdictional requirements
- Competitive environment and market risks
- Technology and cyber threat landscape
- Economic and geopolitical conditions
- Climate and environmental risk factors
- Social and reputational risk environment
