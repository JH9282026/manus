---
name: procedural-generation
description: "Design and implement procedural content generation systems for games and simulations. Use for: terrain generation, procedural textures, vegetation placement, architectural generation, dungeon/level design, noise functions, L-systems, wave function collapse, and creating infinite or varied content."
---

# Procedural Generation

Design and implement procedural content generation systems that create varied, scalable, and replayable content for games and simulations.

## Overview

Procedural generation uses algorithms and rules to create content programmatically rather than by hand. It enables infinite worlds, varied gameplay, and reduced art production costs. This skill covers core noise functions, terrain generation, vegetation placement, architectural systems, and modern techniques like Wave Function Collapse (WFC) — with practical implementation guidance for game engines.

## Algorithm Selection Guide

| Content Type | Algorithm | Control Level | Performance | Quality | Reference |
|-------------|-----------|---------------|-------------|---------|-----------|
| Terrain heightmaps | Perlin/Simplex noise + erosion | Medium | Fast | High | `/references/terrain-generation.md` |
| Cave systems | Cellular automata + marching cubes | Medium | Fast | Good | `/references/terrain-generation.md` |
| Dungeons/levels | BSP tree or WFC | High | Fast | High | `/references/architectural-generation.md` |
| Buildings/cities | L-systems + shape grammar | High | Medium | High | `/references/architectural-generation.md` |
| Vegetation | Poisson disk + L-systems | Medium | Fast | High | `/references/vegetation-systems.md` |
| Textures/materials | Noise layering + math functions | Medium | Fast (GPU) | High | `/references/procedural-textures.md` |
| Loot/items | Weighted random + affixes | High | Instant | Game-dependent | `/references/architectural-generation.md` |
| Names/text | Markov chains + grammars | Medium | Instant | Variable | `/references/architectural-generation.md` |

## Noise Functions Deep Dive

### Noise Type Comparison

| Noise Type | Dimensions | Speed | Artifacts | Best For |
|-----------|------------|-------|-----------|----------|
| Perlin noise | 1D–4D | Fast | Grid-aligned at octave 1 | Terrain, clouds, general purpose |
| Simplex noise | 1D–nD | Faster | Fewer artifacts than Perlin | Same as Perlin, better quality |
| Worley/Voronoi | 2D–3D | Medium | Cell-like patterns | Stone, cells, cracked surfaces |
| Value noise | 1D–3D | Fastest | Blocky at low frequency | Quick prototyping |
| OpenSimplex 2 | 2D–4D | Fast | Minimal | Modern replacement for Perlin |

### Fractal Noise (FBM — Fractional Brownian Motion)

| Parameter | Effect | Typical Range |
|-----------|--------|---------------|
| Octaves | Detail layers | 4–8 (more = more detail, slower) |
| Frequency (lacunarity) | Scale change per octave | 2.0 (standard doubling) |
| Amplitude (persistence) | Weight per octave | 0.5 (each octave half as strong) |
| Scale | Base noise size | Scene-dependent |
| Offset/seed | Starting position | Random per generation |

### Noise Combination Techniques
- **Addition (FBM):** Layer octaves for natural terrain
- **Ridged multifractal:** Absolute value + inversion for mountain ridges
- **Turbulence:** Absolute value of noise for fire, smoke textures
- **Domain warping:** Use one noise to distort another's coordinates for organic shapes
- **Terracing:** Quantize noise output for plateau/step effects

## Terrain Generation Pipeline

| Stage | Operation | Input | Output |
|-------|-----------|-------|--------|
| 1. Base shape | Continent/island mask | Parameters, seed | Binary land/water |
| 2. Height generation | Multi-octave noise | Base mask, noise params | Heightmap |
| 3. Erosion simulation | Hydraulic + thermal erosion | Heightmap | Eroded heightmap |
| 4. Biome assignment | Temperature + moisture maps | Height, latitude | Biome map |
| 5. Detail placement | Rock, vegetation, water | Biome map, slope data | Placement maps |
| 6. Mesh generation | Marching cubes or heightmap mesh | Final height data | Renderable mesh |

