# Zero-Trust Implementation

Implementing zero-trust security architecture.

## Principles

1. Verify explicitly
2. Use least privilege access
3. Assume breach

## Implementation

```python
def verify_request(event):
    # 1. Verify identity
    user = verify_jwt(event['headers']['Authorization'])
    
    # 2. Verify device
    device = verify_device(event['headers']['X-Device-ID'])
    
    # 3. Verify context
    if not is_allowed_location(event['requestContext']['identity']['sourceIp']):
        raise Exception('Unauthorized location')
    
    # 4. Verify resource access
    if not has_permission(user, event['resource']):
        raise Exception('Insufficient permissions')
    
    return user
```
