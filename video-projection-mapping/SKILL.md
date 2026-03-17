---
name: video-projection-mapping
description: "Create video projection mapping installations transforming physical objects and buildings into dynamic display surfaces. Use for architectural mapping, art installations, live events, corporate presentations, museum exhibits, retail displays, stage design, interactive experiences, and spatial augmented reality projects."
---

# Video Projection Mapping

Transform physical objects and architectural structures into dynamic display surfaces using spatially-mapped video projection.

## Overview

This skill covers the complete projection mapping workflow: spatial calibration, content design, software selection, multi-projector blending, installation setup, and interactive integration. Use it when creating architectural projections, immersive art installations, event productions, retail experiences, or any project requiring video content precisely aligned to three-dimensional surfaces.

## Software Selection by Use Case

| Software | Best For | Skill Level | Price | Key Features |
|----------|----------|-------------|-------|-------------|
| HeavyM | Beginners, quick setups, live performances | Beginner | €29-99/mo | Drag-and-drop, visual library, music sync | 
| MadMapper | Professional mapping, precise control | Intermediate-Advanced | €599 | 3D scanner, Bezier masking, timeline |
| Resolume Arena | VJ performances, live events, multi-output | Intermediate-Advanced | €799 | Audio-visual sync, effects, DMX control |
| TouchDesigner | Generative content, interactive installations | Advanced | Free (commercial license €600/yr) | Node-based, real-time generative graphics |
| Smode | Large-scale productions, broadcast | Advanced | €99-299/mo | Real-time 3D, generative content, high-res |
| Disguise | Mega-events, touring productions | Professional | Custom pricing | Cloud pre-viz, workflow integration |
| MapMap | Open-source, budget projects | Beginner-Intermediate | Free | OSC control, basic mapping |

See `/references/mapping-software.md` for detailed software comparisons, feature breakdowns, and workflow guides.

## Core Equipment Requirements

### Essential Components

**Computer**:
- **Minimum**: i7 processor, 16GB RAM, dedicated GPU (GTX 1660 or better)
- **Recommended**: i9/Ryzen 9, 32GB+ RAM, RTX 3070 or better
- **Professional**: Dual GPU setup, 64GB RAM, multiple video outputs
- Must support required video outputs (HDMI, DisplayPort, SDI)

**Projector(s)**:
- **Brightness**: 3,000-5,000 lumens (small indoor), 10,000+ lumens (large/outdoor)
- **Resolution**: 1920x1080 (standard), 1920x1200 (WUXGA), 4K for high-detail
- **Throw Ratio**: Match to distance and surface size
- **Lens**: Interchangeable lenses for flexibility (short-throw, long-throw, ultra-wide)

**Projection Mapping Software**: See table above

**Cables and Adapters**:
- HDMI, DisplayPort, or SDI cables (length as needed)
- Signal boosters for long runs (50+ feet)
- Adapters for computer-to-projector connection

### Optional Equipment

**Sensors and Cameras** (for interactive mapping):
- Kinect, RealSense, or LiDAR for motion tracking
- Webcams for computer vision
- Infrared sensors for touch detection

**Media Servers** (for complex shows):
- Dedicated playback hardware (Disguise, Green Hippo, 7th Sense)
- Redundancy and reliability for critical events

**Mounting and Rigging**:
- Projector mounts, trusses, stands
- Safety cables and power distribution

See `/references/installation-setup.md` for detailed equipment specifications, purchasing guides, and setup configurations.

## Projection Mapping Workflow

### 1. Planning and Pre-Visualization

**Site Survey**:
1. Measure projection surface dimensions
2. Determine projector placement options (distance, angle, height)
3. Assess ambient light conditions (darkness ideal, control light if possible)
4. Identify power and mounting requirements
5. Photograph surface from multiple angles

**Calculate Throw Distance**:
- Use projector's throw ratio to determine placement
- **Formula**: Distance = Throw Ratio × Screen Width
- **Example**: 1.5:1 throw ratio, 20-foot wide surface = 30 feet distance
- Account for keystone correction needs (minimize if possible)

