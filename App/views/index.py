from flask import Blueprint, render_template, request, jsonify 
from App.models import db
from App.controllers import initalizeDB, create_lecturer, add_rubric, create_student

index_views = Blueprint('index_views', __name__, template_folder='../templates')

# Main page
@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    initalizeDB()
    db.drop_all()
    db.create_all()
    rob = create_student('rob', 'robspass', 'rob@mycavehilluwi.edu', 'Rob', 'Renolds', 2222)
    # steve = create_student('steve', 'stevepass', 'steve@mycavehilluwi.edu', 'Steve', 'Pass', 3333)
    ai = create_lecturer('capadviosr', 'capadvisor', 'capadvisor@temp.com', 'Cap', 'Adivosr(AI)', 9999)
    bob = create_lecturer('bob', 'bobspass', 'bob@mycavehilluwi.edu', 'bob', 'smith', 1111)
    # cory = create_lecturer('cory', 'corypass', 'cory@mycavehilluwi.edu', 'Cory', 'Jones', 4444)
    rubric = add_rubric('Default','For practice', 3, 5, 6, 6, 6, 1, 101)
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})
