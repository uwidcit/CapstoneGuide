from datetime import datetime
from App.database import db

class Evaluation(db.Model):
    proposalId = db.Column(db.Integer, db.ForeignKey('proposal.proposalId'))
    id = db.Column(db.Integer, primary_key=True)
    novelty = db.Column(db.Integer)
    relevance = db.Column(db.Integer)
    feasibility = db.Column(db.Integer)
    score = db.Column(db.Integer, default='-')
    impact = db.Column(db.Integer)
    sustainability = db.Column(db.Integer)
    technologies = db.Column(db.Integer)
    created = db.Column(db.String, default=datetime.utcnow().strftime('%d-%B-%Y')) # 13-May-2023

    def __init__(self, novelty, feasibility, score, impact, sustainability, technologies, proposal_id):
        self.proposalId = proposal_id
        self.novelty = novelty
        self.feasibility = feasibility
        self.score = score
        self.impact = impact
        self.technologies = technologies
        self.sustainability = sustainability

