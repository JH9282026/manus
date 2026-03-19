# Flask Blueprints Architecture

Comprehensive guide to structuring Flask applications with blueprints.

---

## Blueprint Basics

Blueprints are Flask's way of organizing applications into modular components.

```python
from flask import Blueprint

# Create blueprint
bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/')
def index():
    return 'Main page'

# Register in app
app.register_blueprint(bp)
```

---

## Application Structure

```
myapp/
├── app/
│   ├── __init__.py          # Application factory
│   ├── models.py            # Database models
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py        # Auth routes
│   │   └── forms.py         # Auth forms
│   ├── api/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── posts.py
│   └── main/
│       ├── __init__.py
│       └── routes.py
├── config.py
├── requirements.txt
└── run.py
```

---

## Modular Blueprint Example

```python
# app/auth/__init__.py
from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

from . import routes

# app/auth/routes.py
from . import auth_bp
from flask import request, jsonify

@auth_bp.route('/login', methods=['POST'])
def login():
    return jsonify({'token': 'abc123'})

# app/__init__.py
def create_app():
    app = Flask(__name__)
    
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    
    return app
```
