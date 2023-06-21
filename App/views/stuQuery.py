from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user, login_required

from App.controllers import get_all_lecturers, get_all_students

stuQuery_views = Blueprint('stuQuery_views', __name__, template_folder='../templates')

@stuQuery_views.route('/ask-query', methods=['GET'])
def get_stuQuery_page():
    return render_template('stuQuery.html')

@stuQuery_views.route('/contacts', methods=['GET'])
def get_contact_page():
    lecturers = get_all_lecturers()
    return render_template('contact.html', lecturers=lecturers)

@stuQuery_views.route('/students', methods=['GET'])
def get_student_page():
    students = get_all_students()
    return render_template('stuContact.html', students=students)