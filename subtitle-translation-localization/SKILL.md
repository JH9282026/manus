---
name: subtitle-translation-localization
description: "Create professional subtitles and captions for video content with accurate translation, timing, and localization. Use for: translating subtitles for films and TV shows, creating SDH (Subtitles for Deaf and Hard of Hearing), spotting and time-coding dialogue, localizing cultural references and idioms, formatting subtitles in SRT/VTT/TTML formats, ensuring reading speed compliance (CPS/CPL standards), synchronizing text with audio and visual cues, adapting content for streaming platforms (Netflix, YouTube), and implementing accessibility standards."
---

# Subtitle Translation and Localization

Create accurate, synchronized, and culturally adapted subtitles for video content across languages and platforms.

## Overview

Subtitle translation and localization combines linguistic expertise with technical precision to make video content accessible to global audiences. This skill covers the complete subtitling workflow from transcription and translation through timing, spotting, quality assurance, and delivery in various formats for different platforms.

## Subtitle Types and Selection

| Type | Purpose | Content | Use Cases |
|------|---------|---------|------------|
| Standard subtitles | Translation for foreign language audiences | Dialogue only | Films, TV shows, international distribution |
| SDH (Subtitles for Deaf and Hard of Hearing) | Accessibility for deaf/HOH audiences | Dialogue + sound effects + speaker ID | Streaming platforms, broadcast, legal compliance |
| Closed captions (CC) | Accessibility for broadcast | Dialogue + sound effects + music cues | TV broadcast, DVD, regulatory compliance |
| Forced narratives (FN) | Translate foreign language within content | Only foreign dialogue in otherwise same-language content | Films with multilingual dialogue |
| Burned-in subtitles | Permanent subtitles | Any content | Social media, promotional videos, no player support |

## Technical Standards and Specifications

### Reading Speed Standards

