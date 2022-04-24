"""
Tests the flask scripts concerned with the School objects.
Written by Roo Case, with help from Artem Yushko in understanding how to properly test Flask stuff with unittests.
"""
from Flask_Scripts import flaskList
from main import list_objects, setup
import unittest

app = flaskList.app

class TestListObjects(unittest.TestCase):
    def test_school_lists(self):
        """
        Tests to see if the printing of schools to a webpage is correct
        """
        self.app = app.test_client()
        schools, districts = setup()
        response = self.app.get('/list/schools', follow_redirects=True)
        self.assertEqual(list_objects(schools), response.data)

    def test_district_lists(self):
        """
        Tests to see if the printing of districts to a webpage is correct
        """
        self.app = app.test_client()
        schools, districts = setup()
        response = self.app.get('/list/districts', follow_redirects=True)
        self.assertEqual(list_objects(districts), response.data)

if __name__ == '__main__':
    unittest.main()