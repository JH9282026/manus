## Create User

Creates a new user account.

**Endpoint:** `POST /api/v1/users`

**Authentication:** Bearer token required

**Request Headers:**
| Header | Required | Description |
|--------|----------|-------------|
| Authorization | Yes | Bearer {token} |
| Content-Type | Yes | application/json |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | User email address |
| name | string | Yes | User display name |
| role | string | No | User role (default: "member") |

**Response:** 201 Created
```
