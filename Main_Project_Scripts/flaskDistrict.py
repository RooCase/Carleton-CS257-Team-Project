from Main_Project_Scripts.main import setup
from Main_Project_Scripts.Listing_Schools_in_a_District import *

app = Flask(__name__)

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


app.run(host='0.0.0.0', port=81)