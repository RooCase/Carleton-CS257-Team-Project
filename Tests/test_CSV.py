import unittest, csv

from Main_Project_Scripts import csvManipulation
from Main_Project_Scripts.school import School


class CSVTest(unittest.TestCase):
    def testLineCSVFile(self):
        ##Unit test for input/output from CSV file.
        exampleListForm = [['Yes', 'Academia Cesar Chavez Charter School', 'Regular school', 'Academia Cesar Chavez Charter Schools', '518', '8/30/20', '9/4/20', 'Closed', '', '', 'K: No Data Available; Gr1: No Data Available; Gr2: No Data Available; Gr3: No Data Available; Gr4: No Data Available; Gr5: No Data Available', 'Gr6: No Data Available; Gr7: No Data Available; Gr8: No Data Available', 'Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA', '', '', '55'], ['Yes', 'Academia Cesar Chavez Charter School', 'Regular school', 'Academia Cesar Chavez Charter Schools', '518', '9/5/20', '9/11/20', 'Virtual', 'Virtual', 'Virtual', 'K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance', 'Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance', 'Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA', '', '', '55'], ['Yes', 'Academia Cesar Chavez Charter School', 'Regular school', 'Academia Cesar Chavez Charter Schools', '518', '9/12/20', '9/19/20', 'Virtual', 'Virtual', 'Virtual', 'K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance', 'Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance', 'Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA', '', '', '55']]



        exampleString = """Charter,SchoolName,SchoolType,DistrictName,EnrollmentTotal,TimePeriodStart,TimePeriodEnd,LearningModel,LearningModelGrK5,LearningModelGr68,LearningModelStateCatGrK5,LearningModelStateCatGr68,LearningModelStateCatGr912,EnrollmentInPerson,EnrollmentHybrid,StaffCount
Yes,Academia Cesar Chavez Charter School,Regular school,Academia Cesar Chavez Charter Schools,518,8/30/20,9/4/20,Closed,,,K: No Data Available; Gr1: No Data Available; Gr2: No Data Available; Gr3: No Data Available; Gr4: No Data Available; Gr5: No Data Available,Gr6: No Data Available; Gr7: No Data Available; Gr8: No Data Available,Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA,,,55
Yes,Academia Cesar Chavez Charter School,Regular school,Academia Cesar Chavez Charter Schools,518,9/5/20,9/11/20,Virtual,Virtual,Virtual,K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance,Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance,Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA,,,55
Yes,Academia Cesar Chavez Charter School,Regular school,Academia Cesar Chavez Charter Schools,518,9/12/20,9/19/20,Virtual,Virtual,Virtual,K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance,Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance,Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA,,,55
"""

        with open("example.csv", 'w') as f:
            f.write(exampleString)
            f.close()

        resultData = csvManipulation.findLines("example.csv")

        self.assertEqual(resultData, exampleListForm)

    def testSchoolObjectCreation(self):
        # TODO: finish what the final script should look like for test cases
        exampleLine = csvManipulation.findLines("example.csv")
        exampleSchool = csvManipulation.createSchool(exampleLine)

        sampleReturnedInfo = exampleSchool.get_school_info()
        supposedReturned = f"""
        School name: Academia Cesar Chavez Charter School
        This is a charter school with a student body of 518 students.
        It is located in Academia Cesar Chavez Charter Schools.
        Those grades are available: K, Gr1, Gr2, Gr3, Gr4, Gr5, Gr6, Gr7, Gr8 
        """

        self.assertEqual(sampleReturnedInfo, supposedReturned)

    def testSchoolDistrictObjectCreation(self):
        # TODO: write this.
        return


if __name__ == '__main__':
    unittest.main()
