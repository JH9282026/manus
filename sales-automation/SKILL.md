---
name: "sales-automation"
description: "Automate sales workflows using AI-powered platforms like HubSpot, Salesforce, Outreach, and Apollo. Use for: email sequencing, multi-channel outreach, lead scoring, follow-up automation, CRM integration, deliverability optimization, and scaling outbound sales efficiently."
---

# Sales Automation

Design and implement automated sales workflows that scale outbound outreach, personalize engagement, and accelerate pipeline velocity using modern sales technology.

## Overview

Sales automation in 2026 goes far beyond basic email sequences. AI-powered platforms now handle personalization, optimal send timing, channel selection, and even objection handling. This skill covers platform selection, workflow design, deliverability optimization, and integration patterns to build a high-performing automated sales engine.

## Platform Selection Guide

| Platform | Best For | AI Features | Price Tier | CRM Integration |
|----------|----------|-------------|------------|----------------|
| Outreach | Enterprise outbound, multi-channel | AI-generated emails, sentiment analysis | $$$$ | Salesforce native |
| Apollo.io | Prospecting + sequencing combo | AI writing, intent data, lead scoring | $$ | Salesforce, HubSpot |
| Salesloft | Mid-market, coaching focus | Conversation intelligence, deal scoring | $$$ | Salesforce, HubSpot |
| HubSpot Sequences | Inbound + outbound hybrid | AI content assistant, predictive scoring | $$–$$$ | HubSpot native |
| Instantly.ai | High-volume cold outreach | AI warmup, send optimization | $ | API-based |
| Lemlist | Personalized cold email | AI variables, image personalization | $$ | HubSpot, Pipedrive |
| Smartlead | Agency/multi-client | AI lead categorization, unified inbox | $$ | API-based |

## Multi-Channel Sequence Architecture

### Optimal Sequence Structure

| Day | Channel | Action | Purpose |
|-----|---------|--------|---------|
| 1 | Email | Personalized cold email | Initial contact, value prop |
| 2 | LinkedIn | Profile view + connection request | Social warming |
| 4 | Email | Follow-up with case study | Provide proof |
| 6 | LinkedIn | Personalized message | Channel diversification |
| 8 | Phone | Cold call (if phone available) | Direct engagement |
| 10 | Email | Breakup email with value add | Final attempt + resource share |
| 14 | LinkedIn | Engage with their content | Long-term nurture |

### Channel Performance Benchmarks

| Channel | Avg Response Rate | Best For | Key Metric |
|---------|-------------------|----------|------------|
| Cold email | 3–8% | Scale, initial outreach | Reply rate |
| LinkedIn InMail | 10–25% | Executive targeting | Accept rate |
| Cold calling | 2–5% connect, 10–15% conversation | Urgency, complex deals | Meetings booked |
| Video (Loom/Vidyard) | 15–30% | Differentiation | View-through rate |
| Direct mail | 5–15% | Enterprise ABM | Response rate |

## Lead Scoring Automation

### Scoring Model Architecture

| Signal Category | Signal | Points | Decay |
|----------------|--------|--------|-------|
| **Demographic** | Title matches ICP | +20 | None |
| **Demographic** | Company size in range | +15 | None |
| **Demographic** | Industry match | +10 | None |
| **Behavioral** | Visited pricing page | +25 | 7 days |
| **Behavioral** | Downloaded whitepaper | +15 | 14 days |
| **Behavioral** | Opened 3+ emails | +10 | 7 days |
| **Behavioral** | Replied to outreach | +30 | None |
| **Intent** | Researching competitor | +20 | 14 days |
| **Intent** | Hiring for relevant role | +15 | 30 days |
| **Negative** | Unsubscribed | −50 | None |
| **Negative** | Bounced email | −30 | None |

**Thresholds:** MQL ≥50 points | SQL ≥80 points | Hot Lead ≥100 points

## Email Deliverability Optimization

### Technical Setup Checklist

