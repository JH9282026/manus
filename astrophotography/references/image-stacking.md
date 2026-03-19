# Image Stacking for Astrophotography

Stacking combines multiple exposures to dramatically improve image quality by increasing signal-to-noise ratio, revealing faint details, and removing artifacts. This guide covers calibration frames, stacking software, and complete workflow.

---

## Why Stacking Works

### Signal vs. Noise

**Signal**: Light from the celestial object—consistent across all frames.

**Noise**: Random variations from sensor noise, light pollution, atmospheric interference—varies between frames.

**Stacking Effect**:
- Signal adds linearly (doubles with 2 frames, triples with 3 frames, etc.)
- Noise averages out (random variations cancel)
- Signal-to-noise ratio (SNR) improves with square root of number of frames
- Example: 100 frames provides 10× better SNR than single frame

### Benefits of Multiple Short Exposures

**vs. Single Long Exposure**:
- Easier on mount tracking (shorter exposures more forgiving)
- Preserves star color (avoids clipping bright star cores)
- Allows rejection of bad frames (satellites, airplanes, clouds)
- Safer (equipment failure doesn't lose entire session)
- Enables dithering (removes artifacts)

**Total Integration Time**: Sum of all exposures—the critical factor for capturing faint objects.
- 60 × 2-minute exposures = 120 minutes total integration time
- More total time = more signal = fainter details visible

---

## Calibration Frames

Calibration frames remove unwanted artifacts and sensor characteristics from light frames, dramatically improving final image quality.

### Dark Frames

**Purpose**: Remove thermal noise, hot pixels, and amp glow from sensor.

**What They Capture**: Sensor noise pattern with no light input.

**How to Capture**:
1. Put lens cap on (or close telescope cover)
2. Use same exposure length as light frames
3. Use same ISO/gain as light frames
4. Use same temperature as light frames (important for cooled cameras)
5. Capture 20-50 dark frames

**When to Capture**: After imaging session (or before), at similar temperature.

**Master Dark**: Average of all dark frames—reduces noise in dark frame itself.

**Dark Library**: Some imagers create library of master darks at various exposure lengths and temperatures for reuse.

### Flat Frames

**Purpose**: Correct vignetting (darkening at edges), dust spots on sensor/optics, and uneven illumination.

**What They Capture**: Uniform illumination showing optical system's response.

**How to Capture**:

**Method 1: T-Shirt Method**
1. Stretch white t-shirt over telescope aperture
2. Point at bright, evenly-lit surface (sky, wall, light panel)
3. Use same focus and aperture as light frames
4. Adjust exposure for mid-range histogram (not too bright or dark)
5. Capture 20-50 flat frames

**Method 2: Twilight Sky**
1. Point at twilight sky (after sunset or before sunrise)
2. Use same focus and aperture as light frames
3. Adjust exposure for mid-range histogram
4. Capture 20-50 flat frames
5. Move telescope slightly between frames to average out stars

**Method 3: Light Panel**
1. Use dedicated flat field panel (electroluminescent panel)
2. Place over telescope aperture
3. Adjust brightness for mid-range histogram
4. Capture 20-50 flat frames

**Critical**: Flats must be taken with same focus, aperture, and optical configuration as light frames. Any change (focus, filter, camera rotation) requires new flats.

**Master Flat**: Average of all flat frames.

### Bias/Offset Frames

**Purpose**: Remove sensor readout noise (electronic noise from reading sensor data).

**What They Capture**: Sensor readout pattern with minimal exposure.

**How to Capture**:
1. Put lens cap on
2. Use shortest possible shutter speed (1/4000s or 1/8000s)
3. Use same ISO/gain as light frames
4. Temperature less critical than darks
5. Capture 50-100 bias frames

**When to Capture**: Anytime (can be reused across sessions if ISO unchanged).

**Master Bias**: Average of all bias frames.

### Dark Flat Frames (Optional)

**Purpose**: Remove thermal noise from flat frames.

**How to Capture**:
1. Put lens cap on
2. Use same exposure length as flat frames
3. Use same ISO/gain as flat frames
4. Capture 20-50 dark flat frames

**Usage**: Some workflows subtract dark flats from flat frames before using flats to calibrate light frames.

### Calibration Frame Summary

| Frame Type | Purpose | Exposure | ISO | Temperature | Quantity |
|------------|---------|----------|-----|-------------|----------|
| **Light** | Actual image | 30s-5min | 800-3200 | Ambient | 30-100+ |
| **Dark** | Remove thermal noise | Same as light | Same as light | Same as light | 20-50 |
| **Flat** | Correct vignetting/dust | Mid-range histogram | Same as light | Not critical | 20-50 |
| **Bias** | Remove readout noise | Shortest possible | Same as light | Not critical | 50-100 |
| **Dark Flat** | Remove noise from flats | Same as flat | Same as light | Not critical | 20-50 |

---

## Stacking Software Options

### DeepSkyStacker (DSS)

**Platform**: Windows (runs on Mac/Linux via Wine)

**Cost**: Free, open-source

**Best For**: Beginners, DSLR/mirrorless users, straightforward workflow

**Strengths**:
- User-friendly interface
- Excellent default settings
- Handles RAW files from most cameras
- Handles FITS files from astronomy cameras
- Automatic star detection and alignment
- Kappa-Sigma clipping for artifact rejection
- Produces high-quality stacked images

**Limitations**:
- Windows only (though Wine works)
- Less control than advanced software
- Slower than some alternatives
- Limited to single-session stacking (can combine multiple nights but less flexible)

### Astro Pixel Processor (APP)

**Platform**: Windows, Mac, Linux

**Cost**: Commercial (~$200 for full version, free trial available)

**Best For**: Intermediate to advanced users, comprehensive workflow

**Strengths**:
- Powerful, comprehensive workflow
- Excellent calibration and stacking
- Advanced features (gradient removal, star analysis, etc.)
- Multi-session integration
- Batch processing
- Regular updates

**Limitations**:
- Commercial software (cost)
- Steeper learning curve than DSS
- Can be overwhelming for beginners

### PixInsight

**Platform**: Windows, Mac, Linux

**Cost**: Commercial (~$300, free trial available)

**Best For**: Advanced users, maximum control, professional results

**Strengths**:
- Industry-standard for serious astrophotography
- Unparalleled control and flexibility
- Advanced calibration, stacking, and processing tools
- Scripting and automation
- Continuous development

**Limitations**:
- Steep learning curve (very complex)
- Expensive
- Overwhelming for beginners
- Requires significant time investment to master

### Sequator

**Platform**: Windows

**Cost**: Free

**Best For**: Star landscapes, Milky Way, tracked sky with foreground

**Strengths**:
- Simple, fast
- Excellent for star landscapes
- Aligns sky and foreground separately
- User-friendly

**Limitations**:
- Limited to specific use cases
- Not ideal for deep-sky objects
- Fewer calibration options

### Siril

**Platform**: Windows, Mac, Linux

**Cost**: Free, open-source

**Best For**: Users wanting free alternative to commercial software

**Strengths**:
- Free and open-source
- Comprehensive features
- Active development
- Cross-platform

**Limitations**:
- Steeper learning curve than DSS
- Less polished interface
- Smaller user community (less support/tutorials)

---

## DeepSkyStacker Workflow

### Step 1: Organize Files

Create folder structure:
```
Imaging_Session_2026-03-17/
├── Lights/
├── Darks/
├── Flats/
├── Bias/
└── Output/
```

Copy captured frames into appropriate folders.

### Step 2: Launch DeepSkyStacker

Open DeepSkyStacker application.

### Step 3: Load Light Frames

1. Click "Open picture files" button
2. Navigate to Lights folder
3. Select all light frames
4. Click "Open"
5. DSS displays list of light frames with thumbnails

**Review Light Frames**:
- Check "Score" column (DSS rates image quality)
- Uncheck poor-quality frames (low score, obvious issues)
- Verify exposure settings are correct

### Step 4: Load Calibration Frames

**Dark Frames**:
1. Click "Dark Files" button
2. Navigate to Darks folder
3. Select all dark frames
4. Click "Open"

**Flat Frames**:
1. Click "Flat Files" button
2. Navigate to Flats folder
3. Select all flat frames
4. Click "Open"

**Bias Frames**:
1. Click "Offset/Bias Files" button
2. Navigate to Bias folder
3. Select all bias frames
4. Click "Open"

**Dark Flat Frames** (if using):
1. Click "Dark Flat Files" button
2. Navigate to Dark Flats folder
3. Select all dark flat frames
4. Click "Open"

### Step 5: Check Settings

Click "Stacking Parameters" button.

**Recommended Settings Tab**:
- DSS provides recommended settings based on loaded files
- Review recommendations

**Stacking Mode**:
- **Kappa-Sigma Clipping (Kappa=2, Iterations=5)**: Recommended—rejects outliers (satellites, cosmic rays)
- **Median**: Alternative—more aggressive outlier rejection but can reduce detail
- **Average**: Simple average—no outlier rejection

**Light Frames**:
- "Stack after registering" selected
- "Create master dark" selected (if darks loaded)
- "Create master flat" selected (if flats loaded)
- "Create master offset" selected (if bias loaded)

**Advanced Settings** (usually leave as default):
- Star detection threshold
- Hot pixel detection
- Comet stacking (if imaging comet)

### Step 6: Register Frames

1. Click "Check all" to select all light frames
2. Click "Register checked pictures"
3. DSS analyzes each frame:
   - Detects stars
   - Measures star positions
   - Calculates alignment transformations
4. Progress bar shows registration progress (can take 10-30 minutes)

**Review Registration**:
- After registration, "Score" column updated
- "FWHM" column shows star sharpness (lower is better)
- Uncheck poorly registered frames

### Step 7: Stack Frames

1. Ensure desired frames are checked
2. Click "Stack checked pictures"
3. DSS performs stacking process:
   - Creates master dark, flat, bias (if loaded)
   - Calibrates each light frame (subtracts dark, divides by flat, subtracts bias)
   - Aligns calibrated frames
   - Combines frames using selected stacking mode
4. Progress bar shows stacking progress (can take 30 minutes to several hours)

**Output**:
- DSS displays stacked image
- Autosave file created (TIFF format) in same folder as light frames

### Step 8: Save Stacked Image

1. Review stacked image in DSS
2. File → Save picture to file
3. Choose format:
   - **TIFF (16-bit)**: Recommended—maximum data for processing
   - **FITS**: Alternative for use with astronomy software
4. Save to Output folder

**Initial Appearance**: Stacked image will appear dark and low-contrast—this is normal. Processing reveals the data.

---

## Advanced Stacking Concepts

### Registration Methods

**Star Detection**:
- DSS automatically detects stars in each frame
- Measures star positions
- Calculates transformation (translation, rotation, scaling) to align frames

**Comet/Asteroid Mode**:
- For moving objects (comets, asteroids)
- Aligns on moving object instead of stars
- Keeps object sharp while stars trail

### Stacking Algorithms

**Average**:
- Simple arithmetic mean of all frames
- No outlier rejection
- Fastest
- Suitable when no artifacts present

**Median**:
- Middle value of all frames at each pixel
- Excellent outlier rejection (removes satellites, airplanes, cosmic rays)
- Can reduce detail if too few frames
- Slower than average

**Kappa-Sigma Clipping**:
- Iteratively rejects outliers beyond threshold (Kappa value)
- Balances outlier rejection with detail preservation
- Recommended for most use cases
- Kappa=2, Iterations=5 typical

**Winsorized Sigma Clipping**:
- Similar to Kappa-Sigma but replaces outliers with clipped values
- Preserves more data than median
- Good for faint targets

### Dithering

**Purpose**: Slightly shift frame between exposures to randomize sensor artifacts (hot pixels, dust spots).

**Effect**: Artifacts appear in different locations across frames and are removed during stacking.

**Implementation**:
- Autoguiding software (PHD2) can dither automatically
- Camera controllers (ASIAIR) can dither
- Typical dither: 2-5 pixels

**Benefits**:
- Removes hot pixels without dark frames (though darks still recommended)
- Reduces impact of dust spots
- Improves final image quality

### Drizzle Integration

**Purpose**: Increase resolution of stacked image beyond native sensor resolution.

**Concept**: Uses sub-pixel shifts between dithered frames to reconstruct higher-resolution image.

**Availability**: PixInsight, some other advanced software.

**Requirements**: Dithered frames with sub-pixel shifts.

**Effect**: Can increase resolution by 1.5-2×, but also increases noise.

---

## Multi-Night Integration

### Combining Sessions

For faint targets, multiple nights of imaging may be required to achieve sufficient total integration time.

**Process**:
1. Stack each night's data separately (creates master light for each night)
2. Combine master lights from multiple nights
3. Align and stack master lights

**Software**:
- **DSS**: Can load master lights as light frames and stack
- **APP**: Excellent multi-session integration
- **PixInsight**: Advanced multi-session workflows

**Considerations**:
- Calibration frames should be from same night as light frames
- Target may shift slightly between nights (software handles this)
- Atmospheric conditions may vary (affects color balance)

---

## Troubleshooting Stacking Issues

| Issue | Likely Cause | Solution |
|-------|--------------|----------|
| Stacked image has star trails | Poor registration, tracking errors | Review light frames, discard frames with trails, improve tracking |
| Stacked image has dark edges | Frames not perfectly aligned | Crop edges in processing |
| Stacked image has artifacts (lines, patterns) | Calibration frame issues | Recapture calibration frames, ensure correct settings |
| Stacked image has vignetting | Flat frames not applied or incorrect | Verify flat frames loaded and correct |
| Stacked image has dust spots | Flat frames not applied or incorrect | Verify flat frames loaded and correct |
| Stacked image has color cast | Light pollution, processing needed | Normal—correct in processing |
| Stacking software crashes | Insufficient RAM, too many frames | Close other programs, stack in batches, upgrade RAM |
| Registration fails | No stars detected, poor image quality | Check focus, exposure, discard bad frames |

---

## Stacking Workflow Summary

### Capture Phase

1. Capture light frames (30-100+ frames)
2. Capture dark frames (20-50 frames, same settings as lights)
3. Capture flat frames (20-50 frames, same focus/aperture as lights)
4. Capture bias frames (50-100 frames, same ISO as lights)

### Pre-Stacking Phase

1. Organize files into folders (Lights, Darks, Flats, Bias)
2. Review light frames, discard obvious bad frames
3. Verify calibration frames are correct

### Stacking Phase (DSS)

1. Load light frames
2. Load calibration frames (darks, flats, bias)
3. Check settings (Kappa-Sigma clipping recommended)
4. Register frames
5. Review registration, uncheck poor frames
6. Stack frames
7. Save stacked image (16-bit TIFF)

### Post-Stacking Phase

1. Import stacked image into processing software (Photoshop, PixInsight)
2. Process image (levels, curves, color balance, etc.)
3. Export final image

---

## Calibration Frame Best Practices

### Dark Frames

- Capture at same temperature as light frames (critical for cooled cameras)
- Capture same exposure length as light frames
- Capture same ISO/gain as light frames
- Capture 20-50 frames (more is better)
- Can create master dark library for reuse (if temperature controlled)

### Flat Frames

- Capture with same focus as light frames (critical)
- Capture with same aperture as light frames
- Capture with same filter as light frames (if using filters)
- Exposure should produce mid-range histogram (not too bright or dark)
- Capture 20-50 frames
- Recapture if focus, aperture, or optical configuration changes

### Bias Frames

- Capture at same ISO/gain as light frames
- Use shortest possible shutter speed
- Temperature less critical than darks
- Capture 50-100 frames
- Can be reused across sessions if ISO unchanged

### Storage and Organization

- Organize by date and target
- Label clearly (date, target, frame type, settings)
- Keep calibration frames with corresponding light frames
- Back up all frames (before and after stacking)
