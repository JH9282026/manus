# VR Performance Optimization

Comprehensive guide to profiling, optimizing, and maintaining high performance for VR games to ensure smooth, comfortable experiences.

---

## VR Performance Requirements

### Frame Rate Targets

VR requires significantly higher frame rates than traditional games to prevent motion sickness and maintain immersion.

**Minimum Frame Rates by Platform:**
- **Meta Quest 2**: 72Hz minimum, 90Hz standard, 120Hz for simple games
- **Meta Quest 3**: 90Hz standard, 120Hz for optimized games
- **PSVR2**: 90Hz minimum, 120Hz for competitive games
- **PC VR (Valve Index)**: 90Hz minimum, 120Hz standard, 144Hz for high-end
- **Apple Vision Pro**: 90Hz minimum, 96Hz/100Hz for optimized experiences

**Frame Time Budgets:**
- **72Hz**: 13.89ms per frame
- **90Hz**: 11.11ms per frame
- **120Hz**: 8.33ms per frame
- **144Hz**: 6.94ms per frame

**Critical**: Dropping below target frame rate causes judder, which leads to motion sickness. Consistent frame rate is more important than high average frame rate.

### Rendering Workload

VR effectively doubles the rendering workload compared to traditional games:

**Stereo Rendering:**
- Two viewpoints (one per eye) must be rendered each frame
- Each eye has slightly different perspective (interpupillary distance ~63mm)
- Naive approach: Render scene twice (2x workload)
- Optimized approach: Stereo instancing (render both eyes in single pass, ~1.3x workload)

**Resolution Targets:**
- **Quest 2**: 1832×1920 per eye (3.5M pixels per eye, 7M total)
- **Quest 3**: 2064×2208 per eye (4.6M pixels per eye, 9.2M total)
- **PSVR2**: 2000×2040 per eye (4.1M pixels per eye, 8.2M total)
- **Valve Index**: 1440×1600 per eye (2.3M pixels per eye, 4.6M total)
- **Vision Pro**: 3680×3140 per eye (11.6M pixels per eye, 23.2M total)

**Comparison**: Traditional 1080p game = 2M pixels, VR = 4.6M to 23.2M pixels (2-11x more pixels)

---

## Profiling VR Performance

### Unity XR Profiler

**Setup:**
1. Build development build with "Autoconnect Profiler" enabled
2. Run on target device (Quest, PSVR2, PC VR)
3. Open Unity Profiler (Window → Analysis → Profiler)
4. Connect to device

**Key Metrics:**
- **CPU Time**: Time spent on CPU per frame (target <11ms for 90Hz)
- **GPU Time**: Time spent on GPU per frame (target <11ms for 90Hz)
- **Draw Calls**: Number of draw calls per frame (target <100)
- **Triangles**: Number of triangles rendered per frame (target <200k)
- **SetPass Calls**: Number of material/shader changes (target <50)

**Identifying Bottlenecks:**
- **CPU-bound**: CPU time >11ms, GPU time <11ms → Optimize scripts, physics, draw calls
- **GPU-bound**: GPU time >11ms, CPU time <11ms → Optimize shaders, reduce overdraw, lower resolution
- **Balanced**: Both CPU and GPU ~11ms → Optimize both

### Unreal VR Profiler

**Console Commands:**
- `stat fps`: Show frame rate and frame time
- `stat unit`: Show CPU, GPU, and frame time breakdown
- `stat gpu`: Show GPU time per rendering pass
- `stat scenerendering`: Show draw calls, triangles, and rendering stats

**Unreal Insights:**
- Advanced profiling tool (replaces old profiler)
- Detailed CPU and GPU traces
- Requires Unreal Engine 5.0+

**Identifying Bottlenecks:**
- **CPU-bound**: Frame time dominated by "Game Thread" or "Render Thread"
- **GPU-bound**: Frame time dominated by "GPU"
- **Draw Call Bound**: High "RHI Thread" time, many draw calls

### On-Device Profiling

**Meta Quest Developer Hub:**
- Real-time performance overlay (FPS, CPU, GPU, memory, thermal)
- Capture performance traces
- Analyze frame drops and stutters

**PSVR2 Profiler:**
- Use PS5 development kit profiler
- Detailed GPU and CPU traces
- Foveated rendering analysis

**SteamVR Frame Timing:**
- Built-in frame timing graph (SteamVR settings)
- Shows CPU and GPU time per frame
- Identifies dropped frames

---

## Rendering Optimization

### Stereo Instancing

