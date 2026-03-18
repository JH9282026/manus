# Optimization and Performance for Mobile Games

Comprehensive guide to profiling, optimizing, and maintaining high performance for mobile games across diverse hardware.

---

## Performance Targets and Constraints

### Frame Rate Targets

**60 FPS (16.67ms per frame):**
- **Target**: Mid-range and flagship devices
- **Genres**: Action, racing, competitive multiplayer, rhythm games
- **Why**: Smooth gameplay, responsive controls, competitive advantage
- **Challenge**: Requires aggressive optimization, not achievable on all devices

**30 FPS (33.33ms per frame):**
- **Target**: Budget devices, complex 3D games
- **Genres**: RPG, strategy, puzzle, casual
- **Why**: Acceptable for slower-paced games, easier to maintain
- **Challenge**: Can feel sluggish for action games

**Variable Frame Rate:**
- **Target**: Adaptive quality settings
- **Implementation**: Detect device capabilities, adjust quality dynamically
- **Why**: Maximizes performance across all devices
- **Challenge**: Requires robust quality scaling system

### Battery Consumption Targets

**<15% per hour:**
- **Target**: All games
- **Why**: Players abandon games that drain battery quickly
- **Measurement**: Test on real devices over 30-60 minute sessions

**<20% per hour:**
- **Acceptable**: High-fidelity 3D games on flagship devices
- **Why**: Players tolerate higher drain for premium experiences
- **Warning**: Above 20% leads to high churn

### Thermal Management

**Device Temperature:**
- **Safe**: <40°C (comfortable to hold)
- **Warning**: 40-45°C (warm, throttling begins)
- **Critical**: >45°C (hot, aggressive throttling, player discomfort)

**Throttling:**
- Mobile devices reduce CPU/GPU performance when overheating
- Can reduce performance by 30-50% after 10-15 minutes
- Must design for sustained performance, not peak performance

### Memory Constraints

**iOS:**
- **Budget (iPhone SE)**: 3-4GB RAM, target <800MB usage
- **Mid-range (iPhone 13-14)**: 4-6GB RAM, target <1.2GB usage
- **Flagship (iPhone 15 Pro)**: 8GB RAM, target <1.5GB usage
- **Warning**: iOS aggressively terminates apps using >1.5GB

**Android:**
- **Budget**: 2-4GB RAM (OS uses 1-2GB), target <500MB usage
- **Mid-range**: 4-8GB RAM, target <1GB usage
- **Flagship**: 8-16GB RAM, target <2GB usage
- **Warning**: Budget devices have very limited memory

### Download Size Targets

**Initial Download:**
- **Target**: <150MB (installs without Wi-Fi warning)
- **Acceptable**: 150-500MB (Wi-Fi warning on cellular)
- **Large**: >500MB (significant install friction)

**Total Size (with assets):**
- **Casual**: <500MB
- **Mid-core**: 500MB-2GB
- **Hardcore**: 2-5GB
- **Warning**: Players uninstall large games when storage is low

---

## Profiling and Diagnostics

### Unity Profiler

**CPU Profiler:**
- Shows time spent in each function per frame
- Identify bottlenecks (rendering, physics, scripts, GC)
- Target: <16ms total for 60 FPS, <33ms for 30 FPS

**GPU Profiler:**
- Shows rendering time (draw calls, shaders, post-processing)
- Identify overdraw, expensive shaders, excessive draw calls
- Target: <10ms for 60 FPS, <20ms for 30 FPS

**Memory Profiler:**
- Shows memory allocation (textures, meshes, audio, scripts)
- Identify memory leaks, excessive allocations
- Target: <1GB total (iOS), <500MB (Android budget)

**Rendering Profiler:**
- Shows draw calls, batches, triangles, vertices
- Identify rendering bottlenecks
- Target: <100 draw calls, <100k triangles per frame

**How to Profile:**
1. Build development build with "Autoconnect Profiler" enabled
2. Run on real device (not editor or simulator)
3. Play through typical gameplay scenarios
4. Identify frames with spikes or consistent high usage
5. Drill down into specific functions or systems
6. Optimize and re-profile

### Xcode Instruments (iOS)

**Time Profiler:**
- Shows CPU usage per thread and function
- Identify hot paths and bottlenecks
- Use "Call Tree" view to see function hierarchy

**Allocations:**
- Shows memory allocations over time
- Identify memory leaks and excessive allocations
- Use "Generations" to track object lifecycles

**GPU Frame Capture:**
- Captures single frame for detailed analysis
- Shows draw calls, shaders, textures, render targets
- Identify overdraw and expensive shaders

