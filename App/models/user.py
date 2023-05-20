from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    user_role = db.Column(db.Boolean(False))
    email = db.Column(db.String, nullable=False, unique=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    def __init__(self, id, first_name, last_name, password, user_role, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = first_name + "." + last_name
        self.set_password(password)
        self.user_role = user_role
        self.email = email

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='scrypt`')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def set_supervisor(self):
        self.user_role = True
