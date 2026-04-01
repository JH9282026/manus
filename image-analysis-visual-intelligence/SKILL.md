---
name: image-analysis-visual-intelligence
description: "Analyze images for content understanding, quality assessment, and visual intelligence extraction. Use for: image content analysis, visual quality assessment, composition evaluation, brand consistency checking, metadata extraction, accessibility alt-text generation, visual sentiment analysis, and automated image categorization."
---

# Image Analysis & Visual Intelligence

Analyze images for content understanding, quality assessment, composition evaluation, and actionable visual intelligence extraction.

## Overview

Image analysis extracts structured information from visual content — identifying objects, assessing quality, evaluating composition, and generating descriptions. This skill covers systematic approaches to visual analysis for marketing, accessibility, content moderation, brand consistency, and creative evaluation. It bridges human visual perception principles with practical analysis frameworks.

## Analysis Type Selection Guide

| Analysis Type | Purpose | Output | Tools/Methods | Reference |
|--------------|---------|--------|---------------|-----------|
| Content identification | What's in the image? | Object list, scene description | Vision AI, manual review | `/references/visual-perception.md` |
| Quality assessment | Is the image technically sound? | Quality score, issues list | Technical metrics, checklist | `/references/visual-perception.md` |
| Composition evaluation | Is it well-composed? | Composition score, suggestions | Design principles analysis | `/references/visual-perception.md` |
| Brand consistency | Does it match brand guidelines? | Compliance checklist | Brand guide comparison | `/references/extraction-composition.md` |
| Accessibility | Can visually impaired users understand? | Alt text, description | Content description frameworks | `/references/extraction-composition.md` |
| Sentiment/mood | What emotion does it convey? | Mood classification | Color psychology, facial analysis | `/references/visual-perception.md` |
| Metadata extraction | Technical image properties | EXIF data, dimensions, format | Metadata readers | `/references/extraction-composition.md` |

## Technical Quality Assessment

### Quality Metrics Checklist

| Metric | Good | Acceptable | Poor | Impact |
|--------|------|-----------|------|--------|
| Resolution | ≥300dpi (print) / ≥72dpi (web) | 150–299dpi / 72dpi | <150dpi / <72dpi | Blurry output |
| Sharpness | Crisp edges, clear details | Slight softness | Visible blur, camera shake | Unprofessional look |
| Exposure | Balanced histogram, detail in highlights/shadows | Slightly over/under | Blown highlights or crushed blacks | Lost information |
| White balance | Neutral whites, accurate skin tones | Slight color cast | Strong color cast | Unnatural appearance |
| Noise/grain | Clean at 100% crop | Slight noise in shadows | Visible noise in midtones | Reduced detail |
| Dynamic range | Detail in both highlights and shadows | Moderate range | Extreme contrast, lost detail | Flat or harsh image |
| Color accuracy | True to life or intentionally styled | Minor shifts | Major color inaccuracies | Misleading representation |

### Format & Size Assessment

| Format | Best For | Max Quality | File Size |
|--------|----------|-------------|-----------|
| JPEG | Photographs, web delivery | 8-bit, lossy | Small–Medium |
| PNG | Graphics, screenshots, transparency | 8/16-bit, lossless | Medium–Large |
| WebP | Web delivery (modern browsers) | 8-bit, lossy/lossless | Small |
| AVIF | Web delivery (newest format) | 10/12-bit, lossy/lossless | Smallest |
| TIFF | Print production, archival | 16-bit, lossless | Very Large |
| RAW | Photography editing (not delivery) | 12/14-bit, unprocessed | Very Large |
| SVG | Icons, logos, illustrations | Vector (infinite) | Small |

## Composition Analysis Framework

| Principle | What to Evaluate | Good Indicator | Poor Indicator |
|-----------|-----------------|----------------|----------------|
| Rule of thirds | Subject placement at intersections | Subject at 1/3 or 2/3 positions | Subject dead center (unless intentional) |
| Leading lines | Lines guiding eye to subject | Lines converge on focal point | Lines leading out of frame |
| Framing | Natural frames around subject | Elements creating depth and focus | Distracting frame elements |
| Balance | Visual weight distribution | Elements balanced across frame | Heavy one side, empty other |
| Negative space | Breathing room around subject | Intentional empty space supports subject | Crowded or wasted space |
| Depth | Foreground/midground/background | Layered elements creating depth | Flat, single-plane composition |
| Color harmony | Color relationships | Complementary or analogous scheme | Clashing or random colors |

