# Extraction & Composition

## Object Extraction
- Instance segmentation: isolate individual objects
- Background removal with alpha channel
- Edge refinement: standard, high-detail (hair), crisp (hard edges)
- Output: PNG transparent, binary mask, layered PSD

## Image Composition
- Insert objects into new backgrounds
- Perspective, scale, and lighting matching
- Shadow generation for depth
- Color grading to match environment

## Color & Aesthetic Analysis
- Composition: rule of thirds, golden ratio, balance
- Technical: sharpness, exposure, noise
- Artistic: style, lighting quality, visual appeal

## Recommended Tools
| Category | Tools |
|----------|-------|
| Detection | YOLO v8, Faster R-CNN, DETR |
| Segmentation | SAM, Mask R-CNN |
| Face | RetinaFace, ArcFace, DeepFace |
| OCR | Tesseract 5, PaddleOCR, EasyOCR |
| Cloud | Google Vision, AWS Rekognition, Azure CV |
