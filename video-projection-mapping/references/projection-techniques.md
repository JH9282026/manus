# Projection Techniques

Advanced calibration methods, multi-projector blending, optimization strategies, and troubleshooting for projection mapping.

## Spatial Calibration Techniques

### Manual Calibration

**Process**:
1. Project test pattern (grid, checkerboard, or high-contrast image)
2. In mapping software, create surface shape (quad, mesh, or Bezier)
3. Adjust corner points to match physical surface edges
4. Add control points along edges for curved surfaces
5. Warp mesh to align with surface features (windows, doors, architectural details)
6. Verify alignment with different test patterns

**Test Patterns**:
- **Grid**: Evenly spaced lines, easy to align with straight edges
- **Checkerboard**: High contrast, reveals warping and distortion
- **Crosshairs**: Precise alignment of specific points
- **Full White**: Check for brightness uniformity and hotspots
- **Full Black**: Verify ambient light control and contrast

**Tips**:
- Start with rough alignment, refine incrementally
- Use high-contrast test patterns for visibility
- Work from corners inward (establish boundaries first)
- Zoom in on software interface for precise adjustments
- Save calibration frequently (avoid losing work)

---

### Camera-Based Auto-Calibration

**Equipment**: Camera (DSLR, webcam, or smartphone), tripod

**Process (MadMapper 3D Scanner)**:
1. Mount camera near projector (same perspective if possible)
2. Project structured light patterns (MadMapper generates automatically)
3. Camera captures patterns on surface
4. Software analyzes images, calculates 3D geometry
5. Automatically generates mapping mesh
6. Fine-tune manually if needed

**Advantages**:
- Fast calibration for complex surfaces
- Accurate 3D geometry capture
- Reduces manual alignment time
- Repeatable (save calibration, reuse)

**Limitations**:
- Requires compatible software (MadMapper, Disguise)
- Camera quality affects accuracy
- Ambient light can interfere (darken room)
- May still need manual refinement

---

### Photogrammetry for Pre-Visualization

**Process**:
1. Photograph surface from multiple angles (20-100+ photos)
2. Use photogrammetry software (RealityCapture, Meshroom, Agisoft Metashape)
3. Software generates 3D model from photos
4. Import model into mapping software or 3D software (Blender, Cinema 4D)
5. Design content on virtual model
6. Export UV maps or projection angles for real installation

**Advantages**:
- Accurate 3D model for content design
- Pre-visualize before installation
- Design content remotely (no need to be on-site)
- Share model with team for collaboration

**Workflow**:
1. Capture photos on-site
2. Generate 3D model
3. Design content in 3D software
4. Test virtually
5. Export content and calibration data
6. Apply to real projection on-site

---

## Multi-Projector Techniques

### Edge Blending

**Purpose**: Seamlessly merge overlapping projector outputs into single, continuous image.

**Setup**:
1. Position projectors with 10-20% overlap
2. In software, define overlap zones
3. Apply blend curve (gamma ramp) to overlap areas
4. Adjust blend width to match physical overlap
5. Test with full-white content to verify seamless blend

**Blend Curves**:
- **Linear**: Simple fade, may show visible seam
- **Gamma**: Curved fade, smoother blend (most common)
- **Custom**: Adjust curve for specific projectors or surfaces

**Software Support**:
- Resolume Arena: Advanced Output > Edge Blend
- MadMapper: Multi-output with blend zones
- Smode: Built-in blending tools
- Disguise: Auto-blending with camera calibration

**Troubleshooting**:
- **Visible seam**: Adjust blend width or gamma curve
- **Bright band in overlap**: Reduce blend intensity or adjust curve
- **Color mismatch**: Calibrate projector color settings

---

### Color Matching

**Challenge**: Different projectors (even same model) have color variations.

**Solutions**:

**1. Use Identical Projectors**:
- Same make, model, and age
- Reduces color variation
- Still requires calibration

**2. Calibrate Projector Settings**:
- Match brightness, contrast, color temperature
- Use projector's built-in color modes (match across all units)
- Disable dynamic brightness or eco modes (causes variation)

**3. Software Color Correction**:
- Apply color correction to each projector output
- Adjust RGB levels, saturation, hue
- Use colorimeter for precise measurement (X-Rite i1Display, Datacolor SpyderX)
- Match to reference white point

**4. Use Media Server**:
- Professional media servers (Disguise, Green Hippo) have advanced color matching
- Measure each projector with colorimeter
- Software auto-corrects to match target color space

---

### Geometric Alignment

