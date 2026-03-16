# Kanban System Implementation

Complete guide to implementing and optimizing Kanban workflow management systems for continuous flow and delivery.

---

## Kanban Fundamentals

### Origins and Philosophy

Kanban originated from Toyota's manufacturing system in the 1940s as a scheduling system for lean and just-in-time production. The term "kanban" means "visual signal" or "card" in Japanese. David J. Anderson adapted Kanban for knowledge work in the 2000s, creating the Kanban Method for software development and other creative work.

### Core Philosophy

- **Start where you are**: Begin with existing process, no need for reorganization
- **Agree to pursue incremental change**: Evolutionary, not revolutionary change
- **Respect current process, roles, responsibilities**: Preserve what works
- **Encourage leadership at all levels**: Everyone can contribute to improvement

## Six Core Practices of Kanban

### 1. Visualize the Workflow

**Purpose**: Make invisible work visible to understand process and identify issues

**Implementation**:

**Basic Kanban Board Structure**:
```
| Backlog | To Do | In Progress | Review | Done |
|---------|-------|-------------|--------|------|
|  Card   | Card  |    Card     |  Card  | Card |
|  Card   | Card  |    Card     |        | Card |
|  Card   |       |             |        | Card |
```

**Column Design Principles**:
- Reflect actual workflow stages
- Include waiting states (e.g., "Ready for Review," "Waiting for Deployment")
- Make policies for each column explicit
- Use swim lanes for different work types or priorities

**Card Information**:
- Title/description
- Assignee(s)
- Priority/class of service
- Due date (if applicable)
- Blocked status
- Age (days in system)

**Advanced Visualization**:
- **Swim Lanes**: Horizontal rows for different work types (features, bugs, technical debt)
- **Color Coding**: By priority, work type, or team
- **Avatars**: Show who's working on what
- **Blocked Indicators**: Red flags or special markers
- **Aging Indicators**: Highlight cards stuck too long

### 2. Limit Work in Progress (WIP)

**Purpose**: Prevent overload, reduce multitasking, accelerate flow

**Setting Initial WIP Limits**:

**Formula Approaches**:
- **Team-based**: 1.5 × number of team members per stage
- **Per-person**: 1-2 items per person
- **Conservative**: Equal to number of team members
- **Aggressive**: Fewer than team members to force collaboration

**WIP Limit Types**:

1. **Column Limits**: Maximum items in entire column
2. **Per-Person Limits**: Maximum items per individual
3. **CONWIP (Constant WIP)**: Limit across entire board
4. **Upstream Limits**: Limit items committed to delivery
5. **Work Type Limits**: Separate limits for bugs vs. features

**Example WIP Limit Configuration**:
```
| Backlog | To Do (5) | In Progress (3) | Review (2) | Done |
|---------|-----------|-----------------|------------|------|
```

**Adjusting WIP Limits**:

**Increase limits when**:
- Frequent idle time
- Team members waiting for work
- Process efficiency very high (>80%)

**Decrease limits when**:
- Too much multitasking
- Items aging excessively
- Bottlenecks not visible
- Process efficiency low (<40%)

**WIP Limit Violations**:
- Make violations visible (different color, alert)
- Discuss in standup why limit was exceeded
- Swarm to resolve before adding more work
- Track violation frequency as metric

### 3. Manage Flow

**Purpose**: Ensure smooth, continuous, predictable movement through system

**Flow Metrics**:

**Lead Time**:
- Time from request to delivery
- Customer-facing metric
- Includes waiting time before work starts

**Cycle Time**:
- Time from work start to completion
- Team-facing metric
- Excludes backlog waiting time

**Throughput**:
- Number of items completed per time period
- Measured daily, weekly, or monthly
- Indicates team capacity

**Work Item Age**:
- How long item has been in system
- Highlights stuck or aging work
- Trigger for intervention

**Flow Efficiency**:
- Percentage of time spent on value-adding work
- Formula: (Active time / Total lead time) × 100
- Typical knowledge work: 15-20%
- Target: >40%

**Optimizing Flow**:

1. **Reduce Batch Size**: Smaller work items flow faster
2. **Minimize Handoffs**: Fewer transitions between people/stages
3. **Eliminate Waste**: Remove non-value-adding activities
4. **Balance Capacity**: Ensure no stage is consistently overloaded
5. **Reduce Variability**: Standardize work item sizes when possible

### 4. Make Policies Explicit

**Purpose**: Enable self-organization and consistent decision-making

**Policies to Document**:

**Definition of Ready** (for each column):
```
Ready for Development:
- User story written with acceptance criteria
- Designs approved
- Dependencies identified
- Estimated by team
- Priority assigned
```

**Definition of Done** (for each column):
```
Done in Development:
- Code complete and committed
- Unit tests written and passing
- Code reviewed
- No known defects
```

**Pull Criteria**:
- When can work be pulled into next stage?
- Who can pull work?
- What happens if WIP limit is reached?

**Class of Service Policies**:

