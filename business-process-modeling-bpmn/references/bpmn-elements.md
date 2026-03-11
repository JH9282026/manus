# BPMN Elements

Comprehensive reference for all BPMN 2.0 elements and their proper usage.

---

## Events

### Start Events

| Type | Symbol | Trigger | Example Use Case |
|------|--------|---------|------------------|
| None | Plain thin circle | Unspecified start | Simple process start |
| Message | Envelope in circle | Message receipt | Customer inquiry arrives |
| Timer | Clock in circle | Time/date trigger | Daily batch job |
| Conditional | Lines in circle | Business condition | Inventory below threshold |
| Signal | Triangle in circle | Broadcast signal | System-wide notification |
| Multiple | Pentagon in circle | Any of several | Multiple trigger options |

### Intermediate Events

| Type | Function | Example Use Case |
|------|----------|------------------|
| Message (Catch) | Wait for message | Await customer response |
| Message (Throw) | Send message | Notify external system |
| Timer | Delay/schedule | Wait 24 hours |
| Conditional | Wait for condition | Wait for approval |
| Signal (Catch) | Receive signal | System event received |
| Signal (Throw) | Broadcast signal | Trigger other processes |
| Link | Off-page connector | Large diagram navigation |
| Compensation | Trigger undo | Rollback scenario |
| Escalation | Escalate up | Manager notification |

### End Events

| Type | Result | Example Use Case |
|------|--------|------------------|
| None | Process complete | Normal completion |
| Message | Send message | Confirmation sent |
| Signal | Broadcast signal | Notify subscribers |
| Error | Error thrown | Exception handling |
| Escalation | Escalate up | Unresolved issue |
| Terminate | Kill all paths | Immediate stop |
| Compensation | Trigger compensation | Undo completed work |

### Boundary Events

Attach to activities to trigger alternative paths:

| Type | Interrupting? | Use Case |
|------|---------------|----------|
| Timer (Interrupting) | Yes | Timeout cancels activity |
| Timer (Non-Interrupting) | No | Send reminder, continue |
| Error | Yes | Exception handling |
| Escalation | Variable | Escalation path |
| Message | Variable | Alternative message receipt |

---

## Activities

### Task Types

| Type | Marker | Purpose | Automation |
|------|--------|---------|------------|
| Abstract Task | None | Unspecified work | Manual |
| User Task | Person | Human work in system | System-supported |
| Manual Task | Hand | Work outside system | Fully manual |
| Service Task | Gear | System-to-system call | Automated |
| Script Task | Script | Automated script | Automated |
| Business Rule Task | Table | Decision table execution | Automated |
| Send Task | Filled envelope | Send message | Automated |
| Receive Task | Empty envelope | Wait for message | System-supported |

### Sub-Process Types

| Type | Marker | Purpose |
|------|--------|--------|
| Embedded | + marker | Contained process |
| Collapsed | + marker, minimized | Hidden detail |
| Event Sub-Process | Dashed border | Triggered by events |
| Transaction | Double border | ACID transactions |
| Call Activity | Thick border | Reusable process reference |

### Multi-Instance Activities

| Type | Marker | Behavior |
|------|--------|----------|
| Parallel | Three vertical lines | All instances simultaneously |
| Sequential | Three horizontal lines | One at a time |

---

## Gateways

### Exclusive Gateway (XOR)

**Behavior**: Only one outgoing path taken based on conditions

**Rules**:
- Exactly one path must be selected
- Include default path for unmatched conditions
- Label all outgoing conditions

```
[Task] → <XOR> → [Condition A]: Path A
              → [Condition B]: Path B  
              → [default]: Path C
```

### Parallel Gateway (AND)

**Behavior**: All outgoing paths execute simultaneously; all incoming paths must complete before proceeding

**Rules**:
- Split: All paths activate
- Join: Waits for all incoming paths
- Always pair splits with joins

```
[Task] → <AND> → [Path A]
             → [Path B]
             → [Path C]
                   ↓
             <AND> → [Continue]
```

### Inclusive Gateway (OR)

**Behavior**: One or more outgoing paths taken based on conditions

**Rules**:
- Any combination of paths can be selected
- At least one path must be selected
- Join waits for all selected paths

```
<OR> → [if email]: Email path
     → [if SMS]: SMS path
     → [if push]: Push path
```

### Event-Based Gateway

**Behavior**: Path determined by which event occurs first

**Rules**:
- Only used with catching events
- First event to fire determines path
- Other paths are abandoned

```
<Event GW> → ○ [Message received] → Path A
           → ○ [Timer: 48h] → Path B
           → ○ [Cancel signal] → Path C
```

---

## Swimlanes

### Pools

**Purpose**: Represent participants in a process

**Guidelines**:
- One pool = one participant
- Use black box pools for external parties
- Sequence flows cannot cross pools
- Message flows connect pools

### Lanes

**Purpose**: Subdivide pools to show responsibilities

**Guidelines**:
- Use for roles, departments, or systems
- Arrange logically (hierarchy or flow)
- Keep lane count manageable (3-7)

---

## Artifacts

### Data Objects

| Type | Symbol | Purpose |
|------|--------|--------|
| Data Object | Document icon | Information used/produced |
| Data Input | Arrow into document | Input to process |
| Data Output | Arrow out of document | Output from process |
| Data Collection | Multiple documents | Collection of items |
| Data Store | Cylinder | Persistent storage |

### Groups and Annotations

| Element | Purpose |
|---------|--------|
| Group | Visual grouping for documentation |
| Text Annotation | Additional information notes |
