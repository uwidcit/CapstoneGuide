from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required
from App.controllers import (add_rubric, remove_rubric, get_proposal_by_rubric, get_user_rubrics, lecturer_required )

from.index import index_views


rubric_views = Blueprint('rubric_views', __name__, template_folder='../templates')

# gets rubric page
@lecturer_required
@rubric_views.route('/rubric', methods=['GET'])
@login_required
def rubric_page():
    # check if authed
    print(current_user.is_authenticated)
    rubrics = get_user_rubrics(current_user.id)
    return render_template('rubric.html', rubrics=rubrics)

# adds rubric to DB
@lecturer_required
@rubric_views.route('/rubric', methods=['POST'])
@login_required
def create_rubric_action():
    data = request.form
    add_rubric(data['name'], data['notes'], data['novelty'], data['relevance'], data['feasibility'], data['impact'], data['sustainability'], data['technology'],current_user.id)
    flash('Rubric Added!')
    return redirect(url_for('rubric_views.rubric_page'))

# removes rubric from DB
@lecturer_required
@rubric_views.route('/delete-rubric/<int:rubricId>', methods=['GET'])
@login_required
def delete_rubric_action(rubricId):
    if(get_proposal_by_rubric(rubricId) == None):
        remove_rubric(current_user.id, rubricId)
        flash('Rubric Deleted!')
        return redirect(url_for('rubric_views.rubric_page'))
    flash('Rubric cannot be deleted. A Proposal is using it!')
    return redirect(url_for('rubric_views.rubric_page'))