# Sampling and Processing

Comprehensive guide to sampling techniques, sample manipulation, and creative audio processing for sound design.

---

## Sampling Fundamentals

### Sample Rate and Bit Depth

**Sample Rate:**
- Number of samples per second (measured in Hz or kHz)
- Determines maximum frequency that can be captured
- Nyquist theorem: Sample rate must be 2x highest frequency
- Common rates:
  - 44.1 kHz: CD quality, captures up to 22.05 kHz
  - 48 kHz: Video standard, professional audio
  - 96 kHz: High-resolution audio
  - 192 kHz: Archival, extreme detail

**Bit Depth:**
- Number of bits per sample
- Determines dynamic range and noise floor
- Each bit = ~6 dB dynamic range
- Common depths:
  - 16-bit: 96 dB dynamic range (CD quality)
  - 24-bit: 144 dB dynamic range (professional standard)
  - 32-bit float: Virtually unlimited dynamic range

**Recommendations:**
- Recording: 24-bit, 48 kHz minimum
- Archival: 24-bit, 96 kHz
- Distribution: 16-bit, 44.1 kHz (CD), 24-bit, 48 kHz (streaming)

---

## Recording Samples

### Field Recording

**Equipment:**
- Portable recorder (Zoom H5, H6, Tascam DR-40)
- Shotgun or stereo microphone
- Windscreen for outdoor recording
- Headphones for monitoring

**Techniques:**
- Record at 24-bit for maximum dynamic range
- Leave headroom (peaks at -12 dB to -6 dB)
- Record room tone (30-60 seconds of silence)
- Multiple takes for variety
- Note recording details (location, source, settings)

**Sources:**
- Nature sounds (birds, water, wind)
- Urban environments (traffic, crowds, machinery)
- Household objects (doors, appliances, utensils)
- Musical instruments (unconventional playing techniques)

---

### Studio Sampling

**Instrument Sampling:**
- Record multiple velocities (soft, medium, hard)
- Capture full range of instrument (all notes)
- Record multiple round-robins (variations of same note)
- Include articulations (staccato, legato, vibrato)

**Foley Recording:**
- Perform actions in sync with visual
- Record multiple takes for selection
- Use props and surfaces for variety
- Close-mic for detail and control

---

## Sample Editing

### Trimming and Looping

**Trimming:**
- Remove silence before and after sound
- Leave small amount of silence (fade-in/out space)
- Ensure clean start and end (zero-crossing points)

**Looping:**
- Find loop points where waveform matches
- Use crossfade to smooth transition
- Adjust loop length to avoid phasing
- Test loop for seamless playback

**Loop Types:**
- **Forward Loop:** Plays forward repeatedly
- **Ping-Pong Loop:** Plays forward, then backward
- **One-Shot:** No loop, plays once

---

### Pitch and Time Manipulation

**Pitch-Shifting:**
- Change pitch without affecting duration
- Algorithms:
  - **Granular:** High quality, minimal artifacts
  - **Formant-Preserving:** Maintains vocal character
  - **Classic:** Faster, lower quality
- Applications:
  - Transpose samples to different keys
  - Create harmonies from single recording
  - Extreme shifts for creative effects

**Time-Stretching:**
- Change duration without affecting pitch
- Algorithms:
  - **Complex:** High quality for polyphonic material
  - **Rhythmic:** Preserves transients for drums
  - **Monophonic:** Optimized for single-note sources
- Applications:
  - Match sample tempo to project
  - Create slow-motion or fast-motion effects
  - Extreme stretching for ambient textures

---

### Normalization and Gain

**Peak Normalization:**
- Raises level so highest peak reaches target (e.g., -0.1 dB)
- Maintains dynamic relationships
- Useful for maximizing level without clipping

**RMS Normalization:**
- Adjusts average level to target
- More consistent perceived loudness
- Useful for sample libraries

**Gain Adjustment:**
- Manual level adjustment
- Useful for matching levels across samples
- Avoid clipping (peaks above 0 dB)

---

## Creative Sample Processing

### Reverse and Reverse Reverb

**Reverse:**
- Flip sample playback direction
- Creates unnatural, ethereal sounds
- Useful for transitions and effects

**Reverse Reverb:**
1. Reverse sample
2. Apply heavy reverb
3. Bounce/render audio
4. Reverse again
- Creates swelling, cinematic effect
- Classic for vocals and impacts

---

### Granular Processing

**Granular Resynthesis:**
- Break sample into grains
- Rearrange, layer, or process grains
- Creates evolving textures from static samples

**Parameters:**
- **Grain Size:** Smaller = more textured, larger = more recognizable
- **Grain Density:** Sparse = rhythmic, dense = smooth
- **Grain Position:** Fixed = loop, scanning = evolving
- **Pitch/Time:** Independent control for creative effects

**Applications:**
- Transform vocals into pads
- Create atmospheric textures from percussion
- Time-stretch without artifacts

---

### Convolution

**Concept:**
Apply characteristics of one sound (impulse response) to another.

**Applications:**
- **Reverb:** Use impulse response of real space
- **Timbral Transfer:** Apply frequency characteristics of one sound to another
- **Creative Effects:** Use unconventional impulse responses (drums, synths)

**Workflow:**
1. Capture or create impulse response
2. Load into convolution plugin
3. Process target audio
4. Adjust mix and parameters

---

### Spectral Processing

**Spectral Editing:**
- Visual editing of frequency content over time
- Surgical removal of unwanted sounds
- Isolate specific frequencies