1. **Domain authentication:** Configure SPF, DKIM, and DMARC for all sending domains
2. **Dedicated sending domain:** Use a subdomain (e.g., `outreach.company.com`) to protect primary domain reputation
3. **Warmup protocol:** Gradually increase volume — start at 20/day, increase by 10–20/day weekly
4. **Inbox rotation:** Distribute sends across multiple mailboxes (max 50 emails/mailbox/day)
5. **List hygiene:** Verify all emails before sequencing (use ZeroBounce, NeverBounce, or MillionVerifier)

### Deliverability Metrics

| Metric | Target | Action if Below |
|--------|--------|----------------|
| Bounce rate | <2% | Clean list, verify emails |
| Spam complaint rate | <0.1% | Improve targeting, add unsubscribe |
| Open rate (cold) | >40% | Fix subject lines, check deliverability |
| Reply rate | >3% | Improve personalization, value prop |
| Unsubscribe rate | <1% | Better targeting, reduce frequency |

## CRM Integration Patterns

| Integration Pattern | Description | When to Use |
|--------------------|-------------|-------------|
| Bi-directional sync | Real-time data flow between automation platform and CRM | Enterprise with complex workflows |
| CRM-first | CRM is source of truth; automation pulls contacts | When CRM data quality is high |
| Automation-first | Automation platform manages sequences; syncs results to CRM | High-volume outbound teams |
| Event-driven | Webhook-based triggers between systems | Custom workflows, multiple tools |

### Essential CRM Fields to Sync
- Sequence status (active, paused, completed, replied)
- Last touch date and channel
- Lead score (real-time)
- Meeting booked (boolean + date)
- Objection reason (if replied negative)

## AI-Powered Personalization

### Personalization Variables

| Variable Type | Example | Impact on Reply Rate |
|--------------|---------|---------------------|
| Company news trigger | "Saw your Series B announcement" | +40–60% |
| Tech stack reference | "Since you use Salesforce..." | +20–30% |
| Mutual connection | "[Name] suggested I reach out" | +50–80% |
| Role-specific pain | "Most VP Sales struggle with..." | +25–35% |
| Industry insight | "In fintech, we're seeing..." | +15–25% |
| Content engagement | "Loved your post about..." | +30–50% |

## Workflow Automation Recipes

1. **Inbound lead response** — Trigger: Form fill → Score lead → Route to SDR (if SQL) or nurture sequence (if MQL) → CRM update
2. **No-show follow-up** — Trigger: Meeting no-show → Wait 1 hour → Send "sorry we missed you" → Offer reschedule link → Alert SDR after 48h
3. **Closed-lost recycling** — Trigger: Deal marked closed-lost → Wait 90 days → Re-engagement sequence → New lead score evaluation
4. **Champion tracking** — Trigger: Contact changes company → Alert AE → Trigger new company research → Start warm outreach

## Best Practices

1. **Personalize at scale, don't spam at scale** — Every automated email should feel hand-written
2. **A/B test everything** — Subject lines, send times, CTAs, sequence length. Minimum 100 sends per variant
3. **Respect the 50/30/20 rule** — 50% personalized emails, 30% semi-personalized, 20% templated
4. **Monitor domain health weekly** — Check Google Postmaster Tools and MXToolbox
5. **Automate the process, not the relationship** — Use automation to free up time for high-value conversations
6. **Set SLAs for speed-to-lead** — Respond to inbound leads within 5 minutes for 8x higher conversion

## Using the Reference Files

### When to Read Each Reference

**`/references/platform-comparison-guide.md`** — Read when evaluating or switching sales automation platforms, comparing features, pricing, and integration capabilities.

**`/references/workflow-automation-templates.md`** — Read when building specific automation workflows, including trigger logic, branching conditions, and CRM sync configurations.

**`/references/ai-personalization-strategies.md`** — Read when implementing AI-driven personalization at scale, training custom models, or configuring AI writing assistants.

**`/references/deliverability-optimization.md`** — Read when troubleshooting deliverability issues, setting up new sending infrastructure, or warming up domains.

**`/references/implementation-playbook.md`** — Read when rolling out a new sales automation stack, migrating between platforms, or training sales teams on automation tools.
