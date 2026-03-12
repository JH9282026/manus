## Trigger-Action Automation Patterns



### Event Triggers

**Webhook Triggers:**
- Real-time notification via HTTP POST
- Payload contains event data
- Immediate workflow initiation
- Best for: Form submissions, payment events, system notifications

**Scheduled Triggers:**
- Time-based execution (cron-style)
- Recurring patterns (hourly, daily, weekly)
- Best for: Reports, data sync, batch processing

**Polling Triggers:**
- Periodic check for new records/changes
- Platform queries source system on schedule
- Interval typically 1-15 minutes
- Best for: Systems without webhook support

**Application-Specific Triggers:**
- New record created
- Record updated
- Record deleted
- Status changed
- Threshold reached



### Action Types

**Create Actions:**
- Create new records in target systems
- Generate documents, files, or media
- Send messages or notifications
- Initiate new processes

**Update Actions:**
- Modify existing records
- Append data to fields
- Change status or state
- Update relationships

**Delete Actions:**
- Remove records
- Clear data
- Archive or deactivate

**Notify Actions:**
- Send emails, SMS, or push notifications
- Post to chat platforms (Slack, Teams)
- Trigger alerts and escalations



### Conditional Logic and Branching

**Filter Conditions:**
- Continue only if conditions met
- Stop workflow execution otherwise
- Useful for: Data validation, deduplication

**Branching (Paths/Routers):**
- Different paths based on conditions
- Mutually exclusive or parallel execution
- Useful for: Status-based routing, A/B workflows

**Switch/Case Logic:**
- Multiple conditions with different outcomes
- Default/fallback path
- Useful for: Multi-option routing



### Loops and Iterations

**Loop Types:**
- **For Each**: Process each item in a collection
- **While**: Continue until condition is false
- **Do-While**: Execute at least once

**Iteration Considerations:**
- Rate limiting and throttling
- Error handling within loops
- Performance optimization
- Pagination handling



### Error Handling and Retries

**Error Types:**
- **Connection Errors**: Network or authentication failures
- **Data Errors**: Invalid or missing data
- **Rate Limit Errors**: API throttling
- **Logic Errors**: Unexpected conditions

**Handling Strategies:**
- **Automatic Retry**: Exponential backoff for transient errors
- **Error Notifications**: Alert administrators of failures
- **Fallback Actions**: Alternative paths when primary fails
- **Dead Letter Queues**: Store failed items for manual review

---



### REST API Basics for Automation

**HTTP Methods:**
- **GET**: Retrieve data (triggers, lookups)
- **POST**: Create new resources
- **PUT/PATCH**: Update existing resources
- **DELETE**: Remove resources

**Request Components:**
- **Endpoint URL**: Resource location
- **Headers**: Authentication, content type, custom headers
- **Query Parameters**: Filtering, pagination, options
- **Request Body**: Data payload (JSON, XML)

**Response Handling:**
- **Status Codes**: 2xx success, 4xx client error, 5xx server error
- **Response Body**: Data returned by API
- **Pagination**: Handling large result sets
- **Error Messages**: Understanding failure reasons



### Webhooks and Real-Time Triggers

**Webhook Implementation:**
1. Register webhook URL with source system
2. Configure events to trigger notifications
3. Handle incoming POST requests
4. Validate webhook authenticity (signatures)
5. Respond quickly (200 OK) to avoid timeouts
6. Process payload asynchronously if needed

**Webhook Security:**
- Validate signatures (HMAC)
- Verify source IP addresses
- Use HTTPS endpoints
- Implement idempotency for duplicate deliveries



### Orchestration vs. Choreography

**Orchestration:**
- Central controller manages workflow execution
- Explicit sequencing and coordination
- Single point of visibility and control
- Best for: Complex, coordinated processes

**Choreography:**
- Decentralized, event-driven coordination
- Services react to events independently
- No central controller
- Best for: Loosely coupled, scalable systems



### When to Use RPA

**Use RPA When:**
- No API available for target system
- Legacy application integration required
- UI-based interaction is only option
- Process is well-defined and stable
- Volume justifies automation investment

**Avoid RPA When:**
- APIs are available (use integration instead)
- UI changes frequently
- Process requires complex decision-making
- Real-time performance is critical

---
