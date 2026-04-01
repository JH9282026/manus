---
name: project-brief-development
description: "The Project Brief Development & Documentation skill enables autonomous creation of comprehensive, stakeholder-ready project briefs that serve as the foundational governance document for any initiative."
---

---
name: Project Brief Development & Documentation
description: A universal, comprehensive skill for creating detailed project briefs that define scope, objectives, stakeholders, timelines, budgets, risks, and success metrics across all project types and domains—from software development to marketing campaigns to construction projects.
---

# Project Brief Development & Documentation


## Overview

This section provides an overview of the skill.

## 1. Skill Description and Purpose

### What This Skill Does

The Project Brief Development & Documentation skill enables autonomous creation of comprehensive, stakeholder-ready project briefs that serve as the foundational governance document for any initiative. This skill synthesizes project information from multiple sources, applies industry-standard project management frameworks, and generates structured documentation that aligns teams, secures approvals, and establishes clear success criteria.

### Strategic Value and Business Impact

Project briefs are the cornerstone of successful project execution. Research from the Project Management Institute (PMI) indicates that organizations with mature project documentation practices complete 89% of projects successfully, compared to just 36% for organizations with poor documentation standards. This skill delivers:

- **Alignment Acceleration**: Reduces stakeholder alignment time by 40-60% through structured, comprehensive documentation
- **Risk Reduction**: Proactive identification of constraints, dependencies, and potential failure points before project initiation
- **Resource Optimization**: Clear budget and resource allocation prevents scope creep and cost overruns
- **Decision Enablement**: Provides executives with sufficient information to make informed go/no-go decisions
- **Accountability Framework**: Establishes clear ownership through RACI matrices and approval workflows

### When to Deploy This Skill

Execute this skill when:

1. **Project Initiation Phase**: When transitioning from concept to formal project planning
2. **Stakeholder Alignment**: When multiple departments or external parties require coordinated understanding
3. **Budget Approval Processes**: When financial authorization requires documented justification
4. **Strategic Planning Cycles**: When portfolio decisions require standardized project comparisons
5. **Vendor/Partner Engagements**: When external parties need formal scope and expectation documentation
6. **Regulatory Compliance**: When audit trails require formal project governance documentation
7. **Post-Mortem Baseline**: When establishing reference points for retrospective analysis

### Framework Adaptability

This skill incorporates and adapts methodologies from:

| Framework | Primary Application | Key Elements Incorporated |
|-----------|-------------------|---------------------------|
| PMI/PMBOK | Enterprise projects | Charter template, WBS structure, stakeholder register |
| Agile/Scrum | Iterative development | User stories, sprint structure, product backlog format |
| PRINCE2 | Governance-heavy projects | Business case format, stage gates, exception handling |
| Lean | Efficiency-focused initiatives | Value stream mapping, waste identification, continuous improvement |
| Six Sigma DMAIC | Quality/process improvement | Define phase structure, metric definition, baseline establishment |
| Waterfall | Sequential/regulated projects | Phase dependencies, milestone gates, formal sign-offs |

---

## 2. Required Inputs/Parameters

### Primary Inputs (Required)

| Parameter | Format | Description | Validation Rules |
|-----------|--------|-------------|------------------|
| `project_name` | String (3-100 chars) | Official project title | Alphanumeric, no special characters except hyphens/underscores |
| `project_type` | Enum | Category classification | Valid values: `software_development`, `marketing_campaign`, `product_launch`, `construction`, `event_planning`, `research`, `manufacturing`, `consulting`, `organizational_change`, `sales_campaign`, `other` |
| `project_description` | String (50-2000 chars) | High-level summary of the project | Must include problem/opportunity statement |
| `business_objectives` | Array[String] | 2-7 primary business objectives | Each objective should follow SMART criteria format |
| `target_start_date` | ISO 8601 Date | Intended project commencement | Must be future date or current date |
| `target_end_date` | ISO 8601 Date | Intended project completion | Must be after start_date |
| `estimated_budget` | Object | Budget allocation | `{total: Number, currency: String, breakdown: Object}` |
| `project_sponsor` | Object | Executive sponsor details | `{name: String, title: String, department: String, contact: String}` |

