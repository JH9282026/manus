# Serverless Patterns with AWS Lambda

Advanced patterns and best practices for serverless architectures on AWS.

---

## Lambda Fundamentals

### How Lambda Works

**Execution model**:
1. Event triggers Lambda function
2. AWS provisions execution environment (cold start)
3. Function code executes
4. Environment may be reused for subsequent invocations (warm start)
5. Environment terminated after idle period

**Pricing**:
- Number of requests ($0.20 per 1M requests)
- Duration (GB-seconds of compute time)
- Free tier: 1M requests and 400,000 GB-seconds per month

### Function Configuration

**Runtime**: Node.js, Python, Java, Go, .NET, Ruby, or custom runtime

**Memory**: 128 MB to 10,240 MB (CPU scales proportionally)

**Timeout**: 1 second to 15 minutes

**Environment variables**: Configuration without code changes

**Layers**: Share code and dependencies across functions

---

## Event Sources and Triggers

### Synchronous Invocation

**Characteristics**:
- Caller waits for response
- Error returned directly to caller
- No built-in retry

**Event sources**:
- API Gateway
- Application Load Balancer
- CloudFront (Lambda@Edge)
- Cognito
- Alexa
- Direct invocation (SDK, CLI)

**Use for**: APIs, real-time processing, user-facing applications

### Asynchronous Invocation

**Characteristics**:
- Caller doesn't wait for response
- Lambda queues event and returns immediately
- Automatic retry (2 times)
- Dead Letter Queue (DLQ) for failed events

**Event sources**:
- S3
- SNS
- EventBridge
- SES
- CloudFormation
- CloudWatch Logs

**Use for**: Background processing, event-driven workflows

### Stream-Based Invocation

**Characteristics**:
- Lambda polls stream for records
- Batch processing
- Ordered processing (per shard/partition)
- Automatic retry until success or data expires

**Event sources**:
- Kinesis Data Streams
- DynamoDB Streams
- SQS (standard and FIFO)
- Kafka (MSK, self-managed)

**Use for**: Real-time data processing, change data capture

---

## Serverless Architecture Patterns

### API Backend Pattern

**Components**:
- API Gateway (REST or HTTP API)
- Lambda functions (business logic)
- DynamoDB (data storage)
- Cognito (authentication)

**Architecture**:
```
Client → API Gateway → Lambda → DynamoDB
                ↓
              Cognito (auth)
```

**Best practices**:
- Use HTTP API for lower cost and latency
- Enable caching in API Gateway
- Use Lambda Proxy integration
- Implement request validation
- Use API keys or Cognito for authentication

### Event-Driven Processing

**Components**:
- S3 (file upload)
- Lambda (processing)
- SNS/SQS (notifications/queuing)
- DynamoDB (metadata)

**Example: Image processing**:
```
S3 upload → Lambda (resize) → S3 (thumbnails)
              ↓
            DynamoDB (metadata)
              ↓
            SNS (notification)
```

**Best practices**:
- Use S3 event notifications
- Process large files asynchronously
- Store results in S3, metadata in DynamoDB
- Use SNS for fan-out to multiple consumers

### Stream Processing Pattern

**Components**:
- Kinesis Data Streams (ingestion)
- Lambda (processing)
- S3 or DynamoDB (storage)
- CloudWatch (monitoring)

**Architecture**:
```
Data sources → Kinesis → Lambda → S3/DynamoDB
                           ↓
                      CloudWatch
```

**Best practices**:
- Use batch processing (up to 10,000 records)
- Implement idempotency
- Handle partial batch failures
- Monitor iterator age

### Scheduled Tasks Pattern

**Components**:
- EventBridge (scheduler)
- Lambda (task execution)
- CloudWatch Logs (logging)

**Use cases**:
- Data backups
- Report generation
- Cleanup tasks
- Health checks

**Example**:
```
EventBridge (cron: 0 2 * * ? *) → Lambda (backup) → S3
```

### Fan-Out Pattern

**Components**:
- SNS topic (publisher)
- Multiple Lambda functions (subscribers)
- SQS queues (buffering)

**Architecture**:
```
Event → SNS → Lambda 1 (email)
          ↓
        Lambda 2 (SMS)
          ↓
        Lambda 3 (database)
```

**Use for**: Parallel processing, multiple downstream systems

---

## Best Practices

### Performance Optimization

**Cold start reduction**:
- Use provisioned concurrency for latency-sensitive functions
- Minimize deployment package size
- Use Lambda layers for dependencies
- Choose appropriate runtime (compiled languages faster)
- Keep functions warm with scheduled pings (if cost-effective)

**Memory allocation**:
- More memory = more CPU
- Test different memory settings
- Use AWS Lambda Power Tuning tool
- Monitor CloudWatch metrics

**Code optimization**:
- Initialize SDK clients outside handler (reuse across invocations)
- Use connection pooling for databases
- Minimize dependencies
- Use async/await properly
- Cache data in /tmp (up to 10 GB)

### Error Handling

**Retry strategies**:
- Synchronous: Implement retry in client
- Asynchronous: Configure retry attempts (0-2)
- Stream-based: Automatic retry until success or expiration

**Dead Letter Queues**:
- Configure DLQ for asynchronous invocations
- Use SQS or SNS as DLQ
- Monitor and process failed events
- Set up alarms for DLQ depth

**Error logging**:
- Use structured logging (JSON)
- Include correlation IDs
- Log errors with context
- Use CloudWatch Insights for analysis

### Security Best Practices

**IAM roles**:
- One role per function (least privilege)
- Grant only necessary permissions
- Use resource-based policies for cross-account access
- Avoid wildcard permissions