**Pre-Visualization**:
- Create 3D model of surface (photogrammetry, CAD, or manual modeling)
- Import into mapping software or Disguise for virtual planning
- Test content ideas and camera positions digitally
- Identify potential issues before installation

### 2. Installation and Calibration

**Physical Setup**:
1. Mount projector(s) at calculated position
2. Secure all cables and power
3. Ensure projector is stable (vibration ruins alignment)
4. Connect projector to computer
5. Configure computer display settings (projector as extended display, not mirrored)

**Spatial Calibration**:
1. Project test pattern onto surface
2. In mapping software, create mesh or mask matching surface geometry
3. Warp and align projected content to physical edges and features
4. Use software's calibration tools (grid, corner pinning, Bezier curves)
5. For 3D objects, map each face separately
6. Test alignment with high-contrast content

**Multi-Projector Blending** (if using multiple projectors):
1. Overlap projector outputs by 10-20%
2. Use edge-blending feature in software
3. Adjust brightness in overlap zones for seamless blend
4. Color-match projectors (white balance, brightness)
5. Test with full-frame content to verify seamless appearance

See `/references/projection-techniques.md` for advanced calibration methods, troubleshooting, and optimization strategies.

### 3. Content Creation

**Design Principles**:
- **Respect Geometry**: Design content that enhances or plays with surface architecture
- **High Contrast**: Bold colors and contrast read better than subtle gradients
- **Motion**: Movement attracts attention and creates dynamism
- **Storytelling**: Use surface features to tell visual stories
- **Illusion**: Create depth, transformation, or impossible physics

**Content Types**:
- **Architectural Illusion**: Make building appear to transform, collapse, or morph
- **Abstract Patterns**: Geometric shapes, flowing textures, generative art
- **Narrative Sequences**: Tell stories using surface as canvas
- **Data Visualization**: Display information spatially
- **Interactive**: Respond to audience input (motion, touch, sound)

**Software for Content Creation**:
- **After Effects**: Motion graphics, compositing, effects
- **Cinema 4D / Blender**: 3D animation, modeling, rendering
- **TouchDesigner / Smode**: Real-time generative graphics
- **Resolume / MadMapper**: Built-in effects and visual libraries
- **Unity / Unreal Engine**: Real-time 3D, interactive content

**Technical Specifications**:
- **Resolution**: Match projector resolution (1920x1080, 1920x1200, 4K)
- **Aspect Ratio**: Match projector aspect ratio (16:9, 16:10, custom)
- **Frame Rate**: 30 fps (standard), 60 fps (smooth motion)
- **Format**: H.264 MP4 (compatibility), HAP codec (performance), image sequences (flexibility)
- **Color Space**: sRGB or Rec.709 (match projector)

See `/references/content-creation.md` for detailed design workflows, creative techniques, and optimization strategies.

### 4. Playback and Control

**Playback Methods**:
- **Timeline-Based**: Pre-programmed sequence plays start to finish
- **Cue-Based**: Trigger specific clips or sequences manually
- **Interactive**: Content responds to sensors, audience, or data inputs
- **Generative**: Real-time content generation (never repeats exactly)

**Control Protocols**:
- **DMX**: Lighting control protocol, sync with stage lighting
- **MIDI**: Musical instrument control, trigger clips with MIDI controllers
- **OSC (Open Sound Control)**: Network-based, flexible control from apps or devices
- **Timecode**: Sync with audio, video, or lighting using SMPTE timecode

**Live Performance**:
- Use VJ software (Resolume, MadMapper) for real-time control
- Map MIDI controllers or keyboards to trigger clips and effects
- Adjust parameters live (color, speed, opacity, effects)
- Prepare backup content and failsafe options

## Application Types

### Architectural Projection Mapping

**Use Cases**: Building facades, monuments, landmarks, festivals

**Considerations**:
- Large scale requires high-lumen projectors (10,000-30,000+ lumens)
- Long throw distances (100-300+ feet)
- Outdoor conditions (weather, ambient light, power)
- Permits and permissions required
- Safety and crowd management

