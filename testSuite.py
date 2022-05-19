"""
Testing the Flask functions.
Written by Artem Yushko and Roo Case, amalgamed and tested by Artem Yushko
"""
from Flask_Scripts import flaskList, flaskSchool
from Main_Project_Scripts import school, district, csvManipulation
from Main_Project_Scripts.csvManipulation import findIndividualGroups, createDistrict
from main import list_objects, setup
import unittest

class TestSuite(unittest.TestCase):
    """
    Test objects to make sure our functions work
    """
    sampleSchool = school.School("No", "DummyDistrict", "DummySchool", 69, [1, 2, 3, 4, 5])
    sampleDistrict = district.District("DummyDistrict", 69, [sampleSchool], [1, 2, 3, 4, 5])

    def test_get_district_info(self):
        """
        Tests if get_district_info in District class returns the correct string
        :return: None
        """
        retrieved_district_data = self.sampleDistrict.get_district_data()
        actual_district_data = "District name: DummyDistrict\nEnrollment for this district: 69\nList of schools:\n  " \
                               "DummySchool\n"
        self.assertEqual(retrieved_district_data, actual_district_data)

    """
    Tests for reading the CSV file. Written by Roo Case, modified by Artem Yushko
    """
    def writeAndRead(self, exampleString):
        """
        A helper function. Creates a CSV file and then reads from it using the CSV module,
        to simulate what the application will be doing on a real dataset.
        :param exampleString: the input into a csv file. It is assumed that the string is already comma-delimited.
        :return: returns the list output from the CSV dataset.
        """
        with open("example.csv", 'w') as f:
            f.write(exampleString)
            f.close()

        return csvManipulation.findLines("example.csv")

    """
    Testing the Flask functions
    """
    def setUp(self):
        """
        Setting everything up for the flask tests
        """
        self.schools, self.districts = setup()

    def test_school_getter(self):
        """
        Test to see if the school object returned is correct
        """
        # initializing the app
        school_app = flaskSchool.app.test_client()
        response = school_app.get('/school/AvalonSchool', follow_redirects=True)
        self.assertEqual(b'\nSchool name: Avalon School.\nThis is a charter school with a student body of 173 students.\n'
                         b'These grades are available: Gr9, Gr10, Gr11, Gr12\n', response.data)

    def test_school_lists(self):
        """
        Tests to see if the printing of schools to a webpage is correct
        """
        # initializing the app
        list_app = flaskList.app.test_client()
        response = list_app.get('/list/schools', follow_redirects=True)
        # it is important to add a new line at the end of the variable
        expected = bytes(str(list_objects(self.schools).strip("\n")) + "\n", 'utf-8')
        self.assertEqual(expected, response.data)

    def test_district_lists(self):
        """
        Tests to see if the printing of districts to a webpage is correct
        """
        # initializing the app
        list_app = flaskList.app.test_client()
        response = list_app.get('/list/districts', follow_redirects=True)
        # it is important to add a new line at the end of the variable
        expected = bytes(str(list_objects(self.districts).strip("\n")) + "\n", 'utf-8')
        self.assertEqual(expected, response.data)


if __name__ == '__main__':
    unittest.main()
