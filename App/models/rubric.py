from App.database import db

class Rubric(db.Model):
    lecturerId = db.Column(db.Integer, db.ForeignKey('lecturer.lecturerId'))
    id = db.Column(db.Integer, primary_key=True)  # to be used for options(CS, SE, all, etc.)
    novelty = db.Column(db.String)
    relevance = db.Column(db.String)
    feasibility = db.Column(db.String)
    notes = db.Column(db.String)
    impact = db.Column(db.String)
    sustainability = db.Column(db.String)
    technologies = db.Column(db.String)

    def __init__(self, novelty, feasibility, notes, impact, sustainability, technologies, lecturerId):
        self.lecturerId = lecturerId
        self.novelty = novelty
        self.feasibility = feasibility
        self.notes = notes
        self.impact = impact
        self.technologies = technologies
        self.sustainability = sustainability

