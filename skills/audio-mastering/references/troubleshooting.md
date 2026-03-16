# Audio Mastering Troubleshooting

Common problems and solutions for mastering engineers.

## Frequency Balance Issues

### Problem: Muddy or Unclear Low-End

**Symptoms:**
- Bass frequencies sound boomy or undefined
- Kick drum and bass guitar compete for space
- Overall mix lacks clarity and punch

**Diagnosis:**
- Excessive energy in 200-400 Hz range
- Overlapping bass and kick drum fundamentals
- Phase issues in low frequencies

**Solutions:**
1. Apply gentle high-pass filter at 20-30 Hz to remove sub-bass rumble
2. Use narrow EQ cut (Q=2-3) to reduce muddiness around 250-350 Hz (-1 to -3 dB)
3. Apply mid-side processing: reduce side channel below 150 Hz to center bass
4. Use multiband compression on low band (20-120 Hz) with moderate ratio (3:1)
5. Check phase correlation in low frequencies; ensure above +0.7

### Problem: Harsh or Fatiguing High Frequencies

**Symptoms:**
- Listening causes ear fatigue quickly
- Cymbals and hi-hats sound brittle or piercing
- Sibilance is excessive and distracting

**Diagnosis:**
- Excessive energy in 2-5 kHz (presence) or 6-10 kHz (sibilance)
- Resonant peaks from mixing stage
- Over-brightening with high-frequency shelf

**Solutions:**
1. Identify harsh frequencies by sweeping with narrow boost, then cut (-1 to -3 dB)
2. Apply gentle high-frequency shelf reduction above 10 kHz (-0.5 to -1.5 dB)
3. Use de-esser targeting 6-8 kHz with threshold set to catch only excessive sibilance
4. Apply tube or tape saturation for smoother high-frequency harmonics
5. Use multiband compression on high band (5-20 kHz) with gentle ratio (2:1)

### Problem: Thin or Weak Sound

**Symptoms:**
- Mix lacks body and weight
- Bass and low-mids are insufficient
- Overall sound feels small or distant

**Diagnosis:**
- Insufficient low-frequency content
- Over-filtering during mixing
- Excessive high-frequency emphasis

**Solutions:**
1. Apply low-frequency shelf boost at 80-150 Hz (+0.5 to +2 dB)
2. Enhance low-mids with broad boost at 200-400 Hz (+0.5 to +1.5 dB)
3. Use harmonic enhancement on low frequencies for added warmth
4. Apply parallel compression with emphasis on low-end
5. Reduce excessive high-frequency content if present

### Problem: Boxy or Nasal Midrange

**Symptoms:**
- Vocals and instruments sound congested
- Mix has "telephone" quality
- Lack of clarity and separation

**Diagnosis:**
- Excessive energy in 400-800 Hz range
- Resonant frequencies from room acoustics
- Insufficient high-frequency content

**Solutions:**
1. Sweep with narrow boost to identify boxy frequencies, then cut (-2 to -4 dB)
2. Apply broad cut around 500-600 Hz (Q=0.7-1.0, -1 to -2 dB)
3. Enhance presence range (2-5 kHz) with gentle boost (+0.5 to +1.5 dB)
4. Use dynamic EQ to reduce boxiness only when excessive
5. Apply mid-side processing: boost mid channel in presence range for clarity

## Dynamic Range Issues

### Problem: Over-Compression (Squashed Dynamics)

**Symptoms:**
- Mix sounds lifeless and flat
- No dynamic variation between sections
- Pumping or breathing artifacts audible

**Diagnosis:**
- Excessive compression during mixing or mastering
- Improper attack/release settings
- Too much limiting for loudness

**Solutions:**
1. Reduce compression ratio (use 1.5:1 to 2:1 maximum for mastering)
2. Increase attack time to preserve transients (30-50 ms)
3. Adjust release time to match musical rhythm (auto or 100-300 ms)
4. Limit gain reduction to 1-3 dB maximum
5. Use parallel compression instead of serial for more natural dynamics
6. Reduce limiting amount; prioritize dynamics over loudness

### Problem: Excessive Transients

**Symptoms:**
- Peaks trigger limiting excessively
- Cannot achieve desired loudness without distortion
- Snare or kick drum too prominent

**Diagnosis:**
- Uncontrolled transients from mixing stage
- Insufficient compression before limiting
- Improper limiter settings

