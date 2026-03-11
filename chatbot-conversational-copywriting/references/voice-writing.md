# Voice Assistant Copywriting

Write effective dialogue for voice-based conversational interfaces.

---

## Voice vs. Text Differences

| Aspect | Text Chat | Voice |
|---|---|---|
| Input | Typed, can review before sending | Spoken, real-time, may be imprecise |
| Output | Read at user's pace, scannable | Heard linearly, must be brief |
| Visual aids | Buttons, images, links | None (or minimal screen) |
| Corrections | Easy to retype | Must verbally correct |
| Multi-tasking | Common | Primary use case |
| Privacy | Private by default | May be overheard |

---

## Voice Writing Principles

### Keep It Short

Voice responses should be 15-30 words maximum. Users cannot "re-read" voice output.

**Too long:**
"I found several options for Italian restaurants near you. The highest rated is Bella Roma on Main Street with 4.8 stars, open until 10 PM. Would you like me to tell you about more options or make a reservation?"

**Better:**
"Bella Roma on Main Street is top-rated with 4.8 stars. Want me to book a table?"

### Write for the Ear

- Use short, simple sentences
- Avoid homonyms that could confuse ("there" vs "their")
- Avoid numbers over 4 digits (say "about twelve hundred" not "1,247")
- Use natural speech patterns and contractions

### Confirmation Patterns

Always confirm before executing actions:
```
User: "Order more coffee"
Bot: "Starbucks Medium Roast, $12.99. Should I order it?"
User: "Yes"
Bot: "Done. Arriving Thursday."
```

---

## Voice-Specific Error Handling

### Misrecognition Recovery

```
"Sorry, I didn't catch that. Could you say it again?"
"I heard [interpretation]. Is that right?"
"Just to make sure — did you mean [option A] or [option B]?"
```

### No-Input Timeout

```
[After 5 seconds]: "Are you still there?"
[After 10 seconds]: "I'll be here when you need me. Just say 'hey [name]' to continue."
```

### Disambiguation

```
"I found a few matches. Did you mean:
First, [option A]?
Or second, [option B]?"
```

---

## Platform-Specific Guidelines

### Amazon Alexa
- Responses must complete within 8 seconds
- Reprompt after no input (required by certification)
- Use SSML tags for emphasis, pauses, and pronunciation
- Card content supplements voice response on screen devices

### Google Assistant
- Support both voice and text input
- Leverage rich responses on screen devices
- Follow Google's conversation design guidelines
- Use Dialogflow for intent management

### Apple Siri / Shortcuts
- Keep responses extremely brief
- Support SiriKit intents for deep integration
- Design for quick, transactional interactions