| Class | Description | WIP Limit | SLA |
|-------|-------------|-----------|-----|
| Expedite | Critical issues, production down | 1 max | 4 hours |
| Fixed Date | Regulatory deadline, commitment | 20% of WIP | By date |
| Standard | Normal features | 70% of WIP | 2 weeks |
| Intangible | Tech debt, research | 10% of WIP | Best effort |

**Blocking Policies**:
- How to mark item as blocked
- How quickly to escalate
- Who resolves different block types
- Maximum time before escalation

### 5. Implement Feedback Loops

**Purpose**: Regular inspection and adaptation for continuous improvement

**Kanban Cadences**:

**Daily Standup** (15 minutes):
- Walk the board from right to left (focus on finishing)
- Identify blockers
- Check WIP limits
- Coordinate for the day

Format: "What's blocked? What's close to done? What needs help?"

**Replenishment Meeting** (Weekly, 1 hour):
- Select new work from backlog
- Prioritize based on class of service
- Ensure sufficient ready work
- Review upcoming commitments

**Service Delivery Review** (Monthly, 2 hours):
- Review delivery metrics (lead time, throughput)
- Analyze flow efficiency
- Discuss customer satisfaction
- Identify improvement opportunities

**Operations Review** (Monthly, 2 hours):
- Review process metrics
- Assess team health and capability
- Discuss strategic direction
- Plan capability improvements

**Retrospective** (Bi-weekly or monthly, 1.5 hours):
- Reflect on process and collaboration
- Identify improvements
- Experiment with changes
- Review previous experiments

### 6. Improve Collaboratively, Evolve Experimentally

**Purpose**: Data-driven, incremental improvement through scientific method

**Improvement Process**:

1. **Observe**: Identify problem or opportunity from data
2. **Hypothesize**: Propose change that might improve situation
3. **Experiment**: Implement change for defined period
4. **Measure**: Collect data on impact
5. **Decide**: Keep, modify, or discard change
6. **Repeat**: Continuous cycle

**Example Experiments**:

**Hypothesis**: Reducing WIP limit in "In Progress" from 5 to 3 will decrease average lead time

**Experiment**:
- Duration: 2 weeks
- Measure: Lead time before and after
- Success criteria: 20% reduction in average lead time

**Types of Improvements**:
- Process changes (new column, different WIP limit)
- Policy changes (new Definition of Done)
- Tool changes (better board, automation)
- Skill development (training, pairing)
- Collaboration changes (new meeting format)

## Identifying and Resolving Bottlenecks

### Bottleneck Indicators

1. **Card Accumulation**: Column consistently at or near WIP limit
2. **Increasing Cycle Time**: Time in specific stage growing
3. **Cumulative Flow Diagram**: Widening band for specific stage
4. **Team Feedback**: Complaints about waiting or overload
5. **Aging Work Items**: Cards stuck in same stage for extended period

### Bottleneck Resolution Strategies

**1. Clarify Exit Criteria**
- Ensure Definition of Done is clear
- Remove ambiguity about when work is complete
- Align understanding across team

**2. Redistribute Capacity**
- Move people to bottleneck stage
- Cross-train team members
- Pair experienced with less experienced

**3. Break Down Work**
- Split large items into smaller pieces
- Reduce batch size
- Enable faster flow through bottleneck

**4. Address Dependencies**
- Identify external dependencies causing delays
- Escalate or find alternatives
- Build slack time into estimates

**5. Adjust WIP Limits**
- Reduce WIP in upstream stages
- Prevent overloading bottleneck
- Force focus on completing work

**6. Automate or Eliminate**
- Automate repetitive tasks in bottleneck stage
- Eliminate non-value-adding activities
- Streamline handoffs

**7. Add Capacity**
- Hire or contract additional resources (last resort)
- Temporary capacity for short-term bottleneck

## Kanban Metrics and Analytics

### Cumulative Flow Diagram (CFD)

**Purpose**: Visualize flow health and identify issues

**Structure**:
- X-axis: Time (days or weeks)
- Y-axis: Number of work items
- Stacked areas: Each workflow stage

**Healthy CFD Characteristics**:
- Smooth, parallel bands
- Consistent vertical distance (stable WIP)
- Steady upward slope (consistent throughput)

**Problem Indicators**:
- Widening band: Bottleneck in that stage
- Flat band: No work in that stage
- Vertical jump: Batch arrival of work
- Narrowing band: Starvation, insufficient work

### Lead Time Distribution

**Purpose**: Understand delivery predictability

**Analysis**:
- Histogram of lead times
- Percentiles (50th, 85th, 95th)
- Use 85th percentile for commitments

**Example**:
- 50% of items: 5 days or less
- 85% of items: 10 days or less
- 95% of items: 15 days or less

Commitment: "We'll deliver in 10 days with 85% confidence"

### Throughput

**Measurement**: Items completed per week/month

**Uses**:
- Capacity planning
- Forecasting completion dates
- Identifying trends

