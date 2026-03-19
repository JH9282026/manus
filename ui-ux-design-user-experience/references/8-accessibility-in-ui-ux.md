
### WCAG Guidelines

**Levels:**
- **A**: Minimum accessibility (must have)
- **AA**: Standard compliance (recommended)
- **AAA**: Highest accessibility (ideal)

**POUR Principles:**
1. **Perceivable**: Content must be presentable to all senses
2. **Operable**: Interface must be navigable by all users
3. **Understandable**: Content and operation must be clear
4. **Robust**: Content must work with assistive technologies

### Inclusive Design

**Design for All Users:**
- Visual impairments (blindness, low vision, color blindness)
- Hearing impairments (deafness, hard of hearing)
- Motor impairments (limited mobility, tremors)
- Cognitive impairments (dyslexia, ADHD, memory issues)

**Principles:**
- Provide multiple ways to access content
- Offer customization options
- Design for temporary and situational disabilities
- Test with diverse users

### Assistive Technologies

- **Screen Readers**: JAWS, NVDA, VoiceOver, TalkBack
- **Screen Magnifiers**: ZoomText, Windows Magnifier
- **Voice Control**: Dragon NaturallySpeaking, Voice Control
- **Switch Access**: Single or multiple switch navigation
- **Braille Displays**: Tactile output for blind users

### Keyboard Navigation

**Requirements:**
- All functionality accessible via keyboard
- Visible focus indicators (never `outline: none`)
- Logical tab order following visual layout
- Skip links to bypass repetitive content
- No keyboard traps

**Focus Management:**
- Manage focus on modal open/close
- Return focus to trigger element
- Announce dynamic content changes

### Screen Reader Compatibility

- **Semantic HTML**: Use correct elements (`<nav>`, `<main>`, `<article>`)
- **ARIA Labels**: `aria-label`, `aria-describedby`, `aria-hidden`
- **Alt Text**: Descriptive image alternatives, empty for decorative
- **Heading Structure**: Logical hierarchy (H1 → H2 → H3)
- **Form Labels**: Explicit `<label>` associations with inputs
- **Link Text**: Descriptive links (not "click here")

---
