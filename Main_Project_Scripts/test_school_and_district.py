#Rowen Hinrichs
import district
import school 
import Listing_Schools_in_a_District
import unittest

class Test_Cases(unittest.TestCase):
    #Test schools
   


    

    # A test for the listSchools function
    # :param: List of all test schools, test district object, expected result
    # :return: list of schools in test district
    def setUp(self):

         #Test districts
        self.District_A = district.District("District_A", 10, [], [1, 2, 3, 4, 5])
        self.District_B = district.District("District_B", 20, [], [1, 2, 3, 4, 5])
        self.District_C = district.District("District_C", 30, [], [1, 2, 3, 4, 5])

        self.school1 = school.School('No', self.District_A, 'Dummy1', 420, [1, 2, 3, 4, 5])
        self.school2 = school.School('No', self.District_A, 'Dummy2', 1000, [1, 2, 3, 4, 5])
        self.school3 = school.School('No', self.District_B, 'Dummy3', 1000, [1, 2, 3, 4, 5])
        self.school4 = school.School('No', self.District_C, 'Dummy4', 1000, [1, 2, 3, 4, 5])
        self.school5 = school.School('No', self.District_B, 'Dummy5', 1000, [1, 2, 3, 4, 5])
        self.school6 = school.School('No', self.District_C, 'Dummy6', 8008, [1, 2, 3, 4, 5])
        self.school7 = school.School('No', self.District_C, 'Dummy7', 1000, [1, 2, 3, 4, 5])
        self.school8 = school.School('No', self.District_B, 'Dummy8', 69, [1, 2, 3, 4, 5])
        self.school9 = school.School('No', self.District_A, 'Dummy9', 1000, [1, 2, 3, 4, 5])
        self.school0 = school.School('No', self.District_C, 'Dummy0', 1000, [1, 2, 3, 4, 5])

         

        self.schoolsList = [self.school1, self.school2, self.school3, 
        self.school4, self.school5, self.school6, self.school7, self.school8, self.school9, self.school0]

       
    def testDummyTestSchoolsInDistrict(self):
        Test1Expected = [self.school1, self.school2, self.school9]
        Test1 = Listing_Schools_in_a_District.listSchools(self.schoolsList, self.District_A)
        self.assertEquals(Test1, Test1Expected)


    #A test for the listOtherSchools function
    #:param: list of all schools, school object, expected result
    #:return: a list of schools that share school5's district.
    def testDummyTestOtherSchools(self):
        Test2Expected = [self.school3, self.school8]
        self.assertEquals(Listing_Schools_in_a_District.listOtherSchools(self.schoolsList, self.school5), Test2Expected)


if __name__ == '__main__':
    unittest.main()