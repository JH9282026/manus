# Spectral Editing Guide

This reference provides comprehensive coverage of spectral editing techniques, tools, and workflows for precise audio manipulation and restoration.

## Understanding Spectral Representation

### What is a Spectrogram?

A spectrogram is a visual representation of audio that displays three dimensions of information:

**Axes and Display**:
- **X-axis (Horizontal)**: Time (left to right)
- **Y-axis (Vertical)**: Frequency (low to high)
- **Color/Brightness**: Amplitude (loudness) at each time-frequency point

**Reading Spectrograms**:
- **Bright/Hot colors** (white, yellow, red): Loud frequencies
- **Dark/Cool colors** (blue, black): Quiet frequencies
- **Horizontal lines**: Sustained tones (hum, whistles, resonances)
- **Vertical lines**: Transients (drums, clicks, pops)
- **Diagonal lines**: Pitch changes (sirens, glissandos)
- **Fuzzy areas**: Noise, complex sounds
- **Patterns**: Speech (formants), music (harmonics)

### Spectrogram vs. Waveform

**Waveform View**:
- Shows amplitude over time
- Good for: Editing timing, seeing overall levels, identifying clipping
- Limited for: Identifying specific frequencies, subtle noise

**Spectrogram View**:
- Shows frequency content over time
- Good for: Identifying noise, targeting specific frequencies, detailed editing
- Limited for: Seeing overall timing, quick edits

**When to Use Each**:
- Waveform: Rough editing, timing adjustments, level checks
- Spectrogram: Noise identification, frequency-specific editing, detailed restoration

### Spectrogram Settings

**FFT Size (Frequency Resolution)**
- Determines how many frequency bands are analyzed
- Common values: 1024, 2048, 4096, 8192, 16384
- **Larger FFT**: More frequency detail, less time detail
- **Smaller FFT**: More time detail, less frequency detail
- **Typical use**: 4096 for general work, 8192 for detailed frequency work

**Window Size (Time Resolution)**
- Affects temporal accuracy
- Trade-off with frequency resolution
- **Larger window**: Better frequency resolution, worse time resolution
- **Smaller window**: Better time resolution, worse frequency resolution

**Window Type**
- Mathematical function applied to analysis
- Common types: Hann, Hamming, Blackman
- **Hann**: Good general purpose
- **Blackman**: Better frequency resolution, less spectral leakage
- Affects how frequencies are represented

**Overlap**
- How much adjacent analysis windows overlap
- Typical: 50-75%
- Higher overlap: Smoother display, more processing
- Lower overlap: Faster, less smooth

**Color Scale**
- **Linear**: Equal color steps for equal amplitude steps
- **Logarithmic (dB)**: More perceptually accurate, shows quiet details
- **Range**: Adjusts dynamic range displayed
- **Palette**: Color scheme (rainbow, grayscale, heat map)

**Frequency Scale**
- **Linear**: Equal spacing for equal Hz
- **Logarithmic**: Equal spacing for equal musical intervals
- **Mel**: Perceptually-based scale
- Choose based on material and task

## Spectral Selection Tools

### Rectangular Selection

**Description**: Select a rectangular time-frequency region

**How to Use**:
- Click and drag to define rectangle
- Horizontal extent: Time range
- Vertical extent: Frequency range

**Best For**:
- Sustained tones (hum, resonances)
- Noise in specific frequency band
- Removing constant-frequency sounds
- Quick, simple selections

**Example Uses**:
- Selecting 60 Hz hum and harmonics
- Removing air conditioning noise in specific frequency range
- Isolating problematic resonance

### Lasso/Freehand Selection

**Description**: Draw custom shape around target frequencies

**How to Use**:
- Click and drag to draw outline
- Follow contours of sound
- Close shape to complete selection

**Best For**:
- Irregular noise patterns
- Sounds that change frequency over time
- Precise targeting of complex shapes
- Following pitch contours

**Example Uses**:
- Selecting siren that changes pitch
- Removing dog bark with complex harmonics
- Targeting speech formants
- Isolating specific musical notes

### Magic Wand/Threshold Selection

**Description**: Automatically selects similar frequencies based on amplitude threshold

**How to Use**:
- Click on target frequency
- Tool selects all similar amplitudes
- Adjust threshold to expand/contract selection
- Can select contiguous or all similar regions

**Parameters**:
- **Threshold**: How similar amplitudes must be
- **Tolerance**: Range of acceptable values
- **Contiguous**: Only connected regions vs. all similar

**Best For**:
- Selecting consistent noise
- Quick selection of similar elements
- Isolating specific sounds from background

**Example Uses**:
- Selecting all instances of hum
- Isolating consistent background noise
- Selecting specific harmonic series

