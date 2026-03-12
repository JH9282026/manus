# Video Sound Design Audio Post - Detailed Reference

## EQ (Equalization) for Video

EQ shapes the frequency content of audio, making elements clearer, warmer, brighter, or helping them fit together in the mix.

### EQ Fundamentals

**Frequency Ranges:**
- **Sub-bass (20-60Hz)**: Rumble, weight, can be problematic
- **Bass (60-250Hz)**: Warmth, fullness, body, can cause muddiness
- **Low-mids (250-500Hz)**: Body, boxy/muddy frequencies
- **Mids (500Hz-2kHz)**: Presence, honk, nasal qualities
- **High-mids (2-4kHz)**: Clarity, harshness, intelligibility
- **Highs (4-8kHz)**: Sibilance, brightness, detail
- **Air (8-20kHz)**: Sparkle, air, can add hiss

### EQ for Dialogue

**General Dialogue EQ:**
- High-pass filter: 80-120Hz to remove rumble
- Cut 200-400Hz if boxy or muddy
- Boost 2-4kHz for clarity and presence
- Cut 4-6kHz if harsh or aggressive
- High-shelf boost around 8kHz for air (subtle)

**Male Voice (typical fundamentals 85-180Hz):**
- Fundamental and warmth in 100-250Hz range
- Presence in 2-4kHz range
- Watch for proximity effect boom

**Female Voice (typical fundamentals 165-255Hz):**
- Fundamental and warmth in 200-400Hz range
- Presence in 3-5kHz range
- May need more sibilance control

### EQ for Music

**General Considerations:**
- Music should support, not compete with dialogue
- Cut frequencies where dialogue lives (2-4kHz)
- Maintain low end and high end for fullness
- Consider ducking (dynamic EQ) during dialogue

**Specific Adjustments:**
- High-pass to remove sub-bass if not needed
- Cut midrange to create space for vocals/dialogue
- Boost highs for brightness and energy
- Adjust based on genre and context

### EQ for Sound Effects

**Matching Reality:**
- EQ effects to match environment
- Distant sounds: Roll off highs, reduce bass
- Close sounds: Full frequency range
- Muffled sounds: Aggressive high cut

**Creating Impact:**
- Boost low frequencies for power
- Enhance high frequencies for detail
- Cut midrange for clarity in mix
- Layer multiple elements for complexity

### EQ Types

**Parametric EQ:**
- Adjustable frequency, gain, and bandwidth (Q)
- Most flexible and precise
- Essential for corrective and creative work

**Graphic EQ:**
- Fixed frequency bands
- Visual representation of curve
- Less precise, good for quick adjustments

**Shelving EQ:**
- Affects all frequencies above (high shelf) or below (low shelf) a point
- Good for broad tonal adjustments
- Natural-sounding results

**High-Pass/Low-Pass Filters:**
- Remove frequencies above or below cutoff
- Essential for cleanup
- Various slopes (6dB/12dB/18dB/24dB per octave)

---

## Compression and Dynamics

Dynamics processing controls the range between quiet and loud sounds, essential for consistent, professional audio.

### Understanding Dynamics

**Dynamic Range:**
- The difference between quietest and loudest parts
- Wide dynamic range: High variation (classical music, film)
- Narrow dynamic range: Consistent level (broadcast, web)

**Why Compression Matters:**
- Ensures dialogue audibility
- Controls peaks to prevent distortion
- Creates consistent listening experience
- Adds punch and presence to elements

### Compression Parameters

**Threshold:**
- Level at which compression begins
- Lower threshold = more compression
- Set based on average levels of material

**Ratio:**
- How much gain reduction is applied above threshold
- 2:1 (subtle) to ∞:1 (limiting)
- Higher ratios for more aggressive control

**Attack:**
- How quickly compression engages
- Fast attack: Controls transients, can reduce punch
- Slow attack: Allows transients through, preserves punch

**Release:**
- How quickly compression disengages
- Fast release: Responsive, can cause pumping
- Slow release: Smooth, may reduce dynamics too much

