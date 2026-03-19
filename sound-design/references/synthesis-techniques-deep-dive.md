# Synthesis Techniques Deep Dive

Comprehensive exploration of synthesis methods, advanced techniques, and practical applications for professional sound design.

---

## Subtractive Synthesis In-Depth

### Historical Context

Subtractive synthesis emerged with early analog synthesizers in the 1960s-70s, becoming the foundation of electronic music. The term "patch" originates from physical patch cables used to connect modules in modular synthesizers.

### Signal Flow

**Classic Subtractive Synthesis Chain:**
```
Oscillator(s) → Mixer → Filter → Amplifier (VCA) → Output
     ↑              ↑           ↑
   LFO/Env       LFO/Env    Envelope
```

### Advanced Oscillator Techniques

**Pulse Width Modulation (PWM):**
- Varies duty cycle of square wave
- Creates chorusing, animated effect
- Modulate with LFO for classic analog movement
- Sweet spot: 20-80% pulse width

**Oscillator Sync:**
- Slave oscillator resets when master completes cycle
- Creates harmonic-rich, aggressive tones
- Modulate slave pitch for timbral changes
- Classic for screaming leads

**Ring Modulation:**
- Multiplies two waveforms
- Creates sum and difference frequencies
- Inharmonic, metallic tones
- Used for bells, sci-fi effects, aggressive sounds

**Amplitude Modulation (AM):**
- Similar to ring modulation but doesn't invert polarity
- Retains original frequencies plus sidebands
- Smoother than ring modulation

### Filter Types and Characteristics

**Filter Slopes:**
- 6 dB/octave: Gentle, subtle filtering
- 12 dB/octave: Standard, musical filtering
- 24 dB/octave: Steep, aggressive filtering (Moog-style)
- 48 dB/octave: Extreme, surgical filtering

**Filter Models:**
- **Moog Ladder:** Warm, musical, self-oscillates smoothly
- **State Variable:** Versatile, multiple outputs (LP, HP, BP, Notch)
- **Sallen-Key:** Clean, precise, less character
- **Diode Ladder:** Aggressive, acidic (TB-303 style)

**Self-Oscillation:**
- Filter resonates at cutoff frequency when resonance at maximum
- Creates pure sine wave tone
- Useful for sub-bass, tonal effects
- Can be played melodically by modulating cutoff

### Envelope Variations

**ADSR Extensions:**
- **AHDSR:** Attack, Hold, Decay, Sustain, Release
  - Hold stage maintains peak before decay
- **DADSR:** Delay, Attack, Decay, Sustain, Release
  - Delay before attack begins
- **Multi-Stage:** Complex envelopes with multiple breakpoints
  - Precise control over evolution

**Envelope Curves:**
- Linear: Constant rate of change
- Exponential: Natural, musical decay
- Logarithmic: Smooth attack, perceived as linear

---

## FM Synthesis In-Depth

### FM Theory

**Basic FM Equation:**
```
Output = sin(2π × fc × t + I × sin(2π × fm × t))

Where:
fc = Carrier frequency
fm = Modulator frequency
I = Modulation index (depth)
t = Time
```

**Sidebands:**
- FM creates sidebands at fc ± (n × fm)
- Number and amplitude of sidebands determined by modulation index
- Higher index = more sidebands = brighter, more complex sound

### Operator Configurations

**Algorithms:**
Arrangement of operators (oscillators) in FM synthesis.

**Common Configurations:**

**Stack (Serial):**
```
Op1 → Op2 → Op3 → Op4 → Output
```
- Each operator modulates the next
- Complex, inharmonic timbres
- Bright, metallic sounds

**Parallel:**
```
Op1 →
Op2 → Mixer → Output
Op3 →
Op4 →
```
- All operators output to mixer
- Additive-style layering
- Organ-like sounds

**Hybrid:**
```
Op1 → Op2 →
              Mixer → Output
Op3 → Op4 →
```
- Combines serial and parallel
- Versatile, balanced complexity
- Most common in DX7 algorithms

### Ratio and Frequency Relationships

**Integer Ratios:**
- Harmonic relationships (1:1, 1:2, 1:3, etc.)
- Musical, tonal sounds
- Stable, predictable timbre

**Non-Integer Ratios:**
- Inharmonic relationships (1:1.5, 1:2.7, etc.)
- Metallic, bell-like sounds
- Complex, evolving timbre

**Fixed Frequencies:**
- Modulator at fixed Hz (not ratio)
- Timbre changes with pitch
- Useful for formant-like effects

