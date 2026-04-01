---
name: color-grading-advanced
description: "Master advanced color grading techniques in DaVinci Resolve and professional color workflows. Use for: primary and secondary color correction, HDR grading, LUT creation and application, node-based workflows, color theory implementation, scopes analysis, color space management, RAW and LOG footage grading, shot matching, and cinematic color styling. Covers DaVinci Resolve, Adobe tools, and professional color pipelines."
---

# Advanced Color Grading

Master professional color correction and grading techniques for cinematic visual storytelling.

## Overview

Advanced color grading transforms footage from technically correct to emotionally compelling, using sophisticated tools and color theory to enhance mood, guide attention, and establish visual style. This skill covers professional workflows in DaVinci Resolve and other industry-standard applications, from technical color correction through creative grading and delivery.

## Color Theory Fundamentals

### Color Spaces and Management

| Color Space | Use Case | Characteristics |
|-------------|----------|------------------|
| Rec. 709 | SDR broadcast, web | Limited range, standard dynamic range |
| Rec. 2020 | HDR, wide gamut | Extended color range, HDR support |
| Rec. 2100 | HDR mastering | Brightest highlights, deepest blacks |
| DCI-P3 | Cinema exhibition | Commercial cinema standard |
| DaVinci Wide Gamut | Processing | Maximum flexibility for grading |

### RAW and LOG Workflows

**RAW Footage**
- Captures 12-14 bits of information
- Maximum control over exposure and color
- Requires powerful hardware for processing
- Ideal for high-end productions

**LOG Footage**
- Optimized gamma curve for extended dynamic range
- Desaturated, low-contrast appearance
- Requires conversion to viewing color space
- Balance between quality and file size

## DaVinci Resolve Core Tools

### Color Wheels and Primary Adjustments

**Primary Wheels**
- **Lift (Shadows)**: Darkest parts of image
- **Gamma (Midtones)**: Mid-range brightness and color
- **Gain (Highlights)**: Brightest areas
- **Offset**: Global brightness and color adjustment

**Log Grading Wheels**
- Tightly defined tonal ranges
- Film-style grading approach
- Adjustments to one range don't significantly impact others
- Ideal for cinematic looks

### Curves for Precision Control

**Custom Curves**
- Independent RGB and luminance control
- Precise tonal adjustments
- S-curves for contrast enhancement

**Advanced Curve Types**
- **Hue Vs Hue**: Change one hue to another (cyan sky to blue)
- **Hue Vs Sat**: Alter saturation of specific hue
- **Hue Vs Lum**: Modify lightness of specific colors
- **Lum Vs Sat**: Adjust saturation in different tonal areas
- **Sat Vs Sat**: Target specific saturation ranges

### Node-Based Workflow

**Node Structure Best Practices**
1. **Node 1**: Exposure and contrast correction
2. **Node 2**: White balance and color temperature
3. **Node 3**: Saturation and vibrance
4. **Node 4**: Secondary corrections (skin tones, skies)
5. **Node 5**: Creative grading and look development
6. **Node 6**: Final refinement and output adjustments

**Node Types**
- **Serial nodes**: Sequential processing
- **Parallel nodes**: Blend multiple grades
- **Layer nodes**: Composite-style grading
- **Outside nodes**: Apply before or after node tree

## LUTs (Lookup Tables)

### LUT Types and Applications

**Technical LUTs**
- Color space conversions
- LOG to Rec.709 conversion
- Camera-specific transforms
- Display calibration

**Creative LUTs**
- Stylistic looks (cinematic, vintage, modern)
- Film emulation
- Brand-specific aesthetics
- Starting points for custom grades

### LUT Workflow

1. Apply technical LUT first (if needed for LOG conversion)
2. Perform color correction
3. Apply creative LUT (optional)
4. Adjust LUT intensity via Key tab Gain field
5. Grade on top of LUT for customization
6. Export custom LUT for consistency across projects

## Professional Scopes

### Essential Scopes for Objective Analysis

**Waveform Monitor**
- Shows luminance distribution across frame
- Horizontal axis = image position
- Vertical axis = brightness level
- Ideal for exposure evaluation

**Parade (RGB)**
- Separate waveforms for red, green, blue channels
- Identifies color casts and imbalances
- Essential for white balance correction

**Vectorscope**
- Displays color information (hue and saturation)
- Radial display with color targets
- Skin tone line for accurate flesh tones
- Saturation shown as distance from center

**Histogram**
- Distribution of tonal values
- Shows clipping in highlights and shadows
- Quick exposure assessment

**CIE Chromaticity**
- Scientific color representation
- Shows color gamut coverage
- Ensures colors within deliverable space

## Secondary Grading Techniques

### Qualifier-Based Selection

**HSL Qualification**
- Select specific hues, saturation ranges, luminance values
- Refine selection with softness and range controls
- Isolate elements like skies, skin tones, foliage

**Qualification Workflow**
1. Use eyedropper to select target color
2. Adjust HSL ranges to refine selection
3. Use Qualifier palette controls for precision
4. Check selection in Highlight mode
5. Apply corrections to selected area only

