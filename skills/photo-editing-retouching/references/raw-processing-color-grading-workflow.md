# RAW Processing, Color Grading, and Workflow

## Overview

A professional photo editing workflow encompasses the entire process from importing RAW files through final export, with RAW processing and color grading serving as critical stages. RAW processing maximizes image quality by leveraging uncompressed sensor data, while color grading adds creative vision and mood. Understanding and implementing an efficient, organized workflow is essential for consistent, high-quality results and professional productivity.

## Understanding RAW Files

### What Are RAW Files?

RAW files are unprocessed, uncompressed data captured directly from a camera's image sensor, containing all the information recorded at the moment of capture.

#### RAW vs. JPEG

**RAW Files:**
- Unprocessed sensor data
- No compression (or lossless compression)
- Maximum editing flexibility
- Larger file sizes (20-50MB typical)
- Require processing software
- Not directly viewable
- Professional standard

**JPEG Files:**
- Processed and compressed by camera
- Smaller file sizes (2-10MB typical)
- Limited editing flexibility
- Immediately viewable
- Convenient for sharing
- Lossy compression
- Data discarded permanently

#### Advantages of Shooting RAW

**Greater Dynamic Range:**
- Capture more highlight and shadow detail
- Better recovery of blown highlights
- Lift shadows without excessive noise
- More information to work with

**White Balance Flexibility:**
- Adjust white balance without quality loss
- Correct color temperature errors
- Creative color temperature adjustments
- Non-destructive changes

**Higher Bit Depth:**
- 12-bit or 14-bit (vs. 8-bit JPEG)
- 4,096-16,384 tones per channel (vs. 256)
- Smoother gradients
- Better color accuracy
- More editing headroom

**Non-Destructive Editing:**
- Original data never altered
- Infinite adjustments possible
- Revert to original anytime
- Experiment freely

**Better Quality:**
- No compression artifacts
- Maximum detail preservation
- Superior print quality
- Professional results

### RAW File Formats

**Proprietary Formats:**
- Canon: .CR2, .CR3
- Nikon: .NEF
- Sony: .ARW
- Fujifilm: .RAF
- Olympus: .ORF
- Panasonic: .RW2
- Pentax: .PEF

**Universal Format:**
- Adobe DNG (Digital Negative)
- Open standard
- Long-term archival
- Some cameras support natively
- Can convert proprietary RAW to DNG

## RAW Processing Workflow

### Stage 1: Import and Organization

#### Importing Files

**Lightroom Classic Import:**

**Process:**
1. Connect camera or card reader
2. File > Import Photos and Video
3. Select source (card, folder)
4. Choose import method:
   - Copy: Copy files to new location
   - Move: Move files to new location
   - Add: Leave files in place, add to catalog
5. Select destination folder
6. Apply import presets if desired
7. Add keywords and metadata
8. Import

**Import Presets:**
- Apply develop settings on import
- Lens corrections
- Camera profile
- Basic adjustments
- Consistent starting point

**File Handling:**
- Build previews (Standard or 1:1)
- Make second copy (backup)
- Add to collection
- Organize by date or project

#### Initial Culling and Selection

**First Pass:**
- Quick review of all images
- Flag picks (P key) and rejects (X key)
- Or use star ratings (1-5)
- Focus on keepers
- Delete obvious rejects

**Second Pass:**
- Review flagged/rated images
- Refine selections
- Choose best from similar shots
- Consider composition, focus, expression
- Final selection for editing

**Organization:**
- Add keywords
- Apply color labels
- Create collections
- Group by subject or theme
- Maintain consistent system

### Stage 2: Global RAW Adjustments

Global adjustments affect the entire image and establish the foundation for further editing.

#### Camera Profile and White Balance

**Camera Profile:**

**Purpose:**
- Determines color rendering
- Affects overall look
- Starting point for color

**Options (Lightroom/Camera Raw):**
- Adobe Color (default, balanced)
- Adobe Landscape (more saturation, vibrance)
- Adobe Portrait (softer, flattering skin tones)
- Adobe Standard (brightens dark areas)
- Adobe Vivid (high saturation)
- Camera matching profiles (match in-camera JPEG)

