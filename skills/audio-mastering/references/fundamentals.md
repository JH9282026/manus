# Audio Mastering Fundamentals

Comprehensive guide to core mastering concepts and foundational techniques.

## Signal Flow and Processing Chain

### Typical Mastering Chain Order

1. **Input Gain Staging** — Set appropriate input levels for optimal headroom
2. **Corrective EQ** — Address frequency problems from mixing stage
3. **Dynamic EQ** — Frequency-specific dynamic control for problem areas
4. **Compression** — Overall dynamic range management
5. **Tonal EQ** — Musical enhancement and character shaping
6. **Stereo Imaging** — Width and spatial adjustments
7. **Saturation/Harmonic Enhancement** — Analog warmth and character
8. **Multiband Compression** — Frequency-specific dynamic control
9. **Limiting** — Final loudness maximization
10. **Metering** — Continuous monitoring of levels and loudness
11. **Dithering** — Bit depth reduction with noise shaping

### Signal Path Considerations

**Headroom Management** — Maintain 3-6 dB of headroom throughout the chain to prevent clipping

**Gain Staging** — Ensure each processor receives optimal input level for its algorithm

**Parallel Processing** — Use parallel compression and saturation for transparent enhancement

**Mid-Side Processing** — Separate processing for center (mid) and sides for enhanced control

## Equalization Theory and Practice

### Types of EQ Curves

**Bell/Parametric** — Adjustable center frequency, gain, and Q (bandwidth) for surgical or broad adjustments

**Shelf** — Boosts or cuts all frequencies above (high shelf) or below (low shelf) a specified frequency

**High-Pass/Low-Pass Filters** — Removes frequencies below or above cutoff point with adjustable slope

**Notch Filter** — Extremely narrow bandwidth for removing specific problem frequencies

### EQ Strategies for Mastering

**Corrective EQ Approach:**
- Identify resonances and problem frequencies through sweeping
- Use narrow Q to notch out harsh or muddy frequencies
- Apply high-pass filter to remove sub-bass rumble (typically 20-30 Hz)
- Address sibilance with narrow cuts around 6-8 kHz if needed

**Tonal Shaping Approach:**
- Use broad Q values for musical enhancement
- Add "air" with gentle high-frequency shelf boost (10-16 kHz, +0.5 to +2 dB)
- Enhance warmth with low-frequency shelf boost (80-150 Hz, +0.5 to +1.5 dB)
- Boost presence for clarity (2-5 kHz, +0.5 to +2 dB)

### Frequency Range Characteristics

**Sub-Bass (20-60 Hz)** — Physical impact and power; often rolled off to prevent system overload

**Bass (60-250 Hz)** — Fundamental warmth and body; critical for genre-appropriate weight

**Low Mids (250-500 Hz)** — Potential muddiness zone; often requires subtle reduction

**Mids (500 Hz-2 kHz)** — Core of most instruments; careful balancing required

**Upper Mids (2-5 kHz)** — Presence and clarity; enhances intelligibility

**Highs (5-10 kHz)** — Brightness and definition; controls sibilance

**Air (10-20 kHz)** — Spaciousness and openness; adds polish and sheen

## Compression Fundamentals

### Compression Parameters

**Threshold** — Level at which compression begins; typically set to catch peaks while allowing dynamics

**Ratio** — Amount of gain reduction applied; mastering typically uses gentle ratios (1.5:1 to 3:1)

**Attack Time** — How quickly compressor responds; slower attacks preserve transients

**Release Time** — How quickly compression stops; should match musical rhythm

**Knee** — Transition smoothness into compression; soft knee for transparent mastering

**Makeup Gain** — Compensates for gain reduction to maintain perceived loudness

### Compression Techniques

**Glue Compression:**
- Very gentle ratio (1.5:1 to 2:1)
- Slow attack (30-50 ms) to preserve transients
- Medium release (auto or 100-300 ms)
- 1-3 dB of gain reduction maximum
- Purpose: Unify mix elements and add cohesion

**Peak Control:**
- Moderate ratio (3:1 to 4:1)
- Fast attack (5-15 ms)
- Fast to medium release (50-150 ms)
- 2-4 dB of gain reduction on peaks
- Purpose: Control excessive transients without squashing dynamics

**Parallel Compression:**
- Heavy compression on duplicate signal
- Blend compressed signal with dry signal
- Maintains dynamics while adding density
- Particularly effective for adding punch without losing transients

### Multiband Compression

**Frequency-Specific Control:**
- Divide spectrum into 3-4 bands (low, low-mid, high-mid, high)
- Apply different compression settings to each band
- Typical crossover points: 120 Hz, 1 kHz, 8 kHz

**Common Applications:**
- Tighten bass without affecting mids and highs
- Control vocal sibilance in high band
- Add punch to kick and bass in low band
- Manage harshness in upper midrange

**Caution:** Multiband compression can introduce phase issues; use sparingly and with linear-phase options when available

## Limiting and Loudness Maximization

