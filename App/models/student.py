from App.database import db
from .user import User

class Student(User):
    student_id = db.Column(db.Integer, unique=True)

    def __init__(self, username, password, email, first_name, last_name, student_id):
        super().__init__(username, password, email, first_name, last_name)
        self.student_id = student_id