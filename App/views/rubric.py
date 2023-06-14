from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required
from App.controllers import (add_rubric, remove_rubric, update_rubric, get_user_rubrics, lecturer_required )

from.index import index_views


rubric_views = Blueprint('rubric_views', __name__, template_folder='../templates')


@rubric_views.route('/rubric', methods=['GET'])
def rubric_page():
    # current_user.id
    # check if authed
    print(current_user.is_authenticated)
    rubrics = get_user_rubrics(current_user.id)
    return render_template('rubric.html', rubrics=rubrics)

@lecturer_required
@rubric_views.route('/rubric', methods=['POST'])
def create_rubric_action():
    data = request.form
    add_rubric(data['name'], data['notes'], data['novelty'], data['relevance'], data['feasibility'], data['impact'], data['sustainability'], data['technology'], current_user.id)
    flash('Rubric Added!')
    return redirect(url_for('rubric_views.rubric_page'))

@lecturer_required
@rubric_views.route('/delete-rubric/<int:rubricId>', methods=['GET'])
def delete_rubric_action(rubricId):
    remove_rubric(current_user.id, rubricId)
    flash('Rubric Deleted!')
    return redirect(url_for('rubric_views.rubric_page'))

# #@lecturer_required
# @rubric_views.route('/update-rubric', methods=['POST'])
# def update_rubric_action(rubric_id):
#     data = request.form
#     update_rubric(rubric_id, data['name'], data['notes'], data['novelty'], data['relevance'], data['feasibility'], data['impact'], data['sustainability'], data['technology'], 1)
#     flash('Rubric Updatd!')
#     return redirect(url_for('rubric_views.rubric_page'))