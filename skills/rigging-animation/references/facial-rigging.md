# Facial Rigging

Comprehensive guide to creating expressive facial rigs for animation.

---

## Facial Anatomy

### Skull Structure

**Key Landmarks:**
- Frontal bone (forehead)
- Zygomatic arch (cheekbones)
- Maxilla (upper jaw)
- Mandible (lower jaw, only moving skull bone)
- Nasal bone
- Orbital cavity (eye sockets)

### Facial Muscles

**Major Expression Muscles:**
- **Frontalis**: Raises eyebrows, wrinkles forehead
- **Corrugator**: Furrows brow (anger, concentration)
- **Orbicularis oculi**: Closes eyelids, squinting
- **Levator labii**: Raises upper lip (snarl, disgust)
- **Zygomaticus major**: Smile muscle
- **Orbicularis oris**: Closes lips, pucker
- **Depressor anguli oris**: Frowns, pulls mouth corners down
- **Masseter**: Jaw muscle, clenching

---

## Facial Rig Components

### Bone-Based Systems

**Essential Facial Bones:**
- **Jaw bone**: Opens/closes mouth, side-to-side movement
- **Eye bones** (L/R): Eye rotation (look direction)
- **Eyelid bones** (optional): Upper/lower eyelid movement
- **Tongue bones** (optional): Tongue movement

**Advantages:**
- Real-time friendly
- Easy to animate
- Good for stylized characters
- Lower memory footprint

**Disadvantages:**
- Limited detail
- Harder to achieve realistic expressions
- Requires more bones for detail

### Blend Shape Systems

**Blend Shape Categories:**

**Eyes:**
- Blink (L, R, both)
- Eye wide (L, R)
- Eye squint (L, R)
- Look up/down/left/right (optional, often use bones)

**Brows:**
- Brow up (L, R, inner, outer)
- Brow down (L, R)
- Brow squeeze (furrow)

**Mouth:**
- Smile (L, R, both)
- Frown (L, R, both)
- Mouth open
- Lips together/apart
- Lip pucker
- Lip funnel (O shape)
- Lip roll (upper, lower)
- Mouth left/right
- Lip corner up/down (L, R)

**Jaw:**
- Jaw open (often bone-driven)
- Jaw left/right
- Jaw forward

**Cheeks:**
- Cheek puff
- Cheek suck
- Cheek raise (smile)

**Nose:**
- Nose wrinkle
- Nostril flare

**Phonemes (Lip Sync):**
- A, E, I, O, U (vowels)
- M/B/P (lips together)
- F/V (teeth on lower lip)
- S/Z (teeth together, lips apart)
- T/D/L (tongue to teeth)
- R (rounded)
- W (rounded, wide)
- TH (tongue between teeth)

**Advantages:**
- High detail possible
- Realistic expressions
- Artist-friendly (sculpt-based)
- Precise control

**Disadvantages:**
- Higher memory cost
- Performance impact (many active shapes)
- Requires good base topology

### Hybrid Systems

**Combination of bones and blend shapes:**
- Bones for jaw and eyes (large movements)
- Blend shapes for lips and expressions (detail)
- Best of both approaches
- Industry standard for games and film

---

## Creating Blend Shapes

### Workflow

1. **Start with neutral face** — Relaxed, neutral expression
2. **Duplicate mesh** — Create copy for each blend shape
3. **Sculpt target** — Move vertices to create expression
4. **Maintain vertex order** — Don't add/remove vertices
5. **Test blend** — Verify smooth interpolation
6. **Create variations** — Left, right, and both sides

### Blend Shape Best Practices

**Symmetry:**
- Create left and right versions separately
- Allows asymmetrical expressions
- More natural, realistic animation
- Example: smile_L, smile_R, smile_both

**Intensity:**
- Sculpt to extreme (100%)
- Animator can dial back (0-100%)
- Better than under-sculpting
- Can go beyond 100% if needed

**Combination Testing:**
- Test multiple blend shapes together
- Check for conflicts or artifacts
- Create combination shapes if needed
- Example: smile + blink = smile_blink

