# Flask Extensions Guide

Essential Flask extensions for building production applications.

---

## Database Extensions

### Flask-SQLAlchemy

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://...'
    db.init_app(app)
    return app
```

### Flask-Migrate

```python
from flask_migrate import Migrate

migrate = Migrate(app, db)
```

---

## Authentication Extensions

### Flask-Login

```python
from flask_login import LoginManager, UserMixin, login_user, logout_user

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

### Flask-JWT-Extended

```python
from flask_jwt_extended import JWTManager, create_access_token

jwt = JWTManager(app)
```

---

## API Extensions

### Flask-RESTful

```python
from flask_restful import Api, Resource

api = Api(app)

class UserResource(Resource):
    def get(self, user_id):
        return {'id': user_id}

api.add_resource(UserResource, '/users/<int:user_id>')
```

---

## Validation

### Flask-Marshmallow

```python
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email')
```
