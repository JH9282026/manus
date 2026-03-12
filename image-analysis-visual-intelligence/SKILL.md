---
name: "image-analysis-visual-intelligence"
description: "Perceive, understand, extract, manipulate, and analyze images with visual intelligence capabilities including scene comprehension, object detection, emotion recognition, OCR, and image composition. Use for: product image processing, background removal, brand monitoring, accessibility alt-text generation, content moderation, data extraction from images, and visual quality assessment."
---

# Image Analysis & Visual Intelligence

Perceive, understand, extract, and analyze images to produce structured, actionable intelligence from visual content.

## Overview

This skill transforms raw images into structured intelligence — scene understanding, object detection, emotion recognition, text extraction, background removal, and image composition.

## Capability Selection

| Need | Capability | Output | Reference |
|------|-----------|--------|-----------|
| Understand content | Scene Understanding | Classification, context | `/references/visual-perception.md` |
| Find objects | Object Detection | Bounding boxes, labels | `/references/visual-perception.md` |
| Remove backgrounds | Extraction | PNG with transparency | `/references/extraction-composition.md` |
| Read text | OCR | Extracted text, language | `/references/visual-perception.md` |
| Analyze emotions | Sentiment Analysis | Emotion scores, mood | `/references/visual-perception.md` |
| Create composites | Composition | Blended image with shadows | `/references/extraction-composition.md` |
| Describe for accessibility | Alt-text | Short, medium, long desc | `/references/visual-perception.md` |

## Supported Formats
JPEG, PNG, GIF, WebP, TIFF, BMP, HEIC, RAW, PDF, SVG

## Quality Standards
- Detection: 85%+ precision common objects; 90%+ primary subjects
- Segmentation: <2px edge error margin
- OCR: 95%+ printed text; 85%+ handwritten
- Processing: <3s standard; <10s full extraction

## Ethics
- Obtain consent for facial recognition
- Comply with GDPR/CCPA
- Implement bias awareness in demographics
- Avoid discriminatory use of facial analysis

## Using the Reference Files

**`/references/visual-perception.md`** — Read for scene analysis, detection, face analysis, OCR, or accessibility descriptions.

**`/references/extraction-composition.md`** — Read for object extraction, background removal, compositing, or quality assessment.

## Reference Files

This skill includes the following detailed reference materials:

- [Extraction Composition](references/extraction-composition.md)
- [Visual Perception](references/visual-perception.md)