**What is Stereo Instancing?**
Render both eyes in a single GPU pass using instanced rendering. GPU renders scene once, duplicates geometry for second eye.

**Performance Gain:**
- Reduces CPU overhead by 30-40%
- Reduces draw calls by ~50%
- Minimal GPU overhead (geometry duplicated, not re-rendered)

**How to Enable:**
- **Unity**: Player Settings → XR Settings → Stereo Rendering Mode → Single Pass Instanced
- **Unreal**: Project Settings → VR → Instanced Stereo Rendering → Enabled

**Limitations:**
- Requires shader support (most modern shaders support it)
- Some post-processing effects may not work
- Test thoroughly (can cause visual artifacts if shaders incompatible)

### Foveated Rendering

**What is Foveated Rendering?**
Render only the foveal area (center of vision) at full resolution, reduce resolution in periphery. Human eyes have high resolution only in center (fovea), periphery is blurry.

**Performance Gain:**
- 30-50% GPU performance improvement
- Allows higher fidelity in center or higher frame rate

**Requirements:**
- Eye tracking (PSVR2, Quest Pro, Vision Pro)
- Or fixed foveation (Quest 2, Quest 3 without eye tracking)

**Types:**

**Fixed Foveated Rendering (FFR):**
- Assumes player looks at center of screen
- Reduces resolution in periphery (fixed pattern)
- No eye tracking required
- Available on all Quest headsets

**Dynamic Foveated Rendering (DFR):**
- Tracks where player is looking (eye tracking)
- Renders high resolution only where player looks
- Requires eye tracking (PSVR2, Quest Pro, Vision Pro)
- Better performance than FFR

**How to Enable:**
- **Unity (Quest)**: Oculus XR Plugin → Foveated Rendering → Enabled
- **Unity (PSVR2)**: PSVR2 SDK → Foveated Rendering → Enabled
- **Unreal (Quest)**: Mobile HDR → Foveated Rendering → Enabled
- **Unreal (PSVR2)**: PSVR2 Plugin → Foveated Rendering → Enabled

### Draw Call Reduction

**Target**: <100 draw calls per frame (VR is more sensitive than flat games)

**Techniques:**

**1. Static Batching:**
- Combines static objects with same material into single draw call
- Unity: Mark objects as "Static", enable Static Batching in Player Settings
- Unreal: Automatic for static meshes
- Limitation: Increases memory usage, objects can't move

**2. GPU Instancing:**
- Renders multiple copies of same mesh in single draw call
- Unity: Enable "GPU Instancing" on materials
- Unreal: Enable "Instanced Static Mesh" component
- Best for: Repeated objects (trees, rocks, enemies)

**3. Texture Atlases:**
- Combine multiple textures into single large texture
- Reduces texture swaps (expensive GPU operation)
- Unity: Use Sprite Atlas for 2D, manual atlases for 3D
- Unreal: Use Texture Atlases or Material Atlases

**4. Mesh Combining:**
- Manually combine multiple meshes into single mesh
- Reduces draw calls but increases memory
- Best for: Static environment objects

**5. Occlusion Culling:**
- Don't render objects hidden behind other objects
- Unity: Bake occlusion data (Window → Rendering → Occlusion Culling)
- Unreal: Enable "Precomputed Visibility" or "Software Occlusion"
- Best for: Complex indoor environments

### Overdraw Reduction

**What is Overdraw?**
Rendering the same pixel multiple times per frame (e.g., overlapping transparent objects). Wastes GPU fill rate.

**How to Measure:**
- Unity: Scene view → Overdraw shading mode
- Unreal: View Mode → Shader Complexity (red = high overdraw)
- Target: <2x overdraw average, <5x overdraw max

**Techniques:**

**1. Reduce Transparent Objects:**
- Transparent objects can't be culled, always rendered
- Use opaque materials when possible
- Minimize overlapping UI elements

**2. Sort Transparent Objects:**
- Render transparent objects back-to-front
- Unity: Automatic for transparent shaders
- Reduces overdraw from overlapping transparency

**3. Use Alpha Testing Instead of Alpha Blending:**
- Alpha testing (cutout) is cheaper than alpha blending
- Best for: Foliage, fences, decals
- Limitation: Hard edges, no smooth transparency

