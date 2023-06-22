from App.database import db
from App.controllers import ( create_student, create_lecturer, get_stu_by_username, get_lect_by_username, get_all_students, get_all_lecturers,
                             add_rubric, get_user_rubric, get_all_rubrics,
                             add_proposal, get_proposal, get_all_proposals,
                             add_evaluation, get_user_evaluation,  get_all_evaluations)

def initalizeDB():
    db.drop_all()
    db.create_all()
    rob = create_student('rob', 'robspass', 'rob@mycavehilluwi.edu', 'Rob', 'Renolds', 2222)
    steve = create_student('steve', 'stevepass', 'steve@mycavehilluwi.edu', 'Steve', 'Pass', 3333)
    ai = create_lecturer('capadviosr', 'capadvisor', 'capadvisor@temp.com', 'Cap', 'Adivosr', 9999)
    bob = create_lecturer('bob', 'bobspass', 'bob@mycavehilluwi.edu', 'bob', 'smith', 1111)
    cory = create_lecturer('cory', 'corypass', 'cory@mycavehilluwi.edu', 'Cory', 'Jones', 4444)
    rubric = add_rubric('Default','For practice', 3, 5, 6, 6, 6, 1, 101)
    cap_advisor = add_proposal(steve.id, rubric.id, 'Cap Advisor', 'Students do not always undertsand how to design capstone projects', 'SWEN and COMP students',
                'Students can submit capstone proposals to and have feedback', 'craete a web app which allows them submit proposal according to capstone rubric',
                3, 'students must submit proposals based on cirtera', 'flask MVC, python, GPT-3', 'students can understand what is required for capstone projects and begine their own',
                  'SWEN and COMP students','manged by lecturer eventually',
                'May be revised')
    flask_test = add_proposal(steve.id, rubric.id, 'Flask Test', 'Students do not always undertsand how to design capstone projects', 'SWEN and COMP students',
                'Students can submit capstone proposals to and have feedback', 'craete a web app which allows them submit proposal according to capstone rubric',
                2, 'students must submit proposals based on cirtera', 'flask MVC, python, GPT-3', 'students can understand what is required for capstone projects and begine their own',
                  'SWEN and COMP students','manged by lecturer eventually',
                'May be revised')
    solo = add_proposal(rob.id, rubric.id, 'Solo', 'Students do not always undertsand how to design capstone projects', 'SWEN and COMP students',
                'Students can submit capstone proposals to and have feedback', 'craete a web app which allows them submit proposal according to capstone rubric',
                5, 'students must submit proposals based on cirtera', 'flask MVC, python, GPT-3', 'students can understand what is required for capstone projects and begine their own',
                  'SWEN and COMP students','manged by lecturer eventually',
                'May be revised')
    add_evaluation('notes', 5, 7, 5, 3, 10, 5, cap_advisor.id, cory.id)
    add_evaluation('crash', 10, 10, 1, 3, 10, 10, flask_test.id, bob.id)
    add_evaluation('crash', 10, 10, 1, 3, 10, 10, solo.id, ai.id)
    print('database intialized')
