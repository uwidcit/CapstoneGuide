from flask_login import login_user, current_user, LoginManager
from App.models import db, User, Student, Lecturer
from .user import create_student, create_lecturer
from functools import wraps

def login(username, password):
    lecturer = Lecturer.query.filter_by(username=username).first()
    if lecturer and lecturer.check_password(password):
        return lecturer
    student = Student.query.filter_by(username=username).first()
    if student and student.check_password(password):
        return student
    return None

def register_student(username, password, email, first_name, last_name, student_id):
    student = Student.query.filter_by(username=username).first()
    if student:
        return "Username already exists"
    new_student = create_student(username=username, first_name=first_name, last_name=last_name, password=password, email=email, student_id=student_id)
    return "Student registered successfully"

def register_lecturer(username, password, email, first_name, last_name, lecturer_id):
    lecturer = Lecturer.query.filter_by(username=username).first()
    if lecturer:
        return "Username already exists"
    new_lecturer = create_lecturer(username=username, first_name=first_name, last_name=last_name, password=password, email=email, lecturer_id=lecturer_id)
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
        print('hello')
        if not current_user.is_authenticated or not isinstance(current_user, Lecturer):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

def setup_flask_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        student =  Student.query.get(user_id)
        if student:
            return customer
        return Lecturer.query.get(user_id)
    
    return login_manager


