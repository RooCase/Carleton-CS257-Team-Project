"""
Custom pages for error handling, and the homepage.
Error handling written by Artem Yushko, homepage written by Roo Case
"""

from flask import Flask
import werkzeug

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
    return """Welcome! Here's a list of things you can do:
    - To access an individual school's information, use the url extension "/school/{school_name}"
    - To access an individual school's COVID data, use the url extension "/school/{school_name}/covid"
    - To access a list of districts, use the url extension "/list/districts"
    - To access a list of schools, use the url extension "/list/schools"
    - To access a list of schools within a specific district, use the url extension "/district/{districtName}/schools"
    
    - If you want to enter a school name to the URL, then write it with all the capital letters without spaces (ex.
    AvalonSchool)
    """

app.run(host='0.0.0.0', port=81)