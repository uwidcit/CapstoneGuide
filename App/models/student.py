from App.database import db
from .user import User

class Student(User):
    uwi_id = db.Column(db.Integer, unique=True)
    proposals = db.relationship('Proposal', backref=db.backref('student', lazy='joined'))
 
    def __init__(self, username, password, email, first_name, last_name, uwi_id):
        super().__init__(username, password, email, first_name, last_name)
        self.uwi_id = uwi_id