from App.models import Rubric
from App.database import db

def add_rubric(novelty, feasibility, notes, impact, sustainability, technologies, supervisorId):
    rubric = Rubric(novelty=novelty, feasibility=feasibility, notes=notes,
                             impact=impact, sustainability=sustainability, technologies=technologies, supervisorId=supervisorId)
    db.session.add(rubric)
    db.session.commit()
    return rubric

def remove_rubric(lecturerId):
    rubric = Rubric.query.get(lecturerId)
    if rubric:
        db.session.delete(rubric)
        res = db.session.commit()
        return res
    return None

def get_user_rubric(lecturerId, evaluationId):
    rubric = Rubric.query.filter_by(lecturerId=lecturerId, evaluationId = evaluationId).all() 
    return rubric

def get_user_rubrics(lecturerId):
    return Rubric.query.filter_by(lecturerId=lecturerId).all()

def get_all_rubric():
    return Rubric.query.all()