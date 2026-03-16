# Django REST Framework Authentication

Comprehensive guide to implementing authentication in Django REST Framework.

---

## Authentication Overview

Authentication in DRF identifies the credentials of an incoming request. It runs at the beginning of view processing, before permission and throttling checks.

**Key Concepts:**
- `request.user`: The authenticated user (or `AnonymousUser`)
- `request.auth`: Additional authentication information (e.g., token)

---

## Built-in Authentication Schemes

### 1. BasicAuthentication

HTTP Basic Authentication (username and password in header).

**Configuration:**
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ]
}
```

**Usage:**
```bash
curl -u username:password http://localhost:8000/api/posts/
```

**Pros:**
- Simple to implement
- Good for testing

**Cons:**
- Credentials sent with every request
- Requires HTTPS in production
- Not suitable for browser-based apps

---

### 2. SessionAuthentication

Uses Django's session framework (cookies).

**Configuration:**
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

**CSRF Protection:**
```python
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def my_view(request):
    return Response({'message': 'Success'})
```

**Pros:**
- Works with Django's auth system
- Good for AJAX clients in same session

**Cons:**
- Requires CSRF tokens for unsafe methods
- Not suitable for mobile apps

---

### 3. TokenAuthentication

Simple token-based authentication.

**Setup:**
```python
# settings.py
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

**Generate Tokens:**
```python
# In Django shell or signal
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username='john')
token = Token.objects.create(user=user)
print(token.key)

# Or via signal
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

**Obtain Token Endpoint:**
```python
# urls.py
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/token/', obtain_auth_token),
]
```

**Usage:**
```bash
# Obtain token
curl -X POST -d "username=john&password=secret" http://localhost:8000/api/token/

# Use token
curl -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" http://localhost:8000/api/posts/
```

**Pros:**
- Simple and stateless
- Good for mobile/desktop apps

**Cons:**
- Tokens don't expire by default
- No built-in refresh mechanism

---

## JWT Authentication

### Simple JWT

**Installation:**
```bash
pip install djangorestframework-simplejwt
```

**Configuration:**
```python
# settings.py
from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```

**URLs:**
```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
```

**Usage:**
```bash
# Obtain tokens
curl -X POST -H "Content-Type: application/json" -d '{"username":"john","password":"secret"}' http://localhost:8000/api/token/

# Response:
# {
#   "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
#   "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
# }

# Use access token
curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..." http://localhost:8000/api/posts/

# Refresh token
curl -X POST -H "Content-Type: application/json" -d '{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGc..."}' http://localhost:8000/api/token/refresh/
```

**Custom Claims:**
```python
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
```

---

## OAuth 2.0

### Django OAuth Toolkit

**Installation:**
```bash
pip install django-oauth-toolkit
```

**Configuration:**
```python
# settings.py
INSTALLED_APPS = [
    'oauth2_provider',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ],
}

OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
    },
    'ACCESS_TOKEN_EXPIRE_SECONDS': 3600,
}
```

**URLs:**
```python
from django.urls import path, include

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
```

---

## Custom Authentication

```python
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_X_API_KEY')
        
        if not token:
            return None
        
        try:
            user = User.objects.get(profile__api_key=token)
        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid token')
        
        return (user, None)
```

**Usage:**
```python
from rest_framework.views import APIView
from rest_framework.response import Response

class MyView(APIView):
    authentication_classes = [CustomTokenAuthentication]
    
    def get(self, request):
        return Response({'message': f'Hello {request.user.username}'})
```

---

## Per-View Authentication

```python
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import TokenAuthentication

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def my_view(request):
    return Response({'message': 'Success'})

# Class-based view
from rest_framework.views import APIView

class MyView(APIView):
    authentication_classes = [TokenAuthentication]
    
    def get(self, request):
        return Response({'message': 'Success'})
```

---

## Permissions

### Built-in Permissions

```python
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    AllowAny,
)

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
```

### Custom Permissions

```python
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
```

---

## Security Best Practices

1. **Use HTTPS**: Always use HTTPS in production
2. **Token Expiry**: Implement token expiration and refresh
3. **Rate Limiting**: Use throttling to prevent abuse
4. **CORS**: Configure CORS properly for browser clients
5. **Secure Storage**: Never store tokens in localStorage (use httpOnly cookies)
6. **Validate Input**: Always validate and sanitize user input
7. **Audit Logs**: Log authentication attempts and failures

---

## Throttling

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
    }
}

# Custom throttle
from rest_framework.throttling import UserRateThrottle

class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'

class SustainedRateThrottle(UserRateThrottle):
    scope = 'sustained'

# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'burst': '60/min',
        'sustained': '1000/day',
    }
}
```

---

## Testing Authentication

```python
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class AuthenticationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('john', 'john@example.com', 'password')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
    
    def test_authentication_required(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 401)
    
    def test_token_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)
    
    def test_jwt_authentication(self):
        response = self.client.post('/api/token/', {
            'username': 'john',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
```
