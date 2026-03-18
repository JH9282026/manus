# VR Interaction Design

Comprehensive guide to designing natural, intuitive, and immersive interactions for virtual reality games and experiences.

---

## Core Principles of VR Interaction Design

### 1. Physicality and Weight

VR interactions should feel physical and grounded in real-world physics. Players expect virtual objects to behave like their real-world counterparts.

**Virtual Hands and Weight Simulation:**
- Virtual hands lag slightly behind real-world controller movements to simulate object weight
- Heavy objects require two-handed interaction or slower movement
- Light objects respond immediately to hand movements
- Objects have momentum and inertia (don't stop instantly)

**Implementation:**
- Use spring joints or physics constraints to create lag between controller and virtual hand
- Adjust spring strength based on object weight (heavier = stronger spring = more lag)
- Apply forces to objects based on hand velocity (throwing, pushing)
- Use haptic feedback to reinforce weight (stronger vibration for heavier objects)

**Example: Picking Up a Heavy Object**
1. Player reaches hand to object
2. Hand touches object, haptic feedback triggers
3. Player presses grip button
4. Virtual hand lags behind controller (simulating effort to lift)
5. Object follows hand with slight delay (weight simulation)
6. Player feels resistance through haptic feedback

### 2. Diegetic UI (In-World Interfaces)

Traditional 2D HUDs break immersion in VR. Diegetic UI exists within the game world and feels natural to interact with.

**Diegetic UI Patterns:**

**Wrist-Mounted UI:**
- Smartwatch or holographic display on virtual wrist
- Player rotates wrist to view, taps to interact
- Always accessible, doesn't clutter view
- Best for: Quick menus, health/ammo display, map

**Over-Shoulder Inventory:**
- Player reaches over shoulder to access virtual backpack
- Items appear as physical objects (not 2D icons)
- Grab item from backpack to equip
- Best for: Inventory management, weapon selection

**In-World Terminals:**
- Computers, tablets, or holographic displays in game world
- Player physically approaches and interacts
- Feels grounded in world, not floating UI
- Best for: Story exposition, mission briefings, settings

**Handheld Tablets:**
- Player holds virtual tablet in one hand, interacts with other
- Can be put away when not needed
- Best for: Maps, objectives, detailed information

**Avoid:**
- Floating 2D menus in front of player (breaks immersion)
- UI attached to head (causes discomfort, hard to read)
- Tiny text or UI elements (eye strain)

### 3. Natural Gestures and Controls

Interactions should mirror real-world actions as closely as possible. Players shouldn't need to learn arbitrary button combinations.

**Natural Gesture Examples:**

**Grabbing:**
- Reach hand to object, press grip button
- Object snaps to hand or follows physics
- Release button to drop

**Throwing:**
- Grab object, swing arm, release grip at apex
- Object velocity based on hand velocity at release
- Natural throwing motion (no button timing required)

**Pushing Buttons:**
- Physically touch button with finger or hand
- Button depresses when touched (visual and haptic feedback)
- No need to press controller button (physical touch is the input)

**Turning Valves:**
- Grab valve with hand, rotate wrist
- Valve rotates with hand motion
- Haptic feedback for resistance

**Opening Doors:**
- Grab door handle, pull or push
- Door follows hand motion (physics-based)
- Can peek through door by opening slightly

**Climbing:**
- Grab ledge with hand, pull body up
- Other hand reaches for next ledge
- Natural climbing motion (no button mashing)

### 4. Guidance Through Environmental Design

Players can't rely on traditional UI markers (arrows, waypoints) in VR. Use environmental design to guide players naturally.

**Visual Guidance:**
- **Lighting**: Bright areas draw attention, dark areas discourage exploration
- **Color Contrast**: Important objects stand out from environment
- **Focal Points**: Composition guides eye to key areas
- **Sightlines**: Clear paths and vistas show where to go

**Spatial Audio Guidance:**
- **Directional Sound**: Players turn toward sound sources
- **Audio Cues**: Sounds indicate interactive objects or events
- **Ambient Audio**: Background sounds create atmosphere and context

**Physical Guidance:**
- **Narrow Paths**: Funnel players toward objectives
- **Obstacles**: Block unintended paths
- **Scale**: Large objects draw attention, small objects are secondary

---

## Hand Presence and Tracking

### Controller-Based Interaction

**Standard VR Controllers:**
- Tracked in 3D space (6DOF: position + rotation)
- Buttons: Grip, trigger, thumbstick, face buttons
- Haptic feedback: Vibration motors
- Most common and reliable tracking method

**Virtual Hand Representation:**
- Controllers represented as hands, tools, or abstract shapes
- Hands are most immersive (players see their "own" hands)
- Tools are contextual (gun, sword, flashlight)
- Abstract shapes are functional but less immersive

**Button Mapping Best Practices:**
- **Grip**: Grab and hold objects
- **Trigger**: Primary action (shoot, use tool, select)
- **Thumbstick**: Locomotion (smooth movement) or teleport
- **Face Buttons**: Secondary actions (reload, jump, menu)
- Keep mappings consistent across interactions (don't change grip function)

### Hand Tracking (Controller-Free)

**Platforms Supporting Hand Tracking:**
- Meta Quest 2, Quest 3, Quest Pro
- Apple Vision Pro
- HoloLens 2

**Hand Tracking Capabilities:**
- Tracks finger positions and gestures
- Pinch gesture for selection and grab
- Point gesture for UI interaction
- No physical buttons (all gesture-based)

**Advantages:**
- More natural (no controllers to hold)
- Lower barrier to entry (no controller learning curve)
- Better for social VR (see real hand gestures)

**Disadvantages:**
- Less precise than controllers (tracking can be jittery)
- No haptic feedback (can't feel button presses)
- Occlusion issues (hands must be visible to cameras)
- Limited button inputs (only gestures)

**Best Use Cases:**
- UI interaction (menus, buttons)
- Casual games (puzzle, social, exploration)
- Social VR (hand gestures for communication)
- Mixed reality (interacting with real and virtual objects)

**Implementation Tips:**
- Provide visual feedback for gestures (highlight when pinch detected)
- Use larger hit boxes for hand tracking (less precise than controllers)
- Offer controller fallback (some players prefer controllers)
- Test extensively (hand tracking varies by lighting and hand size)

---

## Object Interaction Patterns

### Grab and Hold

**Standard Grab:**
1. Player reaches hand to object
2. Hand enters object's grab zone (trigger zone)
3. Visual feedback (highlight, outline, glow)
4. Player presses grip button
5. Object attaches to hand (follows hand position/rotation)
6. Player releases grip to drop

**Snap Grab vs. Physics Grab:**
- **Snap Grab**: Object instantly snaps to hand at predefined position (e.g., gun grip)
  - Pros: Precise, reliable, feels good
  - Cons: Less realistic, can feel "gamey"
- **Physics Grab**: Object follows hand via physics joint (spring, fixed joint)
  - Pros: Realistic, objects have weight and momentum
  - Cons: Can be imprecise, objects can clip through geometry

**Best Practice**: Use snap grab for tools and weapons (precision matters), physics grab for environmental objects (realism matters).

### Distance Grab

**What is Distance Grab?**
Player can grab distant objects without physically reaching them. Object flies to hand or player teleports to object.

**Variants:**
- **Pull to Hand**: Object flies to player's hand (like Force Pull in Star Wars)
- **Teleport to Object**: Player teleports to object's location
- **Extend Arm**: Virtual arm extends to reach distant object

**When to Use:**
- Accessibility (players with limited mobility)
- Convenience (avoid tedious walking to pick up items)
- Gameplay mechanic (telekinesis, grappling hook)

**Implementation:**
1. Player points at distant object (raycast from hand)
2. Object highlights (visual feedback)
3. Player presses grip button
4. Object flies to hand along arc (smooth motion, not instant)
5. Object snaps to hand when close

**Best Practice**: Use sparingly (can break immersion if overused). Provide visual feedback (beam, arc, highlight) so player understands mechanic.

### Two-Handed Interaction

**When to Use Two Hands:**
- Large or heavy objects (crates, barrels, furniture)
- Tools requiring two hands (rifles, bows, two-handed swords)
- Precision tasks (aiming rifle, drawing bow)

**Implementation:**
1. Player grabs object with one hand (primary hand)
2. Object follows primary hand
3. Player grabs object with second hand (secondary hand)
4. Object now controlled by both hands (position, rotation, scale)
5. Release either hand to return to one-handed control

**Two-Handed Weapon Example (Rifle):**
- Primary hand (dominant): Grips rifle handle, controls trigger
- Secondary hand (non-dominant): Grips rifle forend, stabilizes aim
- Rifle rotation based on both hand positions (realistic aiming)
- Recoil affects both hands (haptic feedback)

**Two-Handed Bow Example:**
- Primary hand: Grips bow handle (stationary)
- Secondary hand: Grips arrow, pulls back (draw strength)
- Release secondary hand to fire arrow
- Arrow velocity based on draw distance

### Physics-Based Interaction

**What is Physics-Based Interaction?**
Objects respond to real physics (gravity, momentum, collision). Player interacts by applying forces, not triggering animations.

**Examples:**
- **Throwing**: Object velocity based on hand velocity at release
- **Pushing**: Apply force to object based on hand movement
- **Stacking**: Objects balance and fall based on physics
- **Swinging**: Sword or bat has momentum, affects impact force

**Advantages:**
- Realistic and satisfying
- Emergent gameplay (players discover creative solutions)
- Immersive (objects behave as expected)

**Disadvantages:**
- Unpredictable (physics can glitch or behave unexpectedly)
- Performance cost (physics calculations are expensive)
- Requires extensive tuning (mass, friction, bounciness)

**Implementation Tips:**
- Use simplified collision meshes (primitive shapes, not detailed meshes)
- Tune physics properties (mass, drag, angular drag)
- Clamp velocities (prevent objects from flying at extreme speeds)
- Use physics layers (prevent unwanted collisions)
- Test extensively (physics bugs are common)

---

## UI and Menu Design

### Diegetic UI Patterns

**Wrist-Mounted UI:**
- **Implementation**: Attach UI canvas to wrist bone in VR rig
- **Activation**: Rotate wrist toward face, UI appears
- **Interaction**: Point with other hand, press trigger to select
- **Best For**: Quick access menus, health/ammo, map

**Over-Shoulder Inventory:**
- **Implementation**: Detect hand position behind shoulder, spawn inventory UI
- **Activation**: Reach hand over shoulder
- **Interaction**: Grab items as physical objects, pull to equip
- **Best For**: Weapon selection, item management

**Handheld Tablet:**
- **Implementation**: Spawn tablet object in hand when summoned
- **Activation**: Press menu button, tablet appears in hand
- **Interaction**: Hold tablet with one hand, interact with other
- **Best For**: Detailed information, maps, objectives

**In-World Terminals:**
- **Implementation**: Place UI canvas on in-world object (computer, screen)
- **Activation**: Approach terminal, UI becomes interactive
- **Interaction**: Point and click, or physical button presses
- **Best For**: Story exposition, settings, mission briefings

### World-Space UI

**What is World-Space UI?**
UI elements exist in 3D world space, not attached to player's head. Player can move around UI, view from different angles.

**Best Practices:**
- **Distance**: Place UI 1-3 meters from player (comfortable reading distance)
- **Size**: Large enough to read (minimum 24pt font at 1 meter)
- **Contrast**: High contrast (white on dark, or dark on light)
- **Interaction**: Point and click with hand/controller, or physical touch

**Button Design:**
- Large buttons (10-20cm in world space)
- Clear labels (text + icons)
- Visual feedback on hover (highlight, glow)
- Audio feedback on press (click sound)
- Haptic feedback on press (controller vibration)

**Text Readability:**
- Minimum font size: 24pt at 1 meter distance
- Use bold or medium weight fonts (avoid thin fonts)
- High contrast (white on black, or black on white)
- Avoid small text (causes eye strain)
- Test on target headset (resolution varies)

### Avoiding Common UI Mistakes

**Don't:**
- Attach UI to player's head (causes discomfort, hard to read)
- Use tiny text or buttons (eye strain, hard to interact)
- Place UI too close (<0.5m) or too far (>10m)
- Use low contrast (hard to read)
- Overload UI with information (cognitive overload)

**Do:**
- Use diegetic UI (in-world, contextual)
- Place UI at comfortable distance (1-3m)
- Use large, clear text and buttons
- Provide visual, audio, and haptic feedback
- Test UI readability on target headset

---

## Haptic Feedback

### Importance of Haptics in VR

Haptic feedback (controller vibration) is critical for immersion and usability in VR. It provides tactile confirmation of interactions and enhances presence.

**When to Use Haptics:**
- Object grab (confirm grip)
- Button press (confirm selection)
- Collision (object hits surface)
- Weapon fire (recoil)
- Tool use (sawing, drilling, hammering)
- Environmental effects (rain, wind, explosions)

### Haptic Patterns

**Short Pulse (50-100ms):**
- Button press, UI selection
- Light touch or tap
- Confirmation feedback

**Medium Pulse (100-300ms):**
- Object grab or release
- Collision with object
- Tool activation

**Long Pulse (300-1000ms):**
- Sustained action (holding button, charging weapon)
- Environmental effect (rain, wind)
- Damage or impact

**Rhythmic Pulse:**
- Heartbeat (low health)
- Engine vibration (vehicle)
- Machinery operation

**Variable Intensity:**
- Light touch: Low intensity (10-30%)
- Medium impact: Medium intensity (30-70%)
- Heavy impact: High intensity (70-100%)

### Platform-Specific Haptics

**Meta Quest (Touch Controllers):**
- Single vibration motor per controller
- Amplitude control (0-1)
- Frequency control (0-1)
- Simple but effective

**PSVR2 (Sense Controllers):**
- Advanced haptics (similar to DualSense)
- Adaptive triggers (variable resistance)
- Precise vibration control
- Best haptics in consumer VR

**Valve Index (Index Controllers):**
- Linear actuators (precise, high-fidelity)
- Finger tracking (individual finger haptics)
- Best haptics in PC VR

**Implementation:**
- Use platform SDKs for haptic control
- Test haptics on target hardware (feels different on each platform)
- Don't overuse (constant vibration is annoying)
- Match haptic intensity to action (light touch = light haptic)

---

## Spatial Audio and Sound Design

### Importance of Spatial Audio in VR

Spatial audio (3D audio) is critical for immersion and navigation in VR. Players use sound to locate objects, enemies, and events.

**Spatial Audio Features:**
- **Directionality**: Sound comes from specific direction (left, right, front, back, above, below)
- **Distance**: Sound volume decreases with distance
- **Occlusion**: Sound muffled when blocked by objects
- **Reverb**: Sound reflects off surfaces (room acoustics)
- **HRTF (Head-Related Transfer Function)**: Simulates how ears perceive 3D sound

### Implementing Spatial Audio

**Unity:**
- Use Unity's built-in spatial audio (Audio Source → Spatial Blend = 1)
- Enable "Spatialize" on Audio Source
- Use Oculus Spatializer or Steam Audio for advanced features

**Unreal:**
- Use Unreal's built-in spatial audio (Attenuation Settings)
- Enable "Spatialization" on Sound Cue
- Use Steam Audio or Oculus Audio SDK for advanced features

**Best Practices:**
- Use spatial audio for all 3D sounds (footsteps, gunfire, ambient)
- Use 2D audio for UI sounds (button clicks, menu navigation)
- Test audio with headphones (spatial audio requires stereo)
- Use HRTF for best results (platform-specific)

### Audio Cues for Interaction

**Feedback Sounds:**
- **Grab**: Soft "grab" sound when picking up object
- **Release**: Soft "release" sound when dropping object
- **Button Press**: Click or beep when pressing UI button
- **Collision**: Impact sound when objects collide
- **Weapon Fire**: Gunshot, explosion, or impact sound

**Ambient Sounds:**
- **Environment**: Wind, rain, birds, machinery
- **Footsteps**: Player and NPC footsteps (spatial)
- **Music**: Background music (2D, not spatial)

**Directional Cues:**
- **Enemy Location**: Footsteps, breathing, weapon sounds
- **Objective Location**: Beeping, humming, or voice cues
- **Danger**: Alarm, explosion, or warning sound

---

## Advanced Interaction Techniques

### Finger Tracking (Valve Index, Quest Pro)

**Capabilities:**
- Track individual finger positions
- Detect gestures (point, thumbs up, peace sign)
- Enable more natural hand poses

**Use Cases:**
- Social VR (hand gestures for communication)
- Precise interaction (point at small objects)
- Immersion (realistic hand poses)

**Implementation:**
- Use platform SDKs (Oculus Integration, SteamVR)
- Animate virtual hands based on finger positions
- Detect gestures for custom interactions

### Eye Tracking (PSVR2, Quest Pro, Vision Pro)

**Capabilities:**
- Track where player is looking
- Detect gaze direction and focus point
- Enable foveated rendering (performance boost)

**Use Cases:**
- **Foveated Rendering**: Render only foveal area at full resolution (30-50% performance boost)
- **Gaze-Based Interaction**: Select objects by looking at them
- **Social VR**: Realistic eye contact and gaze direction
- **Analytics**: Track what players look at (heatmaps)

**Implementation:**
- Use platform SDKs (PSVR2 SDK, Meta XR SDK, visionOS SDK)
- Enable foveated rendering in graphics settings
- Use gaze raycast for interaction (alternative to hand pointing)

### Passthrough AR (Quest 3, Vision Pro)

**Capabilities:**
- See real world through headset cameras
- Blend virtual objects with real environment
- Enable mixed reality experiences

**Use Cases:**
- **Mixed Reality Games**: Virtual objects in real room
- **Furniture Placement**: Preview virtual furniture in real space
- **Social VR**: See real people while in VR
- **Safety**: See real obstacles while in VR

**Implementation:**
- Use platform SDKs (Meta XR SDK, visionOS SDK)
- Enable passthrough in settings
- Use spatial anchors to place virtual objects in real space
- Test in various lighting conditions (passthrough quality varies)

---

## Conclusion

VR interaction design requires rethinking traditional game design principles. Prioritize physicality, natural gestures, and diegetic UI to create immersive experiences. Use haptic feedback and spatial audio to reinforce interactions. Test extensively with real users to validate comfort and usability. By following these principles, developers can create intuitive, immersive VR interactions that feel natural and satisfying.