# Post-Processing for Landscape Photography

Post-processing is an essential phase of landscape photography, allowing photographers to refine images, realize their artistic vision, and overcome technical limitations while maintaining natural authenticity.

---

## Philosophy and Approach

### The Role of Post-Processing

Post-processing is not about creating something that didn't exist, but rather about realizing the scene as experienced and overcoming limitations of camera sensors.

**What Post-Processing Should Do**:
- Correct technical issues (exposure, white balance, lens distortion)
- Enhance what was present in the scene
- Guide viewer attention to key elements
- Express the photographer's artistic vision
- Overcome sensor limitations (dynamic range, color rendition)

**What Post-Processing Should Not Do**:
- Fabricate elements that weren't present
- Create unrealistic, over-processed appearance
- Rely on excessive manipulation to compensate for poor capture
- Misrepresent the scene beyond recognition

### Natural vs. Processed

The goal is a polished, refined image that still appears natural and believable.

**Signs of Over-Processing**:
- Oversaturated, neon-like colors
- Excessive contrast (crushed blacks, blown highlights)
- Unnatural HDR halos and artifacts
- Over-sharpened edges and textures
- Obvious cloning or manipulation
- Unnatural color relationships

**Maintaining Authenticity**:
- Make adjustments incrementally
- Step away and return with fresh eyes
- Compare to original periodically
- View at different sizes and on different screens
- Seek feedback from trusted sources

---

## Software Options

### Adobe Lightroom

**Strengths**:
- Powerful RAW processing engine
- Non-destructive editing
- Excellent organization and cataloging
- Batch processing capabilities
- Presets and profiles
- Integration with Photoshop

**Best For**: Primary workflow for RAW processing, organization, and most adjustments.

**Key Features**:
- Global adjustments (exposure, contrast, color)
- Local adjustments (graduated filters, radial filters, adjustment brush)
- Lens corrections and perspective adjustments
- Noise reduction and sharpening
- Color grading tools

### Adobe Photoshop

**Strengths**:
- Advanced pixel-level editing
- Layers and masking
- Specialized techniques (focus stacking, advanced blending)
- Content-aware tools
- Precise selections and adjustments

**Best For**: Advanced techniques beyond Lightroom's capabilities.

**Key Features**:
- Layer-based editing
- Luminosity masking
- Focus stacking
- Exposure blending
- Advanced cloning and healing
- Precise color and tonal control

### Alternative Software

**Capture One**: Professional RAW processor with excellent color handling and tethering.

**DxO PhotoLab**: Superior lens corrections and noise reduction.

**Affinity Photo**: One-time purchase alternative to Photoshop with similar capabilities.

**Luminar Neo**: AI-powered tools for quick enhancements.

**ON1 Photo RAW**: All-in-one solution with effects and presets.

---

## Lightroom Workflow

### Import and Organization

1. **Import RAW files** with consistent naming and folder structure
2. **Add keywords and metadata** for searchability
3. **Rate and flag** images (star ratings, color labels)
4. **Cull** to select best images for processing
5. **Create collections** for projects or locations

### Global Adjustments

Work from top to bottom in the Develop module, making broad adjustments before refining details.

#### Lens Corrections

**Enable Profile Corrections**:
- Automatically corrects lens distortion, vignetting, and chromatic aberration
- Based on lens metadata
- Should be enabled for virtually all images

**Manual Adjustments**:
- Distortion slider for fine-tuning
- Defringe tool for chromatic aberration
- Upright tool for perspective correction

#### Basic Panel

**Exposure**:
- Overall brightness adjustment
- Use histogram as guide
- Typically adjust ±0.5 to 1.5 stops

**Contrast**:
- Global contrast adjustment
- Often better to use Highlights/Shadows/Whites/Blacks for more control
- Use sparingly; can be added later

**Highlights**:
- Recover detail in bright areas
- Typically reduced (-30 to -100)
- Watch for unnatural flattening

**Shadows**:
- Lift detail in dark areas
- Typically increased (+20 to +80)
- Watch for noise in heavily lifted shadows

**Whites**:
- Set white point (brightest tones)
- Hold Alt/Option while adjusting to see clipping
- Adjust until small areas just begin to clip

**Blacks**:
- Set black point (darkest tones)
- Hold Alt/Option while adjusting to see clipping
- Adjust for depth without crushing detail

**Workflow Tip**: Adjust in order: Exposure → Highlights → Shadows → Whites → Blacks for optimal tonal distribution.

