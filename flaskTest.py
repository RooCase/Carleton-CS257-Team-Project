"""
Testing the Flask functions.
Written by Artem Yushko and Roo Case, amalgamed and tested by Artem Yushko
"""
from Flask_Scripts import flaskList, flaskSchool
from main import list_objects, setup, get_weekly_data
import unittest

"""
Initializing the flask apps for later testing.
For the sake of unified response format, we are using class-specific initializations.
"""
list_app = flaskList.app
school_app = flaskSchool.app

class FlaskTest(unittest.TestCase):
    def setUp(self):
        """
        Setting everything up
        """
        self.list_app = list_app.test_client()
        self.school_app = school_app.test_client()
        self.schools, self.districts = setup()

    def test_school_getter(self):
        """
        Test to see if the school object returned is correct
        """
        response = self.school_app.get('/school/AvalonSchool', follow_redirects=True)
        self.assertEqual(b'\nSchool name: Avalon School.\nThis is a charter school with a student body of 173 students.\n'
                         b'These grades are available: Gr9, Gr10, Gr11, Gr12\n', response.data)

    def test_school_lists(self):
        """
        Tests to see if the printing of schools to a webpage is correct
        """
        response = self.list_app.get('/list/schools', follow_redirects=True)
        # it is important to add a new line at the end of the variable
        expected = bytes(str(list_objects(self.schools).strip("\n")) + "\n", 'utf-8')
        self.assertEqual(expected, response.data)

    def test_district_lists(self):
        """
        Tests to see if the printing of districts to a webpage is correct
        """
        response = self.list_app.get('/list/districts', follow_redirects=True)
        # it is important to add a new line at the end of the variable
        expected = bytes(str(list_objects(self.districts).strip("\n")) + "\n", 'utf-8')
        self.assertEqual(expected, response.data)


if __name__ == '__main__':
    unittest.main()
