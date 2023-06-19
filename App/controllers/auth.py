from flask_login import login_user, current_user, LoginManager
from App.models import db, User, Student, Lecturer
#from .user import create_student, create_lecturer

from functools import wraps

def login(username, password):
    #login with username
    lecturer = Lecturer.query.filter_by(username=username).first()
    if lecturer and lecturer.check_password(password):
        return lecturer
    
    student = Student.query.filter_by(username=username).first()
    if student and student.check_password(password):
        return student

    #login with ID    
    lecturer = Lecturer.query.filter_by(uwi_id=username).first()
    if lecturer and lecturer.check_password(password):
        return lecturer
    
    student = Student.query.filter_by(uwi_id=username).first()
    if student and student.check_password(password):
        return student
    return None

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

def setup_flask_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        student =  Student.query.get(user_id)
        if student:
            return student
        return Lecturer.query.get(user_id)
    
    return login_manager


