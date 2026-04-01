---
name: character-modeling-3d
description: "Create professional 3D character models for games, film, and animation. Use for: designing character topology, sculpting organic forms, retopology workflows, UV mapping characters, creating clean edge flow, modeling for animation, optimizing polygon counts, and building production-ready character assets."
---

# Character Modeling 3D

Create professional 3D character models with proper topology, edge flow, and optimization for animation and rendering.

## Overview

This skill covers the complete character modeling pipeline from concept to production-ready asset. Learn topology principles, sculpting techniques, retopology workflows, UV mapping strategies, and optimization methods used in professional game and film production.

## Quick Start: Modeling Approach Selection

| Character Type | Primary Method | Topology Priority | Reference |
|----------------|----------------|-------------------|------------|
| Realistic human | High-poly sculpt → retopo | Animation-friendly quads | `/references/topology-principles.md` |
| Stylized character | Box modeling + subdivision | Clean edge loops | `/references/modeling-workflows.md` |
| Game character (mobile) | Low-poly direct modeling | Triangle budget | `/references/optimization-techniques.md` |
| Film/VFX character | ZBrush sculpt → production mesh | Subdivision-ready | `/references/sculpting-techniques.md` |
| Creature/monster | Organic sculpting + hard surface | Hybrid topology | `/references/advanced-techniques.md` |

## Core Topology Principles

### Edge Flow Fundamentals

1. **Follow muscle structure** — edge loops should follow natural muscle flow and deformation areas
2. **Maintain quad topology** — use quads (four-sided polygons) for areas that deform during animation
3. **Strategic pole placement** — place 5-pole and 3-pole vertices away from deformation zones
4. **Loop termination** — properly terminate edge loops to avoid pinching and artifacts
5. **Density distribution** — add geometry only where detail or deformation requires it

### Critical Edge Loop Locations

- **Face**: Around eyes, mouth, nose, cheeks (follow facial muscles)
- **Body**: Shoulders, elbows, wrists, hips, knees, ankles (joint deformation)
- **Hands**: Knuckles, finger joints, palm creases
- **Torso**: Pectorals, abs, spine (muscle definition and bending)

## Modeling Pipeline Stages

### Stage 1: Concept and Reference

- Gather reference images (front, side, 3/4 views)
- Create or obtain concept art
- Set up reference planes in modeling software
- Establish scale and proportions
- Define polygon budget and technical requirements

### Stage 2: Base Mesh Creation

**Box Modeling Approach:**
- Start with primitive shapes (cube, cylinder, sphere)
- Extrude and shape major forms
- Establish primary proportions
- Create clean, quad-based topology from the start

**Sculpting Approach:**
- Begin with low-poly base mesh or primitive
- Subdivide and sculpt major forms
- Add detail progressively through subdivision levels
- Plan for retopology in later stage

### Stage 3: Refinement and Detail

- Add secondary forms (muscle groups, bone structure)
- Refine proportions and silhouette
- Create proper edge flow for animation
- Add tertiary details (skin folds, wrinkles, pores)
- Maintain clean topology throughout

### Stage 4: Retopology (if sculpting workflow)

- Create production topology over high-poly sculpt
- Follow edge flow principles
- Optimize polygon count for target platform
- Ensure quad topology in deformation areas
- Bake high-poly details to normal maps

### Stage 5: UV Mapping

- Create UV seams along natural boundaries
- Minimize seams in visible areas
- Optimize UV space utilization (texel density)
- Straighten UV shells for easier texturing
- Check for stretching and distortion

### Stage 6: Optimization and Cleanup

- Remove unnecessary geometry
- Merge vertices and clean up topology
- Check for non-manifold geometry
- Validate normals direction
- Prepare for rigging and animation

## Software and Tools

### Primary Modeling Software

| Software | Best For | Strengths |
|----------|----------|------------|
| Blender | General character modeling | Free, complete pipeline, good sculpting |
| Maya | Professional game/film production | Industry standard, excellent topology tools |
| ZBrush | High-detail organic sculpting | Best-in-class sculpting, detail work |
| 3ds Max | Game character modeling | Modifier stack, CAT rigging integration |
| Modo | Hard surface + organic hybrid | Advanced modeling tools, UV workflow |

### Specialized Tools

- **Retopology**: TopoGun, Quad Remesher, Blender's Shrinkwrap + manual retopo
- **Sculpting**: ZBrush, Blender Sculpt Mode, Mudbox
- **UV Mapping**: RizomUV, UVLayout, native tools
- **Baking**: Marmoset Toolbag, Substance Painter, xNormal

## Polygon Budget Guidelines

### Game Characters

| Platform | Triangle Count | Notes |
|----------|----------------|--------|
| Mobile | 5,000-15,000 | Hero characters upper range |
| Console (current-gen) | 30,000-100,000 | AAA game standards |
| PC (high-end) | 50,000-150,000 | With LOD system |
| VR | 20,000-50,000 | Performance critical |

### Film/Animation Characters

- **Base mesh**: 10,000-30,000 polygons
- **Subdivision surface**: 100,000-500,000+ polygons at render time
- **Close-up hero**: 1,000,000+ polygons acceptable

## Common Challenges and Solutions