**Clean Sculpting:**
- Only move necessary vertices
- Smooth transitions
- Avoid artifacts
- Check from all angles

---

## Eye Rigging

### Eye Bone Setup

**Basic Eye Rig:**
1. Create eye bones (L and R)
2. Position at eye center
3. Aim constraint to eye target/control
4. Eye target controls look direction
5. Limit rotation if needed

**Advanced Eye Rig:**
- Separate iris/pupil bone (dilation)
- Eyelid bones or blend shapes
- Eye dart controls (quick movements)
- Lazy eye option (eyes don't move together)
- Eye jitter (subtle random movement)

### Eyelid Rigging

**Bone-Based Eyelids:**
- Upper and lower eyelid bones
- Follow eye rotation
- Blink control
- Automatic eyelid movement with eye rotation

**Blend Shape Eyelids:**
- Blink blend shapes (L, R)
- Eye wide blend shapes
- Eye squint blend shapes
- More control, easier to animate

**Hybrid Approach:**
- Bones for basic movement
- Blend shapes for refinement
- Best quality

---

## Jaw Rigging

### Jaw Bone

**Setup:**
- Pivot at jaw hinge (temporomandibular joint)
- Rotates to open mouth
- Can translate for jaw forward/side movement
- Drives lip blend shapes

### Jaw-Driven Blend Shapes

**Automatic lip movement:**
- Jaw rotation drives mouth open blend shape
- Lips part as jaw opens
- Reduces animator workload
- Can be overridden for specific phonemes

---

## Lip Sync Systems

### Phoneme-Based

**Visemes (visual phonemes):**
- 8-15 mouth shapes for speech
- Map audio phonemes to visemes
- Blend between shapes for smooth speech
- Standard for games and animation

**Common Viseme Set:**
1. Neutral/rest
2. A (father)
3. E (see)
4. I (sit)
5. O (go)
6. U (you)
7. M/B/P (lips together)
8. F/V (teeth on lip)
9. S/Z (teeth together)
10. T/D/L (tongue up)
11. R (rounded)
12. W (wide rounded)

### Automated Lip Sync

**Tools:**
- Papagayo: Free lip sync tool
- Rhubarb Lip Sync: Command-line tool
- FaceFX: Professional facial animation
- Engine built-in (Unreal, Unity plugins)

**Process:**
1. Import audio
2. Analyze phonemes
3. Generate animation curves
4. Refine manually
5. Add expression and emotion

---

## Facial Animation Techniques

### Layered Animation

**Layers:**
1. **Base layer**: Phonemes and lip sync
2. **Expression layer**: Emotion and mood
3. **Detail layer**: Blinks, eye darts, micro-expressions
4. **Corrective layer**: Fix issues, refine

### Micro-Expressions

**Subtle, brief expressions:**
- Blinks (every 3-5 seconds)
- Eye darts (quick eye movements)
- Eyebrow raises
- Lip twitches
- Add life and realism

### Emotional Expressions

**Basic Emotions:**
- Happy: Smile, raised cheeks, crinkled eyes
- Sad: Frown, inner brows up, droopy eyelids
- Angry: Furrowed brow, tight lips, wide eyes
- Surprised: Raised brows, wide eyes, open mouth
- Disgusted: Nose wrinkle, upper lip raise, squint
- Fear: Wide eyes, raised brows, open mouth

---

## Optimization

### Blend Shape Count

**Guidelines:**
- Mobile: 20-40 blend shapes
- Console/PC: 60-100 blend shapes
- Film: 100-200+ blend shapes

### Performance

- Use sparse blend shapes (only changed vertices)
- Disable facial animation at distance
- LOD facial rigs (simpler for distant characters)
- Limit active blend shapes

---

## Testing and Refinement

### Test Expressions

- Neutral
- Smile (subtle and extreme)
- Frown
- Surprise
- Anger
- All phonemes
- Combination expressions

### Common Issues

**Pinching:** Refine weights, add edge loops
**Asymmetry:** Check blend shape symmetry
**Conflicts:** Test blend shape combinations
**Range:** Ensure full range of motion
