---
name: product-requirements-documentation
description: "Product Requirements Documentation is a structured analytical and creative skill that transforms business objectives, user needs, and market opportunities into comprehensive, actionable product specifications."
---

# Product Requirements Documentation

## Overview

This skill provides comprehensive guidance and best practices for this domain.

## 1. Skill Description and Purpose

Product Requirements Documentation is a structured analytical and creative skill that transforms business objectives, user needs, and market opportunities into comprehensive, actionable product specifications. This skill bridges the gap between strategic vision and technical execution by producing documentation that aligns stakeholders and guides development teams.

### Core Capabilities

The skill performs requirements elicitation from multiple sources, prioritizes features using established frameworks, creates detailed user stories and acceptance criteria, defines success metrics and KPIs, identifies technical constraints and dependencies, and produces documentation that meets industry standards for clarity and completeness.

### Documentation Functions

- **Requirements Gathering**: Synthesize inputs from stakeholders, research, and competitive analysis
- **Feature Definition**: Create detailed functional and non-functional requirements
- **User Story Development**: Write user-centered stories with acceptance criteria
- **Prioritization**: Apply frameworks (MoSCoW, RICE, Kano) to rank features
- **Specification Writing**: Produce technical specifications and API contracts
- **Success Metrics**: Define measurable outcomes and evaluation criteria

### When to Use This Skill

Deploy this skill when organizations need to:
- Launch new products or features
- Document requirements for development handoff
- Align cross-functional teams on product scope
- Establish baselines for agile sprint planning
- Create specifications for vendor RFPs
- Document legacy system requirements
- Support product roadmap development

### Value Proposition

This skill accelerates requirements documentation cycles, ensures consistency across product teams, reduces scope creep through precise specifications, and improves development outcomes through clear acceptance criteria and success metrics.

## 2. Required Inputs/Parameters

### Mandatory Inputs

| Parameter | Format | Description |
|-----------|--------|-------------|
| `product_vision` | String/Document | High-level product vision, strategy document, or OKRs |
| `target_users` | JSON | User personas or segment definitions with needs and pain points |
| `scope_definition` | Enum | "new_product", "major_feature", "enhancement", "integration" |
| `document_format` | Enum | "comprehensive_prd", "lean_prd", "user_stories_only", "technical_spec" |

### Conditional Inputs

| Parameter | Required When | Format | Description |
|-----------|---------------|--------|-------------|
| `existing_system_context` | Enhancement/Integration | Document | Current system architecture and capabilities |
| `api_requirements` | Technical spec | Object | API consumers, data formats, integration patterns |
| `regulatory_requirements` | Regulated industry | Document | Compliance requirements affecting product |
| `competitive_analysis` | New product | Document | Competitor feature comparison |

### Optional Inputs

| Parameter | Format | Description |
|-----------|--------|-------------|
| `stakeholder_interviews` | Transcript/Notes | Interview notes from key stakeholders |
| `user_research` | Document | User research findings, survey results, analytics |
| `technical_constraints` | Array | Known technical limitations or dependencies |
| `timeline_constraints` | Object | Release timeline and milestone dates |
| `resource_constraints` | Object | Team capacity, budget limitations |
| `success_metrics_baseline` | Object | Current metrics for comparison |

## 3. Expected Outputs/Deliverables

### Primary Deliverables

**Comprehensive PRD (PDF/DOCX/Confluence)**
- Executive summary and product vision
- Problem statement and opportunity analysis
- User personas and journey maps
- Detailed functional requirements with priorities
- Non-functional requirements (performance, security, scalability)
- User stories with acceptance criteria
- Success metrics and KPIs
- Dependencies and constraints
- Assumptions and risks
- Out-of-scope items
- Glossary and definitions

**User Story Backlog (Jira Export/CSV)**
- Epic definitions with business value
- User stories in standard format ("As a... I want... So that...")
- Acceptance criteria for each story
- Priority rankings (P0, P1, P2)
- Story point estimates (when baseline provided)
- Technical tasks and subtasks
- Dependencies between stories

