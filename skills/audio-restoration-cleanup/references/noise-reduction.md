# Noise Reduction Techniques

This reference provides comprehensive coverage of noise reduction methods, from basic principles to advanced techniques for various types of unwanted audio.

## Understanding Noise

### Types of Noise

**Steady-State Noise**
- Consistent, continuous background sound
- Examples: Hiss, hum, buzz, fan noise, air conditioning
- Characteristics: Stable frequency content and amplitude
- Easiest to remove with profile-based noise reduction

**Variable Noise**
- Changes in level or character over time
- Examples: Traffic, wind, crowd noise
- Characteristics: Fluctuating amplitude and frequency content
- Requires adaptive noise reduction

**Impulse Noise**
- Brief, sudden sounds
- Examples: Clicks, pops, crackle
- Characteristics: Short duration, high amplitude
- Requires specialized de-click/de-crackle tools

**Tonal Noise**
- Specific frequencies or harmonics
- Examples: Electrical hum (50/60 Hz), whistles, resonances
- Characteristics: Narrow frequency bands
- Best removed with notch filters or spectral editing

**Broadband Noise**
- Distributed across wide frequency range
- Examples: White noise, pink noise, tape hiss
- Characteristics: Energy across spectrum
- Requires spectral noise reduction

### Noise Characteristics

**Signal-to-Noise Ratio (SNR)**
- Ratio of desired signal to noise level
- Measured in decibels (dB)
- Higher SNR = cleaner audio
- Low SNR makes restoration challenging

**Frequency Distribution**
- Where noise exists in frequency spectrum
- High-frequency: Hiss, sibilance
- Mid-frequency: Voice range, most problematic
- Low-frequency: Rumble, hum

**Temporal Distribution**
- When noise occurs
- Constant: Throughout recording
- Intermittent: Comes and goes
- Localized: Specific moments

## Profile-Based Noise Reduction

### Principle

Analyzes a sample of pure noise (noise print) and reduces similar frequencies throughout the audio while preserving the desired signal.

### Process

**Step 1: Capture Noise Profile**

1. **Find Noise-Only Section**
   - Locate 1-3 seconds with only noise (no signal)
   - Beginning or end of recording often works
   - Pauses between speech
   - Should be representative of noise throughout

2. **Select and Capture**
   - Highlight noise-only section
   - Use "Learn Noise" or "Capture Noise Print" function
   - Software analyzes frequency characteristics
   - Creates profile for reduction

3. **Verify Profile**
   - Some tools show captured profile visually
   - Ensure it represents the noise accurately
   - Recapture if needed

**Step 2: Apply Noise Reduction**

1. **Select Target Audio**
   - Entire file or specific sections
   - Can process selectively

2. **Adjust Parameters**
   - **Noise Reduction Amount**: How much to reduce (dB)
   - **Sensitivity/Threshold**: How aggressively to detect noise
   - **Frequency Smoothing**: Reduces artifacts
   - **Attack/Release**: How quickly reduction responds

3. **Preview and Adjust**
   - Listen to processed audio
   - Check for artifacts
   - Adjust parameters as needed
   - Compare to original

4. **Process**
   - Apply reduction
   - Save or continue editing

### Parameters Explained

**Noise Reduction Amount**
- How many dB to reduce noise
- Range typically 0-24 dB
- Start conservative (6-12 dB)
- Increase gradually if needed
- Higher values risk artifacts

**Threshold/Sensitivity**
- Determines what's considered noise vs. signal
- Lower threshold = more aggressive
- Higher threshold = more conservative
- Adjust based on SNR

**Frequency Resolution**
- Number of frequency bands analyzed
- Higher resolution = more precise
- Lower resolution = faster, smoother
- Typical range: 2048-8192 FFT size

**Smoothing**
- Blends frequency bands
- Reduces "musical noise" artifacts
- Higher smoothing = fewer artifacts, less precision
- Balance based on noise type

**Attack and Release**
- How quickly reduction responds to changes
- Fast attack: Quick response, potential artifacts
- Slow attack: Smoother, may miss transients
- Adjust for material (fast for music, slower for speech)

