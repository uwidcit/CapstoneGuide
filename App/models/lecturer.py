from App.database import db
from .user import User


class Lecturer(User):
    uwi_id = db.Column(db.Integer, unique=True)
    rubrics = db.relationship('Rubric', backref=db.backref('lecturer', lazy='joined'))

    def __init__(self, username, password, email, first_name, last_name, uwi_id):
        super().__init__(username, password, email, first_name, last_name)
        self.uwi_id = uwi_id