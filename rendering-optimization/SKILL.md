---
name: rendering-optimization
description: "Optimize 3D scenes and assets for efficient real-time rendering. Use for: draw call reduction, occlusion culling, LOD systems, lighting optimization, shader performance, texture streaming, GPU profiling, achieving target frame rates, and cross-platform performance tuning."
---

# Rendering Optimization

Optimize 3D scenes for efficient real-time rendering and consistent target frame rates across platforms.

## Overview

Rendering optimization is the practice of achieving the best visual quality within strict performance budgets. Every frame has a fixed time budget (16.6ms at 60fps, 11.1ms at 90fps VR), and every draw call, shader instruction, and texture fetch competes for that budget. This skill covers systematic approaches to identifying bottlenecks, reducing GPU and CPU overhead, and maintaining visual fidelity while hitting frame rate targets.

## Performance Bottleneck Diagnosis

| Symptom | Likely Bottleneck | Diagnostic Tool | Solution Path | Reference |
|---------|-------------------|-----------------|---------------|-----------|
| Low FPS, GPU time high | Fragment/pixel bound | GPU profiler (RenderDoc, NSight) | Reduce overdraw, simplify shaders | `/references/shader-optimization.md` |
| Low FPS, CPU time high | Draw call bound | CPU profiler, frame debugger | Batch objects, merge meshes | `/references/draw-call-optimization.md` |
| Stuttering during movement | Loading/streaming | Memory profiler | Implement texture streaming, async loading | `/references/memory-optimization.md` |
| FPS drops in dense areas | Geometry bound | Triangle count overlay | Add LODs, use occlusion culling | `/references/culling-techniques.md` |
| Inconsistent frame timing | GC spikes or hitches | Frame time graph | Object pooling, reduce allocations | `/references/memory-optimization.md` |
| High memory usage | Texture memory | VRAM usage counter | Compress textures, reduce resolution | `/references/memory-optimization.md` |

## Draw Call Reduction Strategies

| Technique | Draw Call Savings | Visual Cost | Implementation Effort | Best For |
|-----------|-------------------|-------------|----------------------|----------|
| Static batching | 80–95% for static objects | None | Low | Environments, props |
| Dynamic batching | 50–70% for small meshes | None | Low (automatic) | Particles, small objects |
| GPU instancing | 90%+ for repeated objects | None | Medium | Foliage, crowds, debris |
| Texture atlasing | Enables batching | Slight UV complexity | Medium | Multiple materials → one |
| Mesh merging | Near-total elimination | Loses per-object culling | Medium | Distant or always-visible groups |
| SRP batcher (Unity) | 50–80% for SRP | None | Low (shader compatible) | Unity URP/HDRP projects |
| Indirect rendering | 95%+ for GPU-driven | Complex setup | High | Massive open worlds |

### Draw Call Budget Guidelines
- **Mobile:** <200 draw calls per frame
- **Console:** <2,000 draw calls per frame
- **PC:** <5,000 draw calls per frame
- **VR:** <500 draw calls per frame (double rendering)

## LOD (Level of Detail) Systems

| LOD Level | Screen Size | Poly Reduction | Transition Method |
|-----------|-------------|----------------|-------------------|
| LOD0 | >60% screen | 100% (full detail) | — |
| LOD1 | 30–60% screen | 50% | Cross-fade or dither |
| LOD2 | 10–30% screen | 25% | Cross-fade or pop |
| LOD3 | <10% screen | 10% or billboard | Pop to impostor |
| Culled | <1% screen | 0% (invisible) | Remove from render |

### LOD Best Practices
- Generate LODs automatically first (Simplygon, InstaLOD, engine built-in), then hand-fix issues
- Use dithered cross-fade transitions to avoid visible LOD popping
- Set LOD distances based on gameplay camera, not free camera
- Skinned meshes need LODs too — reduce bone count at lower LODs
- HLOD (Hierarchical LOD) merges distant clusters into single meshes

## Occlusion and Culling Pipeline

| Culling Stage | What It Removes | Performance Cost | Savings Potential |
|---------------|-----------------|------------------|-------------------|
| Frustum culling | Objects outside camera view | Very low (CPU) | 30–70% of scene |
| Distance culling | Objects beyond max draw distance | Very low (CPU) | 10–30% additional |
| Occlusion culling | Objects hidden behind others | Low–medium (CPU/GPU) | 20–50% in dense scenes |
| Small object culling | Sub-pixel objects | Very low | 5–15% of draw calls |
| Shadow distance culling | Shadows beyond distance | Low | 20–40% of shadow cost |
| Contribution culling | Objects too small to matter visually | Very low | Variable |

