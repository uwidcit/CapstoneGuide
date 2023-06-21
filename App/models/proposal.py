from App.database import db
from datetime import datetime


class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    rubric_id = db.Column(db.Integer, db.ForeignKey('rubric.id'))
    proposal_name = db.Column(db.String)
    num_members = db.Column(db.Integer)
    problem_desc = db.Column(db.String)
    audience = db.Column(db.String)
    solution_desc = db.Column(db.String)
    approach = db.Column(db.String)
    requirements = db.Column(db.String)
    tools = db.Column(db.String)
    goals = db.Column(db.String)
    benefit= db.Column(db.String)
    sustainability = db.Column(db.String)
    notes = db.Column(db.String)
    created = db.Column(db.String, default=datetime.utcnow().strftime('%d-%B-%Y')) # 13-May-2023
    status = db.Column(db.Integer, default=0)
    evaluations = db.relationship('Evaluation', backref=db.backref('proposal', lazy='joined'))


    def __init__(self, id, rubric_id, proposal_nm, problem_desc, audience, solution_desc, approach, num_members, requirements, tools, goals, benefit, sustainability, notes):
        self.proposal_name = proposal_nm.capitalize() 
        self.student_id = id.id
        self.rubric_id = rubric_id
        self.problem_desc = problem_desc.capitalize()
        self.audience = audience.capitalize()
        self.solution_desc = solution_desc.capitalize()
        self.approach = approach.capitalize()
        self.num_members = int(num_members)
        self.notes = notes.capitalize()
        self.requirements = requirements.capitalize()
        self.tools = tools.capitalize()
        self.goals = goals.capitalize()
        self.benefit = benefit.capitalize()
        self.sustainability = sustainability.capitalize()