### Power Windows

**Shape-Based Selection**
- Draw shapes around objects (circle, square, polygon, curve)
- Gradient windows for vignettes
- Combine multiple windows for complex selections
- Soften edges for natural blending

**Window Tracking**
- Automatically animate windows to follow moving objects
- Frame-by-frame tracking for precision
- Stabilization for locked-off corrections
- Essential for targeted adjustments on moving subjects

## Advanced Techniques

### HDR Grading (Resolve Studio)

**HDR Color Wheels**
- Zone-based exposure control
- Customizable luminance zones
- Independent color adjustments per zone
- Wide color gamut support

**HDR Workflow**
1. Set timeline to HDR color space (Rec.2100, HLG, Dolby Vision)
2. Use HDR scopes for monitoring
3. Grade with HDR wheels for zone control
4. Manage peak brightness (1000-4000 nits)
5. Create SDR version using color space transform

### Color Warper

**Advanced Hue Manipulation**
- Grid-based hue and saturation warping
- Warp color based on luminance
- Set Hue vs. Hue grades for specific saturations
- Precise color transformations

### Magic Mask (AI-Powered)

**Automatic Masking**
- Detects and tracks people, faces, objects
- No manual rotoscoping required
- Isolated adjustments without qualification
- Significant time savings on complex selections

### Face Refinement Tool

**Automatic Face Detection**
- Finds faces in frame automatically
- Creates masks for different facial areas
- Tracks faces through movement
- Ideal for beauty retouching and skin tone correction

## Shot Matching and Consistency

### Automatic Shot Matching

**Match Workflow**
1. Grade hero shot to desired look
2. Select shots to match
3. Use Shot Match feature
4. Resolve analyzes and matches color, contrast, brightness
5. Refine automatic match manually if needed

### Manual Matching Techniques

**Using Scopes**
- Compare waveforms between shots
- Match luminance distribution
- Align RGB parade for color consistency
- Use vectorscope for hue/saturation matching

**Gallery and Stills**
- Save grades as stills in gallery
- Organize into albums by scene or look
- Apply saved grades to new clips
- Wipe between current and reference for comparison

## Creative Grading Styles

### Popular Cinematic Looks

| Style | Characteristics | Technique |
|-------|-----------------|------------|
| Teal and Orange | Complementary color contrast | Push shadows toward teal, highlights toward orange |
| Bleach Bypass | Desaturated, high contrast | Reduce saturation, increase contrast, crush blacks |
| Film Emulation | Grain, color shifts, halation | Apply film grain, adjust color curves, add glow |
| Vintage | Faded, warm tones | Lift blacks, reduce saturation, warm color temperature |
| Modern Commercial | Clean, vibrant, punchy | Increase saturation, enhance contrast, crisp whites |

### Building Custom Looks

**Look Development Process**
1. Analyze reference images for color palette
2. Identify key color relationships
3. Build look on hero shot
4. Test on various lighting conditions
5. Refine for consistency across scenes
6. Save as LUT or preset for reuse

## Resolve FX and Plugins

### Essential Resolve FX

- **Beauty**: Skin smoothing and enhancement
- **Film Grain**: Add authentic grain texture
- **Glow**: Bloom and diffusion effects
- **Lens Flare**: Optical flare simulation
- **Sharpen**: Detail enhancement
- **Blur**: Various blur types for effects
- **Color Space Transform**: Convert between color spaces

## Workflow Optimization

### Project Setup

**Timeline Settings**
- Set correct timeline color space
- Configure input color space transform
- Set output color space for delivery
- Enable color management for consistency

**Optimization Settings**
- Generate optimized media for smooth playback
- Use render cache for complex grades
- Enable GPU acceleration
- Set appropriate cache format

### Collaborative Grading

**DaVinci Resolve Collaboration**
- Multiple colorists work simultaneously
- Shared database for project access
- Version control for grade iterations
- Real-time updates across workstations

## Delivery and Export

### Export Considerations

**Format Selection**
- Match delivery specifications
- Maintain color space consistency
- Include appropriate metadata
- Test on target display devices

**Multiple Deliverables**
- Create versions for different platforms (cinema, broadcast, web)
- HDR and SDR versions from single grade
- Use color space transforms for conversions
- Maintain quality across all versions

## Using the Reference Files

### When to Read Each Reference

**`/references/resolve-advanced-workflows.md`** — Read when working on complex DaVinci Resolve projects, using advanced features like HDR grading, Color Warper, or collaborative workflows.

**`/references/color-theory-application.md`** — Read when developing custom looks, understanding color relationships, or making creative grading decisions based on color psychology.

**`/references/scopes-and-analysis.md`** — Read when learning to read professional scopes, performing technical color correction, or ensuring broadcast-safe levels.

**`/references/lut-creation-management.md`** — Read when creating custom LUTs, managing LUT libraries, or implementing LUT-based workflows across projects.
