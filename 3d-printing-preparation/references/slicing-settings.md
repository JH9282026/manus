# Slicing Settings

Comprehensive guide to slicer configuration for optimal print quality, strength, and efficiency across layer height, infill, supports, temperature, and advanced settings.

---

## Layer Height Configuration

### Understanding Layer Height

Layer height is the thickness of each printed layer and the primary determinant of vertical resolution and print time.

**Impact on Print Quality:**
- **Thinner Layers (0.1-0.15mm):** Smoother surfaces, finer details, better curves, longer print time
- **Standard Layers (0.2mm):** Balanced quality and speed, most common
- **Thicker Layers (0.28-0.32mm):** Faster prints, visible layer lines, reduced detail

**Impact on Strength:**
- Thinner layers generally produce stronger parts
- Better layer adhesion due to more bonding surfaces
- Difference is modest (10-20% strength increase)

**Nozzle Diameter Relationship:**
- Layer height should be 25-75% of nozzle diameter
- **0.4mm nozzle:** 0.1-0.3mm layer height
- **0.6mm nozzle:** 0.15-0.45mm layer height
- **0.2mm nozzle:** 0.05-0.15mm layer height

### Layer Height Selection Guide

| Print Type | Layer Height | Reason |
|------------|--------------|--------|
| Miniatures, detailed models | 0.1-0.12mm | Maximum detail, smooth curves |
| Standard prints, prototypes | 0.2mm | Balanced quality and speed |
| Large functional parts | 0.24-0.28mm | Faster printing, adequate strength |
| Draft/test prints | 0.3-0.32mm | Maximum speed, quality not critical |
| Mechanical parts (strength) | 0.15-0.2mm | Good layer adhesion, adequate detail |

### Variable Layer Height

Modern slicers support adaptive layer height for optimized quality and speed.

**Concept:**
- Thinner layers on curved or detailed areas
- Thicker layers on flat or simple areas
- Balances quality and print time

**Configuration (PrusaSlicer/SuperSlicer):**
1. Enable "Variable Layer Height"
2. Set minimum and maximum layer heights
3. Adjust smoothing radius
4. Preview shows layer height variation
5. Manually adjust with layer height modifier tool

**Configuration (Cura):**
1. Enable "Adaptive Layers"
2. Set adaptive layer height variation
3. Set variation step size
4. Threshold angle determines where to vary

**Benefits:**
- 10-30% time savings vs. uniform thin layers
- Maintains quality on critical surfaces
- Automatic optimization

### First Layer Height

First layer is critical for bed adhesion.

**Standard Practice:**
- First layer height: 0.2-0.3mm (thicker than other layers)
- Improves adhesion by increasing contact area
- Compensates for bed leveling imperfections

**Configuration:**
- Set "First Layer Height" to 0.2mm or 100-150% of normal layer height
- Reduce first layer speed (20-30mm/s)
- Increase first layer extrusion (105-110%)

---

## Infill Configuration

### Infill Density

Infill density determines internal structure and affects strength, weight, and material usage.

**Density Guidelines:**

| Density | Use Case | Characteristics |
|---------|----------|----------------|
| 0% | Hollow decorative, vases | Minimal material, no internal structure |
| 5-10% | Decorative models | Light, minimal strength, fast |
| 15-25% | Standard functional parts | Good strength-to-weight ratio, most common |
| 30-50% | High-strength parts | Strong, heavier, more material |
| 60-80% | Maximum strength | Very strong, heavy, diminishing returns |
| 100% | Solid (rarely needed) | Maximum strength, very heavy, long print time |

**Diminishing Returns:**
- Beyond 25-30% infill, strength gains are minimal
- Increasing wall count (perimeters) is more effective for strength
- 3-5 perimeters + 20% infill often stronger than 2 perimeters + 50% infill

**Material Savings:**
- 15% infill uses ~40% less material than 100% infill
- 10% infill uses ~50% less material
- Significant cost and time savings

### Infill Patterns

Infill pattern affects strength, print time, and material usage.

**Common Patterns:**

**Grid/Rectilinear:**
- Perpendicular lines in alternating layers
- Fast to print (straight lines)
- Moderate strength in all directions
- Good general-purpose pattern

**Triangular/Tri-Hexagon:**
- Triangular pattern
- Strongest infill pattern (triangles are strongest shape)
- Slower to print (more direction changes)
- Best for parts under stress

**Honeycomb/Hexagon:**
- Hexagonal cells
- Excellent strength-to-weight ratio
- Slower to print (many direction changes)
- Good for lightweight strong parts

**Gyroid:**
- Wavy, organic pattern
- Uniform strength in all directions
- No straight lines (reduces shaking)
- Good for mechanical parts
- Slightly slower than grid

