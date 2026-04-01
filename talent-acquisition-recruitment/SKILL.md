---
name: talent-acquisition-recruitment
description: "The Talent Acquisition & Recruitment skill empowers AI agents to execute comprehensive hiring workflows from job requisition to candidate onboarding."
---

# Talent Acquisition & Recruitment

## Overview

This skill provides comprehensive guidance and best practices for this domain.

## 1. Skill Description and Purpose

The Talent Acquisition & Recruitment skill empowers AI agents to execute comprehensive hiring workflows from job requisition to candidate onboarding. This skill encompasses the full recruitment lifecycle including strategic sourcing across multiple channels, candidate screening and assessment, interview coordination, offer management, and onboarding facilitation.

**Why This Skill Is Valuable:**
- Reduces time-to-hire by automating repetitive recruitment tasks and streamlining candidate pipelines
- Improves quality-of-hire through consistent, data-driven screening criteria and structured interview processes
- Enhances candidate experience with timely communication and transparent process management
- Enables scalable hiring operations without proportional headcount increases in recruiting teams
- Supports diversity, equity, and inclusion (DEI) goals through bias-reduced screening methodologies
- Provides actionable recruitment analytics for continuous process improvement

**When to Use This Skill:**
- Opening new job requisitions and defining position requirements
- Executing multi-channel sourcing campaigns across job boards, LinkedIn, referrals, and campus networks
- Screening and ranking candidates against role specifications
- Coordinating interview schedules and managing interviewer panels
- Generating offer packages and negotiating compensation
- Tracking recruitment metrics and optimizing hiring funnels
- Managing Applicant Tracking System (ATS) workflows and data integrity

**Core Methodologies Applied:**
- Competency-based screening using validated assessment criteria
- Behavioral interviewing using STAR (Situation, Task, Action, Result) methodology
- Technical assessments calibrated to role requirements
- Structured interview scorecards for objective candidate comparison
- Employer brand positioning aligned with Employee Value Proposition (EVP)

## 2. Required Inputs/Parameters

### Job Requisition Data
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| job_title | String | Yes | Official position title |
| department | String | Yes | Hiring department or business unit |
| hiring_manager | Object | Yes | Manager details (name, email, ID) |
| job_description | Text | Yes | Full JD including responsibilities, qualifications, and requirements |
| required_skills | Array | Yes | List of mandatory technical and soft skills |
| preferred_skills | Array | No | Nice-to-have qualifications |
| experience_range | Object | Yes | Min/max years of experience (e.g., {min: 3, max: 7}) |
| education_requirements | Array | Yes | Degree levels and fields of study |
| compensation_range | Object | Yes | Salary band with min/mid/max and currency |
| employment_type | Enum | Yes | Full-time, Part-time, Contract, Intern |
| location | Object | Yes | Work location(s) and remote policy |
| target_start_date | Date | Yes | Desired hire start date |
| headcount | Integer | Yes | Number of positions to fill |

### Sourcing Configuration
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| sourcing_channels | Array | Yes | Channels to activate (LinkedIn, Indeed, Glassdoor, referrals, campus, agencies) |
| sourcing_budget | Number | No | Available budget per channel |
| diversity_targets | Object | No | DEI goals for candidate pipeline |
| boolean_search_strings | Array | No | Custom search strings for sourcing platforms |
| competitor_companies | Array | No | Target companies for passive candidate sourcing |

### Screening Criteria
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| knockout_questions | Array | Yes | Disqualifying criteria (visa requirements, location, availability) |
| scoring_rubric | Object | Yes | Weighted criteria for candidate ranking |
| assessment_requirements | Array | No | Required assessments (technical, personality, cognitive) |
| interview_stages | Array | Yes | Interview rounds with types and interviewers |

### ATS Integration
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| ats_system | String | Yes | ATS platform (Greenhouse, Lever, Workday, iCIMS, Taleo) |
| api_credentials | Object | Yes | Authentication details for ATS integration |
| workflow_template | String | No | Predefined hiring workflow ID |

## 3. Expected Outputs/Deliverables

### Sourcing Outputs
- **Candidate Pipeline Report**: Spreadsheet/JSON with sourced candidates including name, contact, source channel, profile URL, current company/title, match score, and engagement status
- **Sourcing Analytics Dashboard**: Metrics by channel including applications received, qualified candidates, cost-per-applicant, and source effectiveness ranking
- **Outreach Sequences**: Personalized email/InMail templates for passive candidate engagement with A/B test variants

### Screening Outputs
- **Ranked Candidate List**: Scored candidates sorted by weighted criteria match with detailed scoring breakdown
- **Screening Summary Reports**: Individual candidate profiles with skills match analysis, experience alignment, and red flag identification
- **Video Screen Transcripts**: Summarized notes from AI-assisted video screenings with sentiment analysis

### Interview Outputs
- **Interview Schedules**: Coordinated calendar invites with interviewer assignments, room/video link bookings, and candidate preparation materials
- **Interview Scorecards**: Standardized evaluation forms with competency ratings, evidence notes, and hiring recommendations
- **Debrief Summary**: Consolidated interviewer feedback with calibrated ratings and consensus recommendation

