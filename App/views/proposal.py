from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views

proposal_views = Blueprint('proposal_views', __name__, template_folder='../templates')

@proposal_views.route('/proposal', methods=['GET'])
def get_proposal_page():
    return render_template('proposal.html')