**Selection:**
- Choose based on subject and desired look
- Landscape: Adobe Landscape
- Portraits: Adobe Portrait or Adobe Color
- Experiment to find preference

**White Balance:**

**Methods:**

**As Shot:**
- Camera's white balance setting
- Starting point
- May need adjustment

**Auto:**
- Lightroom's automatic white balance
- Often accurate
- Good starting point

**Presets:**
- Daylight, Cloudy, Shade, Tungsten, Fluorescent, Flash
- Match lighting conditions
- Quick adjustments

**Custom:**
- Temperature slider (blue to yellow)
- Tint slider (green to magenta)
- Eyedropper tool (click neutral gray)
- Fine-tune for accuracy or creative effect

**Creative White Balance:**
- Warmer for golden hour enhancement
- Cooler for moody, dramatic feel
- Not always about "correct" color

#### Exposure and Tonal Adjustments

**Basic Panel (Lightroom/Camera Raw):**

**Exposure:**
- Overall brightness
- Affects entire tonal range
- Adjust first
- Typically -1 to +1 stop

**Contrast:**
- Difference between lights and darks
- Increase for punch
- Decrease for flat, soft look
- Use carefully (can clip tones)

**Highlights:**
- Brightest areas
- Negative values recover blown highlights
- Bring down bright skies
- Preserve detail in bright areas

**Shadows:**
- Darkest areas
- Positive values lift shadows
- Reveal hidden detail
- Watch for noise in deep shadows

**Whites:**
- White point
- Sets brightest white in image
- Hold Alt/Option while dragging to see clipping
- Adjust until just before clipping

**Blacks:**
- Black point
- Sets darkest black in image
- Hold Alt/Option to see clipping
- Adjust for desired shadow depth

**Workflow Order:**
1. Exposure (overall brightness)
2. Highlights (recover bright areas)
3. Shadows (lift dark areas)
4. Whites (set white point)
5. Blacks (set black point)
6. Contrast (if needed, after tonal range set)

**Tone Curve:**

**Purpose:**
- More precise tonal control
- Adjust specific tonal ranges
- Create contrast and mood

**Parametric Curve:**
- Four regions: Highlights, Lights, Darks, Shadows
- Sliders adjust each region
- Range sliders control region boundaries
- Intuitive for beginners

**Point Curve:**
- Click to add control points
- Drag points to adjust
- Precise control
- More advanced

**Common Adjustments:**
- S-curve: Increase contrast (lift highlights, lower shadows)
- Fade blacks: Lift bottom-left point (film look)
- Matte effect: Lower top-right point
- Crush blacks: Lower shadows for deep blacks

#### Presence Adjustments

**Texture:**
- Enhances medium-sized details
- Positive: Brings out detail
- Negative: Smooths detail
- Good for skin texture control

**Clarity:**
- Enhances edge contrast (midtone contrast)
- Positive: Adds punch and definition
- Negative: Softens and glows
- Use carefully (can look artificial)

**Dehaze:**
- Removes atmospheric haze
- Increases contrast and saturation
- Powerful for landscapes
- Can be overdone

**Vibrance:**
- Intelligent saturation
- Protects skin tones
- Boosts muted colors more
- Safer than Saturation

**Saturation:**
- Overall color intensity
- Affects all colors equally
- Can oversaturate skin tones
- Use carefully

#### Lens Corrections

**Profile Corrections:**

**Enable Profile Corrections:**
- Automatically detects lens
- Corrects distortion
- Corrects vignetting
- Corrects chromatic aberration
- Should be enabled for most images

**Manual Corrections:**
- Distortion slider (if needed)
- Vignetting amount and midpoint
- Fine-tune if automatic isn't perfect

**Chromatic Aberration:**
- Remove Chromatic Aberration checkbox
- Eliminates color fringing
- Especially visible at high-contrast edges
- Should be enabled

