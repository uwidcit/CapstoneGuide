from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required

from App.controllers import lecturer_required, add_evaluation, get_evaluation, student_required

from.history import history_views

evaluation_views = Blueprint('evaluation_views', __name__, template_folder='../templates')


@student_required
@evaluation_views.route('/get-evaluation/<evaluationId>', methods=['GET'])
@login_required
def get_evaluation_endpoint(evaluationId):
    eval = get_evaluation(evaluationId)
    if eval:
        return jsonify({
            'name': eval.proposal.proposal_name,
            'novelty': {
                'name': 'Novelty',
                'score': eval.novelty,
                'threshold': eval.proposal.rubric.novelty
            },
            'relevance': {
                'name': 'Relevance',
                'score': eval.relevance,
                'threshold': eval.proposal.rubric.relevance
            },
            'feasibility': {
                'name': 'Feasibility',
                'score': eval.feasibility,
                'threshold': eval.proposal.rubric.feasibility
            },
            'impact': {
                'name': 'Impact',
                'score': eval.impact,
                'threshold': eval.proposal.rubric.impact
            },
            'sustainability': {
                'name': 'Sustainability',
                'score': eval.sustainability,
                'threshold': eval.proposal.rubric.sustainability
            },
            'technologies': {
                'name': 'Technology',
                'score': eval.technologies,
                'threshold': eval.proposal.rubric.technology
            },
            'series':[
                {
                    'name': 'Score',
                    'data': [eval.novelty, eval.relevance, eval.feasibility, eval.impact, eval.sustainability, eval.technologies]
                },
                {
                    'name': 'Threshold',
                   'data': [eval.proposal.rubric.novelty, eval.proposal.rubric.relevance, eval.proposal.rubric.feasibility, eval.proposal.rubric.impact, eval.proposal.rubric.sustainability, eval.proposal.rubric.technology]
                }
            ],
            'score': eval.score,
            'comments': eval.comments,
            'notes': eval.proposal.notes,
            'num_members': eval.proposal.num_members,
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

