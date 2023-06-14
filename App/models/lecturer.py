from App.database import db
from .user import User


class Lecturer(User):
    __tablename__ = 'lecturer'
    lecturer_id = db.Column(db.Integer)

    def __init__(self, username, password, email, first_name, last_name, lecturer_id):
        super().__init__(username, password, email, first_name, last_name)
        self.lecturer_id = lecturer_id