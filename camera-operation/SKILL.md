---
name: camera-operation
description: "Execute professional camera operation including exposure control, white balance, focus pulling, frame rate selection, codec configuration, and on-set technical workflows. Use for: setting up cameras for shoots, configuring recording formats, pulling focus on narrative sets, managing media and file structures, operating handheld and stabilized rigs, and troubleshooting technical camera issues."
---

# Camera Operation

Execute professional camera setup, configuration, and operation for video and film production.

## Overview

This skill covers the technical operation of cinema and video cameras — from exposure and white balance through codec selection, media management, and on-set operational workflows. It focuses on the hands-on technical decisions a camera operator or AC makes before and during a shoot.

## Exposure Control Framework

### The Exposure Triangle

| Parameter | Controls | Creative Effect | Typical Range |
|-----------|----------|----------------|---------------|
| ISO / Gain | Sensor sensitivity | Noise floor — lower is cleaner | 100–3200 (cinema), 100–12800 (mirrorless) |
| Shutter Speed / Angle | Motion blur | 180° = natural motion blur | 1/48 for 24fps (180°), 1/50 for 25fps |
| Aperture (T-stop / f-stop) | Depth of field | DOF + light control | T1.3–T22 (cinema), f/1.4–f/22 |

### 180-Degree Shutter Rule

- Standard cinematic motion blur: shutter speed = 1 / (frame rate × 2).
- 24fps → 1/48s (use 1/50 on DSLRs), 30fps → 1/60s, 60fps → 1/120s.
- Faster shutter (e.g., 1/96 = 90°) for staccato action (Saving Private Ryan).
- Slower shutter (e.g., 1/24 = 360°) for dreamy motion blur — rarely used.

### ND Filter Selection

| ND Strength | Stop Reduction | Use When |
|-------------|---------------|----------|
| ND 0.3 (ND2) | 1 stop | Slightly bright — fine tuning |
| ND 0.6 (ND4) | 2 stops | Overcast daylight, open aperture |
| ND 0.9 (ND8) | 3 stops | Bright daylight, wide aperture |
| ND 1.2 (ND16) | 4 stops | Full sun, shallow DOF |
| ND 1.8 (ND64) | 6 stops | Extreme sun, long exposures |
| Variable ND | 1–8 stops | Run-and-gun, unpredictable light |

## White Balance and Color Settings

| Preset | Kelvin Value | Use With |
|--------|-------------|----------|
| Tungsten | 3200K | Indoor tungsten/halogen fixtures |
| Daylight | 5600K | Outdoor sunlight, HMI lights |
| Fluorescent | 4000K (+/- tint) | Office environments |
| Cloudy | 6500K | Overcast skies |
| Custom WB | Measured on gray card | Mixed lighting, precision work |

- Always set WB to the dominant light source and gel mismatched sources.
- Shoot a gray card or color chart at the head of each setup for post reference.
- On cinema cameras, use the built-in color temp + tint controls (green/magenta axis).

## Frame Rate Selection Guide

| Frame Rate | Use Case | Playback Speed at 24fps |
|------------|----------|------------------------|
| 23.976 / 24fps | Standard cinema, narrative | Real time |
| 25fps | PAL broadcast regions | Real time (PAL) |
| 29.97 / 30fps | NTSC broadcast, web content | Real time (NTSC) |
| 48fps | HFR cinema (Hobbit-style) | Real time at 48fps |
| 60fps | Smooth web video, 2.5× slow-mo at 24fps | 40% speed |
| 120fps | Standard slow motion | 20% speed (5× slow) |
| 240fps | Extreme slow motion | 10% speed (10× slow) |

- Higher frame rates require proportionally more light (faster shutter).
- Check sensor crop factor at high frame rates — many cameras crop significantly.

## Recording Codec and Format Guide

