from App.database import db


class User(db.Model):
    supervisorId = db.Column(db.Integer, db.ForeignKey('supervisor.id'))

    def __init__(self, id):
        self.id = id