# Error Handling and Fallbacks

## Error Types

### Intent Not Recognized
Bot doesn't understand what user wants.

```
Level 1: "I didn't quite get that. Could you rephrase?"

Level 2: "Still having trouble. Did you mean:
         [📦 Track order] [🔄 Return item] [👤 Talk to someone]"

Level 3: "I want to make sure you get help. 
         Let me connect you with our team."
```

### Entity Missing
Bot understood intent but lacks required information.

```
"To track your order, I need the order number.
 You can find it in your confirmation email."
```

### API/System Failure
External system didn't respond correctly.

```
"I'm having trouble looking that up right now.
 Can I try again, or would you prefer to speak with someone?
 [Try again] [Connect me]"
```

### Business Logic Error
User request can't be fulfilled.

```
"Unfortunately, that item is final sale and can't be returned.
 I can help you with an exchange or store credit instead.
 What would you prefer?"
```

---

## Writing Error Messages

### Guidelines
- Don't blame the user
- Acknowledge the limitation
- Offer a path forward
- Maintain personality

### Examples

**Poor:**
```
"Error: Invalid input."
"I don't understand. Please try again."
```

**Better:**
```
"Hmm, I couldn't find an order with that number.
 Could you double-check? It's usually 5-6 digits,
 starting with your confirmation email."

"I'm still learning and didn't quite catch that.
 Could you try saying it differently?
 Or I can connect you with someone who can help."
```

---

## Escalation Scripts

### User-Requested Escalation
```
User: "Let me talk to a real person"

Bot: "Absolutely! I'll connect you with our team.
     Before I do, could you briefly describe the issue?
     This helps them help you faster."

[User describes issue]

Bot: "Thanks! Connecting you now. Wait time is about 2 minutes.
     While you wait, you can review your account here: [link]"
```

### Automatic Escalation Triggers
- 3+ fallback responses in a row
- Negative sentiment detected
- High-value customer identified
- Sensitive topic (billing, complaint)
- Keywords: "manager," "angry," "unacceptable"

### Context Handoff
```
Information to pass to agent:
- Customer name and email
- Conversation transcript
- Collected information (order #, issue type)
- Sentiment indicators
- Time spent in conversation
```

---

## Timeout Handling

```
After 5 minutes no response:
"Still there? Let me know if you need anything else."

After 15 minutes:
"Looks like you might be busy. Feel free to come back anytime!"

After 24 hours (for unresolved issues):
"Hi [Name], checking in! Still need help with [topic]?"
```
