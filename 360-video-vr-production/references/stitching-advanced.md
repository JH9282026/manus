# Advanced Stitching Techniques

Deep dive into 360° video stitching workflows for professional results.

---

## Understanding Stitching Fundamentals

### Stitch Lines
The seams where camera views overlap. Goal: invisible transitions.

### Parallax
Objects at different distances appear in different positions relative to camera overlap zones. Close objects = more parallax = harder stitching.

### Optical Flow
Algorithm that analyzes pixel movement to blend overlapping areas smoothly.

---

## Multi-Camera Rig Stitching

### Synchronization Methods
1. **Hardware genlock**: Best accuracy, requires compatible cameras
2. **Timecode sync**: Professional standard, sub-frame accuracy
3. **Audio sync**: Post-production alignment using waveforms
4. **Flash/clap sync**: Manual alignment point

### Calibration Process
1. Capture calibration footage (checkerboard pattern)
2. Generate lens distortion profiles
3. Calculate camera positions/orientations
4. Create stitch template
5. Apply to all footage

### Stitching Software Workflows

#### Mistika VR (Professional)
```
1. Import → Create VR Comp
2. Sync clips via timecode
3. Auto-calibrate or manual adjust
4. Set stitch blend zones
5. Optical flow for moving objects
6. Render to equirectangular
```

#### Autopano Video Pro
```
1. Create new project
2. Import all camera angles
3. Synchronization → Audio-based
4. Stitch → Automatic calibration
5. Adjust blend manually if needed
6. Stabilize → Select method
7. Render settings → Resolution/codec
```

---

## Handling Parallax Issues

### Near-Object Strategies
- **Increase camera distance**: Move rig away from close objects
- **Controlled stitch zones**: Keep important action away from seams
- **Manual masking**: Rotoscope objects crossing seams
- **Optical flow priority**: Let algorithm handle transitions

### Problem Areas
| Issue | Cause | Solution |
|-------|-------|----------|
| Ghosting | Moving object in blend zone | Optical flow or manual mask |
| Visible seam | Calibration error | Re-calibrate or adjust manually |
| Color mismatch | Different exposure/WB | Pre-grade before stitching |
| Warping | Lens profile error | Manual lens calibration |

---

## Manual Stitch Adjustment

### When to Use Manual Adjustment
- Automated stitching fails
- Critical content in stitch zones
- Client requires pixel-perfect results
- Complex multi-camera setups

### Manual Process
1. Identify problem frames
2. Create control points on matching features
3. Adjust blend width and position
4. Use feathering to hide edges
5. Apply optical flow for motion
6. Preview in VR headset

---

## Stabilization Techniques

### Gyroscope-Based
- Use camera's internal gyro data
- Most accurate for aggressive motion
- Supported: Insta360, GoPro, DJI

### Software-Based
- Analyzes frame-to-frame motion
- Works without gyro data
- Tools: Mocha VR, ReelSteady 360

### Horizon Lock
- Maintains level horizon regardless of camera tilt
- Essential for: drone footage, action cameras
- Method: Track horizon, counter-rotate

---

## Color Matching Across Cameras

### Pre-Production
1. Use identical camera settings
2. White balance to same Kelvin
3. Match exposure precisely
4. Disable auto adjustments

### Post-Production Workflow
1. **Primary correction**: Match exposure, WB
2. **Secondary correction**: Specific color ranges
3. **Feather at seams**: Gradual transition
4. **Global grade**: Unified look

### Tools for Color Matching
- DaVinci Resolve: Industry standard
- Mistika VR: Built-in matching
- After Effects: CC plugins

---

## Nadir and Zenith Patching

### Nadir (Bottom)
The tripod/monopod area visible beneath camera.

#### Patching Methods
1. **Logo/graphic overlay**: Brand watermark
2. **Clone/heal**: Paint out tripod
3. **Separate nadir camera**: Shoot clean plate
4. **3D tracked patch**: Insert CG floor

### Zenith (Top)
Top of sphere, often has rig/pole visible.

#### Solutions
1. **Invisible pole**: Insta360 auto-removes
2. **Manual clone**: Copy nearby sky
3. **Graphic mask**: Artistic overlay

---

## Output Formats and Quality

### Equirectangular
Standard format, 2:1 aspect ratio, full sphere.

### Cubemap
Six square faces, efficient for real-time rendering.

### Equi-Angular Cubemap (EAC)
YouTube's optimized format, better quality at edges.

### Resolution Guidelines
| Final Output | Capture Resolution | Notes |
|--------------|-------------------|-------|
| 4K delivery | 5.7K+ capture | Cropping/stabilization headroom |
| 8K delivery | 10K+ capture | Professional standard |
| Stereo 3D | 8K per eye minimum | Doubles processing |

### Codec Recommendations
- **Master**: ProRes 422 HQ or DNxHR
- **Delivery**: H.265/HEVC (best compression)
- **Web**: H.264 (compatibility) or VP9 (YouTube)

---

## Troubleshooting Common Issues

### Visible Seams After Stitching
1. Check sync accuracy
2. Re-run calibration
3. Manually adjust control points
4. Increase blend zone width

### Motion Blur Mismatch
- Ensure identical shutter speeds
- Match frame rates exactly
- Use optical flow blending

### Rolling Shutter Artifacts
- Use global shutter cameras if possible
- Reduce fast panning movements
- Apply rolling shutter correction in post

### Incorrect Projection
- Verify metadata injection
- Check projection type setting
- Re-export with correct flags
