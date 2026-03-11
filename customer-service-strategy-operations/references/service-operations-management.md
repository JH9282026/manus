# Service Operations Management

## Contact Center Operations

### Erlang C Staffing Model

The Erlang C formula calculates the probability of a customer waiting in queue, enabling optimal staffing:

**Inputs required**:
- Call volume per interval (typically 30-minute intervals)
- Average handle time (AHT) including after-call work
- Target service level (e.g., 80% answered in 20 seconds)
- Shrinkage factor (breaks, training, meetings — typically 25-35%)

**Process**:
1. Calculate base staff needed: (Calls × AHT) / Interval duration
2. Apply Erlang C formula to find staff for target service level
3. Add shrinkage: Required staff = Erlang staff / (1 - Shrinkage rate)
4. Round up to whole agents

### Scheduling Strategies

| Strategy | Description | Best For |
|----------|-------------|----------|
| Fixed shifts | Set start/end times | Stable, predictable volume |
| Flexible shifts | Variable start times | Volume fluctuation |
| Split shifts | Two shorter shifts in a day | Bimodal volume patterns |
| Staggered shifts | Overlapping start times | Gradual volume changes |
| On-call/overflow | Agents available when needed | Peak handling |

### Real-Time Management

Monitor these metrics in real-time to make intraday adjustments:
- Current wait time and queue depth
- Service level (rolling 30 minutes)
- Agent states (available, on call, after-call work, break)
- Forecasted vs. actual contact volume
- Adherence to schedule

**Intraday Actions**:
- Move breaks/training when volume spikes
- Activate overflow agents
- Open/close channels based on demand
- Extend or reduce shift lengths
- Cross-skill agents to handle different contact types

---

## Escalation Management

### Escalation Triggers

| Trigger Type | Examples | Action |
|-------------|----------|--------|
| Complexity | Beyond Tier 1 knowledge | Route to Tier 2 specialist |
| Emotion | Customer angry or distressed | Transfer to experienced agent |
| Authority | Refund beyond agent limit | Manager approval workflow |
| Time | SLA at risk of breach | Priority queue + notification |
| VIP | High-value customer | Dedicated support path |
| Legal/Compliance | Regulatory mention, threat | Legal team notification |

### Escalation SLAs

| Priority | Response Time | Resolution Time | Communication Frequency |
|----------|--------------|-----------------|------------------------|
| P1 - Critical | 15 minutes | 4 hours | Every 30 minutes |
| P2 - High | 1 hour | 8 hours | Every 2 hours |
| P3 - Medium | 4 hours | 24 hours | Daily |
| P4 - Low | 8 hours | 72 hours | On resolution |

---

## Multi-Channel Integration

### Omnichannel Design Principles

1. **Unified customer profile** — Single view across all channels
2. **Context preservation** — Customer history travels with them
3. **Consistent experience** — Same quality regardless of channel
4. **Intelligent routing** — Direct to right channel/agent based on issue
5. **Seamless transitions** — Move between channels without repetition

### Channel Deflection Strategy

Guide customers to the most efficient channel for their issue:
1. Invest in self-service content (target 60% deflection)
2. Deploy chatbot for common inquiries (target 30% of remaining)
3. Offer live chat before phone (lower cost, higher CSAT)
4. Reserve phone for complex/emotional issues
5. Measure deflection rates and customer satisfaction by channel
