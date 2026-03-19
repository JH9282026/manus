# Development Platforms for Spatial Computing

Comprehensive guide to selecting and using development platforms, tools, and SDKs for creating spatial computing applications across AR, VR, MR, and XR devices.

## Table of Contents
1. [Platform Selection Criteria](#platform-selection-criteria)
2. [Unity for XR Development](#unity-for-xr-development)
3. [Unreal Engine for XR Development](#unreal-engine-for-xr-development)
4. [Native Platform Development](#native-platform-development)
5. [WebXR Development](#webxr-development)
6. [Specialized Platforms](#specialized-platforms)
7. [Cross-Platform Development Strategy](#cross-platform-development-strategy)
8. [Development Tools and SDKs](#development-tools-and-sdks)

## Platform Selection Criteria

### Decision Matrix

Choose your development platform based on project requirements:

| Criterion | Unity | Unreal Engine | Native (Xcode) | WebXR |
|-----------|-------|---------------|----------------|-------|
| **Cross-platform support** | Excellent | Good | Poor | Excellent |
| **Graphics fidelity** | Good | Excellent | Excellent | Fair |
| **Learning curve** | Moderate | Steep | Moderate | Easy-Moderate |
| **Asset ecosystem** | Extensive | Growing | Limited | Moderate |
| **Performance** | Good | Excellent | Excellent | Fair-Good |
| **Rapid prototyping** | Excellent | Good | Fair | Excellent |
| **Enterprise support** | Excellent | Good | Good | Limited |
| **Build size** | Moderate | Large | Small-Moderate | Small |
| **Cost** | Free-Paid | Free (5% royalty) | Free | Free |

### Use Case Recommendations

**Choose Unity for:**
- Cross-platform XR applications (Quest, Vision Pro, Android XR)
- Mobile XR (ARKit, ARCore)
- Rapid prototyping and iteration
- Projects requiring extensive asset library
- Teams with C# expertise
- Enterprise training and simulation
- Most commercial XR projects (70% market share)

**Choose Unreal Engine for:**
- High-fidelity graphics and photorealism
- Architectural visualization
- PC-tethered VR experiences
- Cinematic VR experiences
- Projects requiring advanced rendering (ray tracing, Nanite, Lumen)
- Teams with C++ expertise
- AAA game development

**Choose Native Development (Xcode) for:**
- Vision Pro-exclusive applications
- Deep visionOS integration
- Productivity and utility apps
- Maximum performance on Apple hardware
- Access to latest Apple platform features
- Swift/SwiftUI expertise

**Choose WebXR for:**
- Browser-based XR experiences
- Marketing and promotional content
- Product visualization and demos
- Maximum accessibility (no app installation)
- Cross-device compatibility
- Rapid deployment and updates

## Unity for XR Development

### Overview

Unity is the industry-standard platform for XR development, powering over 70% of applications on Meta Quest and Android XR stores. It offers comprehensive cross-platform support, extensive documentation, and a mature ecosystem.

### Unity XR Architecture

**Core packages:**

**XR Plugin Management:**
- Centralized management of XR SDKs
- Enables/disables platform-specific plugins
- Handles XR subsystem lifecycle

**XR Interaction Toolkit:**
- High-level interaction system
- Supports controllers, hand tracking, gaze
- Provides locomotion, UI interaction, object manipulation
- Extensible architecture for custom interactions

**XR Hands:**
- Cross-platform hand tracking API
- 21+ joint tracking per hand
- Gesture recognition support
- Works with OpenXR and platform-specific SDKs

**Input System:**
- Modern input handling (replaces legacy Input Manager)
- Action-based input mapping
- Device-agnostic input abstraction
- Supports XR controllers, hands, gaze

### Platform-Specific Unity Support

#### Apple Vision Pro (visionOS)

**Required packages:**
- `com.unity.xr.visionos`: Core visionOS support
- `com.unity.polyspatial.visionos`: Mixed reality support
- `com.unity.polyspatial.xr`: XR integration for PolySpatial

**Development requirements:**
- Unity 2022.3 LTS or later
- Mac with Apple Silicon (M1/M2/M3)
- Xcode 15 Beta 2 or later
- visionOS SDK

**App modes:**

**Windows (2D/3D content without stereo):**
- Runs in Shared Space (multitasking environment)
- Can display 2D UI or 3D objects
- Limited immersion

**Volumes (3D content):**
- Bounded 3D space for objects
- Users can view from any angle
- Runs in Shared Space
- Ideal for 3D visualization, games

**Spaces (Fully immersive):**
- **Shared Space**: Multitasking, multiple apps visible
- **Full Space**: Single-app immersion, VR mode
- Full control over user's view

**PolySpatial workflow:**
- Enables porting Unity projects to visionOS
- Converts Unity scenes to RealityKit representation
- Supports Shared Space and Volume modes
- Allows cross-platform development (visionOS ↔ Android XR)

**Input handling:**
- Gaze + pinch primary interaction
- Hand tracking via XR Hands package
- Game controller support
- Voice commands (via native integration)

**Limitations:**
- Initial versions lacked keyboard text entry (now improved)
- Unity video player support with PolySpatial limited
- "Progressive" immersion style not fully supported
- Shared Space UX requires native SwiftUI for optimal experience

#### Meta Quest (Quest 2, Quest 3, Quest Pro)

**Required packages:**
- `com.unity.xr.oculus`: Meta XR plugin (legacy)
- `com.unity.xr.meta-openxr`: Meta OpenXR plugin (recommended)
- Meta XR SDK (optional, for advanced features)

**Development requirements:**
- Unity 2021.3 LTS or later
- Android Build Support module
- Meta Quest Developer Hub (for device management)
- Oculus ADB Drivers

**Key features:**
- Hand tracking and controller support
- Passthrough API for mixed reality
- Spatial anchors and scene understanding
- Guardian boundary system
- Oculus Link for PC VR development

**Optimization:**
- Target 72fps (Quest 2) or 90fps (Quest 3) minimum
- Use fixed foveated rendering
- Implement dynamic resolution scaling
- Optimize for mobile GPU (Adreno)

#### Android XR

**Overview:**
- Google's unified XR platform (2026)
- Supports Samsung Galaxy XR, other Android XR devices
- AI-native platform (Gemini integration)

**Development:**
- Unity PolySpatial supports Android XR
- OpenXR backend for standardization
- Hand input as primary interaction
- WebXR support in Chrome

**Key features:**
- Multimodal AI (Gemini for contextual understanding)
- Hand and eye tracking
- Stereo depth sensing
- Spatial anchors and plane detection

### Unity XR Development Workflow

**1. Project setup:**
```
1. Create new Unity project (3D Core or URP template)
2. Install XR Plugin Management (Edit > Project Settings > XR Plugin Management)
3. Enable target platform(s) (Oculus, OpenXR, ARKit, ARCore)
4. Install XR Interaction Toolkit (Window > Package Manager)
5. Import XR Interaction Toolkit samples (optional)
```

**2. Scene configuration:**
```
1. Delete Main Camera (replaced by XR Origin)
2. Add XR Origin (XR > XR Origin (Action-based))
3. Configure XR Origin:
   - Camera Offset: Tracking origin mode (Floor, Device)
   - Input Action Manager: Reference to XR input actions
4. Add XR Interaction Manager (XR > XR Interaction Manager)
5. Add locomotion (Teleportation, Continuous Movement)
```

**3. Interaction setup:**
```
1. Add interactable objects (XR > XR Grab Interactable)
2. Configure interaction layers (Physics > Interaction Layer Mask)
3. Set up UI interaction (XR > UI Canvas with XR UI Input Module)
4. Implement custom interactions (extend XRBaseInteractable)
```

**4. Build and deploy:**
```
1. Configure build settings (File > Build Settings)
2. Set platform-specific settings (Player Settings)
3. Build and run on device or simulator
4. Profile performance (Unity Profiler, platform-specific tools)
```

### Unity XR Best Practices

**Performance:**
- Use Universal Render Pipeline (URP) for mobile XR
- Enable GPU instancing for repeated objects
- Implement object pooling for dynamic objects
- Use occlusion culling and LOD groups
- Profile regularly with Unity Profiler

**Cross-platform development:**
- Use OpenXR when possible for maximum compatibility
- Abstract platform-specific code behind interfaces
- Test on all target devices regularly
- Use conditional compilation for platform-specific features

**Asset management:**
- Use Addressables for on-demand asset loading
- Compress textures (ASTC for mobile, BC7 for PC)
- Optimize meshes (reduce polygon count, combine meshes)
- Use asset bundles for modular content

## Unreal Engine for XR Development

### Overview

Unreal Engine excels at high-fidelity graphics and complex simulations, making it ideal for PC-tethered VR, architectural visualization, and AAA XR experiences. Unreal's advanced rendering features (Nanite, Lumen, ray tracing) enable photorealistic immersive environments.

### Unreal XR Architecture

**Core systems:**

**XR System Interface:**
- Abstraction layer for XR hardware
- Supports OpenXR, SteamVR, Oculus, Windows Mixed Reality
- Handles tracking, rendering, input

**Motion Controller Component:**
- Represents physical controllers in scene
- Provides position, rotation, button states
- Supports haptic feedback

**Head Mounted Display (HMD) Blueprint Library:**
- Blueprint-accessible XR functions
- Get HMD position/rotation
- Enable/disable XR mode
- Configure rendering settings

**XR Input:**
- Enhanced Input System integration
- Action-based input mapping
- Supports controllers, hand tracking, gaze

### Platform-Specific Unreal Support

#### PC VR (SteamVR, Oculus Link, Windows Mixed Reality)

**Supported devices:**
- Valve Index, HTC Vive, HP Reverb G2
- Meta Quest (via Oculus Link or Air Link)
- Windows Mixed Reality headsets

**Development requirements:**
- Unreal Engine 4.27+ or UE5
- High-end PC (RTX 3070+ recommended)
- SteamVR or Oculus PC software

**Key features:**
- High-fidelity graphics (ray tracing, Lumen, Nanite)
- Advanced physics simulation
- Blueprint visual scripting
- C++ for performance-critical code

**Optimization:**
- Target 90fps minimum (120fps for Index)
- Use Variable Rate Shading (VRS)
- Implement dynamic resolution scaling
- Optimize for high-end GPU (NVIDIA RTX, AMD Radeon)

#### Meta Quest (Standalone)

**Development requirements:**
- Unreal Engine 4.27+ or UE5
- Android Build Support
- Meta Quest Developer Hub

**Key features:**
- Oculus Mobile SDK integration
- Hand tracking and controller support
- Passthrough API for mixed reality
- Optimized mobile rendering pipeline

**Optimization:**
- Target 72fps (Quest 2) or 90fps (Quest 3)
- Use mobile rendering features (mobile HDR, mobile multi-view)
- Reduce draw calls and polygon count
- Optimize for mobile GPU (Adreno)

**Nanite for VR:**
- Unreal Engine 5.3+ supports Nanite on standalone headsets
- Enables high-polygon models via streaming and foveated rendering
- Requires careful optimization for mobile hardware

#### Apple Vision Pro

**Current status (2026):**
- Unreal Engine support for Vision Pro is less streamlined than Unity
- Requires compilation, building, and device transfer for testing
- No direct VR editor mode launching (as of early 2026)

**Workflow:**
1. Develop in Unreal Editor on Mac
2. Compile for visionOS target
3. Build and package application
4. Transfer to Vision Pro for testing
5. Iterate (slower than Unity workflow)

**Recommendations:**
- Use Unity for Vision Pro development unless photorealistic graphics are essential
- Monitor Unreal Engine updates for improved Vision Pro workflow
- Consider native development (Xcode) for Vision Pro-exclusive apps

### Unreal XR Development Workflow

**1. Project setup:**
```
1. Create new Unreal project (VR template or blank)
2. Enable XR plugins (Edit > Plugins > Virtual Reality)
3. Configure project settings (Edit > Project Settings > XR)
4. Set up input mappings (Edit > Project Settings > Input)
```

**2. VR Pawn setup:**
```
1. Create VR Pawn Blueprint (inherits from Pawn)
2. Add Camera Component (represents HMD)
3. Add Motion Controller Components (left and right hands)
4. Implement locomotion (teleportation, smooth movement)
5. Set up interaction (grab, use, UI interaction)
```

**3. Interaction implementation:**
```
1. Create interactable actors (Blueprint or C++)
2. Implement grab/release logic (attach to motion controller)
3. Add physics interactions (physics handles, constraints)
4. Create VR UI (3D widgets, gaze-based interaction)
```

**4. Build and deploy:**
```
1. Configure platform settings (Project Settings > Platforms)
2. Package project (File > Package Project > [Platform])
3. Deploy to device (via USB or wireless)
4. Profile performance (Unreal Insights, GPU Visualizer)
```

### Unreal XR Best Practices

**Performance:**
- Use forward rendering for VR (better performance than deferred)
- Enable instanced stereo rendering
- Use dynamic resolution scaling
- Optimize materials (reduce shader complexity)
- Profile with GPU Visualizer and Unreal Insights

**Graphics quality:**
- Use physically-based materials (PBR)
- Implement dynamic lighting with Lumen (UE5)
- Use Nanite for high-polygon geometry (UE5, PC VR)
- Enable ray tracing for reflections and shadows (high-end PC VR)

**Blueprint vs. C++:**
- Use Blueprints for rapid prototyping and game logic
- Use C++ for performance-critical code (physics, AI, rendering)
- Combine both: C++ base classes with Blueprint subclasses

## Native Platform Development

### Apple Vision Pro (visionOS)

**Development stack:**
- **Xcode**: Apple's IDE for visionOS development
- **Swift**: Primary programming language
- **SwiftUI**: Declarative UI framework
- **RealityKit**: 3D rendering engine
- **ARKit**: Spatial awareness and tracking
- **Reality Composer Pro**: Scene design and prototyping tool

**Key frameworks:**

**RealityKit:**
- High-performance 3D rendering
- Physics simulation and animations
- Spatial audio integration
- Entity-component system architecture

**ARKit:**
- World tracking (6DOF)
- Plane detection (horizontal and vertical)
- Image tracking and object detection
- Scene reconstruction (spatial mesh)
- People occlusion and segmentation

**SwiftUI for spatial interfaces:**
- Declarative UI for 2D and 3D content
- Seamless integration with RealityKit
- Adaptive layouts for different immersion levels
- Native visionOS controls and interactions

**Development workflow:**

**1. Project setup:**
```swift
1. Create new visionOS project in Xcode
2. Choose template (Immersive Space, Window, or Volume)
3. Configure project settings (bundle ID, capabilities)
4. Set up Reality Composer Pro for 3D content
```

**2. Scene creation:**
```swift
1. Design 3D scenes in Reality Composer Pro
2. Import 3D models (USDZ format)
3. Add animations, physics, and audio
4. Export scene for use in Xcode project
```

**3. Interaction implementation:**
```swift
1. Implement gaze + pinch interactions
2. Add hand gesture recognition (ARKit)
3. Integrate spatial audio (AVFoundation)
4. Handle immersion level transitions
```

**4. Testing and deployment:**
```swift
1. Test in visionOS Simulator (limited fidelity)
2. Deploy to Vision Pro via Xcode (USB or wireless)
3. Use Instruments for performance profiling
4. Submit to App Store via App Store Connect
```

**Advantages of native development:**
- Deep visionOS integration (system-level features)
- Optimal performance (no engine overhead)
- Access to latest Apple platform features first
- Native UI/UX patterns (familiar to Apple users)
- Smaller app size compared to Unity/Unreal

**Disadvantages:**
- Platform-locked (Vision Pro only)
- Steeper learning curve (Swift, RealityKit, ARKit)
- Longer development time for complex 3D content
- Limited cross-platform reusability

### Meta Quest (Native Android)

**Development stack:**
- **Android Studio**: IDE for Android development
- **Java/Kotlin**: Programming languages
- **Meta XR SDK**: Native Quest development SDK
- **OpenXR**: Cross-platform XR standard

**Meta XR SDK features:**
- Hand tracking and controller input
- Passthrough API for mixed reality
- Spatial anchors and scene understanding
- Social features (avatars, parties)
- Performance optimization tools

**Development workflow:**
```
1. Set up Android Studio with Meta XR SDK
2. Create Android project with XR activity
3. Implement rendering loop (OpenGL ES or Vulkan)
4. Add interaction handling (controllers, hands)
5. Build APK and deploy to Quest via ADB
```

**When to use native Quest development:**
- Maximum performance (no engine overhead)
- Deep integration with Meta platform features
- Custom rendering pipelines
- Existing Android development expertise

**Disadvantages:**
- More complex than Unity/Unreal (manual rendering setup)
- Longer development time
- Limited cross-platform reusability

## WebXR Development

### Overview

WebXR enables immersive VR and AR experiences directly in web browsers, eliminating the need for app installation. It provides a low-friction way to experience XR content across diverse devices.

### WebXR API

**Core functionality:**
- Query XR device capabilities
- Request immersive sessions (VR or AR)
- Access device pose and input
- Render to XR display
- Handle session lifecycle

**Session types:**
- **Immersive VR**: Full VR experience (headset)
- **Immersive AR**: AR experience with camera passthrough
- **Inline**: XR content in regular web page (magic window)

**Supported browsers:**
- Chrome (Android, Windows, Android XR)
- Edge (Windows)
- Opera (Android)
- Samsung Internet (Android)
- Oculus Browser (Meta Quest)
- Safari (visionOS - limited support, VR only as of early 2026)

### WebXR Development Frameworks

#### Three.js

**Overview**: Popular JavaScript 3D library with comprehensive WebXR support.

**Features:**
- Easy-to-use API for 3D graphics
- Built-in WebXR support (VRButton, ARButton)
- Extensive examples and documentation
- Large community and ecosystem

**Example workflow:**
```javascript
1. Set up Three.js scene, camera, renderer
2. Enable XR support: renderer.xr.enabled = true
3. Add VRButton or ARButton to page
4. Implement XR render loop
5. Handle controller input and interactions
```

**Best for**: General 3D web experiences, product visualization, games

#### A-Frame

**Overview**: Web framework for building VR experiences using HTML-like syntax.

**Features:**
- Declarative HTML-based development
- Entity-component-system architecture
- Built on Three.js
- Extensive component library
- Low learning curve

**Example:**
```html
<a-scene>
  <a-box position="0 1.5 -3" color="red"></a-box>
  <a-sky color="#ECECEC"></a-sky>
</a-scene>
```

**Best for**: Rapid prototyping, educational projects, simple VR experiences

#### Babylon.js

**Overview**: Powerful 3D engine with advanced features and WebXR support.

**Features:**
- Advanced rendering (PBR, post-processing)
- Physics engine integration
- Comprehensive WebXR support
- Visual editor (Babylon.js Editor)
- TypeScript support

**Best for**: Complex 3D applications, games, enterprise visualization

#### PlayCanvas

**Overview**: Cloud-based game engine with WebXR support.

**Features:**
- Visual editor (browser-based)
- Collaborative development
- Optimized for performance
- Asset pipeline and hosting

**Best for**: Web-based games, collaborative projects, hosted experiences

### WebXR Development Workflow

**1. Project setup:**
```javascript
1. Set up web development environment (Node.js, npm)
2. Choose framework (Three.js, A-Frame, Babylon.js)
3. Install dependencies (npm install three, etc.)
4. Set up local development server (HTTPS required for WebXR)
```

**2. Scene creation:**
```javascript
1. Create 3D scene with camera and lighting
2. Import or create 3D models
3. Add materials and textures
4. Implement animations
```

**3. WebXR integration:**
```javascript
1. Enable XR support in renderer
2. Add VR/AR button to enter immersive mode
3. Implement XR render loop
4. Handle controller input (XRInputSource)
5. Implement interactions (raycasting, grabbing)
```

**4. Testing and deployment:**
```javascript
1. Test in desktop browser (limited XR simulation)
2. Test on physical XR devices (Quest, Vision Pro, AR-capable phones)
3. Optimize performance (reduce draw calls, compress assets)
4. Deploy to web hosting (CDN recommended)
5. Configure CORS and HTTPS
```

### WebXR Best Practices

**Performance optimization:**
- Minimize draw calls (batch geometry, use instancing)
- Compress textures (use WebP, basis universal)
- Implement LOD (level of detail)
- Use frustum culling and occlusion culling
- Target 60fps minimum (90fps for VR if possible)

**Device-first testing:**
- Desktop browser simulation is insufficient
- Test on physical XR devices regularly
- Use remote debugging (Chrome DevTools, Safari Web Inspector)
- Monitor performance (frame rate, memory usage)

**Accessibility:**
- Provide fallback for non-XR devices (inline mode)
- Support multiple input methods (controllers, hands, gaze)
- Include comfort options (teleportation, reduced motion)
- Ensure content is accessible (alt text, audio descriptions)

**Deployment:**
- Use HTTPS (required for WebXR API access)
- Configure CORS for cross-origin assets
- Use CDN for asset delivery (reduce latency)
- Implement progressive loading (load low-res first, stream high-res)

### WebXR Limitations

**Performance:**
- Lower performance than native apps (JavaScript overhead)
- Limited access to hardware features (foveated rendering, etc.)
- Browser compatibility variations

**Hardware access:**
- Limited sensor access compared to native
- No direct access to some platform-specific features
- Dependent on browser WebXR implementation

**Platform support:**
- Safari on visionOS: VR only (no AR mode as of early 2026)
- Inconsistent feature support across browsers
- Requires fallback strategies for unsupported devices

## Specialized Platforms

### Godot Engine

**Overview**: Open-source game engine with XR support.

**Features:**
- Lightweight architecture
- OpenXR support (Godot 4.0+)
- GDScript (Python-like) or C#
- Free and open-source (MIT license)

**Best for**: Indie games, lightweight industrial tools, open-source projects

### Meta Horizon Studio

**Overview**: AI-native development environment for Horizon OS (Meta Quest).

**Features:**
- AssetGen: AI-powered asset creation
- CodeGen: AI-assisted code generation
- Rapid content creation
- Optimized for Meta Quest devices

**Best for**: Rapid prototyping on Meta Quest, AI-assisted development

### Snap Lens Studio

**Overview**: Development platform for Snap Spectacles AR experiences.

**Features:**
- Visual scripting and JavaScript
- AR templates and components
- Snap AR ecosystem integration
- Mobile AR (Snapchat app) and Spectacles support

**Best for**: Social AR experiences, Snapchat integration, mobile AR

## Cross-Platform Development Strategy

### Shared Architecture Approach

**Layer 1: Core logic (platform-agnostic)**
- Business logic, game mechanics, data models
- No platform-specific code
- Implement in C# (Unity) or C++ (Unreal)

**Layer 2: Platform abstraction**
- Input handling (abstract gaze, gestures, controllers)
- Rendering pipeline (abstract platform-specific features)
- Spatial tracking (abstract anchors, planes, markers)
- Use interfaces or abstract classes

**Layer 3: Platform-specific implementation**
- Vision Pro: Eye tracking, hand gestures, spatial audio
- Quest: Controller input, hand tracking, passthrough
- WebXR: Browser APIs, limited hardware access
- Implement platform-specific features as needed

### OpenXR for Standardization

**Benefits:**
- Single API for multiple XR platforms
- Reduces platform-specific code by 60-80%
- Future-proof (new devices support OpenXR)
- Industry-backed standard

**Supported platforms:**
- Meta Quest, HoloLens 2, SteamVR, Varjo, Magic Leap 2, PICO

**Implementation:**
- Use OpenXR plugin in Unity or Unreal
- Leverage spatial entities extensions for anchors, planes, markers
- Implement platform-specific features as OpenXR extensions

### Development Workflow

**1. Develop on primary target platform:**
- Choose platform with largest user base or most critical features
- Implement core functionality
- Test regularly on physical device

**2. Abstract platform-specific code:**
- Identify platform-specific features (input, rendering, tracking)
- Create abstraction layer (interfaces, abstract classes)
- Implement platform-specific versions

**3. Port to secondary platforms:**
- Test on secondary platforms weekly
- Implement platform-specific optimizations
- Maintain feature parity or graceful degradation

**4. Continuous integration:**
- Automate builds for all platforms
- Run automated tests on each platform
- Monitor performance metrics across devices

## Development Tools and SDKs

### Platform SDKs

**Meta XR SDK:**
- Hand tracking, controller input
- Passthrough API, spatial anchors
- Social features (avatars, parties)
- Performance tools (OVR Metrics Tool)

**Apple ARKit:**
- World tracking, plane detection
- Image and object tracking
- Scene reconstruction, people occlusion
- RealityKit integration

**Google ARCore:**
- Motion tracking, environmental understanding
- Light estimation, depth API
- Cloud Anchors for multi-user experiences
- Geospatial API for outdoor AR

**Microsoft Mixed Reality Toolkit (MRTK):**
- Cross-platform XR toolkit for Unity
- UI components, interaction patterns
- Spatial awareness, input handling
- Supports HoloLens, Quest, Windows Mixed Reality

### Debugging and Profiling Tools

**Unity Profiler:**
- CPU, GPU, memory profiling
- Frame debugger for rendering analysis
- Remote profiling on device

**Unreal Insights:**
- Comprehensive performance profiling
- CPU, GPU, memory, networking
- Visual scripting debugger

**Xcode Instruments:**
- Performance profiling for visionOS
- Time Profiler, Allocations, Leaks
- Metal System Trace for GPU analysis

**Meta Quest Developer Hub:**
- Device management and deployment
- Performance metrics (OVR Metrics Tool)
- Screen recording and casting
- Logcat for debugging

**Chrome DevTools:**
- WebXR debugging in browser
- Performance profiling, network analysis
- Remote debugging on mobile devices

### Asset Creation Tools

**3D modeling:**
- Blender (free, open-source)
- Maya, 3ds Max (industry standard)
- Cinema 4D (motion graphics)

**Texturing:**
- Substance Painter (PBR texturing)
- Photoshop (texture editing)
- Quixel Mixer (free, PBR materials)

**Audio:**
- Audacity (free audio editing)
- Reaper, Pro Tools (DAWs)
- Wwise, FMOD (interactive audio middleware)

**Version control:**
- Git (with Git LFS for large files)
- Perforce (industry standard for game development)
- Plastic SCM (Unity-integrated version control)

---

**Key Takeaways:**
- Unity is the most versatile choice for cross-platform XR development (70% market share)
- Unreal Engine excels at high-fidelity graphics for PC VR and architectural visualization
- Native development (Xcode for Vision Pro) provides optimal performance and deep platform integration
- WebXR enables accessible, browser-based XR experiences without app installation
- OpenXR standardization reduces platform-specific code and future-proofs applications
- Choose platform based on project requirements: graphics fidelity, target devices, team expertise, and development timeline