**Challenge**: Align multiple projectors to create seamless, continuous image.

**Manual Alignment**:
1. Project grid or test pattern from all projectors
2. Adjust each projector's position and warp to align grids
3. Ensure overlap zones match precisely
4. Verify with content (not just test pattern)

**Auto-Alignment** (Camera-Based):
1. Mount camera with view of all projectors
2. Software projects patterns, camera captures
3. Software calculates alignment, applies warping automatically
4. Available in Disguise, Scalable Display Technologies, NestMap

**Pixel-Perfect Alignment**:
- Use high-resolution test patterns (1-pixel lines)
- Zoom in on overlap zones
- Adjust warp points for sub-pixel accuracy
- Critical for text or fine details

---

### Stacking (Brightness Boost)

**Purpose**: Increase brightness by overlaying multiple projectors on same area.

**Setup**:
1. Position 2+ projectors to project identical image on same surface
2. Align perfectly (pixel-perfect if possible)
3. Ensure identical content and timing
4. Brightness adds (2 projectors = ~2x brightness)

**Use Cases**:
- Outdoor projections (combat ambient light)
- Large surfaces requiring high brightness
- When single projector insufficient

**Challenges**:
- Requires precise alignment (misalignment creates ghosting)
- Color matching critical (mismatch creates color fringing)
- Synchronization needed (avoid flicker or tearing)

---

## Optimization Strategies

### Content Optimization

**Resolution**:
- Match projector native resolution (1920x1080, 1920x1200, 4K)
- Avoid upscaling (reduces quality, increases processing)
- Downscale high-res content if computer struggles

**Codec**:
- **H.264 (MP4)**: Universal compatibility, moderate performance
- **HAP Codec**: Optimized for real-time playback, low CPU usage (requires QuickTime)
- **Image Sequences**: Maximum flexibility, high disk usage
- **ProRes / DNxHD**: High quality, large file size, good for editing

**Frame Rate**:
- 30 fps: Standard, good balance
- 60 fps: Smooth motion, higher processing demand
- 24 fps: Cinematic, lower processing (acceptable for some content)

**Compression**:
- Balance quality and file size
- Higher bitrate = better quality, larger files
- Test on playback system to ensure smooth performance

---

### Hardware Optimization

**GPU**:
- Dedicated GPU essential (NVIDIA RTX, AMD Radeon)
- More VRAM for higher resolutions and effects (8GB+ recommended)
- Multiple GPUs for multi-output setups

**CPU**:
- Multi-core processor (i7, i9, Ryzen 7, Ryzen 9)
- Higher clock speed for real-time processing

**RAM**:
- 16GB minimum, 32GB+ recommended
- More RAM for complex projects, multiple layers, effects

**Storage**:
- SSD for content (faster read speeds)
- NVMe SSD for best performance
- Sufficient space for high-res content (4K video = large files)

**Cooling**:
- Adequate cooling for sustained performance
- Avoid thermal throttling (reduces performance)
- Consider external cooling for laptops

---

### Software Settings

**Reduce Effects**:
- Disable unnecessary effects (each adds processing load)
- Use simpler effects (blur vs. complex shader)
- Limit layers (fewer layers = better performance)

**Lower Resolution**:
- Reduce output resolution if frame rate drops
- 1280x720 acceptable for some applications
- Test to find balance between quality and performance

**Adjust Buffer Settings**:
- Increase buffer for smoother playback (adds latency)
- Decrease buffer for lower latency (may cause stuttering)
- Balance based on use case (live performance vs. installation)

**Disable Preview**:
- Disable software preview window (reduces processing)
- Output only to projector, not computer screen

---

## Brightness and Contrast Optimization

### Calculating Required Lumens

**Formula**: Lumens = (Surface Area in sq ft × Ambient Light Factor × Desired Brightness) / Projector Efficiency

**Ambient Light Factors**:
- **Dark room**: 10-15 lumens per sq ft
- **Dim room**: 20-30 lumens per sq ft
- **Moderate light**: 40-60 lumens per sq ft
- **Bright room / Outdoor dusk**: 80-120 lumens per sq ft
- **Daylight / Outdoor**: 150-300+ lumens per sq ft

**Example**:
- Surface: 20 ft wide × 15 ft tall = 300 sq ft
- Ambient: Dim room (25 lumens/sq ft)
- Required: 300 × 25 = 7,500 lumens

**Tips**:
- Overestimate lumens (better too bright than too dim)
- Consider projector age (brightness decreases over time)
- Account for throw distance (brightness decreases with distance)

---

