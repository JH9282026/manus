# Game Character Rigging

Rigging techniques optimized for real-time game engines.

---

## Game Engine Requirements

### Performance Constraints

**Bone Count Limits:**
- Mobile: 30-50 bones maximum
- Console/PC: 60-100 bones typical
- VR: 40-60 bones (performance critical)

**Skinning Limits:**
- Mobile: 2 bones per vertex
- Console/PC: 4 bones per vertex
- Minimize bone influences for performance

### Real-Time Considerations

- Avoid complex constraints (expensive to evaluate)
- Use simple IK solvers
- Minimize dynamic parent switching
- Optimize for fast skeletal animation
- Test performance in target engine early

---

## Unity Rigging Workflow

### Humanoid Rig Setup

**Requirements:**
- Standard bone names or mapping
- T-pose or A-pose
- Proper bone orientation
- Root motion bone (optional)

**Import Settings:**
1. Set Rig type to Humanoid
2. Configure Avatar (auto or manual mapping)
3. Verify bone mapping
4. Set up root motion
5. Test with animations

### Generic Rig Setup

- For non-humanoid characters
- Custom bone structure
- Manual animation retargeting
- More flexible but less automated

---

## Unreal Engine Rigging

### Skeleton Asset

- Import FBX with skeleton
- Create Skeleton asset
- Set up bone hierarchy
- Configure retargeting
- Add sockets for attachments

### Control Rig

- Visual scripting for rigs
- IK/FK systems
- Custom controls
- Animation rigging
- Runtime and editor use

---

## Optimization Techniques

### Bone Reduction

**Simplify Skeleton:**
- Remove finger bones (use 1-2 per finger)
- Simplify spine (3-4 bones instead of 7+)
- Remove toe bones if not needed
- Merge helper bones
- Use simpler facial rig

### LOD Skeletons

- Reduce bones for distant LODs
- LOD0: Full skeleton
- LOD1: Remove fingers, simplify
- LOD2: Minimal skeleton
- LOD3: Very simple or static

### Weight Optimization

- Limit bones per vertex (2-4)
- Remove zero-weight influences
- Normalize weights
- Clean up automatic weights
- Test deformation vs. performance

---

## Export Settings

### FBX Export for Games

**Settings:**
- FBX 2020 or engine-compatible version
- Bake animations (if applicable)
- Include: Mesh, Skeleton, Skin, Animations
- Units: Centimeters (or engine standard)
- Up Axis: Y-up (Unity) or Z-up (Unreal)
- Forward Axis: Check engine requirements

### Common Issues

**Scale Problems:**
- Verify unit settings
- Check import scale in engine
- Consistent scale across assets

**Orientation Issues:**
- Check up/forward axis settings
- Verify bone roll/orientation
- Test in engine immediately

**Missing Bones:**
- Ensure all bones exported
- Check bone hierarchy
- Verify naming conventions

---

## Best Practices

### Game-Specific Rigging

1. **Keep it simple** — Fewer bones, simpler systems
2. **Test in engine** — Import and test early and often
3. **Follow conventions** — Use engine-standard naming and structure
4. **Optimize weights** — Clean, efficient skinning
5. **Document** — Note any special requirements or features

### Animation Compatibility

- Use standard bone names for retargeting
- Maintain consistent skeleton across characters
- Plan for animation sharing
- Test with various animations
- Consider mocap compatibility

### Modular Rigging

- Separate body parts for customization
- Standardized attachment points
- Consistent bone structure
- Efficient for character creators
- Test all combinations