### Harmonic Selection

**Description**: Automatically selects fundamental frequency and its harmonics

**How to Use**:
- Click on fundamental frequency
- Tool calculates and selects harmonics
- Adjust number of harmonics included
- Refine selection as needed

**Parameters**:
- **Fundamental**: Base frequency
- **Number of harmonics**: How many to include
- **Tolerance**: How precisely to match calculated frequencies

**Best For**:
- Tonal noise (hum, whistles)
- Musical notes
- Harmonic distortion
- Pitched sounds

**Example Uses**:
- Removing electrical hum and all harmonics
- Isolating specific musical note
- Reducing harmonic distortion

### Brush Selection

**Description**: Paint over areas to select, like a paintbrush

**How to Use**:
- Choose brush size
- Click and drag to paint selection
- Paint over all target areas
- Erase to deselect

**Parameters**:
- **Brush size**: Diameter of brush
- **Hardness**: Edge softness
- **Opacity**: Selection strength

**Best For**:
- Complex, irregular selections
- Building selection gradually
- Detailed, artistic control
- Multiple disconnected regions

**Example Uses**:
- Selecting scattered noise artifacts
- Building complex selection over time
- Detailed restoration work

### Time-Frequency Selection

**Description**: Select based on both time and frequency criteria

**How to Use**:
- Define time range
- Define frequency range
- Combine with other selection methods
- Refine with boolean operations

**Boolean Operations**:
- **Add**: Expand selection
- **Subtract**: Remove from selection
- **Intersect**: Keep only overlap
- **Invert**: Select everything except current selection

**Best For**:
- Complex selections
- Combining multiple criteria
- Precise targeting

## Spectral Editing Operations

### Attenuation (Reduction)

**Description**: Reduce amplitude of selected frequencies without complete removal

**How to Use**:
- Select target frequencies
- Choose attenuation amount (dB)
- Apply reduction
- Preview and adjust

**Parameters**:
- **Amount**: How much to reduce (typically -6 to -40 dB)
- **Curve**: Linear, logarithmic, or custom
- **Edge blending**: Smooths transitions

**Advantages**:
- More natural than complete removal
- Preserves some original character
- Reduces artifacts
- Reversible (in non-destructive workflow)

**Best For**:
- Reducing noise while maintaining ambience
- Subtle corrections
- Preserving natural sound

**Example Uses**:
- Reducing hum by -20 dB
- Lowering resonance without removing
- Subtle noise reduction

### Deletion (Removal)

**Description**: Complete removal of selected frequencies

**How to Use**:
- Select target frequencies
- Delete or set to silence
- Creates "hole" in spectrum

**Advantages**:
- Complete removal of unwanted sound
- Simple and direct
- Effective for isolated noise

**Disadvantages**:
- Can create audible "holes"
- May sound unnatural
- Difficult to reverse
- Can introduce artifacts

**Best For**:
- Isolated, problematic frequencies
- Noise with no overlap with signal
- When complete removal is necessary

**Use Sparingly**: Attenuation usually preferable

### Interpolation

**Description**: Fills selected region with synthesized audio based on surrounding frequencies

**How to Use**:
- Select target region
- Choose interpolation method
- Apply
- Blends with surrounding audio

**Methods**:
- **Linear**: Simple blending of edges
- **Cubic**: Smoother, more complex blending
- **Spectral**: Uses surrounding spectral content
- **Harmonic**: Maintains harmonic relationships

**Advantages**:
- Smoother than deletion
- Reduces artifacts
- More natural sound
- Fills gaps seamlessly

**Best For**:
- Small to medium selections
- Removing isolated sounds
- Smoothing transitions
- Filling gaps

**Example Uses**:
- Removing small clicks or pops
- Smoothing after deletion
- Filling dropouts

### Spectral Repair

**Description**: Advanced reconstruction of damaged or missing audio using surrounding spectral information

**How to Use**:
- Select damaged region
- Choose repair algorithm
- Adjust parameters
- Apply and evaluate

**Algorithms**:

**1. Replace**
- Synthesizes new audio from surrounding content
- Analyzes patterns in adjacent audio
- Generates replacement that matches context
- Best for: Dropouts, missing audio

**2. Interpolate**
- Blends edges of selection smoothly
- Creates transition between boundaries
- Best for: Small gaps, smoothing

**3. Pattern**
- Uses repeating patterns to fill gaps
- Identifies periodic content
- Extends patterns into selection
- Best for: Rhythmic or repetitive material

**4. Attenuate**
- Reduces rather than removes
- Preserves some original content
- Best for: Noise reduction, subtle fixes

