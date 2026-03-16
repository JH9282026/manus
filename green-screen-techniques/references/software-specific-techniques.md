# Software-Specific Green Screen Techniques

Detailed workflows for professional keying in industry-standard applications.

---

## Adobe After Effects

### Keylight Workflow

**Initial Setup**
1. Import footage and create composition
2. Apply Effect > Keying > Keylight (1.2)
3. Use Screen Colour eyedropper to select green
4. Click on evenly lit area of green screen

**View Settings**
- **Final Result**: Shows composited output
- **Screen Matte**: Shows black and white matte (ideal for refinement)
- **Intermediate Result**: Shows semi-transparent areas
- **Status**: Color-codes problem areas (black=opaque, white=transparent, gray=partial)

**Screen Matte Refinement**
- Adjust **Clip Black**: Increases matte density in subject
- Adjust **Clip White**: Removes remaining background
- Adjust **Screen Gain**: Controls overall key strength
- Adjust **Screen Balance**: Fine-tunes color selection

**Edge Refinement**
- **Screen Shrink/Grow**: Contracts or expands matte edges
- **Screen Softness**: Feathers edge transition
- **Screen Despot Black/White**: Removes small artifacts

### Advanced Spill Suppressor

**Application**
1. Apply after Keylight in effect stack
2. Select **Color to Suppress**: Green or Blue
3. Adjust **Suppression**: Amount of color removal (start at 100%)
4. Fine-tune **Accuracy**: How precisely color is targeted

**Advanced Controls**
- **Spill Map**: Shows areas being affected
- **Color Accuracy**: Refines which colors are suppressed
- **Suppression Amount**: Intensity of suppression

### Keylight + Cleaner Preset

**Workflow**
1. Apply Keylight for initial key
2. Add Keylight (1.2) again as "Keylight Cleaner"
3. Set View to Screen Matte
4. Adjust to clean up matte without affecting edges
5. Add Advanced Spill Suppressor
6. Add Simple Choker for final edge refinement

### Troubleshooting in After Effects

**Transparent Subject Areas**
- Reduce Screen Gain
- Increase Clip Black
- Check for color matching between subject and screen

**Remaining Background**
- Increase Screen Gain
- Decrease Clip White
- Use garbage matte to eliminate problem areas

**Noisy/Chattering Edges**
- Increase Screen Softness
- Apply slight blur to matte
- Use temporal smoothing (Keyframe Assistant > Smoother)

## Adobe Premiere Pro

### Ultra Key Workflow

**Basic Setup**
1. Apply Effect > Keying > Ultra Key
2. Use eyedropper to select green screen color
3. Set Output to **Alpha Channel** to view matte
4. Refine key using Matte Generation controls

**Matte Generation**
- **Transparency**: Overall key strength
- **Highlight**: Adjusts bright areas of matte
- **Shadow**: Adjusts dark areas of matte
- **Tolerance**: How much color variation is keyed
- **Pedestal**: Raises or lowers overall matte density

**Matte Cleanup**
- **Choke**: Shrinks matte edges
- **Soften**: Feathers matte edges

**Spill Suppression**
- **Desaturate**: Amount of color removal
- **Range**: Which colors are affected
- **Spillover**: Fine-tunes suppression area

**Color Correction**
- Built-in color correction for keyed subject
- Match subject to background plate
- Adjust Saturation, Hue, Luminance

### Premiere Pro Multi-Pass Technique

**Layer-Based Approach**
1. Duplicate clip on multiple video tracks
2. Apply different Ultra Key settings to each
3. Use track mattes to combine results
4. Blend layers for optimal result

**Track Matte Workflow**
1. Create adjustment layer above keyed footage
2. Apply effects to adjustment layer
3. Use keyed footage as track matte
4. Allows non-destructive refinement

## DaVinci Resolve

### Qualifier-Based Keying

**Color Page Workflow**
1. Navigate to Color page
2. Select clip in timeline
3. Open Qualifier palette
4. Use eyedropper to select green
5. Adjust HSL ranges to refine selection

**Qualifier Controls**
- **Hue**: Width of hue selection
- **Saturation**: Range of saturation included
- **Luminance**: Brightness range selected
- **3D Keyer**: Advanced spatial color selection

