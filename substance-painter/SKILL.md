---
name: substance-painter
description: "Master PBR texturing in Substance Painter for photorealistic materials. Use for: PBR workflows, smart materials, layer-based texturing, mask painting, baking maps, texture sets, real-time preview, and production-ready asset texturing."
---

# Substance Painter

Master physically-based rendering (PBR) texturing in Substance Painter for creating photorealistic materials for games, film, and real-time applications.

## Overview

Substance Painter is Adobe's industry-standard 3D texturing software that fully supports PBR workflows. It enables artists to paint directly on 3D models with real-time feedback, creating realistic materials that render consistently across different lighting conditions.

## PBR Fundamentals

### Physically Based Rendering

**Core Concept**:
- Simulates real-world light interaction
- Materials behave consistently in all lighting
- Based on physical principles
- Energy conservation
- Predictable results

**Benefits**:
- Realistic material appearance
- Consistent across engines and renderers
- Simplified workflow
- No manual lighting adjustments needed
- Industry standard

### PBR Workflows

**Metallic/Roughness** (Most Common):
- Base Color: Object's inherent color
- Metallic: Metal (white) vs. non-metal (black)
- Roughness: Shiny (black) vs. rough (white)
- Normal: Surface detail
- Height: Depth information

**Specular/Glossiness**:
- Diffuse: Non-metallic color
- Specular: Reflection color and intensity
- Glossiness: Inverse of roughness
- Less common in modern workflows

## Interface and Workspace

### Main Viewport

**3D View**:
- Real-time material preview
- Rotate, pan, zoom model
- Multiple camera angles
- Lighting environments (HDRIs)
- Render modes (PBR, normal, AO)

**Display Settings**:
- Wireframe overlay
- UV layout view
- Texture set selection
- Shader settings
- Post-effects

### Essential Panels

**Texture Set Settings**:
- Manage texture sets
- Set resolution (512-8192)
- Add/remove channels
- Baking configuration

**Layers**:
- Non-destructive layer stack
- Fill, paint, and procedural layers
- Masks and effects
- Blend modes
- Layer organization

**Shelf**:
- Materials library
- Smart Materials
- Brushes and alphas
- Procedural textures
- Custom resources

## Texturing Workflow

### Model Preparation

**Requirements**:
- Clean geometry
- Proper UV unwrapping
- No overlapping UVs (unless intentional)
- Appropriate texel density
- Named materials/texture sets

**Importing Models**:
- File > Import (FBX, OBJ, etc.)
- Auto-unwrap if no UVs
- Set up texture sets
- Configure document resolution
- Choose template (PBR Metallic Roughness)

### Baking Maps

**Purpose**:
- Generate mesh information maps
- Normal, AO, curvature, thickness
- Used by Smart Materials
- Essential for realistic results

**Baking Process**:
1. Texture Set Settings > Bake Mesh Maps
2. Select maps to bake (Normal, AO, Curvature, etc.)
3. Configure settings (samples, dilation)
4. Bake all texture sets
5. Verify results

**Common Baked Maps**:
- **Normal**: High to low-poly detail transfer
- **Ambient Occlusion**: Cavity shading
- **Curvature**: Edge detection
- **World Space Normal**: Directional information
- **Thickness**: Subsurface scattering
- **Position**: Spatial data

### Layer-Based Texturing

**Layer Types**:
- **Fill Layer**: Solid material
- **Paint Layer**: Hand-painted details
- **Procedural Layer**: Generated patterns
- **Folder**: Organize layers

**Layer Properties**:
- Blend mode (Normal, Multiply, Overlay, etc.)
- Opacity
- Material properties (color, roughness, etc.)
- Masks
- Effects

**Masking**:
- Black mask: Hide layer
- White mask: Show layer
- Paint masks manually
- Procedural masks (generators)
- Smart Masks

## Smart Materials

### Understanding Smart Materials

**What Are Smart Materials**:
- Pre-built material systems
- Automatically adapt to geometry
- Use baked maps (curvature, AO)
- Procedural effects
- Customizable parameters

**How They Work**:
- Analyze mesh data
- Apply effects based on geometry
- Dirt in cavities
- Wear on edges
- Rust, scratches, dust
- Layered complexity

### Using Smart Materials

**Application**:
1. Drag Smart Material onto model
2. Material applies with automatic masking
3. Adjust parameters in Properties
4. Customize colors and intensity
5. Add additional layers as needed

**Customization**:
- Modify base colors
- Adjust wear amount
- Change dirt intensity
- Alter procedural patterns
- Save custom variations

## Painting Techniques

### Brush Painting

