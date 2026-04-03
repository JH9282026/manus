# Review Report Examples

Concrete examples of design review reports with findings, scores, and recommendations.

---

## Example: SaaS Dashboard Review

### Summary

**Project**: TaskFlow Dashboard v1
**Overall Score**: 6.5/10
**Quality Level**: Average to Good
**Ready for**: Iteration (1–2 more rounds recommended)

The design shows good foundational work with a clear structure and appropriate color palette. However, it needs work on visual hierarchy, consistency, and some UX improvements.

---

### Strengths

1. **Color palette is well-chosen** — Violet primary feels modern and premium with accessible contrast ratios
2. **Navigation structure is clear** — Sidebar organization makes sense, icons support labels
3. **Card-based layout works well** — Information is chunked appropriately with consistent treatment

### Areas for Improvement

1. **Typography hierarchy needs work**
   - Issue: H2 and H3 look too similar
   - Impact: Medium — reduces scanability
   - Fix: Increase size difference (H2: 28px, H3: 22px) or add weight contrast

2. **Inconsistent spacing**
   - Issue: Card padding varies (16px, 20px, 24px)
   - Impact: Medium — looks unpolished
   - Fix: Standardize to 20px for all cards

3. **Stat cards lack visual hierarchy**
   - Issue: Number and label are similar weight
   - Impact: Low — data readable but could be clearer
   - Fix: Make numbers bolder (700) and larger (32px)

### Critical Issues

1. **No loading states designed**
   - Why critical: Users won't know if system is working
   - Fix: Design skeleton loaders for dashboard, task list
   - Estimate: 2 hours

2. **Mobile navigation not resolved**
   - Why critical: Tab bar items undefined, overflow not handled
   - Fix: Design complete mobile nav with all states
   - Estimate: 3 hours

### Detailed Scores

| Category | Score | Notes |
|----------|-------|-------|
| Visual Design | 7/10 | Good colors, needs hierarchy work |
| User Experience | 6/10 | Clear but missing states |
| Consistency | 5/10 | Spacing inconsistencies |
| Responsiveness | 5/10 | Mobile incomplete |
| Accessibility | 7/10 | Good contrast, needs focus states |
| Brand & Polish | 6/10 | Solid foundation, needs refinement |

**Weighted Total: 6.5/10**

---

### Screen-by-Screen Notes

#### Dashboard
- **Working**: Layout structure, stat cards concept, color usage
- **Issues**: Stat cards need stronger number emphasis; "Welcome" message feels generic
- **Suggestions**: Add personalization (time-based greeting), consider "quick actions" section

#### Project List
- **Working**: Card layout, filtering concept
- **Issues**: Cards look identical (hard to scan), no priority indicator, uneven grid spacing
- **Suggestions**: Add color-coded priority/status, consider list view alternative

#### Task Detail (Modal)
- **Working**: Information organization
- **Issues**: Close button too small, no clear primary action, comments section undefined
- **Suggestions**: Add "Mark Complete" as primary CTA, design empty state for no comments

---

### Recommended Next Steps

**Iteration 1 (Critical)** — Target: 7.5/10
1. Design loading/skeleton states (2h)
2. Complete mobile navigation design (3h)
3. Add focus states to all interactive elements (1h)

**Iteration 2 (Important)** — Target: 8.5/10
1. Refine typography hierarchy (1h)
2. Standardize spacing to 8px scale (1h)
3. Add project status indicators (2h)
4. Design empty states (2h)

**Iteration 3 (Polish)** — Target: 9/10
1. Micro-interaction specifications (2h)
2. Edge cases (error states, long content) (2h)
3. Final accessibility audit (1h)