### Best Practices

**Multiple Passes**
- Better to process multiple times with moderate settings
- Example: 3 passes at 6 dB each vs. 1 pass at 18 dB
- Reduces artifacts
- More natural sound

**Preserve Ambience**
- Don't remove all noise
- Some room tone sounds natural
- Complete silence can sound unnatural
- Aim for 10-15 dB reduction, not elimination

**Monitor for Artifacts**
- **Musical noise**: Random tones, like wind chimes
- **Underwater sound**: Muffled, filtered quality
- **Pumping**: Level fluctuations
- **Metallic quality**: Harsh, artificial sound
- If artifacts appear, reduce amount or adjust parameters

**Frequency-Specific Processing**
- Process different frequency ranges separately
- Example: More aggressive on high frequencies (hiss)
- Less aggressive on mid frequencies (voice)
- Preserve low frequencies (warmth)

## Adaptive Noise Reduction

### Principle

Continuously analyzes audio and adapts to changing noise characteristics in real-time, without requiring a noise profile.

### Advantages

- Handles variable noise levels
- No need for noise-only section
- Adapts to changing environments
- Good for long-form content
- Real-time capable

### Disadvantages

- Less precise than profile-based
- May struggle with low SNR
- Can affect signal if not careful
- Requires more processing power

### Parameters

**Adaptation Speed**
- How quickly algorithm responds to changes
- Fast: Responsive but may introduce artifacts
- Slow: Smoother but may lag behind changes
- Adjust based on noise variability

**Threshold**
- Determines noise vs. signal
- Lower = more aggressive
- Higher = more conservative
- Critical parameter for quality

**Reduction Amount**
- How much to reduce detected noise
- Similar to profile-based reduction
- Start moderate, adjust as needed

**Frequency Range**
- Which frequencies to process
- Can limit to specific ranges
- Useful for targeted reduction

### Applications

**Location Recording**
- Variable traffic noise
- Changing wind conditions
- Crowd noise that varies

**Podcasts and Interviews**
- Long-form content
- Changing room acoustics
- Multiple speakers and environments

**Live Streaming**
- Real-time processing
- Unpredictable noise
- No opportunity for post-processing

**Documentary Footage**
- Varied locations
- Uncontrolled environments
- Mixed noise types

### Best Practices

- Start with conservative settings
- Monitor throughout recording
- Adjust in real-time if possible
- Combine with profile-based for best results
- Use as starting point, refine in post

## Specialized Noise Reduction

### De-Hum

**Electrical Hum Characteristics**
- Fundamental frequency: 50 Hz (Europe/Asia/Africa) or 60 Hz (Americas)
- Harmonics at integer multiples: 120, 180, 240, 300 Hz, etc.
- Caused by power lines, lighting, equipment
- Can have 10+ harmonics

**Removal Methods**

**1. Notch Filtering**

Manual placement of narrow filters at hum frequencies.

**Process**:
- Identify fundamental (50 or 60 Hz)
- Calculate harmonics (multiply by 2, 3, 4, etc.)
- Place notch filter at each frequency
- Use narrow Q (bandwidth), typically 0.5-2.0
- Adjust depth (typically -20 to -40 dB)

**Advantages**:
- Precise control
- Minimal impact on surrounding frequencies
- Transparent when done well

**Disadvantages**:
- Time-consuming (many filters needed)
- Manual calculation required
- Doesn't adapt to frequency drift

**2. Automatic De-Hum**

Specialized tools that detect and remove hum automatically.

**Process**:
- Tool analyzes audio
- Detects fundamental frequency
- Identifies harmonics
- Applies adaptive filtering
- Tracks frequency variations

**Advantages**:
- Fast and easy
- Adapts to frequency drift
- Handles complex hum patterns

**Disadvantages**:
- Less control than manual
- May miss some harmonics
- Can affect nearby frequencies

**3. Spectral Editing**

Visual identification and reduction in spectrogram.

**Process**:
- View audio in spectral editor
- Identify hum as horizontal lines
- Select each hum frequency
- Reduce or remove
- Check entire spectrum for harmonics

