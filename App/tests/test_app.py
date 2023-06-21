import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Student, Lecturer
from App.controllers import (
    create_user,
    get_all_users_json,
    login,
    get_user,
    get_user_by_username,
    update_user,
    create_lecturer,
    create_student
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

    # pure function no side effects or integrations called
    
    def test_hashed_stu_password(self):
        password = "dantepass"
        hashed = generate_password_hash(password, method='sha256')
        student = Student("danteb", password, "dante.blunt@mycavehill.uwi.edu", "Dante", "Blunt", "400004050")
        assert student.password != password

    def test_check_stu_password(self):
        password = "dantepass"
        student = Student("danteb", password, "dante.blunt@mycavehill.uwi.edu", "Dante", "Blunt", "400004050")
        assert student.check_password(password)
    
    def test_hashed_lect_password(self):
        password = "alexpass"
        hashed = generate_password_hash(password, method='sha256')
        lecturer = Lecturer("alexa", "alexapass", "alexander.atwell@mycavehill.uwi.edu", "Alexander", "Atwell", "415001713")
        assert lecturer.password != password

    def test_check_lect_password(self):
        password = "alexapass"
        lecturer = Lecturer("alexa", password, "alexander.atwell@mycavehill.uwi.edu", "Alexander", "Atwell", "415001713")
        assert lecturer.check_password(password)
    

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

    # def test_get_all_users_json(self):
    #     users_json = get_all_users_json()
    #     self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], users_json)

    # Tests data changes in the database
    # def test_update_user(self):
    #     update_user(1, "ronnie")
    #     user = get_user(1)
    #     assert user.username == "ronnie"
