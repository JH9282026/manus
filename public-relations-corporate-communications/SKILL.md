---
name: public-relations-corporate-communications
description: The Public Relations & Corporate Communications skill empowers AI agents to deliver comprehensive PR strategy, media relations, crisis communications, and stakeholder engagement capabilities.
---

---
name: Public Relations & Corporate Communications
description: Comprehensive public relations and communications strategy skill enabling media relations, crisis communications, reputation management, and stakeholder engagement to build and protect organizational reputation and brand equity.
---

# Public Relations & Corporate Communications

## Skill Description and Purpose

The Public Relations & Corporate Communications skill empowers AI agents to deliver comprehensive PR strategy, media relations, crisis communications, and stakeholder engagement capabilities. This skill encompasses the complete communications lifecycle from proactive reputation building through crisis response and recovery, enabling organizations to effectively manage their narrative across all stakeholder audiences.

This skill is essential for organizations seeking to build brand awareness, establish thought leadership, manage reputation risks, navigate crises, and communicate effectively with diverse stakeholder groups including media, investors, employees, customers, and communities. The skill enables autonomous development of communications strategies, creation of media engagement programs, crisis preparedness planning, and measurement of communications effectiveness.

**Core Competency Areas:**
- **Media Relations and Press Engagement**: Journalist relationships, media outreach, story placement, and press event management
- **Crisis Communications and Reputation Management**: Crisis preparedness, response protocols, reputation recovery, and issues management
- **Brand Reputation Monitoring and Management**: Reputation tracking, sentiment analysis, brand perception research, and reputation risk management
- **Press Releases and Media Kits**: Press release development, media kit creation, and news announcement strategies
- **Spokesperson Training and Media Coaching**: Executive media training, message discipline, and interview preparation
- **Social Media Crisis Management**: Real-time monitoring, rapid response, social listening, and digital crisis mitigation
- **Stakeholder Communications**: Investor relations support, employee communications, customer communications, and community relations
- **Corporate Messaging and Narrative Development**: Brand narrative, positioning statements, and message architecture
- **Thought Leadership and Executive Visibility**: Executive positioning, speaking engagements, byline articles, and industry influence
- **PR Metrics and Measurement**: Media coverage analysis, sentiment tracking, reach and impressions, and communications ROI

**When to Use This Skill:**
Deploy this skill when developing communications strategy, launching media campaigns, preparing for crises, managing reputation issues, building executive visibility, crafting corporate narratives, planning announcements, or measuring communications effectiveness.

## Required Inputs/Parameters

### Strategic Context Inputs
| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `organization_profile` | JSON object | Company size, industry, geographic presence, and business model | Yes |
| `brand_positioning` | Document/JSON | Brand identity, values, differentiators, and competitive positioning | Yes |
| `strategic_priorities` | Document | Business objectives, growth initiatives, and strategic narrative | Yes |
| `stakeholder_universe` | JSON | Key stakeholder groups, priorities, and relationships | Yes |

### Communications Context Inputs
| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `current_reputation` | Document/data | Reputation research, sentiment data, and brand perception | Recommended |
| `media_landscape` | Document | Key media outlets, journalists, and industry publications | Recommended |
| `communications_history` | Document collection | Past press releases, media coverage, and communications materials | Conditional |
| `crisis_history` | Document | Previous crises, responses, and lessons learned | Conditional |
| `competitive_communications` | Document | Competitor positioning, messaging, and media presence | Recommended |

### Situational Parameters
| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `communications_objective` | String | Proactive (awareness, positioning) or reactive (crisis, issues) | Yes |
| `urgency_level` | Scale (1-10) | Time sensitivity of communications need | Yes |
| `audience_priority` | Ranked list | Primary stakeholder audiences to address | Yes |
| `risk_assessment` | JSON | Potential reputation risks and sensitivities | Recommended |

## Expected Outputs/Deliverables

### Strategic Planning Deliverables
1. **Communications Strategy Document** (25-40 pages)
   - Executive summary with communications vision
   - Situational analysis and reputation assessment
   - Stakeholder analysis and prioritization
   - Strategic communications objectives
   - Message architecture and narrative framework
   - Channel strategy and mix
   - Thought leadership and executive positioning
   - Crisis preparedness overview
   - Measurement framework and KPIs
   - Implementation roadmap and budget

