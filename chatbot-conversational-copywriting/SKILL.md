---
name: "chatbot-conversational-copywriting"
description: "Write dialogue and conversation flows for chatbots, virtual assistants, and conversational interfaces. Use for: customer service bots, sales chatbots, FAQ bots, voice assistants, conversational UI design, bot personality development, error handling scripts, multi-turn conversation flows, NLP training data, and AI-powered chatbot content."
---

# Chatbot & Conversational Copywriting

Write engaging, natural dialogue for chatbots and conversational interfaces that drive user satisfaction and business outcomes.

## Overview

Provide frameworks, templates, and best practices for writing chatbot dialogue across all bot types — customer service, sales, FAQ, voice assistants, and AI-powered conversational agents. Cover conversation design fundamentals, personality development, error handling, escalation flows, and optimization strategies.

## Bot Type Selection Guide

| Bot Type | Primary Goal | Complexity | Reference |
|---|---|---|---|
| Customer service | Resolve inquiries, reduce tickets | Medium-High | `/references/bot-types.md` |
| Sales / lead gen | Qualify leads, drive conversions | Medium | `/references/bot-types.md` |
| FAQ | Answer common questions | Low | `/references/bot-types.md` |
| Voice assistant | Hands-free task completion | High | `/references/voice-writing.md` |
| Hybrid (bot + human) | Triage and escalate | Medium | `/references/error-handling.md` |

## Conversational UI Core Principles

Follow these rules for natural-sounding bot dialogue:

1. **Turn-taking** — Alternate between bot and user; never overwhelm with multiple messages
2. **Relevance** — Respond directly to what the user said; off-topic breaks trust
3. **Clarity** — Use simple, unambiguous language; avoid jargon
4. **Cooperation** — Ask clarifying questions rather than guessing incorrectly
5. **Progressive disclosure** — Reveal information as needed, not all at once
6. **Graceful degradation** — Acknowledge limitations and offer alternatives

## Bot Personality Framework

Define the bot personality along five dimensions:

| Dimension | Casual End | Professional End |
|---|---|---|
| Formality | "Hey! What's up?" | "Hello, how may I assist you?" |
| Humor | Playful, uses emoji | Serious, straightforward |
| Warmth | Friendly, uses names | Polite, maintains distance |
| Directness | Conversational, longer | Concise, to-the-point |
| Confidence | Humble, hedging | Assertive, definitive |

### Persona Template

Define every bot with:
- **Name** — A human-friendly identifier
- **Role** — What the bot does
- **Personality** — 3-4 adjectives
- **Speaking style** — How it communicates
- **Vocabulary** — Words to use and avoid
- **Emoji policy** — Frequency and types

## Conversation Design Essentials

### Flow Structure

Map every conversation path:

```
[Greeting] → [Intent Detection] → [Route]
  ├── Known intent → [Fulfill] → [Confirm] → [Close]
  ├── Unclear intent → [Clarify] → [Route]
  └── Out of scope → [Fallback] → [Escalate or redirect]
```

### Message Components

| Component | Purpose | Example |
|---|---|---|
| Opening | Set expectations | "Hi! I can help with orders, returns, and product questions." |
| Confirmation | Verify understanding | "Got it — you want to track order #12345." |
| Action | Deliver value | "Your order shipped yesterday. Expected delivery: Thursday." |
| Transition | Guide next step | "Is there anything else I can help with?" |
| Closing | End gracefully | "Great, glad I could help! Have a wonderful day." |

## Writing Natural Dialogue

### Key Techniques

- **Use contractions** — "I'm" not "I am", "you'll" not "you will"
- **Use sentence fragments** — "Shipping question? Sure thing!"
- **Vary responses** — Rotate "Got it!", "Okay!", "Perfect, thanks!"
- **Mirror user language** — Match formality level of the user
- **Keep messages short** — 1-3 sentences per message bubble
- **Add natural filler** — "Hmm, let me check..." for processing pauses

### Pacing Rules

- Break long responses into 2-3 separate messages
- Add typing indicators between messages (platform-dependent)
- Front-load the answer, then provide details
- Never exceed 3 messages without user input opportunity

## Error Handling Quick Reference

| Scenario | Response Pattern |
|---|---|
| Didn't understand | "I didn't quite catch that. Could you rephrase?" |
| Out of scope | "That's outside what I can help with. Let me connect you with someone who can." |
| System error | "Something went wrong on my end. Let me try again..." |
| User frustration | "I understand this is frustrating. Let me get you to a person who can help right away." |
| No response (timeout) | "Still there? I'm here if you need anything." |

## Quick Reply & Button Design

- Limit to 3-5 options per prompt
- Use action-oriented labels ("Track Order" not "Order Tracking")
- Always include an escape option ("Something else", "Talk to a person")
- Order options from most to least common
- Keep button text under 25 characters

## Using the Reference Files

**`/references/conversation-design.md`** — Read when designing conversation flows, mapping user journeys, or structuring multi-turn dialogues.

**`/references/bot-types.md`** — Read when building a specific bot type (customer service, sales, FAQ) and need detailed templates and examples.

**`/references/voice-writing.md`** — Read when writing for voice assistants (Alexa, Google Assistant) or speech-based interfaces.

**`/references/error-handling.md`** — Read when designing fallback flows, escalation paths, or handling edge cases.

**`/references/templates.md`** — Read when needing ready-to-use conversation templates, training phrase examples, or persona worksheets.

## Reference Files

This skill includes the following detailed reference materials:

- [Bot Types](./references/bot-types.md)
- [Conversation Design](./references/conversation-design.md)
- [Error Handling](./references/error-handling.md)
- [Templates](./references/templates.md)
- [Voice Writing](./references/voice-writing.md)
