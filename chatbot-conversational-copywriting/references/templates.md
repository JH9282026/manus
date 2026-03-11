# Conversation Templates

## Customer Service Templates

### Order Status Conversation
```
[Opening]
Bot: Hi! Need to check on an order? I can help with that.
     What's your order number?

[Collection]
User: 12345
Bot: Looking up order #12345...

[Delivery]
Bot: Found it! Here's the status:
     📦 Order #12345
     📍 Status: In transit
     📅 Expected: Thursday, Oct 21
     🔗 Track: [link]

[Close]
Bot: Anything else I can help with?
     [🎁 Another order] [🔄 Start return] [✅ All set]
```

### Return Request Conversation
```
[Opening]
Bot: I can help you start a return. What's your order number?

[Collection]
User: 67890
Bot: Order #67890—got it! Which item are you returning?
     [👕 Blue T-Shirt] [👖 Black Jeans] [👟 White Sneakers]

User: [Blue T-Shirt]
Bot: What's the reason for the return?
     [📏 Wrong size] [💥 Damaged] [👎 Didn't like it] [📦 Wrong item]

[Processing]
User: [Wrong size]
Bot: No problem! Here's your return label: [link]
     Drop it at any UPS location within 14 days.
     Refund processes in 3-5 business days.

[Close]
Bot: Return started! Need help with anything else?
```

---

## Lead Generation Templates

### Product Qualification
```
[Opening]
Bot: Hey! 👋 Looking for the right [product] for your team?
     I can help you find the perfect fit.

[Qualification Q1]
Bot: First, how big is your team?
     [1-10] [11-50] [51-200] [200+]

[Qualification Q2]
User: [11-50]
Bot: Mid-sized team! What's your biggest challenge right now?
     [📈 Tracking progress] [💬 Collaboration] [⏰ Time management]

[Recommendation]
User: [Collaboration]
Bot: Collaboration is key for growing teams.
     Our Team Plan includes:
     ✓ Shared workspaces
     ✓ Real-time chat
     ✓ Video calls built in

[CTA]
Bot: Want to see it in action?
     [📅 Schedule demo] [🆓 Start free trial] [ℹ️ More info first]
```

---

## Bot Persona Template

```
BOT PERSONA DEFINITION

Name: [Bot name]
Role: [What does the bot do?]

Personality Traits:
1. [Trait 1—e.g., Helpful]
2. [Trait 2—e.g., Patient]
3. [Trait 3—e.g., Friendly]

Speaking Style:
- Tone: [Professional but warm]
- Formality: [Casual to semi-formal]
- Emoji usage: [Moderate—1-2 per conversation]
- Humor: [Light, appropriate]

Sample Phrases:
- Greeting: "Hi there! How can I help?"
- Clarification: "Let me make sure I understand..."
- Success: "All set! Anything else?"
- Error: "Hmm, that didn't work. Let me try another way."
- Handoff: "I'm connecting you with someone who can help."
- Goodbye: "Thanks for chatting! Have a great day."

Words We Use:
- "Happy to help"
- "Got it!"
- "Let me check on that"

Words We Avoid:
- Corporate jargon
- "Per our policy..."
- "Unfortunately..."
```

---

## Conversation Flow Template

```
[Conversation Name]: [Name]

Trigger: [What initiates this flow?]

1. Opening
   Bot: "[Opening message]"
   Options: [Button 1] [Button 2] [Free text]

2. Intent Recognition
   If [Intent A] → Go to Step 3A
   If [Intent B] → Go to Step 3B
   If Unclear → Go to Fallback

3A. [Intent A Flow]
    Bot: "[Response]"
    Required info: [Entity 1], [Entity 2]
    ...

3B. [Intent B Flow]
    ...

Fallback:
    Bot: "[Clarification message]"
    Options: [Option 1] [Option 2] [Talk to human]

Closing:
    Bot: "[Closing message]"
```
