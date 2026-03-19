# Workflow Optimization

Production pipelines, retopology, export workflows, and efficiency strategies for ZBrush.

---

## Production Pipeline Overview

### Typical ZBrush Production Workflow

**Phase 1: Concept and Blocking (DynaMesh)**
- Import reference or start from primitives
- Use DynaMesh for topology-free exploration
- Block out primary forms and proportions
- Iterate rapidly on design
- Output: Low-to-medium resolution concept sculpt

**Phase 2: Refinement (Subdivision)**
- Convert to Polymesh3D or use ZRemesher
- Begin subdivision workflow
- Add secondary forms and details
- Establish surface breakup
- Output: Medium-resolution refined sculpt

**Phase 3: Detailing (High-Resolution)**
- Subdivide to high levels (6-7)
- Add tertiary details and surface texture
- Apply alphas and Surface Noise
- PolyPaint for color information
- Output: High-resolution detailed sculpt

**Phase 4: Retopology (Clean Topology)**
- Create production-ready topology
- ZRemesher, manual retopo, or external tools
- Optimize for animation or real-time rendering
- Output: Low-resolution clean mesh

**Phase 5: Projection and Baking**
- Project high-resolution details onto low-resolution mesh
- Bake normal maps, displacement maps, texture maps
- Prepare for export to game engines or rendering software
- Output: Game-ready or render-ready asset

**Phase 6: Export**
- Export geometry (OBJ, FBX, etc.)
- Export texture maps (diffuse, normal, displacement)
- Import to target application (Maya, Blender, Unreal, Unity)
- Output: Final production asset

---

## Retopology Workflows

### When Retopology is Needed

Retopology creates clean, animation-ready topology from high-resolution sculpts.

**Required for:**
- Animation (rigging and deformation)
- Game engines (performance optimization)
- Subdivision surface modeling
- Clean edge flow
- Specific polygon budgets

**Not required for:**
- 3D printing (high-resolution mesh is fine)
- Static renders (if performance allows)
- Concept art and illustration

### ZRemesher: Automatic Retopology

ZRemesher creates clean topology automatically with minimal user input.

**Basic ZRemesher Workflow:**

1. **Prepare High-Resolution Sculpt:**
   - Complete all sculpting and detailing
   - Organize with polygroups if needed
   - Ensure clean, closed geometry

2. **Access ZRemesher:**
   - Navigate to Geometry > ZRemesher

3. **Set Target Polygon Count:**
   - Adjust "Target Polygons Count" slider
   - Or enable "Use Polygon Count" and set specific number
   - Typical ranges:
     - Game character: 10,000-30,000
     - Film character: 30,000-100,000
     - Props: 5,000-20,000

4. **Configure Options:**
   - **KeepGroups:** Maintains polygroup boundaries (useful for UV seams)
   - **Adaptive Size:** Varies polygon density based on detail
   - **Use Creases:** Respects edge creases
   - **Detect Edges:** Preserves hard edges

5. **Execute ZRemesher:**
   - Click "ZRemesher" button
   - Wait for processing (can take several minutes)
   - Result: New clean topology

6. **Project Details:**
   - Tool > SubTool > Project All
   - Projects high-resolution details onto new topology
   - Adjust Distance slider if needed
   - Result: Clean topology with projected details

**ZRemesher Advanced Options:**

**Curve-Based Control:**
- Draw curves on model (ZRemesher > Enable Curve Mode)
- Curves guide edge flow
- Useful for specific topology requirements (face loops, etc.)
- Red curves = edge loops, Blue curves = polygon flow

**Adaptive Density:**
- Automatically varies polygon density
- More polygons in detailed areas
- Fewer polygons in flat areas
- Efficient polygon distribution

**Symmetry:**
- Enable symmetry before ZRemeshing
- Ensures symmetric topology
- Critical for character work

### Manual Retopology with ZModeler

Manual retopology provides maximum control but is time-intensive.

**ZModeler Retopology Workflow:**

1. **Prepare:**
   - High-resolution sculpt as reference
   - Create new SubTool (plane or sphere)
   - Enable transparency on high-res sculpt (Display Properties > Transparency)
   - Position low-res SubTool inside high-res

2. **Build Topology:**
   - Activate ZModeler brush (B > Z > M)
   - Use Extrude, Bridge, Insert operations
   - Build quad-based topology
   - Follow anatomical edge flow
   - Maintain good polygon distribution

3. **Refine:**
   - Adjust vertex positions to match high-res surface
   - Ensure even polygon distribution
   - Check for non-quads (triangles, n-gons)
   - Maintain clean edge loops

4. **Project Details:**
   - Tool > SubTool > Project All
   - Projects high-res details onto manual retopo
   - Result: Clean manual topology with details

