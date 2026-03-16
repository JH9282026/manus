# DynamoDB Best Practices

Optimizing DynamoDB for performance and cost.

## Access Patterns

```python
# Single-table design
table.put_item(
    Item={
        'PK': f'USER#{user_id}',
        'SK': f'PROFILE#{user_id}',
        'type': 'user',
        'name': 'John',
        'email': 'john@example.com'
    }
)

# Query pattern
response = table.query(
    KeyConditionExpression='PK = :pk AND begins_with(SK, :sk)',
    ExpressionAttributeValues={
        ':pk': f'USER#{user_id}',
        ':sk': 'ORDER#'
    }
)
```

## Cost Optimization

- Use on-demand billing for unpredictable workloads
- Use provisioned capacity for steady workloads
- Enable auto-scaling
- Use DynamoDB Streams instead of polling
- Implement TTL for automatic data expiration
