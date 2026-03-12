### Error Codes and Messages
Document all possible errors:

| Code | Status | Description | Resolution |
|------|--------|-------------|------------|
| 400 | Bad Request | Invalid request format | Check request body syntax |
| 401 | Unauthorized | Invalid or missing token | Verify your API key |
| 404 | Not Found | Resource doesn't exist | Verify the resource ID |
| 429 | Rate Limited | Too many requests | Implement backoff strategy |
