# Event-Driven Patterns

Implementing event-driven architectures with AWS services.

## Event Sourcing

```python
def handle_order_created(event, context):
    order = event['detail']
    
    # Store event
    events_table.put_item(Item={
        'event_id': str(uuid.uuid4()),
        'event_type': 'OrderCreated',
        'aggregate_id': order['order_id'],
        'data': order,
        'timestamp': datetime.now().isoformat()
    })
    
    # Publish to EventBridge
    eventbridge.put_events(
        Entries=[{
            'Source': 'orders',
            'DetailType': 'OrderCreated',
            'Detail': json.dumps(order)
        }]
    )
```

## Saga Pattern

Coordinate distributed transactions across microservices using Step Functions.