**Upright Tool:**
- Auto: Automatic perspective correction
- Level: Straightens horizon
- Vertical: Corrects vertical perspective
- Full: Corrects both horizontal and vertical
- Guided: Manual perspective correction
- Useful for architecture

### Stage 3: Local Adjustments

Local adjustments target specific areas of the image for refined control.

#### Masking Tools (Lightroom/Camera Raw)

**AI-Powered Masks:**

**Select Subject:**
- Automatically detects main subject
- Creates precise mask
- Adjust subject independently from background
- Refine with brush if needed

**Select Sky:**
- Detects and masks sky
- Perfect for sky adjustments
- Darkening, color changes
- Separate from foreground

**Select Background:**
- Masks everything except subject
- Adjust background independently
- Blur, darken, or color grade

**Select People:**
- Detects people in image
- Sub-masks: Person, Skin, Teeth, Eyes, Hair, etc.
- Targeted portrait adjustments
- Skin retouching, teeth whitening

**Select Objects:**
- Click on object to select
- AI detects object boundaries
- Precise selection
- Adjust or remove objects

**Manual Masks:**

**Brush:**
- Paint mask manually
- Adjustable size, feather, flow, density
- Auto Mask option (edge detection)
- Add or subtract from mask
- Precise control

**Linear Gradient:**
- Straight gradient mask
- Drag to create
- Useful for skies, horizons
- Adjustable feather

**Radial Gradient:**
- Circular/elliptical gradient
- Drag to create
- Invert for vignettes
- Adjustable feather
- Useful for spotlighting

**Mask Refinement:**
- Add or subtract from masks
- Combine multiple mask types
- Intersect masks
- Invert masks
- Adjust mask opacity

#### Local Adjustment Options

Once a mask is created, all basic adjustments are available:
- Exposure, Contrast
- Highlights, Shadows, Whites, Blacks
- Texture, Clarity, Dehaze
- Saturation, Vibrance
- Color Temperature, Tint
- Sharpness, Noise Reduction
- And more

**Common Local Adjustments:**

**Darken Sky:**
- Select Sky mask
- Lower exposure
- Increase contrast
- Adjust color temperature

**Brighten Subject:**
- Select Subject mask
- Increase exposure
- Add clarity or texture
- Enhance colors

**Dodge and Burn:**
- Brush mask on areas to lighten (dodge)
- Increase exposure slightly
- Brush mask on areas to darken (burn)
- Decrease exposure slightly
- Build up gradually

**Skin Retouching:**
- Select People > Skin
- Reduce texture (smoothing)
- Adjust exposure (even tone)
- Reduce clarity (softening)
- Subtle adjustments

**Eye Enhancement:**
- Select People > Eyes
- Increase exposure (brighten)
- Increase clarity (sharpen)
- Increase saturation (enhance color)

**Teeth Whitening:**
- Select People > Teeth
- Increase exposure (brighten)
- Decrease saturation (remove yellow)
- Subtle adjustments

### Stage 4: Detail and Sharpening

#### Sharpening

**Detail Panel:**

**Amount:**
- Strength of sharpening
- 40-60 for most images
- Higher for landscapes, architecture
- Lower for portraits

**Radius:**
- Size of sharpening halo
- 0.5-1.0 for most images
- Smaller for fine detail
- Larger for coarser detail

**Detail:**
- How much fine detail to sharpen
- 25 default
- Higher for maximum detail
- Lower to avoid halos

**Masking:**
- Controls where sharpening is applied
- 0 = entire image
- Higher = only edges
- Hold Alt/Option while dragging to see mask
- Prevents sharpening smooth areas (like skin)

**Sharpening Workflow:**
1. View at 100% zoom
2. Adjust Amount first
3. Adjust Radius for detail size
4. Adjust Detail for fine-tuning
5. Adjust Masking to protect smooth areas
6. Zoom out to check overall effect

#### Noise Reduction

**When to Use:**
- High ISO images
- Underexposed images (lifted shadows)
- Long exposures
- Visible grain or color splotches