## Alt Text Generation Framework

### Alt Text Decision Tree

| Image Context | Alt Text Approach | Example |
|--------------|-------------------|---------|
| Informational (conveys content) | Describe content and purpose | "Bar chart showing Q4 revenue increased 23% YoY" |
| Decorative (visual only) | Empty alt="" | `alt=""` (decorative border image) |
| Functional (button/link) | Describe function, not appearance | "Search" (for magnifying glass icon) |
| Complex (charts, infographics) | Brief alt + long description | alt="Q4 Revenue Summary" + linked detailed description |
| Text in image | Include all text in alt | "Sale: 50% off all winter items through January 31" |

### Alt Text Best Practices
- **Be specific and concise** — 125 characters for simple images, up to 250 for complex
- **Don't start with "Image of" or "Photo of"** — screen readers already announce it's an image
- **Include relevant text** — any text visible in the image must be in the alt text
- **Describe the purpose** — what does this image communicate in this context?
- **Consider the surrounding content** — alt text should complement, not repeat adjacent text

## Brand Consistency Analysis

| Element | Check Against | Compliance Criteria |
|---------|-------------|-------------------|
| Color usage | Brand color palette | Primary/secondary colors within brand guidelines |
| Typography | Brand font list | Approved fonts only, correct usage |
| Logo usage | Logo guidelines | Correct version, clear space, minimum size |
| Photography style | Brand photo guidelines | Lighting, composition, subject matter consistent |
| Tone/mood | Brand personality | Image emotion matches brand values |
| Filter/treatment | Visual style guide | Consistent editing style across assets |

## Batch Image Analysis Workflow

| Step | Action | Output |
|------|--------|--------|
| 1. Inventory | Catalog all images with metadata | Image database with dimensions, format, file size |
| 2. Technical screen | Check resolution, format, file size | Pass/fail list with issues flagged |
| 3. Content classification | Categorize by subject/type | Tagged image library |
| 4. Quality scoring | Rate technical and compositional quality | 1–5 quality scores |
| 5. Brand compliance | Check against brand guidelines | Compliance report with exceptions |
| 6. Accessibility audit | Verify alt text presence and quality | Alt text coverage report |
| 7. Recommendations | Suggest replacements, edits, or removals | Action items per image |

## Visual Sentiment Analysis

| Visual Element | Positive Signals | Negative Signals | Neutral Signals |
|---------------|-----------------|-------------------|-----------------|
| Colors | Warm, bright, saturated | Dark, desaturated, red-heavy | Neutral grays, blues |
| Faces | Smiling, open expressions | Frowning, closed, distressed | Neutral, professional |
| Composition | Open, spacious, balanced | Tight, chaotic, tilted | Centered, structured |
| Lighting | Bright, natural, warm | Dark, harsh shadows, cold | Even, studio-style |
| Subject matter | People, nature, celebration | Conflict, damage, isolation | Objects, architecture |

## Best Practices

- **Analyze with purpose** — define what you're looking for before analyzing; systematic beats random
- **Use checklists** — consistent quality assessment requires a repeatable framework
- **Consider context** — an image's quality depends on where and how it will be used
- **Write alt text for every image** — 96% of the web fails basic image accessibility; don't contribute to this
- **Assess at intended display size** — a photo may look great at 100% but terrible at 300×200px
- **Keep analysis objective** — use measurable criteria (resolution, contrast ratio) alongside subjective assessment

## Using the Reference Files

**`/references/visual-perception.md`** — Read when analyzing image quality, composition, or visual impact. Covers perception principles, quality metrics, composition evaluation, and sentiment analysis frameworks.

**`/references/extraction-composition.md`** — Read when extracting information from images or generating descriptions. Covers alt text frameworks, metadata extraction, brand analysis checklists, and batch processing workflows.
