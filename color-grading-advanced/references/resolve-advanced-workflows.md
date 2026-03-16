# DaVinci Resolve Advanced Workflows

Professional techniques for high-end color grading in DaVinci Resolve.

---

## Node Tree Architecture

### Strategic Node Organization

**Foundation Structure**
- **Node 01 - Balance**: Exposure, contrast, basic correction
- **Node 02 - Temperature**: White balance, color temperature
- **Node 03 - Saturation**: Global saturation and vibrance
- **Node 04 - Primaries**: Primary color adjustments
- **Node 05 - Secondaries**: Targeted corrections (skin, sky, etc.)
- **Node 06 - Look**: Creative grading and style
- **Node 07 - Refinement**: Final tweaks and polish
- **Node 08 - Output**: Delivery adjustments, safe levels

### Advanced Node Types

**Layer Nodes**
- Composite-style grading with blend modes
- Stack multiple corrections like Photoshop layers
- Control opacity for subtle blending
- Ideal for complex, layered looks

**Parallel Nodes**
- Process multiple corrections simultaneously
- Blend results using mix controls
- Compare different approaches side-by-side
- Efficient for A/B testing looks

**Outside Nodes**
- Apply corrections before or after entire node tree
- Useful for global adjustments affecting all nodes
- Input color space transforms
- Output delivery adjustments

**Shared Nodes**
- Create node once, use across multiple clips
- Changes propagate to all instances
- Ideal for consistent corrections (logos, graphics)
- Saves time on repetitive adjustments

### Node Workflow Strategies

**Corrective vs. Creative Separation**
1. First half of tree: Technical corrections
2. Second half of tree: Creative grading
3. Allows easy adjustment of look without affecting corrections
4. Facilitates client revisions and iterations

**Modular Approach**
- Group related corrections in compound nodes
- Label nodes clearly for easy navigation
- Use node comments for complex adjustments
- Create reusable node templates

## HDR Grading Mastery

### HDR Color Space Setup

**Project Settings**
- Timeline Color Space: Rec.2100 ST 2084 (PQ) or HLG
- Output Color Space: Match delivery requirements
- Enable HDR scopes (HDR Waveform, HDR Parade)
- Set peak brightness target (1000, 2000, 4000 nits)

**Color Management**
- Input Color Space: Camera native (e.g., Sony S-Log3, ARRI LogC)
- Color Science: DaVinci YRGB Color Managed
- Processing Mode: DaVinci Wide Gamut
- Automatic color space transforms for clips

### HDR Grading Wheels

**Zone-Based Control**
- Customizable luminance zones (typically 4-6 zones)
- Independent color and exposure per zone
- Smooth transitions between zones
- Precise control over HDR range

**Zone Configuration**
- **Zone 1**: Deep shadows (0-10% luminance)
- **Zone 2**: Shadows (10-30%)
- **Zone 3**: Midtones (30-60%)
- **Zone 4**: Highlights (60-85%)
- **Zone 5**: Specular highlights (85-95%)
- **Zone 6**: Peak whites (95-100%)

**HDR Grading Workflow**
1. Set overall exposure using Offset
2. Adjust individual zones for tonal distribution
3. Add color to specific zones for creative look
4. Manage peak brightness to avoid clipping
5. Check on HDR reference monitor
6. Create SDR version using Color Space Transform

### HDR to SDR Conversion

**Automatic Conversion**
- Add Color Space Transform node
- Input: Timeline color space (HDR)
- Output: Rec.709 Gamma 2.4 (SDR)
- Adjust tone mapping for optimal SDR appearance

**Manual Trim Pass**
- Grade HDR version first
- Create SDR deliverable using transform
- Add trim pass node after transform
- Adjust for SDR-specific issues (crushed blacks, blown highlights)
- Maintain creative intent across both versions

## Color Warper Deep Dive

### Understanding the Warper Interface

**Grid Display**
- Hue on horizontal axis
- Saturation on vertical axis
- Luminance as third dimension (advanced mode)
- Control points for precise warping

**Warping Techniques**
- Drag hues to shift colors
- Push/pull saturation for specific hues
- Create complex color transformations
- Warp based on luminance for selective changes

### Practical Warper Applications

**Skin Tone Refinement**
1. Isolate skin tone hue range
2. Warp toward ideal skin tone hue
3. Adjust saturation for healthy appearance
4. Refine based on luminance (shadows vs. highlights)

**Sky Enhancement**
1. Select cyan/blue hue range
2. Shift toward richer blue
3. Increase saturation selectively
4. Maintain natural appearance

**Foliage Correction**
1. Target yellow-green to blue-green range
2. Shift toward desired green hue
3. Adjust saturation for vibrant or muted look
4. Separate foreground and background greens

## Magic Mask and AI Tools

### Magic Mask Workflow

**Automatic Detection**
1. Add node for isolated adjustment
2. Enable Magic Mask in node
3. Select mask type: Person, Face, or Object
4. Resolve automatically detects and tracks
5. Refine mask if needed
6. Apply corrections to masked area

**Mask Types**
- **Person**: Full body detection and tracking
- **Face**: Facial features and skin
- **Object**: Custom object selection and tracking

**Refinement Options**
- Mask softness for edge blending
- Mask expansion/contraction
- Temporal smoothing for stable tracking
- Manual correction for difficult frames

### Face Refinement Tool

**Automatic Face Analysis**
- Detects faces in frame
- Creates separate masks for:
  - Overall face
  - Skin
  - Eyes
  - Mouth
  - Nose
- Tracks through movement automatically