**Manual Retopology Tips:**
- Start with major edge loops (eyes, mouth, limbs)
- Build outward from these loops
- Maintain quad topology (four-sided polygons)
- Follow muscle flow for organic models
- Use symmetry for efficiency

### External Retopology Tools

Specialized retopology tools offer advanced features.

**Popular Tools:**
- **Topogun:** Dedicated retopology software
- **Maya Quad Draw:** Built into Maya
- **Blender:** Free retopology tools
- **3D-Coat:** Retopology and texturing

**External Retopo Workflow:**
1. Export high-resolution sculpt from ZBrush (OBJ format)
2. Import to retopology tool
3. Create clean topology
4. Export clean mesh
5. Import back to ZBrush
6. Project details from high-res sculpt
7. Continue with texturing and export

---

## Map Baking and Projection

### Normal Map Baking

Normal maps store high-resolution surface detail for use on low-resolution meshes.

**Creating Normal Maps in ZBrush:**

1. **Prepare Models:**
   - High-resolution sculpt (source)
   - Low-resolution clean topology (target)
   - Both models in same ZTool as SubTools

2. **Configure Normal Map:**
   - Select low-resolution SubTool
   - Navigate to Tool > Normal Map
   - Click "Create NormalMap"

3. **Settings:**
   - **SizeMap:** Texture resolution (2048, 4096, 8192)
   - **SubDivisions:** Smoothing quality
   - **Tangent/Object Space:** Tangent for game engines, Object for rendering

4. **Bake:**
   - Click "Create NormalMap"
   - Wait for processing
   - Normal map appears in Texture palette

5. **Export:**
   - Texture palette > Export
   - Save as PNG or TIFF
   - Import to game engine or renderer

**Normal Map Tips:**
- Ensure low-res mesh closely matches high-res silhouette
- Adjust projection distance if artifacts appear
- Use cage for complex projections (external tools)
- Test in target application (game engine, renderer)

### Displacement Map Baking

Displacement maps store actual geometric height information.

**Creating Displacement Maps:**

1. **Prepare:**
   - High-resolution sculpt
   - Low-resolution base mesh with UVs

2. **Configure Displacement:**
   - Select low-resolution SubTool
   - Tool > Displacement > Create DispMap

3. **Settings:**
   - **DpSubPix:** Displacement resolution (higher = more detail)
   - **SmoothUV:** Smooths UV seams
   - **Adaptive:** Varies resolution based on detail

4. **Bake:**
   - Click "Create DispMap"
   - Wait for processing (can be lengthy)
   - Displacement map appears in Alpha palette

5. **Export:**
   - Alpha palette > Export
   - Save as 16-bit or 32-bit TIFF for maximum precision
   - Import to renderer (Arnold, V-Ray, Redshift, etc.)

**Displacement vs. Normal Maps:**
- **Normal Maps:** Fake surface detail, no geometry change, faster
- **Displacement Maps:** Actual geometry displacement, true detail, slower
- Use normal maps for real-time (games)
- Use displacement maps for offline rendering (film, high-quality renders)

### Multi-Map Export

Export multiple map types simultaneously for complete asset preparation.

**Common Map Types:**
- **Diffuse/Albedo:** Base color (from PolyPaint)
- **Normal:** Surface detail
- **Displacement:** Geometric detail
- **Ambient Occlusion:** Cavity shading
- **Roughness:** Surface roughness (can derive from cavity)
- **Metallic:** Metallic areas (paint in PolyPaint)

**Multi-Map Workflow:**
1. Complete high-resolution sculpt with PolyPaint
2. Create clean low-resolution topology with UVs
3. Project PolyPaint and geometry to low-res
4. Bake diffuse map (Texture Map > New From Polypaint)
5. Bake normal map (Normal Map > Create NormalMap)
6. Bake displacement map (Displacement > Create DispMap)
7. Create AO map (Mask By Cavity > Convert to PolyPaint > Export)
8. Export all maps at consistent resolution
9. Import to target application

---

## Export Workflows

### Geometry Export Formats

**OBJ (.obj):**
- Universal format, widely supported
- Exports geometry, UVs, polygroups (as groups)
- No animation or rigging data
- Best for static models
- Export: Tool > Export

**FBX (.fbx):**
- Industry standard for game engines and 3D software
- Supports geometry, UVs, materials, animation (if applicable)
- Better for pipeline integration
- Export: Tool > Export (select FBX format)

**STL (.stl):**
- 3D printing format
- Geometry only, no UVs or color
- Export high-resolution mesh directly
- Export: Tool > Export (select STL format)

**GoZ (ZBrush to other apps):**
- Direct transfer to Maya, Blender, Cinema 4D, etc.
- Maintains SubTools, polygroups, UVs
- Bidirectional workflow
- Access: Tool > GoZ button (configure in Preferences > GoZ)

### Export Settings

