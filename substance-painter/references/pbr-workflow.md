# PBR Workflow in Substance Painter

Comprehensive guide to physically-based rendering workflows and best practices in Substance Painter.

## PBR Theory

### Energy Conservation

**Principle**:
- Light reflected + absorbed = incident light
- No surface reflects more light than it receives
- Ensures physical accuracy
- Consistent across lighting conditions

**Implementation**:
- Roughness controls reflection blur
- Metallic determines reflection behavior
- Base color within valid ranges
- Fresnel effect at grazing angles

### Metallic/Roughness Workflow

**Base Color**:
- Non-metals: Diffuse color (30-240 sRGB)
- Metals: Reflection tint (180-255 sRGB)
- No lighting information
- Pure colors for non-metals
- Avoid very dark or bright values

**Metallic Map**:
- Binary: 0 (non-metal) or 1 (metal)
- No in-between values
- White = metal
- Black = non-metal
- Determines reflection behavior

**Roughness Map**:
- 0 = perfectly smooth/shiny
- 1 = completely rough/matte
- Controls microfacet distribution
- Affects reflection blur
- Most surfaces: 0.2-0.8 range

### Material Types

**Dielectrics (Non-Metals)**:
- Diffuse reflection
- Low specular reflection (4%)
- Base color determines appearance
- Examples: wood, plastic, fabric, skin

**Metals**:
- No diffuse reflection
- High specular reflection (60-100%)
- Colored reflections
- Examples: gold, silver, copper, iron

**Common Materials**:
- **Plastic**: Low roughness, non-metal
- **Wood**: Medium roughness, non-metal
- **Rubber**: High roughness, non-metal
- **Polished Metal**: Low roughness, metal
- **Rusty Metal**: High roughness, metal

## Texturing Workflow

### Preparation

**Model Requirements**:
- Clean topology
- Proper UV unwrapping
- No overlapping UVs (unless mirrored)
- Consistent texel density
- Named texture sets

**Baking Setup**:
- High-poly reference model (optional)
- Low-poly game model
- Matching position and scale
- Cage for projection
- Appropriate padding

### Baking Maps

**Essential Maps**:
- **Normal**: High to low-poly detail
- **Ambient Occlusion**: Cavity shading
- **Curvature**: Edge detection
- **World Space Normal**: Directional info
- **Thickness**: Subsurface scattering

**Baking Settings**:
- Output size: Match final texture resolution
- Samples: Higher for quality (4x4 or 8x8)
- Dilation: Prevent seams (16-32 pixels)
- Match: By mesh name or always
- Cage: Adjust for complex shapes

**Troubleshooting**:
- **Seams in normal map**: Increase dilation
- **Missing details**: Adjust cage
- **Incorrect projection**: Check mesh names
- **Artifacts**: Increase samples

### Base Material

**Starting Point**:
- Add fill layer
- Set base color
- Define metallic value
- Set initial roughness
- Establish foundation

**Material Presets**:
- Use material library
- Drag and drop
- Adjust parameters
- Build from existing
- Save custom presets

### Layering Strategy

**Bottom to Top**:
1. Base material
2. Large wear and damage
3. Medium details
4. Fine details and dirt
5. Final polish and adjustments

**Layer Organization**:
- Use folders for related layers
- Name layers descriptively
- Color-code layer types
- Lock finalized layers
- Delete unused layers

## Smart Materials

### Understanding Smart Materials

**Components**:
- Multiple fill and paint layers
- Procedural masks (generators)
- Effects and filters
- Organized in folders
- Customizable parameters

**How They Work**:
- Analyze baked maps
- Apply effects based on geometry
- Curvature for edge wear
- AO for cavity dirt
- Height for surface variation

### Customizing Smart Materials

**Parameter Adjustment**:
- Base colors
- Wear amount
- Dirt intensity
- Roughness variation
- Height strength

**Modifying Generators**:
- Adjust generator settings
- Change blend modes
- Add additional generators
- Combine multiple effects
- Fine-tune masks

