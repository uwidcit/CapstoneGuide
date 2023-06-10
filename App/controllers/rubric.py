from App.models import Rubric
from App.database import db

def add_rubric(name, notes, novelty, relevance, feasibility, impact, sustainability, technology, lecturerId):
    rubric = Rubric(name, notes, novelty, relevance, feasibility, impact, sustainability, technology, lecturerId)
    db.session.add(rubric)
    db.session.commit()
    return rubric

def remove_rubric(lecturerId, rubricId):
    rubric = Rubric.query.filter_by(lecturerId=lecturerId, id=rubricId).first()
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

def get_all_rubrics():
    return Rubric.query.all()