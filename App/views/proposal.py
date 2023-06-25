from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required
from App.controllers import (get_ai_evaluation, student_required, add_proposal, remove_proposal,remove_evaluation, get_all_rubrics, get_rubric)

from .history import history_views

proposal_views = Blueprint('proposal_views', __name__, template_folder='../templates')

# shows rubrics to select

@proposal_views.route('/proposal', methods=['GET'])
@student_required
def get_proposal_page():
    rubrics = get_all_rubrics()
    return render_template('selectRubric.html', rubrics=rubrics)

# displays proposal form

@proposal_views.route('/select-rubric/<int:rubricId>', methods=['GET'])
@student_required
def submit_proposal_page(rubricId):
    flash(get_rubric(rubricId).name + ' Rubric Selected!')
    return render_template('proposal.html', rubricId=rubricId)

# saves the proposal to the DB and 

@proposal_views.route('/select-rubric/<int:rubricId>', methods=['POST'])
@student_required
def submit_proposal_action(rubricId):
    data = request.form
    add_proposal(current_user.id, rubricId, data['name'], data['problem'], data['audience'], data['solution'], data['approach'], data['group_num'], 
                 data['requirements'], data['tools'],
                 data['goals'], data['benefit'], data['sustain'], data['additional_info'])
    get_ai_evaluation(str(data['name']), str(data['problem']), str( data['audience']), str(data['solution']),
                      str(data['approach'],), str(data['group_num']), str(data['requirements']), str(data['tools']),
                 str(data['goals']), str(data['benefit']), str(data['sustain']), str(data['additional_info']))
    flash('Proposal Submitted. Go to History Page to view results!')
    return redirect(url_for('proposal_views.get_proposal_page'))

# removes a proposal from the DB
@proposal_views.route('/delete-proposal/<int:proposalID>', methods=['GET'])
@student_required
def delete_proposal_action(proposalID):
    remove_evaluation(proposalID)
    remove_proposal(current_user.id, proposalID)
    flash('Proposal Deleted!')
    return redirect(url_for('history_views.get_history_page'))