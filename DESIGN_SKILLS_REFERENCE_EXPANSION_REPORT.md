# Design Workflow Skills — Reference File Expansion Analysis

**Date:** April 3, 2026  
**Repository:** `/home/ubuntu/github_repos/manus/`  

---

## Executive Summary

The 32 design workflow skills are **significantly under-resourced** compared to the rest of the repository. While non-design skills average **4.0 reference files** (median: 4, mode: 4), design skills average only **1.9 reference files** (median: 2.0). Nearly half (15 of 32) have just a **single reference file**, placing them in the bottom 3.4% of all skills by reference count.

**Bottom line:** 23 of 32 design workflow skills need reference file expansion.

---

## Repository-Wide Benchmarks

| Metric | Non-Design Skills (566 typical) | Design Skills (32) | Gap |
|--------|--------------------------------|--------------------|----|
| **Average refs** | 4.0 | 1.9 | −2.1 (53% below) |
| **Median refs** | 4.0 | 2.0 | −2.0 (50% below) |
| **Mode** | 4 | 1 | −3 |
| **Skills with 1 ref** | 19 (3.4%) | 15 (46.9%) | 14× higher rate |
| **Skills with 4+ refs** | 422 (74.6%) | 1 (3.1%) | 24× lower rate |
| **Skills with 5 refs** | 100 (17.7%) | 1 (3.1%) | — |

> **Target benchmark:** A "mature" skill in this repository has **4–5 reference files** totaling **25,000–60,000 bytes** of reference content.

---

## All 32 Skills Ranked by Reference File Count

### 🔴 Critical: 1 Reference File (15 skills)

These skills are in the **bottom 3.4 percentile** of the entire repository.

| # | Skill | Refs | Ref Size | Single Ref File | Content Depth |
|---|-------|------|----------|-----------------|---------------|
| 1 | `design-resources-collection` | 1 | 2,107 B | responsive-design.md | ⚠️ Very thin |
| 2 | `design-workflow-system` | 1 | 2,305 B | detailed-guidelines.md | ⚠️ Very thin |
| 3 | `typography-design-system` | 1 | 4,199 B | typography-system-taskflow.md | Light |
| 4 | `design-accessibility-review` | 1 | 4,323 B | accessibility-audit-taskflow.md | Light |
| 5 | `color-palette-design` | 1 | 4,452 B | color-system-taskflow.md | Light |
| 6 | `design-iteration-workflow` | 1 | 4,548 B | iteration-plan-taskflow-v2-v3.md | Light |
| 7 | `mobile-app-design-patterns` | 1 | 4,630 B | mobile-app-design-taskflow.md | Light |
| 8 | `spacing-rhythm-design` | 1 | 4,785 B | spacing-system-taskflow.md | Light |
| 9 | `design-research-workflow` | 1 | 4,870 B | detailed-guidelines.md | Light |
| 10 | `layout-grid-design` | 1 | 5,296 B | grid-system-taskflow.md | Light |
| 11 | `design-workflow-overview` | 1 | 5,385 B | detailed-guidelines.md | Light |
| 12 | `information-architecture-design` | 1 | 5,725 B | info-architecture-taskflow.md | Light |
| 13 | `wireframing-design` | 1 | 6,365 B | screen-dashboard.md | Moderate |
| 14 | `design-competitive-analysis` | 1 | 6,559 B | competitive-design-analysis-taskflow.md | Moderate |
| 15 | `responsive-web-design` | 1 | 7,432 B | responsive-design-taskflow.md | Moderate |

### 🟡 Below Average: 2 Reference Files (8 skills)

These are below the repository median of 4.

| # | Skill | Refs | Ref Size |
|---|-------|------|----------|
| 16 | `design-scoring-rubric` | 2 | 2,526 B |
| 17 | `imagery-iconography-design` | 2 | 3,287 B |
| 18 | `design-inspiration-gathering` | 2 | 3,674 B |
| 19 | `user-personas-design` | 2 | 3,860 B |
| 20 | `interaction-design-patterns` | 2 | 4,177 B |
| 21 | `design-quality-scoring` | 2 | 4,609 B |
| 22 | `design-review-process` | 2 | 5,145 B |
| 23 | `user-flows-design` | 2 | 5,972 B |

