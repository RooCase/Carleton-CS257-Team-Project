"""
This is our amalgamated flask application, combined from all the files in the "Flask Scripts" folder.
You can look in there for information about individual authors.
Amalgamation created and tested by Roo Case.
"""

import re
from flask import Flask, render_template
from interact_data import InteractDataSource

app = Flask(__name__)

@app.route('/')
def homepage():
    """
    Returns the homepage.
    """
    return render_template("homepage.html")

@app.route('/list/schools')
def listSchools():
    """
    This fn lists, and filters all the districts
    :param: NA
    :return: A rendered flask template for all schools
    """
    my_source = InteractDataSource()
    enrollment, charter, grade, schools = my_source.filter_schools()
    return render_template('filter_school.html', 
                                schools=schools, 
                                enrollment = enrollment,
                                charter = charter, 
                                grade = grade)


@app.route('/list/districts')
def listDisctricts():
    """
    This fn lists alll the districts
    :param: NA
    :return: a rendered flask template for districts.
    """
    my_source = InteractDataSource()
    district_names = my_source.get_district_names()
    return render_template('filter_districts.html', district_names = district_names)

@app.route('/school/<school_name>')
def render_school_info_by_name(school_name):
    """
    This fn renders an info about school and its weekly covid data.
    :param: Name of shool
    :return: A rendered flask template, detailing information about the specified school.
    """
    my_source = InteractDataSource()
    school = my_source.get_school_by_name(school_name)
    (available_grades, weekly_table) = my_source.get_identity_by_name(school_name)
    return render_template('school.html', 
                            school = school, 
                            available_grades = available_grades, 
                            weekly_table = weekly_table)

@app.route('/district/<district_name>')
def render_district_info_by_name(district_name):
    """
    This fn renders an info about district. It includes the district's schools and its weekly covid data
    :param: Name of a district. This parameter comes from the link the user types in the browser.
    :return: Info about that district. "District Not Found" if there is no such district.
    """
    my_source = InteractDataSource()
    district = my_source.get_district_by_name(district_name)
    schools = my_source.get_schools_by_district(district_name)
    (available_grades, weekly_table) = my_source.get_identity_by_name(district_name)
    return render_template('district.html',
                           district = district,
                           available_grades=available_grades,
                           weekly_table = weekly_table,
                           schools = schools)

@app.route("/search")
def underConstruction():
    """
    :return: an "under construction" flask template
    """
    return render_template('under_construction.html')

@app.errorhandler(400)
def page_not_found(e):
    """
    :param e: the details of the error.
    :return: an "error 400" flask template
    """
    return render_template('400.html'), 400

@app.errorhandler(404)
def page_not_found(e):
    """
    :param e: the details of the error.
    :return: an "error 404" flask template
    """
    return render_template('404.html'), 404

@app.errorhandler(405)
def page_not_found(e):
    """
    :param e: the details of the error.
    :return: an "error 404" flask template
    """
    return render_template('405.html'), 405

app.run(host='0.0.0.0', port='5133')
