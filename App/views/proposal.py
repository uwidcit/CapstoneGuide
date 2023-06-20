from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required
from App.controllers import (student_required, add_proposal, remove_proposal,remove_evaluation, get_all_rubrics)

from .history import history_views

proposal_views = Blueprint('proposal_views', __name__, template_folder='../templates')

@student_required
@proposal_views.route('/proposal', methods=['GET'])
@login_required
def get_proposal_page():
    rubrics = get_all_rubrics()
    return render_template('select.html', rubrics=rubrics)

@student_required
@proposal_views.route('/select-rubric/<int:rubricId>', methods=['GET'])
@login_required
def submit_proposal_page(rubricId):
    flash('Rubric Selected!')
    return render_template('proposal.html', rubricId=rubricId)

@student_required
@proposal_views.route('/select-rubric/<int:rubricId>', methods=['POST'])
@login_required
def submit_proposal_action(rubricId):
    data = request.form
    add_proposal(current_user.id, rubricId, data['name'], data['problem'], data['solution'], data['group_num'], data['requirements'], data['tools'],
                 data['goals'], data['sustain'], data['additional_info'])
    flash('Proposal Submitted, Go to History to view!')
    return redirect(url_for('proposal_views.get_proposal_page'))

@student_required
@proposal_views.route('/delete-proposal/<int:proposalID>', methods=['GET'])
@login_required
def delete_proposal_action(proposalID):
    remove_evaluation(proposalID)
    remove_proposal(current_user.id, proposalID)
    flash('Proposal Deleted!')
    return redirect(url_for('history_views.get_history_page'))