**Knee:**
- How gradually compression engages
- Soft knee: Gentle transition, transparent
- Hard knee: Abrupt transition, more obvious effect

**Make-up Gain:**
- Restores level lost through compression
- Matches output to input level or desired level

### Compression for Dialogue

**Settings Starting Points:**
- Threshold: -15 to -20dB
- Ratio: 2:1 to 4:1
- Attack: 10-30ms (preserve consonants)
- Release: 100-300ms (smooth, natural)
- Gain reduction: 3-6dB on peaks

**Techniques:**
- Use multiple stages of light compression
- De-esser for sibilance control
- Limiter as safety net for peaks
- Parallel compression for body without squashing

### Compression for Music

**Full Mix:**
- Light compression for cohesion (2:1, 3-6dB reduction)
- Attack: Medium-slow to preserve transients
- Release: Matched to tempo or auto-release

**Sidechain Compression:**
- Duck music when dialogue plays
- Keyed from dialogue track
- Smooth attack and release for transparency
- Typically 3-6dB of ducking

### Limiting

**What is Limiting:**
- Extreme compression (∞:1 ratio or higher)
- Prevents signal from exceeding threshold
- Used for peak control and loudness

**Applications:**
- Master limiter for output protection
- Brick-wall limiting for broadcast compliance
- Loudness maximization (use sparingly)

---

## Audio Mixing Fundamentals

Mixing combines all audio elements into a cohesive whole where each element is audible and balanced.

### The Mix Hierarchy

**Priority Order (typical):**
1. Dialogue (most important)
2. Key sound effects (sync to picture)
3. Music
4. Ambient sound
5. Background effects

### Level Setting

**Reference Levels:**
- Dialogue: -12 to -6 dBFS average
- Music: -18 to -12 dBFS (under dialogue)
- Effects: Variable based on importance
- Ambient: -30 to -20 dBFS (subtle presence)

**Mixing Approach:**
1. Start with dialogue at reference level
2. Add music below dialogue
3. Bring in effects at appropriate levels
4. Add ambient for atmosphere
5. Fine-tune relationships

### Panning

**Dialogue:**
- Typically center (mono) for clarity
- Match screen position for multi-character scenes
- Avoid extreme panning for key dialogue

**Music:**
- Usually stereo spread
- May pan to leave room for centered dialogue
- Consider left-right balance

**Effects:**
- Pan to match screen position
- Create spatial awareness
- Movement can follow action

**Ambient:**
- Often stereo for envelopment
- Can establish spatial environment
- Should not distract from foreground

### Reverb and Space

**Creating Acoustic Space:**
- Match reverb to visual environment
- Large spaces: More reverb, longer decay
- Small spaces: Shorter, tighter reverb
- Outdoor: Less reverb, more natural ambience

**Reverb Settings:**
- Room size: Match visual space
- Decay time: 0.5-2s for most scenes
- Pre-delay: Separates source from reverb
- Mix: Wet/dry balance (often subtle in film)

**Practical Applications:**
- Add room verb to ADR to match production
- Create off-screen space with reverb
- Use reverb to soften harsh sounds

### Automation

**What is Automation:**
- Recording parameter changes over time
- Essential for dynamic mixing
- Controls level, panning, effects, and more

**Automation Uses:**
- Ride dialogue levels for consistency
- Duck music under dialogue
- Create effects movements
- Control dynamics throughout

**Automation Modes:**
- Read: Plays back automation
- Touch: Records when touching control
- Latch: Records until stopped
- Write: Overwrites all automation

---

## Sound Effects and Foley

Sound effects and Foley bring the visual world to life, creating believable sonic environments and physical reality.

### Types of Sound Effects

**Hard Effects:**
- Sync to specific picture events
- Door slams, gunshots, explosions
- Must match timing precisely

**Background/Ambience:**
- Environmental sounds
- Room tone, traffic, nature
- Create sense of place

**Production Effects:**
- Captured during filming
- May be supplemented or replaced
- Include practical sounds from set

**Designed Effects:**
- Created for fantasy/sci-fi elements
- Layered and processed
- No real-world reference