### Limiter Fundamentals

**Limiting vs. Compression** — Limiters are extreme compressors (typically ∞:1 ratio) that prevent signal from exceeding threshold

**True Peak vs. Sample Peak** — True peak limiting accounts for inter-sample peaks that occur during D/A conversion

**Lookahead** — Allows limiter to anticipate peaks and apply gain reduction smoothly

### Limiting Strategies

**Conservative Approach (Streaming):**
- Set ceiling to -1.0 dB True Peak
- Target -14 LUFS integrated loudness
- Minimize gain reduction (3-5 dB maximum)
- Use longer release times for transparency

**Competitive Approach (Club/Radio):**
- Set ceiling to -0.3 dB True Peak
- Target -8 to -10 LUFS integrated loudness
- Accept more gain reduction (6-10 dB)
- Use adaptive release for musical response

**Audiophile Approach (High-Res):**
- Set ceiling to -2.0 dB True Peak
- Target -16 to -18 LUFS integrated loudness
- Minimal limiting (1-2 dB gain reduction)
- Preserve maximum dynamic range

### Loudness Standards

**Spotify** — -14 LUFS integrated, -2 dB True Peak maximum

**Apple Music** — -16 LUFS integrated, -1 dB True Peak maximum

**YouTube** — -14 LUFS integrated, -1 dB True Peak maximum

**Tidal** — -14 LUFS integrated, -1 dB True Peak maximum

**CD** — No specific standard; typically -9 to -12 LUFS integrated

**Vinyl** — Dynamic range critical; typically -16 to -20 LUFS integrated

## Dithering and Bit Depth Conversion

### Dithering Principles

**Purpose** — Adds low-level noise to mask quantization distortion when reducing bit depth

**When to Apply** — Only at final export stage when converting from higher to lower bit depth (e.g., 24-bit to 16-bit)

**Noise Shaping** — Moves dither noise to less audible frequency ranges (typically above 10 kHz)

### Dithering Types

**TPDF (Triangular Probability Density Function)** — Most common; flat noise floor; no noise shaping

**POW-r (Psychoacoustically Optimized Wordlength Reduction)** — Advanced noise shaping for minimal audible artifacts

**UV22/UV22HR** — Apogee's proprietary dithering with aggressive noise shaping

**IDR (Increased Digital Resolution)** — Waves' dithering algorithm with multiple noise shaping curves

### Best Practices

- Apply dithering only once at final export
- Never dither when staying at same bit depth
- Use noise shaping for 16-bit CD masters
- Disable dithering for high-resolution formats (24-bit)
- Listen to dither noise in isolation to verify appropriate level

## Metering and Analysis

### Essential Metering Tools

**Peak Meters** — Show instantaneous signal peaks; ensure no clipping (0 dBFS)

**RMS Meters** — Display average loudness over time; useful for general level monitoring

**LUFS Meters** — Measure perceived loudness according to ITU-R BS.1770 standard

**True Peak Meters** — Account for inter-sample peaks during D/A conversion

**Phase Correlation Meters** — Show stereo phase relationship (+1 = mono, 0 = wide stereo, -1 = out of phase)

**Spectrum Analyzers** — Display frequency content visually for identifying imbalances

**Stereo Imaging Meters** — Visualize stereo width and balance

### Metering Best Practices

**Integrated LUFS** — Primary loudness measurement for entire track

**Short-Term LUFS** — 3-second window for monitoring loudness changes

**Momentary LUFS** — 400ms window for real-time loudness monitoring

**Loudness Range (LRA)** — Measures dynamic variation; higher values indicate more dynamics

**Reference Levels:**
- Streaming: -14 LUFS integrated, LRA 6-12
- CD: -9 to -12 LUFS integrated, LRA 4-8
- Vinyl: -16 to -20 LUFS integrated, LRA 8-15
- Film/TV: -23 LUFS integrated (dialogue), LRA varies

## Stereo Enhancement Techniques

### Mid-Side Processing

**Mid Channel** — Center information (mono content)

**Side Channel** — Stereo difference information (width)

**Applications:**
- Widen sides with subtle boost (1-2 dB)
- Narrow low frequencies by reducing side content below 150 Hz
- Enhance vocal clarity by boosting mid channel in presence range
- Add spaciousness by enhancing side channel in high frequencies

### Stereo Widening Techniques

**Haas Effect** — Delay one channel by 10-30ms to create width (use cautiously to avoid phase issues)

**Stereo Imaging Plugins** — Adjust width parameter subtly (105-115% maximum)

**Panning Adjustments** — Ensure balanced stereo field without excessive hard panning

**Mono Compatibility** — Always check mix in mono to ensure no phase cancellation

### Phase Considerations

**Phase Correlation Monitoring** — Maintain average correlation above +0.5 for mono compatibility

**Low-End Management** — Keep bass frequencies (below 150 Hz) centered to prevent phase issues

**Stereo Width Limits** — Avoid excessive widening that causes phase problems on mono playback systems