**Brush Tools**:
- Paint: Standard painting
- Eraser: Remove paint
- Projection: Project images
- Clone: Copy areas
- Smudge: Blend colors

**Brush Settings**:
- Size and hardness
- Flow and opacity
- Spacing
- Angle and rotation
- Pressure sensitivity (tablet)

**Painting Channels**:
- Paint on any channel
- Base Color for color
- Roughness for shine variation
- Height for surface detail
- Normal for directional detail

### Stencils and Projections

**Stencil Mode**:
- Project images onto surface
- Adjust position, scale, rotation
- Paint through stencil
- Use for logos, decals, patterns

**Projection Mode**:
- Project from camera view
- Useful for photo textures
- Adjust projection settings
- Paint to apply

### Procedural Texturing

**Generators**:
- Procedural mask creation
- Based on mesh data
- Dirt, rust, wear patterns
- Customizable parameters
- Non-destructive

**Fill Layers with Generators**:
1. Add Fill Layer
2. Add Black Mask
3. Add Generator to mask
4. Adjust generator settings
5. Material appears where generator is white

## Materials and Channels

### PBR Channels

**Base Color**:
- Inherent object color
- No lighting information
- Diffuse reflection color
- For metals: reflection tint

**Metallic**:
- Binary: metal or non-metal
- White = metal
- Black = non-metal
- Avoid gray values

**Roughness**:
- Surface microsurface detail
- Black = smooth/shiny
- White = rough/matte
- Controls reflection blur

**Normal**:
- Surface detail without geometry
- RGB channels = XYZ directions
- Adds perceived depth
- Baked from high-poly or painted

**Height**:
- Actual depth information
- Converted to Normal on export
- White = raised
- Black = lowered
- Gray = neutral

### Additional Channels

**Ambient Occlusion**:
- Cavity shading
- Usually baked, not painted
- Enhances depth perception

**Emissive**:
- Self-illumination
- Glowing elements
- No lighting needed
- Color and intensity

**Opacity**:
- Transparency
- Alpha channel
- For glass, leaves, etc.

## Advanced Techniques

### Anchor Points

**Purpose**:
- Reference other layers
- Create complex material interactions
- Non-destructive workflow

**Usage**:
1. Right-click layer > Create Anchor Point
2. In another layer's mask, add Fill
3. Set Fill to use Anchor Point
4. Adjust blend and parameters

### Particle Brushes

**Particle Painting**:
- Spray multiple elements
- Rocks, bolts, debris
- Randomization settings
- Scale, rotation, spacing variation

**Applications**:
- Surface details
- Scattered elements
- Organic variation
- Quick detailing

### Custom Materials

**Creating Materials**:
1. Build layer stack
2. Adjust all parameters
3. Right-click folder > Create Smart Material
4. Name and save
5. Reuse across projects

**Sharing Materials**:
- Export as .spsm file
- Share with team
- Import into other projects
- Build material library

## Export and Integration

### Export Settings

**Export Textures**:
- File > Export Textures
- Choose preset (Unreal, Unity, etc.)
- Set resolution
- Select format (PNG, TGA, EXR)
- Configure channels

**Export Presets**:
- Engine-specific configurations
- Correct channel packing
- Naming conventions
- Format settings
- Custom presets possible

### Game Engine Integration

**Unreal Engine**:
- Export with Unreal preset
- Base Color, Normal, ORM (Occlusion/Roughness/Metallic)
- Import textures
- Create material
- Connect texture maps

**Unity**:
- Export with Unity preset
- Albedo, Normal, Metallic/Smoothness
- Import to project
- Assign to material
- Configure shader

## Workflow Optimization

### Performance

**Viewport Optimization**:
- Reduce texture resolution for preview
- Simplify shader settings
- Disable post-effects
- Use lower poly proxy
- Optimize layer count

**Project Organization**:
- Name layers descriptively
- Use folders for organization
- Delete unused layers
- Merge layers when finalized
- Regular project cleanup

### Best Practices

**Texturing Strategy**:
- Start with base materials
- Add large details first
- Progress to fine details
- Use reference images
- Test in target engine

**Quality Control**:
- Check all angles
- Verify in different lighting
- Test in target application
- Check texture resolution
- Validate UV layout

## Conclusion

Substance Painter streamlines PBR texturing with intuitive tools, Smart Materials, and real-time feedback. Master the fundamentals, experiment with techniques, and build a library of custom materials. Practice on diverse assets to develop efficiency and artistic judgment.

## Using the Reference Files

- [Pbr Workflow](./references/pbr-workflow.md): Pbr Workflow
- [Smart Materials](./references/smart-materials.md): Smart Materials
