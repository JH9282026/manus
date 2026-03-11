# Delivery Specifications

## Broadcast Standards

### Safe Levels (Rec.709)

| Parameter | Legal Range | Notes |
|-----------|-------------|-------|
| Luminance | 0-100 IRE | No crushing or clipping |
| Chrominance | -20 to +20 | Check vectorscope |
| RGB | 0-100% | No channel clipping |
| Gamut | Within Rec.709 | No illegal colors |

### QC Checks
- No video levels below 0 IRE
- No video levels above 100 IRE
- No saturation exceeding gamut
- Audio/video sync verified
- Format specifications met

---

## Platform Specifications

### Cinema/Theatrical
- DCI-P3 color space
- 24fps (23.976 for US)
- 2K or 4K resolution
- Full dynamic range
- Maximum quality

### Broadcast TV
- Rec.709 color space
- 25fps (PAL) or 29.97fps (NTSC)
- HD or 4K resolution
- Strict broadcast-safe levels
- Consistent look required

### Web/Streaming
- sRGB or Rec.709
- Various frame rates
- Various resolutions
- SDR or HDR
- Consider compression

### Social Media

| Platform | Aspect | Notes |
|----------|--------|-------|
| YouTube | Various | Supports HDR |
| Instagram | 1:1, 4:5, 9:16 | High compression |
| TikTok | 9:16 | Mobile-first |
| Twitter/X | 16:9, 1:1 | Short-form |

---

## HDR Delivery

### HDR Standards

| Standard | Metadata | Peak Brightness |
|----------|----------|----------------|
| HDR10 | Static | Up to 10,000 nits |
| HDR10+ | Dynamic | Up to 4,000 nits |
| Dolby Vision | Dynamic | Up to 10,000 nits |
| HLG | None | Backward compatible |

### HDR Workflow
1. Grade in HDR-capable environment
2. Master in Dolby Vision or HDR10+
3. Create SDR trim pass
4. Verify on reference HDR display
5. Test on consumer displays

---

## Output Formats

### Master Formats

| Format | Use | Quality |
|--------|-----|----------|
| ProRes 4444 | Master archive | Highest |
| ProRes 422 HQ | Intermediate | Very high |
| DNxHR 444 | Master archive | Highest |
| DPX sequence | Film/archive | Lossless |

### Delivery Formats

| Format | Codec | Use |
|--------|-------|-----|
| H.264 | MP4 | Web, mobile |
| H.265/HEVC | MP4 | 4K, HDR |
| ProRes | MOV | Apple ecosystem |
| VP9 | WebM | YouTube, web |

---

## LUT Delivery

### LUT Package Contents
- Technical LUT (camera to working space)
- Creative LUT (look)
- Combined LUT (full pipeline)
- Documentation and instructions

### LUT Formats

| Format | Compatibility |
|--------|---------------|
| .cube | Universal |
| .3dl | Autodesk, some cameras |
| .look | DaVinci Resolve |
| .mga | Assimilate |