**Technical Specification (Markdown/DOCX)**
- System architecture context
- Data model requirements
- API specifications (OpenAPI format)
- Integration requirements
- Security requirements
- Performance requirements and SLAs
- Testing requirements

**Success Metrics Framework (Excel/PDF)**
- Primary KPIs with targets
- Secondary metrics for monitoring
- Measurement methodology
- Data collection requirements
- Reporting cadence and stakeholders

### Quality Standards

- All requirements must be testable and measurable
- User stories must follow INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- Acceptance criteria must be specific and unambiguous
- Non-functional requirements must include quantitative targets
- Dependencies must be bidirectionally validated
- All acronyms and technical terms must be defined

## 4. Example Use Cases

### Use Case 1: B2B SaaS Feature Launch

A SaaS company launching a new analytics dashboard feature needs comprehensive requirements documentation. The skill processes stakeholder interview transcripts, user research findings, and competitive analysis to produce a PRD with 47 user stories, prioritized using RICE framework, complete with API specifications for data visualization integrations and success metrics tied to user adoption and retention.

### Use Case 2: Mobile App MVP Definition

A startup needs to define minimum viable product requirements for investor-ready documentation. The skill synthesizes market research, user interviews, and technical feasibility assessment into a lean PRD with prioritized feature list, core user flows, and MVP success criteria that balances market validation needs against development timeline.

### Use Case 3: Enterprise System Integration

An enterprise needs requirements for integrating CRM with ERP system. The skill analyzes existing system documentation, stakeholder requirements, and data governance policies to produce technical specifications including API contracts, data mapping requirements, error handling specifications, and testing requirements.

### Use Case 4: Regulatory Compliance Feature

A fintech company needs to implement new regulatory requirements in their platform. The skill translates regulatory language into specific functional requirements, defines audit trail specifications, creates acceptance criteria that map to compliance checkpoints, and identifies testing requirements for regulatory certification.

### Use Case 5: Platform Migration Requirements

An organization migrating from legacy system to modern platform needs comprehensive requirements documentation. The skill analyzes existing system functionality, identifies feature parity requirements, documents enhancement opportunities, and creates migration success criteria.

## 5. Prerequisites or Dependencies

### Required Access and Permissions

- Product strategy documents and OKRs
- User research repositories and findings
- Existing system documentation
- Stakeholder availability for clarification
- Analytics and usage data (for enhancements)

### Tool Dependencies

- Requirements management tools (Jira, Azure DevOps, Aha!)
- Documentation platforms (Confluence, Notion, Google Docs)
- Diagramming tools (Lucidchart, Figma, Miro)
- API documentation tools (Swagger, Postman)
- Spreadsheet tools for prioritization matrices

### Domain Knowledge Requirements

- Product management methodologies (Agile, Lean)
- User story writing conventions
- Prioritization frameworks (MoSCoW, RICE, WSJF)
- Non-functional requirements standards
- API design principles (REST, GraphQL)

### Collaboration Requirements

- Product manager review and approval cycles
- Engineering feasibility review
- Design review for user experience requirements
- Legal/compliance review for regulated features
- Executive alignment for strategic requirements

### Limitations and Constraints

- Requirements quality depends on input source quality
- Technical feasibility assessment requires engineering input
- Timeline estimates require team velocity data
- Cross-team dependencies require coordination
- Requirements may evolve; document versioning essential

## Using the Reference Files

- [Prd Best Practices Pitfalls](./references/prd_best_practices_pitfalls.md): Prd Best Practices Pitfalls
- [Prd Creation Process](./references/prd_creation_process.md): Prd Creation Process
- [Prd Fundamentals Overview](./references/prd_fundamentals_overview.md): Prd Fundamentals Overview
- [Prd Tools Templates](./references/prd_tools_templates.md): Prd Tools Templates
- [Prd Vs Related Documents](./references/prd_vs_related_documents.md): Prd Vs Related Documents
