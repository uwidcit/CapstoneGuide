from App.database import db
from datetime import datetime


class Proposal(db.Model):
    proposalId = db.Column(db.Integer, primary_key=True)

    studentId = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    #rubricId = db.Column(db.Integer, db.ForeignKey('rubric.id'))
    proposal_name = db.Column(db.String) 
    problem_desc = db.Column(db.String)
    solution_desc = db.Column(db.String)
    notes = db.Column(db.String)
    requirements = db.Column(db.String)
    tools = db.Column(db.String)
    num_members = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.utcnow)


    def __init__(self, studentId, proposal_nm, problem_desc, solution_desc, num_members, requirements, tools, notes):
        self.proposal_name = proposal_nm
        self.studentId = studentId
        #self.rubricId = 1
        self.problem_desc = problem_desc
        self.solution_desc = solution_desc
        self.num_members = int(num_members)
        self.notes = notes
        self.requirements = requirements
        self.tools = tools