### Challenge: Pinching at Joints

**Solution**: Add supporting edge loops near joints, ensure proper edge flow direction, use 5-6 edge loops around cylindrical joints like elbows and knees.

### Challenge: Topology Poles in Deformation Areas

**Solution**: Relocate poles to non-deforming regions, use edge loop redirection techniques, plan pole placement during base mesh stage.

### Challenge: Maintaining Detail While Optimizing

**Solution**: Use normal maps to bake high-poly details, implement LOD (Level of Detail) system, prioritize geometry in visible/important areas.

### Challenge: UV Seam Visibility

**Solution**: Place seams along natural boundaries (clothing edges, hair lines), hide seams in shadowed areas, use seam blending in texturing.

### Challenge: Asymmetry in Symmetrical Characters

**Solution**: Use symmetry modifiers during modeling, mirror geometry before finalizing, add asymmetry only in final detail pass.

## Best Practices

### Topology Best Practices

1. **Start simple, add complexity gradually** — begin with low-poly base, subdivide as needed
2. **Think about animation early** — model with deformation in mind from the start
3. **Use reference constantly** — check proportions and anatomy throughout process
4. **Save progression versions** — keep milestone saves for rollback options
5. **Test deformation early** — create simple rig to test joint bending

### Workflow Efficiency

1. **Use modifiers non-destructively** — mirror, subdivision, shrinkwrap modifiers
2. **Leverage symmetry** — model one half, mirror for efficiency
3. **Create reusable base meshes** — build library of starting points
4. **Hotkey mastery** — learn software shortcuts for speed
5. **Batch similar tasks** — do all UV mapping together, all optimization together

### Quality Control Checklist

- [ ] All faces are quads in deformation areas
- [ ] No overlapping vertices or faces
- [ ] Normals facing correct direction
- [ ] No non-manifold geometry
- [ ] Edge flow follows muscle structure
- [ ] Poles placed strategically away from joints
- [ ] UV seams minimized and well-placed
- [ ] Polygon count within budget
- [ ] Model scales correctly in scene
- [ ] Clean naming conventions used

## Industry Standards

### Naming Conventions

- **Mesh objects**: `CHR_CharacterName_BodyPart` (e.g., `CHR_Hero_Body`, `CHR_Hero_Head`)
- **UV sets**: `map1`, `UVChannel_1` or descriptive names
- **Material IDs**: Consistent naming across pipeline

### File Organization

```
project/
├── models/
│   ├── highpoly/          # Sculpted high-res versions
│   ├── lowpoly/           # Production meshes
│   └── retopo/            # Retopology work files
├── references/            # Reference images and concept art
├── uvs/                   # UV layout exports
└── exports/               # Final FBX/OBJ exports
```

### Export Settings

**For Game Engines (FBX):**
- Triangulate on export (or keep quads if engine supports)
- Include normals and tangents
- Embed textures or use relative paths
- Scale: Check engine requirements (often 1 unit = 1 meter)

**For Rendering (OBJ/Alembic):**
- Preserve subdivision levels if applicable
- Include UV coordinates
- Export normals
- Use appropriate scale

## Performance Optimization

### Geometry Optimization

1. **Remove hidden faces** — delete geometry inside clothing or not visible
2. **Optimize edge loops** — remove loops that don't contribute to silhouette or deformation
3. **Use LOD system** — create multiple detail levels (LOD0, LOD1, LOD2)
4. **Merge objects strategically** — balance between draw calls and flexibility

### LOD (Level of Detail) Strategy

| LOD Level | Distance | Polygon Reduction | Notes |
|-----------|----------|-------------------|--------|
| LOD0 | 0-5m | 100% (full detail) | Hero/close-up view |
| LOD1 | 5-15m | 50-70% | Medium distance |
| LOD2 | 15-30m | 30-50% | Far view |
| LOD3 | 30m+ | 10-30% | Very far/background |

## Advanced Techniques

### Multi-Resolution Modeling

- Work at multiple subdivision levels simultaneously
- Sculpt details at high levels
- Adjust proportions at low levels
- Propagate changes through subdivision stack

### Modular Character Systems

- Create interchangeable parts (heads, torsos, limbs)
- Standardize connection points and topology
- Build character variations from modules
- Optimize for customization systems

### Blend Shape Preparation

- Create neutral base pose for blend shape targets
- Maintain vertex order and count
- Model extreme expressions for interpolation
- Test blend shape combinations

## Using the Reference Files

### When to Read Each Reference

**`/references/topology-principles.md`** — Read when planning edge flow, troubleshooting deformation issues, or learning proper quad topology for animation-ready characters.

**`/references/modeling-workflows.md`** — Read when choosing between box modeling vs. sculpting approaches, setting up efficient production pipelines, or learning software-specific techniques.

**`/references/sculpting-techniques.md`** — Read when creating high-poly sculpts, adding organic details, or working with ZBrush and digital sculpting tools.

**`/references/optimization-techniques.md`** — Read when reducing polygon counts, creating LOD models, or optimizing characters for real-time rendering and game engines.

**`/references/advanced-techniques.md`** — Read when building modular character systems, creating blend shapes, or implementing advanced production workflows for AAA projects.