### Secondary Inputs (Recommended)

| Parameter | Format | Description | Default Behavior |
|-----------|--------|-------------|------------------|
| `stakeholders` | Array[Object] | Stakeholder registry | Auto-generate template if not provided |
| `key_deliverables` | Array[Object] | Primary outputs and artifacts | Derive from project_type templates |
| `success_metrics` | Array[Object] | KPIs and measurement criteria | Generate industry-standard metrics based on project_type |
| `known_risks` | Array[Object] | Pre-identified risk factors | Populate with common risks for project_type |
| `constraints` | Object | Technical, resource, time, budget limitations | Query for critical constraints |
| `dependencies` | Array[Object] | External dependencies and prerequisites | Identify based on deliverables |
| `communication_preferences` | Object | Stakeholder communication requirements | Apply organizational defaults |
| `methodology` | Enum | Project management approach | Recommend based on project_type and duration |
| `compliance_requirements` | Array[String] | Regulatory or policy requirements | Check against industry and geography |

### Contextual Inputs (Optional Enhancement)

| Parameter | Format | Purpose |
|-----------|--------|---------|
| `historical_projects` | Array[Reference] | Reference similar past projects for estimates and lessons learned |
| `organizational_templates` | Reference | Apply organization-specific formatting and sections |
| `integration_systems` | Array[String] | Target systems for brief distribution (Jira, Asana, Monday.com, etc.) |
| `approval_workflow` | Object | Custom approval chain and requirements |
| `brand_guidelines` | Reference | Visual and formatting standards for documentation |

### Input Validation and Processing

Before brief generation, validate all inputs against these criteria:

1. **Date Logic**: `target_end_date` > `target_start_date`; duration is realistic for `project_type`
2. **Budget Completeness**: Total equals sum of breakdown categories within 5% tolerance
3. **Stakeholder Coverage**: At minimum, sponsor, project manager, and one approver identified
4. **Objective Quality**: Each objective contains measurable outcomes and timeframes
5. **Scope Clarity**: At least 3 in-scope items and 2 out-of-scope items defined

---

## 3. Expected Outputs/Deliverables

### Primary Deliverable: Project Brief Document

**Format Options**: Markdown (.md), PDF, Word (.docx), HTML, JSON (structured data), or direct integration push

**Document Structure**:

```
1. Executive Summary (250-400 words)
   - Project overview and strategic context
   - Key objectives and success criteria summary
   - Budget and timeline overview
   - Critical risks and dependencies

2. Project Definition
   2.1 Vision and Purpose Statement
   2.2 Business Case and Justification
   2.3 Problem Statement / Opportunity Description
   2.4 Strategic Alignment Matrix
   2.5 SMART Objectives Table

3. Scope Definition
   3.1 In-Scope Items (detailed list with descriptions)
   3.2 Out-of-Scope Items (explicit exclusions)
   3.3 Deliverables Registry (with acceptance criteria)
   3.4 Work Breakdown Structure (Level 2-3)
   3.5 Scope Boundaries and Limitations

4. Stakeholder Management
   4.1 Stakeholder Register (name, role, influence, interest)
   4.2 RACI Matrix (all deliverables × all stakeholders)
   4.3 Team Structure and Responsibilities
   4.4 Decision Authority Matrix
   4.5 External Partners and Vendors

5. Timeline and Milestones
   5.1 Project Phases with Date Ranges
   5.2 Milestone Schedule (with dependencies)
   5.3 Critical Path Identification
   5.4 Phase Gate Criteria
   5.5 Gantt Chart Visualization
   5.6 Buffer and Contingency Allocation

6. Budget and Resources
   6.1 Budget Summary by Category
   6.2 Resource Allocation Matrix
   6.3 Cost Estimation Methodology and Assumptions
   6.4 Funding Sources and Approval Status
   6.5 Procurement Schedule
   6.6 Cost-Benefit Analysis Summary

7. Success Metrics and KPIs
   7.1 Quantitative Metrics Table (baseline, target, stretch)
   7.2 Qualitative Assessment Criteria
   7.3 Measurement Methodology
   7.4 Reporting Dashboard Specification
   7.5 ROI Calculation Framework

8. Risk Management
   8.1 Risk Register (probability × impact matrix)
   8.2 Mitigation Strategies by Risk
   8.3 Contingency Plans
   8.4 Assumptions Log
   8.5 Constraint Documentation

9. Communication Plan
   9.1 Stakeholder Communication Matrix
   9.2 Meeting Schedule (type, frequency, attendees)
   9.3 Reporting Cadence and Templates
   9.4 Escalation Procedures
   9.5 Documentation Repository Structure

10. Governance and Approval
    10.1 Approval Workflow Diagram
    10.2 Sign-Off Requirements
    10.3 Change Control Process
    10.4 Version Control Protocol
    10.5 Signature Page
```