### Offer & Onboarding Outputs
- **Offer Package Documentation**: Customized offer letters with compensation details, benefits summary, equity grants, and contingencies
- **Negotiation Tracking Log**: Record of offer iterations, candidate counteroffers, and final terms
- **Onboarding Checklist**: Pre-boarding tasks, Day 1 agenda, equipment requests, and system access provisioning

### Analytics Outputs
- **Recruitment Metrics Report**: Time-to-hire, cost-per-hire, offer acceptance rate, source-of-hire distribution, pipeline conversion rates, and quality-of-hire indicators
- **Diversity Analytics**: Pipeline and hiring demographics compared to targets with funnel stage dropout analysis
- **Process Optimization Recommendations**: Data-driven suggestions for bottleneck elimination and conversion improvement

**Quality Standards:**
- All candidate data must comply with GDPR/CCPA data handling requirements
- Screening decisions must be auditable with documented rationale
- Offer documents must be reviewed against compensation policy guardrails
- Metrics must update in real-time with ATS synchronization

## 4. Example Use Cases

### Use Case 1: High-Volume Engineering Hiring Campaign
A technology company needs to hire 25 software engineers within 90 days for a new product launch. The agent activates multi-channel sourcing across LinkedIn Recruiter, GitHub, Stack Overflow, and technical job boards. It generates role-specific boolean search strings, creates personalized outreach sequences, and manages a pipeline of 500+ candidates through automated screening using technical assessment integration. The agent coordinates 150 technical interviews across 10 hiring managers, generates calibrated scorecards, and tracks conversion metrics to optimize the funnel mid-campaign.

### Use Case 2: Executive Search with Confidentiality Requirements
A company seeks a new Chief Financial Officer without alerting current leadership. The agent conducts discreet passive sourcing through executive networks, creates sanitized job specifications, manages candidate communications through anonymous channels, and coordinates interviews off-site. It performs background verification, negotiates complex compensation packages including long-term incentives, and manages stakeholder communication throughout the sensitive search process.

### Use Case 3: Campus Recruitment Program
A consulting firm executes fall campus recruiting across 15 target universities. The agent manages event registrations, resume collection, first-round screening, and super-day coordination. It tracks candidates through multiple interview rounds, generates comparative analytics across schools, and produces offer decisions with exploding offer management. Post-campaign, it analyzes yield rates by school to inform next year's targeting strategy.

### Use Case 4: Diversity-Focused Hiring Initiative
An organization commits to increasing underrepresented groups in technical roles. The agent expands sourcing to diversity-focused job boards (Jopwell, PowerToFly, Fairygodboss), partners with professional associations (NSBE, SWE, SHPE), implements blind resume screening, and tracks demographic metrics at each funnel stage. It identifies and flags potential bias indicators in interview feedback and generates recommendations for process improvements.

## 5. Prerequisites or Dependencies

### System Access Requirements
- **ATS Platform**: Administrative API access to Greenhouse, Lever, Workday, or equivalent with permissions for candidate management, job posting, and reporting
- **LinkedIn Recruiter**: Seat license with InMail credits for outreach campaigns
- **Job Board Accounts**: Posting credits on Indeed, Glassdoor, ZipRecruiter, and specialty boards
- **Assessment Platforms**: Integration with HackerRank, Codility, Criteria Corp, or similar for automated testing
- **Calendar Systems**: OAuth access to Google Calendar or Microsoft Outlook for interview scheduling
- **HRIS Integration**: Read access for organizational data, compensation bands, and approval workflows
- **Background Check Vendors**: API integration with Checkr, HireRight, or equivalent services

### Data Requirements
- Current job architecture with leveling framework and compensation bands
- Approved headcount plan with budget allocation
- Hiring manager availability and delegation of authority limits
- Standard interview question banks by competency
- Employer brand assets (videos, testimonials, culture content)
- Historical hiring data for benchmarking and ML model training

### Compliance Knowledge
- Local employment laws and anti-discrimination regulations
- EEOC/OFCCP reporting requirements (for US federal contractors)
- Data privacy regulations (GDPR, CCPA, PDPA) for candidate data handling
- Immigration requirements and work authorization verification
- Background check consent and adverse action procedures

### Integration Dependencies
- Email/communication platform for candidate correspondence
- Video conferencing tools for remote interviews (Zoom, Teams, Google Meet)
- Document signing platform (DocuSign, Adobe Sign) for offer acceptance
- Onboarding system for new hire provisioning workflows

## References

- [01 Fundamentals Of Talent Acquisition](references/01-fundamentals-of-talent-acquisition.md)
- [02 Sourcing Strategies And Techniques](references/02-sourcing-strategies-and-techniques.md)
- [03 Candidate Experience And Selection](references/03-candidate-experience-and-selection.md)
- [04 Talent Acquisition Technology And Analytics](references/04-talent-acquisition-technology-and-analytics.md)
