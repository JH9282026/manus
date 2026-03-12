## Color and Contrast Accessibility



### Color Contrast Ratios

WCAG defines specific contrast ratios between text and background colors:

**Level AA Requirements**:
- Normal text (under 18pt or 14pt bold): 4.5:1 minimum contrast ratio
- Large text (18pt+ or 14pt+ bold): 3:1 minimum contrast ratio
- User interface components: 3:1 minimum contrast ratio

**Level AAA Requirements**:
- Normal text: 7:1 minimum contrast ratio
- Large text: 4.5:1 minimum contrast ratio



### Calculating Contrast Ratios

Contrast ratio is calculated using the relative luminance of the foreground and background colors. The formula produces a ratio between 1:1 (no contrast) and 21:1 (maximum contrast—black on white or vice versa).

**High Contrast Examples** (meeting AA standards):
- Black (#000000) on white (#FFFFFF): 21:1
- Dark blue (#003366) on white (#FFFFFF): 12.6:1
- White (#FFFFFF) on dark green (#006600): 6.5:1

**Poor Contrast Examples** (failing AA standards):
- Gray (#777777) on white (#FFFFFF): 4.5:1 (borderline)
- Yellow (#FFFF00) on white (#FFFFFF): 1.07:1 (failing)
- Light blue (#ADD8E6) on white (#FFFFFF): 1.5:1 (failing)



### Color Blindness Considerations

Design for color blindness by following these principles:

**Don't Rely on Color Alone**: Never use color as the only means of conveying information. Add patterns, labels, or icons alongside color coding.

**Problematic Color Combinations**:
- Red and green (affects most color blind users)
- Blue and purple
- Green and brown
- Light green and yellow
- Blue and gray
- Green and gray

**Safe Color Combinations**:
- Blue and orange
- Blue and yellow
- Black and white
- Dark blue and light orange
- Purple and yellow



### Tools for Checking Contrast

**Online Tools**:
- WebAIM Contrast Checker (webaim.org/resources/contrastchecker)
- Contrast Ratio (contrast-ratio.com)
- Accessible Colors (accessible-colors.com)
- Coolors Contrast Checker (coolors.co/contrast-checker)

**Browser Extensions**:
- WAVE Evaluation Tool
- axe DevTools
- Color Contrast Analyzer

**Desktop Applications**:
- Colour Contrast Analyser (by TPGi)
- Sim Daltonism (Mac)
- Color Oracle (Windows, Mac, Linux)

**Presentation Software Tools**:
- PowerPoint Accessibility Checker (built-in)
- Google Slides accessibility extensions



### Not Relying on Color Alone

Ensure all color-coded information has secondary identifiers:

**Charts and Graphs**:
- Add patterns or textures to differentiate data series
- Include direct labels on data points
- Use shape variations (circles, squares, triangles)
- Add a text legend with pattern/shape indicators

**Status Indicators**:
- Combine color with icons (✓ ✗ ⚠)
- Add text labels ("Approved," "Rejected," "Pending")
- Use different shapes for different statuses

**Links and Interactive Elements**:
- Underline links in addition to color
- Add icons to indicate external links
- Provide focus indicators beyond color change

---
