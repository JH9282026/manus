# Research Operations (ReOps)

Scaling user research through systems, tools, and processes for participant management, knowledge management, and operational efficiency.

---

## Participant Management

### Building a Participant Database

**Purpose:** Maintain a pool of qualified, engaged participants for ongoing research.

**Database Structure:**

**Core Fields:**
- **Contact Information:** Name, email, phone
- **Demographics:** Age, location, gender, occupation
- **Behavioral:** Product usage frequency, expertise level, tenure
- **Psychographic:** Goals, motivations, pain points
- **Segmentation:** User type, persona, customer tier
- **Participation History:** Studies participated in, dates, compensation
- **Preferences:** Availability, preferred communication, incentive preferences
- **Consent:** Research consent status, recording permissions, data retention

**Example Database Schema (Airtable/Notion):**

| Field | Type | Example |
|-------|------|----------|
| Participant ID | Auto-number | P001 |
| Name | Text | Sarah Johnson |
| Email | Email | sarah@example.com |
| Phone | Phone | +1-555-0123 |
| Age | Number | 34 |
| Location | Text | San Francisco, CA |
| Role | Select | Product Manager |
| Company Size | Select | 50-200 employees |
| Product Usage | Select | Daily |
| Tenure | Select | 1-2 years |
| User Segment | Select | Power User |
| Participation History | Linked Records | [Study 1, Study 3] |
| Last Participated | Date | 2026-02-15 |
| Consent Status | Checkbox | ✓ |
| Preferred Incentive | Select | Amazon Gift Card |
| Notes | Long text | Very articulate, great for interviews |

**Tools:**
- **Airtable:** Flexible database, forms for intake, automations
- **Notion:** Database + docs, good for small teams
- **Google Sheets:** Simple, free, limited functionality
- **Dedicated platforms:** User Interviews, Respondent (built-in databases)

### Recruitment Workflows

**Recruitment Sources:**

**1. Existing User Base**
- **Pros:** Familiar with product, easy to reach, authentic feedback
- **Cons:** May not represent prospects, potential bias
- **Methods:** Email campaigns, in-app messages, customer success outreach

**2. Recruitment Platforms**
- **User Interviews:** Large panel, screening, scheduling, incentives
- **Respondent:** B2B focus, high-quality professionals
- **Ethnio:** Intercept screeners, panel management
- **Pros:** Fast, diverse, managed incentives
- **Cons:** Cost ($100-300 per participant), less engaged

**3. Social Media & Communities**
- **LinkedIn:** Professional audiences, B2B
- **Reddit:** Niche communities, authentic users
- **Facebook Groups:** Consumer audiences
- **Slack/Discord:** Product-specific communities
- **Pros:** Targeted, engaged, low cost
- **Cons:** Time-consuming, variable quality

**4. Referrals**
- **Snowball sampling:** Ask participants to refer others
- **Employee networks:** Leverage team connections
- **Pros:** High-quality, trusted
- **Cons:** Limited scale, potential bias

**Screening Process:**

**1. Create Screener Survey**

**Screener Best Practices:**
- Keep it short (5-10 questions, <3 min)
- Mix qualifying and disqualifying questions
- Avoid leading questions
- Include attention checks
- End with scheduling availability

**Example Screener (SaaS Product Research):**

```
1. What is your current role?
   [ ] Product Manager
   [ ] Designer
   [ ] Engineer
   [ ] Other: _______
   [Qualify: Product Manager, Designer]

2. How often do you use project management tools?
   [ ] Daily
   [ ] Weekly
   [ ] Monthly
   [ ] Rarely/Never
   [Qualify: Daily, Weekly]

3. Which project management tools do you currently use? (Select all that apply)
   [ ] Asana
   [ ] Jira
   [ ] Trello
   [ ] Monday.com
   [ ] Other: _______
   [Qualify: Any selection]

4. How long have you been using project management tools?
   [ ] Less than 6 months
   [ ] 6 months - 1 year
   [ ] 1-3 years
   [ ] 3+ years
   [Qualify: 6 months+]

5. Have you participated in user research in the past 6 months?
   [ ] Yes
   [ ] No
   [Disqualify if Yes - avoid professional participants]

6. What days/times are you available for a 45-minute video call?
   [Open text or calendar picker]
```

**2. Review Responses**

- Filter by qualifying criteria
- Aim for diversity (roles, experience levels, tools used)
- Flag edge cases or interesting profiles
- Prioritize based on research needs

**3. Invite Participants**

**Invitation Email Template:**

