---
name: project-planning-execution
description: "The Project Planning & Execution skill enables AI agents to manage the complete project lifecycle from initiation through closure using industry-standard methodologies."
---

# Project Planning & Execution

## Overview

This skill provides comprehensive guidance and best practices for this domain.

## 1. Skill Description and Purpose

The Project Planning & Execution skill enables AI agents to manage the complete project lifecycle from initiation through closure using industry-standard methodologies. This skill encompasses scope definition, schedule development, resource planning, risk management, stakeholder communication, and project control to deliver successful project outcomes consistently.

**Why This Skill Is Valuable:**
- Ensures projects deliver intended outcomes within agreed constraints
- Provides structured approach reducing project failure rates significantly
- Enables proactive risk management addressing issues before they impact delivery
- Improves resource utilization through data-driven planning and allocation
- Creates transparency for stakeholders through consistent reporting and communication
- Builds organizational project delivery capability through repeatable processes
- Supports portfolio prioritization and capacity planning across initiatives

**When to Use This Skill:**
- Initiating new projects with charter development and stakeholder identification
- Creating detailed project plans including scope, schedule, budget, and resources
- Developing Work Breakdown Structures (WBS) decomposing deliverables
- Building project schedules with dependencies, milestones, and critical path analysis
- Planning and allocating resources across project activities
- Identifying, assessing, and managing project risks
- Managing stakeholder communication and engagement
- Monitoring project progress and implementing corrective actions
- Executing formal project closure with lessons learned

**Core Methodologies Applied:**
- Project Management Body of Knowledge (PMBOK) for comprehensive PM practices
- PRINCE2 for controlled project delivery with defined stages
- Agile/Scrum for iterative delivery where appropriate
- Critical Path Method (CPM) for schedule optimization
- Earned Value Management (EVM) for performance measurement
- Risk management using probability-impact assessment

## 2. Required Inputs/Parameters

### Project Initiation Inputs
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| project_request | File | Yes | Business case or project request documentation |
| strategic_alignment | Object | Yes | Connection to organizational strategy and objectives |
| sponsor_information | Object | Yes | Project sponsor with authority and accountability |
| preliminary_scope | Object | Yes | High-level scope statement and boundaries |
| constraints | Array | Yes | Known constraints (budget, timeline, resources, regulations) |
| assumptions | Array | Yes | Planning assumptions requiring validation |
| success_criteria | Array | Yes | Measurable criteria defining project success |

### Planning Inputs
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| deliverables | Array | Yes | Required project outputs and outcomes |
| stakeholder_register | File | Yes | Stakeholder identification with influence and interest |
| resource_pool | File | Yes | Available resources with skills and availability |
| historical_data | File | No | Similar project data for estimation reference |
| organizational_assets | File | No | Templates, procedures, and lessons learned repository |
| procurement_requirements | Array | No | External goods/services needed |

### Scheduling Parameters
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| milestone_dates | Array | Yes | Key dates including deadline constraints |
| dependency_rules | Object | Yes | Predecessor/successor relationship types |
| calendar_configuration | Object | Yes | Working days, holidays, resource calendars |
| estimation_method | Enum | Yes | Estimation approach (analogous, parametric, three-point, expert) |
| buffer_strategy | Object | No | Contingency and management reserve approach |

### Risk Management Parameters
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| risk_categories | Array | Yes | Risk taxonomy for systematic identification |
| probability_scale | Object | Yes | Probability rating scale with definitions |
| impact_scale | Object | Yes | Impact rating scale by objective (scope, time, cost, quality) |
| risk_tolerance | Object | Yes | Organizational risk appetite thresholds |
| response_strategies | Array | Yes | Available response types (avoid, mitigate, transfer, accept) |

### Monitoring Parameters
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| reporting_frequency | Enum | Yes | Status reporting cadence (weekly, bi-weekly, monthly) |
| kpi_definitions | Array | Yes | Project health metrics with formulas and thresholds |
| change_control_process | Object | Yes | Change request and approval procedures |
| escalation_matrix | Object | Yes | Issue escalation paths with authority levels |

## 3. Expected Outputs/Deliverables

### Initiation Outputs
- **Project Charter**: Formal authorization document with objectives, scope summary, milestones, budget, roles, and success criteria
- **Stakeholder Analysis**: Comprehensive stakeholder register with engagement strategy by stakeholder
- **Business Case Summary**: Concise justification for project investment with expected benefits
- **Project Organization Chart**: Visual representation of project team structure and reporting
- **Communication Plan**: Stakeholder communication requirements, frequency, channels, and responsibility

### Planning Outputs
- **Project Management Plan**: Integrated plan encompassing all subsidiary plans
- **Scope Statement**: Detailed scope definition with deliverables, acceptance criteria, and exclusions
- **Work Breakdown Structure (WBS)**: Hierarchical decomposition of scope into manageable work packages
- **WBS Dictionary**: Detailed description of each WBS element with effort, duration, and resources
- **Project Schedule**: Gantt chart with activities, dependencies, durations, resources, and critical path
- **Resource Plan**: Resource assignments with loading profiles and capacity analysis
- **Budget**: Detailed cost estimate with contingency and cash flow projection
- **Risk Register**: Identified risks with assessment, response plans, and owners
- **Quality Plan**: Quality standards, assurance activities, and acceptance criteria

