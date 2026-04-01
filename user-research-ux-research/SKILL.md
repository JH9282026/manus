---
name: user-research-ux-research
description: "User Research & UX Research is a systematic approach to understanding users, their behaviors, motivations, pain points, and needs through various qualitative and quantitative methods."
---

# User Research & UX Research

## Overview

This skill provides comprehensive guidance and best practices for this domain.

## Skill Description and Purpose

User Research & UX Research is a systematic approach to understanding users, their behaviors, motivations, pain points, and needs through various qualitative and quantitative methods. This skill enables the collection, analysis, and synthesis of user data to inform product strategy, design decisions, and experience optimization.

The primary purpose of this skill is to bridge the gap between business objectives and user needs by generating actionable insights that drive user-centered design. It encompasses the full spectrum of research activities from discovery research (understanding who users are and what they need) to evaluative research (testing solutions and measuring effectiveness).

This skill should be deployed when:
- Launching new products or features requiring user validation
- Identifying usability issues in existing products
- Understanding why users behave in certain ways
- Validating design hypotheses before development investment
- Measuring user satisfaction and experience quality
- Creating data-driven personas and journey maps
- Optimizing conversion funnels and user flows
- Benchmarking against competitors from a user experience perspective

The value proposition lies in reducing product development risk, increasing user adoption and retention, improving customer satisfaction scores, and ultimately driving business outcomes through superior user experiences.

## Required Inputs/Parameters

### Primary Inputs

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `research_objective` | String | Clear statement of what the research aims to discover or validate | Yes |
| `target_user_segment` | Object | Demographics, psychographics, and behavioral characteristics of target users | Yes |
| `product_context` | Object | Product/service description, current state, and business goals | Yes |
| `research_scope` | Enum | "discovery", "evaluative", "generative", or "comprehensive" | Yes |
| `timeline` | Object | Start date, end date, and key milestones | Yes |
| `budget_constraints` | Object | Available budget and resource limitations | No |

### Secondary Inputs

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `existing_data` | Array | Previous research, analytics data, support tickets, or user feedback | No |
| `competitor_list` | Array | Competitors to include in benchmarking analysis | No |
| `prototype_urls` | Array | Links to prototypes or products for usability testing | No |
| `success_metrics` | Array | KPIs to track (e.g., task completion rate, SUS score, NPS) | No |
| `stakeholder_requirements` | Object | Specific questions or concerns from stakeholders | No |
| `recruitment_criteria` | Object | Specific screening criteria for participant selection | No |

### Data Format Specifications

- User segments should include: age range, occupation, technical proficiency, usage frequency, and behavioral patterns
- Prototypes must be accessible via URL or uploaded as interactive files (Figma, InVision, or HTML)
- Existing data should be provided in CSV, JSON, or structured document formats
- Timeline should specify research phases: planning, recruitment, fieldwork, analysis, and reporting

## Expected Outputs/Deliverables

### Primary Deliverables

1. **Research Report** (PDF/Markdown, 15-30 pages)
   - Executive summary with key findings
   - Methodology documentation
   - Detailed findings organized by research questions
   - Statistical analysis where applicable
   - Actionable recommendations prioritized by impact

2. **User Personas** (Visual document + data files)
   - 3-5 validated personas with demographic and psychographic profiles
   - Goals, motivations, frustrations, and behaviors
   - Quotes and narrative descriptions
   - Persona comparison matrix

3. **User Journey Maps** (Visual diagrams)
   - Current-state journey maps showing touchpoints, emotions, and pain points
   - Future-state journey maps with opportunity areas highlighted
   - Service blueprints connecting user actions to backend processes

4. **Usability Assessment Report** (if evaluative research)
   - Task success rates and completion times
   - Error frequency and severity classifications
   - System Usability Scale (SUS) scores
   - Heuristic evaluation findings using Nielsen's 10 heuristics
   - Prioritized issue list with severity ratings (critical, major, minor)

### Secondary Deliverables

5. **Empathy Maps** - Visual artifacts capturing user thoughts, feelings, actions, and pain points
6. **A/B Test Results** - Statistical analysis of variant performance with confidence intervals
7. **Competitive UX Benchmark** - Feature comparison matrix and experience ratings
8. **Research Repository Update** - Organized findings for future reference and meta-analysis
9. **Stakeholder Presentation** - Executive-level slides summarizing insights and recommendations

### Quality Standards

- All findings must be supported by minimum 5 user data points
- Statistical claims require 95% confidence level
- Usability issues must follow severity rating standards (cosmetic to critical)
- Recommendations must include effort-impact assessment
- All deliverables must be accessible (WCAG 2.1 AA compliant)

## Example Use Cases

### Use Case 1: E-commerce Checkout Optimization