### Quality Standards for Output

| Criterion | Standard | Validation Method |
|-----------|----------|-------------------|
| Completeness | All 10 sections populated | Section checklist verification |
| Consistency | Terminology, dates, figures consistent throughout | Cross-reference validation |
| Clarity | Flesch-Kincaid readability score 40-60 (professional) | Readability analysis |
| Actionability | Each section contains specific, executable items | Action verb presence check |
| Measurability | All objectives have quantified targets | SMART criteria validation |
| Traceability | All deliverables linked to objectives | Mapping matrix generation |

### Supplementary Outputs

1. **Stakeholder Presentation Deck** (10-15 slides): Executive-ready summary for approval meetings
2. **RACI Matrix Spreadsheet**: Editable matrix for ongoing updates
3. **Risk Register Workbook**: Dynamic risk tracking template
4. **Gantt Chart Export**: Project timeline in common formats (MS Project, Asana, Monday.com)
5. **Budget Tracker Template**: Financial monitoring spreadsheet
6. **Change Request Form**: Standardized scope change documentation

---

## 4. Example Use Cases

### Use Case 1: Enterprise Software Development Project

**Scenario**: A financial services company initiates a 12-month core banking system modernization project with $2.4M budget and 15-person cross-functional team.

**Input Parameters**:
- `project_type`: `software_development`
- `methodology`: `agile_scaled` (SAFe framework)
- `compliance_requirements`: ["SOX", "PCI-DSS", "GDPR"]
- `deliverables`: ["API Gateway", "Microservices Architecture", "Data Migration", "User Training"]

**Brief Customization**:
- Technical architecture section added with system integration diagrams
- Sprint structure and release train schedule in timeline
- Technical debt tracking in risk register
- Definition of Done (DoD) criteria for each deliverable
- DevOps pipeline requirements in resource allocation
- Security review gates at each phase

**Generated Sections Emphasis**: Technical scope boundaries, API specifications, data governance, testing strategy, rollback procedures, vendor SLA requirements.

---

### Use Case 2: Multi-Channel Marketing Campaign

**Scenario**: Consumer goods brand launching Q4 holiday campaign across digital, retail, and broadcast channels with $850K budget and 8-week execution window.

**Input Parameters**:
- `project_type`: `marketing_campaign`
- `target_audience`: "Millennials 25-40, household income $75K+, urban/suburban"
- `channels`: ["Social Media", "Programmatic Display", "Retail POP", "Connected TV", "Influencer"]
- `success_metrics`: ["Brand Awareness +15%", "Sales Lift 8%", "ROAS 4.2x"]

**Brief Customization**:
- Creative brief integration with messaging hierarchy
- Media mix allocation by channel and week
- Influencer selection criteria and deliverables
- A/B testing framework for creative variants
- Real-time optimization decision trees
- Post-campaign measurement methodology

