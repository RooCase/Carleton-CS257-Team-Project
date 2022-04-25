from flask import Flask
from Main_Project_Scripts import *
from Main_Project_Scripts.Listing_Schools_in_a_District import *

app = Flask(__name__)

@app.route('/district/')
def home():
    return "To see the schools in a district, go to /districtschools/<District Name>."



@app.route('/district/<districtName>/schools')
def print_district_schools(districtName):
    return listSchools(schools, districtName)


app.run(host='0.0.0.0', port=81)