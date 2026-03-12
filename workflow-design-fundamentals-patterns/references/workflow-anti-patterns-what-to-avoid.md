# Workflow Anti Patterns What To Avoid

Detailed reference content for the Workflow Design Fundamentals Patterns skill.

---

## Workflow Anti-Patterns (What to Avoid)


### 1. Spaghetti Workflow

**Problem**: Overly complex flows with crossing paths and unclear logic.

**Symptoms**:
- Difficult to follow visually
- No clear start-to-end path
- Excessive decision points
- Unmaintainable design

**Solution**: Refactor into modular sub-workflows, simplify decision logic.


### 2. Approval Explosion

**Problem**: Too many approval steps for low-risk items.

**Symptoms**:
- Bottlenecks at approval points
- Long cycle times for simple requests
- Approver fatigue
- Rubber-stamping behavior

**Solution**: Risk-based routing, auto-approval for qualifying items.


### 3. Error Black Hole

**Problem**: Errors are caught but not properly handled or reported.

**Symptoms**:
- Items disappear without completion
- No visibility into failures
- Manual investigation required
- Silent data loss

**Solution**: Explicit error handling, dead letter queues, alerting.


### 4. Tight Coupling

**Problem**: Workflows directly dependent on specific systems or implementations.

**Symptoms**:
- Changes require workflow redesign
- Integration failures cascade
- Testing is difficult
- Low reusability

**Solution**: Abstract interfaces, loose coupling, service-oriented design.


### 5. Missing Exit

**Problem**: Workflows without clear completion or termination conditions.

**Symptoms**:
- Instances run indefinitely
- Resource exhaustion
- Unclear status tracking
- Orphaned work items

**Solution**: Define explicit end states, timeout handling, cleanup processes.


### 6. Human-in-the-Loop Bottleneck

**Problem**: Over-reliance on human intervention for routine tasks.

**Symptoms**:
- Queues build up during off-hours
- Single-person dependencies
- Inconsistent processing times
- Scalability limitations

**Solution**: Automate routine decisions, implement rules engines.


### 7. Over-Engineering

**Problem**: Workflow is more complex than the problem requires.

**Symptoms**:
- Features that are never used
- Excessive configuration options
- Long implementation time
- High maintenance burden

**Solution**: Start simple, iterate based on actual needs, YAGNI principle.

---


