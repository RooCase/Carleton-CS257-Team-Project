"""
Written by Roo Case
"""
import unittest
from Main_Project_Scripts.school import School
from Main_Project_Scripts.district import District

class TestSchoolInDistrict(unittest.TestCase):
    def test_If_School_In_District(self):
        """
        Tests to see if the school's name appears in a district's list of schools
        """
        school = School("No", "Carlesbad School District","Pacific Ridge High School", 100, ["lorem ipsum"])
        district = District("Carlesbad School District", 203954, ["Pacific Ridge High School"], ["lorem ipsum sigdor"])
        self.assertIn(school.name, district.school_list)

    def test_If_District_In_School(self):
        """
        Tests to see if the district's name appears as one of its member school's "district" space.
        """
        school = School("No", "Carlesbad School District","Pacific Ridge High School", 100, ["lorem ipsum"])
        district = District("Carlesbad School District", 203954, ["Pacific Ridge High School"], ["lorem ipsum sigdor"])
        self.assertEqual(school.district, district.name)

if __name__ == '__main__':
    unittest.main()