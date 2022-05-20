"""
This is our amalgamated flask application, combined from all the files in the "Flask Scripts" folder.
You can look in there for information about individual authors.
Amalgamation created and tested by Roo Case.
"""

import re
from flask import Flask, request, render_template
from datasource import DataSource

app = Flask(__name__)

def get_request_args():
    enrollment = "select"
    charter = "select"
    grade = "select"
    if "enrollment" in request.args:
        enrollment = request.args['enrollment']
    if "charter" in request.args:
        charter = request.args['charter']
    if "grade" in request.args:
        grade = request.args['grade']
    return enrollment, charter, grade

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/list/schools')
def listSchools():
    enrollment, charter, grade = get_request_args()
    my_source = DataSource()
    schools1 = my_source.filter_schools(charter)
    return render_template('filter_school.html', schools=schools1)

@app.route('/school/<school_name>')
def print_school_info(school_name):
    # adding spaces before capital letters
    actual_name = re.sub(r"(\w)([A-Z])", r"\1 \2", school_name)
    my_source = DataSource()
    school = my_source.get_school_by_name(actual_name)[0]
    print(school)
    (available_grades, weekly_table) = my_source.get_identity_by_name(actual_name)
    return render_template('school.html', school = school, available_grades = available_grades, weekly_table = weekly_table)

app.run()