**Parameters**:
- **Algorithm**: Which repair method
- **Sensitivity**: How closely to match surroundings
- **Blend**: How much to blend with original
- **Direction**: Which surrounding audio to use (before, after, both)

**Best For**:
- Repairing dropouts
- Removing artifacts
- Fixing damaged audio
- Reconstructing missing sections

### Gain/Amplification

**Description**: Increase amplitude of selected frequencies

**How to Use**:
- Select target frequencies
- Choose gain amount (dB)
- Apply amplification

**Use Cases**:
- Enhancing specific frequencies
- Boosting quiet elements
- Creative sound design
- Correcting frequency imbalances

**Caution**:
- Can introduce distortion
- May amplify noise
- Use moderately
- Monitor for clipping

### Copy and Paste

**Description**: Copy spectral content from one location to another

**How to Use**:
- Select source region
- Copy
- Select destination (time and frequency)
- Paste

**Modes**:
- **Replace**: Overwrites destination
- **Mix**: Blends with destination
- **Add**: Adds to destination

**Use Cases**:
- Repairing dropouts with similar audio
- Duplicating sounds
- Creative editing
- Reconstructing damaged sections

## Advanced Spectral Techniques

### Spectral Layers

**Concept**: Separate audio into multiple spectral layers for independent editing

**Process**:
1. Analyze audio
2. Separate into layers (e.g., vocals, drums, bass, other)
3. Edit each layer independently
4. Recombine layers

**Advantages**:
- Non-destructive workflow
- Independent control
- Complex editing possible
- Easy to compare versions

**Tools**: Steinberg SpectraLayers, iZotope RX (Music Rebalance)

**Applications**:
- Isolating dialogue from background
- Removing specific instruments
- Remixing
- Advanced restoration

### Spectral Molding

**Concept**: Shape frequency content to match a target spectral profile

**Process**:
1. Capture target spectrum (reference)
2. Apply to source audio
3. Source spectrum morphs toward target
4. Adjust amount and parameters

**Use Cases**:
- Matching ambience across shots
- Correcting tonal imbalances
- Creative sound design
- Restoration to reference standard

### Spectral Casting

**Concept**: Use one audio's spectral characteristics to process another

**Process**:
1. Analyze "cast" audio (template)
2. Apply its characteristics to target
3. Target takes on spectral qualities of cast

**Use Cases**:
- Matching room tone
- Creative effects
- Consistent ambience

### Frequency Smoothing

**Concept**: Reduce harsh frequency peaks and irregularities

**Process**:
- Analyzes frequency response
- Smooths peaks and dips
- Adjustable amount
- Preserves overall character

**Use Cases**:
- Reducing harshness
- Smoothing resonances
- Improving tonal balance
- Subtle enhancement

### Spectral Denoising

**Concept**: Noise reduction applied in spectral domain

**Advantages over time-domain**:
- More precise frequency targeting
- Visual feedback
- Better preservation of signal
- Handles complex noise better

**Process**:
- Identify noise in spectrogram
- Select noise regions
- Apply reduction
- Preserve signal regions

## Workflow and Best Practices

### Spectral Editing Workflow

**Step 1: Assessment**
- View audio in spectrogram
- Identify problems visually
- Note time and frequency locations
- Plan editing approach

**Step 2: Optimize Display**
- Adjust FFT size for task
- Set appropriate color scale
- Zoom to problem areas
- Configure for best visibility

**Step 3: Selection**
- Choose appropriate selection tool
- Select target frequencies precisely
- Refine selection boundaries
- Use boolean operations if needed

**Step 4: Processing**
- Choose appropriate operation
- Start with conservative settings
- Preview before applying
- Adjust parameters as needed

**Step 5: Evaluation**
- Listen critically
- Check for artifacts
- View result in spectrogram
- Compare to original

**Step 6: Refinement**
- Adjust if needed
- Additional passes if necessary
- Fine-tune boundaries
- Final quality check

### Selection Best Practices

**Precision**:
- Zoom in for detailed work
- Use appropriate selection tool for task
- Refine boundaries carefully
- Avoid selecting more than necessary

**Edge Handling**:
- Feather selection edges
- Blend transitions
- Avoid hard boundaries
- Smooth time and frequency transitions

**Verification**:
- Solo selection (hear only selected)
- Invert selection (hear everything else)
- Visual confirmation in spectrogram
- Check boundaries carefully

### Processing Best Practices

**Conservative Approach**:
- Start with light settings
- Multiple passes better than one aggressive pass
- Preserve some original character
- Avoid over-processing

**Artifact Prevention**:
- Use attenuation instead of deletion when possible
- Blend edges smoothly
- Avoid creating spectral "holes"
- Monitor for artifacts continuously

**Context Awareness**:
- Consider surrounding audio
- Maintain natural ambience
- Preserve important frequencies
- Think about final use case

