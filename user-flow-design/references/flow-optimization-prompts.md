# Flow Optimization Prompts

AI prompts and checklists for identifying, optimizing, and auditing user flows.

---

## Flow Identification Prompt

```
For [PRODUCT] with these personas:
- [Persona 1]: [Primary goal]
- [Persona 2]: [Primary goal]

Identify all user flows organized by:
1. Acquisition (how users first engage)
2. Activation (first value moment)
3. Core (primary daily usage)
4. Retention (what brings them back)
5. Revenue (upgrade/purchase)

For each, rate importance: Critical / Important / Nice-to-have
```

---

## Flow Optimization Prompt

```
Review this user flow:
[FLOW DESCRIPTION]

Identify:
1. Unnecessary steps to remove
2. Decision points that could be eliminated
3. Places where users might get stuck
4. Opportunities for delight
5. Keyboard shortcuts or accelerators
```

---

## Error Flow Design Prompt

```
For the [FLOW NAME] flow, design error handling:
1. What can go wrong at each step?
2. What error message should users see?
3. How can they recover?
4. Should any errors be prevented vs. handled?
```

---

## Flow Quality Checklist

### Minimum Requirements
- [ ] Critical flows identified and mapped
- [ ] Happy path documented for each
- [ ] Decision points clearly marked
- [ ] Error states considered
- [ ] Screen list derived from flows

### Quality Indicators
- [ ] Flows are efficient (minimal steps)
- [ ] Clear entry and exit points
- [ ] Consistent patterns across flows
- [ ] Personas can complete their goals
- [ ] Accessibility considered in flow design
- [ ] Multi-device handoffs documented
- [ ] Metrics defined for each critical flow

---

## Flow Audit Template

Use this to audit an existing product's flows:

```
For [EXISTING PRODUCT]:

1. List all user flows currently supported
2. For each flow, measure:
   - Number of steps to completion
   - Completion rate (if analytics available)
   - Average time to complete
   - Known drop-off points
3. Identify:
   - Flows that are too long (>7 steps)
   - Flows with low completion rates (<60%)
   - Missing flows that users need
   - Redundant flows that can be merged
```

---

## Conversion Funnel Optimization

When optimizing conversion funnels:

1. **Measure each step** — Track entry, progression, and exit at every step
2. **Fix the biggest leak first** — Prioritize the step with highest drop-off
3. **Reduce form fields** — Every field reduces completion by ~7%
4. **Add progress indicators** — Users complete more when they see progress
5. **Provide social proof** — "10,000 teams trust us" at decision points
6. **Enable guest checkout** — Don't force account creation for purchases
7. **Test one change at a time** — Isolate variables to measure impact
