from App.models import Rubric
from App.database import db

def add_rubric(name, notes, novelty, relevance, feasibility, impact, sustainability, technology, lecturer_id):
    rubric = Rubric(name, notes, novelty, relevance, feasibility, impact, sustainability, technology, lecturer_id)
    db.session.add(rubric)
    db.session.commit()
    return rubric

def remove_rubric(lecturer_id, rubricId):
    rubric = Rubric.query.filter_by(lecturer_id=lecturer_id, id=rubricId).first()
    if rubric:
        db.session.delete(rubric)
        res = db.session.commit()
        return res
    return None


def update_rubric(rubricId, name, notes, novelty, relevance, feasibility, impact, sustainability, technology, lecturer_id):
    rubric = Rubric.query.filter_by(lecturer_id=lecturer_id, id=rubricId).first()
    if rubric:
        rubric.name = name
        rubric.notes = notes
        rubric.novelty = novelty
        rubric.relevance = relevance
        rubric.feasibility = feasibility
        rubric.impact = impact
        rubric.sustainability = sustainability
        rubric.technology = technology
        db.session.add(rubric)
        res = db.session.commit()
        return res
    return None

def get_user_rubric(lecturer_id, rubric_id):
    rubric = Rubric.query.filter_by(lecturer_id=lecturer_id, id = rubric_id).all() 
    return rubric

def get_user_rubrics(lecturer_id):
    return Rubric.query.filter_by(lecturer_id=lecturer_id).all()

def get_all_rubrics():
    return Rubric.query.all()