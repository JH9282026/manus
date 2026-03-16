# Advanced Keying Workflows

Comprehensive techniques for complex chroma key scenarios and professional-grade results.

---

## Multi-Pass Keying Strategy

### When to Use Multi-Pass

- Unevenly lit green screens with varying brightness
- Complex subjects with fine detail (hair, fur, transparent elements)
- Shots with both hard and soft edges requiring different treatment
- Scenarios where single-pass keying leaves artifacts

### Layer-Based Approach

**Pass 1: Core Matte**
- Pull aggressive key on subject's solid areas
- Prioritize clean matte over edge preservation
- Use tighter tolerance settings
- Creates foundation for composite

**Pass 2: Edge Detail**
- Focus exclusively on edge refinement
- Use softer tolerance for fine detail capture
- Preserve hair, fabric texture, semi-transparent elements
- Combine with Pass 1 using matte operations

**Pass 3: Problem Areas**
- Target specific challenging regions
- Use power windows or masks to isolate
- Apply specialized keying or rotoscoping
- Blend seamlessly with other passes

### Combining Passes

- Use matte operations: Max, Min, Add, Subtract
- Layer passes with appropriate blending modes
- Adjust opacity for smooth transitions
- Preview combined result against various backgrounds

## Advanced Edge Techniques

### Edge Color Correction

**Removing Color Fringing**
- Identify residual green/blue on edges
- Use edge color correction tools in keyer
- Apply selective hue shifts to affected areas
- Balance correction to avoid unnatural colors

**Edge Thin/Choke**
- Shrink matte slightly to eliminate problematic edge pixels
- Use sparingly to avoid losing detail
- Combine with edge blur for natural transition
- Adjust based on background plate characteristics

### Hair and Fine Detail

**Preserving Transparency**
- Use screen matte extraction for semi-transparent areas
- Adjust key tolerance to capture fine detail
- Apply edge feathering selectively
- Consider using dedicated hair keying tools

**Dealing with Motion Blur**
- Increase key tolerance for blurred edges
- Use temporal filtering across frames
- Apply edge blur matching motion blur amount
- Consider frame-by-frame refinement for critical shots

## Difference Keying

### Clean Plate Method

**Capturing Clean Plate**
- Record empty green screen before/after subject shoot
- Match exact lighting and camera position
- Use same camera settings and white balance
- Ensure no changes to screen or lighting

**Difference Key Process**
- Compare subject footage to clean plate
- Software identifies differences (subject vs. background)
- Creates matte based on pixel differences
- Effective for static camera shots

**Advantages**
- Handles uneven lighting more effectively
- Reduces spill suppression requirements
- Cleaner keys with less manual refinement
- Ideal for locked-off camera shots

## Luma Key Integration

### Combining Chroma and Luma

**When to Add Luma Keys**
- Very bright highlights on subject
- Deep shadows requiring separate treatment
- Reflective surfaces with complex lighting
- Transparent or translucent materials

**Luma Key Workflow**
- Pull chroma key as primary matte
- Create luma key for specific tonal ranges
- Combine using matte operations
- Refine transition between key types

## Screen Correction Techniques

### Uneven Screen Compensation

**Identifying Issues**
- Use waveform monitor to detect brightness variations
- Check for hotspots and dark areas
- Evaluate color consistency across screen

**Correction Methods**
- Apply graduated filters to even out brightness
- Use power windows for localized adjustments
- Color correct screen before keying
- Consider re-lighting if correction insufficient

### Wrinkle and Texture Removal

**Pre-Key Cleanup**
- Apply subtle blur to screen only (not subject)
- Use noise reduction on background
- Smooth out texture while preserving subject detail
- Balance cleanup with edge preservation

## Advanced Matte Operations

### Matte Choker

- Shrinks or expands matte edges
- Removes thin lines of residual background
- Adjustable geometric vs. soft choke
- Essential for final matte refinement

### Matte Feather

- Softens matte edges for natural blending
- Adjustable feather radius and falloff
- Different settings for different edge types
- Preview against final background for optimization

### Matte Cleanup

- Remove small holes in matte (fill)
- Eliminate isolated pixels (despeckle)
- Smooth jagged edges (smooth)
- Expand/contract matte globally

## Rotoscoping Integration

### When Keying Fails

**Scenarios Requiring Rotoscoping**
- Extreme green spill that can't be suppressed
- Subject wearing green/blue clothing
- Reflective surfaces causing transparency
- Portions of screen damaged or discolored

**Hybrid Approach**
- Use keying for majority of subject
- Rotoscope problem areas manually
- Blend rotoscoped matte with keyed matte
- Maintain consistency across frames

### Rotoscoping Tools

- Mocha Pro for planar tracking and roto
- After Effects Roto Brush for semi-automatic roto
- Silhouette for professional rotoscoping
- Nuke's rotoscoping and tracking tools

## Quality Control Checklist

### Matte Evaluation

- [ ] Clean white on subject, pure black on background
- [ ] No holes or gaps in subject matte
- [ ] Smooth edges without jaggedness
- [ ] Fine detail preserved (hair, fabric)
- [ ] Consistent matte density across frames

### Edge Quality

- [ ] No green/blue fringing on edges
- [ ] Natural edge softness matching subject
- [ ] No chattering or flickering on edges
- [ ] Edge detail preserved through motion

### Composite Integration

- [ ] Subject appears grounded in new background
- [ ] Color and lighting match background plate
- [ ] Shadows and reflections appropriate
- [ ] No visible matte lines or artifacts
- [ ] Consistent quality across entire shot

## Performance Optimization

### Render Efficiency

**Pre-Keying Optimization**
- Trim clips to required duration only
- Use proxies for high-resolution footage
- Apply garbage mattes before keying
- Disable unnecessary effects during preview

**Keying Settings**
- Start with default settings, adjust incrementally
- Avoid over-processing with excessive passes
- Use GPU acceleration when available
- Cache intermediate results for complex composites

### Real-Time Preview

- Lower preview resolution for faster feedback
- Use region of interest for detail work
- Enable draft mode for quick iterations
- Switch to full quality for final evaluation