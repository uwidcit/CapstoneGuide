import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import ( create_student, create_lecturer, add_rubric, remove_rubric, get_all_rubrics, get_all_lecturers )
# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)


# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_lecturer('bob', 'bobpass', 'bob@mycavehilluwi.edu', 'bob', 'smith', 1232)
    create_student('rob', 'robpass', 'rob@mycavehilluwi.edu', 'rob', 'smith', 1232)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# Lecturer Test
# eg : flask user <command>
lecturer_cli = AppGroup('lecturer', help='Lecturer object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@lecturer_cli.command("create", help="Creates a lecturer")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("email", default="rob@mail.com")
def create_lecturer_command(username, password, email):
    create_lecturer(username, password, "bob", "smith", email, 1232)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@lecturer_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_lecturers_command(format):
    if format == 'string':
        print(get_all_lecturers())

app.cli.add_command(lecturer_cli) # add the group to the cli

# Student Test
# eg : flask user <command>
student_cli = AppGroup('student', help='Student object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@student_cli.command("create", help="Creates a student")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("email", default="rob@mail.com")
def create_student_command(username, password, email):
    create_student(username, password, "bob", "smith", email, 1232)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@lecturer_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_students_command(format):
    if format == 'string':
        print(get_all_students())

app.cli.add_command(student_cli) # add the group to the cli


rubric = AppGroup('rubric', help='Rubric object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@rubric.command("create", help="Creates a dummy rubric")
@click.argument("notes", default="notes")
def create_rubric_command(notes):
    add_rubric(notes=notes, lecturerId=1, novelty=5, relevance=5, feasibility=5, impact=5, sustainability=5, technology=5)
    print(f'rubric created!')

@rubric.command("list", help="Lists all rubrics in the database")
def list_rubric_command():
    print(get_all_rubrics())

app.cli.add_command(rubric)  

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)