### Maximizing Contrast

**Control Ambient Light**:
- Darken room (blackout curtains, turn off lights)
- Schedule projection for nighttime (outdoor)
- Use baffles or flags to block stray light

**Projector Settings**:
- Use "Bright" or "Presentation" mode (higher brightness)
- Disable eco mode (reduces brightness)
- Adjust contrast and brightness settings
- Use "Dynamic" iris if available (adjusts per frame)

**Content Design**:
- Use high-contrast visuals (bright colors on dark backgrounds)
- Avoid subtle gradients (lost in ambient light)
- Bold, graphic designs read better than detailed images

**Surface**:
- White or light-colored surfaces reflect more light
- Matte surfaces reduce hotspots (avoid glossy)
- Consider projection screen material for best results

---

## Throw Distance and Lens Selection

### Throw Ratio

**Definition**: Ratio of throw distance to image width.

**Formula**: Throw Ratio = Distance / Width

**Example**: Projector 20 feet from 10-foot wide surface = 20/10 = 2:1 throw ratio

**Throw Ratio Categories**:
- **Ultra-Short Throw**: 0.4:1 or less (very close to surface)
- **Short Throw**: 0.5:1 to 1:1 (close to surface)
- **Standard Throw**: 1.2:1 to 2:1 (moderate distance)
- **Long Throw**: 2:1 to 4:1 (far from surface)
- **Ultra-Long Throw**: 4:1+ (very far from surface)

### Calculating Throw Distance

**Formula**: Distance = Throw Ratio × Width

**Example**: 1.5:1 throw ratio, 15-foot wide surface = 1.5 × 15 = 22.5 feet

**Zoom Lenses**:
- Variable throw ratio (e.g., 1.4-2.2:1)
- Flexibility in placement
- Calculate min and max distances

**Lens Shift**:
- Vertical or horizontal shift without moving projector
- Reduces keystone distortion
- Allows off-center placement

---

### Keystone Correction

**Cause**: Projector not perpendicular to surface (angled up, down, or sideways).

**Effect**: Image appears trapezoidal (wider at top or bottom).

**Solutions**:

**1. Physical Adjustment** (Best):
- Reposition projector to be perpendicular
- Use lens shift if available
- Minimizes image quality loss

**2. Optical Keystone Correction**:
- Adjust projector's built-in keystone settings
- Moderate quality loss
- Limited correction range

**3. Software Keystone Correction**:
- Warp image in mapping software
- Flexible, precise control
- Quality loss from pixel remapping
- Use sparingly (minimize distortion)

**Best Practice**: Minimize keystone correction through proper projector placement.

---

## Troubleshooting Common Issues

### Alignment Drift

**Symptoms**: Calibration shifts over time, content no longer aligns.

**Causes**:
- Projector heat expansion (lens shifts as it warms)
- Vibration or movement (unstable mounting)
- Zoom or focus drift (lens creep)

**Solutions**:
- Allow projector warm-up (30-60 min) before final calibration
- Secure mounting (eliminate vibration)
- Lock zoom and focus rings (tape or mechanical lock)
- Recalibrate if drift occurs
- Use projectors with minimal heat drift (professional models)

---

### Hotspots and Uneven Brightness

**Symptoms**: Bright spot in center, darker edges.

**Causes**:
- Projector optics (inherent to some models)
- Surface angle (not perpendicular to projector)
- Surface texture (reflective or uneven)

**Solutions**:
- Choose projector with even brightness distribution
- Adjust projector angle (more perpendicular)
- Use multiple projectors to even out brightness
- Compensate in content (darken center, brighten edges)
- Apply brightness correction in software (gradient mask)

---

### Flickering or Tearing

**Symptoms**: Image flickers, horizontal lines, stuttering.

**Causes**:
- Frame rate mismatch (content vs. projector)
- Cable issues (poor connection, long run)
- GPU settings (V-sync, refresh rate)

**Solutions**:
- Match content frame rate to projector refresh rate
- Use high-quality cables (certified HDMI, active cables for long runs)
- Enable V-sync in software or GPU settings
- Use signal booster for long cable runs (50+ feet)
- Check GPU output settings (resolution, refresh rate)

---

### Color Banding or Artifacts

**Symptoms**: Visible bands in gradients, compression artifacts.

**Causes**:
- Low bitrate content (over-compressed)
- 8-bit color depth (vs. 10-bit)
- Projector color processing

**Solutions**:
- Use higher bitrate content (less compression)
- Export in 10-bit color if supported
- Avoid subtle gradients (use dithering or noise)
- Adjust projector color settings
- Use higher quality codec (ProRes, HAP)

