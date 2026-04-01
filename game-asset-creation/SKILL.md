---
name: game-asset-creation
description: "Create optimized 3D assets for game engines and real-time applications. Use for: prop modeling, environment assets, modular systems, texture baking, PBR materials, asset optimization, game engine integration, building asset libraries, LOD creation, and UV mapping workflows."
---

# Game Asset Creation

Create optimized 3D assets for game engines and real-time rendering with proper topology, UV mapping, PBR texturing, and engine integration.

## Overview

Game asset creation bridges 3D art and real-time technology. Assets must look great while running efficiently within strict polygon budgets, texture memory limits, and draw call constraints. This skill covers the full production pipeline from blockout to engine-ready asset, including modeling best practices, UV mapping strategies, PBR texturing workflows, and optimization for Unity and Unreal Engine.

## Asset Type Selection Guide

| Asset Type | Poly Budget | Texture Size | LOD Levels | Workflow | Reference |
|------------|-------------|--------------|------------|----------|-----------|
| Hero prop (held item) | 5K–15K tris | 2048×2048 | 3 | High-poly → retopo → bake → texture | `/references/prop-modeling.md` |
| Background prop | 500–3K tris | 512–1024 | 2 | Direct low-poly → texture | `/references/prop-modeling.md` |
| Modular environment | 1K–5K per piece | 1024–2048 atlas | 2–3 | Grid-snapped modules, trim sheets | `/references/environment-assets.md` |
| Vegetation | 500–5K tris | 1024 atlas + alpha | 3+ | Alpha cards, billboard LODs | `/references/environment-assets.md` |
| Character weapon | 3K–10K tris | 2048×2048 | 2 | Sculpt → retopo → bake | `/references/prop-modeling.md` |
| Vehicle | 15K–50K tris | Multiple 2048 | 4 | Modular parts, interior/exterior sets | `/references/prop-modeling.md` |

## Modeling Best Practices

### Topology Guidelines

| Rule | Why | Impact If Ignored |
|------|-----|-------------------|
| All quads for deforming meshes | Clean deformation in animation | Pinching, artifacts on skinned meshes |
| Tris allowed on static props | No deformation = no issues | N/A for static objects |
| Edge loops at bends | Proper silhouette and shading | Faceted, angular appearance |
| Even polygon distribution | Consistent texel density | Blurry/sharp texture inconsistencies |
| No n-gons (5+ sided faces) | Engine triangulation is unpredictable | Shading artifacts, broken normals |
| Welded vertices, no overlapping | Clean lightmaps, proper collision | Light leaks, physics issues |

### Polygon Budget Strategy

- **Mobile:** 300–5K tris per object, 50K–100K per scene
- **Console/PC (current gen):** 5K–100K per object, 1M–5M per scene
- **VR:** 50% of console budgets (must maintain 90fps)
- **LOD0:** Full detail, camera close range
- **LOD1:** 50% of LOD0, medium range
- **LOD2:** 25% of LOD0, far range
- **LOD3/Billboard:** 2D impostor for extreme distance

## UV Mapping Strategy

| Technique | When to Use | Benefit |
|-----------|-------------|---------|
| Unique UVs | Hero assets, baked normals | Maximum texture detail |
| Tiling UVs + trim sheets | Modular environments | Reusable textures, saves memory |
| UV atlasing | Multiple small props | Reduces draw calls via batching |
| UDIM tiles | Film/cinematic assets | Unlimited texture resolution |
| Lightmap UV (UV2) | Static objects with baked lighting | Clean light and shadow bakes |

### Texel Density Rules
- Maintain consistent texel density across all assets in a scene
- Standard: 5.12 px/cm at 2048 textures for console
- Mobile: 2.56 px/cm at 512–1024 textures
- Use checker map in engine to verify consistency
- Hero assets may use 2× density for close-up quality

## PBR Material Workflow

### Texture Map Set (Metallic/Roughness)