```
Subject: Invitation to participate in user research ($100 Amazon gift card)

Hi [Name],

Thank you for your interest in participating in our research study!

Based on your responses, you're a great fit. We'd love to hear about your experience with project management tools.

Details:
- Duration: 45 minutes
- Format: Video call (Zoom)
- Compensation: $100 Amazon gift card
- Timeline: Sessions happening [Date range]

Next steps:
1. Review and sign the consent form: [Link]
2. Schedule your session: [Calendly link]

If you have any questions, feel free to reply to this email.

Looking forward to speaking with you!

Best,
[Your name]
[Your title]
```

**4. Confirm and Remind**

**Confirmation Email (immediately after scheduling):**
```
Subject: Confirmed: User research session on [Date/Time]

Hi [Name],

Your session is confirmed!

Date/Time: [Date/Time with timezone]
Duration: 45 minutes
Zoom Link: [Link]

What to expect:
- We'll ask about your experience with project management tools
- No preparation needed—just your honest feedback
- The session will be recorded (with your consent)

If you need to reschedule, please let me know ASAP.

See you soon!

Best,
[Your name]
```

**Reminder Email (24 hours before):**
```
Subject: Reminder: User research session tomorrow at [Time]

Hi [Name],

Just a friendly reminder about your session tomorrow:

Date/Time: [Date/Time with timezone]
Zoom Link: [Link]

Looking forward to it!

Best,
[Your name]
```

**5. Handle No-Shows**

**Strategies to Reduce No-Shows:**
- Send reminders (24 hours and 1 hour before)
- Confirm via multiple channels (email + SMS)
- Overbook by 10-20%
- Offer flexible rescheduling
- Build rapport in confirmation emails

**No-Show Follow-Up:**
```
Subject: We missed you today

Hi [Name],

We missed you at today's session. I understand things come up!

If you're still interested in participating, we have a few slots available:
- [Option 1]
- [Option 2]
- [Option 3]

Let me know if any of these work for you.

Best,
[Your name]
```

### Incentive Management

**Incentive Guidelines:**

**Standard Rates (US, 2026):**
- **15-30 min session:** $50-75
- **45-60 min session:** $75-150
- **90 min session:** $150-250
- **Diary study (1 week):** $100-200
- **Diary study (2-4 weeks):** $200-400

**Adjustments:**
- **B2B professionals:** +50-100% (harder to recruit)
- **Executives/specialists:** +100-200%
- **Existing customers:** Can be lower (goodwill, product credits)
- **Geographic:** Adjust for cost of living

**Incentive Types:**

**1. Cash (Preferred)**
- **Methods:** PayPal, Venmo, Zelle, bank transfer
- **Pros:** Universal, flexible, fast
- **Cons:** Tax implications (1099 if >$600/year)

**2. Gift Cards**
- **Options:** Amazon, Visa, Target, Starbucks
- **Pros:** Easy to distribute, no tax reporting
- **Cons:** Less flexible than cash

**3. Product Credits**
- **Use case:** Existing customers
- **Pros:** Low cost, increases engagement
- **Cons:** Only valuable to users, may bias feedback

**4. Donations**
- **Use case:** Altruistic participants
- **Pros:** Appeals to some segments
- **Cons:** Less motivating for most

**Distribution Workflow:**

1. **Collect payment info** (during scheduling or after session)
2. **Process incentives** (within 1 week of participation)
3. **Send confirmation** ("Your $100 Amazon gift card has been sent to...")
4. **Track in database** (date sent, amount, method)

**Tools:**
- **Tremendous:** Automated gift card distribution
- **Rybbon:** Digital rewards platform
- **Manual:** Spreadsheet + manual sending (small scale)

### GDPR and Privacy Compliance

**Data Collection Consent:**

**Consent Form Elements:**
- Purpose of research
- How data will be used
- Who will have access
- Data retention period
- Right to withdraw
- Contact information

**Example Consent Form:**

```
User Research Consent Form

Purpose:
We are conducting research to improve our product. Your participation will help us understand user needs and experiences.

What to Expect:
- 45-minute video interview
- Questions about your experience with [product category]
- Session will be recorded (video and audio)

Data Usage:
- Recordings and notes will be used for internal research only
- Data will be anonymized in reports and presentations
- Recordings will be stored securely and deleted after [X months/years]
- Only the research team will have access to raw data

Your Rights:
- Participation is voluntary
- You can withdraw at any time without penalty
- You can request deletion of your data
- You can decline to answer any question

Compensation:
- You will receive a $100 Amazon gift card within 1 week of participation

Contact:
If you have questions, contact [email]

Consent:
[ ] I consent to participate in this research
[ ] I consent to being recorded (video and audio)
[ ] I consent to anonymized quotes being used in reports

Name: _______________________
Signature: ___________________
Date: _______________________
```