**Generated Sections Emphasis**: Target audience personas, creative deliverables matrix, media schedule, UTM tracking specifications, brand safety requirements, agency responsibilities.

---

### Use Case 3: Commercial Construction Project

**Scenario**: Development firm building 45,000 sq ft mixed-use retail/office complex with $18M budget over 18-month timeline.

**Input Parameters**:
- `project_type`: `construction`
- `site_location`: "Downtown Portland, OR"
- `permits_required`: ["Building Permit", "Environmental Review", "Traffic Study", "Fire Marshal Approval"]
- `phases`: ["Site Prep", "Foundation", "Structure", "MEP", "Finishing", "Commissioning"]

**Brief Customization**:
- Permit acquisition timeline and dependencies
- Safety compliance matrix (OSHA requirements)
- Materials procurement schedule with lead times
- Subcontractor registry and scope assignments
- Inspection milestone integration
- Weather contingency protocols
- Liquidated damages clauses reference

**Generated Sections Emphasis**: Site logistics plan, permit dependencies, safety protocols, material specifications, inspection schedules, certificate of occupancy requirements.

---

### Use Case 4: Corporate Event Planning

**Scenario**: Technology company organizing 3-day annual user conference for 2,500 attendees with $1.2M budget.

**Input Parameters**:
- `project_type`: `event_planning`
- `event_format`: `hybrid` (in-person + virtual)
- `venue_requirements`: ["Main hall 2000 capacity", "12 breakout rooms", "Exhibition space"]
- `deliverables`: ["Keynote productions", "Breakout sessions", "Networking app", "Virtual platform"]

**Brief Customization**:
- Venue selection criteria and comparison matrix
- Speaker management and content timeline
- Registration and attendee journey mapping
- Vendor coordination schedule (AV, catering, security)
- Contingency plans for attendance variance
- Post-event survey and ROI measurement
- Virtual platform technical requirements

**Generated Sections Emphasis**: Attendee experience flow, speaker commitments, vendor contracts summary, day-of-event runsheet, contingency scenarios, health/safety protocols.

---

### Use Case 5: Organizational Change Initiative

**Scenario**: Healthcare system implementing new EHR platform affecting 4,500 clinical staff across 12 facilities over 24-month rollout.

**Input Parameters**:
- `project_type`: `organizational_change`
- `change_scope`: ["Process redesign", "Technology adoption", "Workflow modification", "Role changes"]
- `affected_populations`: ["Physicians", "Nurses", "Administrative Staff", "IT Support"]
- `change_framework`: `ADKAR`

**Brief Customization**:
- Change impact assessment by stakeholder group
- Training curriculum and certification requirements
- Resistance management strategies
- Super-user network structure
- Adoption metrics by facility and role
- Parallel run and cutover planning
- Support escalation during stabilization

**Generated Sections Emphasis**: Stakeholder change readiness, communication cascade, training schedule, adoption KPIs, resistance indicators, sustainment plan.

---

## 5. Prerequisites and Dependencies

### Required Access and Permissions

| Requirement | Purpose | Validation |
|-------------|---------|------------|
| Stakeholder contact information | RACI matrix population, communication plan | Verify email/phone availability |
| Budget authorization data | Financial section accuracy | Confirm with finance department |
| Organizational chart | Reporting structure, escalation paths | Access HR systems or manual input |
| Historical project data | Estimation accuracy, lessons learned | Project management office archives |
| Strategic plan documentation | Alignment validation | Executive or strategy team access |

### Required Data Sources

1. **Financial Systems**: Budget codes, cost center information, approval thresholds
2. **HR/Resource Management**: Staff availability, skill matrices, allocation calendars
3. **Project Portfolio Tools**: Dependencies on other initiatives, resource conflicts
4. **Risk Management Database**: Organizational risk categories, historical risk data
5. **Compliance Registry**: Applicable regulations, policy requirements, audit schedules

### Technical Dependencies

