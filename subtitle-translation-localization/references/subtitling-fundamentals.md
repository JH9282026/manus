# Subtitling Fundamentals

Comprehensive foundation of subtitle creation, timing, and accessibility principles.

---

## What Are Subtitles?

Subtitles are text overlays on video content that display dialogue, narration, and sometimes sound effects. They serve multiple purposes:

**Translation**: Making content accessible to audiences who don't speak the source language

**Accessibility**: Providing access for deaf and hard-of-hearing viewers

**Comprehension**: Helping viewers understand dialogue in noisy environments or with accents

**Language learning**: Supporting learners by showing written form of spoken language

**SEO and discoverability**: Making video content searchable and indexable

## Subtitles vs. Captions vs. SDH

### Standard Subtitles

**Purpose**: Translation for foreign language audiences

**Content**: Dialogue and on-screen text only

**Assumption**: Viewer can hear audio

**Format**: Typically SRT or VTT

**Use cases**: International film distribution, streaming platforms, foreign language content

### Closed Captions (CC)

**Purpose**: Accessibility for deaf and hard-of-hearing viewers

**Content**: Dialogue + sound effects + speaker identification + music cues

**Technical**: Can be turned on/off by viewer

**Format**: SCC (broadcast), CEA-608/708 standard

**Regulatory**: Required by law for broadcast television in many countries (FCC in US, CRTC in Canada)

**Use cases**: Broadcast television, DVD, regulatory compliance

### Subtitles for the Deaf and Hard of Hearing (SDH)

**Purpose**: Accessibility for deaf and hard-of-hearing viewers

**Content**: Same as closed captions (dialogue + sound effects + speaker ID + music)

**Technical**: Uses standard subtitle formats (SRT, VTT, TTML) rather than broadcast caption formats

**Format**: More flexible than CC, supports more characters per line (42 vs. 32)

**Use cases**: Streaming platforms (Netflix, Amazon Prime), online video, modern accessibility

**Key difference from CC**: SDH uses subtitle technology and formats, while CC uses broadcast captioning technology. Functionally similar for end users.

### Forced Narratives (FN)

**Purpose**: Translate foreign language dialogue within otherwise same-language content

**Content**: Only dialogue in a different language than the main content

**Example**: English film with a scene in French—forced narrative translates only the French dialogue

**Technical**: Cannot be turned off ("forced" to display)

**Use cases**: Multilingual films, TV shows with foreign language segments

## The Subtitling Process

### 1. Transcription

Creating a written record of all spoken dialogue:

**Verbatim transcription**:
- Capture every word spoken
- Include filler words (um, uh, you know)
- Note false starts and corrections
- Mark unclear or inaudible sections

**Clean transcription**:
- Remove filler words and false starts
- Correct grammatical errors in speech
- Maintain meaning while improving readability
- More common for subtitling than verbatim

**Speaker identification**:
- Label each speaker (by name or description)
- Note when speakers change
- Indicate overlapping dialogue

**Timestamps**:
- Mark approximate times for dialogue
- Note significant sound effects or music
- Identify scene changes

**Tools**:
- Manual transcription: Time-consuming but accurate
- AI transcription (Whisper, Sonix, Rev): Fast but requires review
- Hybrid approach: AI first draft, human refinement

### 2. Spotting (Time-Coding)

Assigning precise in and out times to each subtitle:

**Frame-accurate timing**:
- In time: Exact frame when subtitle should appear
- Out time: Exact frame when subtitle should disappear
- Typically measured in HH:MM:SS:FF (hours:minutes:seconds:frames) or HH:MM:SS.mmm (milliseconds)

