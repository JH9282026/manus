# Stitching and Post-Production

Complete workflow for stitching 360° footage and post-production.

---

## Understanding Stitching

### What Is Stitching?

Stitching combines multiple camera feeds into a single spherical image, aligning and blending the edges where cameras overlap.

### Stitching Methods

**In-Camera Stitching**
- Automatic during recording
- Convenient, fast turnaround
- Limited control over results
- Good for consumer/prosumer cameras
- Adequate for many applications

**Desktop Software Stitching**
- More control over results
- Fix alignment issues manually
- Handle difficult scenes
- Professional results
- Time-consuming process

---

## Stitching Software

### Manufacturer Software

| Software | Cameras | Cost | Strengths |
|----------|---------|------|------------|
| Insta360 Studio | Insta360 cameras | Free | Best results for Insta360, easy workflow |
| GoPro Player | GoPro MAX | Free | Simple, reliable |
| Ricoh Theta+ | Ricoh Theta | Free | Quick processing |

### Professional Stitching Software

| Software | Cost | Strengths |
|----------|------|------------|
| Mistika VR | Subscription | Industry standard, excellent results |
| PTGui | One-time | Stills and video, precise control |
| VideoStitch Studio | One-time | Good multi-camera support |
| Autopano Video | One-time | Legacy but capable |

### Integrated Editing Stitching

| NLE | Stitching Capability |
|-----|---------------------|
| Adobe Premiere Pro | Limited native, plugin support |
| Final Cut Pro X | Basic stitching tools |
| DaVinci Resolve | 360° support, limited stitching |

---

## Stitching Challenges

### Parallax Errors

**Cause**: Different cameras see different perspectives of close objects.

**Symptoms**: Objects near stitch lines appear broken, doubled, or distorted.

**Solutions**:
- Keep objects distant from camera (6+ feet)
- Plan action away from stitch lines
- Manual correction in stitching software
- Accept minor artifacts in problematic areas

### Moving Objects on Stitch Lines

**Cause**: People or objects crossing between camera views during capture.

**Symptoms**: Visible seams, ghosting, cut-off limbs.

**Solutions**:
- Plan blocking to keep subjects away from stitch lines
- Use temporal stitching (software that handles motion)
- Frame-by-frame correction in difficult cases
- Multiple takes with different timing

### Lighting Differences

**Cause**: Different exposure or color between cameras/lenses.

**Symptoms**: Visible brightness or color bands at stitch lines.

**Solutions**:
- Careful exposure matching during capture
- Manual white balance
- Exposure blending in stitching software
- Color correction in post

### Nadir (Bottom) Issues

**Cause**: Tripod, monopod, or mounting hardware visible at bottom of sphere.

**Solutions**:
- Use invisible selfie stick
- Nadir patching with logo/graphic
- Clone stamp/content-aware fill
- Capture clean nadir plate for replacement

---

## Post-Production Pipeline

### 1. Ingest and Organization

**Folder Structure**:
```
project-name/
├── raw/           (original camera files)
├── stitched/      (stitched masters)
├── edits/         (edit project files)
├── audio/         (spatial audio files)
├── exports/       (final deliverables)
└── assets/        (graphics, overlays)
```

**Organization Tips**:
- Date and scene naming convention
- Preserve original files
- Create proxies for editing if needed
- Document camera settings per clip

### 2. Stitching Workflow

1. Import footage into stitching software
2. Check auto-stitch quality
3. Identify problem areas (review full sphere)
4. Manual adjustments for parallax, seams
5. Set horizon level
6. Export stitched master (highest quality)
7. Create proxies for editing if needed

### 3. Editing in NLE

**Software with Native 360° Support**:
- Adobe Premiere Pro
- Final Cut Pro X
- DaVinci Resolve
- Avid Media Composer (VR toolset)

**Editing Workflow**:
1. Import stitched footage
2. Enable VR viewing mode
3. Edit timeline in equirectangular view
4. Preview in headset or VR viewer
5. Add graphics/effects (360°-aware)
6. Integrate spatial audio
7. Color grade
8. Export with metadata