**Luminance:**
- Reduces brightness noise (grain)
- 0-100 scale
- Start around 20-40 for noisy images
- Higher values soften detail
- Balance noise reduction with detail preservation

**Detail:**
- Preserves detail while reducing luminance noise
- Higher values preserve more detail
- Lower values smoother but softer

**Contrast:**
- Preserves contrast while reducing luminance noise
- Adjust to taste

**Color:**
- Reduces color noise (color splotches)
- 25 default
- Increase for visible color noise
- Less impact on detail than luminance

**Detail and Smoothness:**
- Fine-tune color noise reduction
- Adjust as needed

## Color Grading

Color grading is the creative process of manipulating colors to enhance mood, create atmosphere, and realize artistic vision.

### Color Correction vs. Color Grading

**Color Correction:**
- Technical process
- Achieve accurate, neutral colors
- Fix color casts
- Balance white balance
- Foundation for grading

**Color Grading:**
- Creative process
- Stylize colors
- Create mood and atmosphere
- Artistic interpretation
- Builds on corrected image

**Workflow:**
1. Color correct first (accurate colors)
2. Color grade second (creative colors)

### Color Grading Tools

#### Color Grading Panel (Lightroom/Camera Raw)

The Color Grading panel (formerly Split Toning) provides three-way color wheels for precise color control.

**Three-Way Color Wheels:**

**Shadows:**
- Affects darkest tones
- Add color to shadow areas
- Create depth and mood

**Midtones:**
- Affects middle tones
- Most visible adjustments
- Dominant color influence

**Highlights:**
- Affects brightest tones
- Add color to highlight areas
- Create atmosphere

**Global:**
- Affects entire image
- Overall color shift
- Use for subtle tinting

**Using Color Wheels:**

**Hue:**
- Move handle around wheel
- Selects color
- 360-degree color spectrum

**Saturation:**
- Move handle from center to edge
- Center = no color (grayscale)
- Edge = maximum saturation
- Distance from center = intensity

**Luminance:**
- Slider below wheel
- Brightens or darkens tonal range
- Affects brightness of selected tones

**Blending:**
- Controls overlap between tonal ranges
- Higher values = more overlap
- Smoother transitions
- Adjust for natural blending

**Balance:**
- Shifts balance between shadows and highlights
- Negative = more shadow influence
- Positive = more highlight influence
- Fine-tune color distribution

#### HSL/Color Panel

The HSL (Hue, Saturation, Luminance) panel provides precise control over individual color ranges.

**Eight Color Ranges:**
- Red
- Orange
- Yellow
- Green
- Aqua
- Blue
- Purple
- Magenta

**Hue Tab:**
- Shift color itself
- Example: Make sky more cyan or more purple
- Subtle shifts for natural look
- Dramatic shifts for creative effects

**Saturation Tab:**
- Adjust color intensity
- Increase for vibrant colors
- Decrease for muted, desaturated look
- Selective saturation control

**Luminance Tab:**
- Adjust brightness of color
- Lighten or darken specific colors
- Useful for separating tones
- Enhance or subdue colors

**Targeted Adjustment Tool:**
- Click tool icon
- Click and drag on image
- Adjusts color under cursor
- Intuitive and visual
- Faster than sliders

**Common HSL Adjustments:**

**Enhance Blue Sky:**
- Blue Hue: Shift toward cyan
- Blue Saturation: Increase
- Blue Luminance: Decrease slightly

**Improve Skin Tones:**
- Orange Hue: Shift slightly toward red
- Orange Saturation: Decrease slightly
- Orange Luminance: Increase slightly

**Vibrant Foliage:**
- Green Saturation: Increase
- Yellow Saturation: Increase
- Green Luminance: Adjust to taste

**Muted, Desaturated Look:**
- Decrease saturation across all colors
- Increase luminance slightly
- Fade blacks with tone curve

#### Tone Curve for Color Grading

The tone curve can be used creatively for color grading beyond tonal adjustments.

**RGB Channels:**

**Red Channel:**
- Lift curve: Add red
- Lower curve: Add cyan
- Shadows: Cyan shadows, red highlights
- Highlights: Red highlights, cyan shadows

