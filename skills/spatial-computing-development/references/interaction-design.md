# Spatial Interaction Design for XR

Comprehensive guide to designing natural, intuitive, and comfortable interactions for spatial computing applications across AR, VR, MR, and XR platforms.

## Table of Contents
1. [Principles of Spatial Interaction Design](#principles-of-spatial-interaction-design)
2. [Interaction Modalities](#interaction-modalities)
3. [Proxemics and Spatial Arrangement](#proxemics-and-spatial-arrangement)
4. [Field of View and Content Placement](#field-of-view-and-content-placement)
5. [Depth, Scale, and Spatial Perception](#depth-scale-and-spatial-perception)
6. [Multisensory Engagement](#multisensory-engagement)
7. [Comfort and Accessibility](#comfort-and-accessibility)
8. [UI/UX Patterns for Spatial Computing](#ui-ux-patterns-for-spatial-computing)

## Principles of Spatial Interaction Design

### Design for Natural Interactions

Spatial computing enables interaction methods that mimic real-world behaviors, reducing cognitive load and learning curves.

**Core principles:**

**1. Leverage affordances:**
- Make interactive elements appear grabbable, pushable, or actionable
- Use visual cues (highlights, outlines, animations) to indicate interactivity
- Avoid "secret UIs" or hidden features requiring discovery
- Example: A virtual door handle should look and behave like a real door handle

**2. Minimize abstract interfaces:**
- Reduce reliance on traditional 2D menus and buttons
- Prefer direct manipulation of 3D objects
- Use spatial metaphors (shelves for organization, drawers for storage)
- Reserve 2D UI for complex input (text entry, settings)

**3. Provide immediate feedback:**
- Visual feedback: Highlight, color change, animation
- Audio feedback: Spatial sound confirming action
- Haptic feedback: Vibration for tactile confirmation (controllers)
- Multimodal feedback: Combine visual, audio, and haptic for critical actions

**4. Design for context intelligence:**
- Adapt UI based on user's physical environment
- Adjust brightness, contrast, and interaction methods for lighting conditions
- Respond to user's posture (seated, standing, moving)
- Provide contextual help based on user behavior

**5. Respect real-world physics:**
- Digital objects should behave according to physical laws (gravity, momentum, friction)
- Example: A rubber ball should bounce realistically
- Exceptions allowed for "magical" interactions (teleportation, scaling)
- Consistency is key: establish rules and follow them

### Design for Scenes, Not Screens

Spatial computing treats the environment as an "infinite canvas," freeing designers from screen constraints.

**Spatial composition principles:**
- **Scenery**: Background elements, environmental context
- **Lighting**: Mood, focus, depth perception
- **Props**: Interactive objects, tools, content
- **Sound**: Spatial audio, environmental ambiance, feedback
- **Actors**: Users, avatars, NPCs, animated characters

**Considerations:**
- Design for 360° environments (VR) or augmented spaces (AR/MR)
- Consider user spawn points and initial orientation
- Create clear visual hierarchies using depth, scale, and lighting
- Provide environmental storytelling through spatial arrangement

## Interaction Modalities

### Gaze and Eye Tracking

**Overview**: Eye tracking enables selection and interaction by looking at objects, providing a natural, hands-free input method.

**Implementation:**
- Track eye position and gaze direction
- Detect fixations (sustained gaze on target)
- Combine with secondary confirmation (pinch, voice, dwell time)

**Best practices:**

**Do:**
- Use gaze for implicit navigation (UI follows gaze)
- Combine gaze with explicit confirmation (avoid accidental selection)
- Provide visual feedback when gaze is detected (subtle highlight)
- Use gaze for foveated rendering (performance optimization)
- Implement dwell time for hands-free selection (1-2 seconds)

**Don't:**
- Require sustained gaze (causes eye fatigue)
- Use gaze alone for critical actions (combine with confirmation)
- Track gaze without user consent (privacy concerns)
- Assume perfect accuracy (provide generous hit targets)

**Privacy considerations:**
- Apple restricts direct gaze data access (privacy protection)
- Gaze data available only during explicit interactions
- Inform users when gaze tracking is active
- Provide opt-out for gaze-based features

**Use cases:**
- Menu navigation and selection
- Object highlighting and inspection
- Attention analytics (where users look)
- Foveated rendering (render high-res where user looks)
- Accessibility (hands-free interaction)

### Hand Gestures

**Overview**: Hand tracking enables natural, controller-free interaction using computer vision to detect hand pose and gestures.

**Common gestures:**

**Pinch (thumb + index finger):**
- **Action**: Select, grab, confirm
- **Use cases**: Menu selection, object picking, UI interaction
- **Feedback**: Visual highlight, haptic (if available), audio confirmation

**Grab (closed fist):**
- **Action**: Grab and hold object
- **Use cases**: Object manipulation, dragging, throwing
- **Feedback**: Object attaches to hand, visual grip indicator

**Point (extended index finger):**
- **Action**: Direct selection, raycast
- **Use cases**: Distant object selection, UI interaction, drawing
- **Feedback**: Ray visualization, target highlight

**Swipe (hand movement):**
- **Action**: Navigate, scroll, dismiss
- **Use cases**: Menu navigation, content browsing, page turning
- **Feedback**: Content movement, animation

**Palm up (open hand facing up):**
- **Action**: Summon menu, request information
- **Use cases**: Context menu, help, inventory
- **Feedback**: Menu appears above hand

**Two-handed gestures:**
- **Pinch and pull**: Scale object (pinch with both hands, move apart/together)
- **Two-hand rotate**: Rotate object (grab with both hands, rotate)
- **Clap**: Special action, attention-getting

**Best practices:**

**Do:**
- Provide visual feedback for gesture recognition (hand outlines, skeleton)
- Design for gesture fatigue ("gorilla arm" syndrome from extended arm use)
- Support both hands for complex interactions
- Provide controller fallback for accessibility
- Use simple, discoverable gestures (avoid complex multi-step gestures)
- Implement gesture tutorials (contextual, on-demand)

**Don't:**
- Require sustained arm extension (causes fatigue)
- Use overly complex gestures (hard to remember, execute)
- Rely solely on hand tracking (provide controller support)
- Ignore gesture recognition failures (provide clear error feedback)

**Gesture recognition challenges:**
- Occlusion (hands behind objects, out of camera view)
- Lighting conditions (low light, bright sunlight)
- Hand size and shape variations
- Cultural gesture differences

**Use cases:**
- Object manipulation (grab, move, rotate, scale)
- UI interaction (buttons, sliders, toggles)
- Spatial drawing and annotation
- Measurement and spatial tools
- Social gestures (wave, thumbs up)

### Voice Commands

**Overview**: Voice input enables hands-free, natural language interaction, complementing visual and gestural interfaces.

**Implementation:**
- Speech recognition (convert speech to text)
- Natural language processing (understand intent)
- Contextual commands (adapt to current activity)
- Multimodal integration (combine with gaze, gestures)

**Best practices:**

**Do:**
- Support conversational patterns, not just keywords
- Provide visual confirmation of voice input (transcription, command recognized)
- Design for noisy environments (provide visual alternatives)
- Integrate with gaze for "look and speak" interactions
- Implement wake words or push-to-talk for privacy
- Support multiple languages and accents

**Don't:**
- Require exact phrasing (support natural variations)
- Use voice as only input method (provide alternatives)
- Ignore recognition errors (provide correction mechanism)
- Activate voice input without user consent

**Use cases:**
- Navigation ("Go to settings", "Show menu")
- Content search ("Find red objects", "Search for documents")
- Accessibility (hands-free operation for users with limited mobility)
- Dictation (text entry, notes)
- Commands during hands-busy tasks ("Next step", "Zoom in")

**Challenges:**
- Background noise interference
- Accent and language variations
- Privacy concerns (always-listening devices)
- Social awkwardness (speaking in public)

### Controller Input

**Overview**: Physical controllers provide precise, reliable input with haptic feedback, ideal for gaming and complex interactions.

**Controller types:**

**Motion controllers (Meta Quest Touch, Valve Index Controllers):**
- 6DOF tracking (position and rotation)
- Buttons, triggers, thumbsticks, grip buttons
- Haptic feedback (vibration)
- Hand presence (detect when controller is held)

**Game controllers (Xbox, PlayStation):**
- Traditional gamepad layout
- Familiar for gaming experiences
- Limited spatial tracking (3DOF or none)
- Supported by Vision Pro, Quest, PC VR

**Best practices:**

**Do:**
- Map intuitive actions to buttons (trigger for grab, grip for menu)
- Provide haptic feedback for tactile confirmation
- Support both controller and hand tracking simultaneously
- Design for one-handed and two-handed interactions
- Display controller tooltips (button mappings)
- Allow button remapping for accessibility

**Don't:**
- Overload buttons with multiple functions (causes confusion)
- Require simultaneous multi-button presses (difficult to execute)
- Ignore controller battery status (warn before depletion)
- Assume all users have controllers (provide hand tracking alternative)

**Common button mappings:**
- **Trigger**: Primary action (grab, shoot, select)
- **Grip**: Secondary action (menu, tool switch)
- **Thumbstick**: Locomotion (movement, rotation)
- **Face buttons**: Context-specific actions (jump, crouch, interact)
- **Menu button**: Pause, settings, system menu

**Use cases:**
- Gaming (precise aiming, complex controls)
- Precise manipulation (CAD, 3D modeling)
- Legacy VR experiences (designed for controllers)
- Haptic feedback requirements (tactile confirmation)

## Proxemics and Spatial Arrangement

### Proxemic Zones

Proxemics is the study of personal space and how humans use distance in social interactions. In spatial computing, content placement should respect comfortable interaction distances.

**Intimate space (0-1.5 feet / 0-0.5 meters):**
- **Characteristics**: Reserved for highly personal items, "lean-in" experiences
- **Content types**: Private information, detailed inspection, personal items
- **Interaction**: Close examination, fine manipulation
- **Examples**: Watch face, personal notes, jewelry inspection
- **Considerations**: Requires high resolution, precise tracking

**Personal space (1.5-4 feet / 0.5-1.2 meters):**
- **Characteristics**: Arm's reach, primary interaction zone
- **Content types**: Primary UI, interactive objects, tools
- **Interaction**: Direct manipulation, hand gestures, controller input
- **Examples**: Menus, buttons, grabbable objects, virtual keyboard
- **Considerations**: Most comfortable for sustained interaction

**Social space (4-12 feet / 1.2-3.6 meters):**
- **Characteristics**: Collaborative distance, "lean-out" experiences
- **Content types**: Shared visualizations, collaborative content, presentations
- **Interaction**: Pointing, gaze, voice commands
- **Examples**: Shared whiteboards, data visualizations, virtual meetings
- **Considerations**: Larger UI elements, clear visual hierarchy

**Public space (12-25+ feet / 3.6-7.6+ meters):**
- **Characteristics**: Environmental content, passive information
- **Content types**: Large-scale visualizations, environmental storytelling, signage
- **Interaction**: Gaze, voice, minimal direct interaction
- **Examples**: Virtual billboards, architectural models, landscape visualization
- **Considerations**: Very large UI elements, high contrast, minimal detail

**Design implications:**
- Place critical UI in personal space (1.5-4 feet)
- Use intimate space sparingly (requires user to lean in)
- Reserve social space for collaborative and shared content
- Use public space for environmental context, not primary interaction

### Spatial Arrangement Strategies

**Radial layout:**
- Content arranged in arc around user
- Equal distance from user to all elements
- Ideal for menus, toolbars, content galleries
- Minimizes head rotation

**Layered depth:**
- Content at multiple depth planes
- Foreground: Primary UI, active content
- Midground: Secondary content, context
- Background: Environmental elements, passive information
- Creates visual hierarchy, guides attention

**Spatial anchoring:**
- Content fixed to physical locations (AR/MR)
- Persistent across sessions
- Respects real-world geometry
- Examples: Notes on walls, virtual monitors on desks

**Body-relative positioning:**
- Content follows user (head-locked, body-locked)
- Always accessible, no searching
- Can cause discomfort if overused (motion sickness)
- Use sparingly for critical UI (health bar, notifications)

**World-locked positioning:**
- Content fixed in world space
- User moves around content
- Natural for VR environments
- Requires spatial memory (user must remember locations)

## Field of View and Content Placement

### Human Field of View

**Horizontal FOV:**
- Total: ~200° (peripheral vision)
- Binocular: ~114° (both eyes)
- Comfortable focus: ±30° from center
- Optimal UI placement: ±15° from center

**Vertical FOV:**
- Total: ~135° (60° up, 75° down)
- Comfortable focus: ±20° from center
- Optimal UI placement: Slightly above center (10-20° up)
- Reason: Natural gaze direction is slightly downward

### Content Placement Guidelines

**Primary content (critical UI, main interactions):**
- **Horizontal**: ±15° from center
- **Vertical**: 0-20° above center
- **Distance**: 1.5-3 feet (personal space)
- **Rationale**: Minimal head movement, comfortable gaze

**Secondary content (contextual information, tools):**
- **Horizontal**: ±30° from center
- **Vertical**: ±20° from center
- **Distance**: 2-4 feet
- **Rationale**: Accessible with slight head turn

**Tertiary content (environmental, passive information):**
- **Horizontal**: ±60° from center (requires head turn)
- **Vertical**: ±40° from center
- **Distance**: 4+ feet
- **Rationale**: Peripheral awareness, not primary focus

**Avoid:**
- Placing critical UI at extreme angles (requires uncomfortable head rotation)
- Content directly above or below (neck strain)
- Content too close (<1 foot, causes eye strain)
- Content too far (>12 feet, hard to read)

### Dynamic UI Repositioning

**User-initiated repositioning:**
- Allow users to move, resize, and reposition UI elements
- Provide "reset to default" option
- Save user preferences across sessions

**Automatic repositioning:**
- Reposition UI when user changes posture (seated ↔ standing)
- Move UI back into view if user turns away
- Adjust distance based on content type (closer for reading, farther for visualization)

**Comfort-driven adjustments:**
- Detect prolonged head rotation, suggest UI repositioning
- Adjust UI height for seated vs. standing users
- Provide "comfort mode" with all UI in optimal zones

## Depth, Scale, and Spatial Perception

### Depth Cues

Spatial computing leverages multiple depth cues to create convincing 3D perception:

**Stereoscopic depth (binocular disparity):**
- Different images for each eye create depth perception
- Most powerful depth cue for nearby objects (<20 feet)
- Requires accurate interpupillary distance (IPD) calibration

**Motion parallax:**
- Closer objects move faster than distant objects when user moves
- Reinforces depth perception during movement
- Critical for VR presence

**Occlusion:**
- Closer objects block view of distant objects
- Requires accurate depth ordering and rendering
- Essential for realistic AR/MR (digital objects behind physical objects)

**Shadows:**
- Cast shadows indicate object position relative to surfaces
- Contact shadows (where object touches surface) are critical
- Soft shadows more realistic than hard shadows

**Atmospheric perspective:**
- Distant objects appear hazier, lower contrast, bluer
- Simulates light scattering in atmosphere
- Effective for large-scale environments

**Relative size:**
- Known objects (people, furniture) provide scale reference
- Smaller appearance indicates greater distance
- Important for unfamiliar objects

**Texture gradient:**
- Texture detail decreases with distance
- Use mipmapping and LOD for realistic rendering

### Scale Strategies

**Dynamic scaling:**
- Content resizes based on distance to maintain consistent legibility
- Text and UI elements scale up when farther away
- Prevents content from becoming unreadable at distance
- Example: Menu at 2 feet vs. 6 feet appears same size

**Fixed scaling:**
- Objects maintain real-world size regardless of distance
- Appear smaller when farther away (realistic)
- Important for spatial understanding and measurement
- Example: Virtual furniture maintains actual dimensions

**Adaptive scaling:**
- Combine dynamic and fixed scaling based on content type
- UI elements: Dynamic scaling (always readable)
- 3D objects: Fixed scaling (realistic size perception)
- Annotations: Dynamic scaling (always legible)

**Scale manipulation:**
- Allow users to scale objects for inspection or space-saving
- Provide visual indicators of scale (grid, ruler, reference objects)
- Maintain aspect ratio during scaling (avoid distortion)
- Implement scale limits (prevent too small or too large)

### Spatial Audio for Depth Perception

**3D audio positioning:**
- Sound originates from object's spatial location
- Reinforces visual depth cues
- Enables audio-only localization (eyes-free interaction)

**Distance attenuation:**
- Volume decreases with distance (inverse square law)
- Provides auditory depth cue
- Adjustable falloff curves per sound type

**Environmental effects:**
- Reverb indicates room size and material
- Occlusion muffles sound behind objects
- Enhances spatial realism

## Multisensory Engagement

### Visual Feedback

**Highlights and outlines:**
- Indicate interactive elements
- Show selection state (hover, selected, active)
- Use color, brightness, or outline thickness

**Animations:**
- Smooth transitions between states
- Indicate progress (loading, processing)
- Provide visual interest and polish

**Particle effects:**
- Confirm actions (sparkles on selection)
- Indicate state changes (smoke on destruction)
- Add visual flair

**Color coding:**
- Consistent color meanings (green = success, red = error)
- Accessibility: Don't rely solely on color (use icons, text)
- Cultural considerations (color meanings vary)

### Auditory Feedback

**Confirmation sounds:**
- Button clicks, selection beeps
- Distinct sounds for different actions
- Spatial audio (sound from object location)

**Ambient audio:**
- Environmental soundscapes
- Enhances immersion and presence
- Provides context (indoor vs. outdoor, time of day)

**Voice feedback:**
- Spoken confirmations and instructions
- Accessibility (screen reader equivalent)
- Multimodal (combine with visual feedback)

### Haptic Feedback

**Controller vibration:**
- Tactile confirmation of actions
- Varying intensity and duration for different events
- Enhances realism (feeling virtual objects)

**Haptic patterns:**
- Distinct patterns for different actions (short pulse for button, long vibration for error)
- Rhythmic patterns for ongoing processes (heartbeat for health)

**Limitations:**
- Hand tracking lacks haptic feedback (no physical controller)
- Haptic gloves and suits emerging but not mainstream

### Advanced Sensory Engagement

**Olfactory (smell):**
- Emerging technology (scent generators)
- Enhances realism (smell of forest, ocean)
- Limited availability, high cost

**Gustatory (taste):**
- Experimental (taste simulation devices)
- Very limited applications

**Vestibular (balance):**
- Motion platforms (simulate movement)
- Enhances immersion for vehicles, roller coasters
- Expensive, limited to location-based experiences

**Proprioception (body awareness):**
- Full-body tracking (Vive Trackers, mocap suits)
- Avatar embodiment (seeing virtual body)
- Enhances presence and social interaction

## Comfort and Accessibility

### Motion Sickness Prevention

**Causes of VR motion sickness:**
- Sensory conflict (visual motion without physical motion)
- Low frame rate (<90fps)
- High latency (>20ms motion-to-photon)
- Artificial locomotion (smooth movement without walking)
- Acceleration and rotation

**Mitigation strategies:**

**Maintain high frame rate:**
- Target 90fps minimum (120fps preferred)
- Never drop below 90fps (causes immediate discomfort)
- Use dynamic resolution scaling to maintain frame rate

**Minimize artificial locomotion:**
- Prefer teleportation over smooth movement
- Use snap turning (discrete 30-45° turns) over smooth rotation
- Provide comfort options (vignetting, reduced FOV during movement)

**Reduce acceleration:**
- Constant velocity movement (no acceleration/deceleration)
- Instant start/stop (no ramp-up/ramp-down)
- Avoid camera shake and head bobbing

**Provide static reference frame:**
- Cockpit or vehicle interior (provides stable visual reference)
- Virtual nose (subtle, reduces motion sickness)
- Grid floor (stable ground plane)

**Comfort options:**
- Teleportation vs. smooth locomotion (user choice)
- Snap turning vs. smooth turning
- Vignetting during movement (reduce peripheral vision)
- Reduced FOV during movement (tunnel vision effect)
- Seated vs. standing mode

**User education:**
- Gradual exposure (start with short sessions)
- Take breaks at first sign of discomfort
- Build tolerance over time (VR legs)

### Accessibility Considerations

**Multiple input methods:**
- Support controllers, hand tracking, gaze, and voice
- Allow users to switch between input methods
- Provide alternatives for physical gestures

**Adjustable UI:**
- Scalable text and UI elements
- Repositionable UI (user-defined placement)
- High-contrast mode
- Colorblind modes (deuteranopia, protanopia, tritanopia)

**Seated and standing modes:**
- Support both seated and standing play
- Adjust UI height based on mode
- Provide seated alternatives for standing-only interactions

**Audio descriptions:**
- Describe visual content for visually impaired users
- Spatial audio cues for navigation
- Voice feedback for UI interactions

**Subtitles and captions:**
- Subtitles for all spoken content
- Spatial positioning (near speaker)
- Adjustable size, color, and background

**Reduced motion options:**
- Disable animations and transitions
- Static UI (no floating or moving elements)
- Teleportation-only locomotion

**One-handed mode:**
- Support one-handed play for users with limited mobility
- Remap two-handed interactions to single hand
- Provide alternative input methods (voice, gaze)

### Ergonomics and Physical Comfort

**Gorilla arm syndrome:**
- Fatigue from extended arm use
- Mitigation: Support arms-down interactions, provide rest periods, use gaze/voice for extended tasks

**Neck strain:**
- Avoid content placement requiring prolonged head rotation or tilting
- Keep primary UI in comfortable FOV (±30° horizontal, ±20° vertical)
- Provide UI repositioning options

**Eye strain:**
- Avoid content too close (<1 foot)
- Provide breaks for extended use
- Adjust brightness for environment
- Use proper IPD calibration

**Headset comfort:**
- Lightweight design (sub-500g ideal)
- Balanced weight distribution
- Adjustable straps and padding
- Ventilation to prevent overheating

## UI/UX Patterns for Spatial Computing

### Spatial Menus

**Radial menus:**
- Items arranged in circle around center
- Fast selection (gesture toward item)
- Limited items (6-8 optimal)
- Example: Tool selection, quick actions

**Hand menus:**
- Menu attached to user's hand
- Always accessible (look at hand to activate)
- Limited space (palm-sized)
- Example: Settings, inventory, quick tools

**World-space menus:**
- Floating panels in 3D space
- Can be large, detailed
- Requires spatial memory (user must remember location)
- Example: Settings panel, detailed information

**Contextual menus:**
- Appear near relevant object
- Context-specific options
- Disappear when not needed
- Example: Object properties, editing tools

### Object Manipulation

**Direct manipulation:**
- Grab object with hand or controller
- Move, rotate, scale naturally
- Provides immediate feedback
- Most intuitive interaction method

**Raycast selection:**
- Point at distant object with ray
- Select and manipulate from distance
- Useful for out-of-reach objects
- Example: Laser pointer, magic wand

**Gaze and pinch:**
- Look at object, pinch to select
- Hands-free selection
- Manipulation after selection (move hand to move object)
- Example: Apple Vision Pro primary interaction

**Two-handed manipulation:**
- Grab with both hands for rotation and scaling
- Pinch and pull apart to scale up
- Rotate hands to rotate object
- More precise than one-handed

### Locomotion

**Teleportation:**
- Point to destination, confirm to teleport
- No motion sickness (instant transition)
- Breaks immersion (not realistic)
- Best for: Comfort-focused experiences, large spaces

**Smooth locomotion:**
- Continuous movement (like walking)
- More immersive
- Can cause motion sickness
- Best for: Experienced VR users, small movements

**Snap turning:**
- Discrete rotation (30-45° increments)
- Reduces motion sickness vs. smooth turning
- Less immersive than smooth turning
- Best for: Comfort-focused experiences

**Room-scale walking:**
- Physical walking in tracked space
- Most immersive, no motion sickness
- Limited by physical space
- Best for: Small environments, standing experiences

**Arm swinging:**
- Swing arms to move forward (simulates walking)
- Reduces motion sickness (physical movement)
- Can cause arm fatigue
- Best for: Fitness experiences, exploration

### Notifications and Alerts

**Spatial notifications:**
- Appear in 3D space near relevant object
- Contextual and non-intrusive
- Example: "New message" near virtual phone

**Body-locked notifications:**
- Follow user's view (head-locked or body-locked)
- Always visible, can be intrusive
- Use sparingly for critical alerts
- Example: Low battery warning, incoming call

**Audio notifications:**
- Spatial audio from notification source
- Non-visual, doesn't block view
- Combine with visual for important alerts

**Haptic notifications:**
- Controller vibration for alerts
- Subtle, non-intrusive
- Combine with visual/audio for critical alerts

---

**Key Takeaways:**
- Design for natural interactions leveraging affordances and real-world physics
- Respect proxemic zones: place primary UI in personal space (1.5-4 feet)
- Keep critical content within comfortable FOV (±30° horizontal, ±20° vertical)
- Use multiple depth cues (stereoscopy, shadows, occlusion) for spatial perception
- Provide multisensory feedback (visual, audio, haptic) for all interactions
- Prioritize comfort: maintain 90fps+, minimize artificial locomotion, provide comfort options
- Design for accessibility: support multiple input methods, adjustable UI, seated/standing modes
- Use spatial UI patterns (radial menus, direct manipulation, teleportation) for intuitive experiences
