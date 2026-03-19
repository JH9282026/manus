# Detailing and Texturing

Advanced techniques for surface detailing, PolyPaint workflows, and texture creation in ZBrush.

---

## PolyPaint Fundamentals

### What is PolyPaint?

PolyPaint is ZBrush's vertex color painting system that allows direct painting on the model surface without UV maps. Color information is stored per vertex, making it resolution-dependent on polygon density.

**Advantages:**
- No UV maps required initially
- Paint at any resolution
- Flexible workflow
- Can convert to texture maps later
- Non-destructive with layers

**Limitations:**
- Requires high polygon density for detail
- Color resolution tied to mesh resolution
- Larger file sizes with high-resolution color
- Must convert to textures for most external applications

### Setting Up PolyPaint

**Activation:**
1. Ensure model has sufficient polygon density (typically subdivision level 5-7)
2. Navigate to Tool > Polypaint
3. Enable "Colorize" button
4. Disable "Zadd" and "Zsub" (prevents accidental sculpting)
5. Enable "RGB" button in top toolbar
6. Set RGB Intensity to 100

**Interface Setup:**
- Color picker: Click color swatch in top toolbar
- RGB Intensity slider: Controls paint opacity
- Zadd/Zsub off: Prevents sculpting while painting
- RGB on: Enables color painting

### Basic PolyPaint Workflow

1. **Prepare Model:**
   - Subdivide to appropriate level (5-7 for detailed painting)
   - Ensure clean geometry
   - Organize with polygroups if needed

2. **Base Color Pass:**
   - Select Standard brush
   - Disable Zadd/Zsub, Enable RGB
   - Paint broad color areas
   - Use large brush size
   - Build up color gradually

3. **Detail Pass:**
   - Reduce brush size
   - Add color variation
   - Paint details (eyes, lips, markings)
   - Use masking for precision

4. **Refinement:**
   - Blend colors with low RGB Intensity
   - Add highlights and shadows
   - Use cavity masking for automatic variation
   - Final adjustments

---

## Advanced PolyPaint Techniques

### Layer-Based PolyPaint

**Creating Paint Layers:**
1. Tool > Layers > New Layer
2. Name layer descriptively ("Base Color", "Details", "Weathering")
3. Paint on active layer
4. Adjust layer intensity for blending
5. Toggle visibility to compare

**Layer Strategy:**
- **Base Color Layer:** Primary color blocking
- **Variation Layer:** Color variation and gradients
- **Detail Layer:** Fine details (eyes, markings, patterns)
- **Weathering Layer:** Dirt, wear, damage
- **Adjustment Layers:** Subtle color corrections

**Advantages:**
- Non-destructive workflow
- Easy iteration
- Intensity control
- Can delete unsuccessful attempts

### Custom Brushes for Painting

**Brush Settings for PolyPaint:**

**Standard Brush:**
- RGB Intensity: 100 for opaque, lower for transparent
- Focal Shift: Negative for soft edges, positive for hard
- Stroke: Dots, DragRect, or Spray
- Use for general painting

**Color Spray:**
- Spray stroke type with color variation
- Useful for organic texture
- Adjust spray settings for density

**Projection Brush:**
- Projects texture from Spotlight
- Useful for photo-realistic texturing
- Combine with masking for precision

**Creating Custom Paint Brushes:**
1. Select base brush (Standard, Clay, etc.)
2. Adjust settings (RGB Intensity, Focal Shift, Stroke)
3. Disable Zadd/Zsub
4. Enable RGB
5. Save as custom brush (Brush > Save As)

### Masking for Precision Painting

**Mask-Based Painting:**

**Isolate Areas:**
1. Mask areas to protect
2. Paint on unmasked areas
3. Prevents color bleeding
4. Useful for hard edges

**Mask by Cavity:**
1. Tool > Masking > Mask By Cavity
2. Adjust intensity slider
3. Masks recesses or peaks
4. Paint for automatic weathering/variation
5. Invert mask for opposite effect

**Mask by Polygroups:**
1. Ctrl+Shift+Click on polygroup
2. Masks other polygroups
3. Paint isolated area
4. Clean color separation

**Gradient Masking:**
1. Create gradient mask (MaskPen with low intensity)
2. Paint with mask for gradient color transitions
3. Blur mask (Ctrl+Click on mask) for smoother gradients

