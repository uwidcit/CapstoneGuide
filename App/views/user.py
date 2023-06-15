from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required, login_user

from.index import index_views
from .proposal import proposal_views
from .rubric import rubric_views
from .auth import auth_views

from App.controllers import (create_student, create_lecturer)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/user', methods=['POST'])
def create_user_action():
    data = request.form
    if data['role'] == 'Student':
        result = create_student(data['username'], data['re_password'], data['email'], data['first_name'], data['last_name'], data['uwi_id'])
        if result:
            flash('Account Created')
            login_user(result)
            return redirect(url_for('proposal_views.get_proposal_page'))        
    if data['role'] == 'Lecturer':
        result = create_lecturer(data['username'], data['re_password'], data['email'], data['first_name'], data['last_name'], data['uwi_id'])
        if result:
            result.id -= 100
            flash('Account Created')
            login_user(result)
            return redirect(url_for('rubric_views.rubric_page'))
    flash('user exists')
    return redirect(url_for('auth_views.get_registration_page'))