**GDPR Compliance:**

**Key Requirements:**
- **Lawful basis:** Consent or legitimate interest
- **Data minimization:** Collect only what's needed
- **Purpose limitation:** Use data only for stated purpose
- **Storage limitation:** Delete data when no longer needed
- **Right to access:** Participants can request their data
- **Right to erasure:** Participants can request deletion
- **Data security:** Protect data from unauthorized access

**Implementation:**
- Use consent management tools (Jotform, Typeform with GDPR features)
- Store data securely (encrypted, access-controlled)
- Anonymize data in reports (remove names, emails, identifying details)
- Set data retention policies (e.g., delete recordings after 2 years)
- Provide easy way to request data deletion

---

## Research Repository

### Purpose and Benefits

**Why Build a Repository:**
- **Centralize knowledge:** All research in one place
- **Enable discovery:** Find past insights easily
- **Avoid duplication:** Check if question already answered
- **Onboard new team members:** Learn from past research
- **Track trends:** See how insights evolve over time
- **Democratize access:** Make research available to all

### What to Store

**Research Artifacts:**

**1. Study Plans**
- Research briefs
- Discussion guides
- Test scripts
- Screeners

**2. Raw Data**
- Recordings (video/audio)
- Transcripts
- Field notes
- Survey responses
- Diary entries

**3. Synthesis Artifacts**
- Affinity maps
- Journey maps
- Personas
- Thematic analysis
- Coded transcripts

**4. Deliverables**
- Research reports
- Presentation decks
- Highlight reels
- Executive summaries

**5. Metadata**
- Study date and duration
- Participants (anonymized)
- Research questions
- Methods used
- Product area
- Tags and categories

### Repository Structure

**Organizational Approaches:**

**1. By Product Area**
```
/Onboarding
  /2026-Q1-Onboarding-Usability-Test
  /2025-Q4-Onboarding-Interviews
/Dashboard
  /2026-Q2-Dashboard-Redesign-Research
/Mobile App
  /2026-Q1-Mobile-Performance-Study
```

**2. By Research Type**
```
/Interviews
  /2026-Q1-Onboarding-Interviews
  /2026-Q2-Power-User-Interviews
/Usability Tests
  /2026-Q1-Dashboard-Usability-Test
/Surveys
  /2026-Q1-NPS-Survey
```

**3. By Date**
```
/2026
  /Q1
    /Onboarding-Interviews
    /Dashboard-Usability-Test
  /Q2
    /Mobile-Performance-Study
```

**Recommended: Hybrid Approach**
- Primary organization by product area
- Tagging by research type, date, themes
- Search functionality for discovery

### Tagging and Metadata

**Tag Categories:**

**1. Product Area**
- Onboarding, Dashboard, Mobile, Settings, etc.

**2. Research Type**
- Interview, Usability Test, Survey, Diary Study, Ethnography

**3. User Segment**
- New Users, Power Users, Enterprise, SMB, Free, Paid

**4. Themes**
- Navigation, Performance, Collaboration, Pricing, Support

**5. Date**
- Year, Quarter, Month

**6. Status**
- In Progress, Complete, Archived

**Example Metadata:**
```
Study: Onboarding Usability Test
Date: 2026-03-15
Product Area: Onboarding
Research Type: Usability Test
User Segment: New Users
Themes: Navigation, Confusion, First Impressions
Participants: 8
Researcher: Sarah Johnson
Status: Complete
Key Insights: Users overwhelmed by information, unclear next steps
```

### Tools and Platforms

**Dedicated Research Repositories:**

**1. Dovetail**
- **Strengths:** Video clips, tagging, search, collaboration
- **Use case:** Teams doing frequent qualitative research
- **Pricing:** $29-99/user/month

**2. Aurelius**
- **Strengths:** Tagging, synthesis, reporting
- **Use case:** Research-heavy organizations
- **Pricing:** $80-200/user/month

**3. Condens**
- **Strengths:** Transcription, tagging, repository
- **Use case:** European teams (GDPR-compliant)
- **Pricing:** €50-100/user/month

**Knowledge Management Tools:**

**1. Notion**
- **Strengths:** Flexible, databases, docs, affordable
- **Use case:** Small teams, tight budgets
- **Pricing:** Free-$15/user/month