**Green Channel:**
- Lift curve: Add green
- Lower curve: Add magenta
- Creative color shifts

**Blue Channel:**
- Lift curve: Add blue
- Lower curve: Add yellow/orange
- Common for warm/cool contrasts

**Common Tone Curve Color Grades:**

**Cinematic Teal and Orange:**
1. Blue channel: Lift shadows (add teal to shadows)
2. Red channel: Lift highlights (add warmth to highlights)
3. Adjust to taste
4. Popular film look

**Faded Film Look:**
1. RGB curve: Lift bottom-left point (fade blacks)
2. RGB curve: Lower top-right point slightly (fade highlights)
3. Reduces contrast
4. Vintage aesthetic

**Matte Effect:**
1. Lift blacks significantly
2. Lower whites slightly
3. Compressed tonal range
4. Soft, dreamy look

### Color Grading Styles and Moods

#### Cinematic

**Characteristics:**
- Teal shadows, orange highlights
- Desaturated midtones
- Crushed or lifted blacks
- Film-like quality
- High contrast or matte

**How to Achieve:**
1. Color Grading: Teal in shadows, orange in highlights
2. HSL: Desaturate blues and oranges slightly
3. Tone Curve: S-curve for contrast or lift blacks for matte
4. Adjust to taste

#### Vintage/Film

**Characteristics:**
- Warm, faded tones
- Reduced contrast
- Lifted blacks
- Grain
- Nostalgic feel

**How to Achieve:**
1. Tone Curve: Lift blacks, lower highlights
2. Color Grading: Warm tones in midtones and highlights
3. HSL: Reduce saturation overall
4. Add grain (Effects panel)
5. Slight vignette

#### High Fashion

**Characteristics:**
- Cool, desaturated tones
- High contrast
- Selective color pops
- Clean, modern aesthetic
- Crisp and sharp

**How to Achieve:**
1. Cool white balance
2. HSL: Desaturate most colors, keep one or two vibrant
3. High contrast (tone curve or contrast slider)
4. Sharpening
5. Clean, minimal look

#### Moody/Dark

**Characteristics:**
- Dark, rich tones
- Deep shadows
- Muted colors
- Dramatic atmosphere
- Low-key lighting

**How to Achieve:**
1. Lower exposure
2. Crush blacks (tone curve)
3. Desaturate colors (HSL)
4. Color Grading: Dark blues or teals in shadows
5. Vignette
6. Dramatic contrast

#### Bright and Airy

**Characteristics:**
- Light, bright tones
- Lifted shadows
- Soft contrast
- Pastel colors
- Dreamy, ethereal feel

**How to Achieve:**
1. Increase exposure
2. Lift shadows
3. Fade blacks (tone curve)
4. Reduce contrast
5. Desaturate slightly
6. Warm white balance
7. Soft, glowing look

### LUTs (Look-Up Tables)

LUTs are pre-made color grading presets that map input colors to output colors.

**What Are LUTs:**
- Color transformation files
- Apply complex color grades instantly
- Originated in video/film industry
- .cube or .3dl file formats

**Using LUTs:**

**Photoshop:**
- Color Lookup adjustment layer
- Load 3D LUT file
- Adjust opacity for intensity

**Lightroom:**
- Requires plugin or profile
- Or use Photoshop for LUT application

**Capture One:**
- Styles & Presets
- Import LUT
- Apply to image

**Benefits:**
- Quick, professional looks
- Consistent across images
- Cinematic color grades
- Starting point for further adjustments

**Considerations:**
- May need adjustment for specific images
- Not one-size-fits-all
- Adjust opacity or refine after application
- Best on properly exposed, color-corrected images

## Professional Workflow Best Practices

### Workflow Organization

#### Folder Structure

**Recommended Structure:**
```
Year/
  Month/
    Date_ProjectName/
      RAW/
      Edited/
      Delivered/
```

**Or by Project:**
```
Projects/
  ClientName_ProjectName/
    RAW/
    Edited/
    Delivered/
```