**Scenario**: An online retailer experiences 68% cart abandonment rate and needs to understand why users fail to complete purchases.

**Approach**:
- Conduct 15 moderated usability tests observing users complete purchase tasks
- Deploy exit-intent surveys capturing abandonment reasons
- Analyze session recordings and heatmaps from 500+ checkout sessions
- Perform heuristic evaluation of checkout flow against best practices

**Outcome**: Identification of 12 usability issues including confusing shipping options, hidden fees appearing late, and mandatory account creation. Recommendations led to 23% improvement in checkout completion.

### Use Case 2: B2B SaaS Onboarding Experience

**Scenario**: A project management software company sees 40% of trial users never complete onboarding and wants to improve activation rates.

**Approach**:
- Conduct 20 semi-structured interviews with churned trial users
- Create empathy maps for three user segments (individual users, team leads, administrators)
- Map current onboarding journey identifying friction points
- A/B test three onboarding flow variations with 1,000 users per variant

**Outcome**: Discovery that users felt overwhelmed by features. Simplified progressive onboarding increased activation by 35%.

### Use Case 3: Mobile Banking App Redesign

**Scenario**: A regional bank plans to redesign their mobile app and needs to understand current user frustrations and unmet needs.

**Approach**:
- Analyze 2,000 app store reviews using sentiment analysis
- Conduct contextual inquiry with 10 users observing real banking tasks
- Develop 4 data-driven personas representing primary user segments
- Create current and future-state journey maps for key tasks (check balance, transfer money, pay bills)
- Benchmark UX against 5 competitor banking apps

**Outcome**: Comprehensive redesign brief with validated priorities, leading to 4.2 to 4.7 star rating improvement post-launch.

### Use Case 4: Healthcare Patient Portal Accessibility

**Scenario**: A healthcare provider needs to ensure their patient portal is accessible and usable for elderly patients and those with disabilities.

**Approach**:
- Recruit 12 participants including users with visual, motor, and cognitive impairments
- Conduct accessibility audit against WCAG 2.1 AA standards
- Perform usability testing with assistive technology users
- Develop accessibility-focused personas and journey maps

**Outcome**: Identified 47 accessibility issues with remediation roadmap, ensuring compliance and improved experience for 15% of user base.

## Prerequisites or Dependencies

### Required Tools and Platforms

| Tool Category | Recommended Options | Purpose |
|---------------|---------------------|---------|
| User Testing | UserTesting, Lookback, Maze | Remote moderated and unmoderated testing |
| Survey | Typeform, SurveyMonkey, Qualtrics | Survey deployment and analysis |
| Analytics | Google Analytics, Mixpanel, Amplitude | Behavioral data collection |
| Session Recording | Hotjar, FullStory, LogRocket | Qualitative behavior observation |
| Prototyping | Figma, InVision, Axure | Interactive prototype testing |
| Research Repository | Dovetail, Notion, Airtable | Findings storage and synthesis |

### Required Access and Permissions

- User recruitment panel access or customer database access for participant sourcing
- Product analytics dashboard access for behavioral data
- Prototype or staging environment access for testing
- Calendar and video conferencing tools for interview scheduling
- Legal approval for participant consent and data handling

### Prior Knowledge and Skills

- Understanding of cognitive psychology and human-computer interaction principles
- Proficiency in qualitative coding and thematic analysis
- Statistical literacy for quantitative data interpretation
- Familiarity with accessibility standards and inclusive design
- Interview and facilitation techniques
- Synthesis and storytelling skills for insight communication

### Data Requirements

- Minimum 5-8 participants per user segment for qualitative research
- Minimum 100 responses for statistically significant survey results
- 30+ days of analytics data for behavioral pattern analysis
- Access to customer support tickets and feedback for secondary research

### Ethical Considerations

- IRB approval or equivalent ethical review for academic contexts
- GDPR/CCPA compliant data collection and storage procedures
- Informed consent protocols with clear data usage explanations
- Participant compensation guidelines and fair incentive structures
- Data anonymization and secure storage protocols

## Using the Reference Files

- [./references/best_practices.md](./references/best_practices.md): Best Practices
- [./references/fundamentals.md](./references/fundamentals.md): Fundamentals
- [./references/methodologies_and_frameworks.md](./references/methodologies_and_frameworks.md): Methodologies And Frameworks
- [./references/research_methods.md](./references/research_methods.md): Research Methods
- [./references/tools_and_resources.md](./references/tools_and_resources.md): Tools And Resources

## References

- [Best Practices](references/best_practices.md)
- [Fundamentals](references/fundamentals.md)
- [Methodologies And Frameworks](references/methodologies_and_frameworks.md)
- [Research Methods](references/research_methods.md)
- [Tools And Resources](references/tools_and_resources.md)