**Cubic/Cubic Subdivision:**
- 3D cubic pattern
- Uniform strength in all directions
- Efficient material usage
- Good for general use

**Concentric:**
- Follows perimeter shape
- Uniform strength around edges
- Good for flexible parts
- Faster than complex patterns

**Lightning:**
- Minimal infill, optimized for top surface support
- Extremely fast and material-efficient
- Minimal strength (decorative only)
- Good for large decorative prints

**Pattern Selection Guide:**

| Goal | Recommended Pattern |
|------|--------------------|
| Maximum strength | Triangular, Honeycomb |
| Balanced strength and speed | Grid, Gyroid |
| Fastest print | Lightning, Rectilinear |
| Flexible parts | Concentric, Grid |
| Uniform strength (all directions) | Gyroid, Cubic |
| Lightweight and strong | Honeycomb, Gyroid |

### Infill/Perimeter Overlap

Overlap between infill and perimeters affects strength and surface quality.

**Overlap Percentage:**
- Default: 15-25%
- Higher overlap: Better bonding, stronger parts, may show through on surface
- Lower overlap: Cleaner surface, weaker bonding

**Configuration:**
- "Infill/Perimeter Overlap" setting
- Adjust if infill is visible on surface (reduce) or parts are weak (increase)

---

## Shell Configuration

### Perimeters/Walls

Perimeters (walls, shells) are the outer layers of the print and have the greatest impact on strength.

**Perimeter Count:**
- **2 Perimeters:** Minimum for most prints, adequate for decorative
- **3 Perimeters:** Standard for functional parts, good strength
- **4-5 Perimeters:** High-strength parts, mechanical components
- **6+ Perimeters:** Extreme strength, approaching solid print

**Strength Impact:**
- Increasing perimeters has greater strength impact than increasing infill
- 4 perimeters + 15% infill often stronger than 2 perimeters + 50% infill
- Perimeters carry most of the load in functional parts

**Wall Thickness:**
- Total wall thickness = perimeter count × line width
- 3 perimeters × 0.4mm = 1.2mm wall thickness
- Design wall thickness as multiple of line width for optimal results

### Top and Bottom Layers

Solid layers on top and bottom of print.

**Layer Count:**
- **Top Layers:** 4-6 layers for 0.2mm layer height
- **Bottom Layers:** 3-5 layers
- More layers = stronger, smoother top surface
- Fewer layers = faster, may show infill pattern

**Thickness Calculation:**
- Top/bottom thickness = layer count × layer height
- 5 layers × 0.2mm = 1.0mm top thickness
- Adjust layer count when changing layer height

**Top Surface Quality:**
- More top layers = smoother surface
- Ironing feature can further smooth top surface
- Increase top layers if infill pattern is visible

---

## Temperature Settings

### Nozzle Temperature

Nozzle temperature affects extrusion quality, layer adhesion, and print speed.

**Material Temperature Ranges:**

| Material | Temperature Range | Typical |
|----------|------------------|--------|
| PLA | 180-220°C | 200-210°C |
| PETG | 220-250°C | 235-245°C |
| ABS | 220-250°C | 230-240°C |
| TPU/TPE | 210-230°C | 220°C |
| Nylon (PA) | 240-270°C | 250-260°C |
| ASA | 240-260°C | 245-255°C |
| PC (Polycarbonate) | 260-310°C | 280-290°C |

**Temperature Effects:**

**Too Low:**
- Under-extrusion (gaps, weak layers)
- Poor layer adhesion
- Nozzle clogs
- Rough surface

**Too High:**
- Over-extrusion (blobs, oozing)
- Stringing between parts
- Reduced detail
- Filament degradation (burning)

**Tuning Nozzle Temperature:**
1. Start at manufacturer's recommended temperature
2. Print temperature tower (test print with varying temps)
3. Evaluate each section for quality, stringing, layer adhesion
4. Select optimal temperature
5. Fine-tune ±5°C for specific prints

### Bed Temperature

Bed temperature ensures first layer adhesion and prevents warping.

**Material Bed Temperatures:**

| Material | Bed Temperature |
|----------|----------------|
| PLA | 50-60°C |
| PETG | 70-80°C |
| ABS | 95-110°C |
| TPU/TPE | 40-60°C |
| Nylon (PA) | 70-90°C |
| ASA | 90-110°C |
| PC | 110-130°C |

**Bed Temperature Effects:**

**Too Low:**
- Poor first layer adhesion
- Print detaches mid-print
- Warping (especially ABS, Nylon)

**Too High:**
- "Elephant's foot" (first layer spreads)
- Difficult print removal
- Excessive oozing