**Polygon Count:**
- Export at appropriate resolution for target application
- Game engines: 10,000-50,000 polygons (character)
- Rendering: 50,000-500,000+ polygons
- 3D printing: As high as needed for detail

**Scale:**
- ZBrush units may differ from target application
- Check scale after import
- Adjust export scale if needed (Tool > Export > Scale)

**Groups/Polygroups:**
- OBJ exports polygroups as object groups
- Useful for material assignment in other apps
- Organize polygroups before export

**UVs:**
- Ensure UVs are present if textures are needed
- Check UV layout (Tool > UV Map > Morph UV)
- Non-overlapping UVs for unique textures
- Overlapping UVs acceptable for tiling textures

### 3D Printing Export

**Preparing for 3D Printing:**

1. **Optimize Geometry:**
   - Ensure watertight mesh (no holes)
   - Check for non-manifold geometry
   - Use Geometry > Modify Topology > Close Holes if needed

2. **Scale Appropriately:**
   - Set real-world dimensions
   - Tool > Deformation > Size
   - Or scale in slicing software

3. **Export as STL:**
   - Tool > Export
   - Select STL format
   - Choose appropriate resolution

4. **Import to Slicer:**
   - Import STL to slicing software (Cura, PrusaSlicer, etc.)
   - Configure print settings
   - Generate G-code and print

**3D Printing Considerations:**
- High polygon count is acceptable (captures detail)
- Ensure structural integrity (no thin, unsupported areas)
- Consider support structures for overhangs
- Test print small version first

### Game Engine Export

**Preparing for Game Engines (Unity, Unreal):**

1. **Create Low-Resolution Mesh:**
   - Use ZRemesher or manual retopology
   - Target polygon count: 10,000-30,000 (character)
   - Ensure clean quad topology

2. **Bake Maps:**
   - Normal map (surface detail)
   - Diffuse/Albedo map (color)
   - Optional: AO, roughness, metallic

3. **Export Geometry:**
   - Export low-resolution mesh as FBX
   - Ensure UVs are present and non-overlapping

4. **Export Textures:**
   - Export all maps at consistent resolution (2048 or 4096)
   - Use PNG for diffuse, normal
   - Use appropriate formats for other maps

5. **Import to Engine:**
   - Import FBX to Unity/Unreal
   - Import texture maps
   - Assign maps to material
   - Test in engine

**Game Engine Tips:**
- Follow engine-specific guidelines (Unity vs. Unreal)
- Test early and often in target engine
- Optimize polygon count for performance
- Use LODs (Levels of Detail) for distant views

---

## Efficiency Strategies

### Hotkey Customization

Custom hotkeys dramatically improve workflow speed.

**Setting Hotkeys:**
1. Hover over button/function
2. Press Ctrl+Alt+Click
3. Press desired hotkey
4. Hotkey is assigned
5. Save configuration (Preferences > Config > Store Config)

**Essential Hotkeys to Set:**
- Frequently used brushes (Clay Buildup, Move, Standard)
- DynaMesh remesh
- Subdivision up/down (Shift+D, Shift+Ctrl+D are default)
- Polygroup operations
- Masking operations
- SubTool visibility toggles

### Custom UI Layouts

Tailored UI layouts reduce clutter and improve access to tools.

**Creating Custom UI:**
1. Arrange palettes and buttons as desired
2. Remove unused elements
3. Add frequently used tools to top shelf
4. Save layout (Preferences > Config > Store Config)
5. Load layout on startup (Preferences > Config > Load Startup UI)

**UI Tips:**
- Minimize unused palettes
- Create custom menus for specific tasks
- Use Quick Menu (Space bar) for fast access
- Organize by workflow phase (blocking, detailing, export)

### Project Organization

**File Naming Conventions:**
- Descriptive names: "Character_Head_v01.ztl"
- Version numbers: v01, v02, v03
- Date stamps: "Character_2026-03-17.ztl"
- Consistent naming across projects

**Folder Structure:**
```
Project_Name/
├── ZBrush/
│   ├── WIP/
│   │   ├── Character_v01.ztl
│   │   ├── Character_v02.ztl
│   ├── Final/
│   │   ├── Character_Final.ztl
├── Export/
│   ├── Geometry/
│   │   ├── Character_LowRes.fbx
│   │   ├── Character_HighRes.obj
│   ├── Textures/
│   │   ├── Character_Diffuse.png
│   │   ├── Character_Normal.png
├── Reference/
│   ├── Concept_Art.jpg
│   ├── Anatomy_Reference.jpg
```

**Version Control:**
- Save incremental versions frequently
- Keep major milestone versions
- Use descriptive version notes
- Don't overwrite previous versions until certain

### Performance Optimization

**Working Efficiently:**

**Polygon Management:**
- Work at lowest subdivision level possible
- Only subdivide when current level limits detail
- Delete higher levels when not needed (Geometry > Del Higher)
- Use DynaMesh resolution appropriate to detail level