#### Presence Panel

**Texture**:
- Enhances medium-sized details
- Positive values increase detail (rocks, bark, clouds)
- Negative values smooth (water, sky)
- More subtle than Clarity

**Clarity**:
- Enhances midtone contrast and edge definition
- Positive values add punch and definition
- Negative values create soft, dreamy effect
- Use moderately (+10 to +30 typical)
- Can create halos if overused

**Dehaze**:
- Reduces atmospheric haze
- Increases contrast and saturation
- Powerful but can look artificial if overused
- Typical range: +10 to +40

**Vibrance**:
- Increases saturation of muted colors
- Protects already-saturated colors and skin tones
- Preferred over Saturation for natural results
- Typical range: +10 to +30

**Saturation**:
- Increases saturation of all colors equally
- Can quickly look oversaturated
- Use sparingly or not at all
- Typical range: 0 to +15

#### White Balance

**Temperature**:
- Adjust color temperature (warm/cool)
- Move right for warmer (more orange/yellow)
- Move left for cooler (more blue)

**Tint**:
- Adjust green/magenta balance
- Usually requires minimal adjustment

**Approaches**:
- Use eyedropper on neutral gray area
- Use presets (Daylight, Cloudy, Shade) as starting point
- Adjust creatively for mood
- Ensure snow appears white, not blue or yellow

#### Tone Curve

**Purpose**: Fine-tune tonal relationships and contrast.

**Regions**:
- Highlights (upper right)
- Lights (upper middle)
- Darks (lower middle)
- Shadows (lower left)

**Typical Adjustments**:
- Slight S-curve for added contrast
- Lift shadows slightly for detail
- Pull down highlights for control
- Adjust midtones for overall brightness

**Point Curve**: More precise control with custom points on curve.

### Color Adjustments

#### HSL Panel (Hue, Saturation, Luminance)

**Hue**: Shift specific color ranges (e.g., make blues more cyan or purple).

**Saturation**: Increase or decrease intensity of specific colors.

**Luminance**: Brighten or darken specific colors.

**Common Adjustments**:
- **Blue Sky**: Increase blue saturation, decrease luminance slightly
- **Foliage**: Adjust green and yellow hues, increase saturation moderately
- **Sunset**: Enhance orange and yellow saturation
- **Water**: Adjust blue/cyan hue and saturation

**Targeted Adjustment Tool**: Click on color in image and drag to adjust that color range.

#### Color Grading (formerly Split Toning)

**Purpose**: Add color tints to highlights, midtones, and shadows for creative color effects.

**Typical Uses**:
- Warm highlights, cool shadows for dimensional effect
- Consistent color palette across image
- Cinematic or stylized looks
- Subtle toning for mood

**Approach**:
- Use subtly (low saturation values)
- Maintain color harmony
- Consider complementary colors for highlights/shadows

### Local Adjustments

#### Graduated Filter

**Purpose**: Apply adjustments to specific area with gradual transition.

**Common Uses**:
- Darken and enhance sky
- Brighten foreground
- Add warmth to specific area

**Technique**:
- Click and drag from edge toward center
- Adjust size and feather of transition
- Modify exposure, contrast, color, etc.
- Use multiple graduated filters for complex adjustments

#### Radial Filter

**Purpose**: Apply adjustments to elliptical area.

**Common Uses**:
- Vignette effect (darken edges)
- Brighten or enhance specific subject
- Draw attention to focal point

**Technique**:
- Draw ellipse over area
- Choose "Invert" to affect inside or outside of ellipse
- Adjust feather for soft or hard transition
- Modify exposure, contrast, clarity, etc.

#### Adjustment Brush

**Purpose**: Paint adjustments onto specific areas with precision.

**Common Uses**:
- Dodge (lighten) specific elements
- Burn (darken) specific elements
- Enhance or subdue specific areas
- Selective sharpening or softening

**Technique**:
- Select brush size and feather
- Adjust flow and density for subtlety
- Paint over areas to adjust
- Use "Auto Mask" to constrain to edges
- Press O to show/hide mask overlay

**Dodging and Burning**:
- **Dodge**: Increase exposure (+0.5 to +1.0) to lighten and draw attention
- **Burn**: Decrease exposure (-0.5 to -1.0) to darken and subdue
- Build up effect with multiple passes at low flow
- Focus on guiding viewer's eye to key elements

### Detail Panel

#### Sharpening