### 🟢 Near Target: 3 Reference Files (8 skills)

These are close to the median but still below the repository mode of 4.

| # | Skill | Refs | Ref Size |
|---|-------|------|----------|
| 24 | `design-handoff-preparation` | 3 | 3,080 B |
| 25 | `ui-component-design` | 3 | 6,143 B |
| 26 | `design-iteration-refinement` | 3 | 7,848 B |
| 27 | `design-resources-library` | 3 | 6,526 B |
| 28 | `design-review-workflow` | 3 | 9,313 B |
| 29 | `grid-layout-design` | 3 | 8,636 B |
| 30 | `spacing-layout-design` | 3 | 7,994 B |
| 31 | `user-flow-design` | 3 | 13,050 B |

### ✅ At Target: 5 Reference Files (1 skill)

| # | Skill | Refs | Ref Size |
|---|-------|------|----------|
| 32 | `design-documentation-specs` | 5 | 5,923 B |

---

## Expansion Recommendations

### Priority 1 — Critical (15 skills with 1 ref): Add 3–4 reference files each

These need immediate expansion. Each has only a single taskflow/guidelines file and lacks the depth for robust agent performance.

| Skill | Current Refs | Target | Files to Add | Suggested Reference Topics |
|-------|-------------|--------|-------------|---------------------------|
| `color-palette-design` | 1 | 4 | 3 | color-theory-fundamentals.md, accessibility-color-contrast.md, brand-color-systems.md |
| `design-accessibility-review` | 1 | 4 | 3 | wcag-checklist-guide.md, screen-reader-testing.md, accessibility-tools-audit.md |
| `design-competitive-analysis` | 1 | 4 | 3 | competitor-audit-framework.md, design-benchmarking.md, ux-heuristic-evaluation.md |
| `design-iteration-workflow` | 1 | 4 | 3 | feedback-synthesis-methods.md, iteration-tracking-tools.md, design-versioning.md |
| `design-research-workflow` | 1 | 4 | 3 | user-research-methods.md, research-synthesis.md, research-repository-ops.md |
| `design-resources-collection` | 1 | 4 | 3 | design-asset-libraries.md, icon-illustration-sources.md, stock-photo-strategy.md |
| `design-workflow-overview` | 1 | 4 | 3 | phase-transition-guide.md, workflow-automation.md, cross-phase-dependencies.md |
| `design-workflow-system` | 1 | 4 | 3 | skill-dependency-map.md, workflow-customization.md, quality-gate-definitions.md |
| `information-architecture-design` | 1 | 4 | 3 | card-sorting-methods.md, navigation-patterns.md, content-hierarchy-models.md |
| `layout-grid-design` | 1 | 4 | 3 | grid-systems-theory.md, breakpoint-strategy.md, grid-in-figma-sketch.md |
| `mobile-app-design-patterns` | 1 | 4 | 3 | ios-hig-patterns.md, android-material-patterns.md, gesture-navigation-design.md |
| `responsive-web-design` | 1 | 4 | 3 | fluid-typography-spacing.md, responsive-images-media.md, container-queries-modern-css.md |
| `spacing-rhythm-design` | 1 | 4 | 3 | spacing-scale-systems.md, vertical-rhythm-guide.md, density-adaptive-layouts.md |
| `typography-design-system` | 1 | 4 | 3 | type-pairing-guide.md, web-font-performance.md, typographic-scale-systems.md |
| `wireframing-design` | 1 | 4 | 3 | lo-fi-vs-hi-fi-wireframes.md, wireframe-annotation-guide.md, wireframe-to-prototype.md |

**Total files to add: ~45 reference files**

### Priority 2 — Below Average (8 skills with 2 refs): Add 2–3 reference files each