2. **Annual Communications Plan**
   - Communications calendar and key moments
   - Proactive media campaign schedule
   - Thought leadership content calendar
   - Stakeholder engagement timeline
   - Crisis simulation and training schedule
   - Measurement and reporting cadence
   - Budget allocation by initiative
   - Resource and agency requirements

### Media Relations Deliverables
3. **Media Relations Strategy**
   - Target media outlet tiering
   - Journalist relationship mapping
   - Story angle development
   - Exclusive and embargo strategies
   - Press event planning framework
   - Media briefing protocols
   - Editorial calendar alignment
   - Media relationship metrics

4. **Press Materials**
   - Press release templates by announcement type
   - Media kit components and structure
   - Fact sheets and backgrounders
   - Executive biographies
   - Company boilerplate
   - Visual assets and guidelines
   - B-roll and multimedia specifications
   - Press room requirements

### Crisis Communications Deliverables
5. **Crisis Communications Plan** (Comprehensive playbook)
   - Crisis identification and classification
   - Escalation protocols and decision tree
   - Response team structure and roles
   - Holding statements by scenario type
   - Stakeholder notification sequences
   - Media response protocols
   - Social media crisis protocols
   - Legal coordination procedures
   - Post-crisis recovery framework

6. **Crisis Response Materials**
   - Pre-approved holding statements
   - Q&A documents by scenario
   - Key message frameworks
   - Spokesperson assignments
   - Stakeholder communication templates
   - Social media response templates
   - Dark site specifications
   - Crisis contact lists

### Executive Communications Deliverables
7. **Thought Leadership Program**
   - Executive visibility strategy
   - Speaking opportunity targeting
   - Byline article program
   - Podcast and interview strategy
   - Social media presence strategy
   - Industry association involvement
   - Award submission calendar
   - Content calendar and topics

8. **Spokesperson Training Program**
   - Media training curriculum
   - Message development workshops
   - Interview simulation exercises
   - Crisis response drills
   - Social media guidelines for executives
   - Presentation coaching framework
   - Ongoing coaching and feedback

### Stakeholder Communications Deliverables
9. **Stakeholder Communications Framework**
   - Investor communications approach
   - Employee communications strategy
   - Customer communications guidelines
   - Community relations program
   - Government/regulatory communications
   - Partner/supplier communications
   - Channel integration and consistency
   - Feedback and listening mechanisms

10. **Corporate Messaging Architecture**
    - Master narrative and story
    - Positioning statements by audience
    - Key messages and proof points
    - Value proposition messaging
    - Competitive differentiation messages
    - Issue-specific messaging
    - Message testing methodology
    - Message governance process

### Measurement Deliverables
11. **PR Measurement Dashboard**
    - Media coverage metrics (volume, reach, sentiment)
    - Share of voice analysis
    - Message penetration tracking
    - Spokesperson visibility metrics
    - Social media engagement metrics
    - Reputation tracking indicators
    - Campaign-specific KPIs
    - Benchmark comparisons

12. **Communications Audit Framework**
    - Annual audit methodology
    - Stakeholder perception research
    - Media coverage analysis
    - Channel effectiveness assessment
    - Competitive benchmarking
    - Recommendation development
    - Action planning process

### Quality Standards
- All messaging approved through proper governance
- Legal and compliance review integrated
- Consistent voice and tone across materials
- Accessibility standards met
- Multi-channel consistency ensured
- Crisis materials pre-tested
- Measurement tied to business objectives
- Industry best practices followed

## Example Use Cases

### Use Case 1: Corporate Rebrand Launch Campaign
**Scenario**: A technology company completing merger-driven rebrand needs comprehensive communications strategy to launch new brand identity to all stakeholders while maintaining business continuity.

**Application**: The skill develops integrated brand launch communications strategy, creates stakeholder-specific messaging and communication sequences, designs media relations campaign with exclusive announcements, develops employee communications program for brand ambassador activation, creates customer communications addressing continuity and benefits, builds social media launch campaign with brand activation, establishes brand monitoring for sentiment tracking, develops executive visibility program for new brand positioning, and delivers launch campaign achieving 500+ media placements, 85% employee brand comprehension, and positive stakeholder sentiment scores.

### Use Case 2: Crisis Communications Response
**Scenario**: A consumer products company faces viral social media crisis regarding product safety concerns requiring immediate response to protect brand reputation and customer trust.

