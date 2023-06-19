from App.database import db

class Rubric(db.Model):
    lecturer_id = db.Column(db.Integer, db.ForeignKey('lecturer.id'))
    id = db.Column(db.Integer, primary_key=True)  # to be used for options(CS, SE, all, etc.)
    name = db.Column(db.String(80))
    novelty = db.Column(db.Integer)
    relevance = db.Column(db.Integer)
    feasibility = db.Column(db.Integer)
    impact = db.Column(db.Integer)
    sustainability = db.Column(db.Integer)
    technology = db.Column(db.Integer)
    notes = db.Column(db.String(80))

    def __init__(self, name, notes, novelty, relevance, feasibility, impact, sustainability, technology, lecturer_id):
        self.name = name.capitalize() 
        self.notes = notes
        self.novelty = novelty
        self.relevance = relevance
        self.feasibility = feasibility
        self.impact = impact
        self.sustainability = sustainability
        self.technology = technology
        self.lecturer_id = lecturer_id
