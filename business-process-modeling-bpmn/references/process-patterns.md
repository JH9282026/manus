# Process Patterns

Common process patterns and anti-patterns for BPMN modeling.

---

## Sequential Patterns

### Simple Sequence

```
[A] → [B] → [C] → [D]
```

**Use When**: Order matters, dependencies exist between steps

### Conditional Sequence

```
[A] → <XOR> → [Condition met]: [B]
            → [Condition not met]: Skip B
                        ↓
                    <XOR> → [C]
```

**Use When**: Some activities are conditional

---

## Parallel Patterns

### Parallel Split and Synchronization

```
       ┌→ [B] ─┐
[A] → <AND>     <AND> → [E]
       ├→ [C] ─┤
       └→ [D] ─┘
```

**Use When**: Activities are independent and can occur simultaneously

### Generalized AND-Join

**Rule**: Number of AND-joins must equal AND-splits for proper synchronization

---

## Choice Patterns

### Exclusive Choice

```
[A] → <XOR> → [Condition 1]: [B]
            → [Condition 2]: [C]
            → [default]: [D]
```

**Rule**: Conditions must be mutually exclusive

### Multi-Choice (Inclusive)

```
[A] → <OR> → [if X]: [B]
           → [if Y]: [C]
           → [if Z]: [D]
                 ↓
             <OR> → [E]
```

**Use When**: Multiple conditions can be true simultaneously

### Deferred Choice

```
[A] → <Event GW> → ○ Message → [B]
                 → ○ Timer → [C]
                 → ○ Signal → [D]
```

**Use When**: Path depends on external events, not internal conditions

---

## Loop Patterns

### Structured Loop

```
[A] → [B] → <XOR> → [Continue?]: [A]
                  → [Done]: [C]
```

**Use When**: Repeat until condition met

### Multi-Instance (Parallel)

```
[For each item] → [Process Item]Ⅱ → [Collect Results]
```

**Use When**: Process each item in a collection independently

### Multi-Instance (Sequential)

```
[For each item] → [Process Item]═ → [Continue]
```

**Use When**: Must process items in order

---

## Exception Patterns

### Boundary Event Exception

```
┌────────────────┐
│ Process Order    │←Timer
└────────────────┘
         │
         ↓ (if timer fires)
    [Send Reminder]
```

**Use When**: Need alternative path if event occurs during activity

### Error End Event

```
[Task] → <XOR> → [Success]: [Continue]
              → [Error]: (Error End)
```

**Use When**: Need to signal error for higher-level handling

---

## Anti-Patterns

### Spaghetti Flow

**Problem**: Overly complex flows with crossing paths

**Solution**:
- Break into sub-processes
- Simplify logic
- Use link events for off-page connections

### Implicit Termination

**Problem**: Process paths without explicit end events

**Solution**: Always include explicit end events on every path

### Missing Exception Handling

**Problem**: Only modeling the happy path

**Solution**:
- Add boundary events for timeouts
- Include error handling paths
- Model escalation scenarios

### Over-Engineering

**Problem**: Too much detail for the purpose

**Solution**:
- Match detail level to audience
- Use sub-processes to hide complexity
- Reserve L4 detail for automation

### Unbalanced Gateways

**Problem**: Split gateways without matching joins

**Solution**:
- Pair each split with appropriate join
- XOR splits join with XOR
- AND splits join with AND

### Sequence Flows Crossing Pools

**Problem**: Using sequence flows between pools

**Solution**: Use message flows between pools, sequence flows within pools

---

## Pattern Selection Guide

| Scenario | Pattern |
|----------|--------|
| Fixed order of activities | Sequential |
| Independent parallel work | AND split/join |
| One choice from many | XOR gateway |
| Multiple conditions possible | OR gateway |
| Wait for external event | Event-based gateway |
| Repeat until done | Loop |
| Process each item in collection | Multi-instance |
| Handle exceptions | Boundary events |
