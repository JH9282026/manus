# Unity Rendering and Performance Optimization

Comprehensive guide to optimizing Unity games for maximum performance across platforms.

---

## Rendering Pipeline Selection

### Built-in Render Pipeline

**When to Use:**
- Legacy projects requiring backward compatibility
- Simple games with basic lighting needs
- Projects with extensive custom shaders written for Built-in RP

**Limitations:**
- Less efficient than SRP (Scriptable Render Pipeline)
- Limited modern rendering features
- No Shader Graph support
- Harder to customize rendering

### Universal Render Pipeline (URP)

**When to Use:**
- Mobile games (iOS, Android)
- Cross-platform projects (mobile, PC, console)
- 2D games with advanced lighting
- VR/AR applications
- Projects requiring good performance with modern features

**Advantages:**
- Optimized for performance across all platforms
- Shader Graph support for visual shader creation
- 2D Lights and shadows
- Post-processing stack included
- SRP Batcher for draw call optimization
- Customizable via Renderer Features

**Configuration:**
```
URP Asset Settings:
- Rendering Path: Forward (mobile) or Deferred (PC/console)
- Depth Texture: Only if needed (expensive on mobile)
- Opaque Texture: Disable unless using refraction
- HDR: Disable on mobile for performance
- MSAA: 2x or 4x on mobile, higher on PC
- Shadow Resolution: 1024-2048 on mobile, 2048-4096 on PC
```

### High Definition Render Pipeline (HDRP)

**When to Use:**
- High-end PC and console games
- Architectural visualization
- Photorealistic rendering requirements
- Projects targeting powerful hardware

**Features:**
- Physically-based lighting and materials
- Ray tracing support
- Volumetric lighting and fog
- Advanced post-processing
- Screen Space Global Illumination (SSGI)

**Not Suitable For:**
- Mobile devices
- Low-end PCs
- WebGL
- VR (too demanding)

---

## Draw Call Optimization

### Understanding Draw Calls

Each draw call is a command from CPU to GPU to render a mesh. Reducing draw calls improves performance.

**Target Draw Calls:**
- Mobile: 50-100 draw calls per frame
- PC: 500-1000 draw calls per frame
- Console: 1000-2000 draw calls per frame

### Static Batching

**How It Works:**
Combines static (non-moving) objects with the same material into a single draw call.

**Setup:**
1. Mark GameObjects as "Static" in Inspector
2. Ensure objects share the same material
3. Enable Static Batching in Player Settings

**Limitations:**
- Increases memory usage (combined meshes stored)
- Objects cannot move
- Only works with objects using same material

### Dynamic Batching

**How It Works:**
Automatically batches small moving objects at runtime.

**Requirements:**
- Meshes must have fewer than 300 vertices
- Objects must share the same material
- No scale differences between objects

**When to Use:**
- Small particles, UI elements
- Simple moving objects (coins, pickups)

**Limitations:**
- CPU overhead for combining meshes
- Only works with very small meshes
- Less effective than SRP Batcher

### SRP Batcher (URP/HDRP)

**How It Works:**
Reduces CPU overhead by batching draw calls with compatible shaders, even with different materials.

**Setup:**
1. Enable in URP/HDRP Asset settings
2. Use Shader Graph or SRP-compatible shaders
3. Avoid per-material property changes in scripts

**Best Practices:**
- Use MaterialPropertyBlocks for per-object variations
- Keep shader variants minimal
- Avoid frequent material property changes

**Performance Impact:**
Can reduce CPU rendering time by 50% or more.

### GPU Instancing

**How It Works:**
Renders multiple copies of the same mesh in a single draw call.

**Setup:**
```csharp
// Enable in material shader
#pragma multi_compile_instancing

// In shader properties
UNITY_INSTANCING_BUFFER_START(Props)
    UNITY_DEFINE_INSTANCED_PROP(float4, _Color)
UNITY_INSTANCING_BUFFER_END(Props)
```

**Use Cases:**
- Vegetation (trees, grass)
- Crowds of characters
- Repeated environment objects

**Requirements:**
- Same mesh and material
- Per-instance properties via MaterialPropertyBlock

---

## Texture Optimization

