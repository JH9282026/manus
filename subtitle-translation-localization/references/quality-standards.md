# Quality Standards and Platform Requirements

Comprehensive guide to subtitle quality standards, platform-specific requirements, and compliance guidelines.

---

## Universal Quality Standards

### Accuracy

**Definition**: Subtitles must faithfully convey the meaning of the source dialogue and audio.

**Requirements**:
- All dialogue translated or transcribed accurately
- No omissions of plot-relevant information
- No additions or embellishments
- Numbers, names, and facts verified
- Technical terminology correct

**Acceptable adaptations**:
- Condensation for reading speed (while preserving meaning)
- Cultural localization of idioms and references
- Simplification of complex structures for clarity

**Unacceptable errors**:
- Mistranslations that change meaning
- Omission of important dialogue
- Factual errors (wrong numbers, names, dates)
- Misidentification of speakers

### Synchronicity

**Definition**: Subtitles must appear and disappear in sync with audio and visual elements.

**Requirements**:
- Subtitle appears when dialogue begins (or slightly before for anticipation)
- Subtitle disappears when dialogue ends (or shortly after)
- Alignment with shot changes when possible
- Respect for visual cuts (don't carry over unless necessary)

**Tolerance**:
- ±2 frames for in/out times (acceptable variance)
- Longer variance acceptable for fast-paced dialogue
- Shot change respect: Ideally no carryover, but acceptable if split is awkward

**Unacceptable errors**:
- Subtitles appearing before dialogue starts (>0.5 seconds early)
- Subtitles remaining after dialogue ends (>1 second late)
- Subtitles for wrong speaker or scene
- Chronologically out-of-order subtitles

### Readability

**Definition**: Subtitles must be easy to read and comprehend.

**Requirements**:
- Reading speed: 12-20 CPS (depending on audience and platform)
- Line length: 42-47 characters per line maximum
- Maximum two lines per subtitle
- Minimum duration: 1 second
- Maximum duration: 7 seconds
- Proper line breaks at natural linguistic boundaries

**Formatting**:
- Clear, legible font (sans-serif)
- Sufficient contrast (white text with black outline)
- Proper positioning (not obscuring important visuals)
- Consistent formatting throughout

**Unacceptable errors**:
- Excessive reading speed (>20 CPS)
- Lines longer than 47 characters
- More than two lines per subtitle
- Subtitles shorter than 1 second (except brief interjections)
- Line breaks mid-phrase or mid-word

### Completeness

**Definition**: All relevant audio content must be subtitled.

**Requirements**:
- All dialogue subtitled
- All on-screen text translated (if relevant)
- Sound effects included (for SDH)
- Music cues included (for SDH)
- Speaker identification (for SDH when needed)

**Acceptable omissions**:
- Background conversation not relevant to plot
- Repetitive or redundant dialogue (when condensing for reading speed)
- Lyrics of background music (unless plot-relevant)

**Unacceptable omissions**:
- Plot-relevant dialogue
- Important sound effects (for SDH)
- On-screen text necessary for comprehension
- Speaker identification when ambiguous (for SDH)

### Consistency

**Definition**: Subtitles must maintain consistent style, terminology, and formatting.

**Requirements**:
- Character names spelled consistently
- Terminology used consistently
- Formatting applied consistently (italics, speaker IDs, sound effects)
- Style and tone consistent with content
- Punctuation and capitalization consistent

**Unacceptable errors**:
- Character name variations ("John" vs. "Jon")
- Inconsistent terminology ("car" vs. "automobile" for same object)
- Inconsistent formatting (sometimes italics for off-screen, sometimes not)
- Inconsistent punctuation style

## Platform-Specific Requirements

### Netflix

**Technical specifications**:
- **Format**: TTML (DFXP) with Netflix-specific profile
- **Encoding**: UTF-8
- **Frame rate**: Match source video (23.976, 24, 25, 29.97, 30, 50, 59.94, 60 fps)

**Reading speed**:
- **Adult content**: 17 CPS maximum
- **Children's content**: 13 CPS maximum
- **Recommended**: 12-15 CPS for comfortable reading

**Duration**:
- **Minimum**: 5/6 second (20 frames at 24fps)
- **Maximum**: 7 seconds
- **Ideal**: 2-5 seconds

**Line length**:
- **Maximum**: 42 characters per line
- **Maximum lines**: 2

**Positioning**:
- **Default**: Bottom center
- **Alternative**: Top center (to avoid on-screen text or important visuals)
- **Avoid**: Covering faces or critical visual elements

**Shot changes**:
- Subtitles should not cross shot changes unless:
  - Dialogue continues across cut
  - Splitting would create awkward reading
- Maximum 2 frames carryover across shot change

**Content requirements**:
- Translate all dialogue
- Translate all on-screen text (signs, labels, text messages, etc.)
- Include forced narratives for foreign language dialogue
- Provide SDH for accessibility

**Style guidelines** (language-specific):
- Follow Netflix Timed Text Style Guide for each language
- Use approved character names and terminology
- Localize cultural references appropriately
- Maintain consistent tone and register

**Quality control**:
- Pass Netflix automated QC checks
- No errors in metadata (language code, frame rate, etc.)
- Proper TTML structure and syntax
- Compliance with all technical and content requirements

**Delivery**:
- Submit via Netflix Partner Hub
- Include all required metadata
- Provide separate files for each language and subtitle type (standard, SDH, forced)

### YouTube

**Technical specifications**:
- **Format**: SRT, VTT, or TTML
- **Encoding**: UTF-8 required
- **Frame rate**: Any (YouTube handles conversion)

**Reading speed**:
- No strict limit, but 15 CPS recommended for accessibility
- Slower for children's content (12-13 CPS)

**Duration**:
- **Minimum**: 1 second
- **Maximum**: No strict limit, but 7 seconds recommended

**Line length**:
- No strict limit, but 42-47 characters recommended
- YouTube player adjusts display based on screen size

**Content requirements**:
- Translate all dialogue
- Include sound effects for accessibility (optional but recommended)
- Provide multiple language tracks for international audiences

**Auto-captioning**:
- YouTube provides automatic captions (AI-generated)
- Accuracy varies (70-90% depending on audio quality and accent)
- **Must be reviewed and corrected** for professional content
- Not suitable for accessibility compliance without human review

**Quality control**:
- YouTube validates format on upload
- Flags formatting errors
- No automated quality checks for content accuracy

**Delivery**:
- Upload via YouTube Studio
- Can edit captions directly in browser interface
- Supports community contributions (if enabled by creator)

### Broadcast Television (US)

**Regulatory framework**:
- **FCC regulations**: All programming must be captioned
- **21st Century CVAA**: Governs closed caption quality
- **ADA compliance**: Captions required for public-facing content

**Technical specifications**:
- **Format**: SCC (CEA-608) or newer standards (CEA-708)
- **Frame rate**: 29.97 fps (NTSC standard)
- **Encoding**: Limited character set (Latin alphabet)

**Reading speed**:
- **Recommended**: 15-17 CPS
- **Maximum**: 20 CPS (for fast-paced content)

**Duration**:
- **Minimum**: 1 second
- **Maximum**: 7 seconds

**Line length**:
- **Maximum**: 32 characters per line (CEA-608 limitation)
- **Maximum lines**: 4 (but 2-3 recommended for readability)

**Content requirements**:
- **Accuracy**: Must match spoken dialogue
- **Completeness**: All programming must be captioned (no gaps)
- **Synchronization**: Captions must align with audio
- **Sound effects**: Include all meaningful sounds
- **Speaker identification**: Identify speakers when off-screen or ambiguous
- **Music cues**: Indicate music and lyrics when relevant

**Quality standards** (FCC requirements):
- Accurate: Error rate <5%
- Synchronous: Align with audio within 3 seconds
- Complete: No gaps in captioning
- Properly placed: Don't obscure important visuals

**Penalties**: FCC can fine broadcasters for non-compliance

### Broadcast Television (EU)

**Regulatory framework**:
- **European Accessibility Act**: Requires accessibility features including subtitles
- **AVMSD (Audiovisual Media Services Directive)**: Mandates accessibility for public broadcasters
- **National regulations**: Vary by country

**Technical specifications**:
- **Format**: EBU-STL (European standard) or platform-specific
- **Frame rate**: 25 fps (PAL standard) or 50 fps
- **Encoding**: Supports multiple character sets and languages

**Reading speed**:
- **Recommended**: 15-17 CPS
- **Maximum**: 20 CPS

**Duration**:
- **Minimum**: 1 second
- **Maximum**: 7 seconds

**Content requirements**:
- Similar to US broadcast standards
- Language-specific style guides (BBC, ARD, etc.)
- Accessibility focus for public broadcasters

**Quality standards**:
- Vary by country and broadcaster
- Generally align with EBU recommendations
- Emphasis on accuracy, synchronization, and completeness

### Streaming Platforms (General)

**Amazon Prime Video**:
- Similar to Netflix requirements
- TTML or DFXP format
- 17 CPS maximum for adult content
- Comprehensive style guides by language

**Disney+**:
- TTML format
- Strict quality standards
- Platform-specific style guides
- Emphasis on family-friendly content

**Hulu**:
- SRT or TTML format
- 17 CPS maximum
- Standard accessibility requirements

**Apple TV+**:
- TTML or iTT (iTunes Timed Text) format
- High quality standards
- Emphasis on visual presentation

## Accessibility Compliance

### Legal Requirements

**United States**:
- **ADA (Americans with Disabilities Act)**: Requires captions for public-facing video
- **Section 508 (Rehabilitation Act)**: Requires captions for federal government media
- **CVAA (21st Century Communications and Video Accessibility Act)**: Governs broadcast and online video captions

**European Union**:
- **European Accessibility Act**: Requires accessibility features for audiovisual media
- **Web Accessibility Directive**: Requires accessibility for public sector websites and apps

**Canada**:
- **CRTC regulations**: Require closed captioning for broadcast television
- **Accessible Canada Act**: Mandates accessibility in federally regulated sectors

**United Kingdom**:
- **Equality Act 2010**: Requires reasonable adjustments including subtitles
- **Ofcom regulations**: Require subtitles for broadcast content

### WCAG (Web Content Accessibility Guidelines)

**Relevant criteria**:

**1.2.2 Captions (Prerecorded)** (Level A):
- Captions provided for all prerecorded audio content in synchronized media

**1.2.4 Captions (Live)** (Level AA):
- Captions provided for all live audio content in synchronized media

**1.2.5 Audio Description (Prerecorded)** (Level AA):
- Audio description provided for all prerecorded video content

**1.2.6 Sign Language (Prerecorded)** (Level AAA):
- Sign language interpretation provided for all prerecorded audio content

**Compliance levels**:
- **Level A**: Minimum accessibility (captions for prerecorded content)
- **Level AA**: Enhanced accessibility (captions for live content)
- **Level AAA**: Highest accessibility (sign language interpretation)

### SDH Quality Standards

**Content requirements**:
- All dialogue transcribed accurately
- Sound effects described when meaningful
- Music cues included when relevant
- Speaker identification when needed
- Tone and manner indicated when affecting meaning

**Sound effect guidelines**:
- Format: `[description]` or `(description)`
- Concise and specific: `[door slams]` not `[a door slams loudly]`
- Present tense: `[phone ringing]` not `[phone rang]`
- Relevant to plot or atmosphere: Don't describe every sound

**Speaker identification guidelines**:
- Use when speaker is off-screen or ambiguous
- Format: `SPEAKER: Dialogue` or `[Speaker] Dialogue`
- Use character names when known
- Use descriptions when names unknown: `MAN:`, `WOMAN:`, `DOCTOR:`
- Be consistent throughout

**Music and lyrics**:
- Indicate music: `[music playing]`, `[upbeat jazz music]`
- Include song title/artist if relevant: `["Bohemian Rhapsody" by Queen playing]`
- Transcribe lyrics if plot-relevant or significant
- Use musical notes for lyrics: `♪ Lyrics here ♪`

## Quality Assurance Process

### Three-Stage QA

**Stage 1: Linguistic QA**
- Proofread for grammar, spelling, punctuation
- Verify translation accuracy
- Check terminology consistency
- Ensure natural, idiomatic language
- Validate cultural appropriateness

**Stage 2: Technical QA**
- Verify reading speed (CPS compliance)
- Check timing synchronization
- Validate duration (min/max)
- Ensure proper line breaks
- Verify formatting (italics, speaker IDs, sound effects)
- Check gaps between subtitles
- Validate file format and encoding

**Stage 3: Visual QA**
- Review subtitles in context with video
- Check positioning (not obscuring visuals)
- Verify readability (contrast, font size)
- Ensure alignment with shot changes
- Validate subtitle appearance/disappearance timing
- Check for visual errors (flashing, overlapping)

### Error Classification

**Critical errors** (must be fixed):
- Mistranslations that change meaning
- Omission of plot-relevant dialogue
- Factual errors (wrong numbers, names, dates)
- Severe synchronization issues (>2 seconds off)
- Excessive reading speed (>25 CPS)
- File format errors preventing playback

**Major errors** (should be fixed):
- Minor mistranslations
- Awkward or unnatural phrasing
- Inconsistent terminology
- Synchronization issues (0.5-2 seconds off)
- Reading speed violations (20-25 CPS)
- Improper line breaks
- Missing sound effects (SDH)

**Minor errors** (fix if time allows):
- Spelling or punctuation errors
- Inconsistent formatting
- Slight timing imperfections (<0.5 seconds)
- Preferential style choices
- Minor readability issues

### Quality Metrics

**Error rate**: Number of errors per 1000 words or per 100 subtitles
- **Excellent**: <1 error per 1000 words
- **Good**: 1-3 errors per 1000 words
- **Acceptable**: 3-5 errors per 1000 words
- **Unacceptable**: >5 errors per 1000 words

**Accuracy score**: Percentage of subtitles without errors
- **Excellent**: >99%
- **Good**: 97-99%
- **Acceptable**: 95-97%
- **Unacceptable**: <95%

**Client satisfaction**: Feedback and revision requests
- Track revision rate
- Monitor client feedback
- Identify recurring issues
- Implement corrective actions

---

## Summary

Subtitle quality standards ensure accuracy, synchronicity, readability, completeness, and consistency across all content. Platform-specific requirements vary in technical specifications and content guidelines, but all prioritize viewer comprehension and accessibility. Understanding and adhering to these standards—whether for Netflix, YouTube, broadcast television, or accessibility compliance—is essential for professional subtitling. Implementing rigorous quality assurance processes with clear error classification and metrics ensures that subtitles meet professional standards and client expectations.
