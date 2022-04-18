"""
Testing file for the School class.
Written by Artem Yushko.
"""

from Main_Project_Scripts.school import School
import unittest

dummy_grade_data = {'1': [], '2': [], '3': [], '4': [], '5': [],
                    '6': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllInPerson', 'AllInPerson'],
                    '7': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllInPerson', 'Hybrid'],
                    '8': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllInPerson', 'AllInPerson'],
                    '9': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'Hybrid', 'AllInPerson', 'AllInPerson', 'AllInPerson', 'AllInPerson', 'AllInPerson'],
                    '10': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllInPerson', 'AllInPerson', 'AllInPerson', 'AllInPerson', 'AllInPerson', 'AllInPerson'],
                    '11': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllInPerson', 'Hybrid', 'AllInPerson', 'AllInPerson', 'AllInPerson', 'Hybrid'],
                    '12': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllInPerson', 'AllInPerson', 'AllInPerson', 'AllInPerson', 'AllInPerson', 'AllInPerson']}

dummy_school = School("Charter", "Dummy District", "Dummy Name", "1234", dummy_grade_data)
print(dummy_school.get_school_info())
print(dummy_school.get_covid_data())

class SchoolTest(unittest.TestCase):
    def testGetDistrict(self):
        self.assertEqual(dummy_school.get_district(), "Dummy District")

    def testGetAvailableGrades(self):
        self.assertEqual(['6', '7', '8', '9', '10', '11', '12'], dummy_school.get_available_grades())

    def testCharter(self):
        self.assertEqual('Charter', dummy_school.charter)

if __name__ == '__main__':
    unittest.main()