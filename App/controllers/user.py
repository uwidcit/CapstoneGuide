from App.models import User, Student, Lecturer
from App.database import db
from sqlalchemy.exc import SQLAlchemyError

def create_lecturer(username, password, email, first_name, last_name, uwi_id):
    newuser = Lecturer(username=username, first_name=first_name, last_name=last_name, password=password, email=email, uwi_id=uwi_id)
    try:
        db.session.add(newuser)
        db.session.commit()
        newuser.id += 100
        newuser = get_lecturer(newuser.id)
        return newuser
    except SQLAlchemyError as e:
        print(f"Database error occurred: {str(e)}")
        return None

def create_student(username, password, email, first_name, last_name, uwi_id):
    newuser = Student(username=username, first_name=first_name, last_name=last_name, password=password, email=email, uwi_id=uwi_id)
    try:    
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except SQLAlchemyError as e:
        print(f"Database error occurred: {str(e)}")
        return None


def get_lecturer(id):
    return Lecturer.query.get(id)

def get_student(student_id):
    return Student.query.get(student_id)

def is_lecturer(id):
    return Lecturer.query.get(id) != None

def is_student(id):
    return Lecturer.query.get(id) != None

def get_stu_by_username(username):
    return Student.query.filter_by(username=username).first()

def get_lect_by_username(username):
    return Lecturer.query.filter_by(username=username).first()

def get_all_students():
    return Student.query.all()

def get_all_lecturers():
    return Lecturer.query.all()
