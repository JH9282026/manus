# Chatbot Types and Best Practices

## Customer Service Bots

Handle inquiries, complaints, and support requests.

### Key Capabilities
- Answer frequently asked questions
- Process simple requests (order status, password reset)
- Collect information for human agents
- Route issues to appropriate departments
- Provide self-service options

### Writing Guidelines
- Lead with empathy for frustrated users
- Acknowledge the issue before solving
- Provide clear, actionable solutions
- Offer escalation readily
- Confirm resolution before closing

### Example Flow
```
User: Where's my order?
Bot: I can help you track your order! Could you share your order number?
User: 12345
Bot: Found it! Order #12345 shipped yesterday and arrives Thursday.
     Track it here: [link]
     Anything else I can help with?
```

---

## Sales and Lead Generation Bots

Qualify leads, provide product information, guide toward purchase.

### Key Capabilities
- Qualify leads through conversation
- Answer product questions
- Recommend based on needs
- Schedule demos or consultations
- Capture contact information
- Hand off warm leads to sales

### Writing Guidelines
- Focus on understanding needs first
- Keep qualification questions conversational
- Highlight value, not features
- Create urgency without pressure
- Make next steps easy

### Example Flow
```
Bot: Looking for a project management tool? I can help find the right fit.
User: Yes, for my team
Bot: Great! How many people on your team?
     [1-10] [11-50] [50+]
User: 11-50
Bot: Mid-sized team—you'll want collaboration features.
     What's your biggest challenge?
     [Tracking deadlines] [Team collaboration] [Resource allocation]
```

---

## FAQ Bots

Deliver information efficiently without complex conversation.

### Key Capabilities
- Surface relevant FAQ articles
- Provide quick answers
- Guide to resources
- Reduce support ticket volume

### Writing Guidelines
- Get to answers quickly
- Structure information clearly
- Link to detailed resources
- Confirm question was answered
- Offer human help for complexity

---

## Hybrid Bots (Bot + Human)

Combine automation with human handoff.

### Handoff Triggers
- Sensitive topics (complaints, billing disputes)
- Multiple fallback responses in a row
- Frustration keywords detected
- High-value customer identified
- User explicitly requests human

### Smooth Handoff Script
```
Bot: I'm connecting you with a team member who can help further.
     One moment while I transfer you...
     [Provides context to agent]
Agent: Hi [Name], this is Sarah. I see you need help with a return.
       How can I assist?
```
