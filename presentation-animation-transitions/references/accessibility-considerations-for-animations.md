# Accessibility Considerations For Animations

Detailed reference content for the Presentation Animation Transitions skill.

---

## Accessibility Considerations for Animations


### Motion Sensitivity and Vestibular Disorders

Some viewers experience physical discomfort from screen motion:

**Symptoms**: Dizziness, nausea, headaches, disorientation
**Conditions**: Vestibular disorders, motion sensitivity, migraine susceptibility
**Prevalence**: Estimated 35% of adults over 40 have vestibular dysfunction


### Accessible Animation Guidelines

**Avoid**:
- Parallax effects with large disparities
- Continuous looping animations
- Rapid flashing (three times per second or more)
- Large-scale zooming effects
- Auto-playing motion without user control
- Animations covering large screen areas

**Prefer**:
- Subtle, small-scale animations
- Fade transitions over sliding/zooming
- User-controlled animation triggers
- Option to disable animations
- Animations under 0.5 seconds


### WCAG Guidelines for Motion

Web Content Accessibility Guidelines apply to presentations:

**WCAG 2.3.1 (Level A)**: No content flashing more than three times per second
**WCAG 2.3.3 (Level AAA)**: Animation can be disabled unless essential
**WCAG 2.2.2 (Level A)**: Moving content can be paused, stopped, or hidden


### Providing Alternatives

- **Create static version**: Alternative presentation without animations
- **Offer control**: Allow audience to request reduced motion
- **Announce motion**: Warn verbally before dramatic animations
- **Provide handouts**: Static document for reference


### Testing for Accessibility

When evaluating animations for accessibility:

1. **Motion Intensity Check**: Does any animation cover more than 1/3 of the screen?
2. **Duration Assessment**: Are animations under 5 seconds?
3. **Control Verification**: Can viewers pause or stop motion?
4. **Essential Content Test**: Is information still accessible without animation?
5. **Flicker Analysis**: Any elements flashing rapidly?


### Inclusive Design Approach

Building accessibility into animation from the start:

- Design animations that enhance but aren't required for understanding
- Create progressive enhancement layers
- Test with actual users who have motion sensitivity
- Document which animations are essential vs. decorative
- Provide clear navigation without animation dependency

---