### Foley

**What is Foley:**
- Sound effects performed and recorded in sync to picture
- Named after Jack Foley, a pioneer of the technique
- Covers footsteps, cloth movement, handling props

**Common Foley Elements:**
- Footsteps (various surfaces and footwear)
- Cloth and movement sounds
- Hand props (glasses, keys, paper)
- Body falls and impacts

**Foley Recording:**
- Watch picture and perform sounds in sync
- Multiple passes for different elements
- Use appropriate props and surfaces
- Record in quiet, controlled environment

### Sound Effect Libraries

**Commercial Libraries:**
- Pro Sound Effects: Comprehensive professional library
- Boom Library: High-quality designed sounds
- Sound Ideas: Industry standard collections
- Sonniss: Annual free packs (GDC)

**Building Personal Library:**
- Record unique sounds regularly
- Properly metadata and organize
- Create versions (short, long, varied intensity)
- Document usage rights

### Sound Design Techniques

**Layering:**
- Combine multiple sounds for complexity
- Low layer for weight/impact
- Mid layer for body
- High layer for detail/transients

**Processing:**
- Pitch shifting for size/character
- Time stretching for duration
- EQ for tonal shaping
- Reverb for space/environment

**Creative Sound Design:**
- Combine unexpected elements
- Process beyond recognition
- Layer organic with synthetic
- Consider psychological impact

---

## Music Selection and Licensing

Music significantly impacts emotional response and overall production value.

### Types of Music for Video

**Original Score:**
- Composed specifically for project
- Maximum customization
- Higher cost and timeline
- Full rights ownership (work for hire)

**Licensed Music:**
- Pre-existing recordings
- Varies widely in cost
- Requires proper licensing
- May have restrictions on usage

**Production/Library Music:**
- Created for licensing in productions
- Searchable by mood, genre, tempo
- Typically affordable
- Clear licensing terms

**Royalty-Free Music:**
- One-time purchase for unlimited use
- Quality varies widely
- Check specific license terms
- May not actually be "free"

### Music Licensing Basics

**Types of Licenses:**
- **Sync License**: Right to synchronize music with visual media
- **Master License**: Right to use specific recording
- **Performance License**: For public performance (handled by PROs)

**Licensing Considerations:**
- Territory (worldwide vs. regional)
- Media (all vs. specific platforms)
- Duration (perpetual vs. limited term)
- Exclusivity (exclusive vs. non-exclusive)

**Where to License Music:**

**Production Music Libraries:**
- Epidemic Sound: Subscription model, broad catalog
- Artlist: Subscription, unlimited downloads
- Musicbed: Higher-end curation
- Premiumbeat: Individual track licensing

**Direct Licensing:**
- Contact artists/labels directly
- Often for specific songs
- Higher cost, more negotiation
- Clear rights for well-known music

### Music Selection Criteria

**Mood Matching:**
- Energy level appropriate to scene
- Emotional tone supports narrative
- Genre fits project style
- Instrumentation complements visuals

**Technical Considerations:**
- Clean recording quality
- Appropriate length or edit points
- No distracting elements
- Stems available (if needed)

**Rights Clarity:**
- Clear licensing terms
- Appropriate for all platforms
- No unexpected restrictions
- Proper documentation

---

## Voiceover Recording and Editing

### Recording Environment

**Room Treatment:**
- Absorptive treatment to reduce reflections
- Isolation from external noise
- No parallel walls (prevent flutter echo)
- Consistent, quiet HVAC

**Equipment:**
- Large-diaphragm condenser for studio VO
- Dynamic microphone for less controlled environments
- Pop filter to prevent plosives
- Shock mount to reduce vibration
- Quality preamp with phantom power

**Recording Settings:**
- Sample rate: 48kHz (video standard)
- Bit depth: 24-bit
- Headroom: Peak at -12 to -6dBFS
- Record in mono

### Recording Techniques

**Microphone Placement:**
- 6-12 inches from mouth
- Slightly off-axis to reduce plosives
- Consistent distance throughout session
- Pop filter 2-4 inches from microphone

