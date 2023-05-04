from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views

registration_views = Blueprint('registration_views', __name__, template_folder='../templates')

@registration_views.route('/registration', methods=['GET'])
def get_registration_page():
    return render_template('registration.html')