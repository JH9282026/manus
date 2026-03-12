## Conversational UI and Voice/Tone



### Developing Product Voice

Product voice is the consistent personality expressed through language. It should reflect brand values while remaining appropriate for the product context.

**Voice Development Process:**
1. **Define brand attributes** - What personality traits define your brand?
2. **Create voice principles** - How do those traits translate to language?
3. **Develop guidelines** - What does the voice sound like in practice?
4. **Create examples** - Show voice in different contexts
5. **Train team members** - Ensure everyone can write in voice

**Voice Principle Example:**
| Attribute | We Are | We Are Not |
|-----------|--------|------------|
| Friendly | Warm, approachable, human | Overly casual, unprofessional |
| Clear | Direct, simple, helpful | Patronizing, oversimplified |
| Confident | Assured, trustworthy, expert | Arrogant, dismissive |



### Adapting Tone

While voice remains consistent, tone adapts to context. A successful completion should sound different from an error message.

**Tone Spectrum:**
- **Celebratory** - Accomplishments, milestones
- **Neutral** - Instructions, standard interactions
- **Serious** - Errors, warnings, sensitive topics
- **Empathetic** - Frustrations, problems, support

**Same Voice, Different Tone:**

**Celebratory:**
> "You did it! Your first project is live. Share it with the world!"

**Neutral:**
> "Your project is now published. View it here or continue editing."

**Serious:**
> "We couldn't publish your project. Some required fields are incomplete."



### Types of Errors

**Validation Errors** - Input doesn't meet requirements
> "Password must include at least one number."

**System Errors** - Something failed on the backend
> "Something went wrong. Please try again."

**Permission Errors** - User lacks access
> "You don't have permission to edit this file. Request access from the owner."

**Connectivity Errors** - Network issues
> "Can't connect to the server. Check your internet connection."

**Not Found Errors** - Resource doesn't exist
> "This page doesn't exist. It may have been deleted or moved."



### Error Prevention

The best error messages are the ones users never see. Prevention strategies include:

- Clear labels and instructions
- Real-time validation
- Inline formatting hints
- Confirmation dialogs for destructive actions
- Undo options
- Smart defaults



### Writing Effective Error Messages

**Do:**
- Explain what went wrong in plain language
- Provide specific, actionable guidance
- Use appropriate tone (serious but not scary)
- Position errors near relevant fields
- Offer alternative paths when possible

**Don't:**
- Use technical jargon or error codes alone
- Blame the user
- Leave users without next steps
- Use ALL CAPS or excessive punctuation
- Be vague ("An error occurred")
