from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user

from.index import index_views
from .rubric import rubric_views
from .proposal import proposal_views
from App.models import Student, Lecturer

from App.controllers import (
    login 
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
Page/Action Routes
'''

# @auth_views.route('/users', methods=['GET'])
# def get_user_page():
#     return render_template('users.html')


@auth_views.route('/identify', methods=['GET'])
@login_required
def identify_page():
    return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})


@auth_views.route('/login', methods=['GET'])
def get_registration_page():
    return render_template('registration.html')

@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    user = login(data['username'], data['password'])
    if user:
        if type(user) ==  Student:
            login_user(user)
            return redirect(url_for('proposal_views.get_proposal_page'))
        elif type(user) ==  Lecturer:
            login_user(user)
            return redirect(url_for('rubric_views.rubric_page'))
    flash('Incorrect username or password given')
    return redirect(url_for('auth_views.get_registration_page'))

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('auth_views.get_registration_page'))
