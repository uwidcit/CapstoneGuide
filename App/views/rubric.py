from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required
from App.controllers import ( create_lecturer, add_rubric, remove_rubric, get_all_rubrics, get_all_lecturers, get_user_rubrics )

from.index import index_views

rubric_views = Blueprint('rubric_views', __name__, template_folder='../templates')

# @supervisor_required
@rubric_views.route('/rubric', methods=['GET'])
def rubric_page():
    # current_user.id
    rubrics = get_user_rubrics(1)
    return render_template('rubric.html', rubrics=rubrics)

#@lecturer_required
@rubric_views.route('/rubric', methods=['POST'])
def create_rubric_action():
    data = request.form
    add_rubric(data['name'], data['notes'], data['novelty'], data['relevance'], data['feasibility'], data['impact'], data['sustainability'], data['technology'], 1)
    flash('Rubric Added!')
    return redirect(url_for('rubric_views.rubric_page'))

@rubric_views.route('/delete-rubric/<int:rubricId>', methods=['GET'])
def delete_rubric_action(rubricId):
    remove_rubric(1, rubricId)
    flash('Rubric Deleted!')
    return redirect(url_for('rubric_views.rubric_page'))