# Film and VFX Character Rigging

Advanced rigging techniques for film, animation, and VFX production.

---

## Film Rig Requirements

### Complexity vs. Usability

**Film rigs prioritize:**
- Animator control and flexibility
- High-quality deformation
- Complex control systems
- Render-time evaluation acceptable
- Usability over performance

### Typical Film Rig Features

- 100-200+ bones
- IK/FK blending on all limbs
- Space switching (world, local, custom)
- Stretchy limbs
- Advanced facial rig (100+ controls)
- Corrective blend shapes
- Custom attributes and controls
- Layered control systems

---

## Advanced Control Systems

### IK/FK Blending

**Implementation:**
1. Create FK chain (direct bone rotation)
2. Create IK chain (goal-driven)
3. Create blend chain (deformation bones)
4. Constrain blend to FK and IK with blend attribute
5. Add seamless switching (match transforms)

**Blend Attribute:**
- 0 = Full FK
- 1 = Full IK
- Smooth transition between modes
- Per-limb control

### Space Switching

**Common Spaces:**
- World space (global coordinates)
- Local space (parent relative)
- Custom spaces (follow other objects)

**Use Cases:**
- Hand follows world when grabbing object
- Hand follows body when arm swinging
- Head follows body or world
- Weapon follows hand or holster

**Implementation:**
- Parent constraints with multiple targets
- Attribute to switch between spaces
- Smooth transitions
- Bake when switching for animation

### Stretchy Limbs

**Features:**
- Limbs can stretch beyond natural length
- Useful for cartoony animation
- Squash and stretch principles
- Volume preservation option

**Implementation:**
- Measure distance between IK goal and limb start
- Scale bones based on distance
- Add stretch attribute for control
- Clamp or allow infinite stretch

---

## Facial Rigging for Film

### FACS-Based Systems

**Facial Action Coding System:**
- 40-60 base action units
- Combination shapes for common expressions
- Anatomically based
- Industry standard

### Hybrid Bone/Blend Shape Rigs

**Bones for:**
- Jaw open/close
- Eye rotation
- Eyelid movement (optional)
- Tongue

**Blend Shapes for:**
- Lip shapes and phonemes
- Facial expressions
- Wrinkles and details
- Corrective shapes

### Advanced Facial Features

**Eye Rigging:**
- Eye bones with aim constraints
- Eyelid bones or blend shapes
- Blink controls
- Eye dart and saccades
- Pupil dilation

**Lip Sync:**
- Phoneme blend shapes (A, E, I, O, U, M, F, etc.)
- Jaw bone integration
- Lip corner controls
- Lip roll and pucker

---

## Corrective Blend Shapes

### Pose-Based Deformation

**Common Correctives:**
- Shoulder raise (deltoid bulge, armpit fix)
- Elbow bend (bicep bulge, forearm compression)
- Knee bend (hamstring bulge, calf compression)
- Hip raise (glute activation)
- Torso twist (oblique definition)

### Implementation

**Pose Space Deformation (PSD):**
1. Pose character in extreme position
2. Sculpt corrective shape
3. Link to bone rotation/position
4. Blend shape activates automatically
5. Combine multiple drivers if needed

**Blend Shape Drivers:**
- Bone rotation angle
- Bone position
- Combination of multiple bones
- Custom attributes

---

## Control Rig Design

### Control Hierarchy

**Layers:**
1. **Master control** — Move entire character
2. **Body controls** — COG, hips, chest
3. **Limb controls** — IK/FK for arms/legs
4. **Extremity controls** — Hands, feet, fingers
5. **Facial controls** — Face, eyes, jaw

### Control Shapes

**Visual Language:**
- Circles: Rotation controls
- Boxes: Translation controls
- Arrows: Direction/aim controls
- Custom shapes: Specific functions

**Color Coding:**
- Red: Left side
- Blue: Right side
- Yellow: Center/spine
- Green: IK controls
- Purple: FK controls

### Custom Attributes

**Useful Attributes:**
- IK/FK blend sliders
- Space switch enums
- Stretch enable/amount
- Finger curl (all fingers at once)
- Facial expression presets
- Visibility toggles

---

## Advanced Techniques

### Ribbon/Spline IK

**For:**
- Spine (flexible, easy to pose)
- Tails
- Tentacles
- Ropes, whips

**Implementation:**
- Create spline curve
- Attach joints along curve
- Control curve with handles
- Twist and volume controls

### Dynamic Simulation

**Soft body dynamics:**
- Fat/muscle jiggle
- Cloth simulation
- Hair dynamics
- Secondary motion

**Integration:**
- Simulate in animation software
- Bake simulation to bones
- Or use real-time dynamics in engine

### Muscle Systems

**Advanced muscle simulation:**
- Anatomically accurate muscles
- Muscle bulging and sliding
- Skin sliding over muscles
- Film/VFX quality

**Tools:**
- Ziva Dynamics
- Qualoth
- Custom muscle rigs

---

## Pipeline Integration

### Rig Versioning

- Version control for rig files
- Update animations when rig changes
- Maintain backwards compatibility
- Document rig changes

### Rig Publishing

- Publish approved rig versions
- Lock rig for production
- Provide rig documentation
- Animator training/tutorials

### Animation Handoff

- Clean, organized rig
- Intuitive controls
- Documentation and notes
- Example poses/animations
- Support for animators