**Secrets management**:
- Use AWS Secrets Manager or Parameter Store
- Never hardcode secrets
- Cache secrets in memory (with TTL)
- Rotate secrets regularly

**VPC configuration**:
- Use VPC only when necessary (adds cold start latency)
- Use VPC endpoints for AWS services
- Ensure sufficient ENI capacity
- Use security groups for network access control

**Encryption**:
- Encrypt environment variables with KMS
- Use HTTPS for all external calls
- Encrypt data at rest in S3 and DynamoDB

### Cost Optimization

**Right-sizing**:
- Monitor actual memory usage
- Reduce memory if underutilized
- Increase memory if CPU-bound (may reduce duration cost)

**Reduce invocations**:
- Batch processing where possible
- Use SQS to buffer and batch events
- Implement caching (API Gateway, CloudFront, ElastiCache)

**Optimize duration**:
- Minimize cold starts
- Optimize code performance
- Use appropriate runtime
- Reduce deployment package size

**Architecture choices**:
- Use HTTP API instead of REST API (cheaper)
- Use S3 instead of Lambda for static content
- Use Step Functions for long-running workflows (cheaper than Lambda)

---

## Advanced Patterns

### Lambda Layers

**Purpose**: Share code and dependencies across functions

**Use cases**:
- Common libraries (AWS SDK, logging, monitoring)
- Custom runtimes
- Configuration files
- Shared business logic

**Best practices**:
- Version layers
- Keep layers small
- Separate dependencies from code
- Use layers for stable dependencies only

### Lambda Extensions

**Purpose**: Integrate monitoring, security, and governance tools

**Types**:
- Internal extensions (in-process)
- External extensions (separate process)

**Use cases**:
- Custom logging and monitoring
- Secrets caching
- Configuration management
- Security scanning

### Lambda@Edge and CloudFront Functions

**Lambda@Edge**:
- Run Lambda at CloudFront edge locations
- Modify requests and responses
- Use cases: A/B testing, authentication, URL rewriting
- Limitations: 128 MB memory, 5-30 second timeout

**CloudFront Functions**:
- Lightweight JavaScript functions
- Sub-millisecond execution
- Use cases: Header manipulation, URL redirects, simple auth
- Limitations: 2 MB code size, 1 ms timeout

### Step Functions Integration

**Purpose**: Orchestrate complex workflows

**Benefits**:
- Visual workflow designer
- Built-in error handling and retry
- State management
- Long-running workflows (up to 1 year)

**Use cases**:
- Multi-step data processing
- Order fulfillment
- ETL pipelines
- Human approval workflows

**Example workflow**:
```
Start → Lambda (validate) → Lambda (process) → Lambda (notify) → End
                ↓ (error)
              Lambda (handle error)
```

---

## Monitoring and Observability

### CloudWatch Metrics

**Default metrics**:
- Invocations
- Duration
- Errors
- Throttles
- Concurrent executions
- Iterator age (stream-based)

**Custom metrics**:
- Use CloudWatch Embedded Metric Format (EMF)
- Publish custom metrics from function code
- No additional API calls needed

### CloudWatch Logs Insights

**Query examples**:

**Error analysis**:
```
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 20
```

**Performance analysis**:
```
fields @duration
| stats avg(@duration), max(@duration), min(@duration)
```

### X-Ray Tracing

**Benefits**:
- End-to-end request tracing
- Service map visualization
- Performance bottleneck identification
- Error and fault analysis

**Setup**:
1. Enable active tracing on Lambda function
2. Use X-Ray SDK in code
3. View traces in X-Ray console

**Best practices**:
- Trace external API calls
- Add custom subsegments for business logic
- Use annotations for filtering
- Monitor trace sampling rate

---

## Testing and Deployment

### Local Testing

**Tools**:
- AWS SAM CLI (local invoke and API)
- LocalStack (local AWS services)
- Docker (containerized testing)

**Example**:
```bash
sam local invoke MyFunction -e event.json
sam local start-api
```

### CI/CD Pipeline

**Components**:
1. Source control (GitHub, CodeCommit)
2. Build (CodeBuild, GitHub Actions)
3. Test (unit, integration)
4. Deploy (SAM, CloudFormation, Serverless Framework)
5. Monitor (CloudWatch, X-Ray)

**Deployment strategies**:
- All-at-once (simple, downtime risk)
- Canary (gradual rollout, 10% → 100%)
- Linear (incremental, 10% every 10 minutes)
- Blue/green (instant rollback)

### Infrastructure as Code

**AWS SAM**:
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      Runtime: python3.9
      CodeUri: ./src
      Events:
        Api:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

**Serverless Framework**:
```yaml
service: my-service

provider:
  name: aws
  runtime: python3.9

functions:
  hello:
    handler: handler.hello
    events:
      - http:
          path: hello
          method: get
```

---

## Common Anti-Patterns to Avoid

1. **Monolithic functions**: Keep functions small and single-purpose
2. **Synchronous chaining**: Use asynchronous patterns (SQS, SNS, EventBridge)
3. **Recursive invocations**: Can cause runaway costs
4. **Ignoring cold starts**: Use provisioned concurrency for latency-sensitive apps
5. **Over-provisioning memory**: Monitor actual usage and right-size
6. **Not implementing idempotency**: Stream processing must be idempotent
7. **Storing state in /tmp**: Use S3, DynamoDB, or ElastiCache
8. **Not using VPC endpoints**: Reduces cost and improves security
9. **Ignoring concurrency limits**: Monitor and request increases if needed
10. **Not implementing proper error handling**: Use DLQs and alarms
