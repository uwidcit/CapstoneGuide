from App.database import db
from datetime import datetime


class Proposal(db.Model):
    proposal_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    #rubricId = db.Column(db.Integer, db.ForeignKey('rubric.id'))
    proposal_name = db.Column(db.String) 
    problem_desc = db.Column(db.String)
    solution_desc = db.Column(db.String)
    notes = db.Column(db.String)
    requirements = db.Column(db.String)
    tools = db.Column(db.String)
    num_members = db.Column(db.Integer)
    created = db.Column(db.String, default=datetime.utcnow().strftime('%d-%B-%Y')) # 13-May-2023
    status = db.Column(db.Integer, default=0)
    evaluations = db.relationship('Evaluation', backref=db.backref('proposal', lazy='joined'))


    def __init__(self, id, proposal_nm, problem_desc, solution_desc, num_members, requirements, tools, notes):
        self.proposal_name = proposal_nm.capitalize() 
        self.student_id = id.id
        #self.rubricId = 1
        self.problem_desc = problem_desc
        self.solution_desc = solution_desc
        self.num_members = int(num_members)
        self.notes = notes
        self.requirements = requirements
        self.tools = tools