**Amount**: Strength of sharpening (typically 40-80 for landscapes).

**Radius**: Size of sharpening halo (0.8-1.2 typical).

**Detail**: Fine vs. coarse detail emphasis (20-40 typical).

**Masking**: Constrains sharpening to edges (hold Alt/Option while adjusting to see mask).

**Technique**:
- View at 100% magnification
- Adjust Amount first
- Refine with Radius and Detail
- Use Masking to avoid sharpening smooth areas (sky, water)
- Sharpen conservatively; can add more later

#### Noise Reduction

**Luminance**: Reduces grayscale noise (typical range: 20-50 for high ISO).

**Color**: Reduces color noise (typical range: 25-50).

**Detail/Contrast**: Fine-tune noise reduction effect.

**Technique**:
- View at 100% magnification
- Adjust Luminance until noise is reduced but detail remains
- Adjust Color to remove color speckles
- Balance noise reduction against detail preservation
- Noise more visible in shadows and smooth areas

### Export Settings

**File Format**:
- **JPEG**: For web, social media, general sharing
- **TIFF**: For printing or further editing in Photoshop
- **DNG**: For archiving edited RAW files

**Quality**: 80-90 for JPEG (higher for printing).

**Color Space**:
- **sRGB**: For web and most uses
- **AdobeRGB**: For professional printing

**Resolution**: 300 PPI for printing, 72 PPI for web.

**Sharpening**: Output sharpening for screen or print.

---

## Photoshop Techniques

### When to Move to Photoshop

- Exposure blending (HDR)
- Focus stacking
- Advanced cloning and healing
- Luminosity masking
- Precise selections and adjustments
- Compositing (use ethically)

### Exposure Blending (Manual HDR)

**Purpose**: Combine multiple exposures to balance extreme contrast.

**Process**:
1. Open bracketed exposures as layers in Photoshop
2. Align layers (Edit → Auto-Align Layers)
3. Add layer masks to each layer
4. Paint with black/white brush to reveal/hide areas from each exposure
5. Blend exposures for natural result
6. Flatten and refine

**Advantages over HDR Software**:
- More natural results
- Complete control over blending
- Avoids HDR artifacts and halos

### Focus Stacking

**Purpose**: Combine multiple images focused at different distances for extreme depth of field.

**Process**:
1. Open focus-stacked images as layers
2. Select all layers
3. Edit → Auto-Align Layers
4. Edit → Auto-Blend Layers → Stack Images
5. Photoshop automatically creates masks
6. Flatten and refine

**Alternative Software**: Helicon Focus, Zerene Stacker (specialized focus stacking tools).

### Luminosity Masking

**Purpose**: Create selections based on tonal values for precise, natural adjustments.

**Concept**: Masks based on brightness allow adjustments that affect only specific tonal ranges (e.g., only brightest highlights or only darkest shadows).

**Process** (simplified):
1. Create luminosity mask (various techniques and panel plugins available)
2. Use mask to constrain adjustment layer
3. Make adjustments that affect only selected tonal range
4. Refine mask as needed

**Benefits**:
- Extremely natural results
- Precise tonal control
- No visible edges or transitions
- Professional-level refinement

**Learning Curve**: Steeper than basic techniques but powerful for advanced work.

### Dodging and Burning

**Purpose**: Selectively lighten (dodge) or darken (burn) areas to guide attention and add dimension.

**Technique**:
1. Create new layer set to Soft Light or Overlay blend mode
2. Paint with white brush to dodge (lighten)
3. Paint with black brush to burn (darken)
4. Use low opacity brush (10-20%) and build up effect
5. Adjust layer opacity for overall strength

**Targets**:
- Dodge: Main subjects, light-catching elements, areas to emphasize
- Burn: Edges, distracting elements, areas to subdue

### Content-Aware Tools

**Spot Healing Brush**: Remove small distractions (sensor dust, small branches).

**Clone Stamp**: Copy texture from one area to another (remove larger distractions).

**Content-Aware Fill**: Automatically fill selected area with surrounding texture.

**Patch Tool**: Select and replace area with texture from another area.

**Use Ethically**: Remove distractions, not fabricate major elements.

---

## Advanced Techniques

### Orton Effect

**Purpose**: Create soft, dreamy, glowing effect.

**Process**:
1. Duplicate layer
2. Apply Gaussian Blur (20-50 pixels)
3. Set blend mode to Soft Light or Overlay
4. Reduce opacity (20-40%)
5. Mask effect from areas that should remain sharp