### Common Spectral Editing Tasks

**Removing Specific Sounds**

**Example: Dog Bark**
1. Locate bark in spectrogram (vertical burst)
2. Use lasso to select bark's spectral signature
3. Apply spectral repair (replace or attenuate)
4. Blend edges
5. Verify removal

**Example: Phone Ring**
1. Identify ring (horizontal lines at specific frequencies)
2. Select time range and frequency range
3. Use spectral repair or attenuation
4. Check for harmonics
5. Smooth transitions

**Reducing Resonances**

**Process**:
1. Identify resonance (bright horizontal line)
2. Select frequency range (narrow band)
3. Attenuate (typically -6 to -12 dB)
4. Check across entire timeline
5. Verify natural sound

**Removing Hum and Harmonics**

**Process**:
1. Identify fundamental (50 or 60 Hz)
2. Locate harmonics (multiples of fundamental)
3. Use harmonic selection tool
4. Attenuate or remove
5. Check entire spectrum

**Repairing Dropouts**

**Process**:
1. Locate dropout (gap in spectrogram)
2. Select gap region
3. Use spectral repair (replace algorithm)
4. Blend with surrounding audio
5. Verify seamless repair

**Cleaning Up Dialogue**

**Process**:
1. Identify background noise in pauses
2. Select noise regions between words
3. Attenuate or remove
4. Preserve voice frequencies
5. Maintain natural ambience

## Spectral Editing for Different Content

### Dialogue/Speech

**Characteristics**:
- Formants (resonances) in 300-3000 Hz
- Fundamentals typically 80-250 Hz
- Sibilance in 4-8 kHz
- Breath sounds below 500 Hz

**Common Tasks**:
- Remove background noise between words
- Reduce room resonances
- Remove mouth clicks
- Clean up breath sounds
- Remove plosives

**Best Practices**:
- Preserve formants (voice character)
- Be careful with sibilance (4-8 kHz)
- Maintain natural breath
- Don't over-process

### Music

**Characteristics**:
- Wide frequency range
- Complex harmonic content
- Rhythmic elements
- Overlapping instruments

**Common Tasks**:
- Remove clicks and pops
- Reduce tape hiss
- Remove specific instruments (stem separation)
- Fix damaged sections
- Reduce resonances

**Best Practices**:
- Preserve musical transients
- Maintain harmonic relationships
- Be careful with rhythm section
- Avoid dulling high frequencies

### Field Recordings

**Characteristics**:
- Variable background noise
- Wind, traffic, nature sounds
- Unpredictable elements
- Wide dynamic range

**Common Tasks**:
- Remove wind noise
- Reduce traffic sounds
- Remove specific events (sirens, horns)
- Clean up handling noise

**Best Practices**:
- Preserve natural ambience
- Remove only problematic elements
- Maintain environmental context
- Balance cleanup with authenticity

### Archival Material

**Characteristics**:
- Tape hiss, vinyl crackle
- Degraded media
- Historical value
- Limited source quality

**Common Tasks**:
- Remove surface noise
- Repair dropouts
- Reduce hiss and hum
- Fix damaged sections

**Best Practices**:
- Preserve historical character
- Don't over-restore
- Document all changes
- Maintain authenticity
- Create preservation and access versions

## Troubleshooting

### Problem: Artifacts After Processing

**Symptoms**: Metallic, underwater, or unnatural sound

**Solutions**:
- Reduce processing amount
- Use attenuation instead of deletion
- Increase edge blending
- Smooth selection boundaries
- Process in multiple light passes

### Problem: Selection Too Broad

**Symptoms**: Removing desired audio along with noise

**Solutions**:
- Refine selection boundaries
- Use more precise selection tool
- Zoom in for detailed work
- Use lasso instead of rectangle
- Process in smaller sections

### Problem: Spectral "Holes"

**Symptoms**: Obvious gaps in frequency spectrum

**Solutions**:
- Use attenuation instead of deletion
- Apply interpolation after deletion
- Reduce amount of removal
- Blend edges more
- Use spectral repair

### Problem: Inconsistent Results

**Symptoms**: Some sections sound good, others don't

**Solutions**:
- Process sections individually
- Adjust settings for each section
- Use adaptive tools
- Check for varying noise characteristics
- Refine selections

## Conclusion

Spectral editing is a powerful technique that provides surgical precision for audio restoration and manipulation. By visualizing audio in the time-frequency domain, you can target specific problems with minimal impact on desired content. Mastery requires understanding spectral representation, skillful use of selection tools, and judicious application of processing operations. With practice, spectral editing becomes an indispensable tool for solving complex audio problems that would be impossible to address in the time domain alone.