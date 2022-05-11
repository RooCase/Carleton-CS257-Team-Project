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
from Main_Project_Scripts import filter_school
from Main_Project_Scripts.main import find_object_by_name
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
    return render_template("homepage.html")


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
    selected = find_object_by_name(districts, district_name)
    schoolNameList =[]
    for school in selected.getSchoolList():
        schoolNameList.append(school.name)
    return render_template('district.html',
                           name=selected.getName(),
                           enrollment=selected.getSize(),
                           schoolNames=schoolNameList,
                           weeks= selected.getLearningModeWeekly()
                           )


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
    schools, districts = setup()
    enrollment, charter, grade = filter_school.get_request_args()
    return render_template('filter_school.html',
                           schools=filter_school.filter_schools(schools, enrollment, charter, grade))


@app.route('/list/districts')
def listDisctricts():
    schools, districts = setup()
    return list_objects(districts)


app.run(host='0.0.0.0', port=81)
