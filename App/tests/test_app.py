import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Student, Lecturer
from App.controllers import (
    get_all_users_json,
    login,
    create_lecturer,
    create_student, add_proposal, add_rubric, add_evaluation
)


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):
    #User creation
    def test_new_student(self):
        student = Student("danteb", "dantepass", "dante.blunt@mycavehill.uwi.edu", "Dante", "Blunt", "400004050")
        assert student.username == "danteb"

    def test_new_lecturer(self):
        lecturer = Lecturer("alexa", "alexapass", "alexander.atwell@mycavehill.uwi.edu", "Alexander", "Atwell", "415001713")
        assert lecturer.username == "alexa"

    # password checks
    
    def test_hashed_stu_password(self):
        password = "dantepass"
        hashed = generate_password_hash(password, method='sha256')
        student = Student("danteb", hashed, "dante.blunt@mycavehill.uwi.edu", "Dante", "Blunt", "400004050")
        assert student.password != password

    def test_check_stu_password(self):
        password = "dantepass"
        student = Student("danteb", password, "dante.blunt@mycavehill.uwi.edu", "Dante", "Blunt", "400004050")
        assert student.check_password(password)
    
    def test_hashed_lect_password(self):
        password = "alexpass"
        hashed = generate_password_hash(password, method='sha256')
        lecturer = Lecturer("alexa", hashed, "alexander.atwell@mycavehill.uwi.edu", "Alexander", "Atwell", "415001713")
        assert lecturer.password != password

    def test_check_lect_password(self):
        password = "alexapass"
        lecturer = Lecturer("alexa", password, "alexander.atwell@mycavehill.uwi.edu", "Alexander", "Atwell", "415001713")
        assert lecturer.check_password(password)

    # new rubric
    def test_new_rubric(self):
        rubric = add_rubric("Computer Science Project",'For SWEN and COMP students', 3, 5, 6, 6, 6, 1, 101)
        assert rubric.name == "Computer Science Project"
        assert rubric.novelty == 3
    
    # new proposal
    def test_new_proposal(self):
        proposal = add_proposal(1, 1, 'Cap Advisor', 'Students do not always undertsand how to design capstone projects', 'SWEN and COMP students',
                'Students can submit capstone proposals to and have feedback', 'craete a web app which allows them submit proposal according to capstone rubric',
                3, 'students must submit proposals based on cirtera', 'flask MVC, python, GPT-3', 
                'students can understand what is required for capstone projects and begine their own',
                  'SWEN and COMP students','manged by lecturer eventually',
                'May be revised')
        assert proposal.name == "Cap Advisor"
        assert proposal.num_members == 3
        assert proposal.stduent_id == 1
        assert proposal.notes == "May be revised"
    
    # new evaluation 
    def test_new_evaluation(self):
        evaluation= add_evaluation("Notes", 5, 7, 5, 3, 10, 5, 1, 101)
        assert evaluation.novelty == 5
        assert evaluation.score == 6
    

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


def test_authenticate():
    lecturer = Lecturer("alexa", "alexapass", "alexander.atwell@mycavehill.uwi.edu", "Alexander", "Atwell", "415001713")
    #student = Student("danteb", "dantepass", "dante.blunt@mycavehill.uwi.edu", "Dante", "Blunt", "400004050")
    assert login("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_student(self):
        student = create_student("danteb", "dantepass", "dante.blunt@mycavehill.uwi.edu", "Dante", "Blunt", "400004050")
        assert student.username == "danteb"

    def test_create_lecturer(self):
        lecturer = create_lecturer("alexa", "alexapass", "alexander.atwell@mycavehill.uwi.edu", "Alexander", "Atwell", "415001713")
        assert lecturer.username == "alexa"


  
