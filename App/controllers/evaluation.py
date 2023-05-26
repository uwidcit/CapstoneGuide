from App.models import Evaluation 
from App.database import db


def add_evaluation(novelty, feasibility, score, impact, sustainability, technologies, proposal_id):
    evaluation = Evaluation(novelty=novelty, feasibility=feasibility, score=score, 
                         impact=impact, sustainability=sustainability, technologies=technologies, proposal_id=proposal_id)
    db.session.add(evaluation)
    db.session.commit(evaluation)
    return evaluation


def get_user_evaluations(studentId, evaluationId):
    evaluation = Evaluation.query.filter_by(studentId=studentId, evaluationId = evaluationId).all()
    return None

def get_user_evaluation(studentId):
    return Evaluation.query.filter_by(studentId=studentId)

