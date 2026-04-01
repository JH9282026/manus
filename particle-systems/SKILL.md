---
name: particle-systems
description: "Design and implement particle systems for visual effects in games and real-time applications. Use for: fire and smoke effects, magic and energy effects, weather systems, destruction effects, environmental particles, optimizing particle performance, creating reusable particle libraries, and GPU particle systems."
---

# Particle Systems

Design and implement particle systems for compelling real-time visual effects in games and interactive applications.

## Overview

Particle systems simulate complex visual phenomena — fire, smoke, magic, weather, destruction — using thousands of small elements (sprites, meshes, or GPU points) controlled by emission, physics, and rendering rules. This skill covers particle design principles, emitter configuration, GPU vs CPU particles, optimization strategies, and engine-specific implementation in Unity VFX Graph and Unreal Niagara.

## Effect Type Selection Guide

| Effect | System Type | Particle Count | Emitter Style | Performance Cost | Reference |
|--------|-------------|----------------|---------------|-----------------|-----------|
| Campfire | CPU sprite | 50–200 | Continuous cone | Low | `/references/fire-smoke-effects.md` |
| Explosion | GPU burst | 500–2,000 | Burst sphere | Medium–High | `/references/fire-smoke-effects.md` |
| Magic projectile | GPU trail | 100–500 | Point + ribbon | Medium | `/references/magic-energy-effects.md` |
| Rain | GPU instanced | 5,000–50,000 | Volume box | Medium | `/references/weather-systems.md` |
| Snow | CPU/GPU sprite | 1,000–10,000 | Volume box + wind | Low–Medium | `/references/weather-systems.md` |
| Dust motes | CPU sprite | 50–200 | Volume around camera | Very Low | `/references/weather-systems.md` |
| Sparks | GPU sprite | 200–1,000 | Burst point | Low | `/references/magic-energy-effects.md` |
| Smoke trail | CPU ribbon | 20–100 segments | Ribbon along path | Low–Medium | `/references/fire-smoke-effects.md` |

## Particle Property Fundamentals

### Core Properties

| Property | Description | Typical Range | Animation Curve |
|----------|-------------|---------------|-----------------|
| Lifetime | How long particle exists | 0.1–10 seconds | — |
| Start size | Initial particle size | 0.01–5 world units | — |
| Size over life | Size change during lifetime | Grow then shrink | Bell curve |
| Start color | Initial RGBA color | Per-effect | — |
| Color over life | Color change over time | Bright → dim | Gradient ramp |
| Start speed | Initial velocity magnitude | 0.1–20 units/sec | — |
| Gravity modifier | Downward acceleration | -1 to 1 | — |
| Rotation | Spin speed and direction | 0–360 deg/sec | Random range |
| Drag | Air resistance | 0–5 | Higher = faster slowdown |

### Emitter Configuration

| Emitter Shape | Use Case | Key Parameters |
|--------------|----------|----------------|
| Point | Sparks, impacts | Direction, speed range |
| Cone | Fire, fountains | Angle, radius, emit from edge |
| Sphere | Explosions, magic auras | Radius, emit from shell vs volume |
| Box/Volume | Rain, snow, ambient | Size, velocity direction |
| Mesh surface | Dissolve, aura effects | Surface normals, UV-based emission |
| Edge/Line | Laser, beam effects | Start/end points, distribution |
| Circle/Ring | Shockwaves, portals | Radius, emit from edge |

## GPU vs CPU Particles

| Factor | CPU Particles | GPU Particles |
|--------|--------------|---------------|
| Max particle count | ~10,000 practical | 100,000–1,000,000+ |
| Per-particle logic | Full scripting access | Shader/compute only |
| Collision | Physics-based, accurate | Depth buffer or SDF, approximate |
| Sorting | Accurate back-to-front | Limited or none |
| Performance scaling | Linear with count | Massively parallel |
| Engine support | All engines | Unity VFX Graph, Unreal Niagara/GPU |
| Best for | Small counts, complex behavior | Large counts, simple behavior |

