"""
Deals with all the Flask operations for the School object.
Written by Roo Case
"""
from flask import Flask, jsonify
from main import setup, list_objects

app = Flask(__name__)

@app.route('/list/schools')
def listSchools():
    """
    :return: list of all the school names
    """
    schools, districts = setup()
    return list_objects(schools)

@app.route('/list/districts')
def listDisctricts():
    """
    :return: list of all the district names
    """
    schools, districts = setup()
    return list_objects(districts)

# app.run(host='0.0.0.0', port=81)