**Advantages**:
- Visual confirmation
- Precise targeting
- Can handle complex cases

**Disadvantages**:
- Time-consuming
- Requires skill to identify
- Manual process

**Best Practices**:
- Identify all harmonics (check up to 1 kHz or higher)
- Use narrow filters to preserve nearby frequencies
- Check for subharmonics (25/30 Hz)
- Monitor for over-processing
- Verify removal across entire recording

### De-Buzz

Similar to de-hum but for higher-frequency buzzing.

**Characteristics**:
- Often related to electrical interference
- May have irregular harmonics
- Can be variable in frequency

**Removal**:
- Similar techniques to de-hum
- May require wider filters
- Spectral editing often most effective
- Adaptive tools work well for variable buzz

### De-Hiss

**Hiss Characteristics**
- High-frequency broadband noise
- Common in analog recordings (tape hiss)
- Also from preamps, microphones
- Distributed across high frequencies (above 2-3 kHz)

**Removal Methods**

**1. High-Frequency Noise Reduction**
- Profile-based reduction focused on high frequencies
- Capture hiss profile
- Apply reduction above 2-3 kHz
- Preserve mid and low frequencies

**2. Multiband Noise Reduction**
- Process high frequencies more aggressively
- Lighter processing on mids and lows
- Maintains tonal balance

**3. Dynamic EQ**
- Reduces high frequencies only when hiss is present
- Preserves high-frequency content in signal
- More transparent than static EQ

**Best Practices**:
- Don't over-process (dulls audio)
- Preserve some high-frequency content
- Use multiple light passes
- Compare to original frequently
- Accept some residual hiss for natural sound

### De-Rumble

**Rumble Characteristics**
- Low-frequency noise
- Sources: HVAC, traffic, handling, turntable rumble
- Typically below 80-100 Hz

**Removal Methods**

**1. High-Pass Filtering**
- Remove frequencies below certain point
- Typical cutoff: 60-100 Hz (depends on content)
- Slope: 12-24 dB/octave
- Preserves musical low end

**2. Spectral Editing**
- Visual identification of rumble
- Selective reduction
- Preserves desired low frequencies

**3. Multiband Compression**
- Reduces low-frequency dynamics
- Controls rumble without removing all lows
- More transparent than filtering

**Best Practices**:
- Check content for desired low frequencies
- Don't cut too high (removes warmth)
- Use gentle slopes for natural sound
- Monitor on full-range speakers
- Consider content type (music needs more lows than speech)

## Advanced Techniques

### Multiband Noise Reduction

**Principle**: Process different frequency ranges with different settings.

**Process**:
1. Divide spectrum into bands (low, mid, high)
2. Apply different noise reduction to each
3. Recombine bands

**Advantages**:
- Targeted processing
- Preserves important frequencies
- More transparent
- Better tonal balance

**Example Settings**:
- Low (20-200 Hz): Light reduction, preserve warmth
- Mid (200-3000 Hz): Moderate reduction, preserve voice
- High (3000-20000 Hz): Aggressive reduction, remove hiss

### Spectral Noise Reduction

**Principle**: Analyzes and processes individual frequency bands over time.

**Advantages**:
- Extremely precise
- Handles complex noise
- Minimal artifacts when done well

**Process**:
- FFT analysis of audio
- Identifies noise in each frequency band
- Applies reduction to each band independently
- Reconstructs audio

**Parameters**:
- FFT size: Frequency resolution
- Overlap: Smoothness of processing
- Threshold: Noise detection sensitivity
- Reduction: Amount to reduce

### Dialogue-Specific Noise Reduction

**Challenges**:
- Noise often in same frequency range as voice
- Must preserve intelligibility
- Artifacts very noticeable

**Techniques**:

**1. Dialogue Isolate (iZotope RX)**
- AI-powered separation of dialogue from background
- Preserves voice quality
- Removes background noise, reverb
- Real-time capable

**2. Spectral Editing Between Words**
- Aggressive noise reduction in pauses
- Light reduction during speech
- Maintains voice quality
- Time-consuming but effective

