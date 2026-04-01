---
name: video-editing-advanced
description: "Execute advanced video editing techniques including multi-camera editing, proxy workflows, color grading integration, advanced transitions, audio synchronization, VFX round-tripping, and professional delivery formats. Use for: editing multi-cam shoots, setting up proxy-based edit pipelines, conforming timelines for color and VFX, designing complex transitions and motion graphics, preparing delivery masters, and optimizing NLE performance on large projects."
---

# Video Editing Advanced

Execute professional editing workflows for complex, multi-format, and high-volume video productions.

## Overview

This skill covers editing techniques beyond basic cutting — multi-camera synchronization, proxy workflows for performance, color and VFX round-tripping, advanced audio handling, and mastering deliverables. It focuses on the decisions and processes editors face on professional-scale projects.

## NLE Platform Selection

| NLE | Strength | Best For | Proxy Support | Multi-Cam | Color Integration |
|-----|----------|----------|--------------|-----------|-------------------|
| DaVinci Resolve | Color + edit in one app | Color-heavy projects, all-in-one | Native | Excellent | Built-in |
| Adobe Premiere Pro | Integration with AE, Ps, Au | Creative Cloud workflows | Excellent | Excellent | Lumetri + Resolve via XML |
| Avid Media Composer | Collaborative bin sharing | Long-form TV, multi-editor | AMA + transcode | Industry standard | Roundtrip via AAF |
| Final Cut Pro X | Magnetic timeline, speed | Solo editors, Apple ecosystem | Optimized media | Good | Roundtrip via FCPXML |

## Multi-Camera Editing Workflow

### Setup Process

1. **Ingest and organize** — label clips by camera angle (Cam A, Cam B, Cam C, etc.).
2. **Sync method selection:**

| Sync Method | Accuracy | Requires | Best When |
|-------------|----------|----------|-----------|
| Timecode (TC) | Frame-accurate | Matching TC on all cameras | Professional multi-cam, genlock |
| Audio waveform | Near frame-accurate | Scratch audio on all cameras | Event shoots, music |
| Slate / clapper | Frame-accurate | Visible slate on each camera | Narrative production |
| Manual / marker | Approximate | Visual reference point | Last resort |

3. **Create multi-cam clip/group** — combine synced angles into a single multi-cam source.
4. **Edit in real time** — play back the multi-cam and cut between angles live.
5. **Flatten and refine** — after the live cut, flatten the multi-cam and fine-tune individual cuts.
6. **Audio source** — switch audio to the dedicated audio recorder (if applicable) rather than camera scratch audio.

## Proxy Workflow Architecture

### When to Use Proxies

- Source media exceeds NLE's real-time playback capability (e.g., 8K RAW, high bitrate ProRes 4444).
- Timeline contains heavy effects and playback drops below real-time.
- Editing on a laptop or lower-spec machine.

### Proxy Specifications

| Proxy Format | Resolution | Codec | File Size vs. Original |
|-------------|-----------|-------|------------------------|
| Standard proxy | 1/4 of original | ProRes Proxy or H.264 | ~5–10% |
| Offline proxy | 1/2 of original | ProRes LT or DNxHR LB | ~15–25% |
| High-quality proxy | Match original | ProRes 422 or DNxHR SQ | ~40–60% |

### Proxy Pipeline Steps

1. Transcode source to proxy format (DaVinci Resolve, Resolve, or NLE built-in).
2. Maintain matching file names and folder structure.
3. Edit entirely with proxies.
4. Relink to original media before color grading / finishing.
5. Confirm relink by checking a few clips at full resolution.

## Color Grading Round-Trip

| NLE → Color Tool | Exchange Format | Preserves | Notes |
|-----------------|----------------|-----------|-------|
| Premiere → Resolve | XML (FCP7 XML) | Cuts, speed changes | Send ref movie for verification |
| Avid → Resolve | AAF | Cuts, transitions, some effects | Most reliable for long-form |
| FCP X → Resolve | FCPXML | Magnetic timeline as flat cuts | Compound clips need flattening |
| Resolve edit → Resolve color | Same project | Everything | No export needed |

### Conform Checklist

