from App.models import Evaluation 
from App.database import db
from .proposal import get_user_proposals, get_proposal


def add_evaluation(notes, novelty, relevance, feasibility, impact, sustainability, technologies, proposal_id, reviewer):
    proposal = get_proposal(proposal_id)
    if proposal:
        evaluation = Evaluation(comments=notes, novelty=novelty, relevance=relevance, feasibility=feasibility, impact=impact, sustainability=sustainability,
                                 technologies=technologies, proposal_id=proposal_id, reviewer_id=reviewer)
        proposal.evaluations.append(evaluation)
        if(reviewer != 101):
            proposal.status = 1
        db.session.commit()
        return evaluation
    return None

def remove_evaluation(proposal_id):
    evaluation = Evaluation.query.filter_by(proposal_id=proposal_id).first()
    if evaluation:
        db.session.delete(evaluation)
        res = db.session.commit()
        return res
    return None

def get_user_evaluation(proposal_id, evaluation_id):
    evaluation = Evaluation.query.filter_by(id=proposal_id, evaluation_id=evaluation_id).all()
    if evaluation:
        return evaluation
    return None

def get_evaluation(evaluation_id):
    evaluation = Evaluation.query.get(evaluation_id)
    if evaluation:
        return evaluation
    return None

def get_user_evaluations(proposal_id):
    evaluation = Evaluation.query.filter_by(proposal_id=proposal_id).all()
    if evaluation:
        return evaluation
    return None


def get_all_evaluations():
    return Evaluation.query.all()

