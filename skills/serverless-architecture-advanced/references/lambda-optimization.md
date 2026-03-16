# Lambda Optimization

Optimizing AWS Lambda for performance and cost.

## Cold Start Reduction

```python
# Initialize outside handler
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyTable')

def lambda_handler(event, context):
    # Reuse connection
    table.put_item(Item={'id': '123'})
```

## Memory Optimization

Test different memory settings to find optimal cost/performance:
- 512MB: Lowest cost, slower execution
- 1024MB: Balanced
- 1536MB+: Faster execution, higher cost

## Provisioned Concurrency

```yaml
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      ProvisionedConcurrencyConfig:
        ProvisionedConcurrentExecutions: 5
```