**Creating Custom Smart Materials**:
1. Build layer stack
2. Add generators to masks
3. Organize in folder
4. Right-click > Create Smart Material
5. Name and save
6. Reuse across projects

## Advanced Techniques

### Anchor Points

**Purpose**:
- Reference layer data
- Create complex interactions
- Non-destructive workflow
- Efficient masking

**Workflow**:
1. Create layer with desired effect
2. Right-click > Create Anchor Point
3. In another layer's mask, add Fill
4. Set Fill to reference Anchor Point
5. Adjust blend mode and opacity

**Use Cases**:
- Dirt accumulation in worn areas
- Rust where paint is chipped
- Grime in cavities
- Layered weathering effects

### Generators

**Common Generators**:
- **Dirt**: Cavity accumulation
- **Rust**: Edge and cavity corrosion
- **Dust**: Surface accumulation
- **Grunge**: General wear
- **Scratches**: Surface damage

**Generator Settings**:
- Global balance: Overall intensity
- Contrast: Sharpness of effect
- Levels: Fine-tune distribution
- Grunge map: Variation pattern
- Curvature/AO influence

### Masks and Filters

**Mask Types**:
- **Paint**: Hand-painted masks
- **Fill**: Solid or procedural
- **Generator**: Automatic based on maps
- **Color Selection**: From painted layer

**Filters**:
- **Blur**: Soften masks
- **Sharpen**: Enhance edges
- **Levels**: Adjust contrast
- **HSL Perceptive**: Color adjustments
- **Gradient**: Directional effects

## Material Libraries

### Organizing Materials

**Categories**:
- Base materials (metal, plastic, wood)
- Smart materials (weathered, damaged)
- Procedural textures
- Custom creations
- Project-specific

**Naming Conventions**:
- Descriptive names
- Category prefixes
- Version numbers
- Author tags
- Searchable keywords

### Sharing Materials

**Export**:
- Right-click material > Export
- .spsm file format
- Include dependencies
- Document usage
- Share with team

**Import**:
- File > Import Resources
- Select .spsm files
- Materials appear in shelf
- Ready to use
- Update if needed

## Export and Integration

### Export Presets

**Game Engines**:
- **Unreal Engine**: BaseColor, Normal, ORM
- **Unity**: Albedo, Normal, Metallic/Smoothness
- **CryEngine**: Diffuse, Normal, Specular
- **Custom**: Define channel packing

**Render Engines**:
- **V-Ray**: Diffuse, Reflect, Glossiness
- **Arnold**: BaseColor, Metallic, Roughness
- **Redshift**: Diffuse, Reflection, Roughness

### Texture Resolution

**Guidelines**:
- **Hero assets**: 4K (4096x4096)
- **Primary assets**: 2K (2048x2048)
- **Secondary assets**: 1K (1024x1024)
- **Background**: 512x512
- Consider texel density

**Format Selection**:
- **PNG**: Lossless, good for most
- **TGA**: Lossless, widely supported
- **JPEG**: Lossy, smaller files
- **EXR**: HDR, film/VFX
- **TIFF**: Lossless, large files

## Best Practices

### Performance

**Optimize Layers**:
- Merge similar layers
- Delete unused layers
- Simplify complex stacks
- Use appropriate resolution
- Bake effects when finalized

**Texture Size**:
- Start with target resolution
- Don't upscale later
- Consider memory budget
- Use texture atlases
- Implement LODs

### Quality Control

**Validation**:
- Check all angles
- Test in target engine
- Verify in different lighting
- Check for seams
- Validate UV layout

**Consistency**:
- Match reference materials
- Maintain style across assets
- Use consistent wear patterns
- Follow art direction
- Document decisions

## Conclusion

Mastering PBR workflows in Substance Painter requires understanding physical principles, efficient layering strategies, and smart use of procedural tools. Practice on diverse materials, study real-world references, and build a library of reusable smart materials for efficient production.
