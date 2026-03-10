# Interactive VR Development

Building interactive 360° experiences with hotspots, navigation, and user interaction.

---

## Interactive VR Platforms

### No-Code Platforms

#### WondaVR
- **Best For**: Training, corporate VR
- **Features**: Branching, quizzes, analytics
- **Publish To**: Web, Quest, custom apps
- **Pricing**: Subscription-based

#### InstaVR
- **Best For**: Virtual tours, marketing
- **Features**: Hotspots, transitions, GPS
- **Publish To**: iOS, Android, web, headsets
- **Pricing**: Per-project or subscription

#### Kuula
- **Best For**: Real estate tours
- **Features**: Simple hotspots, floor plans
- **Publish To**: Web embed, native apps
- **Pricing**: Free tier + premium

#### Matterport
- **Best For**: Real estate, AEC
- **Features**: 3D dollhouse, measurements
- **Publish To**: Web, iOS, Android
- **Pricing**: Subscription + capture

### Code-Based Frameworks

#### A-Frame (Web)
```html
<a-scene>
  <a-sky src="360-image.jpg"></a-sky>
  <a-entity position="0 1.6 -3">
    <a-box color="red" 
           animation="property: rotation; to: 0 360 0; loop: true">
    </a-box>
  </a-entity>
</a-scene>
```
- **Language**: HTML + JavaScript
- **VR Support**: WebXR (all headsets via browser)
- **Learning Curve**: Low
- **Best For**: Web-based 360 experiences

#### React 360 (Deprecated → React VR)
- **Language**: JavaScript/React
- **Status**: Use A-Frame or Three.js instead

#### Unity + XR Toolkit
- **Best For**: Full VR applications
- **Features**: Complete game engine
- **Publish To**: All major headsets
- **Learning Curve**: Medium-High

#### Unreal Engine
- **Best For**: Cinematic VR, high fidelity
- **Features**: Advanced rendering
- **Learning Curve**: High

---

## Hotspot Implementation

### Types of Hotspots
1. **Navigation**: Move to another scene/location
2. **Information**: Display text/image popup
3. **Video**: Play embedded video
4. **Audio**: Trigger sound/narration
5. **Action**: Execute custom function

### Hotspot Design Principles
- **Visibility**: Clear visual affordance
- **Placement**: Eye level, comfortable viewing zone
- **Feedback**: Hover/gaze states
- **Accessibility**: Consider gaze duration

### Hotspot Positioning
```javascript
// Converting spherical to Cartesian
function sphericalToCartesian(yaw, pitch, radius) {
  return {
    x: radius * Math.sin(yaw) * Math.cos(pitch),
    y: radius * Math.sin(pitch),
    z: radius * Math.cos(yaw) * Math.cos(pitch)
  };
}
```

---

## Gaze-Based Interaction

### Implementation Pattern
1. Cast ray from camera center
2. Detect intersection with interactive elements
3. Start timer on gaze entry
4. Trigger action after dwell time (1.5-2s typical)
5. Provide visual feedback (radial timer)

### A-Frame Gaze Cursor
```html
<a-entity camera look-controls>
  <a-cursor fuse="true" 
            fuse-timeout="1500"
            color="white"
            scale="0.5 0.5 0.5">
  </a-cursor>
</a-entity>
```

### Gaze UX Best Practices
- Minimum dwell time: 1.5 seconds
- Visual progress indicator essential
- Cancel on gaze exit
- Audio feedback on activation

---

## Branching Narratives

### Structure Types
| Type | Description | Use Case |
|------|-------------|----------|
| Linear | Single path | Documentaries |
| Binary choice | Two options per branch | Simple stories |
| Multi-branch | Multiple options | Training, games |
| Hub and spoke | Central location + branches | Virtual tours |
| Open world | Free exploration | Complex environments |

### Design Considerations
- Map all paths before production
- Consider replay value
- Track user choices for analytics
- Provide navigation aids

### Implementation Example (Pseudo-code)
```javascript
const storyGraph = {
  'intro': {
    video: 'intro.mp4',
    choices: [
      { label: 'Go left', target: 'path_a' },
      { label: 'Go right', target: 'path_b' }
    ]
  },
  'path_a': {
    video: 'path_a.mp4',
    choices: [
      { label: 'Continue', target: 'ending_1' }
    ]
  }
};
```

---

## Hand Tracking Integration

### Supported Platforms
- Meta Quest 2/3/Pro: Native hand tracking
- Apple Vision Pro: Full hand/eye tracking
- Ultraleap: Add-on for PC VR

### Gesture Recognition
| Gesture | Common Action |
|---------|---------------|
| Pinch | Select/click |
| Point | Raycast/aim |
| Open palm | Menu/pause |
| Grab | Move objects |
| Thumbs up | Confirm |

### Unity XR Hands Setup
```csharp
// Basic hand tracking setup
using UnityEngine.XR.Hands;

void Start() {
    var handSubsystem = XRHandSubsystemProvider.GetSubsystem();
    handSubsystem.updatedHands += OnHandsUpdated;
}
```

---

## Scene Transitions

### Transition Types
1. **Fade to black**: Standard, reduces motion sickness
2. **Cross-fade**: Blend between scenes
3. **Portal**: Walk through visual portal
4. **Teleport**: Instant with visual effect
5. **Spatial**: Physical movement in VR space

### Motion Sickness Prevention
- Always use fade transitions for camera moves
- Avoid artificial locomotion
- Provide stationary reference points
- Allow user control over movement

### A-Frame Transition Example
```javascript
// Fade transition between scenes
function fadeTransition(targetScene) {
  const fade = document.querySelector('#fade');
  fade.emit('fadeout');
  setTimeout(() => {
    loadScene(targetScene);
    fade.emit('fadein');
  }, 1000);
}
```

---

## Analytics and Tracking

### Key Metrics
- **Heatmaps**: Where users look
- **Dwell time**: Time spent per scene
- **Interaction rate**: Hotspot engagement
- **Drop-off points**: Where users exit
- **Path analysis**: Branching choices

### Implementation Tools
- **Google Analytics**: Basic tracking
- **Cognitive3D**: VR-specific analytics
- **WondaVR**: Built-in analytics
- **Custom**: WebXR + custom events

### Heatmap Data Collection
```javascript
// Track gaze direction every second
setInterval(() => {
  const camera = document.querySelector('[camera]');
  const rotation = camera.getAttribute('rotation');
  sendAnalytics('gaze', {
    yaw: rotation.y,
    pitch: rotation.x,
    timestamp: Date.now()
  });
}, 1000);
```

---

## Publishing Considerations

### Web Deployment
- Host on HTTPS (required for WebXR)
- Optimize assets for bandwidth
- Progressive loading for large scenes
- Fallback for non-VR browsers

### Native App Deployment
- Submit to Meta Quest Store
- Apple Vision Pro App Store review
- Consider sideloading options

### Cross-Platform Testing
- Test on target devices
- Verify performance benchmarks
- Check interaction methods
- Validate accessibility features
