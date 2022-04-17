#Rowen Hinrichs
from Main_Project_Scripts.district import District
from Main_Project_Scripts.school import School
from Main_Project_Scripts.Listing_Schools_in_a_District import *
import unittest

class Test_Cases(unittest.TestCase):
    #Test schools
    school1 = School('No', "District_A", 'Dummy1', 420, [1, 2, 3, 4, 5])
    school2 = School('No', "District_A", 'Dummy2', 1000, [1, 2, 3, 4, 5])
    school3 = School('No', "District_B", 'Dummy3', 1000, [1, 2, 3, 4, 5])
    school4 = School('No', "District_C", 'Dummy4', 1000, [1, 2, 3, 4, 5])
    school5 = School('No', "District_B", 'Dummy5', 1000, [1, 2, 3, 4, 5])
    school6 = School('No', "District_C", 'Dummy6', 8008, [1, 2, 3, 4, 5])
    school7 = School('No', "District_C", 'Dummy7', 1000, [1, 2, 3, 4, 5])
    school8 = School('No', "District_B", 'Dummy8', 69, [1, 2, 3, 4, 5])
    school9 = School('No', "District_A", 'Dummy9', 1000, [1, 2, 3, 4, 5])
    school0 = School('No', "District_C", 'Dummy0', 1000, [1, 2, 3, 4, 5])

    #Test districts
    District_A = District("District_A", [])
    District_B = District("District_B", [])
    District_C = District("District_C", [])

    Test1Expected = [school1, school2, school9]
    Test2Expected = [school3, school8]


    schoolsList = [school1, school2, school3, school4, school5, school6, school7, school8, school9, school0]

    #testing schools in district
    def DummyTestSchoolsInDistrict(self, schoolsList, District_A, Test1Expected):
        self.assertEquals(listSchools(schoolsList, District_A), Test1Expected)


    #testing other schools in a particular school's district.
    def DummyTestOtherSchools(self, schoolsList, school5, Test2Expected):
        self.assertEquals(listOtherSchools(schoolsList, school5), Test2Expected)

if __name__ == '__main__':
    unittest.main()