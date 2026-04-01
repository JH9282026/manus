---
name: 3d-game-development
description: "Create 3D games with comprehensive modeling, animation, and rendering techniques using Blender, Maya, 3ds Max, and game engines. Use for: 3D character modeling and rigging, environment and prop creation, texturing with PBR workflows, skeletal animation and motion capture, implementing 3D physics and collision systems, optimizing polygon counts and LOD systems, creating realistic lighting and materials, developing first-person and third-person games, and building immersive 3D worlds for PC, console, VR, and mobile platforms."
---

# 3D Game Development

Create immersive 3D games through modeling, animation, rendering, and engine integration.

## Overview

3D game development encompasses the creation of three-dimensional interactive experiences, from modeling and texturing assets to implementing gameplay systems in game engines. This skill covers 3D modeling software (Blender, Maya, 3ds Max), texturing workflows (PBR materials), rigging and animation, rendering optimization (LOD, culling, lighting), physics systems, and integration with game engines (Unity, Unreal). 3D games dominate PC, console, and VR platforms, requiring specialized technical and artistic skills.

## 3D Modeling Fundamentals

### Modeling Software Comparison

| Software | Cost | Best For | Industry Use | Learning Curve |
|----------|------|----------|--------------|----------------|
| **Blender** | Free | All-purpose, indie dev | Growing | Medium |
| **Maya** | $235/mo | Animation, rigging | AAA studios | High |
| **3ds Max** | $235/mo | Environment art, arch viz | AAA (esp. environments) | High |
| **ZBrush** | $40/mo | High-poly sculpting, characters | Character artists | High |
| **Houdini** | Free-$269/mo | Procedural, VFX | Technical artists | Very High |

**Recommendation for Game Dev:**
- **Beginners:** Blender (free, comprehensive, good community)
- **Professionals:** Maya (animation) or 3ds Max (environments)
- **Character Artists:** ZBrush + Blender/Maya
- **Technical Artists:** Houdini

### Polygon Modeling

**Mesh Components:**
- **Vertices:** Points in 3D space
- **Edges:** Lines connecting vertices
- **Faces:** Polygons (usually triangles or quads) formed by edges

**Modeling Techniques:**

**Box Modeling:**
Start with primitive (cube, sphere) and refine.
- Good for: Hard-surface objects, props, buildings

**Edge Modeling:**
Build mesh edge-by-edge from scratch.
- Good for: Organic shapes, characters, creatures

**Sculpting:**
Digital clay sculpting for high detail.
- Good for: Characters, organic surfaces, detail passes

### Polygon Count Guidelines

| Platform | Character | Environment | Props |
|----------|-----------|-------------|-------|
| **Mobile** | 5K-15K tris | 50K-150K tris | 500-3K tris |
| **PC/Console** | 20K-50K tris | 200K-500K tris | 2K-10K tris |
| **VR** | 10K-30K tris | 100K-300K tris | 1K-5K tris |
| **High-End** | 50K-100K+ tris | 500K-1M+ tris | 5K-20K tris |

**Optimization:**
- Use quads during modeling (convert to tris on export)
- Avoid n-gons (polygons with more than 4 sides)
- Keep topology clean and even
- Remove hidden/internal faces

### Topology Best Practices

**Good Topology:**
- Even quad distribution
- Edge loops follow form and deformation
- Minimal triangles (except on export)
- No overlapping vertices

