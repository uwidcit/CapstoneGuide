from App.models import Evaluation 
from App.database import db


def add_evaluation(novelty, feasibility, score, impact, sustainability, technologies, proposal_id):
    evaluation = Evaluation(novelty=novelty, feasibility=feasibility, score=score, 
                         impact=impact, sustainability=sustainability, technologies=technologies, proposal_id=proposal_id)
    db.session.add(evaluation)
    db.session.commit(evaluation)
    return evaluation


def get_user_evaluation(studentId, evaluationId):
    evaluation = Evaluation.query.filter_by(studentId=studentId, evaluationId = evaluationId).all()
    if evaluation:
        return evaluation
    return None

def get_user_evaluations(studentId):
    evaluation = Evaluation.query.filter_by(studentId=studentId)
    if evaluation:
        return evaluation
    return None