**Solutions:**
1. Apply fast-attack compressor (5-15 ms) with moderate ratio (3:1 to 4:1)
2. Use transient shaper to reduce attack of drums
3. Apply soft clipper before limiter (0.5-1 dB clipping)
4. Use multiband compression to control specific frequency ranges
5. Implement two-stage limiting for more transparent control

### Problem: Pumping or Breathing Artifacts

**Symptoms:**
- Audible gain reduction following peaks
- Background noise or reverb swells after transients
- Unnatural dynamic movement

**Diagnosis:**
- Release time too fast for musical content
- Excessive compression or limiting
- Improper threshold settings

**Solutions:**
1. Increase release time to match musical rhythm (200-500 ms)
2. Use auto-release feature for adaptive response
3. Reduce compression ratio for gentler gain reduction
4. Raise threshold to reduce amount of compression
5. Use multiband compression to isolate problematic frequency ranges
6. Apply parallel compression for more natural dynamics

## Stereo Image Issues

### Problem: Narrow or Mono-Sounding Mix

**Symptoms:**
- Mix sounds centered and lacks width
- Instruments don't have spatial separation
- Overall sound feels small

**Diagnosis:**
- Insufficient stereo information in mix
- Excessive mono processing
- Phase cancellation reducing width

**Solutions:**
1. Apply subtle stereo widening (105-115% width maximum)
2. Use mid-side processing: boost side channel in high frequencies (+1 to +2 dB)
3. Apply stereo reverb to side channel only
4. Check for phase issues causing width reduction
5. Enhance stereo information with Haas effect (10-20 ms delay, use cautiously)

### Problem: Phase Issues and Mono Incompatibility

**Symptoms:**
- Mix sounds hollow or thin in mono
- Certain elements disappear when summed to mono
- Phase correlation meter shows negative values

**Diagnosis:**
- Out-of-phase stereo information
- Excessive stereo widening
- Improper mid-side processing

**Solutions:**
1. Check phase correlation meter; maintain average above +0.5
2. Reduce stereo width to improve mono compatibility
3. Apply mid-side processing: reduce side channel level (-1 to -2 dB)
4. Center low frequencies by reducing side channel below 150 Hz
5. Use phase correlation plugin to identify and fix phase issues
6. Test mix in mono throughout mastering process

### Problem: Excessive Width Causing Instability

**Symptoms:**
- Mix sounds unstable or disorienting
- Bass frequencies lack focus and power
- Phase correlation shows low or negative values

**Diagnosis:**
- Over-widening with stereo enhancement plugins
- Stereo bass frequencies causing phase issues
- Excessive side channel energy

**Solutions:**
1. Reduce stereo width to more natural level (100-110%)
2. Apply mid-side processing: center bass by reducing side below 150 Hz
3. Use mono-maker plugin on low frequencies
4. Reduce side channel level overall (-1 to -2 dB)
5. Check phase correlation and maintain above +0.5

## Loudness and Limiting Issues

### Problem: Cannot Achieve Target Loudness

**Symptoms:**
- Limiter distorts before reaching target LUFS
- Excessive gain reduction causes pumping
- Mix sounds over-processed when loud enough

**Diagnosis:**
- Insufficient dynamic control before limiting
- Excessive peaks preventing loudness increase
- Improper gain staging

**Solutions:**
1. Apply compression before limiting to control dynamics
2. Use soft clipper to tame transients (0.5-1 dB clipping)
3. Implement two-stage limiting for more transparent loudness
4. Use multiband compression to control specific frequency ranges
5. Check for excessive low-frequency energy triggering limiter
6. Consider if target loudness is appropriate for genre and format

### Problem: Distortion from Limiting

**Symptoms:**
- Audible distortion on peaks
- Harsh, brittle sound quality
- Inter-sample peaks causing clipping

**Diagnosis:**
- Excessive limiting gain reduction
- Improper limiter settings (attack too fast)
- True Peak exceeding 0 dBFS

**Solutions:**
1. Reduce limiting amount; accept lower loudness
2. Increase limiter attack time for smoother response
3. Enable True Peak limiting and set ceiling to -1 dB
4. Use oversampling in limiter to prevent inter-sample peaks
5. Apply soft clipping before limiter to reduce workload
6. Use multi-stage limiting for more transparent results

