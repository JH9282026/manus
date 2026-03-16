---
name: marketing-automation
description: "Implement marketing automation platforms and workflows to streamline campaigns, nurture leads, and personalize customer experiences at scale. Use for: setting up automation platforms, building email workflows, lead scoring, behavioral triggers, CRM integration, campaign management, multi-channel automation, and measuring automation ROI across email, SMS, social, and web channels."
---

# Marketing Automation

Streamline marketing operations and personalize customer experiences at scale through intelligent automation.

## Overview

This skill provides comprehensive guidance on implementing and optimizing marketing automation platforms, building sophisticated workflows, integrating with CRM systems, and leveraging AI to automate repetitive tasks while delivering personalized experiences across email, SMS, social media, and web channels.

## Platform Selection

### Evaluation Criteria

| Factor | Considerations | Weight |
|--------|---------------|--------|
| **Business Size** | SMB, Mid-Market, Enterprise capabilities | High |
| **Use Cases** | Email, SMS, social, ads, web personalization | High |
| **Integration** | CRM, ecommerce, analytics, ad platforms | Critical |
| **Ease of Use** | Visual builders, learning curve, support | Medium |
| **Scalability** | Contact limits, workflow complexity, performance | High |
| **Pricing** | Contact-based, feature-based, flat-rate | High |
| **AI Capabilities** | Predictive scoring, send-time optimization, content | Medium |

### Platform Comparison

**All-in-One Platforms**:

*HubSpot Marketing Hub*:
- Best for: SMB to mid-market, integrated CRM needs
- Strengths: User-friendly, comprehensive features, free tier
- Pricing: Free to $3,600+/month
- Key features: Email, landing pages, forms, workflows, CRM, reporting

*Marketo Engage (Adobe)*:
- Best for: Enterprise B2B, complex workflows
- Strengths: Advanced automation, scalability, attribution
- Pricing: Custom (typically $1,000+/month)
- Key features: Lead management, account-based marketing, revenue attribution

*Pardot (Salesforce)*:
- Best for: B2B companies using Salesforce
- Strengths: Salesforce integration, B2B focus, lead nurturing
- Pricing: $1,250+/month
- Key features: Lead scoring, email marketing, ROI reporting

**Email-Focused Platforms**:

*ActiveCampaign*:
- Best for: SMB to mid-market, email-first approach
- Strengths: Powerful automation, affordable, CRM included
- Pricing: $29-$149+/month
- Key features: Email, automation, CRM, machine learning

*Klaviyo*:
- Best for: Ecommerce, Shopify stores
- Strengths: Ecommerce integration, segmentation, SMS
- Pricing: Based on contacts (free to $1,700+/month)
- Key features: Email, SMS, flows, predictive analytics

*Brevo (formerly Sendinblue)*:
- Best for: Budget-conscious SMBs
- Strengths: Affordable, multi-channel, CRM included
- Pricing: Free to $65+/month
- Key features: Email, SMS, WhatsApp, chat, CRM

**Enterprise Platforms**:

*Oracle Eloqua*:
- Best for: Large enterprises, complex B2B
- Strengths: Scalability, advanced segmentation, campaign management
- Pricing: Custom (enterprise-level)

*Salesforce Marketing Cloud*:
- Best for: Large enterprises, multi-cloud needs
- Strengths: Comprehensive suite, AI (Einstein), cross-channel
- Pricing: Custom (typically $1,250+/month per module)

## Workflow Automation

### Core Workflow Types

**Welcome Series**:
```
Trigger: New subscriber/customer
Goal: Introduce brand, set expectations, drive engagement

Email 1 (Immediate): Welcome + brand introduction
  \u2193 Wait 2 days
Email 2: Value proposition + key resources
  \u2193 Wait 3 days
Email 3: Social proof + testimonials
  \u2193 Wait 3 days
Email 4: Product/service overview
  \u2193 Wait 4 days
Email 5: Special offer or next step CTA
```

**Lead Nurturing**:
```
Trigger: Lead magnet download, form submission
Goal: Educate, build trust, move to sales-ready

Segment by: Industry, role, company size
  \u2193
Personalized content series (5-7 emails over 2-3 weeks)
  \u2193
Engagement scoring (opens, clicks, downloads)
  \u2193
If score > threshold: Notify sales, move to SQL workflow
If score < threshold: Continue nurturing or re-engagement
```

