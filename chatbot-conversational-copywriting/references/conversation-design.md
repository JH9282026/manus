# Conversation Design

Detailed frameworks for designing effective chatbot conversation flows.

---

## Conversation Flow Architecture

### Intent-Based Design

Structure conversations around user intents — what the user wants to accomplish.

**Intent Design Process:**
1. List all tasks the bot should handle
2. Group related tasks into intent categories
3. Write 15-30 training phrases per intent
4. Map each intent to a fulfillment flow
5. Design fallback for unrecognized intents

### Conversation Tree Mapping

Map every branch point in the conversation:

**Node types:**
- **Decision nodes** — Bot asks a question, user responds
- **Action nodes** — Bot performs an action (API call, database query)
- **Confirmation nodes** — Bot confirms understanding before acting
- **Terminal nodes** — Conversation ends (success, escalation, or dead end)

**Design rules:**
- Maximum 5 turns to resolution for common tasks
- Every branch must have a terminal node
- Include escape hatches at every decision point
- Test all paths, including edge cases

---

## Multi-Turn Conversation Management

### Context Preservation

Maintain conversation context across turns:
- Store user-provided entities (name, order number, preferences)
- Reference previously mentioned items without re-asking
- Track conversation state (what has been discussed, resolved)
- Use context to personalize subsequent interactions

### Slot Filling Patterns

When the bot needs multiple pieces of information:

**Sequential slot filling:**
```
Bot: What size do you need?
User: Medium
Bot: And what color?
User: Blue
Bot: Medium blue t-shirt — got it!
```

**Single-utterance extraction:**
```
User: I need a medium blue t-shirt
Bot: Medium blue t-shirt — got it!
```

Design for both patterns — extract entities from natural language when possible, ask individual questions when needed.

---

## Proactive vs. Reactive Design

### Proactive Triggers

Initiate conversations based on user behavior:
- Cart abandonment (3+ minutes idle on checkout)
- Browsing patterns (viewed same product category 3+ times)
- Error states (failed form submission, 404 page)
- Time-based triggers (returning visitor, post-purchase follow-up)

### Proactive Message Guidelines

- Explain why the bot is reaching out
- Offer clear value, not just interruption
- Provide easy dismissal option
- Limit frequency (max 1 proactive message per session)
- Time appropriately (not immediately on page load)

---

## Conversation Testing Methodology

### Wizard of Oz Testing

Before building, simulate the bot with a human operator:
1. Recruit test users who believe they are talking to a bot
2. Have a human respond following the designed conversation scripts
3. Observe where scripts break down or feel unnatural
4. Identify missing intents, confusing flows, and language issues
5. Revise conversation design based on findings

### Conversation Metrics

| Metric | Definition | Target |
|---|---|---|
| Task completion rate | % of conversations achieving user goal | 80%+ |
| Containment rate | % handled without human escalation | 70%+ |
| Average turns to resolution | Number of back-and-forth exchanges | <5 for common tasks |
| User satisfaction (CSAT) | Post-conversation rating | 4.0+ / 5.0 |
| Fallback rate | % of messages triggering fallback | <15% |
