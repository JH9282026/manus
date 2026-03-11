# Email Deliverability

## Sender Reputation

### Reputation Factors

| Factor | Impact | How to Optimize |
|--------|--------|----------------|
| Bounce rate | High | Verify lists, remove invalids |
| Spam complaints | High | Send relevant content |
| Engagement | Medium | Write compelling emails |
| Send volume | Medium | Consistent patterns |
| Domain age | Low | Use established domains |

---

## Email Authentication

### Required Records

**SPF (Sender Policy Framework)**
- Specifies authorized mail servers
- Add to DNS as TXT record
- Include all sending services

**DKIM (DomainKeys Identified Mail)**
- Adds digital signature
- Verifies email authenticity
- Configure in sending platform

**DMARC (Domain-based Message Authentication)**
- Tells receivers how to handle failures
- Builds on SPF and DKIM
- Start with p=none, progress to p=reject

---

## Domain Warm-Up

### New Domain Schedule

| Week | Daily Volume | Focus |
|------|--------------|-------|
| 1 | 10-20 | High-engagement recipients |
| 2 | 25-50 | Expand gradually |
| 3 | 50-100 | Monitor metrics |
| 4+ | 100+ | Increase to target |

### Warm-Up Best Practices
- Start with engaged recipients
- Send from personal account first
- Generate replies early
- Mix cold and warm emails
- Monitor reputation closely

---

## Spam Trigger Avoidance

### Words to Avoid
- FREE, URGENT, ACT NOW
- Excessive punctuation (!!!)
- ALL CAPS
- "Click here," "Limited time"
- Money symbols ($$$)

### Format Best Practices
- Text-to-link ratio (minimal links)
- No URL shorteners
- No attachments in cold emails
- Include plain text version
- Consistent formatting

---

## List Hygiene

### Verification Process
1. Run through verification service
2. Remove hard bounces
3. Remove role accounts (info@, sales@)
4. Check for spam traps
5. Validate regularly (quarterly)

### Verification Services
- ZeroBounce
- NeverBounce
- Hunter.io
- Clearout

---

## Monitoring Metrics

### Key Indicators

| Metric | Healthy Range | Action if Poor |
|--------|---------------|----------------|
| Open rate | 40-60% | Check subject lines, sender |
| Bounce rate | <2% | Clean list |
| Spam complaint | <0.1% | Review content, targeting |
| Reply rate | 5-15% | Improve copy, personalization |

### Monitoring Tools
- Google Postmaster Tools
- Microsoft SNDS
- MXToolbox
- Mail-tester.com
