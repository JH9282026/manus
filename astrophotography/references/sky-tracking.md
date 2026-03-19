# Sky Tracking for Astrophotography

Accurate tracking is essential for astrophotography, allowing long exposures without star trails. This guide covers polar alignment, tracking mount operation, autoguiding, and troubleshooting tracking issues.

---

## Understanding Celestial Motion

### Earth's Rotation

Earth rotates 360 degrees in approximately 24 hours, or 15 degrees per hour (0.25 degrees per minute, 15 arc-seconds per second).

**Effect on Astrophotography**:
- Stars appear to move across the sky from east to west
- Without tracking, stars create trails in exposures longer than a few seconds
- Longer focal lengths show star trailing more quickly

**Rule of 500** (approximate maximum untracked exposure):
- Maximum exposure (seconds) = 500 ÷ focal length (mm)
- Example: 50mm lens = 500 ÷ 50 = 10 seconds maximum
- Example: 200mm lens = 500 ÷ 200 = 2.5 seconds maximum
- Modern high-resolution sensors may require "Rule of 300" for pixel-level sharpness

### Equatorial Coordinates

Celestial objects are located using equatorial coordinates:
- **Right Ascension (RA)**: East-west position (measured in hours, minutes, seconds)
- **Declination (DEC)**: North-south position (measured in degrees, arc-minutes, arc-seconds)

**Celestial Poles**:
- **North Celestial Pole (NCP)**: Point in sky directly above Earth's North Pole (near Polaris)
- **South Celestial Pole (SCP)**: Point in sky directly above Earth's South Pole (no bright star)

**Equatorial Mounts**: Aligned with celestial poles, allowing single-axis tracking to follow stars.

---

## Polar Alignment

### Why Polar Alignment is Critical

Polar alignment is the process of aligning the mount's rotational axis with Earth's rotational axis (pointing at the celestial pole).

**Perfect Polar Alignment**:
- Mount's RA axis points exactly at celestial pole
- Tracking requires only RA axis rotation (no DEC drift)
- Stars remain centered in frame during long exposures

**Poor Polar Alignment**:
- Stars drift in DEC axis during exposure
- Creates elongated stars (field rotation)
- Limits maximum exposure length
- Autoguiding can compensate but not eliminate

**Accuracy Requirements**:
- **Wide-field (lenses up to 200mm)**: ±5 degrees acceptable
- **Medium focal length (200-600mm)**: ±1-2 degrees
- **Long focal length (600mm+)**: Arc-minute precision required
- **Extreme focal length (1000mm+)**: Arc-second precision (drift alignment or autoguiding essential)

### Rough Polar Alignment (Northern Hemisphere)

**Quick Method for Wide-Field Imaging**:

1. **Level Tripod**: Use bubble level to ensure tripod is level
2. **Set Latitude**: Adjust mount's latitude setting to match your location's latitude
3. **Point North**: Aim mount's polar axis toward Polaris (North Star)
4. **Rough Alignment**: Polaris should be visible in polar scope or roughly aligned

**Accuracy**: ±5 degrees—sufficient for short focal lengths and exposures under 1-2 minutes.

### Polar Scope Alignment

**Equipment**: Built-in polar scope in mount.

**Process**:

1. **Level Mount**: Ensure tripod is level
2. **Set Latitude**: Adjust mount's latitude to your location
3. **Illuminate Reticle**: Use red LED illuminator (preserves night vision)
4. **Locate Polaris**: Look through polar scope
5. **Position Polaris**: Adjust mount's azimuth (left-right) and altitude (up-down) to place Polaris in correct position on reticle
   - Reticle shows Polaris position relative to true NCP
   - Use planetarium app to determine Polaris position for current date/time
6. **Verify**: Polaris should be in correct position on reticle pattern

**Accuracy**: ±10-30 arc-minutes—good for most imaging applications.

**Southern Hemisphere**: Similar process but no bright star at SCP—use Sigma Octantis (faint) or polar scope patterns.

### Polar Alignment Apps

**Popular Apps**:
- **Polar Finder** (iOS/Android): Shows Polaris position for current time
- **PS Align** (iOS/Android): Augmented reality polar alignment
- **SkySafari**: Planetarium app with polar alignment feature

**Process**:
1. Enter location and time
2. App shows where Polaris should be positioned in polar scope
3. Adjust mount to match app display

**Advantages**: More accurate than estimating Polaris position, accounts for date and time.