### Texture Compression

| Platform | Format | Quality | Use Case |
|----------|--------|---------|----------|
| iOS | PVRTC | Good | Mobile, older devices |
| iOS | ASTC | Better | Modern iOS devices |
| Android | ETC2 | Good | All Android devices |
| Android | ASTC | Best | High-end Android |
| PC | DXT/BC | Excellent | Desktop |
| Console | Platform-specific | Excellent | PS5, Xbox |

**Settings:**
```
Texture Import Settings:
- Max Size: 2048 for main textures, 512-1024 for details
- Compression: Platform-specific (ASTC/ETC2 for mobile)
- Mipmaps: Enable for 3D textures, disable for UI
- Read/Write: Disable unless needed (doubles memory)
```

### Texture Atlasing

Combine multiple textures into a single atlas to reduce draw calls.

**Tools:**
- Sprite Atlas (2D)
- Texture Packer (external tool)
- Unity's Sprite Packer

**Benefits:**
- Fewer texture swaps
- Better batching
- Reduced memory bandwidth

### Mipmap Optimization

**What Are Mipmaps:**
Pre-calculated lower-resolution versions of textures for distant objects.

**Benefits:**
- Reduces texture aliasing
- Improves performance (GPU reads less data)
- Reduces memory bandwidth

**When to Disable:**
- UI textures (always viewed at same distance)
- Skyboxes
- Textures that never scale

---

## Lighting Optimization

### Realtime vs. Baked Lighting

| Type | Performance | Flexibility | Use Case |
|------|-------------|-------------|----------|
| Realtime | Expensive | High | Dynamic scenes, moving lights |
| Baked | Fast | Low | Static environments |
| Mixed | Moderate | Medium | Static environment + dynamic objects |

### Lightmapping (Baked Lighting)

**Setup:**
1. Mark static objects as "Lightmap Static"
2. Set lights to "Baked" or "Mixed" mode
3. Configure Lighting Settings:
   - Lightmap Resolution: 20-40 for mobile, 40-80 for PC
   - Lightmap Size: 1024-2048
   - Enable Progressive GPU Lightmapper
4. Generate Lighting

**Benefits:**
- Near-zero runtime cost
- High-quality shadows and global illumination
- Supports complex lighting scenarios

**Limitations:**
- Cannot change at runtime
- Increases build size
- Requires baking time

### Light Probe Optimization

Light Probes capture baked lighting for dynamic objects.

**Placement:**
- Place in areas where dynamic objects move
- Higher density in areas with lighting variation
- Avoid placing too many (expensive to interpolate)

**Best Practices:**
- Use Light Probe Groups for manual placement
- 50-200 probes for small scenes
- 200-500 for medium scenes
- Avoid excessive probe density

### Reflection Probes

Capture environment reflections for realistic materials.

**Types:**
- **Baked:** Pre-rendered, fast, static reflections
- **Realtime:** Dynamic, expensive, updates every frame
- **Custom:** Manually assigned cubemap

**Optimization:**
- Use baked probes for static environments
- Limit realtime probes to 1-2 per scene
- Reduce resolution (128-256 for mobile, 512-1024 for PC)
- Disable "Box Projection" if not needed

### Shadow Optimization

**Shadow Settings:**
```
Quality Settings:
- Shadow Distance: 50-100 on mobile, 150-300 on PC
- Shadow Cascades: 2 on mobile, 4 on PC
- Shadow Resolution: Medium on mobile, High on PC
```

**Per-Light Settings:**
- Use "Soft Shadows" sparingly (expensive)
- Reduce shadow distance for less important lights
- Disable shadows on small/distant lights

**Mobile Optimization:**
- Limit to 1-2 shadow-casting lights
- Use baked shadows where possible
- Reduce shadow resolution to 512-1024

---

## Level of Detail (LOD)

### LOD Groups

Automatically switch between mesh detail levels based on distance.

**Setup:**
1. Create LOD meshes (high, medium, low poly)
2. Add LOD Group component
3. Assign meshes to LOD levels
4. Configure transition percentages

