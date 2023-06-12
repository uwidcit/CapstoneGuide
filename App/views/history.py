from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required
from App.controllers import (get_user_proposal, get_user_proposals, student_required)

from.index import index_views

history_views = Blueprint('history_views', __name__, template_folder='../templates')

#student_required
@history_views.route('/history', methods=['GET'])
def get_history_page():
    # current_user.id
    proposals = get_user_proposals(1)
    return render_template('history.html', proposals=proposals)