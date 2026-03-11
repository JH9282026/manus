# Dashboard Design

Comprehensive guide to dashboard design, visualization standards, and user experience.

---

## Dashboard Types

### Strategic Dashboards
**Purpose:** High-level KPIs for executives
**Refresh:** Weekly to monthly
**Characteristics:**
- 5-10 key metrics maximum
- Trend indicators (vs. target, vs. prior)
- Exception highlighting
- Minimal interactivity

### Operational Dashboards
**Purpose:** Monitor daily operations
**Refresh:** Daily to real-time
**Characteristics:**
- Current performance status
- Exception alerts
- Action-oriented metrics
- Moderate interactivity

### Analytical Dashboards
**Purpose:** Deep-dive exploration
**Refresh:** On-demand
**Characteristics:**
- Multiple filter options
- Drill-down capabilities
- Cross-filtering
- High interactivity

## Visual Design Principles

### Layout
- Most important information top-left
- Related metrics grouped together
- Consistent alignment and spacing
- Clear visual hierarchy

### Color Usage
- Limit to 5-7 colors
- Use semantic colors (red=bad, green=good)
- Consider colorblind accessibility
- Maintain brand consistency

### Typography
- Maximum 2 font families
- Clear size hierarchy
- Sufficient contrast
- Readable at all sizes

### Whitespace
- Minimum 10-15% whitespace
- Consistent margins and padding
- Visual breathing room
- Avoid clutter

## Chart Selection Guide

### Comparison Charts
| Chart | Use When |
|-------|----------|
| Bar | Comparing categories |
| Column | Time-based comparison |
| Bullet | Actual vs. target |
| Lollipop | Clean category comparison |

### Trend Charts
| Chart | Use When |
|-------|----------|
| Line | Continuous trends |
| Area | Volume over time |
| Sparkline | Compact trend indication |
| Slope | Before/after comparison |

### Part-to-Whole Charts
| Chart | Use When |
|-------|----------|
| Pie | 2-5 categories (use sparingly) |
| Donut | Part-to-whole with center stat |
| Treemap | Hierarchical proportions |
| Stacked Bar | Part-to-whole over categories |

### Distribution Charts
| Chart | Use When |
|-------|----------|
| Histogram | Single variable distribution |
| Box Plot | Distribution comparison |
| Violin | Distribution shape |

### Relationship Charts
| Chart | Use When |
|-------|----------|
| Scatter | Two-variable relationship |
| Bubble | Three variables |
| Heatmap | Matrix relationships |

## KPI Card Design

### Essential Elements
- Metric name (clear, unambiguous)
- Current value (prominent)
- Comparison (vs. target, vs. prior)
- Trend indicator (direction arrow)
- Sparkline (optional context)

### Status Indicators
- Green: On track (>= 100% of target)
- Yellow: At risk (80-99% of target)
- Red: Off track (< 80% of target)

## Interactivity Patterns

### Filters
- Global filters at top
- Context-specific filters near charts
- Clear filter state indication
- Reset option always visible

### Drill-Down
- Consistent drill paths
- Visual indication of drill capability
- Breadcrumb navigation
- Return to summary option

### Cross-Filtering
- Click to filter related charts
- Clear visual feedback
- Consistent behavior
- Reset capability

## Mobile Design

### Responsive Considerations
- Design mobile-first for critical dashboards
- Stack visualizations vertically
- Simplify interactions for touch
- Test on actual devices

### Mobile-Specific
- Larger touch targets (44x44px minimum)
- Simplified navigation
- Key metrics first
- Reduced chart complexity