### 4. Reframing

**Purpose**: Adjust default viewing direction.

**Uses**:
- Point viewers toward primary action
- Correct horizon tilt
- Center content for initial view

**Available In**: Most NLEs with 360° support.

### 5. Stabilization

**Post-Production Stabilization**:
- Essential for handheld shots
- Horizon leveling
- Smooths camera movement

**Considerations**:
- May introduce artifacts
- Can reduce effective resolution
- Balance stability with quality
- Plan for stabilization when shooting

---

## Transition Strategies

### Recommended Transitions

| Transition | Characteristics | Best For |
|------------|-----------------|----------|
| Fade/Dissolve | Safe, comfortable | Scene changes, time passing |
| Dip to Black | Clear scene change | Major location changes |
| Cut | Quick, dynamic | Same location, matched direction |

### Cut Considerations

- Match viewing directions when cutting
- Avoid opposite direction cuts (disorienting)
- Allow settling time after cuts
- Consider continuity of viewer position

### Creative Transitions

- Swirl/warp effects (motivated)
- Light leaks, flares
- Spatial transitions (moving through space)
- Use sparingly, should be motivated

---

## Color Grading for 360°

### Challenges

- Uniform look across entire sphere
- Avoiding visible gradients at seams
- Exposure differences between directions

### Approach

1. Global adjustments first (exposure, contrast, saturation)
2. Check consistency across full sphere
3. Targeted adjustments for specific areas (carefully)
4. View in headset to verify

### Software

- DaVinci Resolve (strongest for color)
- Adobe Premiere Pro Lumetri
- Assimilate Scratch

---

## Graphics and Text in 360°

### Placement Considerations

- Consider viewing angle (not all viewers see all areas)
- Curved distortion at edges
- Place in primary viewing zone when important
- Allow time to read (no rushing)

### Creation Tools

- After Effects with VR tools
- Cinema 4D
- Blender (free)
- Native NLE 360° graphics

### Text Guidelines

- Larger text than traditional video
- Simple, readable fonts
- High contrast
- Avoid placing at extreme top/bottom (distortion)

---

## Export and Delivery

### Metadata Requirements

**Critical**: 360° video requires proper metadata to display correctly.

**Metadata Injection Tools**:
- Spatial Media Metadata Injector (Google)
- YouTube 360 Video Metadata App
- GoPro VR Plugin for Premiere/Final Cut
- Handbrake (with options)

**Required Metadata**:
- Spherical video flag
- Projection type (equirectangular)
- Stereoscopic mode (if applicable)
- Spatial audio format (if applicable)

### Export Settings by Platform

| Platform | Resolution | Codec | Bitrate |
|----------|------------|-------|--------|
| YouTube | Up to 8K | H.264/H.265 | 50-150+ Mbps |
| Facebook | 4K-8K | H.264 | 40-80 Mbps |
| Vimeo | Up to 8K | H.264/H.265 | 50-100+ Mbps |
| Quest native | 5.7K recommended | H.264 | 40-60 Mbps |

### Quality Checklist Before Export

- [ ] Full sphere reviewed (all directions)
- [ ] Stitch quality acceptable
- [ ] Horizon level correct
- [ ] Audio synced and spatial
- [ ] Color consistent across sphere
- [ ] No unwanted elements visible
- [ ] Nadir treated (patched or logo)
- [ ] Metadata will be embedded

---

## Testing

### Test on Target Devices

**Before Final Delivery**:
- Test on VR headset
- Test on mobile (YouTube/Facebook app)
- Test on desktop browser
- Verify spatial audio works
- Check for playback issues

### Common Issues to Check

| Issue | Test Method | Solution |
|-------|-------------|----------|
| Not displaying as 360° | Play on YouTube/platform | Fix metadata |
| Visible stitch lines | View in headset | Re-stitch or fix |
| Motion sickness | Watch full experience | Reduce movement |
| Audio doesn't rotate | Turn head while watching | Check spatial audio export |
| Resolution too low | View details | Export at higher resolution |