### Color Blending Techniques

**Smooth Color Transitions:**

**Low RGB Intensity:**
- Set RGB Intensity to 10-30
- Paint over color boundaries
- Gradually blends colors
- Build up slowly

**Smudge Technique:**
- Use Move brush with RGB enabled
- Low intensity
- Drag colors into each other
- Creates organic blending

**Spray Stroke:**
- Standard brush with Spray stroke
- Low RGB Intensity
- Spray colors over boundaries
- Organic, textured blending

**Color Modifiers:**
- Adjust Color > Modifiers in Brush palette
- Hue, Saturation, Value variation
- Creates dynamic color application
- Useful for organic variation

---

## Spotlight: Texture Projection

### Spotlight Fundamentals

Spotlight projects 2D images onto 3D models for painting and reference.

**Activation:**
1. Load texture (Texture palette > Import)
2. Enable Spotlight (Texture > Spotlight)
3. Spotlight appears on canvas
4. Position and scale with on-screen controls

**Spotlight Controls:**
- **Move:** Drag center circle
- **Scale:** Drag corner handles
- **Rotate:** Drag rotation handle
- **Opacity:** Adjust in Spotlight settings
- **Toggle Visibility:** Press Z key

### Spotlight Painting Workflow

**Projecting Textures:**

1. **Load Reference Image:**
   - Texture palette > Import
   - Select image file
   - Image loads into Spotlight

2. **Position Spotlight:**
   - Move and scale to align with model
   - Rotate as needed
   - Adjust opacity for visibility

3. **Paint Projection:**
   - Select Standard or Projection brush
   - Enable RGB, disable Zadd/Zsub
   - Paint on model
   - Projected texture paints onto surface

4. **Refine:**
   - Reposition Spotlight for different areas
   - Blend multiple projections
   - Adjust colors as needed

**Multiple Texture Projection:**
1. Project first texture
2. Load new texture (Texture > Import)
3. Spotlight updates with new texture
4. Position and project
5. Repeat for complex texturing
6. Blend projections with low RGB Intensity

### Spotlight Advanced Techniques

**Blending Modes:**
- Adjust in Spotlight settings
- Multiply, Add, Screen, Overlay
- Affects how projection interacts with existing color

**Opacity Control:**
- Spotlight Radius slider controls opacity
- Lower opacity for subtle projection
- Higher opacity for strong application

**Masking with Spotlight:**
1. Create mask on model
2. Project texture
3. Only unmasked areas receive projection
4. Precise texture placement

---

## Alpha-Based Detailing

### Using Alphas for Surface Detail

Alphas modulate brush intensity for pattern and texture application.

**Loading Alphas:**
- Alpha palette > Import
- Drag and drop onto Alpha palette
- Select from ZBrush alpha library

**Alpha Application Methods:**

**DragRect Stroke:**
1. Select Standard brush
2. Load alpha (Alpha palette)
3. Set Stroke to DragRect
4. Click and drag on model
5. Rectangle appears, release to apply
6. Adjust size and angle before releasing

**Standard Stroke:**
1. Select Standard brush
2. Load alpha
3. Set Stroke to Dots or DragDot
4. Paint on model
5. Alpha repeats with each stroke

**Spray Stroke:**
1. Select Standard brush
2. Load alpha
3. Set Stroke to Spray
4. Adjust Spray settings (Flow, Density)
5. Spray alpha pattern onto model
6. Organic, random distribution

### Creating Custom Alphas

**From Scratch:**
1. Create grayscale image in Photoshop/GIMP
2. White = raised (full intensity)
3. Black = recessed (no intensity)
4. Gray = mid-level (partial intensity)
5. Save as TIFF, PSD, or BMP
6. Import to Alpha palette

**From ZBrush Sculpt:**
1. Sculpt detail on flat plane
2. Frame detail in viewport
3. Alpha > Grab Doc
4. Captures viewport as alpha
5. Use on other models

**From Photos:**
1. Convert photo to grayscale
2. Adjust contrast for clarity
3. Ensure seamless tiling if needed
4. Import to Alpha palette
5. Use for realistic textures

### Alpha Techniques

**Seamless Tiling:**
- Use tileable alphas for large areas
- Avoid visible seams
- Adjust alpha offset in Alpha palette