**Tools:**
- iZotope RX (industry standard)
- Adobe Audition Spectral Editor
- SpectraLayers Pro

**Applications:**
- Remove background noise
- Isolate vocals or instruments
- Create unique textures by removing/isolating frequencies

---

## Multi-Sampling

### Velocity Layers

**Concept:**
Record same note at different velocities for dynamic response.

**Typical Layers:**
- Soft (pp): Gentle, mellow
- Medium (mf): Balanced, natural
- Hard (ff): Aggressive, bright
- Very Hard (fff): Maximum intensity (optional)

**Benefits:**
- Realistic dynamic response
- Expressive playability
- Natural timbral variation

---

### Round-Robins

**Concept:**
Multiple recordings of same note/velocity to avoid "machine-gun" effect.

**Implementation:**
- Record 3-5 variations of each note
- Sampler cycles through variations
- Creates natural, organic feel

**Benefits:**
- Avoids repetitive, robotic sound
- Adds realism and variation
- Essential for realistic instrument emulation

---

### Key Mapping

**Chromatic Mapping:**
- Each key triggers different sample
- Full keyboard range
- Realistic pitch across range

**Zone Mapping:**
- Different samples in different key ranges
- Example: Bass in low range, lead in high range
- Efficient use of keyboard

**Layered Mapping:**
- Multiple samples triggered by single key
- Velocity or modulation determines which layer plays
- Creates complex, dynamic sounds

---

## Creating Custom Wavetables

### From Audio Samples

**Workflow:**
1. Select source audio (synth, vocal, instrument)
2. Extract single-cycle waveforms
   - Use wavetable editor (Serum, WaveEdit)
   - Manually select and export cycles
3. Arrange waveforms in sequence
4. Create smooth transitions between frames
5. Export as wavetable file

**Tips:**
- Use diverse source material for variety
- Ensure smooth transitions to avoid clicks
- Test wavetable across pitch range

---

### From Synthesis

**Workflow:**
1. Generate waveforms using synthesis or math functions
2. Create variations (filter sweeps, harmonic changes)
3. Arrange in wavetable
4. Export for use in wavetable synth

**Techniques:**
- Morph between basic waveforms (sine to saw)
- Apply filter sweeps to create evolving wavetable
- Use additive synthesis to build custom harmonics

---

## Sample Libraries and Organization

### Building a Personal Library

**Categories:**
- Drums and Percussion
- Bass and Sub-Bass
- Leads and Melodies
- Pads and Atmospheres
- FX and Transitions
- Vocals and Vocal Chops
- Field Recordings and Foley

**Organization:**
- Consistent folder structure
- Descriptive file names
- Metadata and tags
- Preview/audition system

**Maintenance:**
- Regularly review and cull unused samples
- Back up library to multiple locations
- Update organization as library grows

---

### Sample Library Tools

**Sample Managers:**
- **ADSR Sample Manager:** Free, cross-platform
- **Soundly:** Professional, extensive library integration
- **Loopcloud:** Cloud-based, AI-powered search
- **Native Instruments Komplete Kontrol:** Integrated with NI ecosystem

**Benefits:**
- Fast search and preview
- Tag-based organization
- Integration with DAW
- Cloud sync and backup

---

## Legal and Ethical Considerations

### Copyright and Licensing

**Royalty-Free Samples:**
- One-time purchase, unlimited use
- Check license for commercial use restrictions
- Examples: Splice, Loopmasters, Sample Magic

**Creative Commons:**
- Various licenses (CC0, CC BY, CC BY-SA, etc.)
- Check specific license terms
- Attribution may be required
- Examples: Freesound.org, ccMixter

**Sampling Existing Music:**
- Requires clearance and licensing
- Expensive and time-consuming
- Transformative use may qualify as fair use (consult lawyer)
- Avoid uncleared samples in commercial releases

---

### Ethical Sampling

**Best Practices:**
- Credit original creators when possible
- Respect cultural significance of sounds
- Avoid exploitative sampling practices
- Support sample creators by purchasing libraries

**Transformative Use:**
- Significantly alter samples to create new work
- Combine multiple sources
- Use samples as starting point, not focal element
- Adds creative value beyond original

---

## Advanced Techniques

### Convolution Reverb with Custom IRs

**Creating Custom Impulse Responses:**
1. Record space with impulse sound (balloon pop, starter pistol)
2. Deconvolve recording to extract IR
3. Load IR into convolution reverb
4. Apply to audio for realistic space

**Creative IRs:**
- Use drum hits, synth sounds, or vocals as IRs
- Creates unique, unconventional reverb effects
- Experiment with different sources

---

### Vocoding and Formant Shifting

**Vocoding:**
- Impose frequency characteristics of one sound onto another
- Classic: Voice modulating synth
- Creates robotic, synthesized vocals

**Formant Shifting:**
- Shift formants (resonant frequencies) without changing pitch
- Makes vocals sound larger, smaller, or different gender
- Useful for character voices and creative effects

---

### Sidechain Processing

**Sidechain Compression:**
- Compressor triggered by external signal
- Classic: Kick triggers compression on bass (ducking)
- Creates rhythmic pumping effect

**Sidechain Gating:**
- Gate triggered by external signal
- Rhythmic gating effects
- Useful for creating rhythmic textures from sustained sounds

**Sidechain EQ:**
- Dynamic EQ triggered by external signal
- Frequency-specific ducking
- Resolve frequency conflicts between instruments