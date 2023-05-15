from App.database import db


class User(db.Model):
    studentId = db.Column(db.Integer, db.ForeignKey('student.id'))

    def __init__(self, id):
        self.id = id