| Map | Color Space | Format | Purpose |
|-----|-------------|--------|---------|
| Base Color (Albedo) | sRGB | RGB | Surface color without lighting info |
| Normal Map | Linear | RGB (tangent space) | Surface detail without geometry |
| Roughness | Linear | Grayscale | Microsurface scattering (0=mirror, 1=matte) |
| Metallic | Linear | Grayscale (binary preferred) | Conductor vs. dielectric (0 or 1) |
| Ambient Occlusion | Linear | Grayscale | Contact shadows and cavity darkening |
| Emissive | sRGB | RGB | Self-illuminating surfaces |
| Height/Displacement | Linear | Grayscale | Parallax or tessellation |

### Substance Painter Workflow
1. **Bake mesh maps** from high-poly (normal, AO, curvature, position, thickness)
2. **Block in base materials** using smart materials or fill layers
3. **Add wear and damage** using generators (edge wear, dirt, dust)
4. **Hand-paint details** for hero assets on separate layers
5. **Export textures** using engine-specific preset (Unity or Unreal)

### Common PBR Mistakes to Avoid
- Lighting baked into albedo map (should be flat, even lighting)
- Metallic values between 0.0 and 1.0 (should be binary except for rust/patina)
- Roughness too uniform (real surfaces vary — add micro-variation)
- Normal map intensity too high (causes sparkle artifacts)

## Engine Integration Checklist

| Step | Unity | Unreal Engine |
|------|-------|---------------|
| Format | FBX (Binary) | FBX (Binary) |
| Scale | 1 unit = 1 meter | 1 unit = 1 cm |
| Forward axis | Z-forward | X-forward |
| Import normals | Import from file | Import from file |
| Material setup | Standard/URP/HDRP Lit | M_Standard PBR |
| Collision | Generate or custom mesh | UCX_ prefix for custom |
| LODs | Import LOD group | LOD naming convention |
| Lightmap UV | Auto-generate or UV2 | UV channel 1 |

### Optimization Targets by Platform

| Platform | Draw Calls | Total Tris/Frame | Texture Memory | Target FPS |
|----------|-----------|-------------------|----------------|------------|
| Mobile | <200 | <300K | <256 MB | 30–60 |
| Console | <2,000 | <5M | <2 GB | 30–60 |
| PC (high) | <5,000 | <10M | <4 GB | 60–144 |
| VR | <500 | <1M | <1 GB | 90+ |

## Asset Production Checklist

1. ☐ Reference gathering and concept art review
2. ☐ Blockout model at correct scale
3. ☐ High-poly sculpt or detail pass
4. ☐ Retopology to target poly budget
5. ☐ UV layout with consistent texel density
6. ☐ Mesh map baking (normals, AO, curvature)
7. ☐ PBR texturing in Substance Painter/Designer
8. ☐ LOD creation (manual or automatic)
9. ☐ Export with correct settings for target engine
10. ☐ Engine import and material setup
11. ☐ Collision mesh setup
12. ☐ Lightmap UV verification
13. ☐ Performance profiling in-engine

## Best Practices

- **Model at real-world scale** from the start — retrofitting scale breaks UVs, physics, and lighting
- **Name everything consistently** — `SM_Props_Chair_01`, `T_Chair_01_BC`, `M_Chair_01`
- **Bake detail, don't model it** — if a player won't see the silhouette change, it belongs in a normal map
- **Use trim sheets** for environments — one 2048 texture can cover an entire building
- **Profile early** — import a test asset to engine before finishing the full set
- **Build modular** — snap to grid, share materials, reduce unique assets

## Using the Reference Files

**`/references/prop-modeling.md`** — Read when creating individual props, weapons, or vehicles. Covers high-poly to low-poly workflows, baking, and hero asset techniques.

**`/references/environment-assets.md`** — Read when building modular level art, terrain assets, or vegetation. Covers grid-snapping, trim sheets, and foliage cards.

**`/references/pbr-materials.md`** — Read when texturing assets. Covers Substance Painter/Designer workflows, material layering, and texture optimization.

**`/references/engine-integration.md`** — Read when importing assets into Unity or Unreal. Covers import settings, material setup, LOD configuration, and platform-specific optimization.