**Benefits:**
- Easy to locate files
- Consistent organization
- Scalable system
- Professional structure

#### Backup Strategy

**3-2-1 Rule:**
- 3 copies of data
- 2 different media types
- 1 off-site backup

**Implementation:**
- Original files on computer
- Backup to external hard drive
- Cloud backup (Backblaze, Crashplan, etc.)
- Or second external drive off-site

**Frequency:**
- Backup immediately after shoots
- Automated daily backups
- Verify backups regularly
- Don't delete originals until backed up

### Batch Processing and Efficiency

#### Sync Settings

**Lightroom Sync:**
1. Edit one image
2. Select similar images
3. Click Sync button
4. Choose settings to sync
5. Apply to all selected

**Benefits:**
- Consistent look across series
- Massive time savings
- Efficient workflow

#### Presets

**Creating Presets:**
1. Edit image to desired look
2. Develop > New Preset
3. Name descriptively
4. Choose settings to include
5. Save

**Using Presets:**
- Apply on import
- Apply during editing
- One-click application
- Adjust after application

**Preset Organization:**
- Organize in folders by type
- Naming convention
- Delete unused presets
- Share or sell presets

#### Copy/Paste Settings

**Quick Method:**
1. Edit image
2. Cmd/Ctrl + C (copy settings)
3. Select other images
4. Cmd/Ctrl + V (paste settings)
5. Choose settings to paste

### Export Workflow

#### Export Settings

**File Format:**
- JPEG: Web, client delivery, social media
- TIFF: Print, archival, further editing
- PSD: Layered files for Photoshop
- PNG: Transparency needs

**Quality:**
- JPEG: 80-100 quality
- 90-95 good balance of quality and size
- 100 for maximum quality (larger files)

**Color Space:**
- sRGB: Web, social media, most uses
- Adobe RGB: Print, professional output
- ProPhoto RGB: Maximum color gamut (archival)

**Resolution:**
- Web: 72 PPI, resize to pixel dimensions
- Print: 300 PPI, actual print size
- Social media: Specific pixel dimensions

**Sharpening:**
- Output sharpening for intended use
- Screen: Standard
- Matte Paper: Low
- Glossy Paper: Standard or High

**Metadata:**
- Include copyright
- Include contact info
- Remove location data if privacy concern
- Include keywords for searchability

#### Export Presets

**Create Export Presets:**
- Common export scenarios
- Web export (sRGB, 2000px long edge, 90 quality)
- Print export (Adobe RGB, 300 PPI, full size)
- Social media (specific dimensions)
- Client delivery

**Benefits:**
- One-click export
- Consistent settings
- No mistakes
- Efficient workflow

### Quality Control

#### Final Review

**Checklist:**
- Exposure correct?
- White balance accurate or intentional?
- Colors pleasing?
- Sharpness appropriate?
- No dust spots or distractions?
- Skin retouching natural?
- Consistent with series?
- Meets client expectations?

**Zoom In:**
- Check at 100% zoom
- Look for artifacts
- Check sharpness
- Spot dust and blemishes

**Fresh Eyes:**
- Take breaks
- Review next day if possible
- Get second opinion
- Avoid over-editing

## Conclusion

A professional photo editing workflow encompasses the entire process from RAW import through final export, with each stage building upon the previous. RAW processing maximizes image quality by leveraging the full data captured by the camera sensor, allowing extensive adjustments to exposure, color, and detail without quality loss. Color grading adds creative vision, transforming technically correct images into emotionally resonant works of art. An organized, efficient workflow with proper file management, backup strategies, and batch processing techniques enables photographers to maintain consistency, meet deadlines, and focus creative energy where it matters most. Mastering this complete workflow is essential for professional photography and retouching success.

## References

- Boris FX: How to Color Grade in Lightroom and Photoshop
- PetaPixel: My Color Grading Workflow for RAW Landscape Photos
- Tapflare: Lightroom Workflow Use Cases
- DIY Photography: RAW Photo Processing Workflow
- Noam Kroll: Best Order of Operations for Color Grading