### Occlusion Implementation
- **Precomputed (Unity):** Bake occlusion data at build time, works for static scenes
- **GPU occlusion queries:** Runtime queries, 1-frame latency, good for dynamic scenes
- **Software rasterization:** CPU-based depth buffer (Unreal Nanite approach)
- **Portal-based:** Manual volume placement for interiors (rooms + portals)
- **Hierarchical Z-buffer:** GPU-driven culling using depth mip chain

## Shader Optimization Quick Reference

| Optimization | Instruction Savings | When to Apply |
|--------------|--------------------|----|
| Replace pow() with approximation | 10–50 cycles | Specular calculations |
| Use half precision (mobile) | 30–50% faster | Color, UV calculations |
| Avoid dynamic branching | Variable | Conditional effects |
| Precompute in vertex shader | Per-pixel → per-vertex | Slowly varying values |
| Use lookup textures (LUTs) | Replace complex math | Color grading, toon shading |
| Reduce texture samples | 1 sample = 4–20 cycles | Combine maps into channels |
| Avoid alpha testing (mobile) | Breaks early-Z | Use alpha blend or opaque when possible |

## Lighting Optimization

| Technique | Quality | Performance | Use Case |
|-----------|---------|-------------|----------|
| Fully baked lightmaps | High (static) | Best runtime | Static environments |
| Light probes | Good approximation | Low cost | Dynamic objects in baked scenes |
| Reflection probes | Good reflections | Medium | Shiny surfaces, interiors |
| Real-time shadows (1 light) | High fidelity | High cost | Player, key dynamic objects |
| Cascaded shadow maps | Good outdoor shadows | High | Open world, directional light |
| Screen-space shadows | Contact shadows only | Medium | Close-range detail |
| Forward+ / Clustered | Many lights | Better than deferred | Scenes with 100+ lights |

## Performance Budget Template

| Category | Mobile (16ms) | Console (16ms) | VR (11ms) |
|----------|---------------|----------------|-----------|
| CPU game logic | 4ms | 5ms | 3ms |
| CPU render prep | 3ms | 3ms | 2ms |
| GPU geometry | 2ms | 3ms | 2ms |
| GPU pixel/fragment | 4ms | 3ms | 2ms |
| GPU post-processing | 2ms | 1.5ms | 1ms |
| Buffer/headroom | 1ms | 0.5ms | 1ms |

## Profiling Workflow

1. **Capture baseline** — record 30 seconds of typical gameplay, note average and worst-case frame times
2. **Identify bound** — compare CPU vs GPU frame time; the higher one is your bottleneck
3. **Drill into bottleneck** — use engine profiler to find the most expensive calls
4. **Fix the biggest issue first** — Amdahl's Law: optimizing a 1% cost gives <1% improvement
5. **Re-measure after every change** — optimization without measurement is guessing
6. **Test on target hardware** — editor performance ≠ build performance ≠ target device performance

## Best Practices

- **Profile before optimizing** — never guess at bottlenecks; measure first
- **Set frame budgets early** — decide ms budgets per system before production ramps up
- **Optimize the biggest cost first** — 80/20 rule: a few items dominate frame time
- **Test on lowest target hardware** — if it runs on min-spec, it runs everywhere
- **Use engine built-in tools** — Unity Profiler, Unreal Insights, RenderDoc are free and powerful
- **Batch similar materials** — fewer material switches = fewer state changes = faster rendering

## Using the Reference Files

**`/references/draw-call-optimization.md`** — Read when draw calls are the bottleneck. Covers batching strategies, instancing setup, mesh merging, and SRP batcher configuration.

**`/references/shader-optimization.md`** — Read when GPU fragment time is high. Covers instruction reduction, precision optimization, shader variants, and mobile-specific techniques.

**`/references/culling-techniques.md`** — Read when too many objects are being rendered. Covers occlusion culling setup, portal systems, LOD configuration, and hierarchical culling.

**`/references/memory-optimization.md`** — Read when VRAM usage is high or streaming hitches occur. Covers texture compression, streaming systems, memory pools, and platform-specific memory budgets.
