# Green Screen Troubleshooting Guide

Comprehensive solutions for common chroma key challenges.

---

## Matte Quality Issues

### Holes in Subject Matte

**Symptoms**
- Transparent areas within subject
- Background visible through subject
- Inconsistent matte density

**Causes**
- Subject clothing/accessories matching screen color
- Over-aggressive keying settings
- Extreme green spill on subject
- Reflective surfaces on subject

**Solutions**
1. **Adjust Key Tolerance**: Reduce key strength/gain
2. **Multi-Pass Keying**: Use separate key for problem areas
3. **Rotoscoping**: Manually matte affected areas
4. **Wardrobe Change**: Avoid colors matching screen
5. **Matte Cleanup**: Use fill holes/despeckle tools

### Remaining Background in Matte

**Symptoms**
- Green/blue areas not fully transparent
- Patchy background removal
- Inconsistent keying across frame

**Causes**
- Uneven screen lighting
- Insufficient key strength
- Color variation in screen
- Shadows on screen

**Solutions**
1. **Increase Key Strength**: Adjust gain/tolerance settings
2. **Garbage Matte**: Mask out problem areas before keying
3. **Multi-Pass Keying**: Use multiple keys for different screen areas
4. **Screen Correction**: Color correct screen before keying
5. **Re-Light**: Improve screen lighting for future shoots

### Noisy/Grainy Matte

**Symptoms**
- Speckled appearance in matte
- Flickering edges across frames
- Inconsistent matte density

**Causes**
- High ISO footage
- Compression artifacts
- Poor lighting
- Low-quality camera

**Solutions**
1. **Noise Reduction**: Apply before keying
2. **Matte Cleanup**: Use despeckle/smooth tools
3. **Temporal Smoothing**: Average matte across frames
4. **Blur Matte**: Slight blur to reduce noise
5. **Re-Shoot**: Use lower ISO, better camera if possible

## Edge Quality Problems

### Green/Blue Fringing

**Symptoms**
- Colored halo around subject edges
- Unnatural color cast on subject outline
- Visible screen color on subject

**Causes**
- Insufficient spill suppression
- Green spill from screen reflection
- Subject too close to screen
- Excessive background lighting

**Solutions**
1. **Spill Suppression**: Apply dedicated spill removal
2. **Edge Color Correction**: Shift hue on edges
3. **Matte Choke**: Shrink matte slightly to eliminate fringe
4. **Increase Subject Distance**: Move subject further from screen
5. **Reduce Background Light**: Lower screen light intensity

### Jagged/Stair-Stepped Edges

**Symptoms**
- Pixelated edge appearance
- Visible steps along curves
- Harsh, unnatural edges

**Causes**
- Low-resolution footage
- Insufficient edge feathering
- Over-sharpened matte
- Aggressive matte choking

**Solutions**
1. **Edge Feathering**: Increase edge softness
2. **Matte Blur**: Apply subtle blur to edges only
3. **Higher Resolution**: Shoot at higher resolution
4. **Reduce Choke**: Less aggressive matte shrinking
5. **Anti-Aliasing**: Enable in keying software

### Chattering/Flickering Edges

**Symptoms**
- Edges change frame-to-frame
- Unstable matte over time
- Pulsing or breathing edges

**Causes**
- Inconsistent lighting
- Camera auto-settings changing
- Compression artifacts
- Motion blur variations

**Solutions**
1. **Temporal Smoothing**: Average key across frames
2. **Lock Camera Settings**: Disable auto-exposure, auto-white balance
3. **Consistent Lighting**: Ensure stable light output
4. **Higher Bitrate**: Use less compressed footage
5. **Frame-by-Frame Adjustment**: Manual refinement if necessary

### Thin/Disappearing Edges

**Symptoms**
- Subject appears smaller than actual
- Fine details lost (hair, fabric)
- Over-eroded matte

**Causes**
- Excessive matte choking
- Over-aggressive keying
- Insufficient edge preservation
- Poor lighting on subject edges

**Solutions**
1. **Reduce Choke**: Less matte shrinking
2. **Edge Preservation**: Use edge-aware keying tools
3. **Multi-Pass Keying**: Separate pass for fine detail
4. **Hair/Edge Lighting**: Improve backlighting on subject
5. **Matte Expansion**: Grow matte slightly to restore edges

## Lighting-Related Issues

### Uneven Screen Brightness

**Symptoms**
- Hotspots (overly bright areas)
- Dark patches on screen
- Inconsistent keying across frame

**Causes**
- Insufficient number of lights
- Poor light positioning
- Lights at different power levels
- Reflective screen material

**Solutions**
1. **Add More Lights**: Increase number for better coverage
2. **Reposition Lights**: Angle for even overlap
3. **Balance Light Output**: Use waveform monitor to match levels
4. **Diffusion**: Add diffusion to soften and spread light
5. **Screen Correction**: Color correct screen in post

### Shadows on Screen

**Symptoms**
- Dark areas behind subject
- Subject silhouette visible on screen
- Difficult keying in shadow areas

**Causes**
- Subject too close to screen
- Hard light sources
- Insufficient background lighting
- Subject blocking lights

**Solutions**
1. **Increase Distance**: Move subject 3-5 feet minimum from screen
2. **Soften Lights**: Use diffusion on background lights
3. **Add More Lights**: Eliminate shadow with additional sources
4. **Reposition Lights**: Angle to avoid subject blocking
5. **Raise Subject**: Use platform to separate from floor shadows

### Green Spill on Subject

**Symptoms**
- Green tint on subject edges
- Subject appears to glow green
- Transparency issues on subject

**Causes**
- Subject too close to screen
- Excessive background light
- Insufficient edge lighting on subject
- Reflective subject materials

