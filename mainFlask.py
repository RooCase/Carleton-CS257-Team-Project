"""
This is our amalgamated flask application, combined from all the files in the "Flask Scripts" folder.
You can look in there for information about individual authors.
Amalgamation created and tested by Roo Case.
"""

import re
import werkzeug
from flask import Flask, jsonify, request, render_template
from Flask_Scripts import *
from Main_Project_Scripts.Listing_Schools_in_a_District import listSchools
from main import setup, get_weekly_data, importSchools, list_objects, find_school_info_by_name, \
    find_district_info_by_name

app = Flask(__name__)


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request():
    return 'Something went wrong on our side! Try another request.', 400


@app.errorhandler(werkzeug.exceptions.NotFound)
def handle_not_found():
    return """Most likely, you have entered an incorrect school name! 
    Remember: 
        - To access an individual school's information, use the url extension "/school/{school_name}"
        - To access an individual school's COVID data, use the url extension "/school/{school_name}/covid"
        - To access a list of districts, use the url extension "/list/districts"
        - To access a list of schools, use the url extension "/list/schools"
        - To access a list of schools within a specific district, use the url extension "/district/{districtName}/schools"
    
        - If you want to enter a school name to the URL, then write it with all the capital letters without spaces (ex.
        AvalonSchool)""", 404


@app.errorhandler(werkzeug.exceptions.MethodNotAllowed)
def handle_method_not_allowed():
    return "This method is not allowed!", 405


@app.route('/')
def homepage():
    return \
        """Welcome! Here's a list of things you can do:
        - To access an individual school's information, use the url extension "/school/{school_name}"
        - To access an individual school's COVID data, use the url extension "/school/{school_name}/covid"
        - To access a list of districts, use the url extension "/list/districts"
        - To access a list of schools, use the url extension "/list/schools"
        - To access a list of schools within a specific district, use the url extension "/district/{districtName}/schools"
    
        - If you want to enter a school name to the URL, then write it with all the capital letters without spaces (ex.
        AvalonSchool)
        """

@app.route('/district/')
def home():
    return \
    """
    - To access a list of districts, use the url extension "/list/districts
    - To access a list of schools within a specific district, use the url extension "/district/<districtName>/schools"
    """

@app.route('/district/<districtName>/schools')
def print_district_schools(districtName):
    schools, district = setup()
    return listSchools(schools, districtName)


@app.route('/district/<district_name>')
def render_district_info_by_name(district_name):
    """
    This function is a modification of find_district_info_by_name function for Flask. Also, it calls setup so it might be a little slow.
    :param: Name of a district. This parameter comes from the link the user types in the browser.
    :return: Info about that district. "District Not Found" if there is no such district.
    """
    schools, districts = setup()
    return find_district_info_by_name(districts, district_name)

@app.route('/school/<school_name>')
def print_school_info(school_name):
    # adding spaces before capital letters
    actual_name = re.sub(r"(\w)([A-Z])", r"\1 \2", school_name)
    return find_school_info_by_name(importSchools(), actual_name)


"""
Function for getting school-specific detailed covid data.
"""

@app.route('/school/<school_name>/covid')
def print_school_covid_data(school_name):
    # adding spaces before capital letters
    actual_name = re.sub(r"(\w)([A-Z])", r"\1 \2", school_name)
    # converting pandas dataframe to JSON
    df = get_weekly_data(importSchools(), actual_name)
    df_list = df.values.tolist()
    json_data = jsonify(df_list)
    return json_data

@app.route('/list/schools')
def listSchools():
    enrollment, charter, grade = get_request_args()
    return render_template('filter_school.html', schools=filterSchools(schools, enrollment, charter, grade))
    
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
    
def filterSchoolsByCharter(myschools, charter):
    if charter == "select":
        return myschools
    ans = []
    for school in myschools:
        if school.charter == charter:
            ans.append(school)
    return ans

def filterSchoolsByEnrollment(myschools, enrollment):
    l = 0
    r = 0
    if enrollment == "select":
        return myschools
    if enrollment == "0-99":
        l = 0
        r = 99
    if enrollment == "100-999":
        l = 100
        r = 999
    if enrollment == "1000-Inf":
        l = 1000
        r = 100000

    ans = []
    for school in myschools:
        if l <= int(school.size) and int(school.size) <= r:
            ans.append(school)
    return ans

def filterSchoolsByGrade(myschools, grade):
    if grade == "select":
        return myschools
    ans = []
    for school in myschools:
        if grade in school.get_available_grades():
            ans.append(school)
    return ans

def filterSchools(myschools, enrollment, charter, grade):
    print("Yooo this is " + grade)
    myschools = filterSchoolsByEnrollment(myschools, enrollment)
    myschools = filterSchoolsByCharter(myschools, charter)
    myschools = filterSchoolsByGrade(myschools, grade)
    return myschools

@app.route('/list/districts')
def listDisctricts():
    schools, districts = setup()
    return list_objects(districts)

app.run(host='0.0.0.0', port=81)

