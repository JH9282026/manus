---
name: "business-process-modeling-bpmn"
description: "Create visual representations of business processes using BPMN 2.0 and other notation standards for analysis, improvement, and automation. Use for: process documentation, workflow design, BPMN diagram creation, process analysis and optimization, cross-functional process mapping, process simulation, and business process automation planning."
---

# Business Process Modeling & BPMN

Create visual representations of business processes for analysis, improvement, and automation.

## Overview

Business process modeling captures how work flows through an organization—activities, decisions, resources, and information that transform inputs into outputs. This skill covers BPMN 2.0 notation, process hierarchy levels, cross-functional mapping, and best practices for creating models that support both human understanding and automated execution.

## Why Process Modeling Matters

| Purpose | Benefit |
|---------|---------|
| Organizational Clarity | Documents how work should be performed |
| Process Improvement | Reveals bottlenecks, redundancies, inefficiencies |
| Compliance | Provides auditable evidence for certifications |
| Training | Accelerates employee onboarding |
| Technology Implementation | Ensures technology supports actual needs |
| Communication | Creates shared understanding across stakeholders |

## Process Hierarchy Levels

| Level | Name | Purpose | Detail |
|-------|------|---------|--------|
| L0 | Process Landscape | Enterprise-wide view of major process areas | 5-15 major categories |
| L1 | High-Level Maps | Overview of processes within each L0 area | Major activities and flows |
| L2 | Detailed Process Flows | Comprehensive workflows for analysis | Complete activities, decisions |
| L3 | Procedures | Step-by-step work instructions | Specific guidance for operators |
| L4 | Task Level | Atomic task specifications | Automation-ready detail |

## BPMN 2.0 Core Elements

### Flow Objects

| Element | Shape | Purpose |
|---------|-------|---------|
| Start Event | Thin circle | Where process begins |
| Intermediate Event | Double circle | Occurs between start and end |
| End Event | Thick circle | Where process path ends |
| Task | Rounded rectangle | Unit of work |
| Sub-Process | Rounded rectangle with + | Activity containing other activities |
| Gateway | Diamond | Controls flow divergence/convergence |

### Gateway Types

| Gateway | Symbol | Behavior |
|---------|--------|----------|
| Exclusive (XOR) | X in diamond | One path from multiple options |
| Parallel (AND) | + in diamond | All paths taken simultaneously |
| Inclusive (OR) | O in diamond | One or more paths taken |
| Event-Based | Pentagon in diamond | Path based on which event occurs first |

### Connecting Objects

| Element | Line Style | Purpose |
|---------|------------|---------|
| Sequence Flow | Solid arrow | Shows order of activities |
| Message Flow | Dashed arrow | Communication between pools |
| Association | Dotted line | Connects artifacts to flow objects |

### Swimlanes

| Element | Purpose |
|---------|---------|
| Pool | Represents a participant (organization/role) |
| Lane | Subdivides pool to show responsibilities |

### Events by Type

| Category | Common Types | Use Cases |
|----------|--------------|-----------|
| Start | None, Message, Timer, Conditional | Process triggers |
| Intermediate | Message, Timer, Link, Compensation | Mid-process events |
| End | None, Message, Error, Terminate | Process completion |
| Boundary | Attached to activities | Exception handling |

### Task Types

| Task Type | Marker | Use Case |
|-----------|--------|----------|
| User Task | Person icon | Human work in system |
| Manual Task | Hand icon | Work outside system |
| Service Task | Gear icon | Automated system call |
| Script Task | Script icon | Automated script execution |
| Business Rule Task | Table icon | Decision table execution |
| Send Task | Filled envelope | Send message |
| Receive Task | Empty envelope | Wait for message |

## Process Modeling Best Practices

### Before Modeling

1. **Define scope clearly** — What process, boundaries, detail level
2. **Identify stakeholders** — Who knows the process, who will use the model
3. **Choose appropriate notation** — Match to audience and purpose
4. **Gather existing documentation** — Review current procedures

### During Modeling

1. **Start with happy path** — Document main success scenario first
2. **Walk the process** — Trace through each step mentally or physically
3. **Ask "what happens if"** — Explore exceptions and errors
4. **Capture actual practice** — How work really happens, not idealized
5. **Note pain points** — Mark areas of difficulty or delay

### After Modeling

1. **Validate with participants** — Have performers review for accuracy
2. **Review for completeness** — Check all paths, decisions, end states
3. **Test readability** — Can someone unfamiliar understand it?
4. **Document the model** — Add metadata, version, ownership
5. **Plan for maintenance** — Establish update procedures

## BPMN Patterns

### Common Process Patterns

| Pattern | Structure | Use Case |
|---------|-----------|----------|
| Sequential | A → B → C | Activities in fixed order |
| Parallel Split | A → AND → B + C | Independent simultaneous work |
| Exclusive Choice | A → XOR → B or C | Conditional branching |
| Deferred Choice | A → Event GW → events | Wait for external triggers |
| Loop | A → B → XOR → A or C | Repeat until condition met |
| Multi-Instance | For each item → Process | Process collections |

### Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Spaghetti Flow | Too many crossing paths | Break into sub-processes |
| Implicit Termination | No explicit end events | Add end events |
| Missing Exception Handling | Happy path only | Add boundary events |
| Over-Engineering | Too much detail | Match detail to purpose |
| Single Pool Syndrome | No lane structure | Use lanes for roles |

## BPMN Validation Checklist

### Structural Validation
- [ ] All start events have outgoing flows
- [ ] All end events have incoming flows
- [ ] All activities have both incoming and outgoing flows
- [ ] Gateway splits and joins are balanced
- [ ] No orphaned elements
- [ ] No deadlocks or livelocks

### Semantic Validation
- [ ] Activity names are clear (verb-noun format)
- [ ] Decision conditions are complete and exclusive
- [ ] Swimlane assignments are appropriate
- [ ] Events are correctly typed

### Business Validation
- [ ] Process reflects actual practice
- [ ] All scenarios are covered
- [ ] Exception handling is complete
- [ ] Performance requirements addressed

## Process Notation Comparison

| Notation | Best For | Complexity |
|----------|----------|------------|
| Basic Flowchart | Simple processes, non-technical audiences | Low |
| Swimlane Diagram | Cross-functional processes | Medium |
| BPMN 2.0 | Detailed analysis, automation | High |
| Value Stream Map | Lean manufacturing, waste analysis | Medium |
| UML Activity Diagram | Software development | Medium-High |

## Process Modeling Tools

| Category | Examples |
|----------|----------|
| Enterprise | Bizagi, Signavio, ARIS, IBM Blueworks |
| Open Source | Camunda Modeler, bpmn.io, jBPM |
| Diagramming | Lucidchart, Visio, Draw.io, Miro |

## Using the Reference Files

### When to Read Each Reference

**`/references/bpmn-elements.md`** — Read when creating BPMN diagrams for detailed guidance on all element types, symbols, and proper usage.

**`/references/process-patterns.md`** — Read when designing complex process flows for proven patterns and anti-pattern avoidance.

**`/references/modeling-methodology.md`** — Read when planning process modeling projects for workshop facilitation, validation, and documentation approaches.
