# Workflow Design Patterns

Detailed reference content for the Workflow Design Fundamentals Patterns skill.

---

## Workflow Design Patterns


### 8. Escalation Pattern

**Description**: Automatically escalates work when conditions are met.

**Structure**:
```
Task Assigned → IF not completed within SLA:
  Notify Manager → IF not resolved:
    Escalate to Director → IF not resolved:
      Executive Review
```

**When to Use**:
- Time-sensitive processes
- SLA management
- Risk mitigation

**Implementation**:
- Define escalation triggers (time, status)
- Specify escalation chain
- Include notification at each level
- Enable de-escalation paths


### 9. Approval Pattern

**Description**: Structured approval process with defined authority levels.

**Variants**:

**Sequential Approval**:
```
Request → Manager Approval → Director Approval → VP Approval
```

**Parallel Approval**:
```
Request → [Legal | Finance | Technical] → Consolidate → Final Decision
```

**Threshold-Based**:
```
Request → IF amount < $1000: Manager
         IF amount < $10000: Director
         ELSE: VP
```

**Best Practices**:
- Define approval criteria clearly
- Include rejection paths with feedback
- Enable delegation and out-of-office handling
- Track approval history


