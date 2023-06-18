from App.models import Proposal
from App.database import db

def add_proposal(student_id, proposal_nm, problem_desc, solution_desc,
                 num_members, notes, functionalities, technologies):
    proposal = Proposal(student_id=student_id,proposal_nm=proposal_nm, problem_desc=problem_desc, solution_desc=solution_desc,
                 num_members=num_members, requirements=functionalities, tools=technologies, notes=notes,)
    db.session.add(proposal)
    db.session.commit()
    return proposal

def remove_proposal(student_id):
    proposal = Proposal.query.get(student_id)
    if proposal:
        db.session.delete(proposal)
        res = db.session.commit()
        return res
    return None

def get_user_proposal(student_id, evaluationId):
    proposal = Proposal.query.filter_by(student_id=student_id, evaluationId = evaluationId).all() 
    return proposal

def get_user_proposals(student_id):
    return Proposal.query.filter_by(student_id=student_id).all()

def get_all_proposals():
    return Proposal.query.all()