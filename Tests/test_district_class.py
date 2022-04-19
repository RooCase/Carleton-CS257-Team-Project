from Main_Project_Scripts import district, school
import unittest

class TestDistrict(unittest.TestCase):
    sampleSchool = school.School("No", "DummyDistrict", "DummySchool", 69, [1, 2, 3, 4, 5])
    sampleDistrict = district.District("DummyDistrict", 69, [sampleSchool])

    def test_get_district_info(self):
        retrievedDistrictData = self.sampleDistrict.get_district_data()
        actualDistrictData = "District name: DummyDistrict\nEnrollment for this district: 69\nList of schools:\n  DummySchool\n"
        self.assertEqual(retrievedDistrictData, actualDistrictData) 

    def test_weekly_mode_tracker(self):
        self.sampleDistrict.add_week(['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance10', 'AllDistance', 'AllDistance'])
        assert(self.sampleDistrict.get_weeks_for_grade(10), ['AllDistance'])

if __name__ == '__main__':
    unittest.main()
