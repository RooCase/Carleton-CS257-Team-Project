import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "Main_Project_Scripts"))
import district
import school

class TestDistrict(unittest.TestCase):
    
    def test_get_district_info(self):
        sampleSchool = school.School("No", "DummyDistrict", "DummySchool", "Regular", 69, "Yes", "No", "No")
        sampleDistrict = district.District("DummyDistrict", 69, [sampleSchool])
        retrievedDistrictData = sampleDistrict.get_district_data()
        actualDistrictData = "District name: DummyDistrict\nEnrollment for this district: 69\nList of schools:\n  DummySchool\n"
        self.assertEqual(retrievedDistrictData, actualDistrictData) 

if __name__ == '__main__':
    unittest.main()



