---
name: "business-process-modeling-bpmn"
description: "Create visual process models using BPMN notation for documentation, analysis, and automation. Use for: process mapping and documentation, BPMN diagram creation, workflow analysis, process improvement, automation requirements, compliance documentation, and process hierarchy design (L0-L4)."
---

# Business Process Modeling & BPMN

Create standardized visual representations of organizational workflows using Business Process Model and Notation (BPMN) for documentation, analysis, and automation.

## Overview

This skill enables creation of process models at various levels of detail—from enterprise process landscapes to detailed executable workflows. Use this for documenting existing processes, designing improvements, supporting digital transformation, or preparing for workflow automation.

## Process Modeling vs Workflow Design

| Aspect | Process Modeling | Workflow Design |
|--------|------------------|-----------------|
| Focus | Understanding current flows | Designing system execution |
| Purpose | Analysis, documentation | Automation, execution |
| Scope | Enterprise or cross-department | Specific bounded workflows |
| Detail | Varies by need | Implementation-ready |
| Audience | Business stakeholders | Technical teams |

## Process Hierarchy Levels

| Level | Name | Scope | Example |
|-------|------|-------|---------|
| L0 | Process Landscape | Enterprise-wide | All major process areas |
| L1 | Process Groups | Major processes | Order-to-Cash |
| L2 | Processes | End-to-end flows | Order Fulfillment |
| L3 | Sub-Processes | Detailed steps | Pick and Pack |
| L4 | Tasks | Individual actions | Scan barcode |

## BPMN Core Elements

### Flow Objects

| Element | Symbol | Purpose |
|---------|--------|---------|
| Start Event | Circle | Process initiation |
| End Event | Bold circle | Process completion |
| Task | Rectangle | Single work unit |
| Gateway | Diamond | Decision/branching |
| Intermediate Event | Double circle | Mid-process event |

### Gateway Types

| Gateway | Purpose | Use When |
|---------|---------|----------|
| Exclusive (XOR) | One path only | Either/or decisions |
| Parallel (AND) | All paths | Concurrent activities |
| Inclusive (OR) | One or more paths | Multiple options possible |
| Event-Based | Wait for events | External triggers |

### Connecting Objects

| Element | Purpose |
|---------|---------|
| Sequence Flow | Shows order of activities |
| Message Flow | Communication between pools |
| Association | Links artifacts to elements |

### Swimlanes

| Element | Purpose |
|---------|---------|
| Pool | Represents participant/organization |
| Lane | Subdivisions within pool (roles/departments) |

## Process Documentation Template

### Process Header
- **Name**: Clear, descriptive title
- **Owner**: Accountable individual
- **Version**: Document version
- **Last Updated**: Date of last revision

### Process Definition
- **Purpose**: Why process exists
- **Scope**: What's included/excluded
- **Triggers**: What initiates process
- **Outputs**: What process produces
- **KPIs**: How success is measured

### RACI Matrix

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| Task 1 | Role A | Role B | Role C | Role D |

## Process Analysis Techniques

| Technique | Purpose | When to Use |
|-----------|---------|-------------|
| Value Stream | Identify waste | Lean improvements |
| Cycle Time | Measure duration | Speed optimization |
| Root Cause | Find problem sources | Issue resolution |
| Capacity | Assess throughput | Scaling decisions |

## Process Improvement Patterns

| Pattern | Problem | Solution |
|---------|---------|----------|
| Elimination | Unnecessary steps | Remove non-value activities |
| Automation | Manual repetition | Automate routine tasks |
| Parallelization | Sequential bottlenecks | Run activities concurrently |
| Standardization | Variation and errors | Create consistent procedures |

## Using the Reference Files

### When to Read Each Reference

**`/references/bpmn-notation.md`** — Read when creating BPMN diagrams, needing element specifications, or designing detailed process flows.

**`/references/process-analysis.md`** — Read when analyzing processes for improvement, conducting value stream analysis, or identifying optimization opportunities.

**`/references/modeling-best-practices.md`** — Read when establishing process modeling standards, creating governance frameworks, or training teams.