**Energy Log:**
- Shows battery usage over time
- Identify energy-intensive operations (CPU, GPU, network, location)
- Target: <15% battery per hour

**How to Profile:**
1. Build Xcode project from Unity/Unreal
2. Run on real device connected via USB
3. Open Instruments, select profiling template
4. Record during gameplay
5. Analyze results, identify bottlenecks
6. Optimize and re-profile

### Android Profiler (Android Studio)

**CPU Profiler:**
- Shows CPU usage per thread and method
- Identify bottlenecks and hot paths
- Use "Flame Chart" for visual hierarchy

**Memory Profiler:**
- Shows memory usage over time (Java heap, native heap, graphics)
- Identify memory leaks and excessive allocations
- Use "Heap Dump" to analyze object retention

**GPU Profiler:**
- Shows rendering time per frame
- Requires device with GPU profiling support
- Identify rendering bottlenecks

**Energy Profiler:**
- Shows battery usage over time (CPU, network, location)
- Identify energy-intensive operations
- Target: <15% battery per hour

**How to Profile:**
1. Build Android project from Unity/Unreal
2. Run on real device connected via USB
3. Open Android Studio, attach profiler
4. Record during gameplay
5. Analyze results, identify bottlenecks
6. Optimize and re-profile

---

## Rendering Optimization

### Draw Call Reduction

**What are Draw Calls?**
Instructions from CPU to GPU to render objects. Each draw call has overhead, so minimizing them improves performance.

**Target:**
- **Budget devices**: <50 draw calls per frame
- **Mid-range devices**: <100 draw calls per frame
- **Flagship devices**: <200 draw calls per frame

**Techniques:**

**1. Static Batching (Unity)**
- Combines static objects with same material into single draw call
- Enable in Player Settings → "Static Batching"
- Mark objects as "Static" in Inspector
- Limitation: Increases memory usage, objects can't move

**2. Dynamic Batching (Unity)**
- Combines small dynamic objects with same material
- Enable in Player Settings → "Dynamic Batching"
- Limitation: Only works for <300 vertices per object

**3. GPU Instancing (Unity/Unreal)**
- Renders multiple copies of same mesh in single draw call
- Enable "GPU Instancing" on materials
- Best for: Repeated objects (trees, rocks, enemies)

**4. Texture Atlases**
- Combine multiple textures into single large texture
- Reduces texture swaps (expensive GPU operation)
- Unity: Use Sprite Atlas for 2D, manual atlases for 3D
- Unreal: Use Texture Atlases or Material Atlases

**5. Mesh Combining**
- Manually combine multiple meshes into single mesh
- Reduces draw calls but increases memory
- Best for: Static environment objects

**6. Occlusion Culling**
- Don't render objects hidden behind other objects
- Unity: Bake occlusion data (Window → Rendering → Occlusion Culling)
- Unreal: Enable "Precomputed Visibility" or "Software Occlusion"
- Best for: 3D games with complex environments

### Overdraw Reduction

**What is Overdraw?**
Rendering the same pixel multiple times per frame (e.g., overlapping transparent objects). Wastes GPU fill rate.

**How to Measure:**
- Unity: Scene view → Overdraw shading mode
- Xcode: GPU Frame Capture → Fragment Overdraw
- Target: <2x overdraw average, <5x overdraw max

**Techniques:**

**1. Reduce Transparent Objects**
- Transparent objects can't be culled, always rendered
- Use opaque materials when possible
- Minimize overlapping UI elements

**2. Sort Transparent Objects**
- Render transparent objects back-to-front
- Unity: Automatic for transparent shaders
- Reduces overdraw from overlapping transparency

**3. Use Alpha Testing Instead of Alpha Blending**
- Alpha testing (cutout) is cheaper than alpha blending
- Best for: Foliage, fences, decals
- Limitation: Hard edges, no smooth transparency

