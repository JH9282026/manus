# Compositing and VFX Basics

Green screen, masking, and motion tracking fundamentals.

---

## Chroma Keying (Green Screen)

### Workflow
1. **Pre-correct**: Balance exposure before keying
2. **Initial key**: Sample color, set tolerance
3. **Matte refinement**: Clean edges, fill holes
4. **Edge treatment**: Spill removal, feathering
5. **Composite**: Match lighting, add shadows

### Common Problems

| Problem | Cause | Solution |
|---------|-------|----------|
| Uneven key | Bad lighting | Light screen evenly |
| Color spill | Too close | Distance subject |
| Motion blur | Fast movement | Higher shutter |
| Fine detail | Complex edges | Specialized tools |

---

## Masking Fundamentals

### Mask Types
- Shape masks (ellipse, rectangle)
- Bezier masks (curves)
- Drawn masks (pen tool)
- Generated masks (from effects)

### Applications
- Selective color correction
- Focus attention
- Create composites
- Hide unwanted elements

---

## Rotoscoping

### Process
1. Create initial mask around subject
2. Advance frame by frame
3. Adjust mask to follow movement
4. Set keyframes at change points
5. Refine between keyframes

### Tips
- Start at most complex frames
- Use motion tracking where possible
- Work in sections
- Build in extra edge space
- Feather for natural integration

---

## Motion Tracking

### Track Types
| Type | Tracks | Use Case |
|------|--------|----------|
| Point | Single point | Simple attachments |
| Planar | Flat surfaces | Screen replacement |
| 3D Camera | Scene depth | 3D object insertion |

### Applications
- Pin graphics to moving surfaces
- Face tracking for effects
- Object removal
- Camera motion recreation

---

## Video Stabilization

### Methods
- **Warp**: Analyzes entire frame (can warp)
- **Transform**: Move, rotate, scale only
- **Rolling shutter**: Fix sensor artifacts

### Considerations
- Requires cropping
- May introduce artifacts
- Balance stability vs. crop
