# Troubleshooting Quality Issues

Comprehensive guide to diagnosing and fixing common 3D printing quality problems including warping, adhesion, stringing, layer issues, and dimensional accuracy.

---

## Warping and Bed Adhesion

### Understanding Warping

Warping occurs when printed material cools unevenly, causing internal stresses that lift corners or edges from the build plate.

**Causes:**
- Uneven cooling (temperature gradients)
- Poor bed adhesion
- Material shrinkage during cooling
- Drafts or temperature fluctuations
- Large flat surfaces
- Incorrect bed temperature

**Materials Most Prone to Warping:**
- **High Risk:** ABS, ASA, Nylon, PC, Polypropylene
- **Medium Risk:** PETG
- **Low Risk:** PLA

### Preventing Warping

**Bed Temperature Optimization:**

| Material | Bed Temperature |
|----------|----------------|
| PLA | 50-60°C |
| PETG | 70-80°C |
| ABS | 95-110°C |
| ASA | 90-110°C |
| Nylon | 70-90°C |
| PC | 110-130°C |

**Bed Temperature Strategy:**
- Use higher temperature for first layer
- Reduce slightly after first 3-5 layers
- Example: ABS 110°C first layer, 100°C remaining

**Bed Adhesion Aids:**

**Glue Stick:**
- Apply thin, even layer to build surface
- Elmer's Disappearing Purple or UHU stic
- Reapply every 3-5 prints
- Easy cleanup with water

**Painter's Tape:**
- Blue painter's tape on glass bed
- Provides texture for adhesion
- Replace when worn
- Good for PLA

**Hairspray:**
- Light, even coat on bed
- Unscented varieties preferred
- Strong adhesion
- Cleanup with isopropyl alcohol

**Specialized Adhesives:**
- Magigoo, 3DLac, Dimafix
- Material-specific formulas
- Strong adhesion
- More expensive

**Build Surface Selection:**
- **Glass:** Smooth finish, requires adhesive
- **PEI Sheet:** Excellent adhesion, durable
- **Textured PEI:** Good adhesion, textured bottom
- **BuildTak:** Strong adhesion, wears over time

**Bed Leveling:**
- Properly leveled bed is critical
- First layer should be slightly squished
- Use paper test (slight drag)
- Auto bed leveling (ABL) recommended
- Re-level regularly

**Brim and Raft:**

**Brim:**
- Extra perimeters around first layer
- Increases contact area with bed
- Easy to remove
- Minimal material usage
- Recommended for most prints prone to warping

**Raft:**
- Thick platform printed under model
- Maximum adhesion
- More material usage
- Leaves texture on bottom
- Use for severe warping issues

**Configuration:**
- Brim width: 5-10mm (10-20 lines)
- Raft layers: 2-3 layers
- Enable in slicer settings

**Environmental Control:**

**Enclosure:**
- Maintains consistent temperature
- Blocks drafts
- Essential for ABS, ASA, Nylon
- DIY or commercial enclosures
- Keep doors closed during printing

**Room Temperature:**
- Stable 20-25°C
- Avoid air conditioning vents
- Avoid windows and drafts
- Consistent environment critical

**Part Cooling Fan:**
- Disable or minimize for first 3-5 layers
- Reduce fan speed for warp-prone materials
- ABS/ASA: 0-30% fan
- Nylon: 0-20% fan
- PLA: Can use 100% after first layer

**Design Modifications:**

**Chamfer Bottom Edges:**
- 45° chamfer on bottom corners
- Reduces sharp corners that lift
- Maintains functionality

**Mouse Ears:**
- Small discs at corners
- Increases adhesion at lift-prone areas
- Easy to remove after printing

**Split Large Prints:**
- Divide into smaller sections
- Reduces warping forces
- Assemble after printing

### Fixing Warped Prints

**Heat Gun Method:**
1. Heat warped area with heat gun (low setting)
2. Gently press flat against surface
3. Hold until cooled
4. Repeat if necessary
5. Risk of over-heating and deformation

