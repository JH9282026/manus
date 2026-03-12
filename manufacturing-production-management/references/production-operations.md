# Production Operations

## Production Scheduling

### Scheduling Methods
| Method | Best For | Complexity |
|--------|----------|-----------|
| Forward scheduling | Known start date | Low |
| Backward scheduling | Fixed due date | Low |
| Finite capacity | Constrained resources | High |
| Theory of Constraints | Bottleneck-driven | Medium |

### Master Production Schedule (MPS)
1. Aggregate demand forecast by period
2. Available-to-promise calculation
3. Capacity rough-cut planning
4. Firm planned orders within frozen horizon
5. Weekly review and adjustment

### Production Sequencing Rules
| Rule | Criterion | Best When |
|------|----------|-----------|
| FCFS | First come, first served | Equal priority jobs |
| SPT | Shortest processing time | Minimize average lateness |
| EDD | Earliest due date | Minimize maximum lateness |
| CR | Critical ratio (time remaining/work remaining) | Balance all criteria |

---

## Overall Equipment Effectiveness (OEE)

### OEE Calculation
- **Availability** = Run Time / Planned Production Time
- **Performance** = (Ideal Cycle Time × Total Count) / Run Time
- **Quality** = Good Count / Total Count
- **OEE** = Availability × Performance × Quality

### Six Big Losses
| Loss Category | OEE Factor | Examples |
|--------------|-----------|---------|
| Breakdowns | Availability | Equipment failure, unplanned maintenance |
| Setup/changeover | Availability | Tool changes, material changes |
| Minor stops | Performance | Jams, misfeeds, cleaning |
| Reduced speed | Performance | Worn equipment, suboptimal settings |
| Startup rejects | Quality | Defects during warmup |
| Production rejects | Quality | In-process defects |

### OEE Benchmarks
| Level | OEE | Status |
|-------|-----|--------|
| World Class | >85% | Industry leader |
| Good | 70-85% | Competitive |
| Average | 60-70% | Improvement needed |
| Low | <60% | Significant losses |

---

## Total Productive Maintenance (TPM)

### Eight Pillars
1. Autonomous maintenance (operator-led)
2. Planned maintenance (scheduled PM)
3. Quality maintenance (zero defects)
4. Focused improvement (kaizen)
5. Early equipment management (design for maintainability)
6. Training and education
7. Safety, health, environment
8. Office TPM (administrative improvement)

### Maintenance Strategy Selection
| Equipment Criticality | Strategy | Approach |
|---------------------|----------|----------|
| Critical (stops production) | Predictive + Preventive | Condition monitoring, scheduled PM |
| Important (reduces output) | Preventive | Time/usage-based PM |
| Non-critical (backup available) | Run-to-failure | Replace when broken |

---

## Capacity Planning

### Capacity Calculation
- **Design capacity**: Maximum possible output
- **Effective capacity**: Maximum output accounting for maintenance, changeovers
- **Actual output**: Real production achieved
- **Utilization** = Actual output / Design capacity
- **Efficiency** = Actual output / Effective capacity

### Bottleneck Management (Theory of Constraints)
1. **Identify** the bottleneck (constraint)
2. **Exploit** — Maximize output from constraint
3. **Subordinate** — Align other processes to constraint
4. **Elevate** — Invest to increase constraint capacity
5. **Repeat** — Find next constraint
