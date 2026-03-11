# Conversation Design Fundamentals

## Flow Architecture

### Happy Path
The ideal flow when everything goes smoothly:
1. Greeting and capability setting
2. Intent identification
3. Information gathering
4. Solution delivery
5. Confirmation and close

### Edge Cases to Plan For
- User says something off-topic
- User provides wrong format
- User asks for unavailable capability
- User expresses frustration
- User asks for human
- User doesn't respond
- System/API failures

---

## Conversation Components

### Opening Message
```
Elements:
1. Greeting
2. Bot identity (optional)
3. Capability overview
4. Invitation to interact

Example:
"Hi! 👋 I help with orders, returns, and product questions.
 What can I help with today?"
```

### User Input Collection
```
Best Practices:
- One question per message
- Explain why you need information
- Provide format guidance
- Confirm before proceeding

Example:
"What's your order number? You can find it in your confirmation email."
[User provides number]
"Got it, order #12345. Let me look that up..."
```

### Response Delivery
```
Structure:
- Acknowledge the request
- Deliver the information
- Provide next steps
- Offer additional help

Example:
"Found your order!
 📦 Status: Shipped
 📅 Arrives: Thursday, Oct 21
 🔗 Track here: [link]
 
 Need anything else?"
```

---

## Multi-Turn Context

### Context to Maintain
- User's name (if provided)
- Current intent and entities
- Information already collected
- Previous conversation topics

### Context Application
```
User: "I want to return order #12345"
[Bot stores: intent=return, order_number=12345]

Bot: "I can help with that return. What's wrong with the item?"

User: "It's damaged"
[Bot updates: reason=damaged]

Bot: "Sorry about the damage. For order #12345, I'll start a damaged 
     item return. Upload a photo of the damage?"
```

---

## Branching Logic

### Decision Tree Structure
```
[Initial Intent]
    ├── Order Status → [Collect order #] → [Deliver status]
    ├── Return → [Collect order #] → [Get reason] → [Process]
    ├── Product Question → [Identify product] → [Answer]
    └── Other → [Clarify] or [Escalate]
```

### Transition Phrases
- "Got it! Now let me..."
- "Perfect. Next, I'll need..."
- "Thanks for that. One more thing..."
- "All set with that. Moving on to..."
