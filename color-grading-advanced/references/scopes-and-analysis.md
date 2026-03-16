# Professional Scopes and Analysis

Mastering video scopes for objective color correction and technical quality control.

---

## Waveform Monitor

### Understanding the Waveform

**Display Characteristics**
- Horizontal axis: Represents image from left to right
- Vertical axis: Luminance level (0-100 IRE or 0-1023 for 10-bit)
- Shows brightness distribution across frame
- Essential for exposure evaluation

**Reading the Waveform**
- **Top of waveform**: Brightest areas of image
- **Bottom of waveform**: Darkest areas of image
- **Density**: How much of image at that brightness level
- **Shape**: Overall tonal distribution

### Waveform Applications

**Exposure Correction**
- Identify clipped highlights (waveform touching top)
- Identify crushed blacks (waveform touching bottom)
- Evaluate overall exposure distribution
- Match exposure across shots

**Broadcast Safe Levels**
- Legal range: 0-100 IRE (broadcast)
- Data range: -7.5 to 109 IRE (full range)
- Ensure waveform stays within legal limits for broadcast
- Use Soft Clip or Legalizer for compliance

**Contrast Evaluation**
- Wide waveform spread: High contrast
- Narrow waveform spread: Low contrast
- Adjust to achieve desired contrast range

### Waveform Modes

**Luma (Y)**
- Shows luminance only
- Ignores color information
- Best for exposure and contrast evaluation

**RGB Overlay**
- Shows red, green, blue channels overlaid
- Identifies color casts (one channel higher/lower)
- Useful for white balance evaluation

**YCbCr Parade**
- Separate displays for Y (luma), Cb (blue-yellow), Cr (red-cyan)
- Technical color space representation
- Used in broadcast workflows

## RGB Parade

### Understanding RGB Parade

**Display Characteristics**
- Three separate waveforms: Red, Green, Blue
- Each shows that color channel's luminance
- Side-by-side comparison of channels
- Essential for color balance

**Reading the Parade**
- **Aligned channels**: Neutral/balanced color
- **One channel higher**: Color cast toward that color
- **One channel lower**: Color cast away from that color
- **Shape similarity**: Indicates color balance across tonal range

### RGB Parade Applications

**White Balance Correction**
1. Identify which channel(s) are misaligned
2. Adjust color temperature/tint to align channels
3. Focus on midtones and highlights for white balance
4. Verify alignment in parade

**Color Cast Removal**
- Green cast: Green channel higher than red/blue
- Magenta cast: Red and blue higher than green
- Correct using offset or color wheels

**Matching Shots**
1. Display reference shot parade
2. Display current shot parade
3. Adjust current shot to match parade shapes
4. Verify color consistency

### Parade Interpretation

**Neutral Gray Card**
- All three channels at same level
- Indicates perfect color balance
- Use as reference for correction

**Skin Tones**
- Red channel slightly higher than green
- Green slightly higher than blue
- Typical relationship: R > G > B
- Varies by skin tone and lighting

**Skies**
- Blue channel highest
- Green channel moderate
- Red channel lowest
- Relationship: B > G > R

## Vectorscope

### Understanding the Vectorscope

**Display Characteristics**
- Circular display with color targets
- Center: No saturation (grayscale)
- Outer edge: Maximum saturation
- Angle: Hue
- Distance from center: Saturation

**Color Targets**
- Red, Magenta, Blue, Cyan, Green, Yellow
- Positioned at standard color locations
- Used for color accuracy verification
- Skin tone line between yellow and red

### Vectorscope Applications

**Skin Tone Evaluation**
- Skin tones should fall on or near skin tone line
- Line runs from center toward orange/red
- Distance from center indicates saturation
- Verify all skin tones align on line

**Color Saturation Control**
- Dots near center: Desaturated
- Dots near edge: Highly saturated
- Adjust saturation to keep within appropriate range
- Avoid exceeding outer boundary (over-saturation)

**Hue Accuracy**
- Verify colors align with appropriate targets
- Identify color shifts or casts
- Correct hue to align with targets

**Broadcast Safe Colors**
- Ensure vectorscope stays within legal limits
- Outer boxes indicate broadcast safe boundaries
- Reduce saturation if exceeding limits

### Vectorscope Interpretation

**Neutral Image**
- Single dot in center
- Indicates no color (pure grayscale)
- Useful for verifying neutral balance

**Colorful Image**
- Dots spread across vectorscope
- Pattern indicates color palette
- Concentration shows dominant colors

**Color Cast**
- All dots shifted toward one direction
- Indicates overall color cast
- Correct by shifting opposite direction

## Histogram

### Understanding the Histogram

**Display Characteristics**
- Horizontal axis: Tonal range (shadows to highlights)
- Vertical axis: Number of pixels at that level
- Shows distribution of tonal values
- Quick exposure assessment

**Reading the Histogram**
- **Left side**: Shadows and blacks
- **Middle**: Midtones
- **Right side**: Highlights and whites
- **Height**: Quantity of pixels at that level

### Histogram Applications

**Exposure Evaluation**
- Histogram touching left edge: Crushed blacks
- Histogram touching right edge: Clipped highlights
- Centered histogram: Balanced exposure
- Histogram shape indicates tonal distribution

**Contrast Assessment**
- Wide histogram: High contrast
- Narrow histogram: Low contrast
- Gaps in histogram: Posterization or limited tonal range