**Best Practices**:
- Scout location during day and night
- Test projector placement and brightness
- Create content that enhances architectural features
- Plan for weather contingencies (rain covers, wind)
- Coordinate with local authorities and building owners

### Art Installations

**Use Cases**: Galleries, museums, public art, immersive experiences

**Considerations**:
- Creative freedom and experimentation
- Interactive elements enhance engagement
- Looping content for continuous display
- Ambient sound or music integration

**Best Practices**:
- Design for the space (consider viewer positions and movement)
- Test with audience to refine interaction
- Create seamless loops (content repeats without jarring transitions)
- Provide artist statement or context for viewers

### Live Events and Performances

**Use Cases**: Concerts, theater, corporate events, product launches

**Considerations**:
- Real-time control and flexibility
- Sync with audio, lighting, and performers
- Backup systems for reliability
- Quick setup and teardown

**Best Practices**:
- Rehearse extensively with performers
- Create cue sheets and timelines
- Have backup projectors and computers ready
- Coordinate with lighting and audio teams
- Test all control systems before show

### Retail and Commercial

**Use Cases**: Store displays, trade shows, brand activations, advertising

**Considerations**:
- Brand messaging and visual identity
- Attract attention in busy environments
- Durability for extended operation
- Easy content updates

**Best Practices**:
- High-contrast, bold visuals for visibility
- Short, looping content (30-60 seconds)
- Align with brand colors and messaging
- Schedule content updates to maintain freshness

## Common Challenges and Solutions

| Challenge | Cause | Solution |
|-----------|-------|----------|
| Keystone distortion | Projector not perpendicular to surface | Reposition projector, use lens shift, minimize software correction |
| Ambient light washout | Bright environment | Increase projector lumens, control ambient light, schedule for darkness |
| Alignment drift | Projector movement, heat expansion | Secure mounting, allow warm-up time, recalibrate if needed |
| Color mismatch (multi-projector) | Different projector models/settings | Use same projector models, calibrate white balance and brightness |
| Flickering or tearing | Frame rate mismatch, cable issues | Match frame rates, use quality cables, check GPU settings |
| Low frame rate | Underpowered computer, complex content | Upgrade hardware, optimize content, use HAP codec |
| Hotspots or uneven brightness | Projector placement, surface texture | Adjust projector angle, use multiple projectors, compensate in content |

See `/references/projection-techniques.md` for detailed troubleshooting and advanced problem-solving.

## Interactive Projection Mapping

### Motion Tracking

**Sensors**: Kinect, RealSense, LiDAR, webcams

**Applications**:
- Content responds to viewer movement
- Particles follow or avoid people
- Trigger animations when someone approaches
- Create virtual shadows or reflections

**Software**: TouchDesigner, Isadora, Processing, Max/MSP

### Touch Detection

**Methods**:
- Infrared touch frames
- Computer vision (detect touch via camera)
- Capacitive surfaces

**Applications**:
- Interactive walls or tables
- Games and educational exhibits
- Data exploration interfaces

### Audio Reactivity

**Input**: Microphone, audio interface, music playback

**Applications**:
- Visuals pulse with music beats
- Frequency-based animations (bass, mids, highs)
- Voice-activated content
- Ambient sound visualization

**Software**: Resolume, HeavyM, TouchDesigner, MadMapper

## Using the Reference Files

### When to Read Each Reference

**`/references/mapping-software.md`** — Read when selecting software for your project, comparing features and workflows, learning specific software techniques, or troubleshooting software issues.

**`/references/projection-techniques.md`** — Read when calibrating projectors, solving alignment issues, implementing multi-projector blending, optimizing image quality, or troubleshooting technical problems.

**`/references/content-creation.md`** — Read when designing projection content, learning creative techniques, optimizing video for performance, creating generative or interactive content, or planning visual narratives.

**`/references/installation-setup.md`** — Read when planning installations, selecting and configuring equipment, calculating throw distances and brightness requirements, setting up interactive systems, or managing large-scale productions.