**Performance Direction:**
- Provide clear context and direction
- Allow warm-up takes
- Record multiple takes
- Note preferred takes during session
- Get wild lines and variations

### Editing Voiceover

**Cleanup:**
- Remove mouth clicks and pops
- Reduce or remove breaths (vary by style)
- Cut hesitations and mistakes
- Smooth transitions between takes

**Timing:**
- Match to picture if needed
- Adjust pacing for clarity
- Remove unnecessary pauses
- Maintain natural rhythm

**Processing:**
- EQ for clarity and presence
- Compression for consistency
- De-ess if needed
- Light limiting for peaks

---

## Audio Levels and Loudness Standards (LUFS)

### Understanding Loudness

**Peak vs. Loudness:**
- Peak: Maximum instantaneous level
- Loudness: Perceived overall volume
- Two sources with same peak can have very different loudness
- Loudness measurement accounts for human hearing

**LUFS (Loudness Units Full Scale):**
- Standard measurement for perceived loudness
- Based on human hearing characteristics
- Used for broadcast and streaming standards
- Negative values (closer to 0 = louder)

### Platform Standards

**Broadcast:**
- US (ATSC A/85): -24 LUFS ± 2 LU
- Europe (EBU R128): -23 LUFS ± 1 LU
- True Peak limit: -2 dBTP (typically)

**Streaming:**
- YouTube: -14 LUFS (normalizes to this)
- Spotify: -14 LUFS
- Apple Music: -16 LUFS
- Netflix: -27 LUFS dialog, -24 LUFS overall
- Amazon: -24 LUFS

**Social Media:**
- Instagram: -14 LUFS
- Facebook: -16 LUFS
- TikTok: -14 LUFS (approximately)
- Twitter: -14 LUFS

### Measuring Loudness

**Loudness Meters:**
- Integrated: Overall loudness (entire program)
- Short-term: 3-second rolling average
- Momentary: 400ms rolling average
- True Peak: Maximum peak level

**Loudness Range (LRA):**
- Difference between quiet and loud
- Higher LRA = more dynamic
- Lower LRA = more compressed
- Target varies by content type

### Setting Correct Levels