| Skill | Current Refs | Target | Files to Add | Suggested Reference Topics |
|-------|-------------|--------|-------------|---------------------------|
| `design-scoring-rubric` | 2 | 4 | 2 | scoring-criteria-deep-dive.md, calibration-exercises.md |
| `imagery-iconography-design` | 2 | 4 | 2 | icon-design-systems.md, image-optimization-guide.md |
| `design-inspiration-gathering` | 2 | 4 | 2 | mood-board-creation.md, design-trend-analysis.md |
| `user-personas-design` | 2 | 4 | 2 | persona-research-methods.md, jobs-to-be-done-mapping.md |
| `interaction-design-patterns` | 2 | 4 | 2 | micro-interaction-catalog.md, animation-principles-ui.md |
| `design-quality-scoring` | 2 | 4 | 2 | quality-metrics-framework.md, scoring-automation.md |
| `design-review-process` | 2 | 4 | 2 | review-critique-methods.md, design-crit-facilitation.md |
| `user-flows-design` | 2 | 4 | 2 | task-analysis-techniques.md, flow-diagramming-tools.md |

**Total files to add: ~16 reference files**

### Priority 3 — Near Target (8 skills with 3 refs): Add 1–2 reference files each (optional)

These are adequate but could be enhanced to match the repository mode of 4.

| Skill | Current Refs | Target | Files to Add |
|-------|-------------|--------|-------------|
| `design-handoff-preparation` | 3 | 4 | 1 |
| `ui-component-design` | 3 | 4 | 1 |
| `design-iteration-refinement` | 3 | 4 | 1 |
| `design-resources-library` | 3 | 4 | 1 |
| `design-review-workflow` | 3 | 4 | 1 |
| `grid-layout-design` | 3 | 4 | 1 |
| `spacing-layout-design` | 3 | 4 | 1 |
| `user-flow-design` | 3 | 4 | 1 |

**Total files to add: ~8 reference files**

---

## Content Depth Concern

Beyond file count, many existing reference files are **undersized**:

| Metric | Design Skill Refs | Mature Repo Skill Refs |
|--------|-------------------|----------------------|
| Avg size per ref file | ~2,900 B | ~8,000–12,000 B |
| Total ref content per skill | ~5,461 B | ~25,000–60,000 B |

Even `design-documentation-specs` with 5 refs only has 5,923 bytes total — a well-developed skill like `angular-framework` has 61,920 bytes across 5 refs. The existing design reference files should also be **expanded in content depth** (target: 8,000–12,000 bytes each).

---

## Summary Action Plan

| Priority | Skills | Files to Add | Effort Estimate |
|----------|--------|-------------|-----------------|
| 🔴 P1: Single-ref skills | 15 | ~45 | High (3–4 hours) |
| 🟡 P2: Two-ref skills | 8 | ~16 | Medium (1–2 hours) |
| 🟢 P3: Three-ref skills | 8 | ~8 | Low (30–60 min) |
| ✅ Already at target | 1 | 0 | None |
| **Total** | **32** | **~69** | **~5–7 hours** |

Additionally, existing reference files should be deepened from ~3–5 KB to ~8–12 KB each.

---

## Answer: Which Skills Need More Reference Files and Why?

**23 of 32 design workflow skills need expansion** (all except `design-documentation-specs`):

1. **15 skills with only 1 reference file** are critically underserved. The repository standard is 4 files — these have 75% fewer references than typical skills. They lack topical breadth (e.g., `color-palette-design` has zero refs on color theory, accessibility contrast, or brand systems).

2. **8 skills with 2 reference files** are below the repository median and miss key supporting topics.

3. **8 skills with 3 reference files** are functional but below the mode of 4, and could benefit from 1 additional file each.

The design skills were created in a batch process that prioritized structural compliance (YAML, formatting, line counts) but didn't generate the same reference depth as skills added through the standard workflow. This makes them structurally sound but **content-thin** compared to peers.