### Drift Alignment (High Precision)

**Purpose**: Achieve arc-minute or arc-second precision for long focal lengths.

**Concept**: Observe star drift over time and make corrections to eliminate drift.

**Process**:

**Step 1: DEC Drift (Azimuth Adjustment)**
1. Point telescope at star near celestial equator (DEC 0°) and meridian (due south/north)
2. Center star in high-magnification eyepiece or camera view
3. Observe star drift for 5-10 minutes:
   - **Star drifts north**: Mount pointing too far east—adjust azimuth west
   - **Star drifts south**: Mount pointing too far west—adjust azimuth east
4. Make small adjustment and repeat until drift is eliminated

**Step 2: RA Drift (Altitude Adjustment)**
1. Point telescope at star near celestial equator (DEC 0°) and eastern horizon (rising)
2. Center star in high-magnification eyepiece or camera view
3. Observe star drift for 5-10 minutes:
   - **Star drifts north**: Mount altitude too low—adjust altitude up
   - **Star drifts south**: Mount altitude too high—adjust altitude down
4. Make small adjustment and repeat until drift is eliminated

**Step 3: Verify**
1. Return to meridian star and verify no drift
2. Repeat process if necessary

**Accuracy**: Arc-minute to arc-second precision—best manual method.

**Time Required**: 30-60 minutes for precise alignment.

### Electronic Polar Alignment

**Available on Some Mounts**: Sky-Watcher, iOptron, Celestron (specific models).

**Process**:
1. Mount takes images of star field
2. Plate solving identifies exact pointing
3. Software calculates polar alignment error
4. Display shows which direction to adjust mount
5. Make adjustments as directed
6. Repeat until alignment is within tolerance

**Advantages**: Fast (10-15 minutes), accurate (arc-minute precision), no manual drift observation.

**Requirements**: Mount with electronic polar alignment feature, clear view of alignment stars.

---

## Tracking Mount Operation

### Equatorial Mount Axes

**Right Ascension (RA) Axis**:
- Aligned with Earth's rotational axis (points at celestial pole)
- Rotation compensates for Earth's rotation
- Tracking motor drives RA axis at sidereal rate

**Declination (DEC) Axis**:
- Perpendicular to RA axis
- Used for pointing at different declinations
- No tracking motion on DEC axis (with perfect polar alignment)

### Sidereal Tracking Rate

