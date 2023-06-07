from flask_login import login_user, current_user
from App.models import db, User, Student, Lecturer
from functools import wraps

def login(username, password):
    lecturer = Lecturer.query.filter_by(username=username).first()
    if lecturer and lecturer.check_password(password):
        return lecturer
    student = Student.query.filter_by(username=username).first()
    if student and student.check_password(password):
        return student
    return None

def register_student(username, first_name, last_name, password, email):
    student = Student.query.filter_by(username=username).first()
    if student:
        return "Username already exists"
    new_student = create_student(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
    return "Student registered successfully"

def register_lecturer(username, first_name, last_name, password, email):
    lecturer = Lecturer.query.filter_by(username=username).first()
    if lecturer:
        return "Username already exists"
    new_lecturer = create_lecturer(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
    return "Lecturer registered successfully"

def initialize():
    db.drop_all()
    db.create_all()

   
def student_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Student):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

def lecturer_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Lecturer):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

 

