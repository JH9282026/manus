---
name: serverless-architecture-advanced
description: "Master advanced serverless architecture patterns with AWS Lambda, event-driven design, and microservices. Use for: building serverless applications, implementing event-driven architectures, designing Lambda functions, managing API Gateway, orchestrating Step Functions, optimizing cold starts, implementing serverless patterns, cost optimization, and deploying production serverless systems."
---

# Serverless Architecture Advanced

Master advanced serverless patterns, event-driven design, and production-ready serverless systems.

## Overview

Serverless architecture allows building and running applications without managing servers. This skill covers advanced patterns including event-driven design, Lambda optimization, API Gateway integration, Step Functions orchestration, and production best practices for scalable serverless systems.

## When to Use Serverless

| Scenario | Reason | Key Service |
|----------|--------|-------------|
| Variable traffic | Auto-scaling, pay-per-use | AWS Lambda |
| Event processing | Native event integration | EventBridge, SQS |
| API backends | Managed infrastructure | API Gateway |
| Data processing | Parallel execution | Lambda + S3 |
| Scheduled tasks | Cron-like execution | EventBridge |
| Microservices | Independent deployment | Lambda + API Gateway |
| Real-time processing | Stream processing | Lambda + Kinesis |

## AWS Lambda Fundamentals

### Basic Function

```python
import json

def lambda_handler(event, context):
    # Event contains trigger data
    # Context provides runtime information
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Success'})
    }
```

### Environment Variables

```python
import os

def lambda_handler(event, context):
    db_host = os.environ.get('DB_HOST')
    api_key = os.environ.get('API_KEY')
    
    # Use configuration
    return {'statusCode': 200}
```

### Layers

```python
# Layer structure
python/
  lib/
    python3.11/
      site-packages/
        requests/
        boto3/

# Use in function
import requests  # From layer
```

## Event Sources

### API Gateway

```python
def lambda_handler(event, context):
    # HTTP method
    method = event['httpMethod']
    
    # Path parameters
    user_id = event['pathParameters']['id']
    
    # Query parameters
    page = event['queryStringParameters'].get('page', '1')
    
    # Body
    body = json.loads(event['body'])
    
    # Headers
    auth = event['headers'].get('Authorization')
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'user_id': user_id})
    }
```

### S3 Events

```python
def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        # Process file
        s3.download_file(bucket, key, '/tmp/file')
        process_file('/tmp/file')
```

### SQS

```python
def lambda_handler(event, context):
    for record in event['Records']:
        message = json.loads(record['body'])
        
        # Process message
        process_message(message)
        
        # Message automatically deleted on success
```

### EventBridge

```python
def lambda_handler(event, context):
    # Scheduled event
    if event['source'] == 'aws.events':
        run_scheduled_task()
    
    # Custom event
    elif event['source'] == 'custom.app':
        handle_custom_event(event['detail'])
```

## Advanced Patterns

### Fan-Out Pattern

```python
# Publisher Lambda
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    message = {'order_id': '123', 'amount': 100}
    
    sns.publish(
        TopicArn='arn:aws:sns:region:account:orders',
        Message=json.dumps(message)
    )

# Subscriber Lambdas (multiple)
def process_payment(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    # Process payment

def send_notification(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    # Send notification
```

### Saga Pattern (Step Functions)

```json
{
  "StartAt": "ProcessOrder",
  "States": {
    "ProcessOrder": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:...:function:ProcessOrder",
      "Next": "ChargePayment",
      "Catch": [{
        "ErrorEquals": ["States.ALL"],
        "Next": "CancelOrder"
      }]
    },
    "ChargePayment": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:...:function:ChargePayment",
      "Next": "ShipOrder",
      "Catch": [{
        "ErrorEquals": ["States.ALL"],
        "Next": "RefundPayment"
      }]
    },
    "ShipOrder": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:...:function:ShipOrder",
      "End": true
    },
    "RefundPayment": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:...:function:RefundPayment",
      "Next": "CancelOrder"
    },
    "CancelOrder": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:...:function:CancelOrder",
      "End": true
    }
  }
}
```

