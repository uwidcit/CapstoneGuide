from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required

from App.controllers import lecturer_required, add_evaluation, get_evaluation

from.history import history_views

evaluation_views = Blueprint('evaluation_views', __name__, template_folder='../templates')

@evaluation_views.route('/proposal-evaluation', methods=['GET'])
@login_required
def get_evaluation_page():
    return render_template('evaluation.html')

@evaluation_views.route('/get-evaluation/<evaluationId>', methods=['GET'])
def get_evaluation_endpoint(evaluationId):
    eval = get_evaluation(evaluationId)
    if eval:
        return jsonify({
            'novelty': {
                'score': eval.novelty,
                'threshold': eval.proposal.rubric.novelty
            },
            'relevance': {
                'score': eval.relevance,
                'threshold': eval.proposal.rubric.relevance
            },
            'feasibility': {
                'score': eval.feasibility,
                'threshold': eval.proposal.rubric.feasibility
            },
            'impact': {
                'score': eval.impact,
                'threshold': eval.proposal.rubric.impact
            },
            'sustainability': {
                'score': eval.sustainability,
                'threshold': eval.proposal.rubric.sustainability
            },
            'technologies': {
                'score': eval.technologies,
                'threshold': eval.proposal.rubric.technology
            },
            'comments': eval.comments
        })
    return jsonify(message="Evaluation not found!")
    

@lecturer_required
@evaluation_views.route('/man-evaluation', methods=['POST'])
@login_required
def lect__evaluate():
    data = request.form
    add_evaluation(data['notes'], data['novelty'], data['relevance'], data['feasibility'], data['impact'],
                    data['sustainability'], data['technology'], data['prop_id'], current_user.id)
    flash('Evaluation Completed!')
    return redirect(url_for('history_views.get_submission_page'))