1. Export timeline from NLE in supported format (XML/AAF/FCPXML).
2. Import into color tool with original media paths.
3. Verify clip count matches NLE timeline.
4. Spot-check 5+ random points in timeline for frame accuracy.
5. Grade on original full-resolution media.
6. Render graded timeline and reimport to NLE for final master.

## Advanced Transition and Effects Techniques

| Technique | Method | Use For |
|-----------|--------|---------|
| J-cut / L-cut | Audio leads or trails the video cut | Natural dialogue flow |
| Match cut | Visual or action continuity between scenes | Thematic transitions |
| Whip pan transition | Fast pan with motion blur bridge | Energetic scene changes |
| Morph cut (Premiere) | AI-based face interpolation | Removing pauses in interviews |
| Speed ramp | Variable speed keyframes | Action highlights, dramatic timing |
| Freeze frame to motion | Hold frame → resume playback | Emphasis, title cards |
| Split screen | Multiple sources composited | Comparison, multi-POV |

## Audio Post-Production Integration

### NLE Audio Workflow

1. **Sync dual-system audio** — match camera scratch to external recorder via timecode or waveform.
2. **Rough mix in NLE** — set dialogue levels to -12 dBFS, music to -18 dBFS, SFX to -15 dBFS.
3. **Export for audio post** — AAF or OMF with embedded audio and 2-second handles.
4. **Receive mixed audio** — import final mix stems back into NLE timeline.
5. **Verify sync** — check lip sync at 3+ points in the timeline.

### Level Targets

| Content Type | Integrated Loudness | True Peak Max |
|-------------|--------------------|--------------|
| Broadcast (ATSC) | -24 LKFS ±2 | -2 dBTP |
| Streaming (Netflix, etc.) | -27 LKFS ±2 | -2 dBTP |
| YouTube / web | -14 LKFS (normalized) | -1 dBTP |
| Podcast | -16 LKFS | -1 dBTP |

## Delivery Master Specifications

| Deliverable | Resolution | Codec | Bitrate / Quality |
|-------------|-----------|-------|-----------------|
| Broadcast master | 1920×1080 | ProRes 422 HQ / DNxHR HQX | ~220 Mbps |
| Cinema DCP | 2048×1080 or 4096×2160 | JPEG 2000 | ~250 Mbps |
| Streaming master (Netflix) | 3840×2160 | ProRes 422 HQ | ~600 Mbps |
| YouTube upload | 3840×2160 | H.264/H.265 | 40–80 Mbps |
| Social media | 1080×1920 (vertical) | H.264 | 8–15 Mbps |
| Client review | 1920×1080 | H.264 | 10–20 Mbps |

## NLE Performance Optimization

1. **Store media on SSD** — NVMe preferred for 4K+ RAW playback.
2. **Render cache** — pre-render heavy effects sections.
3. **Reduce playback resolution** — 1/4 or 1/2 for editing, full for review.
4. **Close background apps** — maximize RAM for NLE.
5. **Use optimized media** — transcode once, edit fast, relink for finish.
6. **GPU acceleration** — enable hardware decoding/encoding in NLE preferences.

## Best Practices

1. **Organize before you cut** — bin structure, naming conventions, and metadata save hours later.
2. **Save versions** — save as new version at each major milestone (assembly, rough, fine, locked).
3. **Never delete source media** — archive everything until the project is fully delivered.
4. **Edit with sound** — audio drives pacing; don't edit on mute.
5. **Watch at real speed** — always review the full timeline at 1× speed before sharing.
6. **Backup the project file** — store project files separately from media with daily versioning.

## Using the Reference Files

### When to Read Each Reference

**`/references/fundamentals.md`** — Read when learning core editing theory, cut types (hard cut, dissolve, wipe), pacing principles, or understanding timeline structure and track management.

**`/references/advanced-techniques.md`** — Read when executing complex workflows like nested timelines, dynamic linking to After Effects, multicam with 8+ angles, or conforming between different NLEs.

**`/references/workflows-best-practices.md`** — Read when setting up a multi-editor project, designing file naming conventions, creating a DIT-to-edit ingest pipeline, or standardizing delivery specifications.

**`/references/troubleshooting.md`** — Read when diagnosing timeline performance issues, fixing audio drift, resolving media offline errors, or troubleshooting export failures and codec incompatibilities.