**Boiling Water Method (PLA):**
1. Boil water
2. Submerge warped print for 10-30 seconds
3. Remove and reshape while soft
4. Hold shape until cooled
5. PLA softens at ~60°C

**Oven Method:**
1. Preheat oven to material's glass transition temperature
2. Place print on flat surface in oven
3. Heat for 5-10 minutes
4. Remove and flatten
5. Allow to cool completely
6. Risk of over-heating

---

## Stringing and Oozing

### Understanding Stringing

Stringing occurs when filament oozes from the nozzle during travel moves, creating thin strands between parts.

**Causes:**
- Insufficient retraction
- Nozzle temperature too high
- Slow travel speed
- Wet filament (moisture absorption)
- Material properties (PETG strings more than PLA)

### Eliminating Stringing

**Retraction Tuning:**

**Retraction Distance:**
- **Direct Drive:** 0.5-2mm
- **Bowden:** 4-8mm
- Increase by 0.5mm increments if stringing persists
- Too much causes under-extrusion and grinding

**Retraction Speed:**
- Typical: 25-45mm/s
- Faster retraction reduces oozing time
- Too fast causes filament grinding
- Material-specific:
  - PLA: 40mm/s
  - PETG: 25-35mm/s (slower, more viscous)
  - TPU: 20-30mm/s

**Retraction Test:**
1. Print retraction test model (towers with gaps)
2. Start with conservative settings
3. Increase distance if stringing persists
4. Adjust speed if grinding occurs
5. Find optimal balance

**Temperature Reduction:**

**Lower Nozzle Temperature:**
- Reduce by 5°C increments
- Test for stringing improvement
- Monitor for under-extrusion
- Don't go below material's minimum temperature

**Temperature Tower:**
1. Print temperature tower test
2. Evaluates multiple temperatures in one print
3. Identify optimal temperature for minimal stringing
4. Balance stringing, layer adhesion, and surface quality

**Travel Speed:**

**Increase Travel Speed:**
- Faster travel = less time for oozing
- Typical: 150-200mm/s
- Limited by printer's maximum speed
- Balance with acceleration to avoid ringing

**Minimize Travel Distance:**
- Enable "Avoid Crossing Perimeters" in slicer
- Reduces travel moves over open spaces
- Increases print time slightly
- Reduces stringing opportunities

**Z-Hop (Z-Lift):**

**Enable Z-Hop:**
- Lifts nozzle during travel moves
- Prevents nozzle dragging through strings
- Height: 0.2-0.5mm
- Increases print time
- Use if other methods insufficient

**Filament Drying:**

**Moisture Absorption:**
- Hygroscopic materials absorb moisture (Nylon, PETG, PLA)
- Moisture causes bubbling, oozing, stringing
- Reduces print quality and strength

**Drying Methods:**

**Filament Dryer:**
- Dedicated filament dryer (50-70°C)
- 4-8 hours drying time
- Most effective method

**Food Dehydrator:**
- Set to 50-60°C
- 4-6 hours
- Ensure filament fits

**Oven:**
- Low temperature (40-50°C)
- 4-6 hours
- Monitor closely to avoid melting
- Leave door slightly open

**Drying Temperatures:**
- PLA: 40-50°C
- PETG: 60-70°C
- Nylon: 70-80°C
- ABS: 60-70°C

**Material-Specific Tips:**

**PETG:**
- Strings more than PLA
- Lower temperature by 5-10°C
- Increase retraction distance
- Dry filament thoroughly

**TPU/Flexible:**
- Minimize retraction (can cause jams)
- Lower temperature
- Slow print speed
- Direct drive preferred

---

## Layer Adhesion Issues

### Understanding Layer Adhesion

Layers must bond properly for strong, functional prints. Poor adhesion causes weak parts that split along layer lines.

**Causes:**
- Nozzle temperature too low
- Insufficient cooling time between layers
- Print speed too fast
- Over-cooling (excessive fan)
- Contaminated filament
- Incorrect layer height