### Problem: Loudness Inconsistency Across Album

**Symptoms:**
- Tracks vary significantly in perceived volume
- Listener must adjust volume between tracks
- Album lacks cohesion

**Diagnosis:**
- Inconsistent integrated LUFS across tracks
- Different dynamic ranges between songs
- Improper loudness matching

**Solutions:**
1. Measure integrated LUFS for all tracks
2. Match LUFS within ±0.5 LU across album
3. Consider artistic intent for dynamic variation
4. Use loudness matching plugin for consistency
5. Reference all tracks together to verify cohesion

## Technical Issues

### Problem: Clipping or Digital Distortion

**Symptoms:**
- Audible distortion on peaks
- Waveform shows flat-topped peaks
- Harsh, unpleasant sound quality

**Diagnosis:**
- Sample peaks exceeding 0 dBFS
- Clipping in plugin chain
- Insufficient headroom

**Solutions:**
1. Reduce input gain to provide headroom (-3 to -6 dB)
2. Check each plugin in chain for clipping
3. Use True Peak metering to identify inter-sample peaks
4. Apply limiting with ceiling set to -1 dB True Peak
5. Enable oversampling in plugins to prevent aliasing

### Problem: Noise or Hum in Master

**Symptoms:**
- Audible hiss, hum, or buzz in quiet sections
- Noise floor higher than acceptable
- Electrical interference audible

**Diagnosis:**
- Noise from mixing stage
- Ground loop hum (50/60 Hz)
- Plugin noise or dither applied incorrectly

**Solutions:**
1. Use spectral editor to identify and remove noise
2. Apply de-hummer to remove 50/60 Hz hum and harmonics
3. Use noise reduction plugin with gentle settings
4. Check for noisy plugins in chain and replace
5. Ensure dithering only applied at final export
6. Request cleaner mix from client if noise excessive

### Problem: Clicks, Pops, or Digital Artifacts

**Symptoms:**
- Audible clicks or pops during playback
- Digital glitches or dropouts
- Artifacts at edit points

**Diagnosis:**
- Edit points without crossfades
- Clipping causing clicks
- Plugin processing artifacts

**Solutions:**
1. Use spectral editor to identify and remove clicks
2. Apply de-clicker plugin with appropriate settings
3. Add short crossfades at edit points (5-10 ms)
4. Check for clipping in plugin chain
5. Reduce plugin processing if causing artifacts
6. Increase buffer size to prevent dropouts

## Format-Specific Issues

### Problem: Streaming Platform Loudness Reduction

**Symptoms:**
- Track sounds quieter than expected on streaming services
- Excessive loudness normalization applied
- Loss of impact compared to other tracks

**Diagnosis:**
- Master exceeds platform loudness target
- Excessive limiting causing normalization
- Improper loudness target for platform

**Solutions:**
1. Target platform-specific loudness (Spotify: -14 LUFS, Apple: -16 LUFS)
2. Prioritize dynamic range over maximum loudness
3. Test with platform normalization enabled
4. Reduce limiting to maintain dynamics
5. Consider creating platform-specific masters

### Problem: Vinyl Mastering Issues

**Symptoms:**
- Excessive sibilance causes distortion
- Bass causes groove jumping or skipping
- Stereo width causes cutting problems

**Diagnosis:**
- Uncontrolled high frequencies
- Excessive or out-of-phase bass
- Improper stereo bass management

**Solutions:**
1. Apply de-esser to control sibilance (6-8 kHz)
2. Center bass frequencies below 150 Hz (mono)
3. Reduce excessive low-end energy
4. Limit side length to 12-15 minutes for optimal quality
5. Consult with cutting engineer for specific requirements
6. Request test pressing before approval

### Problem: Codec Artifacts in Lossy Formats

**Symptoms:**
- MP3 or AAC version sounds worse than WAV
- Audible artifacts in high frequencies
- Loss of stereo width or depth

**Diagnosis:**
- Excessive high-frequency content
- Extreme stereo width
- Bitrate too low for content

**Solutions:**
1. Test master with target codec (MP3, AAC) before delivery
2. Reduce excessive high-frequency content above 16 kHz
3. Moderate stereo width for better codec compatibility
4. Recommend higher bitrate for encoding (320 kbps MP3, 256 kbps AAC)
5. Avoid extreme processing that doesn't encode well
