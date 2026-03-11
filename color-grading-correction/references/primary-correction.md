# Primary Color Correction

## Correction Workflow

### Step 1: Normalize Exposure

**Using Waveform**
1. Set black point (lift) to 0-5 IRE
2. Set white point (gain) to 95-100 IRE
3. Adjust midtones (gamma) for overall brightness
4. Check histogram for clipping

**Exposure Issues**
- Underexposed: Raise gain, then gamma
- Overexposed: Lower gain, check for clipping
- Low contrast: Expand lift/gain range
- Flat: Add contrast with S-curve

---

### Step 2: White Balance

**Using RGB Parade**
1. Find neutral reference (white/gray)
2. Align RGB channels at that point
3. Adjust using temperature/tint or RGB balance
4. Verify neutrals appear gray

**Common Color Casts**
- Orange (tungsten): Add blue
- Blue (daylight): Add orange
- Green (fluorescent): Add magenta
- Mixed lighting: Selective correction

---

### Step 3: Contrast Adjustment

**Contrast Controls**

| Tool | Effect |
|------|--------|
| Lift/Gain | Blacks/whites independently |
| Contrast slider | Overall range expansion |
| Curves | Precise tonal control |
| Pivot | Contrast center point |

**Contrast Styles**
- High contrast: Dramatic, bold
- Low contrast: Soft, dreamy
- S-curve: Classic film look
- Linear: Documentary, natural

---

### Step 4: Saturation Balance

**Global Saturation**
- Adjust overall color intensity
- Check skin tones for over-saturation
- Maintain natural appearance

**Saturation by Range**
- Shadows: Often undersaturated
- Highlights: May need reduction
- Midtones: Primary saturation control

---

## Working with LOG Footage

### LOG Normalization

| Camera | LOG Format | Transform |
|--------|------------|----------|
| Sony | S-Log3 | Sony LUT to Rec.709 |
| Canon | C-Log3 | Canon LUT to Rec.709 |
| RED | Log3G10 | RED IPP2 |
| ARRI | LogC | ARRI LUT to Rec.709 |
| Blackmagic | BMD Film | BMD LUT to Rec.709 |

### LOG Workflow Options
1. **LUT-first**: Apply technical LUT, then grade
2. **Manual**: Develop look from LOG directly
3. **ACES**: Color-managed workflow

---

## Color Wheels

### Three-Way Color Correction

| Wheel | Affects | Use For |
|-------|---------|----------|
| Lift | Shadows | Black point, shadow color |
| Gamma | Midtones | Overall color, exposure |
| Gain | Highlights | White point, highlight color |

### Offset/Master
- Affects entire image uniformly
- Useful for overall color shift
- Brightness affects all ranges

---

## Curves

### RGB Curves
- Luma curve: Contrast control
- Red curve: Red/cyan balance
- Green curve: Green/magenta balance
- Blue curve: Blue/yellow balance

### Hue vs. Curves
- Hue vs. Hue: Shift specific hues
- Hue vs. Sat: Saturate specific colors
- Hue vs. Luma: Brighten/darken specific colors
