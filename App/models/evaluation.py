from typing import Type

from App.database import db

class Evaluation(db.Model):
    proposalId = db.Column(db.Integer, db.ForeignKey('proposal.id'))
    id = db.Column(db.Integer, primary_key=True)
    novelty = db.Column(db.Integer)
    relevance = db.Column(db.Integer)
    feasibility = db.Column(db.Integer)
    score = db.Column(db.Integer)
    impact = db.Column(db.Integer)
    sustainability = db.Column(db.Integer)
    technologies = db.Column(db.Integer)

    def __init__(self, novelty, feasibility, score, impact, sustainability, technologies, proposal_id):
        self.proposalId = proposal_id
        self.novelty = novelty
        self.feasibility = feasibility
        self.score = score
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

