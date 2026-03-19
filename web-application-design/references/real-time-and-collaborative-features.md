
### Real-Time Updates

**WebSockets** enable bidirectional communication for live data updates.

**Server-Sent Events** provide efficient one-way real-time data streams.

**Polling** periodically checks for updates when WebSockets aren't feasible.

### Live Data

Real-time dashboards update metrics automatically. Activity feeds display new items as they occur.

Indicate data freshness—timestamps, "Live" indicators, or refresh timing.

### Collaborative Editing

Support multiple users editing simultaneously. Display **presence indicators** showing active collaborators.

**Cursor positions** reveal where others are working. **Selection highlights** show what others have selected.

### Activity Feeds

Display recent actions with actors, actions, and timestamps. Support filtering by activity type or user.

### Presence Indicators

Show online/offline status for team members. Display typing indicators in communication contexts.

### Conflict Resolution

**Last write wins** simplicity suits many scenarios but risks overwriting concurrent changes.

**Operational transformation** enables real-time collaboration by transforming concurrent operations.

**CRDTs** (Conflict-free Replicated Data Types) provide eventual consistency for distributed editing.

---
