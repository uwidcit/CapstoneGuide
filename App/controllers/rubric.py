from App.models import Rubric
from App.database import db
from .user import get_lecturer

def add_rubric(name, notes, novelty, relevance, feasibility, impact, sustainability, technology, lecturer_id):
        rubric = Rubric(name, notes, novelty, relevance, feasibility, impact, sustainability, technology, lecturer_id)
        db.session.add(rubric)
        db.session.commit()
        return rubric


def remove_rubric(lecturer_id, rubricId):
    rubric = Rubric.query.filter_by(id=lecturer_id, rubric_id=rubricId).first()
    if rubric:
        db.session.delete(rubric)
        res = db.session.commit()
        return res
    return None


def get_user_rubric(lecturer_id, evaluationId):
    rubric = Rubric.query.filter_by(id=lecturer_id, evaluationId = evaluationId).all() 
    return rubric

def get_user_rubrics(lecturer_id):
    return Rubric.query.filter_by(id=lecturer_id).all()

def get_all_rubrics():
    return Rubric.query.all()