**Abandoned Cart Recovery**:
```
Trigger: Cart abandonment (no purchase within 1 hour)
Goal: Recover lost revenue

Email 1 (1 hour): Reminder with cart contents
  \u2193 If no purchase, wait 23 hours
Email 2 (24 hours): Add urgency + social proof
  \u2193 If no purchase, wait 2 days
Email 3 (3 days): Discount offer (10-15%)
  \u2193 If no purchase, wait 4 days
Email 4 (7 days): Final reminder + stronger incentive
```

**Re-engagement**:
```
Trigger: No engagement for 60-90 days
Goal: Reactivate dormant subscribers

Email 1: "We miss you" + value reminder
  \u2193 Wait 5 days
Email 2: Special offer or new features
  \u2193 Wait 5 days
Email 3: Preference center or final chance
  \u2193
If engaged: Move back to active segment
If not engaged: Suppress or remove from list
```

**Post-Purchase**:
```
Trigger: Purchase completion
Goal: Onboard, educate, drive repeat purchase

Email 1 (Immediate): Order confirmation
  \u2193
Email 2 (1 day): Shipping notification
  \u2193
Email 3 (Delivery): Delivery confirmation + usage tips
  \u2193 Wait 7 days
Email 4: How-to content + support resources
  \u2193 Wait 14 days
Email 5: Review request
  \u2193 Wait 30 days
Email 6: Cross-sell or replenishment
```

### Workflow Best Practices

**Trigger Design**:
- Use specific, measurable triggers
- Combine multiple conditions (AND/OR logic)
- Set appropriate time delays
- Account for timezone differences
- Test trigger accuracy

**Personalization**:
- Dynamic content blocks
- Conditional logic based on data
- Behavioral personalization
- Predictive content recommendations
- A/B test personalization impact

**Exit Criteria**:
- Define clear exit conditions
- Prevent workflow overlap
- Remove upon goal achievement
- Suppress based on actions
- Set maximum workflow duration

**Testing**:
- Test workflows with sample contacts
- Verify all branches and conditions
- Check timing and delays
- Validate personalization tokens
- Monitor for errors post-launch

## Lead Scoring

### Scoring Model Design

**Demographic Scoring** (Explicit Data):

| Attribute | Score | Rationale |
|-----------|-------|-----------|
| **Job Title** | | |
| C-Level | +20 | Decision maker |
| VP/Director | +15 | Influencer |
| Manager | +10 | User |
| Individual Contributor | +5 | End user |
| **Company Size** | | |
| Enterprise (1000+) | +20 | High value |
| Mid-Market (100-999) | +15 | Good fit |
| SMB (10-99) | +10 | Moderate fit |
| Small (<10) | +5 | Low fit |
| **Industry** | | |
| Target Industry A | +15 | Ideal customer |
| Target Industry B | +10 | Good fit |
| Other | +5 | Possible fit |

**Behavioral Scoring** (Implicit Data):

| Action | Score | Rationale |
|--------|-------|-----------|
| **Email Engagement** | | |
| Email open | +2 | Basic interest |
| Email click | +5 | Active interest |
| Multiple clicks | +10 | High interest |
| **Website Activity** | | |
| Page visit | +1 | Awareness |
| Pricing page visit | +10 | Consideration |
| Demo request | +25 | High intent |
| Case study download | +15 | Evaluation |
| **Content Engagement** | | |
| Blog read | +3 | Learning |
| Whitepaper download | +10 | Research |
| Webinar attendance | +15 | Engaged |
| Video watch (>50%) | +8 | Interested |

**Negative Scoring** (Disqualifiers):

| Attribute/Action | Score | Rationale |
|-----------------|-------|-----------|
| Personal email | -10 | Not business |
| Competitor | -50 | Not prospect |
| Student | -15 | Not buyer |
| Unsubscribe | -50 | Not interested |
| Spam complaint | -100 | Remove |

**Score Thresholds**:
- 0-25: Cold lead (nurture)
- 26-50: Warm lead (continue nurturing)
- 51-75: Hot lead (sales notification)
- 76-100: Very hot lead (immediate sales follow-up)

### Predictive Lead Scoring

Use machine learning to predict conversion likelihood:

**Implementation**:
1. Collect historical lead data (demographics, behavior, outcome)
2. Train ML model on converted vs. non-converted leads
3. Apply model to score new leads (0-100)
4. Continuously retrain with new data
5. Combine with rule-based scoring

**Platforms with Predictive Scoring**:
- HubSpot Predictive Lead Scoring
- Salesforce Einstein Lead Scoring
- Marketo Predictive Content
- 6sense
- Madkudu

## CRM Integration

### Integration Benefits

- Unified customer data
- Automated lead handoff to sales
- Closed-loop reporting (marketing to revenue)
- Sales activity triggers for marketing
- Account-based marketing coordination
- Better attribution and ROI measurement

