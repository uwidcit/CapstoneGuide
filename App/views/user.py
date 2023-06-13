from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required

from.index import index_views
from .proposal import proposal_views
from .registration import registration_views

from App.controllers import ( register_student, register_lecturer)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/user', methods=['POST'])
def create_user_action():
    data = request.form
    if data['role'] == 'Student':
        result = register_student(data['username'], data['re_password'], data['first_name'], data['last_name'], data['email'], 1)
        if result:
            #jsonify({"message": f"Customer created with id {result.id}"}), 201
            print('user added')
            return redirect(url_for('proposal_views.get_proposal_page'))        
    else:
        result = register_lecturer(data['username'], data['re_password'], data['first_name'], data['last_name'], data['email'], 1)
        if result:
            print('user added')
            #jsonify({"message": f"Customer created with id {result.id}"}), 201
            return redirect(url_for('rubric_views.rubric_page'))
    
    #jsonify({"error": f"Username {data['username']} already exists "}), 500    
    print('user exists')
    return redirect(url_for('registration_views.get_registration_page'))
    

# @user_views.route('/api/users', methods=['POST'])
# def create_user_endpoint():
#     data = request.json
#     create_user(data['username'], data['password'])
#     return jsonify({'message': f"user {data['username']} created"})

