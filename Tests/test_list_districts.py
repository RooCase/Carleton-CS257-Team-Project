import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "Main_Project_Scripts"))
import district
import main
import school

class TestListDistrict(unittest.TestCase):
    
    def test_list_district(self):
        sampleSchool = school.School("No", "DummyDistrict", "DummySchool", 69, [1, 2, 3, 4, 5])
        sampleDistrictList = [district.District("DummyDistrict1", 69, [sampleSchool]), district.District("DummyDistrict2", 70, [sampleSchool])]
        retrievedDistrictList = main.list_districts(sampleDistrictList)
        actualDistrictList = "DummyDistrict1\nDummyDistrict2\n"
        self.assertEqual(retrievedDistrictList, actualDistrictList) 

if __name__ == '__main__':
    unittest.main()