### Deinterlacing

When working with interlaced content, deinterlacing converts to progressive format:

**Methods:**
- **Bob**: Displays each field as full frame (doubles frame rate)
- **Weave**: Combines fields (causes combing on motion)
- **Blend**: Averages fields (causes blur)
- **Adaptive**: Analyzes motion, applies appropriate method
- **IVTC (Inverse Telecine)**: Recovers original 24p from 30i

**Best Practices:**
- Deinterlace before editing when possible
- Use high-quality adaptive algorithms
- Match output frame rate appropriately
- Preview results before batch processing

---