---

### Ambient Light Washout

**Symptoms**: Image appears washed out, low contrast.

**Causes**:
- Insufficient projector brightness
- Excessive ambient light
- Poor surface reflectivity

**Solutions**:
- Increase projector lumens (brighter projector or multiple projectors)
- Control ambient light (darken room, schedule for night)
- Use high-contrast content (bold colors, avoid pastels)
- Improve surface (white, matte, or projection screen material)
- Stack projectors for brightness boost

---

## Advanced Techniques

### Projection on Reflective or Transparent Surfaces

**Challenges**: Glass, mirrors, water reflect or transmit light unpredictably.

**Techniques**:
- **Rear Projection**: Project from behind translucent surface (frosted glass, screen)
- **Polarized Projection**: Use polarizing filters to control reflections
- **Content Design**: Embrace reflections as part of aesthetic
- **Surface Treatment**: Apply coating to make surface more suitable (frosted spray, projection film)

---

### Projection on Moving Surfaces

**Challenges**: Surface moves, calibration becomes invalid.

**Techniques**:
- **Tracking**: Use camera or sensors to track surface movement
- **Real-Time Adjustment**: Software adjusts mapping in real-time (TouchDesigner, custom systems)
- **Predictable Movement**: If movement is repeatable, pre-program mapping changes
- **Projection on Performers**: Track dancers or actors, project onto them

**Software**: TouchDesigner, Isadora, custom Max/MSP patches

---

### 360° Projection (Domes, Cylinders)

**Setup**:
- Multiple projectors arranged in circle or dome
- Blend edges for seamless 360° image
- Fisheye lenses for dome projection (single projector)

**Content**:
- Equirectangular format (360° video)
- Unwrap and map to dome or cylinder geometry
- Software: Smode, TouchDesigner, specialized dome software (Fulldome.pro)

**Calibration**:
- Auto-calibration with camera (Disguise, Scalable Display)
- Manual warping for each projector
- Blend zones critical for seamless experience

---

### Projection Mapping on Water

**Challenges**: Water surface moves, absorbs light, creates reflections.

**Techniques**:
- Use high-lumen projectors (water absorbs light)
- Project on water features (fountains, waterfalls) for dynamic effects
- Embrace movement (design content that works with ripples)
- Use fog or mist as projection surface (volumetric projection)

**Examples**: Fountain shows, water screens, fog projections

---

## Safety and Best Practices

### Electrical Safety
- Use proper power distribution (avoid overloading circuits)
- Ground all equipment
- Use surge protectors
- Weatherproof connections for outdoor use
- Hire licensed electrician for complex setups

### Projector Safety
- Never look directly into projector lens (eye damage)
- Secure projectors overhead (safety cables, proper rigging)
- Ensure adequate ventilation (prevent overheating)
- Follow manufacturer weight limits for mounts

### Site Safety
- Secure cables (tape down, use cable covers to prevent tripping)
- Mark hazards (dark areas, steps, obstacles)
- Provide adequate lighting for crew (work lights, not affecting projection)
- Follow venue safety regulations

### Permits and Permissions
- Obtain permits for public projections (buildings, monuments)
- Get permission from property owners
- Coordinate with local authorities (police, fire department)
- Ensure compliance with noise ordinances (if using audio)

---

## Projection Mapping Checklist

**Pre-Production**:
- [ ] Site survey (measurements, photos, ambient light)
- [ ] Calculate throw distance and required lumens
- [ ] Select projector(s) and software
- [ ] Plan content (design, format, resolution)
- [ ] Obtain permits and permissions

**Installation**:
- [ ] Mount projector(s) securely
- [ ] Connect all cables and power
- [ ] Configure computer display settings
- [ ] Test projector output

**Calibration**:
- [ ] Project test pattern
- [ ] Create mapping surfaces in software
- [ ] Align and warp to match physical surface
- [ ] Blend edges (multi-projector)
- [ ] Color match projectors
- [ ] Save calibration

**Content and Playback**:
- [ ] Import content into software
- [ ] Assign content to surfaces
- [ ] Test playback (frame rate, quality)
- [ ] Program timeline or cues
- [ ] Rehearse (if live performance)

**Final Checks**:
- [ ] Verify alignment and brightness
- [ ] Test all control systems (MIDI, OSC, timecode)
- [ ] Prepare backup systems (spare projector, computer)
- [ ] Document setup (photos, notes, calibration files)
- [ ] Run full show/installation test