### When to Choose GPU Particles
- Particle count exceeds 5,000
- Simple physics (gravity + drag only)
- No per-particle collision response needed
- Visual density is the priority (rain, snow, sparks, magic fields)

## Common Effect Recipes

### Fire Effect Stack
1. **Core flame:** Orange–yellow sprites, size grows over life, fade out at end
2. **Ember sparks:** Small bright particles with high initial velocity, long gravity drag
3. **Smoke:** Large dark sprites above flame, slow rise, high drag, fade to transparent
4. **Heat distortion:** Screen-space distortion shader on invisible emitter (if supported)
5. **Light source:** Point light with flicker animation at fire position

### Impact/Hit Effect
1. **Flash:** Single large sprite, 0.05s lifetime, bright white
2. **Sparks:** Burst of 20–50 small particles, high speed, gravity, bounce
3. **Debris:** Mesh particles (small chunks), physics-enabled, short lifetime
4. **Dust cloud:** Slow-expanding ring of soft sprites
5. **Decal:** Scorch mark or impact crater on surface

## Engine-Specific Implementation

| Feature | Unity VFX Graph | Unreal Niagara |
|---------|----------------|----------------|
| System type | Visual graph (GPU) | Module stack (GPU/CPU) |
| Particle capacity | Millions | Millions |
| Custom logic | HLSL blocks | Module scripts, HLSL |
| Events/triggers | GPU events, spawn on death | Event handlers, data interfaces |
| Mesh particles | Supported | Supported |
| Ribbon/trails | Supported | Ribbon renderer |
| Signed Distance Fields | Supported | Supported for collision |
| LOD system | Manual distance check | Built-in scalability |

## Performance Optimization

| Technique | Savings | Trade-off |
|-----------|---------|-----------|
| Reduce particle count | Proportional | Less visual density |
| Lower overdraw (smaller particles) | Major on mobile | Less coverage |
| Use GPU particles | 10–100× count ceiling | Less per-particle control |
| Particle LOD by distance | 50–80% at distance | Pop if aggressive |
| Disable collision on distant FX | Significant CPU savings | Less physical accuracy |
| Limit active emitters | Proportional | Fewer simultaneous effects |
| Pool and reuse systems | Eliminates spawn overhead | Memory reservation |
| Reduce texture resolution | VRAM savings | Slightly softer particles |

### Performance Budget (per platform)
- **Mobile:** 500–2,000 total particles on screen, <5 emitters active
- **Console:** 10,000–50,000 particles, <30 emitters active
- **PC:** 50,000–500,000 (GPU), <50 emitters active
- **VR:** 2,000–10,000 particles, minimize overdraw

## Best Practices

- **Layer multiple simple systems** rather than one complex system — fire = flame + sparks + smoke + light
- **Use flipbook/sprite sheet animation** for complex shapes (smoke puffs, explosions)
- **Match particle color to scene lighting** — particles that ignore scene light look pasted on
- **Add randomness to everything** — random lifetime, size, speed, rotation prevents uniformity
- **Pre-warm looping effects** — avoid the "startup" look when entering an area
- **Sort transparent particles** only when needed — sorting is expensive on GPU

## Using the Reference Files

**`/references/fire-smoke-effects.md`** — Read when creating fire, explosions, smoke, or combustion effects. Covers flame shader techniques, flipbook animations, and volumetric smoke approaches.

**`/references/magic-energy-effects.md`** — Read when designing stylized game effects like spells, energy beams, impacts, or UI particles. Covers shader tricks, color ramps, and distortion effects.

**`/references/weather-systems.md`** — Read when implementing rain, snow, fog, or environmental ambiance particles. Covers large-volume emitters, wind integration, and camera-relative spawning.

**`/references/particle-optimization.md`** — Read when particle effects cause frame rate drops. Covers LOD systems, overdraw reduction, GPU migration, and per-platform budgets.