**Characters Per Second (CPS)**:
- **Professional standard**: 15-20 CPS maximum
- **Netflix standard**: 17 CPS maximum (adult content), 13 CPS (children's content)
- **BBC standard**: 15-17 CPS
- **Comfortable reading**: 12-15 CPS

**Characters Per Line (CPL)**:
- **Standard**: 42-47 characters per line maximum
- **Two lines maximum** per subtitle event
- **SDH**: Up to 42 characters per line
- **Closed captions**: 32 characters per line (broadcast limitation)

### Timing Standards

**Duration**:
- **Minimum**: 1 second (0.8 seconds for very short interjections)
- **Maximum**: 7 seconds (6 seconds preferred)
- **Ideal**: 2-5 seconds for comfortable reading

**Synchronization**:
- Subtitles appear when dialogue begins
- Disappear promptly after dialogue ends
- Align with visual cuts when possible
- Respect shot changes (don't carry over unless necessary)

**Gaps**:
- **Minimum gap between subtitles**: 2 frames (0.08 seconds at 24fps)
- Allows viewer's eye to register change
- Prevents subtitle "flashing"

### Positioning and Formatting

**Placement**:
- **Default**: Bottom center of screen
- **Alternative**: Top center (to avoid obscuring on-screen text or important visuals)
- **Speaker identification**: Left or right alignment for multiple speakers
- **Avoid**: Covering faces, on-screen text, or critical visual elements

**Formatting**:
- **Font**: Sans-serif (Arial, Helvetica) for legibility
- **Size**: Proportional to screen resolution
- **Color**: White text with black outline or semi-transparent background
- **Line breaks**: At natural linguistic boundaries (not mid-phrase)
- **Italics**: For off-screen dialogue, voice-over, song lyrics, emphasis

## Subtitling Workflow

### 1. Transcription and Spotting

**Transcription**:
- Create verbatim transcript of all dialogue
- Include speaker identification
- Note sound effects and music for SDH
- Mark timestamps for key events

**Spotting (Time-coding)**:
- Assign precise in and out times to each subtitle
- Align with dialogue onset and offset
- Respect shot changes and visual cuts
- Ensure reading speed compliance
- Place line breaks at natural pauses

**AI-assisted spotting**:
- Use tools like Matesub, Subtitle Edit with Whisper, or Sonix
- AI generates initial time-coded captions
- Human review required for accuracy and refinement
- Particularly useful for long-form content

### 2. Translation and Localization

**Translation principles**:
- **Accuracy**: Convey the meaning faithfully
- **Conciseness**: Condense for reading speed without losing meaning
- **Naturalness**: Use idiomatic target language
- **Synchrony**: Match subtitle length to available screen time

**Condensation techniques**:
- Remove redundancy and filler words
- Simplify complex sentence structures
- Omit non-essential information
- Prioritize key message over verbatim translation

**Cultural adaptation**:
- Localize idioms and cultural references
- Adapt humor for target audience
- Explain culturally specific concepts when necessary
- Consider regional variations (US vs. UK English, European vs. Latin American Spanish)

**Challenges**:
- **Wordplay and puns**: Often require creative adaptation
- **Cultural references**: May need explanation or substitution
- **Dialects and accents**: Indicate through word choice or notes
- **Profanity**: Adapt to target culture norms and platform guidelines
- **Songs and poetry**: Balance meaning, rhythm, and synchronization

### 3. SDH-Specific Elements

**Sound effect descriptions**:
- **Format**: [description in brackets] or (description in parentheses)
- **Placement**: Separate line or integrated with dialogue
- **Content**: Meaningful sounds that affect comprehension or atmosphere

**Examples**:
- `[door slams]`
- `[ominous music swells]`
- `[footsteps approaching]`
- `[phone vibrating]`
- `[speaking in French]`
- `[sarcastic tone]`

**Speaker identification**:
- Use character names or descriptions
- Format: `JOHN: Dialogue` or `[John] Dialogue`
- Essential when speaker is off-screen or ambiguous
- Use consistently throughout

**Music cues**:
- Indicate when music starts, changes, or is significant
- Include song title and artist if relevant
- Use musical notes symbol: `♪ song lyrics ♪`
- Example: `♪ "Bohemian Rhapsody" by Queen playing ♪`

### 4. Quality Assurance

**Linguistic QA**:
- Proofread for grammar, spelling, punctuation
- Verify translation accuracy against source
- Check terminology consistency
- Ensure natural, idiomatic language
- Validate cultural appropriateness

**Technical QA**:
- Verify reading speed (CPS/CPL compliance)
- Check timing synchronization with audio
- Validate subtitle duration (min/max)
- Ensure proper line breaks
- Verify formatting (italics, speaker IDs, sound effects)
- Check for gaps between subtitles
- Validate file format and encoding (UTF-8)

**Visual QA**:
- Review subtitles in context with video
- Check positioning (not obscuring important visuals)
- Verify readability (contrast, font size)
- Ensure alignment with shot changes
- Validate subtitle appearance and disappearance timing

**Automated QA tools**:
- Subtitle Edit: Built-in QA checks for timing, length, formatting
- EZTitles: Comprehensive QA suite
- CAT tools with subtitle support: Trados, MemoQ
- Platform-specific validators: Netflix Timed Text Style Guide validator

## File Formats

### SRT (SubRip Text)

**Structure**:
```
1
00:00:10,500 --> 00:00:13,000
First subtitle line
Second subtitle line

2
00:00:15,000 --> 00:00:18,000
Next subtitle
```

**Characteristics**:
- Plain text format, easy to edit
- Widely supported by players and platforms
- Timecode format: HH:MM:SS,mmm
- Unofficial support for basic formatting (bold, italic, underline)
- No official styling or positioning standard

**Use cases**: YouTube, Facebook, general web video, most media players

### WebVTT (Web Video Text Tracks)

**Structure**:
```
WEBVTT

00:00:10.500 --> 00:00:13.000
First subtitle line
Second subtitle line

00:00:15.000 --> 00:00:18.000 align:start position:10%
Next subtitle with positioning
```

**Characteristics**:
- W3C standard for HTML5 video
- UTF-8 encoding required
- Supports styling and positioning
- Timecode format: HH:MM:SS.mmm
- Cue settings for alignment and position

**Use cases**: Web streaming, HTML5 video, Vimeo, modern web platforms

### TTML/DFXP (Timed Text Markup Language)

**Structure**: XML-based format with comprehensive styling

**Characteristics**:
- W3C standard
- Extensive styling capabilities (color, font, position)
- Supports multiple languages in single file
- Complex structure, not easily hand-edited
- Timecode format: HH:MM:SS.mmm or HH:MM:SS:FF (frames)

**Use cases**: Netflix, professional broadcast, streaming platforms requiring advanced styling

### SCC (Scenarist Closed Captions)

**Characteristics**:
- Based on CEA-608 broadcast standard
- Hexadecimal encoding
- Limited character set (Latin alphabet only)
- Frame rate: 29.97 fps only
- Line length: 37 characters maximum
- Supports text styling and positioning

**Use cases**: Broadcast television, DVD, Adobe Premiere, Final Cut Pro

### EBU-STL (European Broadcasting Union Subtitle)

**Characteristics**:
- Binary format (not human-readable)
- Broadcast industry standard in Europe
- Includes metadata (program title, copyright)
- Supports 25 and 30 fps only
- Limited color support

**Use cases**: European broadcast, professional linear television

### ASS/SSA (Advanced SubStation Alpha)

**Characteristics**:
- Text-based format with extensive styling
- Supports animations and special effects
- Highly customizable (fonts, colors, positioning, effects)
- Complex syntax
- Popular in anime fansubbing community

**Use cases**: Anime, fansubbing, projects requiring visual customization

### Format Selection Guide

| Platform | Recommended Format | Alternative |
|----------|-------------------|-------------|
| YouTube | SRT, VTT | TTML |
| Netflix | TTML (DFXP) | - |
| Vimeo | VTT | SRT |
| Facebook | SRT | VTT |
| Broadcast TV (US) | SCC | - |
| Broadcast TV (EU) | EBU-STL | - |
| Web streaming | VTT | SRT |
| DVD/Blu-ray | SCC, EBU-STL | - |
| Anime/Fansubbing | ASS | SRT |

## Platform-Specific Requirements

### Netflix

**Technical requirements**:
- Format: TTML (DFXP) with specific Netflix profile
- Reading speed: 17 CPS maximum (adult), 13 CPS (children)
- Duration: 1-7 seconds per subtitle
- Line length: 42 characters maximum
- Positioning: Bottom center, can be moved to avoid on-screen text

**Content requirements**:
- Translate all dialogue and on-screen text
- Include SDH for accessibility
- Localize cultural references appropriately
- Follow Netflix Timed Text Style Guide (language-specific)
- Use approved terminology and character names

**Delivery**:
- Use Netflix Partner Hub for submission
- Pass automated QC checks
- Include metadata (language, type, frame rate)

### YouTube

**Technical requirements**:
- Format: SRT, VTT, or TTML
- Encoding: UTF-8
- Automatic captioning available (requires review)
- Supports multiple language tracks

**Best practices**:
- Keep reading speed comfortable (15 CPS or less)
- Use clear, concise language
- Include sound effects for accessibility
- Proofread auto-generated captions carefully

**Delivery**:
- Upload via YouTube Studio
- Can edit captions directly in interface
- Supports community contributions (if enabled)

### Broadcast Television

**US (FCC regulations)**:
- Format: SCC (CEA-608) or newer standards
- Accuracy: Must match spoken dialogue
- Completeness: All programming must be captioned
- Synchronization: Captions must align with audio

**EU (accessibility directives)**:
- Format: EBU-STL or platform-specific
- Accessibility: Subtitles required for public broadcasters
- Quality: Must meet national standards

## Tools and Software

### Professional Subtitling Software

**Subtitle Edit** (Free, open-source):
- Supports 200+ subtitle formats
- Audio waveform visualization
- Integrated Whisper AI for auto-transcription
- Comprehensive QA checks
- Batch processing
- Best for: General subtitling, format conversion, QA

**Aegisub** (Free, open-source):
- Advanced styling (ASS/SSA format)
- Audio spectrum analyzer for precise timing
- Visual typesetting
- Lua scripting for automation
- Best for: Anime, fansubbing, complex visual effects

**EZTitles** (Commercial):
- Professional broadcast-quality subtitling
- Advanced spotting and timing tools
- Comprehensive QA suite
- Support for all major formats
- Best for: Professional subtitling, broadcast, high-volume production

**Subtitle Workshop** (Free):
- User-friendly interface
- Real-time preview
- Multiple format support
- Timing and synchronization tools
- Best for: Beginners, simple projects

### Online Subtitling Platforms

**Amara** (Web-based):
- Collaborative subtitling
- Crowdsourced translation
- Integration with YouTube and Vimeo
- Accessibility focus
- Best for: Community projects, non-profit, education

**Kapwing** (Web-based):
- Auto-captioning with AI
- Styling templates for social media
- Video editing integration
- Best for: Social media content, marketing videos

**Typito** (Web-based):
- Branded "burnt-in" subtitles
- Styling and animation
- Video editing features
- Best for: Marketing, promotional videos, social media

### AI-Powered Transcription

**Whisper (OpenAI)**:
- State-of-the-art speech recognition
- Multilingual support
- Free and open-source
- Integrates with Subtitle Edit
- Requires technical setup

**Sonix**:
- Automated transcription and subtitling
- SDH generation (with human review)
- Multi-language support
- Cloud-based
- Commercial service

**Rev.com**:
- Human transcription and captioning services
- High accuracy
- Fast turnaround
- SDH and closed captioning
- Commercial service

## Best Practices

### Translation Best Practices

1. **Prioritize meaning over verbatim translation**: Convey the message, not word-for-word
2. **Respect reading speed limits**: Condense without losing essential information
3. **Maintain character voice**: Preserve personality, tone, and speaking style
4. **Localize culturally**: Adapt references, humor, and idioms for target audience
5. **Use consistent terminology**: Maintain character names, place names, and key terms
6. **Consider context**: Review surrounding dialogue for coherence

### Timing Best Practices

1. **Align with speech**: Subtitles appear when dialogue starts, disappear when it ends
2. **Respect shot changes**: Don't carry subtitles across cuts unless necessary
3. **Use natural line breaks**: Break at punctuation or natural pauses, not mid-phrase
4. **Maintain minimum duration**: At least 1 second for readability
5. **Avoid subtitle flashing**: Minimum 2-frame gap between subtitles
6. **Balance reading speed**: Aim for 12-15 CPS for comfortable reading

### SDH Best Practices

1. **Include meaningful sounds**: Not every sound, but those affecting comprehension or atmosphere
2. **Identify speakers**: When off-screen or ambiguous
3. **Describe tone when relevant**: [sarcastic], [whispering], [shouting]
4. **Indicate language**: [speaking in French] when not translated
5. **Format consistently**: Use same style for sound effects throughout
6. **Don't over-describe**: Keep descriptions concise and relevant

### Quality Assurance Best Practices

1. **Review in context**: Always watch subtitles with video
2. **Check reading speed**: Use automated tools to verify CPS/CPL
3. **Proofread carefully**: Grammar, spelling, punctuation errors are highly visible
4. **Verify synchronization**: Subtitles must align with audio precisely
5. **Test on target platform**: Ensure formatting and positioning work correctly
6. **Get feedback**: Have another person review for clarity and accuracy

## Using the Reference Files

### When to Read Each Reference

**`/references/subtitling-fundamentals.md`** — Read when you need comprehensive understanding of subtitling principles, the difference between subtitles and captions, accessibility requirements, or detailed explanations of timing and spotting techniques.

**`/references/translation-localization.md`** — Read when translating subtitles for foreign audiences, adapting cultural references, handling idiomatic expressions, condensing dialogue for reading speed, or maintaining character voice across languages.

**`/references/technical-workflow.md`** — Read when setting up subtitling projects, configuring software tools, implementing automated workflows, integrating AI transcription, or troubleshooting technical issues with formats and encoding.

**`/references/quality-standards.md`** — Read when implementing QA processes, understanding platform-specific requirements (Netflix, YouTube, broadcast), ensuring accessibility compliance, or establishing quality benchmarks for subtitling teams.

## References

- [Quality Standards](references/quality-standards.md)
- [Subtitling Fundamentals](references/subtitling-fundamentals.md)
- [Technical Workflow](references/technical-workflow.md)
- [Translation Localization](references/translation-localization.md)
