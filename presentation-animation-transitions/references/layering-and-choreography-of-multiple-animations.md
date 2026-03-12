## Layering and Choreography of Multiple Animations



### Animation Choreography Principles

When multiple elements animate, coordination becomes crucial:

**Hierarchy**: Animate important elements distinctly from supporting elements
**Grouping**: Related elements should animate together or in close sequence
**Flow**: Eye movement should follow logical patterns (typically left-to-right, top-to-bottom)
**Breathing Room**: Allow pauses between animation groups



### Staggered Animations

Creating cascading effects with delays:

**Bullet Point Stagger**: Each point appears 0.1-0.2 seconds after the previous
**Grid Reveal**: Elements reveal in wave pattern across grid
**Timeline Build**: Sequential points appear along timeline

**Implementation**:
1. Apply same animation to all elements
2. Set first element to desired trigger
3. Set subsequent elements to "After Previous" with incremental delays



### Simultaneous vs. Sequential

**Simultaneous Animations**:
- Elements appearing together indicate equal importance
- Creates dynamic, energetic moments
- Risk of overwhelming viewers

**Sequential Animations**:
- Establishes hierarchy and order
- Guides attention systematically
- Better for complex information

**Hybrid Approach**:
- Group related elements to animate simultaneously
- Sequence groups for progressive disclosure



### Layer Management

Complex animations require attention to visual layering:

- **Z-order**: Elements in front animate independently of those behind
- **Grouping**: Animate grouped objects as single units
- **Backgrounds**: Background elements often shouldn't animate at all
- **Overlapping**: Plan for elements that cross paths during animation

---