**Beauty Retouching Workflow**
1. Enable Face Refinement
2. Adjust skin smoothing (subtle for natural look)
3. Brighten eyes selectively
4. Enhance lip color if needed
5. Reduce shine on skin
6. Maintain texture for realism

## Advanced Qualifier Techniques

### Precision Color Selection

**HSL Qualification Mastery**
- Start with narrow selection, expand as needed
- Use Hue width for color range
- Saturation range to exclude desaturated areas
- Luminance range for tonal selectivity

**Qualifier Refinement**
- **Blur Radius**: Softens selection edges
- **Denoise**: Reduces noise in selection
- **Matte Finesse**: Overall matte refinement
- **In/Out Ratio**: Adjusts selection density

### Combining Qualifiers and Windows

**Hybrid Selection**
1. Use qualifier for color-based selection
2. Add power window for spatial limitation
3. Combine using matte operations (Intersect, Add, Subtract)
4. Refine combined selection
5. Apply targeted correction

**Matte Operations**
- **Add**: Combines selections (union)
- **Subtract**: Removes one selection from another
- **Intersect**: Only areas in both selections
- **Invert**: Reverses selection

## Tracking and Stabilization

### Power Window Tracking

**Tracking Workflow**
1. Position power window on target
2. Enable tracking in Tracker palette
3. Set tracking mode (Forward, Backward, All)
4. Analyze motion
5. Review and refine tracking
6. Apply corrections to tracked window

**Tracking Modes**
- **Point Tracker**: Single point tracking
- **Window Tracker**: Tracks window shape and position
- **3D Tracker**: Tracks in 3D space (Resolve Studio)

**Tracking Refinement**
- Manually adjust keyframes where tracking fails
- Use onion skin to visualize tracking path
- Smooth tracking data for natural movement
- Adjust tracking sensitivity for difficult shots

### Stabilization for Grading

**Stabilize for Correction**
1. Stabilize shot in Color page
2. Apply corrections to stabilized image
3. Corrections remain locked to image
4. Useful for moving shots requiring precise adjustments

## Resolve FX Advanced Usage

### Film Grain Emulation

**Authentic Grain**
- Choose grain type (16mm, 35mm, 65mm)
- Adjust grain size and intensity
- Control grain in shadows, midtones, highlights separately
- Add grain after all corrections for realism

**Grain Workflow**
1. Complete all color corrections
2. Add Film Grain node at end of tree
3. Select appropriate grain type for look
4. Adjust intensity (subtle for modern, heavy for vintage)
5. Vary grain by tonal range for authenticity

### Glow and Diffusion

**Cinematic Glow**
- Simulates optical diffusion and halation
- Adjustable threshold for glow activation
- Control glow spread and intensity
- Separate color control for glow

**Glow Applications**
- Soften harsh digital look
- Create dreamy, romantic atmosphere
- Enhance practical lights in frame
- Simulate vintage lens characteristics

### Color Space Transform

**Flexible Color Space Conversion**
- Convert between any color spaces
- Input and output color space selection
- Tone mapping options for HDR/SDR
- Gamut mapping for wide gamut sources

**Common Uses**
- LOG to Rec.709 conversion
- HDR to SDR conversion
- Camera color space to timeline color space
- Delivery format conversions

## Shot Matching Strategies

### Automatic Shot Match

**Match Workflow**
1. Grade reference shot (hero shot)
2. Select clips to match in timeline
3. Right-click > Shot Match To > [Reference Clip]
4. Resolve analyzes and applies matching grade
5. Review and refine automatic match

**Match Options**
- Match color only
- Match color and contrast
- Match color, contrast, and brightness
- Custom match parameters

### Manual Matching Techniques

**Scope-Based Matching**
1. Display reference shot in left viewer
2. Display current shot in right viewer
3. Enable scopes for both viewers
4. Match waveform shapes for luminance
5. Match RGB parade for color balance
6. Match vectorscope for hue and saturation

**Gallery Workflow**
1. Save reference grade as still
2. Enable wipe mode to compare
3. Adjust current grade to match reference
4. Use split screen for side-by-side comparison
5. Save matched grade as new still

## Performance Optimization

### Render Cache Strategy

**Cache Types**
- **Smart Cache**: Caches complex effects automatically
- **User Cache**: Manual cache of selected clips
- **Render Cache**: Pre-renders for real-time playback

**Optimization Workflow**
1. Enable Smart Cache in Playback menu
2. Set cache format (ProRes, DNxHR)
3. Cache complex grades for smooth playback
4. Clear cache when making significant changes
5. Render cache before client review

### Optimized Media

**Proxy Workflow**
1. Generate optimized media on import
2. Grade using optimized media
3. Automatically uses original media on export
4. Significant performance improvement for 4K+

**Optimized Media Settings**
- Resolution: Half or quarter of original
- Format: ProRes Proxy or DNxHR LB
- Maintains color accuracy
- Transparent to grading workflow

## Collaborative Workflows

### Multi-User Collaboration

**Setup Requirements**
- Shared PostgreSQL database
- Network storage for media
- Multiple Resolve workstations
- Consistent color management settings

**Collaboration Features**
- Multiple colorists work simultaneously
- Real-time updates across workstations
- Timeline locking to prevent conflicts
- Chat and annotation tools
- Version control for grades

### Remote Grading

**Remote Workflow**
- Colorist works remotely on project
- Client reviews via streaming or review tools
- Feedback integrated into grading session
- Deliver final grade remotely

**Tools for Remote Collaboration**
- Frame.io integration for review
- Zoom/Teams for real-time communication
- Remote desktop for client viewing
- Cloud-based project sharing