# Layers, Masks, and Compositing Fundamentals

## Overview

Layers, masks, and compositing form the foundation of modern non-destructive photo editing. These fundamental concepts enable photographers and retouchers to make complex adjustments, combine multiple images, and create sophisticated effects while maintaining complete flexibility and control. Understanding these tools is essential for professional-quality photo editing and retouching.

## Understanding Layers

Layers are the fundamental building blocks of non-destructive editing in software like Adobe Photoshop. They function as transparent sheets stacked on top of each other, each containing different elements or effects.

### The Layer Concept

#### Visualization

Think of layers as transparent sheets of acetate stacked on top of each other:
- Each sheet can contain different content
- You can see through transparent areas to layers below
- The order of sheets affects what you see
- You can show, hide, or rearrange sheets
- Changes to one sheet don't affect others

#### Why Layers Matter

**Non-Destructive Editing:**
- Original image remains untouched
- Changes can be modified or removed anytime
- Experiment without risk
- Maintain editing flexibility
- Professional workflow standard

**Organization:**
- Separate different elements and adjustments
- Easy to locate and modify specific edits
- Complex projects remain manageable
- Collaborative work simplified

**Flexibility:**
- Turn effects on/off instantly
- Adjust intensity with opacity
- Reorder for different results
- Combine multiple techniques

### Layer Types

#### Image Layers (Pixel Layers)

Standard layers containing pixel information.

**Characteristics:**
- Contain actual image data
- Can be painted on, cloned, healed
- Subject to resolution limitations
- Most common layer type

**Uses:**
- Duplicate of original for safety
- Separate elements in composition
- Retouching work
- Painted or drawn content

#### Adjustment Layers

Special layers that apply color and tonal adjustments non-destructively.

**Types:**
- Levels
- Curves
- Hue/Saturation
- Color Balance
- Black & White
- Brightness/Contrast
- Selective Color
- Photo Filter

**Benefits:**
- Don't alter original pixels
- Can be modified anytime
- Include built-in layer mask
- Affect all layers below
- Can be clipped to single layer

**Workflow:**
1. Create adjustment layer
2. Make adjustments in Properties panel
3. Use mask to control where adjustment applies
4. Adjust opacity for intensity
5. Modify or delete anytime

#### Text Layers

Layers containing editable text.

**Features:**
- Fully editable text
- Font, size, color adjustable
- Character and paragraph formatting
- Layer styles applicable
- Can be rasterized if needed

**Uses:**
- Titles and captions
- Watermarks
- Graphic design elements
- Typography work

#### Shape Layers

Vector-based layers containing geometric shapes.

**Characteristics:**
- Resolution-independent (vector)
- Infinitely scalable
- Crisp edges at any size
- Editable paths

**Uses:**
- Geometric elements
- Icons and graphics
- Masks and selections
- Design elements

#### Smart Objects

Special layers that embed raster or vector data.

**Key Features:**

**Non-Destructive Transformations:**
- Scale, rotate, warp without quality loss
- Original data preserved
- Can reset transformations
- Multiple transformations without degradation

**Smart Filters:**
- Filters applied non-destructively
- Can be adjusted or removed
- Include filter masks
- Stack multiple filters

**Linked Instances:**
- Edit one, update all instances
- Efficient workflow for repeated elements
- Maintain consistency

**Creating Smart Objects:**
- Right-click layer > Convert to Smart Object
- Place file as Smart Object
- Layer > Smart Objects > Convert to Smart Object

**When to Use:**
- Before transforming layers
- When applying filters
- For linked instances
- Embedding external files
- Preserving quality

### Layer Properties and Controls

#### Visibility

**Eye Icon:**
- Click to show/hide layer
- Hidden layers don't affect output
- Useful for comparing versions
- Organize complex documents

**Shortcuts:**
- Alt/Option + click eye: Solo layer (hide all others)
- Useful for isolating specific layers

#### Opacity

**Control:**
- 0% = Completely transparent
- 100% = Completely opaque
- Slider or numeric input
- Keyboard shortcuts: 1 = 10%, 5 = 50%, 0 = 100%