### FM Sound Design Techniques

**Electric Piano:**
- Algorithm: 1 → 2, 3 → 4 (two stacks in parallel)
- Ratios: 1:1 or 1:2 for carriers, 14:1 for modulators
- Fast attack, medium decay, no sustain
- Velocity-sensitive modulation index

**Bass:**
- Simple algorithm: 1 → 2
- Ratio: 1:1 (carrier and modulator same frequency)
- High modulation index for harmonics
- Filter to shape tone

**Bells:**
- Multiple operators with non-integer ratios
- Ratios: 1:1.4, 1:2.3, 1:3.7
- Fast attack, long decay, no sustain
- High initial modulation index, decaying over time

**Brass:**
- Algorithm: 1 → 2 → 3
- Ratios: 1:1:1 or slight detuning
- Envelope-controlled modulation index
- Velocity-sensitive brightness

---

## Wavetable Synthesis In-Depth

### Wavetable Concepts

**Wavetable vs. Waveform:**
- **Waveform:** Single cycle of audio (sine, saw, square)
- **Wavetable:** Collection of waveforms arranged in sequence
- Wavetable position determines which waveform is played

**Wavetable Scanning:**
- Smoothly morph between waveforms in table
- Modulate position with LFO, envelope, or manually
- Creates evolving, dynamic timbres

### Creating Custom Wavetables

**From Audio:**
1. Import audio sample
2. Analyze and extract single-cycle waveforms
3. Arrange waveforms in sequence
4. Smooth transitions between frames

**From Synthesis:**
1. Generate waveforms using synthesis or math functions
2. Create variations (filter sweeps, harmonic changes)
3. Arrange in wavetable
4. Export for use in wavetable synth

**Tools:**
- Serum: Built-in wavetable editor
- WaveEdit: Standalone wavetable creation
- Audacity: Extract single-cycle waveforms

### Advanced Wavetable Techniques

**Unison and Detune:**
- Multiple voices playing same wavetable
- Slight pitch detuning between voices
- Creates width and thickness
- "Supersaw" effect: 7-9 detuned saw waves

**Wavetable Modulation:**
- LFO modulating wavetable position
- Envelope sweeping through wavetable
- Velocity controlling wavetable position
- Creates dynamic, responsive sounds

**Phase Modulation:**
- Modulate phase of wavetable oscillator
- Similar to FM synthesis
- Creates complex, evolving timbres

---

## Granular Synthesis In-Depth

### Granular Parameters

**Grain Size:**
- 1-10ms: Percussive, glitchy textures
- 10-50ms: Smooth, musical textures
- 50-100ms: Recognizable source material
- Larger grains = more source recognition

**Grain Density:**
- Low density (1-10 grains/sec): Sparse, rhythmic
- Medium density (10-50 grains/sec): Textured, musical
- High density (50+ grains/sec): Smooth, continuous

**Grain Envelope:**
- Shape of each grain (attack/decay)
- Gaussian (bell curve): Smooth, no clicks
- Rectangular: Percussive, potential clicks
- Affects texture and smoothness

**Playback Position:**
- Fixed: Loops small section
- Scanning: Moves through source audio
- Random: Unpredictable, chaotic
- Modulated: LFO or envelope controls position

### Granular Techniques

**Time-Stretching:**
- Slow down or speed up audio without pitch change
- Grain position advances slower/faster than real-time
- Maintains pitch by resampling grains

**Pitch-Shifting:**
- Change pitch without affecting duration
- Resample grains at different rate
- Maintain playback speed

**Granular Clouds:**
- Random grain parameters (size, pitch, position)
- Creates evolving, organic textures
- Useful for pads and atmospheres

**Granular Delay:**
- Grains extracted from delayed signal
- Creates shimmering, reverb-like effects
- Pitch and time modulation for movement

---

## Physical Modeling In-Depth

### Modeling Approaches

**Modal Synthesis:**
- Models resonant modes of object
- Each mode = sine wave with specific frequency, amplitude, decay
- Sum of modes creates complex timbre
- Efficient for metallic and percussive sounds

**Waveguide Synthesis:**
- Models wave propagation through medium
- Simulates strings, tubes, membranes
- Delay lines represent wave travel time
- Filters simulate energy loss

**Mass-Spring Systems:**
- Models physical objects as connected masses and springs
- Simulates vibration and resonance
- Computationally intensive
- Highly realistic and expressive

### Physical Modeling Parameters

**Excitation:**
- How object is set into vibration
- Pluck, strike, bow, blow
- Affects attack and initial timbre