### Improving Layer Adhesion

**Temperature Optimization:**

**Increase Nozzle Temperature:**
- Higher temperature improves layer bonding
- Increase by 5°C increments
- Test for improved adhesion
- Monitor for stringing (balance required)

**Temperature Range Testing:**
- Print temperature tower
- Evaluate layer adhesion at each temperature
- Select temperature with best adhesion and quality

**Cooling Reduction:**

**Reduce Part Cooling Fan:**
- Excessive cooling prevents layer bonding
- Reduce fan speed by 10-20%
- Materials prone to poor adhesion:
  - ABS: 0-30% fan
  - ASA: 0-30% fan
  - Nylon: 0-20% fan
  - PETG: 30-50% fan

**Disable Fan for First Layers:**
- No fan for first 3-5 layers
- Gradually increase fan speed
- Improves bed adhesion and initial layer bonding

**Print Speed:**

**Reduce Print Speed:**
- Slower printing allows more time for layer bonding
- Reduce by 10-20mm/s
- Especially important for perimeters
- Balance with print time

**Layer Height:**

**Optimize Layer Height:**
- Layer height should be 25-75% of nozzle diameter
- Too thick layers reduce bonding surface area
- Thinner layers improve adhesion
- 0.2mm is standard for 0.4mm nozzle

**Extrusion Multiplier:**

**Calibrate Flow Rate:**
- Under-extrusion causes gaps between layers
- Calibrate extrusion multiplier (flow rate)
- Should be close to 100% (95-105%)
- Adjust if layers appear gapped or over-extruded

**Calibration Process:**
1. Print single-wall cube
2. Measure wall thickness with calipers
3. Calculate: (Expected / Actual) × Current Flow
4. Adjust flow rate in slicer
5. Re-test until accurate

---

## Surface Quality Issues

### Layer Lines and Roughness

**Causes:**
- Layer height too large
- Z-axis binding or wobble
- Inconsistent extrusion
- Vibrations

**Solutions:**

**Reduce Layer Height:**
- 0.1-0.15mm for smooth surfaces
- Increases print time
- Improves curves and details

**Mechanical Improvements:**
- Tighten loose belts
- Lubricate Z-axis lead screw
- Check for Z-axis wobble
- Ensure printer is on stable surface

**Post-Processing:**
- Sanding (start with 200 grit, progress to 800+)
- Filler primer and paint
- Acetone vapor smoothing (ABS only)
- Epoxy coating

### Ringing/Ghosting

Ripples or echoes around sharp corners and features.

**Causes:**
- Excessive print speed
- High acceleration/jerk
- Printer vibrations
- Loose belts or components

**Solutions:**

**Reduce Speed:**
- Lower print speed by 10-20mm/s
- Especially reduce perimeter speed

**Reduce Acceleration/Jerk:**
- Lower acceleration (500-1000mm/s²)
- Lower jerk (8-12mm/s)
- Smoother motion, less vibration

**Mechanical Improvements:**
- Tighten belts (should "twang" when plucked)
- Secure loose components
- Add dampening feet to printer
- Place printer on stable, heavy surface

**Input Shaping (Advanced):**
- Klipper firmware feature
- Compensates for printer resonance
- Requires accelerometer and calibration
- Dramatically reduces ringing

### Blobs and Zits

Small bumps or blobs on surface, often at layer start/end points.

**Causes:**
- Retraction settings
- Seam placement
- Over-extrusion
- Coasting/wipe settings

**Solutions:**

**Seam Placement:**
- Set seam position to "Rear" or "Random"
- "Aligned" creates visible seam line
- "Random" distributes artifacts
- Manually place seam on hidden edge

**Retraction Tuning:**
- Ensure proper retraction distance and speed
- Extra restart distance (negative value) can reduce blobs
- Typical: -0.1 to -0.2mm

