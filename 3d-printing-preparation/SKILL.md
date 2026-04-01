---
name: 3d-printing-preparation
description: "Prepare 3D models for successful printing through optimization, slicing configuration, and quality troubleshooting. Use for: optimizing STL files for FDM/SLA/SLS printing, configuring slicer settings (layer height, infill, supports), designing support structures, fixing mesh errors, reducing print failures, troubleshooting quality issues (warping, stringing, layer adhesion), preparing models for different materials (PLA, ABS, PETG, resin), and ensuring dimensional accuracy for functional parts."
---

# 3D Printing Preparation

Optimize 3D models and configure print settings for successful, high-quality 3D prints across FDM, SLA, and SLS technologies.

## Overview

Successful 3D printing requires meticulous model preparation, strategic slicing configuration, and understanding of material behaviors. This skill covers the complete preparation pipeline from model optimization through slicing settings to post-print troubleshooting. Whether printing functional prototypes, artistic models, or production parts, proper preparation minimizes failures, reduces material waste, and ensures dimensional accuracy.

## Quick Start: Print Type Selection

| Print Goal | Technology | Key Preparation | Reference |
|------------|-----------|----------------|----------|
| Functional prototype | FDM | Optimize wall thickness, infill 20-30% | `/references/model-optimization.md` |
| High-detail miniature | SLA/DLP | Minimize supports, hollow large volumes | `/references/support-structures.md` |
| Mechanical part | FDM | Orient for strength, 3+ perimeters | `/references/slicing-settings.md` |
| Large decorative print | FDM | Minimize warping, use brim/raft | `/references/troubleshooting-quality.md` |
| Production part | SLS | Optimize nesting, uniform wall thickness | `/references/model-optimization.md` |
| Organic sculpture | SLA | Tree supports, optimal orientation | `/references/support-structures.md` |

## Model Preparation Fundamentals

### Pre-Flight Checks

Before slicing, verify model integrity:

**Mesh Validation:**
- **Watertight/Manifold:** No holes, gaps, or open edges
- **Correct Normals:** All faces oriented outward
- **No Non-Manifold Geometry:** Each edge shared by exactly two faces
- **No Intersecting Faces:** Clean, non-overlapping geometry

**Repair Tools:**
- **Meshmixer:** Free, powerful mesh repair (Autodesk)
- **Netfabb:** Professional mesh repair and analysis
- **Slicer Built-in:** Most slicers auto-repair minor issues
- **Blender 3D Print Toolbox:** Free add-on for mesh validation

### Critical Dimensions

**Wall Thickness:**
- **FDM Minimum:** 0.8-1.2mm (2-3 nozzle widths for 0.4mm nozzle)
- **SLA/DLP Minimum:** 0.6-1.0mm (thinner possible but fragile)
- **SLS Minimum:** 0.7-1.0mm
- **Functional Parts:** 2-4mm for structural integrity

**Minimum Feature Size:**
- **FDM:** 0.4-0.8mm (nozzle diameter dependent)
- **SLA/DLP:** 0.1-0.3mm (higher resolution)
- **SLS:** 0.3-0.5mm
- **Rule of Thumb:** Features should be 4× layer height minimum

**Clearances and Tolerances:**
- **Tight Fit (press-fit):** 0.0-0.1mm clearance
- **Sliding Fit:** 0.2-0.3mm clearance
- **Loose Fit:** 0.4-0.5mm clearance
- **3D-to-3D Parts:** 0.2mm tolerance
- **3D-to-Real Object:** 0.1mm tolerance

## Orientation Strategy

### Optimal Orientation Principles

**Strength Considerations:**
- Parts are strongest in XY plane (parallel to build plate)
- Weakest along Z-axis (layer lines)
- Orient stress directions parallel to layers
- Avoid loading perpendicular to layer lines

**Surface Quality:**
- Top surfaces: smoothest finish
- Bottom surfaces: build plate texture
- Vertical surfaces: visible layer lines
- Place visible surfaces facing upward when possible

**Support Minimization:**
- Minimize overhangs beyond 45° (FDM) or 30° (SLA)
- Reduce support contact with visible surfaces
- Orient to use self-supporting geometries (arches, chamfers)
- Consider splitting model to reduce supports

**Print Time and Material:**
- Minimize Z-height to reduce print time
- Use largest flat surface as base for stability
- Balance support material vs. print time

### Technology-Specific Orientation

**FDM:**
- Minimize bridging distances
- Avoid thin vertical walls (vibration risk)
- Orient for minimal support material
- Consider layer adhesion for functional parts

**SLA/DLP/LCD:**
- Angle models 15-30° to reduce suction forces
- Minimize cross-sectional area per layer
- Ensure resin drainage paths
- Reduce peel forces on large flat surfaces

**SLS:**
- Maximize nesting efficiency (no supports needed)
- Ensure powder escape routes for hollow parts
- Orient for uniform cooling

## Material Selection

### Common FDM Materials

| Material | Bed Temp | Nozzle Temp | Characteristics | Best For |
|----------|----------|-------------|-----------------|----------|
| PLA | 50-60°C | 190-220°C | Easy, brittle, low warp | Prototypes, decorative |
| PETG | 70-80°C | 230-250°C | Strong, flexible, durable | Functional parts |
| ABS | 95-110°C | 220-250°C | Strong, heat-resistant, warps | Mechanical parts |
| TPU/TPE | 40-60°C | 210-230°C | Flexible, rubber-like | Gaskets, grips |
| Nylon (PA) | 70-90°C | 240-270°C | Very strong, flexible, hygroscopic | High-strength parts |
| ASA | 90-110°C | 240-260°C | UV-resistant, like ABS | Outdoor parts |

### Material-Specific Considerations

**PLA:**
- Minimal warping, no enclosure needed
- Cooling fan at 100% after first layer
- Brittle, not suitable for functional parts under stress
- Biodegradable, low temperature resistance

**ABS:**
- Requires heated bed and enclosure
- Reduce cooling fan (0-30%)
- Prone to warping on large prints
- Acetone vapor smoothing possible

**PETG:**
- Moderate cooling (30-50%)
- Strings easily, tune retraction
- Good layer adhesion
- Chemical resistant

**Flexible (TPU):**
- Slow print speeds (20-30mm/s)
- Minimal retraction (direct drive) or none (Bowden)
- Reduce infill (10-20%) for flexibility
- Difficult to print overhangs

## Using the Reference Files

### When to Read Each Reference

**`/references/model-optimization.md`** — Read when preparing models for printing, fixing mesh errors, optimizing geometry for specific technologies, reducing file size, designing for minimal supports, or ensuring watertight meshes.

**`/references/slicing-settings.md`** — Read when configuring slicer software, adjusting layer height for quality vs. speed, setting infill density and patterns, tuning temperature and speed settings, or optimizing for specific materials and print goals.

**`/references/support-structures.md`** — Read when designing support strategies, configuring automatic support generation, creating custom supports, optimizing support removal, or printing complex geometries with overhangs and bridges.

**`/references/troubleshooting-quality.md`** — Read when diagnosing print failures, fixing warping and adhesion issues, eliminating stringing and oozing, improving surface quality, resolving layer separation, or addressing dimensional inaccuracy.
