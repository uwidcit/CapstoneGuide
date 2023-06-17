from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required
from App.controllers import (get_user_proposal, get_user_proposals, get_all_proposals, get_user_evaluations, student_required, lecturer_required)

from.index import index_views

history_views = Blueprint('history_views', __name__, template_folder='../templates')

@student_required
@history_views.route('/history', methods=['GET'])
@login_required
def get_history_page():
    proposals = get_user_proposals(current_user.id)
    print(proposals)
    #evaluations = get_user_evaluations(proposals.proposal_id)
    #if proposal.student = current user get all evaluations where proposal id
    return render_template('history.html', proposals=proposals)

@lecturer_required
@history_views.route('/submissions', methods=['GET'])
@login_required
def get_submission_page():
    proposals = get_all_proposals()
    return render_template('submissions.html', proposals=proposals)