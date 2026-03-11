# Chatbot Types and Templates

Detailed dialogue templates and examples for each major chatbot category.

---

## Customer Service Bots

### Capabilities
- Answer FAQs, process simple requests (order status, password reset)
- Collect information for human agents
- Route issues to appropriate departments
- Provide self-service options

### Template: Order Tracking

```
Bot: I can help you track your order! Could you share your order number?
     You can find it in your confirmation email.

User: [provides order number]

Bot: Found it! Order #[number] shipped [date] and is expected to arrive
     [delivery date]. Track it here: [link]

     Is there anything else I can help with?
```

### Template: Returns Initiation

```
Bot: I can start a return for you. Could you share:
     1. Your order number
     2. Which item you'd like to return

User: [provides details]

Bot: Got it — [item name] from order #[number].

     What's the reason for the return?
     [Wrong size] [Damaged] [Changed mind] [Other]

User: [selects reason]

Bot: I've created return label RMA-[number]. Here's what to do:
     1. Pack the item in its original packaging
     2. Attach the return label: [link]
     3. Drop it off at any [carrier] location

     Refund will process within 5-7 business days after we receive it.
```

---

## Sales & Lead Generation Bots

### Qualification Flow Template

```
Bot: Hi! 👋 Looking for [product category]? I can help you find the right fit.

User: [interest signal]

Bot: Great! To recommend the best option, I have a few quick questions.

     How many [users/seats/units] do you need?
     [1-10] [11-50] [51-200] [200+]

User: [selects]

Bot: What's your biggest challenge right now?
     [Option A] [Option B] [Option C] [Something else]

User: [selects]

Bot: Based on what you've told me, I'd recommend [Plan/Product].
     It includes [key features relevant to their answers].

     Would you like to:
     [Start free trial] [Book a demo] [See pricing]
```

---

## FAQ Bots

### Design Principles
- Keep answers concise (2-3 sentences max)
- Link to detailed resources for complex topics
- Offer related questions after each answer
- Track unanswered questions to expand knowledge base

### Template Structure

```
Bot: Ask me anything about [topic areas].

User: [question]

Bot: [Concise answer in 1-3 sentences]
     [Link to detailed resource if applicable]

     Was this helpful?
     [Yes, thanks] [No, I need more help]

     Related questions:
     • [Related FAQ 1]
     • [Related FAQ 2]
```