**Uses:**
- Reduce effect intensity
- Blend layers subtly
- Create transparency effects
- Fine-tune adjustments

#### Fill

**Difference from Opacity:**
- Affects layer content only
- Doesn't affect layer styles
- Useful for style-only effects

#### Blending Modes

Blending modes determine how a layer interacts with layers below.

**Common Blending Modes:**

**Normal:**
- Default mode
- No blending
- Covers layers below (based on opacity)

**Multiply:**
- Darkens image
- Multiplies colors
- Good for shadows and darkening

**Screen:**
- Lightens image
- Opposite of Multiply
- Good for highlights and lightening

**Overlay:**
- Combines Multiply and Screen
- Increases contrast
- Preserves highlights and shadows
- Good for dodge/burn layers

**Soft Light:**
- Subtle version of Overlay
- More natural results
- Good for gentle contrast

**Color:**
- Applies hue and saturation only
- Preserves luminosity
- Good for colorizing

**Luminosity:**
- Applies brightness only
- Preserves hue and saturation
- Good for sharpening without color shifts

**Experimentation:**
- Try different modes
- Combine with opacity adjustments
- Different modes for different effects
- No right or wrong, only what works

#### Layer Order (Stacking)

**Importance:**
- Layers on top appear in front
- Order affects final appearance
- Adjustment layers affect layers below

**Reordering:**
- Drag layers up or down
- Cmd/Ctrl + [ or ] to move
- Experiment with different orders

### Layer Organization

#### Naming Layers

**Best Practices:**
- Descriptive names ("Skin Retouching" not "Layer 1")
- Consistent naming convention
- Include purpose or content
- Makes navigation easier

**Renaming:**
- Double-click layer name
- Type new name
- Press Enter

#### Color Coding

**Purpose:**
- Visual organization
- Group related layers
- Quick identification
- Personal system

**How:**
- Right-click layer
- Select color
- Apply to related layers

#### Layer Groups

**Creating Groups:**
- Select layers
- Cmd/Ctrl + G
- Or: Layer > Group Layers
- Name group descriptively

**Benefits:**
- Collapse/expand for cleaner workspace
- Apply adjustments to entire group
- Move multiple layers together
- Organize complex projects
- Apply masks to groups

**Group Properties:**
- Opacity affects all layers in group
- Blending modes available
- Can nest groups within groups
- Can apply layer masks

#### Linking Layers

**Purpose:**
- Move multiple layers together
- Maintain relationships
- Don't need to group

**How:**
- Select multiple layers (Cmd/Ctrl + click)
- Click link icon at bottom of Layers panel
- Linked layers move together

## Understanding Masks

Masks are powerful tools that control the visibility of layer content without permanently deleting pixels. They function like stencils, revealing or concealing portions of a layer.

### The Fundamental Principle

#### White Reveals, Black Conceals

This is the core concept of masking:
- **White (255):** Fully visible
- **Black (0):** Fully hidden
- **Gray (1-254):** Partially visible (transparency)

**Grayscale Values:**
- 50% gray = 50% opacity
- Lighter gray = more visible
- Darker gray = more hidden
- Smooth gradients = smooth transitions

### Layer Masks

Layer masks control the visibility of a specific layer.

#### Creating Layer Masks

**Methods:**
1. Click mask icon at bottom of Layers panel
2. Layer > Layer Mask > Reveal All (white mask)
3. Layer > Layer Mask > Hide All (black mask)
4. Make selection, then add mask (masks selection)

**Default:**
- White mask (reveals all)
- Start with everything visible
- Paint black to hide

#### Working with Layer Masks

**Painting on Masks:**

**Tools:**
- Brush Tool (B): Paint black or white
- Gradient Tool (G): Smooth transitions
- Selection tools: Fill areas

**Technique:**
1. Click mask thumbnail (white border indicates active)
2. Select Brush Tool
3. Paint with black to hide
4. Paint with white to reveal
5. Use gray for partial transparency