**Synchronization principles**:
- Subtitle appears when dialogue begins (or slightly before for anticipation)
- Subtitle disappears when dialogue ends (or shortly after)
- Align with visual cuts when possible
- Respect shot boundaries (don't carry over unless necessary)

**Reading speed calculation**:
- Count characters in subtitle (including spaces)
- Calculate duration in seconds
- CPS = characters / duration
- Adjust timing or text to meet CPS standards (15-20 CPS)

**Line breaks**:
- Break at natural linguistic boundaries (punctuation, phrase boundaries)
- Avoid breaking between article and noun ("the / house" is bad)
- Avoid breaking between adjective and noun ("red / car" is bad)
- Prefer breaking at conjunctions, prepositions, or punctuation
- Top line should be shorter or equal to bottom line (pyramid structure)

**Shot change respect**:
- Ideally, subtitles don't span shot changes
- If dialogue continues across cut, consider splitting subtitle
- If split is awkward, allow subtitle to carry over but minimize duration
- Some platforms (Netflix) have specific rules about shot change tolerance

### 3. Segmentation

Dividing dialogue into readable subtitle units:

**Principles**:
- Each subtitle should be a complete thought or phrase
- Maximum two lines per subtitle
- Maximum 42-47 characters per line
- Minimum 1 second, maximum 7 seconds duration

**Segmentation strategies**:
- Break at sentence boundaries when possible
- Break at clause boundaries for long sentences
- Keep subject and verb together
- Keep verb and object together
- Avoid orphaned words (single word on second line)

**Condensation**:
- Remove redundancy and filler
- Simplify complex structures
- Prioritize key information
- Maintain meaning and tone

### 4. Formatting

Applying visual styling to subtitles:

**Italics**:
- Off-screen dialogue or voice-over
- Narration
- Song lyrics
- Emphasis (sparingly)
- Thoughts or internal monologue
- Foreign language within same-language content (sometimes)

**Bold**:
- Rarely used in professional subtitling
- May be used for emphasis in some contexts
- Not supported by all formats

**Capitalization**:
- Standard sentence case for dialogue
- ALL CAPS for shouting or emphasis (use sparingly)
- Title case for proper nouns

**Punctuation**:
- Standard punctuation rules apply
- Ellipsis (...) for trailing off or interruption
- Dash (—) for interruption or abrupt change
- Question marks and exclamation points as appropriate

**Speaker identification (SDH)**:
- Format: `SPEAKER: Dialogue` or `[Speaker] Dialogue`
- Use when speaker is off-screen or ambiguous
- Use character names or descriptions (MAN, WOMAN, DOCTOR, etc.)
- Be consistent throughout

**Sound effects (SDH)**:
- Format: `[description]` or `(description)`
- Lowercase for descriptions
- Concise and relevant
- Examples: `[door slams]`, `[phone ringing]`, `[ominous music]`

## Reading Speed and Timing

### Characters Per Second (CPS)

The primary metric for subtitle reading speed:

**Calculation**: Total characters (including spaces) divided by duration in seconds

**Standards**:
- **Comfortable reading**: 12-15 CPS
- **Professional maximum**: 17-20 CPS
- **Netflix adult content**: 17 CPS maximum
- **Netflix children's content**: 13 CPS maximum
- **BBC**: 15-17 CPS
- **Accessible subtitles**: 12-15 CPS recommended

**Factors affecting reading speed**:
- **Audience**: Children and non-native speakers need slower speeds
- **Content complexity**: Technical or dense content needs more time
- **Visual complexity**: Busy visuals require more cognitive load, slower reading
- **Language**: Some languages require more characters to express same meaning

**Adjusting for CPS**:
- If CPS is too high: Condense text or extend duration
- If duration can't be extended: Prioritize key information, omit less essential details
- If text can't be condensed: Split into multiple subtitles

### Characters Per Line (CPL)

**Standards**:
- **Standard subtitles**: 42-47 characters per line maximum
- **SDH**: 42 characters per line
- **Closed captions (broadcast)**: 32 characters per line
- **Two lines maximum** per subtitle event

**Line balancing**:
- Top line should be shorter or equal to bottom line (pyramid structure)
- Avoid single-word lines when possible
- Break at natural linguistic boundaries

### Duration Standards

**Minimum duration**: 1 second (0.8 seconds for very short interjections like "Oh!" or "No!")
- Shorter than 1 second is difficult to read
- Viewer's eye needs time to locate and process subtitle

**Maximum duration**: 7 seconds (6 seconds preferred)
- Longer than 7 seconds feels static
- Viewer may re-read, causing distraction
- Exception: Slow-paced dialogue or narration may extend slightly

**Ideal duration**: 2-5 seconds
- Comfortable reading without rushing
- Allows viewer to glance at visuals
- Maintains engagement

### Gaps Between Subtitles

**Minimum gap**: 2 frames (approximately 0.08 seconds at 24fps)
- Allows viewer's eye to register that subtitle has changed
- Prevents "flashing" effect
- Some platforms require longer gaps (4-6 frames)

**When to use longer gaps**:
- Between sentences or thoughts
- At scene changes
- When speaker changes
- To give viewer a visual break

**When to minimize gaps**:
- Continuous rapid dialogue
- Maintaining flow of conversation
- When reading speed is already challenging

## Accessibility Principles

### Legal Requirements

**United States**:
- **Americans with Disabilities Act (ADA)**: Requires captions for public-facing video content
- **21st Century Communications and Video Accessibility Act (CVAA)**: Governs closed captions for broadcast and online video
- **Section 508 of Rehabilitation Act**: Requires captions for federal government electronic media

**European Union**:
- **European Accessibility Act**: Requires accessibility features including subtitles for audiovisual media services
- **Audiovisual Media Services Directive**: Mandates accessibility for public broadcasters

**Canada**:
- **CRTC regulations**: Require closed captioning for broadcast television

**United Kingdom**:
- **Equality Act 2010**: Requires reasonable adjustments including subtitles for accessibility

### SDH Best Practices

**Sound effect descriptions**:
- Include sounds that affect comprehension or atmosphere
- Don't describe every sound (avoid clutter)
- Be concise and specific
- Use present tense: `[door slams]` not `[door slammed]`
- Describe tone when relevant: `[ominous music]`, `[cheerful whistling]`

**Speaker identification**:
- Identify speaker when off-screen or ambiguous
- Use character names when known
- Use descriptions when names unknown: `MAN:`, `WOMAN:`, `DOCTOR:`
- Be consistent throughout
- Not needed when speaker is obvious from visuals

**Music and lyrics**:
- Indicate when music is playing: `[music playing]`
- Include song title and artist if relevant: `["Bohemian Rhapsody" by Queen playing]`
- Transcribe lyrics if they're important to plot or atmosphere
- Use musical note symbols for lyrics: `♪ We are the champions ♪`
- Indicate genre or mood if lyrics aren't transcribed: `[upbeat jazz music]`

**Tone and manner of speaking**:
- Indicate when tone affects meaning: `[sarcastic]`, `[whispering]`, `[shouting]`
- Don't over-describe (avoid `[speaking normally]`)
- Use when tone isn't obvious from context or visuals

**Language identification**:
- Indicate when characters speak a foreign language: `[speaking in French]`
- If foreign dialogue is translated in forced narratives, don't duplicate in SDH
- Indicate if language is important to plot

### Inclusive Design

**Readability**:
- Use clear, legible fonts (sans-serif)
- Ensure sufficient contrast (white text with black outline)
- Avoid placing subtitles over busy backgrounds
- Use semi-transparent background box if needed

**Positioning**:
- Default to bottom center
- Move to top if bottom obscures important visuals
- Avoid covering faces or on-screen text
- Be consistent in positioning throughout

**Cognitive accessibility**:
- Use simple, clear language
- Avoid jargon unless necessary
- Break complex information into smaller chunks
- Maintain consistent formatting

---

## Summary

Subtitling is a specialized skill that combines linguistic expertise with technical precision. Understanding the fundamentals—types of subtitles, timing principles, reading speed standards, and accessibility requirements—is essential for creating professional, effective subtitles. Whether translating for international audiences or providing accessibility for deaf and hard-of-hearing viewers, subtitlers must balance accuracy, readability, and synchronization to deliver a seamless viewing experience.