**Solutions**
1. **Increase Distance**: Move subject further from screen
2. **Reduce Background Light**: Lower screen light intensity
3. **Add Edge Lighting**: Backlight and hair light on subject
4. **Spill Suppression**: Apply in post-production
5. **Wardrobe/Props**: Use matte, non-reflective materials

## Footage Quality Issues

### Motion Blur Problems

**Symptoms**
- Blurred edges difficult to key
- Ghosting around moving subjects
- Inconsistent edge quality during motion

**Causes**
- Slow shutter speed
- Fast subject movement
- Camera movement
- Insufficient lighting

**Solutions**
1. **Faster Shutter**: Use 1/250 or faster
2. **More Light**: Increase lighting to allow faster shutter
3. **Slow Movement**: Direct subject to move slower
4. **Stabilize Camera**: Use tripod or stabilization
5. **Edge Blur Matching**: Add blur to composite to match

### Compression Artifacts

**Symptoms**
- Blocky appearance in footage
- Color banding on screen
- Difficult keying with artifacts

**Causes**
- High compression codec (H.264, H.265)
- Low bitrate recording
- Multiple compression generations
- Camera limitations

**Solutions**
1. **Higher Bitrate**: Record at maximum quality
2. **Better Codec**: Use ProRes, DNxHD, or RAW
3. **Avoid Re-Compression**: Work with original files
4. **Noise Reduction**: Apply before keying
5. **Upgrade Camera**: Use camera with better codecs

### Color Space Issues

**Symptoms**
- Incorrect colors in composite
- Mismatch between subject and background
- Unexpected color shifts

**Causes**
- Mismatched color spaces
- Incorrect gamma settings
- Log footage not converted
- Monitor calibration issues

**Solutions**
1. **Color Space Management**: Set correct input/output spaces
2. **LUT Application**: Convert log to Rec.709 or appropriate space
3. **Monitor Calibration**: Use calibrated reference monitor
4. **Consistent Pipeline**: Maintain same color space throughout
5. **Color Matching**: Grade subject to match background

## Composite Integration Issues

### Subject Doesn't Match Background

**Symptoms**
- Subject appears pasted on
- Lighting doesn't match
- Color temperature mismatch
- Unrealistic integration

**Causes**
- Different lighting on subject vs. background
- Color temperature mismatch
- No shadows or reflections
- Depth of field mismatch

**Solutions**
1. **Color Grading**: Match subject to background plate
2. **Add Shadows**: Create artificial shadows
3. **Light Wrap**: Blend edges with background light
4. **Depth of Field**: Match blur between subject and background
5. **Atmospheric Effects**: Add haze, grain to match background

### Visible Matte Lines

**Symptoms**
- Hard line around subject
- Visible edge of matte
- Unnatural separation

**Causes**
- Insufficient edge feathering
- Matte too hard-edged
- No edge blending
- Incorrect composite order

**Solutions**
1. **Increase Feathering**: Soften matte edges
2. **Edge Blur**: Apply selective blur to edges
3. **Light Wrap**: Blend edges with background
4. **Matte Refinement**: Smooth and soften matte
5. **Composite Order**: Ensure correct layer stacking

### Subject Appears Flat

**Symptoms**
- No depth or dimension
- Subject looks 2D
- Doesn't integrate with background

**Causes**
- No shadows or reflections
- Lighting too flat
- No atmospheric perspective
- Missing depth cues

**Solutions**
1. **Add Shadows**: Create contact shadows, cast shadows
2. **Atmospheric Depth**: Add haze, reduce contrast for distance
3. **Color Grading**: Adjust for depth (cooler/less saturated for distance)
4. **Reflections**: Add if appropriate for scene
5. **Lighting Variation**: Add dimension with lighting adjustments

## Performance and Workflow Issues

### Slow Rendering

**Symptoms**
- Long render times
- Sluggish preview playback
- System resource exhaustion

**Causes**
- High-resolution footage
- Multiple keying passes
- Complex effect stack
- Insufficient hardware

**Solutions**
1. **Proxy Workflow**: Use lower-resolution proxies for editing
2. **Pre-Render**: Cache intermediate results
3. **Optimize Effects**: Disable unnecessary effects during preview
4. **Hardware Upgrade**: More RAM, faster GPU
5. **Simplify Composite**: Reduce number of layers/effects

### Inconsistent Results

**Symptoms**
- Key quality varies across shots
- Different settings needed for each clip
- Unpredictable results

**Causes**
- Inconsistent lighting between shots
- Camera settings changing
- Different screen conditions
- Varying subject distances

**Solutions**
1. **Standardize Setup**: Consistent lighting and camera settings
2. **Document Settings**: Record successful configurations
3. **Test Before Shooting**: Verify key quality before production
4. **Lock Camera Settings**: Disable auto-adjustments
5. **Consistent Distance**: Mark subject positions for consistency

## Emergency Fixes

### When Keying Completely Fails

**Last Resort Options**
1. **Rotoscoping**: Manual frame-by-frame masking
2. **Hybrid Approach**: Combine keying with rotoscoping
3. **AI-Assisted Tools**: Use machine learning-based masking
4. **Re-Shoot**: If possible, re-shoot with better setup
5. **Alternative Techniques**: Consider different compositing methods

### Quick Fixes for Tight Deadlines

**Acceptable Compromises**
1. **Aggressive Garbage Matte**: Eliminate problem areas
2. **Tighter Framing**: Crop to avoid difficult edges
3. **Motion Blur**: Add blur to hide edge issues
4. **Depth of Field**: Blur background to hide imperfections
5. **Creative Grading**: Use stylized look to mask problems