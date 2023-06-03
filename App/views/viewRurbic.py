from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views

viewRubric_views = Blueprint('viewRubric_views', __name__, template_folder='../templates')

@viewRubric_views.route('/view-rubric', methods=['GET'])
def get_viewRubric_page():
    return render_template('viewRubric.html')