**Use**: Subtle enhancement for ethereal mood, not heavy-handed effect.

### Panorama Stitching

**Lightroom**:
1. Select images to stitch
2. Photo → Photo Merge → Panorama
3. Adjust projection and boundary warp
4. Merge to create DNG file
5. Process as normal

**Photoshop**:
1. File → Automate → Photomerge
2. Select images and projection type
3. Photoshop stitches and creates layered file
4. Crop and flatten

**Shooting for Panoramas**:
- Overlap images by 30-50%
- Use manual exposure (consistent across frames)
- Use manual focus
- Use manual white balance
- Shoot in portrait orientation for more vertical coverage
- Use tripod and level

### Time Blending

**Purpose**: Combine images from different times (e.g., blue hour sky with golden hour foreground).

**Ethical Consideration**: Disclose if images are from significantly different times; some consider this compositing rather than photography.

**Process**: Similar to exposure blending—layer images and mask to reveal desired elements from each.

---

## Color Correction vs. Color Grading

### Color Correction

**Purpose**: Achieve accurate, neutral color representation.

**Process**:
- Remove color casts
- Balance white balance
- Ensure neutral tones are neutral
- Correct for lighting conditions

**Goal**: Natural, accurate color.

### Color Grading

**Purpose**: Creative color adjustments to establish mood and style.

**Process**:
- Add color tints to highlights/shadows
- Shift color relationships
- Create cohesive color palette
- Establish visual style

**Goal**: Artistic color expression.

**Approach**: Color correct first, then color grade creatively.

---

## Workflow Efficiency

### Develop Consistent Workflow

1. Import and organize
2. Cull and select
3. Apply lens corrections
4. Global adjustments (exposure, contrast, color)
5. Local adjustments (dodging, burning, selective enhancements)
6. Detail refinement (sharpening, noise reduction)
7. Final review
8. Export

**Benefits**:
- Faster processing
- Consistent results
- Less decision fatigue
- Easier to refine over time

### Presets and Profiles

**Presets**: Saved adjustment settings applied with one click.

**Use Cases**:
- Starting point for similar images
- Consistent look across series
- Speed up repetitive adjustments

**Caution**: Presets are starting points, not final solutions; always refine for specific image.

### Batch Processing

**Sync Settings**: Apply adjustments from one image to multiple similar images.

**Process**:
1. Adjust one image
2. Select similar images
3. Sync settings
4. Refine individual images as needed

**Use**: Images from same location/time with similar lighting.

---

## Final Review and Quality Control

### Review Checklist

- [ ] Exposure balanced (no clipped highlights or blocked shadows)?
- [ ] White balance natural and appropriate?
- [ ] Colors saturated but not oversaturated?
- [ ] Contrast appropriate for mood?
- [ ] Sharpness adequate at 100% view?
- [ ] Noise acceptable?
- [ ] Horizon level?
- [ ] Distractions removed or minimized?
- [ ] Dodging and burning subtle and effective?
- [ ] Overall appearance natural and believable?
- [ ] Image conveys intended mood and story?

### Common Issues

**Halos**: Caused by excessive clarity, dehaze, or HDR—reduce effect or mask from edges.

**Oversaturation**: Reduce vibrance/saturation globally or target specific colors in HSL.

**Unnatural Shadows**: Caused by lifting shadows too much—reduce shadow adjustment or add blacks.

**Noise in Shadows**: Caused by lifting underexposed shadows—apply noise reduction or reduce shadow lift.

**Soft Images**: Increase sharpening, check focus, ensure optimal aperture was used.

### Viewing Conditions

- View at multiple sizes (100%, fit to screen, thumbnail)
- View on calibrated monitor
- View on different devices (phone, tablet)
- View in different lighting conditions
- Take breaks and return with fresh eyes
- Seek feedback from trusted sources

---

## Ethical Considerations

### Acceptable Practices

- Adjusting exposure, contrast, color
- Removing sensor dust spots
- Removing small distractions (trash, small branches)
- Cropping and straightening
- Blending exposures from same scene
- Focus stacking

### Questionable Practices

- Significant sky replacements
- Adding elements not present
- Removing major elements
- Time blending from very different times
- Heavy manipulation that misrepresents scene

### Disclosure

- Disclose significant manipulations
- Be transparent in competitions and publications
- Consider context (fine art vs. documentary)
- Maintain personal integrity and standards