| Tool/System | Purpose | Integration Method |
|-------------|---------|-------------------|
| Calendar systems | Timeline validation, meeting scheduling | API integration (Google, Outlook) |
| Project management platforms | Gantt export, task creation | Native connectors (Jira, Asana, Monday.com) |
| Document management | Brief storage, version control | SharePoint, Confluence, Google Drive |
| Communication platforms | Stakeholder notification | Slack, Teams, Email integration |
| Visualization tools | Charts, diagrams, presentations | Mermaid, Lucidchart, PowerPoint |

### Knowledge Prerequisites

For optimal brief generation, the following information should be gathered or accessible:

1. **Organizational Context**: Strategic priorities, fiscal year planning, executive preferences
2. **Domain Expertise**: Industry-specific terminology, regulatory environment, competitive landscape
3. **Historical Performance**: Past project success rates, common failure modes, estimation accuracy
4. **Stakeholder Dynamics**: Political considerations, relationship histories, communication preferences
5. **Resource Landscape**: Available talent, skill gaps, external partner capabilities

### Pre-Execution Checklist

Before initiating project brief generation, confirm:

- [ ] Project sponsor identified and available for input validation
- [ ] Preliminary budget range approved by finance
- [ ] Key stakeholders identified (minimum 5)
- [ ] Target dates discussed with resource managers
- [ ] Business case or opportunity statement documented
- [ ] Success criteria discussed with executive sponsor
- [ ] Organizational templates reviewed (if applicable)
- [ ] Compliance requirements identified
- [ ] Integration targets specified (where brief will be stored/shared)

### Escalation Protocols

If required inputs are unavailable:

1. **Missing Sponsor**: Escalate to requesting party; brief cannot proceed without executive ownership
2. **Undefined Budget**: Generate brief with placeholder; flag for finance review before approval
3. **Incomplete Stakeholders**: Proceed with known stakeholders; add discovery task to brief
4. **Unclear Objectives**: Conduct objective-setting workshop; document outcomes before brief finalization
5. **Unknown Constraints**: Apply industry-standard assumptions; document for validation

---

## Appendix: Project Type Adaptation Matrix

| Project Type | Primary Focus Areas | Unique Sections | Typical Duration |
|--------------|--------------------|-----------------|--------------------|
| Software Development | Technical scope, architecture, testing | Technical requirements, sprint structure, deployment plan | 3-18 months |
| Marketing Campaign | Audience, creative, channels | Media plan, creative brief, measurement framework | 4-16 weeks |
| Product Launch | Go-to-market, readiness | Launch phases, sales enablement, market analysis | 2-6 months |
| Construction | Site, permits, safety | Permit timeline, safety compliance, inspection schedule | 6-36 months |
| Event Planning | Venue, attendees, logistics | Run of show, vendor matrix, contingency scenarios | 2-12 months |
| Research | Methodology, data, analysis | Research design, IRB compliance, publication plan | 3-24 months |
| Manufacturing | Production, quality, supply chain | Production schedule, QC checkpoints, supplier management | 3-18 months |
| Consulting | Client deliverables, methodology | Engagement model, deliverable acceptance, knowledge transfer | 1-12 months |
| Organizational Change | People, process, adoption | Change impact, training plan, adoption metrics | 6-36 months |
| Sales Campaign | Pipeline, targets, enablement | Territory plan, quota allocation, CRM integration | 1-4 quarters |

---

*This skill document version 1.0 | Last updated: March 2026 | Compatible with Manus.im Agent Framework v2.x+*

## Using the Reference Files

- [Brief Best Practices](./references/brief_best_practices.md): Brief Best Practices
- [Brief Components Templates](./references/brief_components_templates.md): Brief Components Templates
- [Brief Creation Process](./references/brief_creation_process.md): Brief Creation Process
- [Brief Vs Other Documents](./references/brief_vs_other_documents.md): Brief Vs Other Documents
- [Project Brief Fundamentals](./references/project_brief_fundamentals.md): Project Brief Fundamentals
