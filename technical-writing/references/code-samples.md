### Code Samples
Provide examples in multiple languages:

**JavaScript:**
```javascript
const response = await fetch('https://api.example.com/v1/users', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${apiKey}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ email, name })
});
```

**Python:**
```python
import requests

response = requests.post(
    'https://api.example.com/v1/users',
    headers={'Authorization': f'Bearer {api_key}'},
    json={'email': email, 'name': name}
)
```

---
