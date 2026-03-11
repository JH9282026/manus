# Email Deliverability

Optimize cold email deliverability to reach the inbox, not the spam folder.

---

## Domain and Infrastructure Setup

### Technical Requirements

| Configuration | Purpose | Priority |
|---|---|---|
| SPF record | Authorize sending servers | Required |
| DKIM signing | Authenticate email integrity | Required |
| DMARC policy | Prevent spoofing, receive reports | Required |
| Custom tracking domain | Branded links, avoid shared domain reputation | Recommended |
| Dedicated IP | Isolated sending reputation | For high volume (1,000+ daily) |
| BIMI | Brand logo in inbox | Optional but beneficial |

### Domain Warming Schedule

New domain or IP must be warmed gradually:

| Week | Daily Volume | Focus |
|---|---|---|
| 1 | 10-20 emails | Send to engaged contacts, personal network |
| 2 | 20-50 emails | Expand to warm contacts, request replies |
| 3 | 50-100 emails | Begin limited cold outreach |
| 4 | 100-200 emails | Scale cautiously, monitor deliverability |
| 5+ | Increase 20-30% weekly | Scale based on engagement metrics |

**Critical:** Never exceed 200 cold emails/day per domain. Use multiple sending domains for higher volume.

---

## Spam Filter Avoidance

### Content Guidelines

**Avoid these spam triggers:**
- ALL CAPS words
- Excessive exclamation marks (!!!)
- Spam phrases: "Act now", "Limited time", "Free", "Click here"
- Image-heavy emails with little text
- Large attachments
- URL shorteners (bit.ly)
- Too many links (keep to 1-2 maximum)

**Best practices:**
- Plain text outperforms HTML for cold email
- Keep emails under 150 words
- Use natural language, not marketing copy
- Include a plain-text signature
- One link maximum in cold emails
- Always include physical address (CAN-SPAM)

---

## Deliverability Metrics

| Metric | Healthy Range | Action if Below |
|---|---|---|
| Delivery rate | >95% | Check bounce reasons, clean list |
| Open rate | >40% (cold) | Improve subject lines, check deliverability |
| Reply rate | >5% (cold) | Improve personalization and offer |
| Bounce rate | <3% | Verify emails before sending |
| Spam complaint rate | <0.1% | Reduce volume, improve targeting |
| Unsubscribe rate | <0.5% | Better targeting, respect opt-outs |

### Monitoring Tools

- Google Postmaster Tools — Monitor Gmail reputation
- Microsoft SNDS — Monitor Outlook reputation
- Mail-tester.com — Check email spam score
- MXToolbox — Verify DNS and blacklist status
- GlockApps — Test inbox placement across providers
