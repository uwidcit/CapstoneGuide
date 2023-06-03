from App.database import db

class Rubric(db.Model):
    supervisorId = db.Column(db.Integer, db.ForeignKey('supervisor.id'))
    id = db.Column(db.Integer, primary_key=True)  # to be used for options(CS, SE, all, etc.)
    novelty = db.Column(db.String)
    relevance = db.Column(db.String)
    feasibility = db.Column(db.String)
    notes = db.Column(db.String)
    impact = db.Column(db.String)
    sustainability = db.Column(db.String)
    technologies = db.Column(db.String)

    def __init__(self, novelty, feasibility, notes, impact, sustainability, technologies, supervisorId):
        self.supervisorId = supervisorId
        self.novelty = novelty
        self.feasibility = feasibility
        self.notes = notes
        self.impact = impact
        self.technologies = technologies
        self.sustainability = sustainability

# Sample Code
    """
    def __repr__(self):
        return f'<listing {self.listingId} for ${self.price}>'

    def toJSON_with_game(self):
        return{
            'listingId': self.listingId,
            'ownerId': self.ownerId,
            'condition': self.condition,
            'price': self.price,
            'status': self.status,
            'created': self.created.strftime("%Y/%m/%d, %H:%M:%S"),
            'game': self.game.toJSON(),
        }

    def toJSON(self):
        return{
            'title': self.game.title,
            'owner': self.ownerId,
            'condition': self.condition,
            'price': self.price,
            'created': self.created.strftime("%Y/%m/%d, %H:%M:%S"),
            'status': self.status
        }
    """