### Key Integration Points

**Data Sync**:
- Bi-directional contact/lead sync
- Custom field mapping
- Deduplication rules
- Sync frequency (real-time vs. scheduled)
- Conflict resolution

**Lead Lifecycle**:
- Lead creation and assignment
- Lead status updates
- MQL to SQL transition
- Opportunity creation
- Won/lost feedback to marketing

**Activity Tracking**:
- Email opens and clicks
- Website visits
- Content downloads
- Form submissions
- Campaign responses

**Reporting**:
- Campaign influence on opportunities
- Marketing-sourced revenue
- Lead conversion rates
- Sales cycle length
- ROI by campaign/channel

### Common CRM Integrations

**Salesforce**:
- Native integrations: Pardot, Marketing Cloud, HubSpot, Marketo
- Sync: Leads, contacts, accounts, opportunities, campaigns
- Features: Lead assignment, scoring sync, campaign tracking

**HubSpot CRM**:
- Native to HubSpot Marketing Hub
- Sync: Contacts, companies, deals, tickets
- Features: Unified timeline, automated workflows, reporting

**Microsoft Dynamics**:
- Integrations: ClickDimensions, Marketo, HubSpot
- Sync: Leads, contacts, accounts, opportunities
- Features: Marketing lists, campaign tracking, lead scoring

## Multi-Channel Automation

### Email Automation

**Capabilities**:
- Triggered emails based on behavior
- Drip campaigns and nurture sequences
- Dynamic content personalization
- A/B testing automation
- Send-time optimization
- Automated list segmentation

**Best Practices**:
- Segment audiences for relevance
- Personalize beyond first name
- Test subject lines and content
- Optimize for mobile (60%+ opens)
- Monitor deliverability metrics
- Maintain list hygiene

### SMS Automation

**Use Cases**:
- Appointment reminders
- Order status updates
- Flash sales and promotions
- Abandoned cart recovery
- Two-factor authentication
- Customer service notifications

**Best Practices**:
- Obtain explicit consent (TCPA compliance)
- Keep messages concise (<160 characters)
- Include opt-out instructions
- Time messages appropriately
- Personalize when possible
- Track opt-out rates

**Platforms**:
- Klaviyo (ecommerce focus)
- Brevo (multi-channel)
- Twilio (developer-friendly)
- Attentive (SMS marketing)

### Social Media Automation

**Capabilities**:
- Scheduled posting
- Content calendar management
- Social listening and monitoring
- Automated responses
- Lead generation from social
- Social advertising automation

**Platforms**:
- Hootsuite
- Sprout Social
- Buffer
- HubSpot Social Tools

**Caution**:
- Don't over-automate engagement
- Monitor for brand safety
- Respond personally when needed
- Maintain authentic voice

### Web Personalization

**Capabilities**:
- Dynamic content based on visitor data
- Personalized CTAs
- Smart forms (progressive profiling)
- Chatbot automation
- Behavioral popups
- Account-based web experiences

**Implementation**:
- Identify visitor (known vs. anonymous)
- Segment by attributes or behavior
- Serve personalized content
- Track engagement and conversions
- Optimize based on performance

## AI-Powered Automation

### Send-Time Optimization

AI predicts optimal send time for each individual based on historical engagement patterns.

**How It Works**:
1. Analyze past email engagement by time/day
2. Identify patterns for each contact
3. Predict best send time
4. Automatically schedule emails accordingly

**Platforms**:
- Seventh Sense (for HubSpot, Marketo)
- Mailchimp (built-in)
- Klaviyo (built-in)
- ActiveCampaign (built-in)

### Content Recommendations

AI suggests content based on user behavior and preferences.

**Applications**:
- Email content blocks
- Website recommendations
- Product suggestions
- Next-best content

**Platforms**:
- Dynamic Yield
- Optimizely
- Adobe Target
- Marketo Predictive Content

### Automated Segmentation

AI automatically creates and updates segments based on behavior patterns.

**Benefits**:
- Discover hidden segments

## Using the Reference Files

### When to Read Each Reference

**`/references/platform-implementation.md`** — Read when selecting, implementing, or migrating marketing automation platforms, including setup checklists and integration guides.

**`/references/advanced-workflows.md`** — Read when building complex multi-step workflows, conditional logic, or industry-specific automation sequences.

**`/references/integration-guide.md`** — Read when integrating marketing automation with CRM, ecommerce, analytics, or other marketing tools.

**`/references/ai-automation.md`** — Read when implementing AI-powered features like predictive scoring, send-time optimization, or automated content recommendations.