### CQRS Pattern

```python
# Command (Write)
def create_order(event, context):
    order = json.loads(event['body'])
    
    # Write to DynamoDB
    table.put_item(Item=order)
    
    # Publish event
    eventbridge.put_events(
        Entries=[{
            'Source': 'orders',
            'DetailType': 'OrderCreated',
            'Detail': json.dumps(order)
        }]
    )

# Query (Read)
def get_orders(event, context):
    # Read from optimized read model
    orders = table.query(...)
    return {'statusCode': 200, 'body': json.dumps(orders)}

# Event Handler (Update Read Model)
def update_read_model(event, context):
    order = event['detail']
    # Update read-optimized table
```

## Performance Optimization

### Cold Start Reduction

```python
# Provisioned concurrency
# Set via AWS Console or IaC

# Keep connections warm
import boto3

# Initialize outside handler
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyTable')

def lambda_handler(event, context):
    # Reuse connection
    table.put_item(Item={'id': '123'})
```

### Memory Optimization

```python
# More memory = more CPU
# Test different memory settings: 512MB, 1024MB, 1536MB

# Use /tmp for large files (512MB limit)
import os

def lambda_handler(event, context):
    tmp_file = '/tmp/data.csv'
    s3.download_file('bucket', 'key', tmp_file)
    process_file(tmp_file)
    os.remove(tmp_file)
```

## Security Best Practices

### IAM Roles

```yaml
# Least privilege principle
Resources:
  LambdaExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: LambdaPolicy
          PolicyDocument:
            Statement:
              - Effect: Allow
                Action:
                  - dynamodb:PutItem
                  - dynamodb:GetItem
                Resource: !GetAtt MyTable.Arn
              - Effect: Allow
                Action:
                  - logs:CreateLogGroup
                  - logs:CreateLogStream
                  - logs:PutLogEvents
                Resource: '*'
```

### Secrets Management

```python
import boto3
import json

secrets = boto3.client('secretsmanager')

def get_secret(secret_name):
    response = secrets.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

def lambda_handler(event, context):
    db_creds = get_secret('prod/db/credentials')
    # Use credentials
```

## Monitoring and Observability

### CloudWatch Logs

```python
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('Processing event', extra={'event': event})
    
    try:
        result = process_event(event)
        logger.info('Success', extra={'result': result})
        return result
    except Exception as e:
        logger.error('Error', exc_info=True)
        raise
```

### X-Ray Tracing

```python
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

@xray_recorder.capture('process_order')
def process_order(order_id):
    # Traced automatically
    pass

def lambda_handler(event, context):
    process_order(event['order_id'])
```

## Cost Optimization

1. **Right-size memory**: Test and optimize memory allocation
2. **Use ARM (Graviton2)**: 20% cost reduction
3. **Batch processing**: Process multiple items per invocation
4. **Async invocation**: Use SQS for non-critical paths
5. **Reserved concurrency**: Limit concurrent executions
6. **Lifecycle policies**: Delete old logs and data

## Deployment

### SAM Template

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: app.lambda_handler
      Runtime: python3.11
      CodeUri: ./src
      MemorySize: 512
      Timeout: 30
      Environment:
        Variables:
          TABLE_NAME: !Ref MyTable
      Events:
        Api:
          Type: Api
          Properties:
            Path: /users
            Method: get
```

## Using the Reference Files

### When to Read Each Reference

**`/references/lambda-optimization.md`** — Read when optimizing Lambda performance, reducing cold starts, or managing memory.

**`/references/event-driven-patterns.md`** — Read when designing event-driven architectures, implementing async workflows, or using EventBridge.

**`/references/step-functions-orchestration.md`** — Read when orchestrating complex workflows, implementing sagas, or handling distributed transactions.

## References

- [Event Driven Patterns](references/event-driven-patterns.md)
- [Lambda Optimization](references/lambda-optimization.md)
- [Step Functions Orchestration](references/step-functions-orchestration.md)
