---
name: "chatbot-conversational-copywriting"
description: "Write dialogue and conversation flows for chatbots, virtual assistants, and conversational interfaces. Use for: customer service bots, sales chatbots, FAQ bots, voice assistants, conversational UI design, bot personality development, error handling scripts, and multi-turn conversation flows."
---

# Chatbot & Conversational Copywriting

Craft natural, engaging dialogue for chatbots and conversational interfaces.

## Overview

This skill provides frameworks for writing chatbot conversations that feel human, achieve business goals, and handle the complexity of automated dialogue. Create bot personalities, design conversation flows, handle errors gracefully, and optimize for user engagement and conversion.

## Chatbot Type Selection

| Bot Type | Primary Goal | Key Focus | Reference |
|----------|-------------|-----------|----------|
| Customer service | Issue resolution | Empathy, efficiency | `/references/bot-types.md` |
| Sales/lead gen | Qualification, booking | Value, low friction | `/references/bot-types.md` |
| FAQ bot | Information delivery | Clarity, completeness | `/references/bot-types.md` |
| Voice assistant | Task completion | Natural speech, brevity | `/references/voice-writing.md` |

## Core Competencies

### Conversation Design
- Map conversation flows and branching logic
- Design happy paths and edge case handling
- Structure multi-turn conversations
- Create context-aware dialogue sequences

### Bot Personality Development
- Define personality attributes and voice
- Create consistent tone across interactions
- Write persona documentation
- Design branded greeting and closing messages

### User Input Handling
- Anticipate user intent variations
- Write intent recognition training phrases
- Design entity extraction patterns
- Handle ambiguous and unexpected inputs

### Error Recovery
- Create graceful fallback messages
- Design escalation to human agents
- Write clarification requests
- Handle system errors with empathy

## Conversation Structure

### Opening Messages
- Greet and establish bot identity
- Set expectations for capabilities
- Invite user interaction
- Keep concise (under 50 words)

### User Input Collection
- Ask one question at a time
- Provide clear options when appropriate
- Confirm understanding before proceeding
- Validate inputs helpfully

### Response Delivery
- Keep messages short (1-3 sentences)
- Break complex info into multiple messages
- Use formatting for readability
- Always provide next steps

### Conversation Closing
- Confirm resolution or next steps
- Offer additional help
- Thank user appropriately
- Provide satisfaction feedback option

## Quick Reply and Button Guidelines

| Scenario | Use Buttons/Replies | Use Free Text |
|----------|--------------------|--------------|
| Limited valid options | ✓ | |
| Known intent categories | ✓ | |
| Accuracy critical | ✓ | |
| Open-ended questions | | ✓ |
| Specific data entry | | ✓ |
| Natural conversation | | ✓ |

## Key Deliverables

### Strategy Documents
- Bot Persona Document
- Conversation Flow Diagrams
- Voice and Tone Guidelines
- Use Case Prioritization

### Conversation Content
- Opening/Closing Scripts
- Happy Path Dialogues
- Error and Fallback Messages
- Escalation Scripts

### Training Content
- Intent Training Phrases
- Entity Examples
- Synonym Lists
- Validation Messages

## Writing Guidelines

### Language Style
- Use contractions (I'm, you'll, we're)
- Write conversationally, not formally
- Keep sentences under 20 words
- Avoid jargon and corporate speak

### Message Formatting
- Use line breaks for readability
- Limit paragraphs to 2-3 sentences
- Use emojis sparingly and purposefully
- Ensure mobile-friendly length

### Personalization
- Use names when available
- Reference context from earlier in conversation
- Acknowledge returning users
- Adapt tone to user sentiment

## Using the Reference Files

### When to Read Each Reference

**`/references/bot-types.md`** — Read when designing specific bot types (customer service, sales, FAQ) or understanding best practices for each category.

**`/references/conversation-design.md`** — Read when mapping conversation flows, designing branching logic, or planning multi-turn interactions.

**`/references/voice-writing.md`** — Read when writing for voice assistants (Alexa, Google Assistant) or audio-first interfaces.

**`/references/error-handling.md`** — Read when designing fallback behavior, escalation flows, or recovering from conversation failures.

**`/references/templates.md`** — Read when needing ready-to-use conversation templates or script frameworks.