| Codec | Type | Bit Depth | Compression | Best For |
|-------|------|-----------|-------------|----------|
| ProRes 422 HQ | Intra-frame | 10-bit | ~18:1 | High-end production, VFX-ready |
| ProRes 422 | Intra-frame | 10-bit | ~25:1 | Standard production, editing |
| ProRes LT | Intra-frame | 10-bit | ~37:1 | Proxy, space-limited shoots |
| H.264 / AVC | Inter-frame (Long GOP) | 8-bit | ~100:1+ | Web delivery, DSLRs |
| H.265 / HEVC | Inter-frame (Long GOP) | 10-bit | ~150:1+ | Efficient delivery, mirrorless |
| BRAW (Blackmagic) | Visually lossless RAW | 12-bit | Variable (3:1–12:1) | Full RAW flexibility, BMPCC |
| R3D (RED) | Wavelet RAW | 16-bit | Variable (2:1–22:1) | VFX, cinema |
| ARRIRAW | Uncompressed RAW | 12/16-bit | ~3.2:1 (open gate) | Highest quality cinema |

### Log vs. Rec.709 Decision

- **Log (S-Log3, C-Log3, V-Log, Log-C):** Captures maximum dynamic range (13–16 stops). Requires color grading. Use for: narrative, commercials, any production with grading pipeline.
- **Rec.709 / Standard:** Ready-to-use color. Less latitude for grading. Use for: live events, news, fast turnaround.
- **LUTs on set:** Apply viewing LUTs on monitor for exposure judgment but record in Log.

## Focus Pulling Workflow

1. **Mark actors' positions** — use tape marks on the floor for start, middle, and end positions.
2. **Measure distances** — use a laser rangefinder or measuring tape from the film plane marker.
3. **Set marks on follow focus ring** — mark distances on the focus wheel disc.
4. **Rehearse** — pull focus during blocking rehearsals before rolling.
5. **Use peaking / punch-in** — enable focus peaking on the AC monitor.
6. **Communicate** — 1st AC and operator coordinate via comms on complex moves.

## Media Management On-Set

- Use **dual card slots** in mirror/backup mode when available.
- Label cards with shoot date, camera letter, card number (e.g., A001_20260401).
- **Offload to two separate drives** before formatting cards.
- Use checksum verification (MHL, Silverstack) to confirm data integrity.
- Never format a card until both copies are verified.
- Maintain a camera report log: roll number, scene, take, lens, notes.

## Camera System Quick Reference

| Camera System | Sensor Size | DR (stops) | Max Resolution | Typical Use |
|---------------|------------|------------|----------------|-------------|
| ARRI ALEXA 35 | Super 35 (open gate) | 17 stops | 4.6K | High-end cinema, TV |
| RED V-RAPTOR | Vista Vision | 16+ stops | 8K | Cinema, VFX-heavy |
| Sony VENICE 2 | Full frame | 16 stops | 8.6K | Cinema, large format |
| Blackmagic URSA Mini 12K | Super 35 | 14 stops | 12K | VFX, indie cinema |
| Canon C70 / C300 III | Super 35 / S35 | 16 stops | 4K/6K | Documentary, corporate |
| Sony FX6 / FX3 | Full frame | 15 stops | 4K | Run-and-gun, doc, hybrid |
| Panasonic GH7 / S5 IIX | M4/3 / Full frame | 13 stops | 5.7K / 6K | Indie, content creation |

## Best Practices

1. **Power up early and test** — boot cameras 30 min before call time, confirm all settings.
2. **Shoot a chart** — color chart and gray card at the top of each setup for post reference.
3. **Monitor with scopes** — waveform for exposure, vectorscope for color, false color for highlights.
4. **Protect highlights** — clipped highlights cannot be recovered. Expose to the right in Log (ETTR).
5. **Communication** — call "rolling", "speed", "mark", "action" consistently for sound sync.
6. **Battery management** — carry 3× expected runtime in batteries, rotate charged spares.

## Using the Reference Files

### When to Read Each Reference

**`/references/fundamentals.md`** — Read when learning exposure theory, sensor basics, or understanding the relationship between ISO, shutter, and aperture for creative and technical control.

**`/references/advanced-techniques.md`** — Read when operating in specialized conditions like high-speed shooting, underwater housings, drone cinematography, or multi-camera synchronized rigs.

**`/references/workflows-best-practices.md`** — Read when designing on-set camera workflows, DIT setups, media management protocols, or standardizing camera reports across a production.

**`/references/troubleshooting.md`** — Read when diagnosing sensor issues (dead pixels, banding), codec playback problems, overheating, or unexpected rolling shutter artifacts.