**Recommended LOD Levels:**
- LOD 0 (0-25%): Full detail, 10,000+ triangles
- LOD 1 (25-50%): Medium detail, 5,000 triangles
- LOD 2 (50-75%): Low detail, 1,000 triangles
- LOD 3 (75-100%): Culled or billboard

**Tools:**
- Unity's LOD Group component
- Simplygon (automatic LOD generation)
- Blender (manual LOD creation)

### Billboard Rendering

Replace distant 3D objects with 2D sprites.

**Use Cases:**
- Distant trees in forests
- Background buildings
- Crowd characters

**Implementation:**
- Use as final LOD level
- Render 3D object to texture
- Display as quad facing camera

---

## Occlusion Culling

### What Is Occlusion Culling

Prevents rendering objects hidden behind other objects.

**Setup:**
1. Mark occluders as "Occluder Static" (large objects that block view)
2. Mark occludees as "Occludee Static" (objects that can be hidden)
3. Bake occlusion data: Window > Rendering > Occlusion Culling
4. Configure settings:
   - Smallest Occluder: 5 (larger = faster bake, less accurate)
   - Smallest Hole: 0.25
   - Backface Threshold: 100

**Best Practices:**
- Use for indoor scenes and dense environments
- Mark large walls, buildings as occluders
- Don't use for open outdoor scenes (overhead not worth it)
- Test with Occlusion Culling visualization

**Performance Impact:**
Can reduce draw calls by 30-70% in dense scenes.

---

## Mobile-Specific Optimizations

### Graphics API Selection

| Platform | Recommended API | Fallback |
|----------|----------------|----------|
| iOS | Metal | OpenGL ES 3 |
| Android | Vulkan | OpenGL ES 3 |

### Mobile Quality Settings

```
Recommended Settings:
- Pixel Light Count: 1
- Texture Quality: Medium
- Anisotropic Textures: Per Texture
- Anti Aliasing: 2x MSAA (or disabled)
- Soft Particles: Disabled
- Realtime Reflection Probes: Disabled
- Billboards Face Camera: Enabled
```

### Overdraw Reduction

Overdraw occurs when pixels are drawn multiple times (transparent objects, UI).

**Visualization:**
- Scene View > Overdraw mode
- Red areas = high overdraw (bad)

**Reduction Techniques:**
- Minimize transparent objects
- Use opaque shaders where possible
- Optimize UI (disable invisible elements)
- Sort transparent objects front-to-back

### Shader Variants

Reduce shader compilation time and build size.

**Optimization:**
- Disable unused shader features in URP Asset
- Use Shader Variant Stripping
- Avoid multi_compile directives when possible
- Use shader_feature for optional features

---

## Profiling and Debugging

### Unity Profiler

**Key Metrics:**
- **CPU Usage:** Should be under 16ms for 60 FPS
- **Rendering:** Draw calls, batches, triangles
- **Memory:** Allocations, GC spikes
- **GPU:** Fragment shader cost, vertex processing

**Profiling Workflow:**
1. Profile on target device (not Editor)
2. Identify bottlenecks (CPU vs GPU)
3. Focus on highest time consumers
4. Make changes and re-profile

### Frame Debugger

Step through rendering frame-by-frame.

**Usage:**
1. Window > Analysis > Frame Debugger
2. Enable and step through draw calls
3. Identify redundant draws, state changes
4. Optimize material/shader usage

### GPU Profiling

**Tools:**
- Unity Profiler (GPU module)
- RenderDoc (external, detailed GPU analysis)
- Platform-specific tools (Xcode, Android GPU Inspector)

**Common GPU Bottlenecks:**
- High-resolution textures
- Complex fragment shaders
- Excessive overdraw
- Too many vertices

---

## Best Practices Summary

### Do:
- Use URP for most projects
- Enable SRP Batcher
- Bake lighting for static scenes
- Use LOD Groups for detailed meshes
- Compress textures appropriately
- Profile on target devices
- Use object pooling for frequently spawned objects

### Don't:
- Use realtime lights excessively on mobile
- Ignore draw call counts
- Use uncompressed textures
- Enable features you don't need
- Optimize prematurely (profile first)
- Forget to test on low-end devices

Optimization is an iterative process. Profile, identify bottlenecks, optimize, and repeat.