**4. Optimize UI**
- UI is often major source of overdraw
- Minimize overlapping UI elements
- Use opaque backgrounds instead of transparent
- Disable invisible UI elements (don't just set alpha to 0)

### Shader Optimization

**Mobile Shader Complexity:**
- Mobile GPUs are less powerful than desktop
- Avoid expensive operations: sin/cos, pow, normalize, complex lighting
- Use simplified shaders for mobile

**Unity:**
- Use "Mobile" shaders (Mobile/Diffuse, Mobile/Unlit)
- Use Universal Render Pipeline (URP) for optimized mobile shaders
- Avoid Standard shader (too expensive for mobile)

**Unreal:**
- Use "Mobile" material quality level
- Disable expensive features (reflections, subsurface scattering)
- Use simple lighting models (Unlit, Default Lit)

**Shader Variants:**
- Shaders with many keywords generate many variants
- Each variant increases build size and memory
- Strip unused variants (Unity: Graphics Settings → Shader Stripping)

### Level of Detail (LOD)

**What is LOD?**
Using simpler models for distant objects to reduce rendering cost.

**LOD Levels:**
- **LOD0**: Full detail (close to camera)
- **LOD1**: 50% triangles (medium distance)
- **LOD2**: 25% triangles (far distance)
- **LOD3**: 10% triangles (very far distance)
- **Culled**: Not rendered (beyond max distance)

**Unity:**
- Use LOD Group component
- Assign meshes for each LOD level
- Configure transition distances

**Unreal:**
- LODs generated automatically on import
- Configure LOD settings in Static Mesh Editor
- Adjust LOD distances in World Settings

**Best Practices:**
- Use aggressive LOD for mobile (more levels, shorter distances)
- Test LOD transitions (avoid popping)
- Use LOD for characters, vehicles, environment objects

### Texture Optimization

**Texture Compression:**
- **iOS**: ASTC (Adaptive Scalable Texture Compression)
- **Android**: ETC2 (Ericsson Texture Compression 2)
- **Fallback**: PVRTC (iOS), ETC1 (Android)
- Compression reduces memory and bandwidth by 4-8x

**Texture Resolution:**
- Use smallest resolution that looks acceptable
- **UI**: 512x512 or 1024x1024 max
- **Characters**: 1024x1024 or 2048x2048
- **Environment**: 512x512 or 1024x1024
- **Effects**: 256x256 or 512x512

**Mipmaps:**
- Pre-generated lower-resolution versions of textures
- GPU selects appropriate mipmap based on distance
- Reduces aliasing and improves performance
- Enable for all textures except UI

**Texture Atlases:**
- Combine multiple textures into single large texture
- Reduces texture swaps and draw calls
- Unity: Sprite Atlas (2D), manual atlases (3D)
- Unreal: Texture Atlases or Material Atlases

---

## Scripting Optimization

### Garbage Collection (GC)

**What is Garbage Collection?**
Automatic memory management that reclaims unused objects. GC pauses can cause frame drops.

**GC Triggers:**
- Heap memory full (allocations exceed threshold)
- Manual call to `GC.Collect()` (avoid in gameplay)
- Scene load or unload

**GC Impact:**
- GC pause: 5-50ms (can cause frame drops)
- More allocations = more frequent GC = more frame drops

**Techniques to Reduce GC:**

**1. Object Pooling**
- Reuse objects instead of Instantiate/Destroy
- Pre-allocate pool of objects at start
- Return objects to pool instead of destroying
- Best for: Bullets, enemies, particles, UI elements

**2. Avoid Allocations in Update/FixedUpdate**
- Don't create new objects every frame
- Cache references instead of GetComponent every frame
- Use for-loops instead of foreach (foreach allocates)
- Avoid LINQ (allocates enumerators)

**3. Use Structs Instead of Classes**
- Structs are value types (stack-allocated, no GC)
- Classes are reference types (heap-allocated, GC)
- Best for: Small data structures (Vector3, Color, etc.)
- Limitation: Structs are copied, not referenced

**4. String Concatenation**
- Strings are immutable (each concatenation allocates new string)
- Use StringBuilder for frequent concatenation
- Cache strings instead of regenerating

**5. Coroutines**
- Coroutines allocate enumerators (GC)
- Use sparingly, avoid starting many coroutines per frame
- Alternative: Custom update managers

### CPU Optimization

**1. Cache Component References**
```csharp
// Bad: GetComponent every frame (slow)
void Update() {
    GetComponent<Rigidbody>().velocity = Vector3.zero;
}

// Good: Cache reference once
private Rigidbody rb;
void Start() {
    rb = GetComponent<Rigidbody>();
}
void Update() {
    rb.velocity = Vector3.zero;
}
```

**2. Use FixedUpdate for Physics**
- Update: Called every frame (variable rate)
- FixedUpdate: Called at fixed intervals (physics timestep)
- Use FixedUpdate for physics operations (AddForce, velocity)
- Use Update for input and rendering

**3. Avoid Find and SendMessage**
- GameObject.Find: Searches entire scene (very slow)
- SendMessage: Searches all components (slow)
- Alternative: Cache references, use direct calls

**4. Use Object Pooling**
- Instantiate and Destroy are expensive
- Pre-allocate objects, reuse from pool
- Reduces CPU spikes and GC

**5. Optimize Loops**
- Cache array length outside loop
- Use for-loops instead of foreach (foreach allocates)
- Avoid nested loops when possible

**6. Use Coroutines for Time-Based Logic**
- Instead of checking timer every frame in Update
- Use coroutine with WaitForSeconds
- Reduces Update overhead

---

## Physics Optimization

### Physics Settings

**Fixed Timestep:**
- Default: 0.02 (50 physics updates per second)
- Lower = more accurate, higher CPU cost
- Higher = less accurate, lower CPU cost
- Mobile recommendation: 0.02-0.03 (30-50 updates/sec)

**Solver Iterations:**
- Default: 6 velocity iterations, 2 position iterations
- Lower = less accurate, better performance
- Mobile recommendation: 4 velocity, 1 position

**Collision Detection:**
- **Discrete**: Fastest, can miss fast-moving objects
- **Continuous**: Slower, prevents tunneling
- **Continuous Dynamic**: Slowest, most accurate
- Mobile recommendation: Discrete for most objects, Continuous for fast projectiles

### Physics Optimization Techniques

**1. Reduce Rigidbody Count**
- Each Rigidbody has CPU cost
- Use static colliders for non-moving objects
- Combine multiple colliders into single Rigidbody when possible

**2. Simplify Colliders**
- **Primitive colliders** (box, sphere, capsule): Fast
- **Mesh colliders**: Slow, avoid when possible
- Use primitive colliders for gameplay, mesh colliders for static environment

**3. Use Layers and Collision Matrix**
- Disable unnecessary collision checks (Edit → Project Settings → Physics)
- Example: Bullets don't collide with other bullets
- Reduces collision detection overhead

**4. Sleep Rigidbodies**
- Rigidbodies automatically sleep when stationary
- Sleeping Rigidbodies don't update (saves CPU)
- Avoid waking sleeping Rigidbodies unnecessarily

**5. Use Raycasts Instead of Triggers**
- Raycasts are cheaper than continuous trigger checks
- Best for: Line-of-sight checks, ground detection

**6. Spatial Partitioning**
- Physics engine uses spatial partitioning (octree, grid)
- Keep objects spread out when possible
- Avoid hundreds of objects in small area

---

## Memory Optimization

### Texture Memory

**Texture Compression:**
- ASTC (iOS): 4-8x compression, excellent quality
- ETC2 (Android): 4-6x compression, good quality
- Always enable compression for mobile

**Texture Resolution:**
- Use smallest resolution that looks acceptable
- Halving resolution = 4x memory savings
- Example: 2048x2048 = 16MB, 1024x1024 = 4MB

**Texture Formats:**
- **RGBA**: 4 bytes per pixel (full color + alpha)
- **RGB**: 3 bytes per pixel (no alpha)
- **Alpha8**: 1 byte per pixel (alpha only)
- Use RGB when alpha not needed (25% memory savings)

**Mipmaps:**
- Mipmaps increase memory by 33%
- Disable for UI textures (always viewed at full resolution)
- Enable for 3D textures (improves quality and performance)

### Audio Memory

**Audio Compression:**
- **Music**: Vorbis (streaming), 128-192 kbps
- **Long SFX**: Vorbis (compressed in memory), 96-128 kbps
- **Short SFX**: ADPCM (decompressed in memory), 4:1 compression
- Never use uncompressed audio on mobile

**Audio Loading:**
- **Decompress on Load**: Loads fast, uses more memory
- **Compressed in Memory**: Loads slow, uses less memory, CPU overhead
- **Streaming**: No memory, CPU overhead, best for music
- Mobile recommendation: Stream music, decompress short SFX, compress long SFX

### Mesh Memory

**Mesh Optimization:**
- Reduce polygon count (use LODs)
- Remove unnecessary vertices and triangles
- Use mesh compression (Unity: Mesh Compression in Import Settings)

**Mesh Compression:**
- Reduces memory by 50-75%
- Slight quality loss (usually imperceptible)
- Enable for all meshes on mobile

### Asset Streaming

**Addressables (Unity):**
- Load assets on-demand instead of including in build
- Reduces initial download size
- Streams assets from CDN or local storage
- Best for: Large games with lots of content

**Asset Bundles (Unity, legacy):**
- Similar to Addressables, older system
- More manual management
- Being replaced by Addressables

**Pak Files (Unreal):**
- Unreal's asset packaging system
- Supports streaming and on-demand loading
- Configure in Project Settings → Packaging

---

## Battery Optimization

### CPU Optimization

**Reduce CPU Usage:**
- Lower frame rate for menus (30 FPS)
- Use fixed timestep for game loop (avoid variable delta time)
- Disable unnecessary updates (pause background systems)
- Use coroutines and timers instead of Update loops

**Sleep/Idle Optimization:**
- Reduce update frequency when app in background
- Pause game logic, keep only essential systems running
- Unity: OnApplicationPause callback

### GPU Optimization

**Reduce GPU Usage:**
- Lower rendering resolution (render at 0.75x or 0.5x, upscale to screen)
- Disable expensive post-processing (bloom, depth of field, motion blur)
- Reduce draw calls and overdraw
- Use simpler shaders

**Dynamic Quality Scaling:**
- Detect battery level and thermal state
- Reduce quality settings when battery low or device hot
- Unity: SystemInfo.batteryLevel, Unreal: Device Profiles

### Sensor Optimization

**Disable Unnecessary Sensors:**
- GPS: High battery drain, disable when not needed
- Gyroscope/Accelerometer: Moderate drain, disable when not needed
- Camera: High drain, disable when not needed
- Unity: Input.gyro.enabled, Input.location.Stop()

### Network Optimization

**Reduce Network Usage:**
- Batch network requests (send multiple updates in single request)
- Use compression for data transfer
- Cache data locally (avoid redundant downloads)
- Use Wi-Fi when possible (cellular uses more battery)

---

## Platform-Specific Optimization

### iOS Optimization

**Metal API:**
- Use Metal for best performance (mandatory on modern iOS)
- Avoid OpenGL ES (deprecated, slower)

**IL2CPP:**
- Use IL2CPP scripting backend (faster than Mono)
- Longer build times, better runtime performance

**Bitcode:**
- Enable bitcode for App Store optimization
- Apple can recompile for future hardware

**App Thinning:**
- App Store delivers device-specific builds
- Reduces download size (only includes assets for user's device)
- Automatic, no configuration needed

### Android Optimization

**Vulkan API:**
- Use Vulkan for flagship devices (40-60% performance gain)
- Fallback to OpenGL ES 3.0 for older devices
- Unity: Enable both in Player Settings, auto-select at runtime

**IL2CPP:**
- Use IL2CPP scripting backend (faster than Mono)
- Longer build times, better runtime performance

**App Bundle:**
- Use Android App Bundle (AAB) instead of APK
- Google Play delivers device-specific APKs
- Reduces download size by 20-50%

**ARM64:**
- Target ARM64 (64-bit) for modern devices
- Required by Google Play since August 2019
- Better performance than ARMv7 (32-bit)

---

## Testing and Validation

### Device Testing Matrix

**iOS:**
- **Budget**: iPhone SE (2022)
- **Mid-range**: iPhone 13
- **Flagship**: iPhone 15 Pro
- **Tablet**: iPad (9th gen), iPad Pro

**Android:**
- **Budget**: Samsung Galaxy A14, Xiaomi Redmi 10
- **Mid-range**: Samsung Galaxy A54, Google Pixel 7
- **Flagship**: Samsung Galaxy S24, Google Pixel 8 Pro
- **Tablet**: Samsung Galaxy Tab A8

### Performance Testing Checklist

- [ ] Test on real devices (not simulator/emulator)
- [ ] Profile on target devices (budget, mid-range, flagship)
- [ ] Test 30-60 minute sessions (thermal throttling)
- [ ] Measure battery drain (<15% per hour)
- [ ] Check frame rate (60 FPS target, 30 FPS minimum)
- [ ] Monitor memory usage (<1GB iOS, <500MB Android budget)
- [ ] Test on low battery (some devices throttle at <20%)
- [ ] Test on different network conditions (Wi-Fi, 4G, 5G, offline)
- [ ] Test app backgrounding and resuming
- [ ] Test interruptions (phone calls, notifications)

### Automated Testing

**Unity Test Framework:**
- Write unit tests for game logic
- Run tests in CI/CD pipeline
- Catch regressions early

**Firebase Test Lab:**
- Automated testing on real devices (Android)
- Run tests on 20+ device models
- Generates performance reports

**Xcode UI Testing:**
- Automated UI testing for iOS
- Record interactions, replay on devices
- Integrates with CI/CD

---

## Conclusion

Mobile game optimization is an ongoing process that requires profiling, testing, and iteration. Target 60 FPS on mid-range devices, <15% battery drain per hour, and <1GB memory usage. Use aggressive rendering optimization (draw call reduction, LODs, texture compression), scripting optimization (object pooling, GC reduction), and physics optimization (simplified colliders, collision layers). Test on real devices across the performance spectrum, and implement dynamic quality scaling to ensure smooth gameplay for all players.