### Erosion Parameters

| Type | Effect | Iterations | Speed |
|------|--------|-----------|-------|
| Hydraulic | Carves rivers, valleys, sediment deposit | 50,000–500,000 droplets | Slow but realistic |
| Thermal | Smooths steep slopes, creates talus | 50–200 passes | Fast |
| Wind | Creates dunes, exposes rock faces | 100–1,000 passes | Medium |

## Wave Function Collapse (WFC)

### When to Use WFC
- Tiled dungeon/level generation with adjacency rules
- City block layouts that need to "make sense"
- Texture generation from example images
- Any grid-based content with local constraints

### WFC Process
1. **Define tile set** — create tiles with labeled edges/sockets
2. **Define adjacency rules** — which tiles can be neighbors (auto-extract from example or manual)
3. **Initialize grid** — all cells start with all tiles as possibilities
4. **Collapse lowest entropy cell** — pick the cell with fewest remaining options, assign a tile
5. **Propagate constraints** — remove incompatible tiles from neighboring cells
6. **Repeat** until all cells collapsed or contradiction found
7. **Handle contradictions** — backtrack or restart with different seed

### WFC Tips
- Start with a small tile set (8–16 tiles) and expand
- Add frequency hints — common tiles should appear more often
- Use backtracking WFC for guaranteed completion (slower)
- Pre-seed important locations (entrances, exits, boss rooms) before running WFC

## L-Systems for Vegetation and Architecture

### Basic L-System Components

| Symbol | Meaning | Example |
|--------|---------|---------|
| F | Draw forward | Trunk, branch segment |
| + | Rotate right | Branch angle |
| - | Rotate left | Branch angle |
| [ | Push state (save position) | Start sub-branch |
| ] | Pop state (restore position) | End sub-branch |
| X, A, B | Variables (replaced by rules) | Growth patterns |

### Example: Simple Tree
- **Axiom:** `X`
- **Rules:** `X → F[+X][-X]FX`, `F → FF`
- **Iterations:** 4–6
- **Angle:** 25°–35°
- Result: increasingly complex branching tree

## Performance Optimization

| Technique | Application | Benefit |
|-----------|-------------|---------|
| Chunk-based generation | Terrain, open worlds | Only generate visible areas |
| LOD for procedural content | Distant terrain, vegetation | Reduce detail at distance |
| GPU compute shaders | Noise generation, erosion | 10–100× faster than CPU |
| Caching/memoization | Repeated noise lookups | Avoid redundant calculations |
| Async generation | Level loading, streaming | No frame hitches |
| Seed-based determinism | Multiplayer, save/load | Same seed = same result |

## Best Practices

- **Always use seeds** — deterministic generation enables reproducibility, debugging, and multiplayer sync
- **Layer multiple systems** — combine noise + rules + simulation for realistic results
- **Hand-author the rules, not the content** — design systems that generate good content, not individual pieces
- **Test with many seeds** — ensure quality across random variations, not just "the good seed"
- **Provide artist override** — let designers paint masks, set spawn points, or constrain generation
- **Profile generation time** — players shouldn't wait; generate in background or at load time

## Using the Reference Files

**`/references/terrain-generation.md`** — Read when building terrain systems. Covers heightmap generation, erosion simulation, biome assignment, and chunk-based streaming.

**`/references/vegetation-systems.md`** — Read when placing vegetation procedurally. Covers Poisson disk distribution, L-systems for trees, biome-aware placement, and LOD strategies.

**`/references/procedural-textures.md`** — Read when generating textures procedurally. Covers noise-based materials, Substance Designer graphs, and GPU texture generation.

**`/references/architectural-generation.md`** — Read when generating buildings, dungeons, or levels. Covers BSP trees, WFC implementation, shape grammars, and city generation.