**Process:**
1. Mix to sound good (don't chase numbers)
2. Measure integrated loudness
3. Adjust master level to hit target
4. Check true peak compliance
5. Verify with multiple measurement tools

**Tips:**
- Different platforms normalize differently
- Master slightly above target (platforms turn down, not up)
- Don't sacrifice dynamics for loudness
- Consider multiple deliverables for different platforms

---

## Stereo vs. Surround Sound

### Stereo (2.0)

**Applications:**
- Most web content
- Social media
- Small-scale productions
- Personal viewing

**Mixing for Stereo:**
- Dialogue centered
- Music spread across stereo field
- Effects positioned left/center/right
- Limited spatial positioning

### Surround Sound Formats

**5.1 Surround:**
- Left, Center, Right (front)
- Left Surround, Right Surround (rear)
- LFE (Low Frequency Effects/subwoofer)
- Standard for DVD, Blu-ray, streaming

**7.1 Surround:**
- Adds side surround channels
- More immersive experience
- Blu-ray, streaming, cinema

**Dolby Atmos:**
- Object-based audio
- Height channels
- Scalable to any speaker configuration
- Premium streaming, cinema

### Surround Mixing Considerations

**Channel Assignments:**
- **Center**: Dialogue, key sync effects
- **Left/Right Front**: Music, effects, ambience
- **Surrounds**: Ambient, off-screen effects, immersion
- **LFE**: Low-frequency impact (use sparingly)

**Downmix Compatibility:**
- Always check stereo fold-down
- Ensure nothing is lost or buried
- Center channel elements remain audible
- Surround elements fold to stereo appropriately

---

## Audio Synchronization

### Types of Sync

**Lip Sync:**
- Matching audio to visible speech
- Most critical sync relationship
- Human perception very sensitive to lip sync errors
- Generally must be within 2-3 frames

**Sound Effect Sync:**
- Matching effects to visual events
- Some flexibility depending on sound type
- Hard sounds (impacts) require precise sync
- Soft sounds (ambience) more forgiving

### Sync Methods

**Camera Audio:**
- Audio recorded to camera
- Automatically synced
- Often lower quality than external recording

**Dual-System Audio:**
- Separate audio recorder (higher quality)
- Requires synchronization in post
- Sync via timecode, slate, or waveform

**Synchronization Techniques:**

**Timecode Sync:**
- Matching timecode from camera and recorder
- Most accurate method
- Requires timecode-capable equipment
- Jamming/syncing timecode before shooting

**Waveform Sync:**
- Software matches audio waveforms
- Uses camera audio as reference
- Generally accurate
- PluralEyes, Premiere Pro, DaVinci Resolve

**Manual Sync:**
- Align to clapper/slate
- Visual and audio spike alignment
- Time-consuming but reliable backup

### Sync Problems and Solutions

**Drift:**
- Audio gradually goes out of sync
- Caused by different sample rates
- Caused by clock differences
- Solution: Resample or stretch audio

**Jump Cuts:**
- Audio doesn't match edited video
- Solution: Edit audio to match picture
- Use room tone to fill gaps

**ADR Sync:**
- Replaced dialogue must match original
- Use waveform as guide
- Time-stretch for precise matching
- Manual adjustment for lip sync

---

## Audio Export Settings

### Common Export Formats

**Uncompressed:**
- WAV (Waveform Audio): Universal standard
- AIFF (Audio Interchange): Apple standard
- Best quality, largest files
- Use for masters and archives

**Lossless Compression:**
- FLAC: Open-source, widely supported
- ALAC: Apple lossless
- Smaller than uncompressed, no quality loss
- Good for archiving

**Lossy Compression:**
- AAC: High quality at lower bitrates
- MP3: Universal compatibility
- Quality loss, much smaller files
- Use for delivery, not masters

### Export Settings

**Sample Rate:**
- 48kHz: Video standard
- 44.1kHz: Audio CD standard
- 96kHz: High-resolution (if source is 96kHz)
- Match project and delivery requirements

**Bit Depth:**
- 24-bit: Professional standard
- 16-bit: CD standard, acceptable for delivery
- 32-bit float: Working format in DAW (not delivery)

**Channel Configuration:**
- Stereo: Most common
- Mono: Specific use cases
- 5.1/7.1: Surround deliverables
- Stems: Multiple separate mixes

### Delivery Specifications

**Full Mix:**
- Complete audio with all elements
- Primary deliverable
- Format per specifications

**Stems:**
- Separate mixes of element groups
- Dialogue, Music, Effects (D/M/E)
- Allows remixing/localization
- Match full mix levels when summed

**M&E (Music and Effects):**
- Mix without dialogue
- Used for foreign language dubbing
- Includes all non-dialogue elements
- Essential for international distribution

---

## Software Tools for Audio Post-Production

### Digital Audio Workstations (DAWs)

**Adobe Audition:**
- Integrated with Premiere Pro
- Excellent for podcast/voice work
- Strong noise reduction
- Multitrack and waveform editing
- Best for: Adobe workflow, podcasts

**Pro Tools:**
- Industry standard for film/TV
- Powerful mixing and automation
- Extensive plugin support
- Hardware integration options
- Best for: Professional film/TV audio

**Logic Pro:**
- Mac only, one-time purchase
- Excellent for music
- Strong built-in plugins
- Good for scoring to picture
- Best for: Music production, Mac users

**Audacity:**
- Free, open-source
- Basic but capable
- Cross-platform
- Good for simple tasks
- Best for: Beginners, basic editing

**DaVinci Resolve Fairlight:**
- Integrated with video editing
- Increasingly capable
- Free version available
- Best for: Resolve users, complete workflow

**Reaper:**
- Affordable, highly customizable
- Low system requirements
- Extensive flexibility
- Best for: Budget-conscious, customization

### Specialized Plugins

**Noise Reduction:**
- iZotope RX: Industry standard restoration
- Waves: WNS, X-Noise
- Accusonus ERA: User-friendly cleanup

**Dialogue Processing:**
- Waves: Clarity Vx, Renaissance Channel
- iZotope: Dialogue Match, RX
- FabFilter: Pro-C, Pro-Q

**Reverb:**
- Altiverb: Convolution reverb
- FabFilter Pro-R: Algorithmic reverb
- Valhalla: Various quality reverbs

**Loudness Metering:**
- iZotope Insight: Comprehensive metering
- Waves WLM Plus: Loudness meter
- Nugen VisLM: Loudness metering

---

## Common Audio Mistakes in Video

### Recording Mistakes

1. **Not monitoring audio during recording**: Discover problems too late
2. **Recording too hot**: Clipping and distortion (unrecoverable)
3. **Recording too quiet**: Excessive noise when boosted
4. **Ignoring room acoustics**: Problematic reverb/echo
5. **Poor microphone placement**: Inconsistent quality, off-axis sound

### Editing Mistakes

1. **Not using room tone**: Obvious edits, unnatural gaps
2. **Obvious audio edits**: Clicks, pops, level jumps
3. **Inconsistent dialogue levels**: Hard to follow conversation
4. **Over-processing**: Unnatural, artifacts
5. **Ignoring sync**: Distracting lip sync errors

### Mixing Mistakes

1. **Music too loud**: Drowns out dialogue
2. **Effects overwhelming**: Fatiguing, distracting
3. **Inconsistent levels**: Volume jumping throughout
4. **No headroom**: Clipping, distortion
5. **Not checking on multiple systems**: Sounds bad elsewhere

### Delivery Mistakes

1. **Wrong loudness standard**: Rejected or sounds wrong
2. **Missing deliverables**: No stems, M&E when required
3. **Wrong format/sample rate**: Compatibility issues
4. **No quality check**: Errors in final delivery
5. **No backup/archive**: Project lost

---

## Audio Post-Production Best Practices

### Production Planning

1. **Budget adequate time for audio**: Often underestimated
2. **Plan for ADR if needed**: Schedule talent availability
3. **Communicate delivery specs early**: Avoid last-minute changes
4. **Organize media before starting**: Saves time during editing

### Technical Excellence

1. **Work in proper sample rate/bit depth**: Match delivery requirements
2. **Maintain headroom throughout**: Prevent clipping
3. **Use reference tracks**: Compare to professional work
4. **Monitor at consistent levels**: Ensure accurate judgments
5. **Check on multiple systems**: Headphones, speakers, consumer devices

### Creative Standards

1. **Serve the story first**: Audio supports narrative
2. **Less is often more**: Don't overload the soundtrack
3. **Create contrast**: Dynamic range creates interest
4. **Listen critically**: Develop discerning ear
5. **Accept feedback**: Fresh ears catch what yours miss

### Workflow Efficiency

1. **Use templates**: Consistent starting points
2. **Create presets**: Reusable processing chains
3. **Organize sessions logically**: Clear labeling and structure
4. **Save incrementally**: Protect work with versions
5. **Document decisions**: Notes for future reference

---

## Conclusion

Audio post-production is a sophisticated discipline that combines technical expertise with creative sensibility. When done well, audio work is largely invisible to audiences—they simply experience a rich, immersive soundscape that enhances the visual story without calling attention to itself.

The key principles of successful audio post-production include:

- **Dialogue clarity**: The audience must understand what's being said
- **Appropriate balance**: All elements audible without competition
- **Emotional support**: Music and sound design enhance the narrative
- **Technical compliance**: Meeting delivery specifications
- **Seamless integration**: No distracting audio issues

Developing expertise requires practice, critical listening, and continuous learning. Study films and videos with excellent audio. Analyze how professionals handle dialogue, music, and effects. Invest in proper monitoring equipment to make accurate judgments.

Whether you're producing YouTube content, corporate videos, documentaries, or feature films, attention to audio quality elevates your work from amateur to professional. Remember: viewers may forgive imperfect visuals, but poor audio causes them to click away immediately.

Audio truly is half the video experience—invest the time and attention it deserves.