**Brush Settings:**
- Hardness: 0% for soft edges, 100% for hard edges
- Opacity: Lower for gradual building
- Flow: Controls paint application rate
- Size: Appropriate for area

**Keyboard Shortcuts:**
- X: Switch foreground/background colors (black/white)
- D: Default colors (white foreground, black background)
- [ or ]: Decrease/increase brush size
- Shift + [ or ]: Decrease/increase brush hardness

#### Viewing and Editing Masks

**View Mask:**
- Alt/Option + click mask thumbnail
- See mask in black and white
- Easier to see what you've painted
- Click again to return to normal view

**View Mask as Overlay:**
- \ (backslash) key
- Red overlay shows masked areas
- See mask and image simultaneously
- Adjust overlay color in mask properties

**Disable Mask Temporarily:**
- Shift + click mask thumbnail
- Red X appears on mask
- See layer without mask effect
- Click again to re-enable

**Delete Mask:**
- Right-click mask > Delete Layer Mask
- Or drag mask to trash icon
- Choose to apply or discard

#### Refining Mask Edges

**Select and Mask Workspace:**

**Access:**
- Select > Select and Mask
- Or click "Select and Mask" button in Options bar

**Tools:**
- Refine Edge Brush: Improve edge quality
- Brush Tool: Add or subtract from selection
- Lasso Tool: Manual adjustments

**Settings:**
- Radius: Edge detection area
- Smooth: Reduce jagged edges
- Feather: Soften edge transition
- Contrast: Sharpen edge definition
- Shift Edge: Expand or contract edge

**Output:**
- Output to: Layer Mask
- Decontaminate Colors: Remove color fringe
- Essential for hair and fur masking

### Advanced Masking Techniques

#### Gradient Masks

Create smooth transitions between visible and hidden areas.

**Process:**
1. Add layer mask
2. Select Gradient Tool (G)
3. Choose black to white gradient
4. Drag across image
5. Creates smooth fade

**Uses:**
- Blending images
- Vignettes
- Graduated adjustments
- Sky replacements
- Smooth transitions

#### Luminosity Masks

Select areas based on brightness values.

**Concept:**
- Target specific tonal ranges
- Highlights, midtones, or shadows
- Natural-looking adjustments
- Professional technique

**Creating Luminosity Masks:**
1. Cmd/Ctrl + click RGB channel thumbnail
2. Creates selection of highlights
3. Save selection as channel
4. Invert for shadows
5. Intersect for midtones

**Uses:**
- Selective dodging and burning
- Targeted color grading
- Natural-looking adjustments
- Landscape photography
- HDR blending

#### Color Range Masks

Select areas based on color.

**Process:**
1. Select > Color Range
2. Click color in image or choose preset
3. Adjust fuzziness (tolerance)
4. Preview selection
5. OK to create selection
6. Add layer mask from selection

**Uses:**
- Isolate specific colors
- Adjust single color
- Remove color casts
- Selective saturation

#### Channel Masks

Use color channels for complex selections.

**Process:**
1. Open Channels panel
2. Find channel with best contrast
3. Duplicate channel
4. Adjust levels to increase contrast
5. Load as selection
6. Use as layer mask

**Best For:**
- Hair and fur
- Trees and foliage
- Complex edges
- Transparent objects

### Clipping Masks

Clipping masks use one layer to define the visibility of layers above it.

#### How Clipping Masks Work

**Concept:**
- Base layer defines visible area
- Clipped layers only show where base layer has pixels
- Non-transparent areas of base reveal clipped layers
- Multiple layers can be clipped to one base

**Creating Clipping Masks:**
1. Place layer above base layer
2. Alt/Option + click between layers
3. Or: Layer > Create Clipping Mask
4. Or: Cmd/Ctrl + Alt/Option + G

**Visual Indicator:**
- Clipped layer indented
- Down arrow icon
- Layer thumbnail shows clipping

#### Uses for Clipping Masks

