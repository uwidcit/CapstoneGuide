from App.database import db
from .user import User


class Lecturer(User):
    __tablename__ = 'lecturer'
    lecturerId = db.Column(db.Integer, unique=True)

    def __init__(self, username, password, email, first_name, last_name, lecturerId):
        super().__init__(username, password, email, first_name, last_name)
        self.lecturerId = lecturerId