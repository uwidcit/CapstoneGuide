from App.models import Proposal
from App.database import db

def add_proposal(studentId, rubricId, problem_desc, solution_desc,
                 num_members, notes, functionalities, technologies):
    proposal = Proposal(studentId=studentId, rubricId=rubricId, problem_desc=problem_desc, solution_desc=solution_desc,
                 num_members=num_members, notes=notes, functionalities=functionalities, technologies=technologies)
    db.session.add(proposal)
    db.session.commit()
    return proposal

def remove_proposal(studentId):
    proposal = Proposal.query.get(studentId)
    if proposal:
        db.session.delete(proposal)
        res = db.session.commit()
        return res
    return None

def get_user_proposal(studentId, evaluationId):
    proposal = Proposal.query.filter_by(studentId=studentId, evaluationId = evaluationId).all() 
    return proposal

def get_user_proposals(studentId):
    return Proposal.query.filter_by(studentId=studentId).all()

def get_all_proposal():
    return Proposal.query.all()