**2. Confluence**
- **Strengths:** Enterprise features, integrations
- **Use case:** Large orgs already using Atlassian
- **Pricing:** $5-10/user/month

**3. Airtable**
- **Strengths:** Database + attachments, flexible views
- **Use case:** Structured data, custom workflows
- **Pricing:** Free-$20/user/month

**File Storage:**

**1. Google Drive**
- **Strengths:** Familiar, collaborative, free (with limits)
- **Use case:** Small teams, simple needs

**2. Dropbox**
- **Strengths:** Reliable, large files, integrations
- **Use case:** Video-heavy research

**3. Box**
- **Strengths:** Enterprise security, compliance
- **Use case:** Regulated industries

**Selection Criteria:**
- Team size and budget
- Research volume
- Collaboration needs
- Security and compliance requirements
- Integration with existing tools

### Repository Best Practices

**1. Consistent Naming Conventions**

**Format:** `[Date]-[Product Area]-[Research Type]-[Brief Description]`

**Examples:**
- `2026-03-15-Onboarding-Usability-Test-New-Flow`
- `2026-02-10-Dashboard-Interviews-Power-Users`
- `2026-01-20-Mobile-Survey-Performance-Feedback`

**2. Anonymize Participant Data**

- Use participant IDs (P1, P2, P3) instead of names
- Remove email addresses and phone numbers from shared artifacts
- Redact identifying information from quotes
- Store PII separately with restricted access

**3. Create Study Summaries**

For each study, create a one-page summary:

**Summary Template:**
```
# [Study Name]

**Date:** [Date]
**Researcher:** [Name]
**Product Area:** [Area]
**Method:** [Method]

## Objectives
[What we wanted to learn]

## Participants
[Who we talked to, sample size]

## Key Insights
1. [Insight 1]
2. [Insight 2]
3. [Insight 3]

## Recommendations
1. [Recommendation 1]
2. [Recommendation 2]

## Artifacts
- [Link to full report]
- [Link to presentation]
- [Link to recordings]
```

**4. Regular Maintenance**

- **Quarterly review:** Archive old studies, update tags
- **Annual cleanup:** Delete outdated or irrelevant research
- **Continuous improvement:** Gather feedback on repository usability

**5. Promote Discovery**

- **Onboarding:** Introduce repository to new team members
- **Slack reminders:** "Did you know we have research on [topic]?"
- **Research share-outs:** Highlight repository in presentations
- **Search training:** Teach team how to find insights

---

## Scaling Research

### Templatizing Common Studies

**Benefits:**
- Faster study setup
- Consistent quality
- Easier for non-researchers
- Reusable across teams

**Templates to Create:**

**1. Onboarding Research Template**

**Includes:**
- Research brief template
- Screener (new users, <30 days)
- Discussion guide (onboarding experience)
- Synthesis worksheet
- Report template

**2. Feature Validation Template**

**Includes:**
- Research brief template
- Prototype testing script
- Usability metrics (SUS, task success)
- Synthesis worksheet
- Report template

**3. Competitive Analysis Template**

**Includes:**
- Competitor selection criteria
- Evaluation framework
- Interview guide (users of competitor products)
- Comparison matrix
- Report template

**4. NPS Follow-Up Template**

**Includes:**
- Screener (segment by NPS score)
- Interview guide (why that score?)
- Synthesis worksheet
- Report template

**Template Library:**
Store templates in repository with clear instructions and examples.

### Training Non-Researchers

**Research Enablement Program:**

**Goal:** Empower PMs and designers to conduct lightweight research independently.

**Training Modules:**

**Module 1: Research Fundamentals (2 hours)**
- When to do research vs. when to ask a researcher
- Choosing the right method
- Ethics and consent
- Recruiting participants

**Module 2: Interviewing Skills (2 hours)**
- Writing discussion guides
- Active listening and probing
- Avoiding bias
- Practice interviews (role-play)

**Module 3: Usability Testing (2 hours)**
- Writing test plans and tasks
- Facilitating tests
- Note-taking and observation
- Practice sessions

**Module 4: Synthesis (2 hours)**
- Affinity mapping basics
- Identifying themes
- Developing insights
- Practice synthesis exercise

**Certification:**
- Complete all modules
- Conduct a supervised study
- Pass quality review
- Receive "Research Certified" badge

**Ongoing Support:**
- Office hours (weekly)
- Slack channel for questions
- Peer reviews of research plans
- Quarterly refresher sessions

### Research Review Process

**Quality Gates:**

