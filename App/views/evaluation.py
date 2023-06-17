from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required

from App.controllers import lecturer_required, add_evaluation

from.history import history_views

evaluation_views = Blueprint('evaluation_views', __name__, template_folder='../templates')

@evaluation_views.route('/proposal-evaluation', methods=['GET'])
@login_required
def get_evaluation_page():
    return render_template('evaluation.html')

@lecturer_required
@evaluation_views.route('/man-evaluation', methods=['POST'])
@login_required
def lect__evaluate():
    data = request.form
    print(data['prop_id'])
    add_evaluation(data['notes'], data['novelty'], data['relevance'], data['feasibility'], data['impact'],
                    data['sustainability'], data['technology'], 1)
    flash('Evaluation Completed!')
    return redirect(url_for('history_views.get_submission_page'))