**Coasting:**
- Stops extrusion slightly before layer end
- Reduces pressure in nozzle
- Minimizes blobs at seam
- Enable in slicer (0.2-0.5mm coasting distance)

**Wipe:**
- Moves nozzle along perimeter after layer end
- Wipes excess material
- Reduces visible seam
- Enable in slicer

---

## Dimensional Accuracy

### Oversized or Undersized Parts

**Causes:**
- Incorrect extrusion multiplier
- Elephant's foot (first layer squish)
- Material shrinkage
- Incorrect steps/mm calibration

**Solutions:**

**Calibrate Extrusion Multiplier:**
1. Print single-wall cube
2. Measure wall thickness
3. Calculate correction factor
4. Adjust flow rate
5. Re-test

**Elephant's Foot Compensation:**
- First layer spreads due to bed adhesion
- Enable "Elephant Foot Compensation" in slicer
- Typical value: 0.1-0.2mm
- Shrinks first layer slightly

**Horizontal Expansion/Shrinkage:**
- Slicer setting to compensate for material shrinkage
- Positive value shrinks part (for over-sized prints)
- Negative value expands part (for under-sized prints)
- Typical: -0.1 to +0.1mm

**Steps/mm Calibration:**
1. Mark filament 120mm from extruder
2. Extrude 100mm
3. Measure remaining distance
4. Calculate: (100 / Actual) × Current Steps
5. Update firmware with new steps/mm

### Holes Too Small or Too Large

**Causes:**
- Horizontal expansion
- Over-extrusion
- Hole orientation (vertical vs. horizontal)

**Solutions:**

**Horizontal Hole Expansion:**
- Enable "Hole Horizontal Expansion" in slicer
- Expands holes to compensate for shrinkage
- Typical: 0.05-0.1mm

**Design Compensation:**
- Design holes slightly larger than needed
- Test print and measure
- Adjust model dimensions
- Document compensation for future prints

**Drill/Ream After Printing:**
- Print holes slightly undersized
- Drill or ream to exact size
- Most accurate method for critical dimensions

---

## Under-Extrusion and Over-Extrusion

### Under-Extrusion

Insufficient material extruded, causing gaps and weak layers.

**Symptoms:**
- Gaps between perimeters
- Visible infill through walls
- Weak, brittle parts
- Inconsistent layers

**Causes:**
- Clogged nozzle
- Incorrect extrusion multiplier
- Filament diameter variation
- Extruder tension too low
- Nozzle temperature too low

**Solutions:**

**Clean or Replace Nozzle:**
- Heat nozzle to printing temperature
- Push filament through manually
- Use nozzle cleaning needle
- Cold pull method (heat, cool to ~90°C, pull)
- Replace nozzle if severely clogged

**Increase Extrusion Multiplier:**
- Increase flow rate by 2-5%
- Test print
- Adjust until gaps disappear

**Check Filament Diameter:**
- Measure filament with calipers
- Should be 1.75mm ± 0.05mm (or 2.85mm ± 0.1mm)
- Update slicer if diameter is incorrect
- Poor quality filament has inconsistent diameter

**Adjust Extruder Tension:**
- Too loose: filament slips, under-extrusion
- Too tight: filament grinds, under-extrusion
- Adjust tension screw
- Should grip firmly without deforming filament

**Increase Nozzle Temperature:**
- Low temperature causes high viscosity
- Increase by 5°C increments
- Monitor for stringing

### Over-Extrusion

Excessive material extruded, causing blobs, rough surfaces, and dimensional inaccuracy.

**Symptoms:**
- Blobs and bumps on surface
- Rough, over-filled top layers
- Dimensional inaccuracy (oversized)
- Stringing

**Causes:**
- Incorrect extrusion multiplier
- Nozzle temperature too high
- Filament diameter incorrect in slicer

**Solutions:**

**Decrease Extrusion Multiplier:**
- Reduce flow rate by 2-5%
- Test print
- Adjust until surface is smooth