Stars move at **sidereal rate**: one complete rotation in 23 hours, 56 minutes, 4 seconds (slightly faster than Earth's rotation relative to the Sun).

**Mount Tracking**: Motor drives RA axis at sidereal rate to keep stars stationary.

**Other Rates**:
- **Lunar Rate**: For tracking Moon (slower than sidereal)
- **Solar Rate**: For tracking Sun (slower than sidereal)
- **King Rate**: Slightly faster than sidereal (compromise for long exposures)

For deep-sky astrophotography, use **sidereal rate**.

### Mount Initialization

**GoTo Mounts Require Alignment**:

1. **Power On**: Turn on mount
2. **Enter Location and Time**: Some mounts require manual entry; others use GPS
3. **Home Position**: Mount slews to home position (usually pointing north, level)
4. **Star Alignment**: Mount slews to alignment stars
   - Center each star in eyepiece or camera view
   - Confirm alignment
   - Typically 1-3 stars required
5. **Alignment Complete**: Mount now knows its orientation and can GoTo targets

**Star Trackers**: No alignment required—just turn on and start tracking.

### Using GoTo

1. **Select Target**: Choose object from mount's database or enter coordinates
2. **Slew**: Mount automatically moves to target
3. **Verify**: Check that target is in frame (take test exposure)
4. **Fine-Tune**: Adjust framing as needed

**Plate Solving**: Advanced technique where software analyzes star field to determine exact pointing, enabling precise GoTo.

---

## Autoguiding

### Purpose and Benefits

Autoguiding uses a guide camera to monitor a star's position and send real-time corrections to the mount, compensating for:
- Polar alignment errors
- Periodic error (mechanical imperfections in mount gears)
- Wind gusts and vibrations
- Atmospheric refraction

**Benefits**:
- Enables longer exposures (5-10+ minutes)
- Allows use of longer focal lengths
- Compensates for less-than-perfect polar alignment
- Improves tracking accuracy

### Autoguiding Components

**Guide Scope**: Small telescope (30-60mm aperture, 150-300mm focal length) mounted parallel to main telescope.

**Guide Camera**: Small, sensitive camera (ZWO ASI120MM, QHY5, Orion StarShoot) attached to guide scope.

**Guiding Software**: PHD2 Guiding (free, excellent) or alternatives.

**Connection**: Guide camera → Computer → Mount (via ST-4 cable or USB).

### PHD2 Guiding Setup

**Step 1: Connect Equipment**
1. Connect guide camera to computer via USB
2. Connect computer to mount via ST-4 cable or USB
3. Launch PHD2 Guiding

**Step 2: Configure PHD2**
1. Select guide camera from dropdown
2. Select mount from dropdown
3. Set guide camera exposure (1-5 seconds typical)
4. Set focal length of guide scope

**Step 3: Select Guide Star**
1. Point telescope at target area
2. Click "Loop" to start live view from guide camera
3. Click on suitable guide star (bright but not saturated)
4. PHD2 places green box around selected star

**Step 4: Calibrate**
1. Click "Guide" button
2. PHD2 moves mount in RA and DEC to measure response
3. Calibration takes 1-2 minutes
4. PHD2 calculates correction parameters

**Step 5: Start Guiding**
1. After calibration, guiding begins automatically
2. PHD2 monitors guide star position
3. Sends corrections to mount when star drifts
4. Graph shows tracking performance

**Step 6: Monitor Performance**
- **RMS Error**: Root mean square of tracking error
  - Under 1 arc-second: Excellent
  - 1-2 arc-seconds: Good
  - Over 2 arc-seconds: Investigate issues
- **Graph**: Shows RA and DEC error over time
- Stable, small oscillations indicate good guiding

### Autoguiding Best Practices

**Guide Star Selection**:
- Choose moderately bright star (not too bright or too faint)
- Avoid saturated stars (overexposed)
- Avoid stars near edge of frame
- SNR (signal-to-noise ratio) should be 10+ (PHD2 displays this)

**Guide Camera Exposure**:
- 1-3 seconds typical
- Longer exposures = smoother guiding but slower response
- Shorter exposures = faster response but more noise

**Aggressiveness Settings**:
- **Hysteresis**: Prevents over-correction
- **Min Motion**: Minimum error before correction applied
- Start with default settings
- Adjust if guiding is unstable or under-correcting

**Dithering**:
- Slightly moving frame between exposures
- Helps remove artifacts during stacking
- PHD2 can dither automatically (triggered by imaging software)
- Typical dither: 2-5 pixels

### Troubleshooting Autoguiding Issues

| Issue | Likely Cause | Solution |
|-------|--------------|----------|
| High RMS error (>2 arc-seconds) | Poor polar alignment, balance, guide star | Improve polar alignment, check balance, select better guide star |
| Oscillating corrections | Aggressive settings, poor balance | Reduce aggressiveness, check balance |
| Drift in one direction | Polar alignment error | Improve polar alignment |
| Sudden jumps | Wind, vibration, cable snag | Shield from wind, check cables, ensure stability |
| Guide star lost | Clouds, poor focus, guide star too faint | Wait for clouds to pass, refocus, select brighter star |
| Calibration fails | Mount not responding, cable issue | Check connections, verify mount control |

---

## Periodic Error and Correction

### Periodic Error (PE)

**Cause**: Mechanical imperfections in mount's worm gear cause slight variations in tracking speed.

**Effect**: Stars drift back and forth in RA axis with period matching worm gear rotation (typically 8-10 minutes).

**Magnitude**: Varies by mount quality—can be ±5 to ±30 arc-seconds.

### Periodic Error Correction (PEC)

**Concept**: Record periodic error pattern and play back corrections to cancel it.

**Process**:
1. **Record PEC**: Mount tracks star for one full worm gear rotation while recording error
2. **Save PEC Data**: Error pattern saved to mount's memory
3. **Playback PEC**: During imaging, mount applies corrections based on recorded pattern

**Effectiveness**: Can reduce periodic error by 50-90%.

**Limitations**: Only corrects repeatable error, not random errors or polar alignment issues.

**Availability**: Feature on higher-end mounts (Sky-Watcher EQ6-R, Celestron CGX, etc.).

---

## Tracking Accuracy Requirements

### Focal Length and Tracking Precision

Longer focal lengths magnify tracking errors, requiring more precise tracking.

**Tracking Error Tolerance** (approximate):
- **Wide-field (50-200mm)**: ±30 arc-seconds acceptable
- **Medium (200-600mm)**: ±10 arc-seconds
- **Long (600-1200mm)**: ±5 arc-seconds
- **Extreme (1200mm+)**: ±2 arc-seconds or better

**Pixel Scale**: Smaller pixels (higher resolution sensors) show tracking errors more readily.

**Rule of Thumb**: Tracking error should be less than half the pixel scale for round stars.

### Exposure Length Considerations

**Shorter Exposures**:
- Less demanding on tracking accuracy
- Easier on mount
- More frames to stack (can be beneficial)
- Less impact from individual bad frames

**Longer Exposures**:
- More light per frame
- Fewer frames needed for same total integration time
- More demanding on tracking
- Greater impact from bad frames

**Optimal Exposure Length**: Balance between tracking capability and efficiency—typically 1-5 minutes for most setups.

---

## Field Rotation

### Alt-Azimuth vs. Equatorial Mounts

**Alt-Azimuth Mounts** (altitude-azimuth):
- Move in altitude (up-down) and azimuth (left-right)
- Simple, intuitive
- **Field rotation**: Sky appears to rotate around target during tracking
- Not suitable for long-exposure astrophotography (except very short exposures)

**Equatorial Mounts**:
- Aligned with celestial poles
- Single-axis tracking follows celestial motion
- No field rotation
- Essential for astrophotography

### Wedge for Alt-Az Mounts

Some alt-azimuth mounts (e.g., Dobsonians) can be placed on equatorial wedge to convert to equatorial tracking, but this is uncommon for imaging.

---

## Practical Tracking Workflow

### Pre-Imaging

1. **Polar Alignment**: Achieve appropriate accuracy for focal length
2. **Balance Mount**: Ensure RA and DEC axes are balanced
3. **Initialize Mount**: Star alignment for GoTo mounts
4. **Start Tracking**: Enable sidereal tracking

### During Imaging

1. **Monitor Tracking**: Check first few frames for elongated stars
2. **Start Autoguiding** (if applicable): Calibrate and begin guiding
3. **Monitor Guiding Performance**: Check PHD2 graph periodically
4. **Adjust if Needed**: Refine polar alignment or guiding settings if issues arise

### Troubleshooting Tracking Issues

**Elongated Stars in One Direction**:
- **RA elongation**: Polar alignment error in azimuth
- **DEC elongation**: Polar alignment error in altitude
- **Solution**: Improve polar alignment

**Elongated Stars Randomly**:
- **Cause**: Focus issue, wind, vibration, cable snag
- **Solution**: Check focus, shield from wind, ensure stability, manage cables

**Gradual Drift**:
- **Cause**: Polar alignment error, mount not tracking
- **Solution**: Verify tracking is enabled, improve polar alignment

**Periodic Oscillation**:
- **Cause**: Periodic error, aggressive autoguiding
- **Solution**: Use PEC, adjust autoguiding settings

---

## Advanced Tracking Techniques

### Drift Alignment During Imaging

Some imagers perform drift alignment at the start of each session for maximum precision, especially with long focal lengths.

### Multi-Star Guiding

Advanced guiding software can monitor multiple guide stars simultaneously for improved accuracy.

### Adaptive Optics

Professional observatories use adaptive optics to correct for atmospheric distortion in real-time—not practical for amateur astrophotography but represents ultimate tracking precision.

### Permanent Polar Alignment

Imagers with permanent setups (observatories, piers) can achieve extremely precise polar alignment once and maintain it indefinitely, eliminating need for repeated alignment.

---

## Tracking Performance Evaluation

### Analyzing Captured Frames

**Star Shape**:
- **Round stars**: Good tracking
- **Elongated stars**: Tracking error
- **Trailing in one direction**: Polar alignment error
- **Random elongation**: Focus, wind, vibration

**Full Width Half Maximum (FWHM)**:
- Measurement of star size in pixels
- Smaller FWHM = sharper stars
- Consistent FWHM across frames indicates stable tracking
- Increasing FWHM may indicate focus drift or tracking degradation

**Stacking Software Feedback**:
- DeepSkyStacker and other software report star quality and registration accuracy
- Review rejected frames to identify tracking issues

### Continuous Improvement

- **Log Sessions**: Record polar alignment method, tracking performance, issues
- **Refine Technique**: Improve polar alignment accuracy over time
- **Upgrade Equipment**: Better mount, autoguiding, permanent setup
- **Practice**: Tracking accuracy improves with experience
