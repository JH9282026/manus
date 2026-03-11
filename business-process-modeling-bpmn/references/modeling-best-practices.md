# Modeling Best Practices

Standards and guidelines for effective process modeling.

---

## Modeling Principles

### Clarity
- One activity per task symbol
- Clear, action-oriented names
- Consistent level of detail
- Avoid crossing flow lines

### Completeness
- Every process has start and end
- All paths lead somewhere
- All gateways merge appropriately
- All exceptions handled

### Consistency
- Follow naming conventions
- Use standard symbols
- Consistent layout patterns
- Uniform level of detail

---

## Naming Conventions

### Activities
- Verb + Noun format
- Action-oriented language
- Specific and clear

**Good:** "Review Application", "Send Confirmation Email"
**Bad:** "Application", "Confirmation"

### Events
- Noun + Past Participle
- Describe the state/condition

**Good:** "Order Received", "Payment Completed"
**Bad:** "Start", "End"

### Gateways
- Question format for decisions
- Clear condition description

**Good:** "Order > $1000?", "Customer Approved?"
**Bad:** "Decision", "Check"

### Pools and Lanes
- Role or organization names
- Nouns, not actions

**Good:** "Customer Service", "Finance Department"
**Bad:** "Process Orders", "Handle Payments"

---

## Layout Guidelines

### Flow Direction
- Left to right (primary)
- Top to bottom (secondary)
- Consistent throughout diagram

### Alignment
- Align related elements
- Consistent spacing
- Balanced distribution

### Swimlane Organization
- Initiator at top/left
- Sequence follows handoffs
- Related roles adjacent

### Size and Spacing
- Consistent element sizes
- Minimum 1 element width spacing
- Room for labels and annotations

---

## Level of Detail

### When to Abstract
- Details not needed for audience
- Sub-process reusable elsewhere
- Diagram becoming cluttered

### When to Expand
- Details critical for understanding
- Training purposes
- Automation requirements

### Balancing Detail

| Audience | Detail Level |
|----------|-------------|
| Executives | L0-L1 (high level) |
| Managers | L1-L2 (process level) |
| Analysts | L2-L3 (detailed) |
| Developers | L3-L4 (executable) |

---

## Common Mistakes

### Gateway Errors
- Missing merge gateway after split
- Wrong gateway type for logic
- Conditions not mutually exclusive
- No default path on exclusive gateway

### Flow Errors
- Sequence flow between pools
- Missing end events
- Orphaned elements
- Crossing message and sequence flows

### Documentation Errors
- Vague activity names
- Missing process metadata
- Inconsistent notation
- No version control

---

## Governance Framework

### Roles and Responsibilities
| Role | Responsibility |
|------|----------------|
| Process Owner | Accountability for process |
| Process Manager | Day-to-day management |
| Process Analyst | Modeling and analysis |
| Process Architect | Standards and governance |

### Review Process
1. Initial draft by analyst
2. Review with process owner
3. Stakeholder validation
4. Technical review (if automation)
5. Approval and publication
6. Periodic review schedule

### Version Control
- Semantic versioning (major.minor.patch)
- Change log maintenance
- Archive previous versions
- Clear current version identification

### Quality Checklist
- [ ] Follows naming conventions
- [ ] All paths complete
- [ ] Appropriate level of detail
- [ ] Gateways properly merged
- [ ] Process metadata documented
- [ ] Stakeholder validated
- [ ] Version controlled
