# BPMN Notation

Complete reference for BPMN 2.0 elements and their usage.

---

## Events

### Start Events
| Type | Symbol | Description |
|------|--------|-------------|
| None | Plain circle | General process start |
| Message | Envelope | Started by message receipt |
| Timer | Clock | Started at specific time |
| Conditional | Document | Started when condition met |
| Signal | Triangle | Started by broadcast signal |

### End Events
| Type | Symbol | Description |
|------|--------|-------------|
| None | Bold circle | Process completes |
| Message | Envelope | Sends message on completion |
| Error | Lightning | Error termination |
| Terminate | Filled circle | Immediate process end |
| Escalation | Arrow | Escalate to higher level |

### Intermediate Events
| Type | Description |
|------|-------------|
| Catching | Waits for event to occur |
| Throwing | Triggers event to happen |
| Boundary | Attached to task, handles exceptions |

---

## Tasks

### Task Types
| Type | Symbol | Use When |
|------|--------|----------|
| User Task | Person icon | Human performs work |
| Service Task | Gears | System performs work |
| Script Task | Document | Script executes |
| Business Rule | Table | Rules engine invoked |
| Send Task | Envelope | Message sent |
| Receive Task | Envelope | Wait for message |
| Manual Task | Hand | Offline human work |

### Task Markers
| Marker | Meaning |
|--------|----------|
| Loop | Task repeats |
| Multi-Instance | Multiple executions |
| Compensation | Undo capability |

---

## Gateways

### Exclusive Gateway (XOR)
- Only one outgoing path taken
- Based on conditions on sequence flows
- Use for either/or decisions

**Example:** 
- Approve or Reject
- Pass or Fail

### Parallel Gateway (AND)
- All outgoing paths taken simultaneously
- Waits for all incoming paths before continuing
- Use for concurrent work

**Example:**
- Send email AND update system AND notify manager

### Inclusive Gateway (OR)
- One or more outgoing paths taken
- Based on conditions (at least one must be true)
- Use when multiple options possible

**Example:**
- Notify customer AND/OR update inventory

### Event-Based Gateway
- Waits for one of multiple events
- First event that occurs determines path
- Use for external trigger scenarios

**Example:**
- Wait for customer response OR timeout

---

## Sub-Processes

### Embedded Sub-Process
- Contained within parent process
- Visible in same diagram
- Shares parent's context

### Call Activity
- References reusable process
- Defined separately
- Promotes reuse

### Event Sub-Process
- Triggered by events within parent
- Handles exceptions or interruptions
- Can be interrupting or non-interrupting

---

## Swimlanes

### Pools
- Represent participants in collaboration
- Separate organizations or systems
- Message flows between pools

### Lanes
- Subdivide pools
- Represent roles, departments, systems
- No message flows between lanes (same pool)

### Lane Organization
- Horizontal: Traditional, roles left side
- Vertical: Good for sequential handoffs
- Nested: Sub-lanes for complex organizations

---

## Artifacts

### Data Objects
| Type | Purpose |
|------|----------|
| Data Object | Single instance of data |
| Data Collection | Multiple data instances |
| Data Store | Persistent storage |
| Data Input | Process input |
| Data Output | Process output |

### Annotations
- Text annotations for documentation
- Connect to elements with associations
- Provide additional context

### Groups
- Visual grouping of elements
- No execution semantics
- Documentation purposes

---

## Sequence Flow Rules

### Valid Connections
- Flow objects within same pool
- From events, tasks, gateways
- To events, tasks, gateways

### Invalid Connections
- Between pools (use message flow)
- From end events
- To start events

### Conditional Flows
- Diamond marker on flow
- Condition expression attached
- Evaluated at runtime

### Default Flows
- Slash marker on flow
- Taken when no other condition true
- Used with exclusive/inclusive gateways
