---
name: rendering-optimization
description: "Optimize 3D scenes and assets for efficient real-time rendering. Use for: draw call reduction, occlusion culling, LOD systems, lighting optimization, shader performance, texture streaming, GPU profiling, and achieving target frame rates."
---

# Rendering Optimization

Optimize 3D scenes for efficient real-time rendering and target frame rates.

## Overview

Rendering optimization ensures smooth performance by reducing draw calls, optimizing shaders, implementing LOD systems, and efficiently managing GPU resources.

## Quick Start

| Bottleneck | Solution | Reference |
|------------|----------|-----------|
| Draw calls | Batching, atlasing | `/references/draw-call-optimization.md` |
| GPU time | Shader optimization | `/references/shader-optimization.md` |
| Overdraw | Occlusion culling | `/references/culling-techniques.md` |
| Memory | Texture streaming | `/references/memory-optimization.md` |

## Core Concepts

### Draw Call Reduction
- Static batching
- Dynamic batching
- GPU instancing
- Texture atlasing

### LOD Systems
- Distance-based LOD
- Screen-size LOD
- Automatic LOD generation
- LOD transitions

### Occlusion Culling
- Frustum culling
- Occlusion queries
- Portal-based culling
- Software occlusion

## Using the Reference Files

**`/references/draw-call-optimization.md`** — Reducing draw calls through batching and instancing.

**`/references/shader-optimization.md`** — Optimizing shader performance and complexity.

**`/references/culling-techniques.md`** — Occlusion and frustum culling strategies.

**`/references/memory-optimization.md`** — Texture streaming and memory management.