### Execution Outputs
- **Task Assignments**: Work authorizations with clear deliverables and deadlines
- **Meeting Minutes**: Documented decisions, action items, and issues from project meetings
- **Deliverable Documentation**: Project outputs meeting defined acceptance criteria
- **Change Requests**: Formal requests for scope, schedule, or budget modifications
- **Issue Log**: Tracked issues with ownership, actions, and resolution status

### Monitoring Outputs
- **Project Status Report**: Regular report with accomplishments, upcoming activities, risks, issues, and metrics
- **Earned Value Report**: EVM metrics (PV, EV, AC, SV, CV, SPI, CPI) with trend analysis
- **Risk Status Report**: Updated risk register with newly identified risks and response progress
- **Schedule Variance Analysis**: Comparison of planned versus actual progress with explanations
- **Forecast Update**: Revised estimates at completion (EAC) with underlying assumptions

### Closure Outputs
- **Final Project Report**: Comprehensive summary of project performance against objectives
- **Lessons Learned Document**: Documented successes, challenges, and recommendations for future projects
- **Deliverable Acceptance**: Formal sign-off on all project deliverables
- **Resource Release**: Documentation releasing project resources to functional managers
- **Archive Package**: Organized project documentation for organizational records

**Quality Standards:**
- Project charter must be formally approved by sponsor before planning proceeds
- WBS must decompose to work packages of 8-80 hours (or appropriate size for project)
- Schedule must show valid critical path with no open-ended activities
- Risk register must be reviewed and updated at minimum weekly
- Status reports must be distributed per communication plan without exception
- All changes must flow through formal change control process

## 4. Example Use Cases

### Use Case 1: Enterprise Software Implementation
A company implements a new ERP system affecting all business functions. The agent develops comprehensive project charter with executive sponsorship, creates WBS covering software configuration, data migration, integration, testing, training, and go-live, builds schedule with parallel workstreams and critical path identification, develops risk register addressing technical, organizational, and vendor risks, creates communication plan for 500+ affected stakeholders, and manages 18-month implementation through staged go-lives.

### Use Case 2: Product Launch Project
A consumer products company launches a new product line. The agent coordinates cross-functional project spanning R&D, manufacturing, marketing, and sales, creates integrated schedule aligning product development with marketing campaigns and supply chain readiness, manages dependencies across 15 functional workstreams, tracks milestones against launch date, addresses supply chain risks through contingency planning, and delivers successful launch meeting revenue targets.

### Use Case 3: Facility Construction Project
A company builds a new manufacturing facility. The agent develops project plan covering design, permitting, construction, equipment installation, and commissioning, creates detailed schedule with construction sequencing and long-lead equipment procurement, manages contractor relationships and change orders, tracks budget using earned value management, coordinates inspections and regulatory approvals, and delivers facility on schedule within 3% of budget.

### Use Case 4: Business Process Transformation
A company redesigns core business processes for efficiency. The agent creates project plan for process assessment, design, piloting, and rollout, manages change resistance through stakeholder engagement and communication, coordinates process changes with IT system modifications, develops training program for affected employees, manages pilot phases with feedback incorporation, and achieves 30% efficiency improvement through successful rollout.

### Use Case 5: Regulatory Compliance Program
A company responds to new regulatory requirements with compliance deadline. The agent develops compliance project plan with regulatory interpretation, gap assessment, remediation, and certification phases, creates risk-based prioritization of compliance activities, manages external consultant and auditor relationships, tracks compliance across multiple business units, coordinates regulatory submissions, and achieves certification before deadline.

## 5. Prerequisites or Dependencies

### System Access Requirements
- **Project Management Platform**: Access to MS Project, Smartsheet, Asana, Monday.com, or equivalent
- **Collaboration Platform**: Access to SharePoint, Confluence, or equivalent for documentation
- **Communication Platform**: Access to email, Teams/Slack for project communications
- **Resource Management System**: Access to resource scheduling and capacity tools
- **Financial System**: Access for budget tracking and cost recording
- **Risk Management Tool**: Access to risk register platform if separate from PM tool

### Data Requirements
- Historical project data for estimation benchmarking
- Resource availability and allocation data
- Organizational calendar with holidays and blackout periods
- Vendor and contractor information for procurement planning
- Lessons learned repository from prior projects
- Organizational process assets (templates, procedures, standards)

### Organizational Dependencies
- Project sponsor with authority and budget accountability
- Resource commitment from functional managers
- Governance structure for decision-making and escalation
- Change control board for scope change approval
- PMO support for methodology and tool guidance

### Knowledge Requirements
- Project management methodology (PMBOK, PRINCE2, or organizational standard)
- Scheduling techniques (CPM, PERT, resource leveling)
- Earned value management for performance measurement
- Risk management principles and techniques
- Stakeholder management and communication strategies
- Change management for organizational adoption

### Integration Dependencies
- Calendar integration for scheduling and resource management
- Financial system integration for budget tracking
- Time tracking system for actual effort capture
- Document management for deliverable storage
- Reporting platform for status dashboards
- Email/notification system for automated communications

## References

- [Execution Challenges](references/execution_challenges.md)
- [Methodologies Approaches](references/methodologies_approaches.md)
- [Monitoring Control Techniques](references/monitoring_control_techniques.md)
- [Planning Execution Fundamentals](references/planning_execution_fundamentals.md)
- [Tools Best Practices](references/tools_best_practices.md)