**Matching Exposures**
1. Compare histogram shapes between shots
2. Adjust exposure to match distribution
3. Verify consistency across sequence

### Histogram Interpretation

**Low-Key Image**
- Histogram concentrated on left side
- Indicates dark, moody image
- Common in noir, horror, dramatic scenes

**High-Key Image**
- Histogram concentrated on right side
- Indicates bright, airy image
- Common in comedy, commercial, upbeat scenes

**Balanced Image**
- Histogram spread across full range
- Indicates good tonal distribution
- Typical for most content

## CIE Chromaticity Scope

### Understanding CIE Chromaticity

**Display Characteristics**
- Scientific color representation
- Horseshoe-shaped gamut display
- Shows color space coverage
- Indicates color accuracy and gamut

**Color Gamut Boundaries**
- Outer boundary: Visible spectrum
- Inner triangles: Specific color spaces (Rec.709, P3, Rec.2020)
- Dots: Colors present in image
- Concentration: Dominant colors

### CIE Scope Applications

**Gamut Verification**
- Ensure colors within target color space
- Identify out-of-gamut colors
- Verify delivery compliance
- Manage wide gamut to standard gamut conversion

**Color Space Comparison**
- Visualize difference between color spaces
- Understand gamut limitations
- Plan for color space conversions

**Color Accuracy**
- Verify colors match intended targets
- Identify color shifts or inaccuracies
- Ensure consistent color reproduction

## Scope-Based Workflows

### Technical Correction Workflow

**Step 1: Exposure (Waveform)**
1. Check for clipped highlights or crushed blacks
2. Adjust exposure to achieve proper range
3. Ensure waveform within legal limits
4. Verify consistent exposure across shots

**Step 2: White Balance (RGB Parade)**
1. Identify channel misalignment
2. Adjust color temperature and tint
3. Align channels in midtones and highlights
4. Verify neutral grays are balanced

**Step 3: Saturation (Vectorscope)**
1. Check overall saturation levels
2. Verify skin tones on skin tone line
3. Ensure colors within broadcast safe limits
4. Adjust saturation as needed

**Step 4: Verification (All Scopes)**
1. Review all scopes for technical compliance
2. Verify consistency across shots
3. Check for any remaining issues
4. Confirm broadcast safe if required

### Creative Grading with Scopes

**Using Scopes for Consistency**
- Match scope patterns across shots in scene
- Maintain consistent look throughout project
- Use scopes to verify creative intent
- Balance technical requirements with creative goals

**Scopes as Creative Tools**
- Intentionally shift vectorscope for color palette
- Use waveform to create specific contrast
- Monitor histogram for tonal distribution
- Verify creative choices are consistent

## Broadcast Standards and Compliance

### Legal Levels

**Rec.709 (HD Broadcast)**
- Luma: 16-235 (8-bit) or 64-940 (10-bit)
- Chroma: 16-240 (8-bit) or 64-960 (10-bit)
- Ensure waveform and vectorscope within these ranges

**Full Range (Data/Web)**
- Luma: 0-255 (8-bit) or 0-1023 (10-bit)
- Chroma: 0-255 (8-bit) or 0-1023 (10-bit)
- More flexibility, but requires proper handling

### Compliance Workflow

**Ensuring Broadcast Safe**
1. Check waveform for legal luma range
2. Check vectorscope for legal chroma range
3. Apply Soft Clip or Legalizer if needed
4. Verify compliance on all shots
5. Export with correct levels (legal vs. full)

**Soft Clip vs. Hard Clip**
- **Soft Clip**: Gradually compresses out-of-range values (preferred)
- **Hard Clip**: Abruptly cuts off out-of-range values (can cause banding)
- Use Soft Clip for better quality

## Scope Calibration and Setup

### Monitor Calibration

**Importance**
- Scopes provide objective measurement
- Calibrated monitor ensures accurate visual assessment
- Combine scope analysis with calibrated viewing
- Regular calibration maintains accuracy

**Calibration Tools**
- Hardware calibrators (X-Rite, Datacolor)
- Calibration software
- Test patterns and charts
- Regular verification

### Scope Settings

**Waveform Settings**
- Choose appropriate mode (Luma, RGB, YCbCr)
- Set scale (IRE, %, 10-bit values)
- Enable/disable filtering

**Vectorscope Settings**
- Enable skin tone line
- Show/hide color targets
- Adjust gain for visibility

**General Settings**
- Scope size and layout
- Update rate (real-time vs. paused)
- Overlay options

## Advanced Scope Techniques

### Using Multiple Scopes Simultaneously

**Comprehensive Analysis**
- Waveform for exposure
- RGB Parade for color balance
- Vectorscope for saturation and hue
- Histogram for tonal distribution
- All scopes provide complete picture

**Efficient Workflow**
- Arrange scopes for easy viewing
- Focus on relevant scope for current adjustment
- Cross-reference between scopes
- Verify changes across all scopes

### Scope-Based Shot Matching

**Matching Workflow**
1. Display reference shot scopes
2. Display current shot scopes
3. Adjust current shot to match scope patterns
4. Verify match across all scopes
5. Fine-tune based on visual assessment

**Scope Comparison**
- Match waveform shape and range
- Match RGB parade channel relationships
- Match vectorscope color distribution
- Match histogram tonal distribution