**Alpha Intensity:**
- Adjust Z Intensity for depth control
- Lower intensity for subtle texture
- Higher intensity for pronounced detail

**Combining Alphas:**
1. Apply first alpha
2. Switch to different alpha
3. Apply in different areas or overlapping
4. Build complex textures from simple alphas

**Alpha with PolyPaint:**
1. Load alpha
2. Enable RGB, disable Zadd/Zsub
3. Paint with alpha
4. Creates textured color application
5. Useful for fabric patterns, scales, etc.

---

## Surface Noise and Texture

### Surface Noise Tool

Surface Noise adds procedural texture across entire model or masked areas.

**Activation:**
- Tool > Surface > Noise

**Noise Parameters:**

**Scale:** Controls texture size
- Low values = fine texture
- High values = large texture

**Strength:** Controls intensity
- Low values = subtle texture
- High values = pronounced texture

**Type:** Noise algorithm
- Various presets for different textures
- Experiment to find desired effect

**Applying Noise:**
1. Navigate to Tool > Surface > Noise
2. Adjust Scale and Strength sliders
3. Preview updates in real-time
4. Click "Apply to Mesh" when satisfied
5. Noise becomes permanent geometry

**Masked Noise:**
1. Mask areas to protect
2. Apply Surface Noise
3. Only unmasked areas receive noise
4. Useful for localized texture

**Noise with Layers:**
1. Create new layer
2. Apply Surface Noise
3. Adjust layer intensity
4. Non-destructive noise application

### Noise Strategies

**Skin Texture:**
- Low Scale (0.5-2)
- Low Strength (0.01-0.05)
- Apply at high subdivision level
- Combine with PolyPaint for realism

**Fabric Texture:**
- Medium Scale (5-15)
- Medium Strength (0.05-0.15)
- Use appropriate noise type
- Combine with alpha brushes for weave

**Stone/Rock Texture:**
- High Scale (20-50)
- High Strength (0.1-0.3)
- Multiple noise passes with different scales
- Combine with sculpting for realism

**Metal Wear:**
- Low Scale (1-5)
- Low Strength (0.01-0.05)
- Apply to masked areas (Mask by Cavity)
- Subtle surface variation

---

## Exporting Texture Maps

### Converting PolyPaint to Textures

**UV Mapping:**

PolyPaint requires UV coordinates to export as texture maps.

**Creating UVs:**
1. Tool > UV Map > Unwrap (automatic unwrapping)
2. Or use external UV tools (Maya, Blender, etc.)
3. Import UV-mapped model back to ZBrush
4. Project PolyPaint onto UV-mapped model

**Projection Workflow:**
1. Complete PolyPaint on high-resolution model (no UVs needed)
2. Create low-resolution model with clean UVs
3. Import low-res model as new SubTool
4. Tool > SubTool > Project All (projects PolyPaint from high-res to low-res)
5. Low-res model now has PolyPaint with UVs

**Exporting Texture Maps:**
1. Ensure model has UVs and PolyPaint
2. Tool > Texture Map > New From Polypaint
3. Set texture resolution (2048, 4096, 8192)
4. Click Create
5. Texture appears in Texture palette
6. Export texture (Texture > Export)
7. Save as PNG, TIFF, or PSD

### Multi-Channel Export

**Diffuse/Albedo Map:**
- PolyPaint color information
- Texture Map > New From Polypaint
- Base color for materials

**Normal Map:**
- Surface detail as normal information
- Tool > Normal Map > Create NormalMap
- Set resolution and options
- Captures sculpted detail for low-res models

**Displacement Map:**
- Geometric detail as height information
- Tool > Displacement > Create DispMap
- Higher resolution than normal maps
- Actual geometry displacement

**Ambient Occlusion:**
- Cavity shading information
- Tool > Masking > Mask By Cavity
- Convert mask to PolyPaint (Tool > Polypaint > Colorize)
- Export as texture
- Useful for material definition

**Cavity Map:**
- Similar to AO, emphasizes recesses
- Mask By Cavity with adjusted settings
- Export as texture
- Useful for weathering and wear

### Export Settings

**Texture Resolution:**
- **1024x1024:** Low-res, mobile, background assets
- **2048x2048:** Standard game assets
- **4096x4096:** Hero assets, close-up models
- **8192x8192:** Cinematic, extreme detail

