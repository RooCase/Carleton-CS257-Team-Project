import unittest

from Main_Project_Scripts.district import District
from Main_Project_Scripts.school import School


class TestDistrict(unittest.TestCase):
    school = School("No", "Carlesbad School District", "Pacific Ridge High School", 100, ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance10', 'AllDistance', 'AllDistance'])
    district = District("Carlesbad School District", 203954, [school], ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance10', 'AllDistance', 'AllDistance'])

    def test_get_district_info(self):
        """
        Tests if get_district_info in District class returns the correct string
        :return: None
        """
        retrievedDistrictData = self.district.get_district_data()
        self.assertIn("District name: Carlesbad School District", retrievedDistrictData)
        self.assertIn("Enrollment for this district: 203954", retrievedDistrictData)
        self.assertIn("List of schools:", retrievedDistrictData)
        self.assertIn("Pacific Ridge High School", retrievedDistrictData)

    def test_weekly_mode_tracker(self):
        """
        Tests if weekly_mode_tracker in District class returns the correct list
        :return: None
        """
        self.assertEqual(self.district.learning_modes_for_grades, ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance10', 'AllDistance', 'AllDistance'])

if __name__ == '__main__':
    unittest.main()
