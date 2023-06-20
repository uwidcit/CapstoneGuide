from datetime import datetime
from App.database import db

class Evaluation(db.Model):
    evaluation_id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposal.proposal_id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey('lecturer.id'))
    novelty = db.Column(db.Integer)
    relevance = db.Column(db.Integer)
    feasibility = db.Column(db.Integer)
    impact = db.Column(db.Integer)
    sustainability = db.Column(db.Integer)
    technologies = db.Column(db.Integer)
    comments = db.Column(db.String)
    score = db.Column(db.Integer, default=None)
    created = db.Column(db.String, default=datetime.utcnow().strftime('%d-%B-%Y')) # 13-May-2023

    def __init__(self, comments, novelty, relevance ,feasibility, impact, sustainability, technologies, proposal_id, reviewer_id):
        self.proposal_id = proposal_id
        self.reviewer_id = reviewer_id
        self.comments = comments
        self.novelty = novelty
        self.relevance = relevance
        self.feasibility = feasibility
        self.score = round((int(novelty) + int(feasibility) + int(impact) + int(technologies) + int(sustainability) + int(relevance)) / 6)
        self.impact = impact
        self.technologies = technologies
        self.sustainability = sustainability