**Texturing Text:**
- Text layer as base
- Image layer clipped above
- Image only visible in text shape
- Non-destructive texturing

**Selective Adjustments:**
- Shape or selection as base
- Adjustment layer clipped above
- Adjustment only affects base layer
- Precise control

**Collages and Composites:**
- Shape defines visible area
- Multiple images clipped to shape
- Easy repositioning
- Clean edges

**Pattern Fills:**
- Object layer as base
- Pattern layer clipped above
- Pattern fills object shape
- Adjustable and flexible

## Compositing: Combining Images

Compositing is the art and technique of combining multiple images or elements into a single, cohesive image.

### Compositing Fundamentals

#### Planning Your Composite

**Before You Start:**

**Concept:**
- Clear vision of final result
- Sketch or reference image
- List of needed elements
- Understand lighting and perspective

**Gather Elements:**
- Source images
- Similar lighting conditions
- Matching perspectives
- Appropriate resolution
- Consistent quality

**Consider:**
- Light direction and quality
- Color temperature
- Perspective and scale
- Depth of field
- Shadows and reflections

#### Basic Compositing Workflow

**Step 1: Prepare Images**
- Open all source images
- Basic color correction
- Crop if needed
- Adjust resolution to match

**Step 2: Extract Elements**
- Make selections
- Refine edges
- Create layer masks
- Clean up edges

**Step 3: Combine Elements**
- Copy/paste or drag between documents
- Position elements
- Scale and transform
- Arrange layer order

**Step 4: Blend Elements**
- Refine masks
- Adjust opacity
- Try blending modes
- Match colors and tones

**Step 5: Integrate Elements**
- Add shadows
- Create reflections
- Match lighting
- Color grade for consistency

**Step 6: Final Adjustments**
- Overall color grading
- Sharpening
- Final touches
- Export

### Blending Techniques

#### Layer Masks for Blending

**Soft Edges:**
- Use soft brush on mask
- Low opacity for gradual blending
- Build up gradually
- Smooth transitions

**Gradient Blending:**
- Gradient on mask
- Smooth fade between images
- Natural-looking blends

**Brush Blending:**
- Paint on mask with soft brush
- Vary opacity
- Follow natural edges
- Blend irregularly for realism

#### Blending Modes for Compositing

**Multiply:**
- Blend dark elements
- Add shadows
- Darken backgrounds

**Screen:**
- Blend light elements
- Add light effects
- Lighten backgrounds

**Overlay/Soft Light:**
- Texture overlays
- Subtle blending
- Maintain contrast

**Lighten/Darken:**
- Preserve lighter/darker pixels
- Useful for specific blending needs

#### Matching Colors and Tones

**Color Match:**
- Image > Adjustments > Match Color
- Match one layer to another
- Adjust intensity
- Neutralize if needed

**Curves Adjustment:**
- Match tonal ranges
- Adjust individual RGB channels
- Sample colors from reference
- Fine-tune relationships

**Hue/Saturation:**
- Match color intensity
- Adjust specific color ranges
- Colorize if needed

### Creating Realistic Composites

#### Matching Lighting

**Light Direction:**
- Ensure consistent light direction
- Add shadows in correct direction
- Highlight appropriate areas
- Match light quality (hard/soft)

**Light Color:**
- Match color temperature
- Warm or cool consistently
- Consider ambient light
- Use color balance adjustments

**Adding Shadows:**
1. Create new layer below subject
2. Paint shadow with soft black brush
3. Blur shadow (Gaussian Blur)
4. Reduce opacity (20-40%)
5. Transform to match perspective
6. Adjust based on light source

**Adding Highlights:**
- Dodge tool or white brush
- Low opacity
- Follow light direction
- Enhance existing highlights

#### Matching Perspective

**Transform Tools:**
- Edit > Transform > Perspective
- Match vanishing points
- Align with background perspective
- Use guides and rulers

**Distortion:**
- Edit > Transform > Distort
- Adjust corners independently
- Match angles and planes

**Warp:**
- Edit > Transform > Warp
- Subtle adjustments
- Match curves and contours