**Reduce Nozzle Temperature:**
- High temperature reduces viscosity
- Decrease by 5°C increments
- Monitor for under-extrusion

**Verify Filament Diameter:**
- Ensure slicer has correct diameter (1.75mm or 2.85mm)
- Measure actual filament
- Update slicer if incorrect

---

## First Layer Issues

### First Layer Not Sticking

**Causes:**
- Bed not level
- Nozzle too far from bed
- Bed temperature too low
- Dirty bed surface
- Incorrect bed surface for material

**Solutions:**

**Level Bed:**
- Use paper test (slight drag)
- Auto bed leveling (ABL) if available
- Re-level regularly

**Adjust Z-Offset:**
- Lower nozzle closer to bed
- First layer should be slightly squished
- Adjust in 0.05mm increments
- Too close causes nozzle scraping

**Increase Bed Temperature:**
- See material-specific temperatures above
- Higher temperature improves adhesion

**Clean Bed:**
- Isopropyl alcohol (IPA) for most surfaces
- Soap and water for PEI
- Remove oils, dust, residue

**Use Adhesion Aids:**
- Glue stick, hairspray, or specialized adhesive
- See warping section above

### Elephant's Foot

First layer spreads outward, creating wider base.

**Causes:**
- Nozzle too close to bed
- Bed temperature too high
- First layer over-extrusion

**Solutions:**

**Increase Z-Offset:**
- Raise nozzle slightly (0.05mm increments)
- Reduces first layer squish

**Reduce Bed Temperature:**
- Lower by 5°C after first layer
- Reduces material softness

**Enable Elephant Foot Compensation:**
- Slicer setting shrinks first layer
- Typical: 0.1-0.2mm
- Compensates for spreading

**Reduce First Layer Extrusion:**
- Decrease first layer flow to 95-98%
- Reduces material volume

---

## Print Failure Mid-Print

### Layer Shifting

Layers misaligned, creating offset in print.

**Causes:**
- Loose belts
- Stepper motor skipping
- Mechanical obstruction
- Print speed too high
- Acceleration too high

**Solutions:**

**Tighten Belts:**
- Belts should be taut ("twang" when plucked)
- Not too tight (causes binding)

**Reduce Speed/Acceleration:**
- Lower print speed
- Reduce acceleration and jerk
- Prevents stepper skipping

**Check for Obstructions:**
- Ensure axes move freely
- Remove debris
- Lubricate if needed

**Increase Stepper Current:**
- If motors are skipping
- Adjust stepper driver current (advanced)
- Ensure adequate cooling for drivers

### Print Detaching from Bed

Print comes loose mid-print.

**Causes:**
- Poor bed adhesion (see first layer issues)
- Warping forces
- Bed temperature too low

**Solutions:**
- See warping and bed adhesion sections above
- Use brim or raft
- Increase bed temperature
- Use adhesion aids
- Ensure proper first layer

### Nozzle Clog

Filament stops extruding mid-print.

**Causes:**
- Debris in nozzle
- Heat creep (filament softening in heat break)
- Wet filament (moisture causes bubbles)
- Incorrect temperature

**Solutions:**

**Cold Pull:**
1. Heat nozzle to printing temperature
2. Push filament through
3. Cool to ~90°C (PLA) or ~140°C (ABS)
4. Pull filament out firmly
5. Debris should come out with filament
6. Repeat if necessary

**Atomic Pull (Similar to Cold Pull):**
1. Heat to printing temperature
2. Push filament through
3. Cool to ~100°C
4. Pull firmly
5. Clears partial clogs

**Nozzle Cleaning Needle:**
- Heat nozzle
- Insert cleaning needle from bottom
- Push debris through
- Use appropriate size needle

**Replace Nozzle:**
- If cleaning doesn't work
- Nozzles are inexpensive
- Keep spares on hand

**Prevent Heat Creep:**
- Ensure cooling fan for heat break is working
- Reduce print temperature if possible
- Check for heat break damage
