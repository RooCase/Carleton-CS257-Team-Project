"""
Deals with all the Flask operations for the School object.
Written by Roo Case
"""
from flask import Flask, jsonify
from main import setup, list_objects

app = Flask(__name__)


@app.route('/list/schools')
def listSchools():
    schools, districts = setup()
    return list_objects(schools)

@app.route('/list/districts')
def listDisctricts():
    schools, districts = setup()
    return list_objects(districts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)

