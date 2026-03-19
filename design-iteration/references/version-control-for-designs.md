# Version Control for Designs

## Overview

Design version control tracks changes over time, enables collaboration, and provides a history of decisions. Proper versioning prevents confusion, enables rollback, and documents the design evolution.

---

## Versioning Schemes

**Semantic Versioning (Major.Minor.Patch)**: 
- Major (1.0, 2.0): Fundamental changes in direction or structure
- Minor (1.1, 1.2): Significant changes to specific areas
- Patch (1.1.1, 1.1.2): Small refinements and fixes

**Date-Based Versioning (YYYY-MM-DD)**: Useful for time-sensitive projects or when changes are continuous. Example: 2026-03-18

**Iteration-Based (v1, v2, v3)**: Simple sequential numbering. Works well for projects with clear iteration milestones.

**Hybrid (v1.2_2026-03-18)**: Combines semantic and date-based. Provides both logical structure and temporal context.

---

## File Naming Conventions

**Structure**: `project-name_component_version_status.ext`

**Examples**:
- `ecommerce_checkout-flow_v2.1_draft.fig`
- `mobile-app_home-screen_v3.0_final.sketch`
- `website_navigation_v1.5_review.xd`

**Status Indicators**:
- `draft`: Work in progress, not ready for review
- `review`: Ready for feedback
- `approved`: Stakeholder approved
- `final`: Ready for development
- `archived`: Superseded by newer version

**Benefits**: Immediately clear what file contains, what version it is, and what state it's in.

---

## Figma Version Control

**Built-in Version History**: Figma automatically saves version history. Access via File > Show version history.

**Named Versions**: Save important milestones with descriptive names. Right-click in version history > 'Save as named version'.

**Branching**: Create branches for experimental work. File > Save to version history > Create branch. Merge back when ready.

**Best Practices**: 
- Save named versions before major changes
- Use descriptive names: 'Pre-stakeholder review' not 'Version 1'
- Create branches for risky experiments
- Review version history before making destructive changes

---

## Git for Design Files

**Why Git for Design**: Provides robust version control, enables branching and merging, integrates with development workflow.

**Challenges**: Binary files don't diff well, large files can bloat repository, merge conflicts are difficult to resolve.

**Solutions**: 
- Use Git LFS (Large File Storage) for design files
- Store source files in Git, export assets separately
- Use Abstract, Kactus, or Plant for design-specific Git workflows
- Establish clear branching strategy (main, develop, feature branches)

**Workflow Example**:
1. Create feature branch: `git checkout -b feature/new-checkout-flow`
2. Make design changes and commit: `git commit -m 'Update checkout flow with new payment options'`
3. Push branch: `git push origin feature/new-checkout-flow`
4. Create pull request for review
5. Merge to main after approval

---

## Design System Versioning

**Component Versioning**: Each component should have its own version number. Allows independent evolution.

**System-Level Versioning**: Overall design system version reflects major releases. Example: 'Design System v3.0'

**Changelog**: Document all changes with each version. Include what changed, why, and migration guidance.

**Deprecation Strategy**: When removing or significantly changing components:
1. Mark as deprecated in current version
2. Provide migration path to replacement
3. Remove in next major version
4. Document in changelog

**Semantic Versioning for Design Systems**:
- Major: Breaking changes requiring design updates
- Minor: New components or non-breaking enhancements
- Patch: Bug fixes and minor refinements

---

## Collaboration and Handoff

**Single Source of Truth**: Designate one file/location as canonical. All other copies are references.

**Access Control**: Use appropriate permissions. Editors can modify, viewers can comment, developers get view-only access to final versions.

**Handoff Packages**: When handing off to development:
- Include final design files
- Export assets in required formats
- Provide specifications (spacing, colors, typography)
- Include version number and date
- Document any known issues or future iterations

**Communication**: Notify stakeholders when new versions are available. Include summary of changes and what requires attention.

---
