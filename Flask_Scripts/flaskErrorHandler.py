"""
Custom pages for error handling.
Written by Artem Yushko
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
    Remember: the correct address is capitalized name with no spaces (ex. Avalon School -> AvalonSchool)""", 404

@app.errorhandler(werkzeug.exceptions.MethodNotAllowed)
def handle_method_not_allowed():
    return "This method is not allowed!", 405
