#Rowen Hinrichs
import district
import school 
import Listing_Schools_in_a_District
import unittest

class Test_Cases(unittest.TestCase):
    #Test schools
    school1 = school.School('No', "District_A", 'Dummy1', 420, [1, 2, 3, 4, 5])
    school2 = school.School('No', "District_A", 'Dummy2', 1000, [1, 2, 3, 4, 5])
    school3 = school.School('No', "District_B", 'Dummy3', 1000, [1, 2, 3, 4, 5])
    school4 = school.School('No', "District_C", 'Dummy4', 1000, [1, 2, 3, 4, 5])
    school5 = school.School('No', "District_B", 'Dummy5', 1000, [1, 2, 3, 4, 5])
    school6 = school.School('No', "District_C", 'Dummy6', 8008, [1, 2, 3, 4, 5])
    school7 = school.School('No', "District_C", 'Dummy7', 1000, [1, 2, 3, 4, 5])
    school8 = school.School('No', "District_B", 'Dummy8', 69, [1, 2, 3, 4, 5])
    school9 = school.School('No', "District_A", 'Dummy9', 1000, [1, 2, 3, 4, 5])
    school0 = school.School('No', "District_C", 'Dummy0', 1000, [1, 2, 3, 4, 5])

    #Test districts
    District_A = district.District("District_A", 10, [], [1, 2, 3, 4, 5])
    District_B = district.District("District_B", 20, [], [1, 2, 3, 4, 5])
    District_C = district.District("District_C", 30, [], [1, 2, 3, 4, 5])

    Test1Expected = [school1, school2, school9]
    Test2Expected = [school3, school8]


    schoolsList = [school1, school2, school3, school4, school5, school6, school7, school8, school9, school0]

    #A test for the listSchools function
    #:param: List of all test schools, test district object, expected result
    #:return: list of schools in test district
    def testDummyTestSchoolsInDistrict(self, schoolsList, District_A, Test1Expected):
        self.assertEquals(Listing_Schools_in_a_District.listSchools(schoolsList, District_A), Test1Expected)


    #A test for the listOtherSchools function
    #:param: list of all schools, school object, expected result
    #:return: a list of schools that share school5's district.
    def testDummyTestOtherSchools(self, schoolsList, school5, Test2Expected):
        self.assertEquals(Listing_Schools_in_a_District.listOtherSchools(schoolsList, school5), Test2Expected)

if __name__ == '__main__':
    unittest.main()