**Forecasting with Throughput**:
- Average throughput: 20 items/week
- Backlog: 100 items
- Forecast: 5 weeks (100 ÷ 20)
- Add buffer for confidence (e.g., 6-7 weeks for 85% confidence)

### Blocked Time

**Measurement**: Percentage of time items are blocked

**Target**: <5% of total time

**Analysis**:
- Track block reasons
- Identify patterns
- Address systemic causes

## Classes of Service

### Purpose

Differentiate work types with different risk profiles, urgency, and business value

### Standard Classes

**Expedite**:
- **Description**: Critical, urgent work (production outages)
- **WIP Limit**: 1 (only one expedite item at a time)
- **SLA**: Immediate (hours)
- **Policy**: Drops everything else, swarm to resolve
- **Percentage**: <5% of work

**Fixed Date**:
- **Description**: Hard deadline (regulatory, contractual)
- **WIP Limit**: 20-30% of total WIP
- **SLA**: Must meet deadline
- **Policy**: Pull early enough to meet date with buffer
- **Percentage**: 10-20% of work

**Standard**:
- **Description**: Normal business value work
- **WIP Limit**: 60-70% of total WIP
- **SLA**: Target lead time (e.g., 2 weeks)
- **Policy**: First-in-first-out within priority
- **Percentage**: 60-70% of work

**Intangible**:
- **Description**: Technical debt, research, improvements
- **WIP Limit**: 10-20% of total WIP
- **SLA**: Best effort, no commitment
- **Policy**: Fill capacity when available
- **Percentage**: 10-20% of work

### Visual Representation

Use swim lanes or color coding:
- Red: Expedite
- Orange: Fixed Date
- Blue: Standard
- Green: Intangible

## Kanban for Different Contexts

### Software Development

**Typical Workflow**:
Backlog → Analysis → Development → Code Review → Testing → Deployment → Done

**Key Practices**:
- Integrate with CI/CD pipeline
- Automate testing and deployment
- Include technical debt swim lane
- Track defect escape rate

### Support/Maintenance

**Typical Workflow**:
Inbox → Triage → Investigation → Resolution → Verification → Closed

**Key Practices**:
- Use classes of service for severity levels
- Track first response time
- Measure resolution time by severity
- Maintain knowledge base

### Marketing

**Typical Workflow**:
Ideas → Planning → Creation → Review → Approval → Publishing → Analysis

**Key Practices**:
- Campaign-based swim lanes
- Track from idea to published
- Measure engagement metrics
- Include creative review cycles

### Personal Kanban

**Simplified Workflow**:
To Do → Doing → Done

**Key Practices**:
- WIP limit of 3-5 items
- Daily review and reprioritization
- Include personal and professional tasks
- Reflect weekly on completion

## Tools for Kanban

### Physical Boards

**Advantages**:
- High visibility
- Tactile, engaging
- Easy to modify
- No technical barriers

**Best Practices**:
- Use whiteboard or corkboard
- Sticky notes for cards
- Tape or string for columns
- Markers for WIP limits
- Place in high-traffic area

### Digital Tools

**Trello**:
- Simple, visual
- Good for small teams
- Limited metrics
- Free tier available

**Jira**:
- Comprehensive features
- Advanced reporting
- Customizable workflows
- Enterprise-grade

**Azure DevOps**:
- Microsoft ecosystem integration
- Built-in CI/CD
- Good for software teams

**LeanKit**:
- Purpose-built for Kanban
- Advanced analytics
- Enterprise features

**Kanbanize**:
- Advanced Kanban features
- Portfolio management
- Analytics and forecasting

**Monday.com**:
- Flexible, visual
- Good for non-technical teams
- Multiple view options

## Kanban vs. Scrum

| Aspect | Kanban | Scrum |
|--------|--------|-------|
| Cadence | Continuous flow | Fixed sprints |
| Roles | No prescribed roles | Product Owner, Scrum Master, Dev Team |
| Commitment | No fixed commitment | Sprint commitment |
| Changes | Anytime | Only between sprints |
| Metrics | Lead time, cycle time, throughput | Velocity, burndown |
| WIP | Limited explicitly | Limited by sprint capacity |
| Board | Persistent | Reset each sprint |
| Best for | Continuous delivery, support | Product development, defined releases |

## Scrumban: Combining Kanban and Scrum

### When to Use Scrumban

- Transitioning from Scrum to Kanban
- Need sprint structure but want flow optimization
- Maintenance teams with some project work
- Teams wanting best of both approaches

### Scrumban Practices

**From Scrum**:
- Sprint planning (optional, or just replenishment)
- Daily standup
- Retrospectives
- Roles (optional)

**From Kanban**:
- Visual board
- WIP limits
- Continuous flow
- Pull system
- Flow metrics

**Typical Implementation**:
- 1-2 week sprints (shorter than typical Scrum)
- Kanban board with WIP limits
- Sprint planning focuses on replenishment
- Can add work mid-sprint if capacity available
- Retrospectives for continuous improvement
- Track both velocity and lead time