**Resonator:**
- Vibrating body of instrument
- String, tube, membrane, plate
- Determines sustained timbre

**Material Properties:**
- Stiffness, damping, density
- Affects tone, decay, and realism

**Geometry:**
- Size, shape, thickness
- Determines pitch and harmonic content

---

## Advanced Modulation Techniques

### Matrix Modulation

**Concept:**
Flexible routing of modulation sources to multiple destinations.

**Implementation:**
- Modulation matrix with sources (rows) and destinations (columns)
- Assign any source to any destination
- Control modulation depth per connection
- Multiple sources can modulate same destination

**Benefits:**
- Extreme flexibility
- Complex, evolving sounds
- Efficient workflow

### Envelope Followers

**Concept:**
Extract amplitude envelope from audio signal to modulate parameters.

**Applications:**
- Sidechain effects (ducking, pumping)
- Dynamic filtering (louder = brighter)
- Vocoder-style effects
- Rhythmic modulation from drums

### Step Sequencers as Modulators

**Concept:**
Use step sequencer to create rhythmic modulation patterns.

**Applications:**
- Rhythmic filter cutoff changes
- Stepped pitch sequences (arpeggios)
- Rhythmic panning or stereo width
- Gate patterns for rhythmic effects

### Macro Controls

**Concept:**
Single control modulates multiple parameters simultaneously.

**Implementation:**
1. Assign multiple parameters to macro
2. Set modulation depth for each parameter
3. Control all parameters with single knob/slider

**Benefits:**
- Simplified performance control
- Complex timbral changes with single movement
- Useful for live performance and automation

---

## Analog vs. Digital Synthesis

### Analog Synthesis

**Characteristics:**
- Voltage-controlled oscillators (VCOs)
- Continuous, smooth parameter changes
- Slight pitch instability (drift)
- Harmonic distortion and saturation
- Limited polyphony (often monophonic)

**Advantages:**
- Warm, organic sound
- Tactile, hands-on control
- Unique character and imperfections
- No aliasing or digital artifacts

**Disadvantages:**
- Expensive
- Requires maintenance and calibration
- Limited preset recall
- Temperature-sensitive

### Digital Synthesis

**Characteristics:**
- Digitally generated waveforms
- Precise, stable tuning
- Complex algorithms (FM, wavetable, granular)
- Extensive polyphony
- Perfect preset recall

**Advantages:**
- Affordable
- Stable and reliable
- Complex synthesis methods
- Extensive modulation options
- Easy integration with DAWs

**Disadvantages:**
- Potential aliasing (high-frequency artifacts)
- Can sound sterile or cold
- Less tactile than hardware

### Hybrid Approach

**Analog Modeling:**
- Digital emulation of analog circuits
- Combines analog warmth with digital convenience
- Examples: U-he Diva, Arturia V Collection

**Digital Oscillators with Analog Filters:**
- Stable digital oscillators
- Warm analog filtering
- Best of both worlds
- Examples: Dave Smith Prophet 12, Moog Subsequent 37

---

## Synthesis in Different Genres

### Electronic Dance Music (EDM)

**Basses:**
- Wavetable synthesis (Serum, Massive)
- Heavy distortion and processing
- Sidechain compression for pumping
- Sub-bass layer (sine wave)

**Leads:**
- Bright, cutting waveforms (saws, squares)
- Unison and detune for width
- Filter modulation for movement
- Reverb and delay for space

**Plucks:**
- Fast attack, short decay
- Filter envelope for brightness decay
- Delay for rhythmic interest
- Layered with percussion

### Ambient and Soundscapes

**Pads:**
- Slow attack, long release
- Multiple detuned oscillators
- Lush reverb and chorus
- Subtle modulation for evolution

**Textures:**
- Granular synthesis of field recordings
- Layered, evolving sounds
- Minimal rhythmic elements
- Emphasis on space and atmosphere

### Hip-Hop and Trap

**808 Bass:**
- Sine wave with pitch envelope
- Fast pitch decay (1-2 octaves)
- Slight distortion for harmonics
- Tuned to song key

**Synth Leads:**
- Simple waveforms (saw, square)
- Minimal processing
- Melodic, catchy phrases
- Often sampled and chopped

### Synthwave and Retro

**Analog-Style Sounds:**
- Subtractive synthesis
- Warm, vintage character
- Chorus and analog delay
- Gated reverb on drums

**Arpeggios:**
- Step sequencer patterns
- Sync'd to tempo
- Filter and resonance modulation
- Sidechain compression