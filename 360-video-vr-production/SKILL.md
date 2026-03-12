---
name: 360-video-vr-production
description: "Create immersive 360° video and VR content including camera selection, stitching workflows, spatial audio, and interactive experiences. Use for shooting 360 footage, stitching panoramic video, adding spatial audio, creating VR experiences, optimizing for VR headsets, building interactive 360 tours, and publishing to YouTube 360 or VR platforms."
---

# 360° Video & VR Production

Create immersive 360-degree video content and virtual reality experiences from capture to delivery.

## Overview

This skill covers the complete 360° video and VR production pipeline: camera systems, shooting techniques, stitching workflows, spatial audio integration, interactive elements, and platform-specific delivery. Use it when producing immersive content for VR headsets, YouTube 360, social media, or custom applications.

## Camera System Selection

| Use Case | Camera Type | Resolution | Budget | Reference |
|----------|-------------|------------|--------|-----------|
| Professional cinematic | Multi-camera rig (6-24 cameras) | 8K+ | $50K+ | `/references/camera-systems.md` |
| High-end production | Insta360 Pro 2, Kandao Obsidian | 8K | $3K-$10K | `/references/camera-systems.md` |
| Mid-range content | Insta360 One X3, GoPro MAX | 5.7K | $400-$600 | `/references/camera-systems.md` |
| Entry/prosumer | Ricoh Theta Z1, Insta360 ONE RS | 5.7K | $200-$800 | `/references/camera-systems.md` |
| Real estate/tours | Matterport Pro2, Ricoh Theta X | 4K-5.7K | $400-$4K | `/references/camera-systems.md` |

## Shooting Best Practices

### Camera Placement
- **Height**: Position at eye level (1.5-1.7m) for natural viewer perspective
- **Distance**: Keep subjects 1.5-3m from camera; closer creates distortion
- **Stability**: Use monopod or tripod; hide stand in post or use nadir patch
- **Lighting**: Ensure even 360° illumination; avoid mixed color temperatures

### Common Mistakes to Avoid
1. Standing too close to camera (creates giant effect)
2. Uneven lighting creating harsh exposure differences
3. Visible crew/equipment in frame
4. Camera shake during capture
5. Forgetting to check all angles before shooting

## Stitching Workflow

| Software | Best For | Platform | Price |
|----------|----------|----------|-------|
| Mistika VR | Professional cinema | Win/Mac | $2K+ |
| Autopano Video Pro | Multi-cam rigs | Win/Mac | $600 |
| Insta360 Studio | Insta360 cameras | Win/Mac | Free |
| GoPro Player | GoPro MAX/Fusion | Win/Mac | Free |
| DaVinci Resolve | Color grading + stitch | Win/Mac/Linux | Free/$295 |

### Stitching Process
1. **Import** footage from all cameras/lenses
2. **Sync** clips using audio waveforms or timecode
3. **Calibrate** lens profiles and stitch lines
4. **Blend** seams using optical flow or manual masking
5. **Stabilize** using gyro data or software stabilization
6. **Render** to equirectangular format

## Spatial Audio Integration

| Audio Format | Headset Support | Channels | Use Case |
|--------------|-----------------|----------|----------|
| Ambisonics (1st order) | All VR headsets | 4 ch | Standard VR |
| Ambisonics (3rd order) | High-end | 16 ch | Premium VR |
| Object-based | Quest, PSVR2 | Variable | Interactive |
| Binaural | All headphones | 2 ch | 360 video |

### Spatial Audio Workflow
1. Record with ambisonic microphone (Zoom H3-VR, Rode NT-SF1)
2. Sync audio to video using slate or timecode
3. Process in spatial audio DAW (Reaper + plugins, FB360)
4. Export ambisonics or binaural depending on platform

## Interactive VR Elements

| Element Type | Tool/Platform | Complexity | Reference |
|--------------|---------------|------------|-----------|
| Hotspots/waypoints | WondaVR, InstaVR | Low | `/references/interactive-vr.md` |
| Branching narratives | Unity, Unreal | Medium | `/references/interactive-vr.md` |
| Gaze-based interaction | A-Frame, React 360 | Medium | `/references/interactive-vr.md` |
| Hand tracking | Quest SDK, Unity XR | High | `/references/interactive-vr.md` |
| Full room-scale | SteamVR, Quest | High | `/references/interactive-vr.md` |

## Export & Delivery Specifications

| Platform | Max Resolution | Frame Rate | Codec | Max Bitrate |
|----------|----------------|------------|-------|-------------|
| YouTube 360 | 8K (8192×4096) | 60fps | H.264/VP9 | 120 Mbps |
| Meta Quest | 5.7K (5760×2880) | 72fps | H.265 | 100 Mbps |
| Vimeo 360 | 8K | 60fps | H.264 | 80 Mbps |
| Facebook 360 | 4K | 60fps | H.264 | 45 Mbps |
| Apple Vision Pro | 8K+ | 90fps | HEVC | 150 Mbps |

### Metadata Injection
- **YouTube/Facebook**: Use Spatial Media Metadata Injector
- **Custom apps**: Embed projection type in container metadata
- **Projection**: Equirectangular (standard) or EAC (YouTube optimized)

## Using the Reference Files

### When to Read Each Reference

**`/references/camera-systems.md`** — Read when selecting cameras for a specific project, comparing sensor specs, or troubleshooting camera-specific issues.

**`/references/stitching-advanced.md`** — Read when dealing with complex multi-camera rigs, manual stitch line adjustment, or resolving parallax issues.

**`/references/interactive-vr.md`** — Read when adding interactive elements, building VR tours, or implementing branching narratives.

**`/references/spatial-audio-deep-dive.md`** — Read when setting up ambisonic recording, processing spatial audio, or troubleshooting head-tracking audio sync.