**Gate 1: Research Plan Review**
- **When:** Before recruitment
- **Reviewer:** Senior researcher
- **Checklist:**
  - [ ] Clear objectives
  - [ ] Appropriate method
  - [ ] Unbiased screener
  - [ ] Sufficient sample size
  - [ ] Realistic timeline

**Gate 2: Discussion Guide Review**
- **When:** Before data collection
- **Reviewer:** Senior researcher or peer
- **Checklist:**
  - [ ] Questions align with objectives
  - [ ] No leading questions
  - [ ] Logical flow
  - [ ] Appropriate depth

**Gate 3: Synthesis Review**
- **When:** After data collection, before sharing
- **Reviewer:** Senior researcher
- **Checklist:**
  - [ ] Rigorous synthesis process
  - [ ] Insights supported by evidence
  - [ ] Recommendations actionable
  - [ ] No overgeneralizations

**Review Turnaround:** 1-2 business days

### Automation Opportunities

**1. Scheduling**
- **Tool:** Calendly, Acuity Scheduling
- **Automation:** Participants self-schedule, automatic reminders

**2. Transcription**
- **Tool:** Otter.ai, Rev, Descript
- **Automation:** Auto-transcribe recordings, sync to repository

**3. Incentive Distribution**
- **Tool:** Tremendous, Rybbon
- **Automation:** Trigger gift card send after session completion

**4. Recruitment**
- **Tool:** User Interviews, Respondent
- **Automation:** Screener distribution, qualification, scheduling

**5. Data Collection**
- **Tool:** Typeform, SurveyMonkey
- **Automation:** Survey distribution, response collection, basic analysis

**6. Repository Updates**
- **Tool:** Zapier, Make (Integromat)
- **Automation:** Auto-create repository entries when study completes

**Example Automation Workflow:**
```
1. Participant completes screener (Typeform)
   ↓
2. Zapier checks if qualified
   ↓
3. If qualified, send Calendly link (email)
   ↓
4. Participant schedules session
   ↓
5. Auto-add to participant database (Airtable)
   ↓
6. Send confirmation email with consent form
   ↓
7. Send reminder 24 hours before (automated)
   ↓
8. After session, trigger incentive send (Tremendous)
   ↓
9. Auto-transcribe recording (Otter.ai)
   ↓
10. Add to research repository (Notion)
```

---

## Research Metrics and KPIs

### Operational Metrics

**1. Research Velocity**
- Studies completed per quarter
- Time from request to insights
- Average study duration

**2. Coverage**
- Product areas researched
- User segments studied
- Research methods used

**3. Efficiency**
- Cost per study
- Cost per participant
- Researcher utilization

**4. Quality**
- Stakeholder satisfaction (survey)
- Study completion rate
- Participant show rate

### Impact Metrics

**1. Decision Influence**
- Decisions informed by research
- Features shipped based on research
- Features killed based on research

**2. Product Outcomes**
- Metrics improved (activation, retention, NPS)
- Support tickets reduced
- Feature adoption increased

**3. Organizational**
- Research requests (demand)
- Research literacy (people trained)
- Repository usage (views, searches)

### Tracking and Reporting

**Research Dashboard:**

Track key metrics in a shared dashboard (Notion, Airtable, Google Sheets).

**Example Dashboard:**

| Metric | Q1 2026 | Q2 2026 | Target |
|--------|---------|---------|--------|
| Studies Completed | 8 | 12 | 10/quarter |
| Avg Time to Insights | 3 weeks | 2.5 weeks | <3 weeks |
| Product Areas Covered | 5 | 7 | All (8) |
| Stakeholder Satisfaction | 4.2/5 | 4.5/5 | >4.0 |
| Decisions Influenced | 15 | 22 | 20/quarter |
| Repository Views | 120 | 180 | 150/quarter |

**Quarterly Review:**
- Review metrics with team
- Identify trends and issues
- Adjust processes and goals
- Celebrate wins

---

## ReOps Checklist

**Participant Management:**
- [ ] Participant database set up
- [ ] Recruitment workflows documented
- [ ] Screener templates created
- [ ] Incentive process established
- [ ] Consent forms and GDPR compliance

**Research Repository:**
- [ ] Repository platform selected
- [ ] Organizational structure defined
- [ ] Tagging system established
- [ ] Naming conventions documented
- [ ] Team trained on repository use

**Scaling Research:**
- [ ] Study templates created
- [ ] Training program developed
- [ ] Review process established
- [ ] Automation implemented

**Metrics and Reporting:**
- [ ] Key metrics defined
- [ ] Dashboard created
- [ ] Quarterly review cadence set