**Matte Finesse**
- **Blur Radius**: Softens matte edges
- **Clean Black/White**: Removes noise from matte
- **Matte Finesse**: Overall matte refinement
- **In/Out Ratio**: Adjusts matte density

### 3D Keyer (Resolve Studio)

**Advanced Keying**
1. Enable 3D Keyer in Qualifier
2. Select key color with eyedropper
3. Adjust 3D color space selection
4. Refine using X, Y, Z controls

**Advantages**
- More precise color selection
- Better handling of color variations
- Superior edge preservation
- Ideal for challenging keys

### Fusion Page Keying

**Node-Based Workflow**
1. Switch to Fusion page
2. Add Primatte or Delta Keyer node
3. Connect to MediaIn node
4. Adjust keying parameters
5. Add additional nodes for refinement

**Primatte Keyer**
- Automatic background selection
- Interactive spill suppression
- Matte refinement tools
- Professional-grade results

**Delta Keyer**
- Difference-based keying
- Requires clean plate
- Excellent for uneven screens
- Minimal spill issues

### Resolve Spill Suppression

**Color Page Method**
1. Create new node after key node
2. Use Qualifier to select spill color
3. Adjust Hue to shift green to neutral
4. Reduce Saturation in affected areas
5. Use Blur to soften correction

**Fusion Page Method**
1. Add Color Suppressor node after keyer
2. Select suppression color
3. Adjust suppression amount
4. Fine-tune affected range

## Final Cut Pro

### Keyer Effect Workflow

**Basic Setup**
1. Select clip in timeline
2. Apply Effects > Keying > Keyer
3. Use color picker to select green
4. Adjust Strength slider for initial key

**Refine Key**
- **Strength**: Overall key intensity
- **Fill Holes**: Removes small gaps in matte
- **Edge Distance**: Adjusts edge refinement area
- **Spill Level**: Amount of color suppression

**Matte Tools**
- **View Matte**: Shows black and white matte
- **Matte Tools**: Advanced refinement options
- **Light Wrap**: Blends edges with background

### Final Cut Pro X Advanced Techniques

**Layered Keying**
1. Duplicate clip to connected storyline
2. Apply different Keyer settings
3. Use blend modes to combine
4. Mask specific areas for targeted keying

**Motion Tracking Integration**
1. Key footage using Keyer
2. Add graphics or effects
3. Use Motion tracking to follow subject
4. Combine keying with tracking for complex composites

## Nuke (High-End Compositing)

### Primatte Keyer

**Professional Workflow**
1. Add Primatte node to node graph
2. Use Select BG Color to sample green
3. Use Clean BG to refine background removal
4. Use Select FG to protect subject
5. Use Clean FG to refine subject matte

**Spill Suppression**
- Built-in spill suppression in Primatte
- Automatic color matching
- Adjustable suppression amount
- Real-time preview

### IBK Keyer (Image-Based Keyer)

**Advanced Technique**
1. Requires clean plate of empty green screen
2. Add IBKGizmo node
3. Connect footage and clean plate
4. Adjust screen type (green/blue)
5. Refine using IBK controls

**Advantages**
- Handles uneven lighting excellently
- Superior edge preservation
- Minimal spill issues
- Professional-grade results

### Nuke Matte Refinement

**Node-Based Approach**
- **Erode/Dilate**: Shrink or grow matte
- **FilterErode**: Smooth matte edges
- **Despeckle**: Remove small artifacts
- **Inpaint**: Fill holes in matte
- **EdgeBlur**: Soften edges selectively

**Combining Mattes**
- Use Merge nodes with matte operations
- Max, Min, Plus, Multiply for combining
- Layer multiple keys for complex shots
- Use Roto nodes for manual refinement

## Cross-Platform Best Practices

### Consistent Workflow Elements

**Regardless of Software**
1. Start with garbage matte
2. Pull initial key with conservative settings
3. Refine matte using software-specific tools
4. Apply spill suppression
5. Perform edge refinement
6. Color match subject to background
7. Add shadows and light wrap
8. Final quality control review

### Export Considerations

**Preserving Alpha Channels**
- Use QuickTime with Animation codec
- Use PNG sequence for still frames
- Use ProRes 4444 for high-quality video
- Avoid formats that don't support alpha (H.264, MP4)

**Delivery Formats**
- Match background plate specifications
- Maintain color space consistency
- Include alpha channel in deliverables
- Provide both keyed and original footage when possible