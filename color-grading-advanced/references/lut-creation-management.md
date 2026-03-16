# LUT Creation and Management

Comprehensive guide to creating, managing, and applying LUTs in professional workflows.

---

## Understanding LUTs

### What is a LUT?

**Lookup Table Definition**
- Mathematical transformation of color values
- Maps input colors to output colors
- Applies consistent color transformation
- Can be 1D (luminance only) or 3D (color and luminance)

**LUT Types**
- **1D LUT**: Adjusts luminance values only, no color transformation
- **3D LUT**: Transforms both color and luminance, full color grading capability
- **3D LUTs** are standard for color grading workflows

### LUT Formats

**Common Formats**
- **.cube**: Most universal, supported by virtually all software
- **.3dl**: Autodesk/Lustre format, widely supported
- **.mga**: Pandora format
- **.csp**: Rising Sun Research ColorSpace format

**LUT Sizes**
- **17x17x17**: Small, fast, less precise
- **33x33x33**: Standard, good balance of speed and quality
- **65x65x65**: Large, slower, maximum precision
- Larger LUTs provide smoother gradations

## Technical vs. Creative LUTs

### Technical LUTs

**Purpose**
- Color space conversions
- Camera LOG to Rec.709 conversion
- Display calibration
- Gamut mapping

**Common Technical LUTs**
- Sony S-Log3 to Rec.709
- ARRI LogC to Rec.709
- RED Log3G10 to Rec.709
- Rec.2020 to Rec.709

**Application**
- Apply early in node tree
- Before any color corrections
- Converts footage to viewable color space
- Essential for LOG workflows

### Creative LUTs

**Purpose**
- Apply stylistic looks
- Establish visual aesthetic
- Provide starting point for grading
- Ensure consistency across projects

**Creative LUT Categories**
- Film emulation (Kodak, Fuji stocks)
- Cinematic looks (teal and orange, bleach bypass)
- Vintage styles (70s, 80s, 90s aesthetics)
- Genre-specific (horror, romance, sci-fi)

**Application**
- Apply after technical corrections
- Before or during creative grading
- Adjust intensity as needed
- Grade on top of LUT for customization

## Creating Custom LUTs

### LUT Creation Workflow in DaVinci Resolve

**Method 1: From Single Clip**
1. Grade clip to desired look
2. Right-click on clip thumbnail
3. Select "Generate 3D LUT (33 Point Cube)"
4. Choose location and name
5. LUT saved for use in other projects

**Method 2: From Node**
1. Create grade in specific node
2. Right-click on node
3. Select "Generate 3D LUT"
4. Choose size (17, 33, or 65 point)
5. Save LUT file

**Method 3: Timeline-Level LUT**
1. Apply color management settings
2. Export timeline LUT
3. Includes all color space transforms
4. Useful for consistent delivery

### LUT Creation Best Practices

**Start with Neutral Footage**
- Use properly exposed, color-balanced footage
- Avoid extreme corrections in LUT
- LUT should enhance, not fix problems

**Avoid Extreme Adjustments**
- Subtle adjustments translate better across footage
- Extreme corrections may not work on all clips
- Test LUT on variety of footage

**Consider Skin Tones**
- Ensure LUT doesn't negatively affect skin tones
- Test on various skin tones
- Adjust if skin tones shift unnaturally

**Test Across Tonal Range**
- Verify LUT works in shadows, midtones, highlights
- Check for clipping or crushing
- Ensure smooth gradations

### Creating LUTs from Reference Images

**Match Grading Workflow**
1. Import reference image as still
2. Import similar footage to grade
3. Grade footage to match reference
4. Generate LUT from graded footage
5. Test LUT on other clips

**Film Emulation LUTs**
1. Analyze film stock characteristics
2. Recreate color response curves
3. Add appropriate grain and halation
4. Generate LUT from emulation grade
5. Refine based on testing

## LUT Application Techniques

### Applying LUTs in DaVinci Resolve

**Method 1: LUT Browser**
1. Open LUT browser in Color page
2. Navigate to LUT location
3. Drag LUT onto clip or node
4. LUT applied instantly

**Method 2: Right-Click Menu**
1. Right-click on clip or node
2. Select "3D LUT" > "Browse"
3. Navigate to LUT file
4. Select and apply

**Method 3: Color Management**
1. Project Settings > Color Management
2. Set Input LUT for clips
3. Set Timeline LUT for viewing
4. Set Output LUT for delivery

### Adjusting LUT Intensity

**Key Tab Method**
1. Apply LUT to node
2. Open Key tab
3. Adjust Gain slider (default 1.0)
4. Reduce for subtle effect (e.g., 0.5 = 50% intensity)
5. Increase for stronger effect (e.g., 1.5 = 150% intensity)

**Layer Node Method**
1. Apply LUT to layer node
2. Adjust layer node opacity
3. Blend LUT with original image
4. More intuitive control

**Parallel Node Method**
1. Create parallel node
2. Apply LUT to one branch
3. Leave other branch ungraded
4. Adjust mix between branches

### LUT Stacking

**Combining Multiple LUTs**
1. Apply technical LUT first (LOG conversion)
2. Apply creative LUT second (look)
3. Apply output LUT last (delivery format)
4. Each LUT serves specific purpose