**Bed Temperature Strategy:**
- Higher temperature for first layer (improve adhesion)
- Reduce after first few layers (reduce warping, elephant's foot)
- Example: PLA 60°C first layer, 50°C remaining layers

---

## Speed Settings

### Print Speed

Print speed affects quality, strength, and print time.

**Speed Guidelines:**

| Speed | Use Case |
|-------|----------|
| 20-30mm/s | First layer, fine details, flexible materials |
| 40-60mm/s | Standard quality prints |
| 60-80mm/s | Balanced speed and quality |
| 80-100mm/s | Fast prints, quality compromise |
| 100-150mm/s | Speed-optimized printers, draft quality |

**Speed Effects:**

**Slower Speeds:**
- Better layer adhesion
- Smoother surfaces
- Improved detail
- Longer print time

**Faster Speeds:**
- Reduced layer adhesion (weaker parts)
- Visible artifacts (ringing, ghosting)
- Under-extrusion risk
- Shorter print time

**Feature-Specific Speeds:**

Modern slicers allow different speeds for different features:

- **First Layer:** 20-30mm/s (adhesion critical)
- **Perimeters:** 40-60mm/s (quality important)
- **Infill:** 60-100mm/s (quality less critical, can be faster)
- **Top Solid Layers:** 30-50mm/s (smooth surface)
- **Supports:** 50-80mm/s (quality not critical)
- **Travel Moves:** 150-200mm/s (non-printing moves)

### Acceleration and Jerk

Acceleration and jerk control how quickly the printer changes speed and direction.

**Acceleration:**
- Rate of speed change (mm/s²)
- Lower acceleration: Smoother motion, less vibration, slower
- Higher acceleration: Faster direction changes, more vibration
- Typical: 500-1500mm/s²

**Jerk:**
- Instantaneous speed change at corners (mm/s)
- Lower jerk: Smoother corners, less vibration
- Higher jerk: Faster corners, more ringing
- Typical: 8-15mm/s

**Tuning:**
- Reduce if ringing/ghosting is visible
- Increase for faster prints (quality compromise)
- Balance speed and quality

---

## Cooling Settings

### Part Cooling Fan

Part cooling fan cools the extruded plastic immediately after extrusion.

**Material-Specific Cooling:**

**PLA:**
- High cooling (80-100%)
- Improves overhangs and bridges
- Reduces stringing
- Enables sharper details

**PETG:**
- Moderate cooling (30-50%)
- Too much cooling reduces layer adhesion
- Balance between quality and strength

**ABS/ASA:**
- Minimal cooling (0-30%)
- High cooling causes warping and layer separation
- Use enclosure instead of fan

**TPU/Flexible:**
- Low to moderate cooling (20-40%)
- Helps with overhangs
- Too much cooling can cause under-extrusion

**Nylon:**
- Minimal to no cooling (0-20%)
- Prone to warping with cooling
- Use enclosure

**Cooling Strategy:**
- Disable fan for first 1-3 layers (improve bed adhesion)
- Gradually increase fan speed after first layers
- Maximum fan speed for overhangs and bridges
- Reduce fan speed for small layers (prevent over-cooling)

### Layer Time and Minimum Layer Time

Minimum layer time ensures each layer has time to cool before the next layer.

**Minimum Layer Time:**
- Default: 10-15 seconds
- Slicer slows down if layer prints faster than minimum time
- Prevents printing on insufficiently cooled layers
- Critical for small layers (tops of towers, small details)

**Configuration:**
- Set "Minimum Layer Time" to 10-15 seconds
- Enable "Slow Down if Layer Print Time is Below"
- Slicer automatically reduces speed for fast layers

---

## Retraction Settings

### Understanding Retraction

Retraction pulls filament back into the nozzle during travel moves to prevent oozing and stringing.

**Retraction Distance:**
- **Direct Drive:** 0.5-2mm
- **Bowden:** 4-8mm
- Longer Bowden tubes require more retraction

**Retraction Speed:**
- Typical: 25-45mm/s
- Too slow: Oozing occurs before retraction completes
- Too fast: Filament grinding, extruder skipping

**Retraction Effects:**

**Insufficient Retraction:**
- Stringing between parts
- Blobs and zits on surface
- Oozing during travel moves

**Excessive Retraction:**
- Filament grinding
- Under-extrusion after travel
- Nozzle clogs
- Extruder skipping

### Tuning Retraction

**Retraction Test:**
1. Print retraction test model (towers with gaps)
2. Start with conservative settings (Direct: 1mm, Bowden: 5mm)
3. Increase distance by 0.5mm increments if stringing persists
4. Reduce if under-extrusion or grinding occurs
5. Adjust speed if needed

**Material-Specific Retraction:**

**PLA:**
- Direct: 0.5-1.5mm
- Bowden: 4-6mm
- Speed: 40mm/s

**PETG:**
- Direct: 1-2mm
- Bowden: 5-7mm
- Speed: 25-35mm/s (slower, PETG strings easily)

**TPU/Flexible:**
- Direct: 0.5-1mm
- Bowden: Avoid if possible (flexible filament difficult in Bowden)
- Speed: 20-30mm/s

**ABS:**
- Direct: 0.5-1mm
- Bowden: 4-6mm
- Speed: 40mm/s

### Z-Hop (Z-Lift)

Z-hop raises the nozzle during travel moves to avoid collisions.

**When to Enable:**
- Prints with many travel moves
- Tall, thin features that nozzle might hit
- Reduces nozzle dragging across print

**Z-Hop Height:**
- Typical: 0.2-0.5mm
- Higher values increase print time
- Too low may not clear obstacles

**Drawbacks:**
- Increases print time (Z-axis moves are slow)
- Can cause blobs at Z-hop points
- Use only when necessary

---

## Advanced Settings

### Ironing

Ironing smooths top surfaces by running the nozzle over them with minimal extrusion.

**Effect:**
- Glass-smooth top surfaces
- Fills in gaps between top layer lines
- Improves aesthetic quality

**Configuration:**
- Enable "Ironing" for top surfaces
- Set ironing flow rate (10-20%)
- Set ironing speed (slower than normal, 20-30mm/s)
- Set ironing pattern (zig-zag or concentric)

**Drawbacks:**
- Increases print time (10-30% for top surfaces)
- May cause artifacts if settings are incorrect
- Not needed for functional parts

### Adaptive Layer Height

See "Variable Layer Height" section above.

### Sequential Printing (One at a Time)

Print multiple objects sequentially instead of layer-by-layer.

**Advantages:**
- If one print fails, others are unaffected
- Reduces oozing between objects
- Each object completes before next starts

**Disadvantages:**
- Requires sufficient Z-clearance (printhead must clear completed objects)
- Limits number of objects (collision risk)
- Longer time to first completed object

**Configuration:**
- Enable "Complete Individual Objects" or "Sequential Printing"
- Arrange objects with sufficient spacing
- Verify no collisions in preview

### Fuzzy Skin

Adds random texture to outer surface.

**Effect:**
- Matte, textured surface
- Hides layer lines
- Unique aesthetic

**Use Cases:**
- Artistic prints
- Organic models (rocks, terrain)
- Hiding print imperfections

**Configuration:**
- Enable "Fuzzy Skin"
- Set thickness (0.1-0.3mm)
- Set point distance (0.5-1mm)

---

## Profile Management

### Creating Custom Profiles

Save optimized settings for different scenarios.

**Profile Types:**
- **Quality Profiles:** 0.1mm layers, slow speeds, high detail
- **Speed Profiles:** 0.28mm layers, fast speeds, draft quality
- **Material Profiles:** Optimized for specific materials (PLA, PETG, etc.)
- **Printer Profiles:** Settings for specific printers

**Creating Profiles:**
1. Start with default profile
2. Adjust settings for specific use case
3. Test print and refine
4. Save as custom profile with descriptive name
5. Document settings and use cases

**Profile Organization:**
- Name profiles clearly ("PLA_Quality_0.12mm", "PETG_Fast_0.24mm")
- Organize by material, quality, or use case
- Export profiles for backup and sharing

### Slicer-Specific Tips

**PrusaSlicer/SuperSlicer:**
- Excellent default profiles
- Modifier meshes for local setting changes
- Variable layer height tool
- Extensive customization

**Cura:**
- User-friendly interface
- Extensive plugin ecosystem
- Good default profiles
- Adaptive layers feature

**Simplify3D:**
- Professional features
- Excellent support generation
- Process-based workflow
- Paid software

**OrcaSlicer:**
- Fork of PrusaSlicer with enhancements
- Improved UI
- Additional features
- Active development

---

## Troubleshooting Slicer Issues

### Preview Doesn't Match Print

**Problem:** Print doesn't look like slicer preview

**Solutions:**
- Verify correct printer profile selected
- Check nozzle diameter setting matches actual nozzle
- Ensure filament diameter is correct (1.75mm or 2.85mm)
- Calibrate extrusion multiplier (flow rate)

### Estimated Time Inaccurate

**Problem:** Print takes much longer or shorter than estimated

**Solutions:**
- Slicer estimates are approximations
- Actual time depends on acceleration, jerk, firmware
- Use slicer's time estimate as rough guide
- Track actual times for better future estimates

### Settings Not Applying

**Problem:** Changed settings don't affect print

**Solutions:**
- Re-slice after changing settings
- Check if setting is overridden by another profile
- Verify setting is supported by printer firmware
- Check for conflicting settings
