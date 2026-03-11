# Modeling Methodology

Approaches for conducting process modeling projects.

---

## Process Modeling Project Phases

### Phase 1: Planning

| Activity | Output |
|----------|--------|
| Define scope and objectives | Project charter |
| Identify stakeholders | Stakeholder map |
| Select notation and tools | Standards document |
| Plan workshops | Workshop schedule |
| Gather existing documentation | Document inventory |

### Phase 2: Discovery

| Activity | Output |
|----------|--------|
| Conduct stakeholder interviews | Interview notes |
| Facilitate process workshops | Draft process maps |
| Observe work in practice | Observation notes |
| Review existing systems | System documentation |

### Phase 3: Modeling

| Activity | Output |
|----------|--------|
| Create draft models | BPMN diagrams |
| Document assumptions | Assumptions log |
| Add supporting information | Data objects, annotations |
| Identify pain points | Issue register |

### Phase 4: Validation

| Activity | Output |
|----------|--------|
| Review with process performers | Validated models |
| Test for completeness | Validation report |
| Verify accuracy | Sign-off |
| Document changes | Change log |

### Phase 5: Documentation

| Activity | Output |
|----------|--------|
| Finalize models | Published diagrams |
| Create supporting documents | Process narratives |
| Establish version control | Version history |
| Plan maintenance | Update procedures |

---

## Workshop Facilitation

### Pre-Workshop Preparation

1. **Define scope clearly**
   - Which process?
   - What boundaries?
   - What level of detail?

2. **Identify participants**
   - Process performers (know the reality)
   - Process managers (know the intent)
   - IT representatives (know the systems)
   - Customers (know the outcomes)

3. **Prepare materials**
   - Large paper or whiteboard
   - Sticky notes in different colors
   - Markers
   - Reference documents
   - Existing process documentation

### Workshop Structure

| Time | Activity |
|------|----------|
| 10 min | Introduction and objectives |
| 15 min | Scope confirmation |
| 60 min | Happy path walkthrough |
| 15 min | Break |
| 45 min | Exceptions and variations |
| 15 min | Pain points and issues |
| 15 min | Review and next steps |

### Facilitation Techniques

| Technique | Purpose |
|-----------|--------|
| "Walk me through..." | Get narrative of process |
| "What happens if..." | Explore exceptions |
| "Who decides..." | Identify decision points |
| "How often..." | Understand volumes |
| "What frustrates you..." | Identify pain points |

---

## Remote Collaboration

### Tools for Remote Process Modeling

| Category | Options |
|----------|--------|
| Whiteboarding | Miro, Mural, Lucidspark |
| BPMN Modeling | Camunda Modeler, Bizagi, Lucidchart |
| Video Conference | Zoom, Teams, Google Meet |
| Documentation | Confluence, Notion, SharePoint |

### Remote Workshop Tips

1. Send pre-work to participants
2. Use breakout rooms for parallel discovery
3. Record sessions for reference
4. Take breaks every 45-60 minutes
5. Assign a dedicated note-taker
6. Use visual collaboration tools

---

## Naming Conventions

| Element | Convention | Examples |
|---------|------------|----------|
| Activities | Verb-Noun | Review Application, Send Notification |
| Events | Noun-Verb | Application Received, Timer Expired |
| Gateways | Question | Credit Approved?, Inventory Available? |
| Data Objects | Noun | Customer Order, Invoice |
| Pools | Organization/Role | Customer, Sales Department |
| Lanes | Role/Position | Sales Rep, Manager |

---

## Model Documentation

### Model Metadata

| Field | Content |
|-------|--------|
| Process Name | Unique identifier |
| Process ID | System reference |
| Version | Current version number |
| Status | Draft, Reviewed, Approved, Active, Retired |
| Owner | Accountable person |
| Author | Model creator |
| Created | Creation date |
| Modified | Last modification date |
| Related Documents | Links to procedures, policies |

### Supporting Documentation

| Document | Content |
|----------|--------|
| Process Narrative | Text description of the process |
| Business Rules | Detailed decision logic |
| Data Dictionary | Definition of data elements |
| System References | Systems involved |
| Performance Metrics | KPIs and measurement |
| Compliance Mapping | Regulatory requirements |

---

## Quality Assurance

### Model Review Checklist

**Structural Quality**:
- [ ] All start events have outgoing flows
- [ ] All end events have incoming flows
- [ ] No orphaned elements
- [ ] Gateways properly balanced
- [ ] No deadlocks or livelocks

**Semantic Quality**:
- [ ] Naming conventions followed
- [ ] Decision conditions labeled
- [ ] Roles properly assigned
- [ ] Data objects connected

**Business Quality**:
- [ ] Reflects actual practice
- [ ] Covers all scenarios
- [ ] Exception paths included
- [ ] Validated by performers

### Common Review Findings

| Finding | Resolution |
|---------|------------|
| Missing end events | Add explicit termination |
| Unlabeled conditions | Add condition labels |
| Crossing sequence flows | Restructure or use sub-processes |
| Inconsistent naming | Apply naming conventions |
| Missing exception handling | Add boundary events |