**4. Optimize UI:**
- UI is often major source of overdraw
- Minimize overlapping UI elements
- Use opaque backgrounds instead of transparent
- Disable invisible UI elements (don't just set alpha to 0)

### Level of Detail (LOD)

**What is LOD?**
Using simpler models for distant objects to reduce rendering cost.

**LOD Levels:**
- **LOD0**: Full detail (close to camera)
- **LOD1**: 50% triangles (medium distance)
- **LOD2**: 25% triangles (far distance)
- **LOD3**: 10% triangles (very far distance)
- **Culled**: Not rendered (beyond max distance)

**VR-Specific Considerations:**
- Use more aggressive LOD than flat games (shorter transition distances)
- VR players notice detail up close, but distant objects can be simplified
- Test LOD transitions (avoid popping)

**Unity:**
- Use LOD Group component
- Assign meshes for each LOD level
- Configure transition distances (shorter for VR)

**Unreal:**
- LODs generated automatically on import
- Configure LOD settings in Static Mesh Editor
- Adjust LOD distances in World Settings (shorter for VR)

### Shader Optimization

**Mobile-Quality Shaders:**
- VR headsets have mobile-class GPUs (Quest) or console-class GPUs (PSVR2, PC VR)
- Use simplified shaders (avoid expensive operations)

**Avoid:**
- Real-time reflections (use cubemaps)
- Real-time global illumination (use baked lighting)
- Complex post-processing (bloom, depth of field, motion blur)
- Expensive math operations (sin, cos, pow, normalize)

**Unity:**
- Use "Mobile" shaders (Mobile/Diffuse, Mobile/Unlit)
- Use Universal Render Pipeline (URP) for optimized mobile shaders
- Avoid Standard shader (too expensive for VR)

**Unreal:**
- Use "Mobile" material quality level
- Disable expensive features (reflections, subsurface scattering)
- Use simple lighting models (Unlit, Default Lit)

---

## Asset Optimization

### Texture Optimization

**Texture Compression:**
- **Quest**: ASTC (Adaptive Scalable Texture Compression)
- **PSVR2**: BC7 (console compression)
- **PC VR**: BC7 or DXT5
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

### Mesh Optimization

**Polygon Count:**
- **Target**: <200k triangles per frame (total scene)
- **Characters**: 10k-30k triangles
- **Environment objects**: 1k-10k triangles
- **Props**: 500-5k triangles

**LODs:**
- Use aggressive LOD settings (5+ levels)
- Transition distances shorter than flat games
- Cull distant objects aggressively

**Collision Meshes:**
- Use simplified collision meshes (primitive shapes)
- Avoid using render mesh as collision mesh (too expensive)
- Unity: Generate collision mesh in import settings
- Unreal: Use "Simple Collision" or "Complex as Simple"

### Audio Optimization

**Spatial Audio:**
- Use spatial audio (HRTF) for immersion
- Limit simultaneous audio sources (<32)
- Use audio occlusion (sounds muffled behind walls)

**Audio Compression:**
- **Music**: Vorbis (streaming), 128-192 kbps
- **Long SFX**: Vorbis (compressed in memory), 96-128 kbps
- **Short SFX**: ADPCM (decompressed in memory), 4:1 compression
- Never use uncompressed audio in VR

**Audio Loading:**
- **Decompress on Load**: Loads fast, uses more memory
- **Compressed in Memory**: Loads slow, uses less memory, CPU overhead
- **Streaming**: No memory, CPU overhead, best for music
- VR recommendation: Stream music, decompress short SFX, compress long SFX

---

## CPU Optimization

### Scripting Optimization

**Avoid Expensive Operations in Update:**
- Don't call GetComponent every frame (cache references)
- Don't use Find or FindObjectOfType (very slow)
- Don't allocate memory in Update (causes garbage collection)
- Use object pooling for frequently spawned objects

**Physics Optimization:**
- Reduce Rigidbody count (use static colliders for non-moving objects)
- Simplify colliders (use primitive shapes, not mesh colliders)
- Use layers and collision matrix (disable unnecessary collision checks)
- Lower physics timestep (0.02-0.03 for VR)

**Garbage Collection:**
- Avoid allocations in Update (causes GC pauses)
- Use object pooling (reuse objects instead of Instantiate/Destroy)
- Use structs instead of classes for small data (stack-allocated, no GC)
- Cache strings (don't regenerate every frame)

### Multi-Threading

**Unity Jobs System:**
- Offload heavy calculations to worker threads
- Use for: Pathfinding, procedural generation, AI
- Requires C# Job System and Burst Compiler

**Unreal Task Graph:**
- Offload heavy calculations to worker threads
- Use for: Pathfinding, procedural generation, AI
- Built into Unreal Engine

---

## Platform-Specific Optimization

### Meta Quest Optimization

**Mobile GPU Constraints:**
- Qualcomm Snapdragon XR2 (mobile chipset)
- Thermal throttling after 15-20 minutes
- Battery life: 2-3 hours

**Optimization Priorities:**
1. Draw call reduction (<100 per frame)
2. Texture compression (ASTC)
3. Simplified shaders (mobile-quality)
4. Aggressive LOD and culling
5. Foveated rendering (Quest 3, Quest Pro)

**Quest-Specific Features:**
- **Fixed Foveated Rendering**: Enable for 20-30% performance boost
- **Dynamic Resolution**: Automatically lower resolution to maintain frame rate
- **Oculus Performance HUD**: Real-time performance overlay

### PSVR2 Optimization

**Console GPU Constraints:**
- PS5 GPU (RDNA 2, ~10 TFLOPS)
- Shared 16GB RAM (OS uses ~3GB)
- Must render two 2000×2040 viewpoints at 90Hz+

**Optimization Priorities:**
1. Foveated rendering via eye tracking (30-50% performance boost)
2. Forward rendering (better for VR than deferred)
3. Baked lighting (avoid real-time GI)
4. LOD and occlusion culling
5. Texture streaming (manage memory)

**PSVR2-Specific Features:**
- **Eye Tracking Foveated Rendering**: Enable for 30-50% performance boost
- **Reprojection**: Automatically fills in dropped frames (last resort, avoid relying on it)

### PC VR Optimization

**Desktop GPU Constraints:**
- Wide GPU range (GTX 1060 to RTX 4090)
- Must support low-end (GTX 1060, 6GB VRAM) and high-end (RTX 4090, 24GB VRAM)
- Players expect scalable graphics settings

**Optimization Priorities:**
1. Scalable quality settings (low, medium, high, ultra)
2. Dynamic resolution scaling (maintain frame rate)
3. Forward rendering (better for VR)
4. Texture streaming (manage VRAM)
5. Multi-threaded rendering (utilize desktop CPUs)

**PC VR-Specific Features:**
- **SteamVR Motion Smoothing**: Interpolates frames to maintain frame rate (last resort)
- **Dynamic Resolution**: Automatically lower resolution to maintain frame rate
- **Supersampling**: Render at higher resolution, downsample (improves clarity on high-end GPUs)

---

## Thermal Management and Battery Optimization

### Thermal Throttling (Quest)

**Problem:**
- Quest headsets throttle CPU/GPU when overheating (40-45°C)
- Can reduce performance by 30-50% after 10-15 minutes
- Players feel discomfort from heat

**Solutions:**
- Design for sustained performance, not peak performance
- Target 80% GPU utilization (not 100%)
- Use dynamic quality scaling (reduce quality when thermal throttling detected)
- Test over 30-60 minute sessions (not just 5 minutes)

### Battery Optimization (Quest)

**Problem:**
- Quest battery lasts 2-3 hours
- Players sensitive to battery drain
- High GPU usage drains battery quickly

**Solutions:**
- Target <80% GPU utilization
- Use fixed foveated rendering
- Lower frame rate for menus (72Hz instead of 90Hz)
- Disable unnecessary features (hand tracking when not needed)

---

## Testing and Validation

### Performance Testing Checklist

- [ ] Test on target devices (not just editor or simulator)
- [ ] Profile on lowest-spec target device (Quest 2 for standalone)
- [ ] Test 30-60 minute sessions (thermal throttling)
- [ ] Measure frame rate (90Hz target, never drop below 72Hz)
- [ ] Monitor CPU and GPU time (<11ms per frame for 90Hz)
- [ ] Check draw calls (<100 per frame)
- [ ] Check triangle count (<200k per frame)
- [ ] Test battery drain (Quest: <20% per hour)
- [ ] Test thermal performance (Quest: avoid throttling)
- [ ] Validate comfort (no motion sickness, eye strain)

### Automated Performance Testing

**Unity Performance Testing Extension:**
- Automated performance tests in CI/CD
- Measure frame rate, CPU time, GPU time
- Fail build if performance targets not met

**Unreal Automation Tool:**
- Automated performance tests
- Measure frame rate, draw calls, memory
- Generate performance reports

---

## Conclusion

VR performance optimization is critical to user comfort and experience. Target 90Hz+ frame rate, minimize draw calls and overdraw, use foveated rendering and stereo instancing, and optimize assets aggressively. Profile on target hardware regularly, test over extended sessions to catch thermal throttling, and validate comfort with real users. By following these optimization techniques, developers can create smooth, comfortable VR experiences that run well across diverse hardware.