**SubTool Management:**
- Hide SubTools not currently being worked on
- Delete unnecessary SubTools
- Merge SubTools when appropriate (reduces overhead)
- Use folders for complex scenes

**Memory Management:**
- Lower undo history (Preferences > Undo History)
- Clear undo history after major milestones (Edit > Clear All)
- Close other applications while working
- Increase virtual memory (system settings)

**Viewport Performance:**
- Reduce active polygon count
- Disable unnecessary display features (shadows, ambient occlusion)
- Use lower-resolution materials during sculpting
- Enable Fast Shader (Document > Fast Shader)

### Batch Processing

**Processing Multiple SubTools:**

Many operations can be applied to all SubTools simultaneously.

**Examples:**
- Tool > SubTool > Project All (projects details to all SubTools)
- Tool > SubTool > Duplicate All (duplicates all SubTools)
- Tool > Geometry > Divide All (subdivides all SubTools)

**Scripting and Macros:**
- Record repetitive tasks as macros (Macro > Record)
- Play back macros for batch processing
- Use ZScript for advanced automation
- Share macros across projects

---

## Troubleshooting Export Issues

### Geometry Export Problems

**Problem:** Exported model appears broken or incomplete

**Solutions:**
- Ensure all SubTools are visible before export
- Check for non-manifold geometry (holes, overlapping faces)
- Use Geometry > Modify Topology > Close Holes
- Verify export format is correct for target application
- Check scale (may be too large or small)

**Problem:** Polygroups don't export

**Solutions:**
- Use OBJ format (exports polygroups as groups)
- FBX may not preserve polygroups (check target application)
- Manually assign materials based on polygroups before export

### Texture Export Problems

**Problem:** Texture map is blank or incorrect

**Solutions:**
- Verify model has UV coordinates
- Check UV layout (Tool > UV Map > Morph UV)
- Ensure PolyPaint is present on model
- Increase texture resolution
- Check for overlapping UVs (causes texture artifacts)

**Problem:** Normal map appears incorrect in game engine

**Solutions:**
- Verify tangent space vs. object space (use tangent for games)
- Check normal map format (DirectX vs. OpenGL, flip Y channel if needed)
- Ensure low-res mesh closely matches high-res silhouette
- Adjust projection distance in ZBrush
- Test with simple geometry first

### Scale Issues

**Problem:** Model imports at wrong scale

**Solutions:**
- Check export scale settings (Tool > Export > Scale)
- Verify units in target application match ZBrush
- Use Tool > Deformation > Size to set real-world dimensions
- Scale in target application if needed
- Establish consistent scale pipeline for projects

---

## Pipeline Integration

### ZBrush to Maya/Blender

**GoZ Workflow:**
1. Configure GoZ (Preferences > GoZ > select target application)
2. Complete sculpting in ZBrush
3. Click GoZ button (Tool > GoZ)
4. Model automatically imports to Maya/Blender
5. Make changes in Maya/Blender
6. Send back to ZBrush via GoZ
7. Bidirectional workflow

**Manual Export/Import:**
1. Export from ZBrush (OBJ or FBX)
2. Import to Maya/Blender
3. Assign materials and textures
4. Rig, animate, or render

### ZBrush to Substance Painter

**Texturing Workflow:**
1. Complete sculpting and retopology in ZBrush
2. Export low-resolution mesh (FBX with UVs)
3. Export high-resolution mesh (OBJ)
4. Import both to Substance Painter
5. Bake maps in Substance Painter (normal, AO, curvature)
6. Paint textures in Substance Painter
7. Export textures for game engine or renderer

**Alternative: PolyPaint to Substance:**
1. Complete PolyPaint in ZBrush
2. Export diffuse map from ZBrush
3. Import to Substance Painter as base layer
4. Refine and add additional texture layers
5. Export final textures

### ZBrush to Game Engines

**Unity Workflow:**
1. Create low-resolution mesh with ZRemesher
2. Bake normal and diffuse maps
3. Export low-res mesh as FBX
4. Export texture maps (PNG)
5. Import FBX to Unity
6. Import textures
7. Create material and assign textures
8. Test in Unity scene

**Unreal Workflow:**
1. Create low-resolution mesh with ZRemesher
2. Bake normal, diffuse, and optional maps
3. Export low-res mesh as FBX
4. Export texture maps (PNG or TGA)
5. Import FBX to Unreal
6. Import textures
7. Create material in Unreal Material Editor
8. Assign textures to material nodes
9. Apply material to mesh
10. Test in Unreal level

**Game Engine Tips:**
- Follow engine-specific import guidelines
- Test early in target engine
- Optimize for performance (polygon count, texture resolution)
- Use engine-specific features (LODs, material systems)
