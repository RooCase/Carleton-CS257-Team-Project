from flask import *
from main import find_district_info_by_name, setup

app = Flask(__name__)

@app.route("/")
def homepage():
    """
    This function renders the homepage which shows how to use this app
    """
    return f"""
This app helps you get a district information using its name. Enter the link "http://127.0.0.1:5000/district/[Enter District Name Here]". (An example district name could be "Alexandria Public School District").
    """

@app.route('/district/<district_name>')
def render_district_info_by_name(district_name):
    """
    This function is a modification of find_district_info_by_name function for Flask. Also, it calls setup so it might be a little slow.
    :param: Name of a district. This parameter comes from the link the user types in the browser.
    :return: Info about that district. "District Not Found" if there is no such district.
    """
    schools, districts = setup()
    return find_district_info_by_name(districts, district_name)

if __name__ == '__main__':
    app.run()
