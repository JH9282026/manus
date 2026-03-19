# Advanced Rigging Systems

Advanced techniques and systems for professional character rigging.

---

## IK/FK Systems

### IK Solvers

**Two-Bone IK (2B-IK):**
- For arms and legs (3-bone chains)
- Shoulder-elbow-wrist or hip-knee-ankle
- Pole vector controls bend direction
- Most common IK type

**Spline IK:**
- For spine, tails, tentacles
- Follows curve path
- Multiple control points
- Twist and stretch controls

**Single-Chain IK:**
- For fingers, toes
- Simple goal-based
- Good for procedural animation

### IK/FK Blending

**Seamless Switching:**
1. Create FK chain (animator rotates bones)
2. Create IK chain (animator moves goal)
3. Create deformation chain (actual skinned bones)
4. Constrain deform to FK and IK with blend
5. Add match transforms for seamless switch

**Blend Attribute:**
- 0.0 = Full FK mode
- 1.0 = Full IK mode
- Smooth interpolation between
- Per-limb control

**Matching:**
- When switching, match transforms
- FK to IK: Position IK goal at hand/foot
- IK to FK: Rotate FK bones to match current pose
- Prevents popping

---

## Twist Bone Systems

### Purpose

**Solve twist distribution:**
- Single bone twist looks unnatural
- Distribute twist along limb length
- Forearm and upper arm twist
- Thigh and calf twist

### Implementation

**Twist Bone Setup:**
1. Create helper bones along limb (2-4 bones)
2. Constrain to distribute twist
3. Skin mesh to twist bones
4. Smooth weight distribution

**Quaternion-Based Twist:**
- Calculate twist from bone rotation
- Distribute along chain
- More accurate than simple constraints

---

## Ribbon/Spline Rigs

### Spine Ribbon

**Setup:**
1. Create NURBS or Bezier curve
2. Attach joints along curve
3. Control curve with handles (3-5 controls)
4. Skin spine to joints
5. Add twist and volume controls

**Advantages:**
- Easy to pose (move a few controls)
- Smooth, natural curves
- Good for cartoony or realistic
- Flexible and animator-friendly

### Tail/Tentacle Rigs

**Dynamic Tails:**
- Spline IK for base control
- Dynamic simulation for secondary motion
- Blend between manual and dynamic
- Adjustable stiffness and damping

---

## Stretchy Limbs

### Implementation

**Measure and Scale:**
1. Measure distance between IK goal and limb start
2. Compare to natural limb length
3. Scale bones when distance exceeds length
4. Add stretch attribute for control

**Volume Preservation:**
- As limb stretches, reduce thickness
- Maintain volume (length × width² = constant)
- Optional, depends on style

**Soft IK:**
- Gradual stretch as approaching limit
- Prevents hard stops
- More natural feeling

---

## Space Switching

### Parent Space Switching

**Common Spaces:**
- World space (global)
- Local space (parent)
- Custom spaces (follow other objects)

**Use Cases:**
- Hand: World (grabbing object) vs. Body (swinging)
- Head: Body (normal) vs. World (looking at something)
- Weapon: Hand (holding) vs. Holster (stored)

**Implementation:**
- Parent constraint with multiple targets
- Attribute to switch between targets
- Smooth blending between spaces
- Bake animation when switching

---

## Quadruped Rigging

### Skeletal Differences

**Quadruped vs. Biped:**
- Four legs instead of two
- Horizontal spine
- Different weight distribution
- Digitigrade legs (many animals)

### Leg Types

**Plantigrade:**
- Flat feet (bears, humans)
- Heel, ball, toes on ground
- Standard foot rig

**Digitigrade:**
- Walk on toes (dogs, cats, dinosaurs)
- Heel is elevated (actually ankle)
- Reverse foot rig adapted

**Unguligrade:**
- Walk on hooves (horses, deer)
- Only hoof tip touches ground
- Simplified foot rig

### Spine Rigging

**Horizontal Spine:**
- More flexible than biped
- Spline IK common
- 5-7 spine bones typical
- Tail integration

---

## Facial Rig Advanced

### Bone-Driven Blend Shapes

**Automatic Activation:**
- Blend shapes driven by bone rotation
- Example: Jaw open drives lips apart
- Reduces animator workload
- Pose Space Deformation (PSD)

### Corrective Blend Shapes

**Fix Deformation Issues:**
- Activate based on bone combinations
- Example: Smile + jaw open = specific shape
- Improves quality
- Essential for realistic faces

---

## Custom Rigging Tools

### Scripting Rigs

**Python/MEL (Maya):**
- Automate rig creation
- Consistent, repeatable rigs
- Easy to update and maintain
- Build custom tools

**Blender Python:**
- Rigify addon (built-in)
- Custom rig generators
- Automate repetitive tasks

### Modular Rigging

**Component-Based:**
- Build rig from modules (arm, leg, spine, etc.)
- Reusable components
- Easy to customize
- Faster rig creation

**Frameworks:**
- mGear (Maya)
- Rigify (Blender)
- Advanced Skeleton (Maya)
- Custom frameworks

---

## Performance Optimization

### Bone Count Reduction

**Strategies:**
- Remove unnecessary bones
- Simplify finger rigs (1-2 bones per finger)
- Reduce spine bones
- Remove helper bones if not needed
- LOD skeletons

### Constraint Optimization

**Reduce Evaluation Cost:**
- Minimize constraint count
- Bake constraints when possible
- Use simpler constraint types
- Avoid cyclic dependencies

---

## Testing and Validation

### Rig Testing

**Test Poses:**
- Neutral pose
- Extreme joint bends
- Combination poses
- Animation cycles
- Edge cases

**Automated Testing:**
- Script to test all controls
- Verify no flipping or breaking
- Check constraint behavior
- Performance profiling

### Quality Assurance

**Checklist:**
- All controls work as expected
- No gimbal lock issues
- Smooth IK/FK switching
- Proper space switching
- Good deformation
- Performance acceptable
- Documentation complete
