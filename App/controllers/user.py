from App.models import User, Student, Lecturer
from App.database import db

def create_student(username, password, email, first_name, last_name, student_id):
    newuser = Student(username=username, first_name=first_name, last_name=last_name, password=password, email=email, student_id=student_id)
    try:    
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except:
        return None

def create_lecturer(username, password, email, first_name, last_name, lecturer_id):
    newuser = Lecturer(username=username, first_name=first_name, last_name=last_name, password=password, email=email, lecturer_id=lecturer_id)
    try:
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except:
        return None


def get_lecturer(lecturer_id):
    return Lecturer.query.get(lecturer_id)

def get_student(studentId):
    return Student.query.get(studentId)

def is_lecturer(lecturer_id):
    return Lecturer.query.get(lecturer_id) != None

def is_student(studentId):
    return Lecturer.query.get(studentId) != None

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_students():
    return Student.query.all()

def get_all_lecturers():
    return Lecturer.query.all()

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None