#### Matching Focus and Depth

**Blur Matching:**
- Match background blur
- Filter > Blur > Gaussian Blur or Lens Blur
- Adjust amount to match
- Use layer mask for selective blur

**Depth of Field:**
- Foreground sharper
- Background softer
- Gradual transition
- Realistic depth

**Atmospheric Perspective:**
- Distant objects less contrast
- Cooler colors
- Less saturation
- Lighter tones

#### Edge Refinement

**Defringe:**
- Layer > Matting > Defringe
- Remove color halos
- 1-2 pixel radius usually sufficient

**Remove Color Fringe:**
- Select and Mask > Decontaminate Colors
- Removes edge color contamination
- Essential for hair and transparent objects

**Manual Edge Cleanup:**
- Zoom in to edges
- Paint on mask with small brush
- Refine problem areas
- Use Clone Stamp if needed

### Advanced Compositing Techniques

#### Double Exposure Effect

**Process:**
1. Place two images in same document
2. Align as desired
3. Change top layer blend mode (Screen, Lighten, or Overlay)
4. Adjust opacity
5. Use layer mask to refine
6. Adjust colors for cohesion

#### Replacing Skies

**Process:**
1. Select sky in original image
2. Delete or mask out sky
3. Place new sky below
4. Refine edge of selection
5. Match colors and tones
6. Add atmospheric haze if needed
7. Adjust lighting to match

**Photoshop Sky Replacement:**
- Edit > Sky Replacement
- Automatic sky detection
- Choose from presets or custom
- Adjust settings
- Refine mask if needed

#### Reflection Creation

**Process:**
1. Duplicate subject layer
2. Flip vertical (Edit > Transform > Flip Vertical)
3. Position below subject
4. Reduce opacity (30-60%)
5. Add gradient mask (fade bottom)
6. Blur slightly (motion blur)
7. Adjust perspective if needed

## Workflow Best Practices

### Non-Destructive Editing

**Principles:**
- Never edit original layer directly
- Use adjustment layers
- Work with layer masks
- Use Smart Objects
- Keep layered master file

**Benefits:**
- Complete flexibility
- Ability to revise
- Experiment safely
- Professional workflow
- Client revisions easier

### File Management

**Saving:**
- Save as PSD (preserves layers)
- Save often (Cmd/Ctrl + S)
- Save versions for major changes
- Export flattened for delivery

**File Size:**
- Large files with many layers
- Consider flattening unused layers
- Delete hidden layers if not needed
- Save space when possible

### Keyboard Shortcuts

**Essential Shortcuts:**
- Cmd/Ctrl + J: Duplicate layer
- Cmd/Ctrl + G: Group layers
- Cmd/Ctrl + E: Merge down
- Cmd/Ctrl + Shift + E: Merge visible (to new layer: add Alt/Option)
- Cmd/Ctrl + [ or ]: Move layer down/up
- Cmd/Ctrl + Shift + [ or ]: Move to bottom/top
- Alt/Option + click mask: View mask
- Shift + click mask: Disable mask
- \ (backslash): View mask overlay

**Efficiency:**
- Learn shortcuts gradually
- Customize if desired
- Significant time savings
- Smoother workflow

## Conclusion

Layers, masks, and compositing are the fundamental building blocks of professional photo editing and retouching. Layers provide organization and flexibility, allowing non-destructive editing and complex adjustments. Masks offer precise control over visibility, enabling seamless blending and selective adjustments. Compositing combines these tools to create sophisticated images from multiple sources. Mastering these fundamentals is essential for any serious photographer or retoucher, forming the foundation upon which all advanced techniques are built.

## References

- ProEDU: The Magic of Masking - Photoshop's Hidden Power
- ProEDU: Mastering Layers in Photoshop - A Photographer's Guide
- Phlearn: Photoshop Basics - Adjustments vs Adjustment Layers
- ProEDU: The Power of Adjustment Layers in Photo Editing
- Fiveable: Introduction to Photoshop and Illustrator - Unit 6