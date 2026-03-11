# Effects and Compositing

Integrate visual effects through masking, tracking, and keying.

---

## Masking Fundamentals

### Mask Types

- **Shape masks**: Ellipse, rectangle, polygon
- **Bezier masks**: Smooth curves
- **Drawn masks**: Pen tool
- **Generated masks**: From effects

### Applications

- Selective color correction
- Focus attention on subjects
- Create composites
- Hide unwanted elements
- Create split screens

---

## Rotoscoping

### Definition

Frame-by-frame masking of moving subjects to isolate from backgrounds.

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

## Green Screen / Chroma Keying

### Professional Workflow

**Step 1: Color Correction**
- Balance exposure before keying
- Address color casts
- Maximize separation

**Step 2: Initial Key**
- Sample key color
- Adjust tolerance/range
- Create initial matte

**Step 3: Matte Refinement**
- Clean edges
- Fill holes
- Address hair and transparency

**Step 4: Edge Treatment**
- Remove color spill
- Apply feathering
- Light wrap from background

**Step 5: Composite**
- Match depth of field
- Add interactive lighting
- Color grade to match

### Common Problems

| Problem | Solution |
|---------|----------|
| Uneven lighting | Light screen separately |
| Color spill | Distance subject, use suppression |
| Motion blur | Higher shutter speed |
| Fine detail (hair) | Multiple keys layered |

---

## Motion Tracking

### Point Tracking

- Follows single point
- Generates X/Y position data
- Used for attaching graphics

### Planar Tracking

- Tracks flat surfaces
- Handles perspective changes
- Better for screen replacement

### 3D Camera Tracking

- Reconstructs camera movement
- Creates 3D scene data
- Allows placing 3D objects

### Applications

- Attach graphics to surfaces
- Screen replacement
- Object removal
- Face tracking for effects

---

## Stabilization

### Warp Stabilization

- Analyzes entire frame
- Warps footage to remove shake
- Can create artifacts

### Transform Stabilization

- Moves, rotates, scales
- Simpler but effective
- May require cropping

### Rolling Shutter Correction

- Addresses "jello" effect
- Important for smartphone footage
- Often combined with stabilization

---

## Keyframing and Animation

### Animatable Properties

- Position (X, Y)
- Scale
- Rotation
- Opacity
- Effect parameters

### Interpolation Types

| Type | Effect | Use Case |
|------|--------|----------|
| Linear | Constant rate | Technical animations |
| Bezier/Eased | Variable rate | Natural movement |
| Hold | Instant change | Step effects |

### Animation Principles

- **Anticipation**: Small opposite movement before action
- **Follow-through**: Continued movement after action
- **Timing**: Keyframe spacing affects feel
