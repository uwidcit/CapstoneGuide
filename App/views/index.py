from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_student, create_lecturer

index_views = Blueprint('index_views', __name__, template_folder='../templates')

# Main page
@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_lecturer('capadviosr', 'capadvisor', 'capadvisor@temp.com', 'Cap', 'Adivosr', 0)
    add_rubric('Default','For practice', 3, 5, 6, 6, 6, 1, 101)
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})