**Application**: The skill activates crisis communications protocol, conducts rapid situation assessment and stakeholder impact analysis, develops crisis messaging framework with approved statements, creates social media response strategy for real-time engagement, prepares executive spokesperson with media training and Q&A, coordinates stakeholder notification sequence (regulators, retailers, customers), establishes monitoring war room for sentiment tracking, develops recovery communications plan, and delivers crisis response limiting reputation damage, restoring customer confidence within 30 days, and improving crisis preparedness capabilities.

### Use Case 3: Executive Thought Leadership Program
**Scenario**: A B2B software company CEO seeks to establish industry thought leadership position to support enterprise sales, investor relations, and talent attraction.

**Application**: The skill assesses current executive visibility and competitive positioning, develops thought leadership strategy with differentiated point of view, creates content calendar with speaking engagements, byline articles, and podcast appearances, secures keynote opportunities at 6 industry conferences, develops social media strategy for LinkedIn and Twitter engagement, coordinates media opportunities including tier-1 business press, creates measurement framework tracking visibility and business impact, and delivers thought leadership program achieving 300% increase in executive visibility, speaking at 15 events annually, and measurable contribution to enterprise deal flow.

### Use Case 4: IPO Communications Strategy
**Scenario**: A high-growth technology company preparing for IPO needs comprehensive communications strategy to build investment narrative, manage regulatory requirements, and establish public company communications infrastructure.

**Application**: The skill develops pre-IPO communications strategy with quiet period protocols, creates investment narrative and positioning for analyst and investor audiences, designs roadshow presentation and executive preparation, establishes media relations strategy compliant with SEC regulations, develops employee communications addressing IPO implications, creates post-IPO communications infrastructure and governance, builds investor relations function integration, implements crisis preparedness for public company exposure, and delivers IPO communications program supporting successful offering with strong analyst coverage and employee understanding.

### Use Case 5: Reputation Recovery Program
**Scenario**: A financial services company needs to rebuild reputation following regulatory enforcement action and negative media coverage, re-establishing trust with customers, regulators, and employees.

**Application**: The skill conducts comprehensive reputation assessment and stakeholder impact analysis, develops reputation recovery strategy with phased approach, creates accountability communications acknowledging issues and actions taken, establishes proactive media relations focusing on remediation progress, develops customer communications restoring trust and demonstrating commitment, builds employee communications addressing concerns and culture change, creates thought leadership program demonstrating reformed practices, implements reputation monitoring with recovery metrics, and delivers reputation recovery program achieving measurable sentiment improvement, restored regulatory relationships, and employee confidence within 18 months.

## Prerequisites or Dependencies

### Knowledge Prerequisites
- Public relations principles and best practices
- Media relations and journalism understanding
- Crisis communications methodologies
- Corporate communications fundamentals
- Social media strategy and management
- Brand management principles
- Stakeholder engagement theory
- Communications measurement and analytics

### Data and System Requirements
- Media monitoring and analytics platforms
- Social listening tools
- Press release distribution services
- Media database and journalist contacts
- Content management systems
- Digital asset management
- Survey and research tools
- Analytics and reporting platforms

### Tool Dependencies
- Media monitoring services (Meltwater, Cision, Muck Rack)
- Social listening platforms (Brandwatch, Sprout Social)
- Press release distribution (PR Newswire, Business Wire)
- Media database services
- Content creation and design tools
- Video production capabilities
- Survey and research platforms
- Measurement and dashboard tools

### Stakeholder Access Requirements
- CEO and executive team for messaging approval
- Legal counsel for compliance and risk review
- Marketing for brand alignment
- Investor relations for financial communications
- HR for employee communications
- Customer success for customer communications
- Business units for operational context

### Integration Dependencies
- Marketing for brand and campaign alignment
- Legal for compliance and review processes
- HR for internal communications
- Investor relations for financial messaging
- Customer success for customer communications
- Product/Operations for factual accuracy
- IT for communications technology
- Compliance for regulated communications

### Environmental Considerations
- Industry regulatory environment
- Competitive communications landscape
- Media environment and journalist relationships
- Social media platform dynamics
- Stakeholder expectations and sensitivities
- Cultural and geographic considerations
- Political and economic context
- Technology and communication trends