**Character Topology:**
- Edge loops around eyes, mouth for facial animation
- Edge loops around joints (shoulders, elbows, knees) for deformation
- Consistent density (don't mix high/low poly areas abruptly)

## Texturing and Materials

### PBR (Physically Based Rendering)

Modern standard for realistic materials.

**PBR Texture Maps:**

| Map | Purpose | Values |
|-----|---------|--------|
| **Albedo/Base Color** | Surface color (no lighting info) | RGB color |
| **Metallic** | Metal vs. non-metal | 0 (non-metal) to 1 (metal) |
| **Roughness** | Surface smoothness | 0 (smooth/shiny) to 1 (rough/matte) |
| **Normal** | Surface detail without geometry | RGB (XYZ directions) |
| **Ambient Occlusion** | Crevice shading | 0 (occluded) to 1 (exposed) |
| **Height/Displacement** | Surface depth | Grayscale height values |
| **Emissive** | Self-illumination | RGB color + intensity |

**PBR Workflow:**
1. Create high-poly model (sculpting)
2. Create low-poly model (game mesh)
3. UV unwrap low-poly model
4. Bake high-poly details to normal map
5. Create PBR textures (Substance Painter, Quixel, Photoshop)
6. Import to game engine

### UV Mapping

**UV Unwrapping:**
Flatten 3D model surface to 2D texture space.

**Unwrapping Techniques:**
- **Automatic:** Quick, often needs manual cleanup
- **Smart UV Project:** Good starting point
- **Manual Seams:** Mark edges where model "unfolds," then unwrap
- **Cylindrical/Spherical:** For round objects

**Best Practices:**
- Minimize seams (hide on less visible areas)
- Avoid stretching (check UV checker pattern)
- Use texture space efficiently (pack UVs tightly)
- Consistent texel density (similar detail across model)
- Leave small padding between UV islands (prevent bleeding)

### Texture Resolution

| Asset Type | Mobile | PC/Console | High-End |
|------------|--------|------------|----------|
| **Character** | 1024x1024 | 2048x2048 | 4096x4096 |
| **Environment** | 512x512 | 1024x1024 | 2048x2048 |
| **Props** | 256x256 | 512x512 | 1024x1024 |
| **UI** | 512x512 | 1024x1024 | 2048x2048 |

**Texture Atlasing:**
Combine multiple textures into one atlas to reduce draw calls.

## Rigging and Animation

### Skeletal Rigging

**Armature/Skeleton:**
Bone hierarchy controlling mesh deformation.

**Rigging Process:**
1. Create bone structure matching character anatomy
2. Position bones inside mesh
3. Skin mesh to bones (weight painting)
4. Test deformation, adjust weights
5. Add control rig (IK, constraints) for animators

**Common Bone Chains:**
- Spine (hips → chest → neck → head)
- Arms (shoulder → upper arm → forearm → hand → fingers)
- Legs (thigh → shin → foot → toes)

### Weight Painting

Defines how much each bone influences each vertex.

**Best Practices:**
- Smooth gradients at joints
- 100% weight at bone centers
- Gradual falloff toward neighboring bones
- Test with extreme poses
- Fix clipping and unnatural deformation

### Animation Techniques

**Keyframe Animation:**
Manually set poses at key moments, engine interpolates between.

**Motion Capture (MoCap):**
Record real actor movements, apply to 3D character.
- **Pros:** Realistic, fast for complex animations
- **Cons:** Expensive equipment, requires cleanup, less stylized

**Procedural Animation:**
Code-driven animation (IK, physics-based).
- **Use:** Foot placement, looking at targets, ragdolls

**Animation Blending:**
Smoothly transition between animations.
- Walk → Run (blend based on speed)
- Idle → Attack (transition animation)

### Animation Best Practices

**Frame Rate:**
- 30 FPS: Standard for games
- 60 FPS: Smooth, but doubles file size
- 24 FPS: Cinematic, stylized

**Animation Types:**
- **Looping:** Walk, run, idle (seamless start/end)
- **One-Shot:** Attack, jump, death (play once)
- **Additive:** Breathing, looking (layered on base animation)

**Root Motion:**
Animation drives character movement (vs. code-driven).
- **Use:** Cinematic movement, attacks with lunges
- **Avoid:** Responsive player control (use code instead)

## 3D Rendering and Lighting

### Lighting Types

**Directional Light:**
Simulates sun (parallel rays, infinite distance).
- **Use:** Outdoor scenes, primary light source

**Point Light:**
Emits light in all directions from a point.
- **Use:** Lamps, torches, explosions

**Spot Light:**
Cone-shaped light beam.
- **Use:** Flashlights, stage lights, focused illumination

**Area Light:**
Light emitted from a surface.
- **Use:** Soft lighting, windows, light panels

### Lighting Techniques

**Three-Point Lighting:**
Classic setup for characters:
1. **Key Light:** Main light source (brightest)
2. **Fill Light:** Softens shadows from key light
3. **Rim/Back Light:** Separates subject from background

**Baked vs. Realtime Lighting:**

| Type | Performance | Flexibility | Use Case |
|------|-------------|-------------|----------|
| **Baked** | Fast | Static only | Static environments, mobile |
| **Realtime** | Expensive | Fully dynamic | Dynamic scenes, destructible environments |
| **Mixed** | Moderate | Hybrid | Static environment + dynamic objects |

**Global Illumination:**
Indirect lighting (light bouncing off surfaces).
- **Baked GI:** Pre-calculated, fast, static
- **Realtime GI:** Dynamic, expensive (Lumen in UE5, SSGI)

### Shadows

**Shadow Types:**
- **Hard Shadows:** Sharp edges, fast
- **Soft Shadows:** Blurred edges, realistic, expensive

**Shadow Mapping:**
- **Resolution:** Higher = sharper shadows, more memory
- **Distance:** Limit shadow rendering distance
- **Cascades:** Multiple shadow maps at different distances (for directional lights)

**Optimization:**
- Bake shadows for static objects
- Limit realtime shadow-casting lights (1-3 on mobile)
- Use lower resolution for distant shadows

## Level of Detail (LOD)

### LOD System

Automatically switch between mesh detail levels based on distance.

**LOD Levels:**
- **LOD 0:** Full detail (close to camera)
- **LOD 1:** Medium detail (medium distance)
- **LOD 2:** Low detail (far distance)
- **LOD 3:** Very low or culled (very far)

**Polygon Reduction:**
- LOD 0: 100% polygons
- LOD 1: 50% polygons
- LOD 2: 25% polygons
- LOD 3: 10% polygons or billboard

**Tools:**
- Blender: Decimate modifier
- Simplygon: Automatic LOD generation
- Engine tools: Unity/Unreal LOD groups

### Culling Techniques

**Frustum Culling:**
Don't render objects outside camera view (automatic in engines).

**Occlusion Culling:**
Don't render objects hidden behind other objects.
- **Setup:** Mark occluders (large objects), bake occlusion data
- **Use:** Indoor scenes, dense cities

**Distance Culling:**
Don't render objects beyond certain distance.

## 3D Physics

### Collision Shapes

**Simple Colliders (Fast):**
- **Box:** Rectangular objects, walls, crates
- **Sphere:** Balls, round objects
- **Capsule:** Characters, pills
- **Cylinder:** Barrels, columns

**Complex Colliders (Slow):**
- **Mesh Collider:** Exact mesh shape (use sparingly)
- **Convex Mesh:** Simplified convex hull

**Best Practices:**
- Use simple colliders whenever possible
- Combine multiple simple colliders for complex shapes
- Create separate low-poly collision mesh
- Avoid mesh colliders for moving objects

### Rigidbody Physics

**Properties:**
- **Mass:** Object weight (affects force response)
- **Drag:** Air resistance
- **Angular Drag:** Rotation resistance
- **Gravity:** Enable/disable gravity
- **Constraints:** Freeze position/rotation axes

**Physics Materials:**
- **Friction:** Surface grip (ice = low, rubber = high)
- **Bounciness:** Restitution (0 = no bounce, 1 = perfect bounce)

## Game Engine Integration

### Asset Import Pipeline

**Workflow:**
1. Model in 3D software (Blender, Maya, etc.)
2. Export to engine-compatible format (FBX, OBJ, GLTF)
3. Import to game engine
4. Configure import settings (scale, materials, animations)
5. Set up prefabs/blueprints

**Export Settings:**
- **Format:** FBX (most compatible), GLTF (modern, open)
- **Scale:** Match engine units (Unity: 1 unit = 1 meter)
- **Axis:** Y-up (Unity, Unreal) vs. Z-up (Blender)
- **Triangulate:** Convert quads to triangles
- **Bake Transforms:** Apply scale, rotation

### Material Setup in Engine

**Unity:**
- Create materials with shaders (Standard, URP/Lit, HDRP/Lit)
- Assign texture maps to material slots
- Adjust material properties (metallic, smoothness, normal strength)

**Unreal:**
- Create material with Material Editor
- Connect texture samples to material inputs
- Compile and assign to mesh

## Performance Optimization

### Rendering Optimization

**Draw Call Reduction:**
- Combine meshes with same material
- Use texture atlases
- Enable GPU instancing for repeated objects
- Use static batching for non-moving objects

**Polygon Optimization:**
- Implement LOD systems
- Remove hidden faces
- Optimize character topology
- Use normal maps instead of geometry for detail

**Texture Optimization:**
- Compress textures (DXT, ASTC, ETC2)
- Use mipmaps
- Reduce resolution where possible
- Texture atlasing

### Memory Optimization

**Asset Streaming:**
Load/unload assets based on player location.

**Object Pooling:**
Reuse objects instead of instantiate/destroy.

**Texture Compression:**
- Mobile: ASTC (Android), PVRTC (iOS)
- PC: DXT/BC
- Reduce memory usage by 75%+

## Using the Reference Files

### When to Read Each Reference

**`/references/3d-modeling-texturing.md`** — Read when creating 3D models in Blender/Maya/3ds Max, UV unwrapping meshes, creating PBR textures, or learning modeling best practices and topology guidelines.

**`/references/animation-rigging.md`** — Read when rigging characters, weight painting, creating skeletal animations, implementing motion capture, or setting up animation systems in game engines.

**`/references/3d-rendering-optimization.md`** — Read when optimizing rendering performance, implementing LOD systems, configuring lighting and shadows, reducing draw calls, or troubleshooting performance bottlenecks.

**`/references/3d-game-implementation.md`** — Read when integrating 3D assets into game engines, setting up physics systems, implementing gameplay mechanics, or deploying 3D games to various platforms.

## References

- [3D Game Implementation](references/3d-game-implementation.md)
- [3D Modeling Texturing](references/3d-modeling-texturing.md)
- [3D Rendering Optimization](references/3d-rendering-optimization.md)
- [Animation Rigging](references/animation-rigging.md)
