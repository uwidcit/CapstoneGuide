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
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})