**File Formats:**
- **PNG:** Lossless, good for most uses
- **TIFF:** Lossless, 16-bit support, large files
- **PSD:** Photoshop format, layer support
- **JPEG:** Lossy, smaller files, avoid for production

**Bit Depth:**
- **8-bit:** Standard, sufficient for most uses
- **16-bit:** Higher precision, larger files, useful for displacement

---

## Detailing Workflows

### Organic Detailing

**Skin Detailing:**

1. **Primary Forms (Subdivision 1-3):**
   - Major muscle groups
   - Bone landmarks
   - Overall proportions

2. **Secondary Forms (Subdivision 4-5):**
   - Muscle definition
   - Fat deposits
   - Major wrinkles and folds

3. **Tertiary Details (Subdivision 6-7):**
   - Fine wrinkles
   - Pores (Surface Noise or alpha brushes)
   - Skin texture
   - Veins and capillaries

4. **PolyPaint:**
   - Base skin tone
   - Color variation (red in cheeks, blue in shadows)
   - Subsurface scattering simulation
   - Details (lips, eyes, nails)

**Creature Detailing:**

1. **Scales/Skin Texture:**
   - Alpha brushes for scale patterns
   - DragRect for individual scales
   - Spray stroke for organic distribution
   - Vary scale size and orientation

2. **Surface Variation:**
   - Multiple alpha passes
   - Different scales in different areas
   - Smooth transitions between textures
   - Surface Noise for micro-detail

3. **Color Variation:**
   - Base color with PolyPaint
   - Mask by Cavity for automatic variation
   - Gradient color transitions
   - Patterns and markings

### Hard-Surface Detailing

**Mechanical Detailing:**

1. **Panel Definition:**
   - Mask panel boundaries
   - Inflate or deflate for raised/recessed panels
   - Trim Dynamic for clean cuts
   - Polish for flat surfaces

2. **Panel Lines:**
   - Dam Standard for recessed lines
   - Thin, consistent depth
   - Follow design logic
   - Connect to functional elements

3. **Greebles and Details:**
   - Small mechanical details
   - Alpha brushes for repeated elements
   - Boolean operations for complex shapes
   - Vary size and placement

4. **Wear and Damage:**
   - Mask by Cavity for edge wear
   - PolyPaint for rust, dirt, scratches
   - Subtle Surface Noise for metal texture
   - Asymmetric damage for realism

**Armor/Costume Detailing:**

1. **Fabric Texture:**
   - Alpha brushes for weave patterns
   - Surface Noise for subtle texture
   - Dam Standard for seams and stitching
   - Vary texture by material type

2. **Leather Texture:**
   - Alpha brushes for grain
   - Surface Noise for pores
   - Dam Standard for creases
   - PolyPaint for color variation

3. **Metal Elements:**
   - Polish for smooth metal surfaces
   - Dam Standard for engravings
   - Alpha brushes for decorative patterns
   - PolyPaint for oxidation and wear

---

## Troubleshooting Texture Issues

### PolyPaint Not Appearing

**Problem:** PolyPaint doesn't show on model

**Solutions:**
- Enable "Colorize" (Tool > Polypaint > Colorize)
- Check if RGB is enabled (top toolbar)
- Verify model has sufficient polygon density
- Ensure PolyPaint data exists (may have been deleted)
- Check material settings (some materials don't show color)

### Texture Export Issues

**Problem:** Texture map is blank or incorrect

**Solutions:**
- Verify model has UV coordinates
- Check UV layout (Tool > UV Map > Morph UV)
- Ensure PolyPaint is present on model
- Increase texture resolution
- Check for overlapping UVs

### Color Bleeding

**Problem:** Colors bleed into unwanted areas

**Solutions:**
- Use masking to isolate areas
- Reduce brush size
- Lower RGB Intensity for more control
- Increase polygon density for sharper color boundaries
- Use polygroups to separate areas

### Low Color Resolution

**Problem:** PolyPaint appears blocky or pixelated

**Solutions:**
- Increase subdivision level before painting
- Subdivide to level 6-7 for detailed painting
- Cannot add color resolution after painting (must repaint at higher resolution)
- Export at higher texture resolution when converting to maps
