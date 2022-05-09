"""
Deals with all the Flask operations for the School object.
Written by Artem Yushko
"""

from flask import Flask, jsonify
from Main_Project_Scripts.main import find_school_info_by_name, importSchools, get_weekly_data
import re

app = Flask(__name__)

"""
Function for getting general information about a specific school.
"""


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


app.run(host='0.0.0.0', port=81)