**3. Multiband Processing**
- Preserve mid frequencies (voice fundamentals)
- Reduce lows (rumble) and highs (hiss)
- Careful with 2-4 kHz (voice presence)

**Best Practices**:
- Prioritize intelligibility over complete noise removal
- Accept some noise during speech
- Process pauses more aggressively
- Use dialogue-specific tools when available
- Test on various playback systems

### Noise Gating

**Principle**: Reduces or mutes audio below a threshold, removing noise in quiet sections.

**Parameters**:
- **Threshold**: Level below which gate closes
- **Attack**: How quickly gate opens
- **Release**: How quickly gate closes
- **Hold**: Minimum time gate stays open
- **Range**: How much to reduce (not full mute)

**Applications**:
- Removing noise between words or phrases
- Cleaning up pauses
- Reducing background in quiet sections

**Limitations**:
- Doesn't help during signal
- Can sound unnatural (sudden silence)
- Requires careful adjustment
- Not suitable for all material

**Best Practices**:
- Use range (partial reduction) instead of full gate
- Set attack fast enough to not cut signal
- Set release slow enough for natural decay
- Use hold to prevent chattering
- Combine with other noise reduction

## Artifact Management

### Common Artifacts

**Musical Noise**
- Random tones, like wind chimes
- Caused by aggressive noise reduction
- Frequency bands being turned on/off

**Solution**:
- Reduce noise reduction amount
- Increase smoothing
- Use multiple light passes
- Lower frequency resolution

**Underwater/Muffled Sound**
- Loss of high frequencies
- Dull, filtered quality
- Over-processed noise reduction

**Solution**:
- Reduce amount of noise reduction
- Process high frequencies less aggressively
- Use multiband processing
- Add subtle high-frequency enhancement

**Pumping/Breathing**
- Level fluctuations
- Noise reduction responding to signal changes
- Sounds like breathing or pumping

**Solution**:
- Adjust attack/release times
- Reduce sensitivity
- Use adaptive noise reduction
- Process in shorter sections

**Metallic Quality**
- Harsh, artificial sound
- Excessive spectral processing
- Phase issues

**Solution**:
- Reduce processing amount
- Increase smoothing
- Check for phase problems
- Use different algorithm

### Minimizing Artifacts

**General Strategies**:
- Use lightest effective settings
- Multiple passes with moderate settings
- Increase smoothing/frequency blending
- Preserve some noise for natural sound
- Monitor on multiple systems
- Take breaks to avoid ear fatigue
- Compare to original frequently

**Testing**:
- Listen to processed audio critically
- Check on headphones and speakers
- Listen at different volumes
- Have others listen (fresh ears)
- Solo different frequency ranges

## Workflow Integration

### When to Apply Noise Reduction

**Early in Chain**:
- Before compression or limiting
- Before EQ (in most cases)
- After structural repairs (de-clip, dropout repair)

**Rationale**:
- Compression amplifies noise
- EQ can emphasize noise
- Clean signal processes better

**Exception**:
- Sometimes EQ before noise reduction helps
- Remove problematic frequencies first
- Then apply noise reduction

### Combining Techniques

**Layered Approach**:
1. Remove tonal noise (de-hum, de-buzz)
2. Remove impulse noise (de-click, de-crackle)
3. Apply broadband noise reduction
4. Spectral editing for remaining issues
5. Final polish (subtle EQ, compression)

**Rationale**:
- Each tool addresses specific problem
- Easier to process one issue at a time
- Better results than trying to fix everything at once

### Real-Time vs. Offline Processing

**Real-Time**:
- During recording or live streaming
- Immediate results
- Less control
- Adaptive algorithms work well

**Offline**:
- Post-production
- More control and precision
- Can use more intensive processing
- Can compare and revise

**Hybrid**:
- Real-time during recording (safety)
- Offline refinement in post
- Best of both worlds

## Conclusion

Noise reduction is both science and art. Understanding the technical principles allows you to choose the right tools and settings, while critical listening and experience guide you to natural, transparent results. The goal is not to eliminate all noise, but to reduce it to acceptable levels while preserving the integrity and character of the original audio. With practice and patience, even heavily contaminated recordings can be restored to professional quality.