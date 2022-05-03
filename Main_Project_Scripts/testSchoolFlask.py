"""
Tests the flask scripts concerned with the School objects.
Written by Artem Yushko
"""
from Main_Project_Scripts import flaskSchool
from main import get_weekly_data
import unittest

app = flaskSchool.app

class TestSchoolFlask(unittest.TestCase):
    def test_school_getter(self):
        self.app = app.test_client()
        response = self.app.get('/school/AvalonSchool', follow_redirects=True)
        self.assertEqual(b'School name: Avalon School. This is a charter school with a student body of 173 students. '
                         b'These grades are available: Gr9, Gr10, Gr11, Gr12', response.data)

    def test_covid_data(self):
        self.app = app.test_client()
        response = self.app.get('/school/AvalonSchool/covid', follow_redirects=True)
        self.assertEqual(bytes(get_weekly_data('Avalon School'), 'utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()