**Stacking Considerations**
- Order matters significantly
- Test combinations thoroughly
- Avoid excessive stacking (quality degradation)
- Document LUT chain for consistency

## LUT Management and Organization

### Folder Structure

**Recommended Organization**
```
LUTs/
├── Technical/
│   ├── Camera_Conversions/
│   │   ├── Sony/
│   │   ├── ARRI/
│   │   └── RED/
│   └── Color_Space_Transforms/
├── Creative/
│   ├── Film_Emulation/
│   ├── Cinematic/
│   ├── Vintage/
│   └── Genre_Specific/
├── Custom/
│   ├── Project_Specific/
│   └── Signature_Looks/
└── Output/
    ├── Broadcast/
    ├── Cinema/
    └── Web/
```

### Naming Conventions

**Descriptive Names**
- Include LUT type (Technical, Creative)
- Include purpose or look name
- Include size if relevant (33pt, 65pt)
- Include version number for iterations

**Examples**
- `Tech_SLog3_to_Rec709_33pt.cube`
- `Creative_TealOrange_Cinematic_v2.cube`
- `Custom_ProjectName_HeroLook_65pt.cube`
- `Output_Rec709_Broadcast_Safe.cube`

### LUT Libraries

**Building Personal Library**
- Collect LUTs from various sources
- Create custom LUTs for signature looks
- Organize by category and purpose
- Regularly review and cull unused LUTs

**Commercial LUT Packs**
- Film emulation packs (FilmConvert, Dehancer)
- Cinematic look packs (various vendors)
- Genre-specific collections
- Evaluate quality before purchasing

**Free LUT Resources**
- Camera manufacturer LUTs (Sony, ARRI, RED)
- Community-created LUTs
- Tutorial-included LUTs
- Test thoroughly before use

## LUT Limitations and Considerations

### What LUTs Can't Do

**Limitations**
- Can't recover clipped highlights or crushed blacks
- Can't fix poorly exposed footage
- Can't correct severe color casts perfectly
- Can't replace proper color correction

**LUTs as Starting Points**
- Use LUTs to establish look direction
- Grade on top of LUT for refinement
- Adjust LUT intensity for flexibility
- Don't rely solely on LUTs for final grade

### LUT Quality Issues

**Banding and Posterization**
- Caused by aggressive LUT transformations
- More common with smaller LUT sizes (17pt)
- Use larger LUTs (33pt or 65pt) for smoother results
- Add subtle grain to mask banding

**Color Shifts**
- LUT may shift colors unexpectedly
- Test LUT on various footage types
- Adjust or avoid LUT if shifts are problematic
- Create custom LUT if needed

**Skin Tone Issues**
- Some LUTs negatively affect skin tones
- Always check skin tones after applying LUT
- Use secondary correction to fix if needed
- Choose LUTs that preserve skin tones

## Advanced LUT Techniques

### Conditional LUT Application

**Qualifier-Based LUT**
1. Create node with qualifier
2. Select specific color range or luminance
3. Apply LUT to qualified area only
4. Blend for natural integration

**Window-Based LUT**
1. Create node with power window
2. Draw window around target area
3. Apply LUT inside or outside window
4. Soften edges for seamless blend

### LUT Blending Modes

**Using Layer Nodes**
1. Apply LUT to layer node
2. Change blend mode (Overlay, Multiply, Screen, etc.)
3. Adjust opacity for intensity
4. Experiment with different modes for unique looks

**Blend Mode Applications**
- **Overlay**: Enhances contrast while preserving color
- **Multiply**: Darkens image, intensifies colors
- **Screen**: Lightens image, reduces saturation
- **Color**: Applies LUT color while preserving luminance

### Creating LUT Variations

**Intensity Variations**
1. Start with base LUT
2. Create versions at different intensities (25%, 50%, 75%, 100%)
3. Save each as separate LUT
4. Provides quick intensity options

**Tonal Variations**
1. Apply base LUT
2. Create variations for different tonal ranges
3. One for bright scenes, one for dark scenes
4. Ensures consistent look across varying exposures

## LUT Workflow Integration

### On-Set LUT Application

**Monitoring LUTs**
- Apply LUT to on-set monitors
- Shows approximate final look during shooting
- Helps director and DP visualize result
- Does not affect recorded footage

**LUT Boxes**
- Hardware devices for real-time LUT application
- Teradek, SmallHD, Atomos devices
- Load LUTs for on-set monitoring
- Essential for LOG shooting

### Editorial LUT Workflow

**Proxy LUTs**
- Apply LUT to proxies for editing
- Editor works with approximate final look
- Simplifies editorial color decisions
- LUT removed before final color grading

**Offline to Online**
- Editor applies temporary LUT
- Colorist receives original footage
- Colorist creates final grade
- Final grade replaces editorial LUT

### Delivery LUTs

**Output LUTs**
- Convert from grading color space to delivery space
- Rec.2020 to Rec.709 for SDR delivery
- HDR to SDR conversion
- Ensures proper color space for distribution

**Platform-Specific LUTs**
- Create LUTs for specific platforms (Netflix, Amazon, etc.)
- Meet technical requirements
- Ensure consistent appearance across platforms
- Test on target platform before delivery