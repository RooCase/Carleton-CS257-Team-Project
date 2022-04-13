import unittest, csv

from Main_Project_Scripts import csvManipulation
from Main_Project_Scripts.school import School


class CSVTest(unittest.TestCase):
    def test2LineCSVFile(self):
        ##Unit test for input/output from CSV file.
        exampleString = """DistrictName,DistrictType,EnrollmentTotal,TimePeriodInterval,TimePeriodStart,TimePeriodEnd,LearningModel,LearningModelGrK5,LearningModelGr68,LearningModelGr912,LearningModelStateCat,LearningModelStateCatGrK5,LearningModelStateCatGr68,LearningModelStateCatGr912,EnrollmentInPerson,EnrollmentHybrid,EnrollmentVirtual \nAcademia Cesar Chavez Charter School,Charter agency,518,Weekly,9/1/20,9/8/20,,,,,,K: No Data Available; Gr1: No Data Available; Gr2: No Data Available; Gr3: No Data Available; Gr4: No Data Available; Gr5: No Data Available,Gr6: No Data Available; Gr7: No Data Available; Gr8: No Data Available,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,\nAcademia Cesar Chavez Charter School,Charter agency,518,Weekly,9/9/20,9/11/20,,Virtual,Virtual,,No Current Model,K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance,Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,\nAcademia Cesar Chavez Charter School,Charter agency,518,Weekly,9/12/20,9/18/20,Virtual,Virtual,Virtual,,Distance,K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance,Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,"""
        exampleListForm = ["DistrictName,DistrictType,EnrollmentTotal,TimePeriodInterval,TimePeriodStart,TimePeriodEnd,LearningModel,LearningModelGrK5,LearningModelGr68,LearningModelGr912,LearningModelStateCat,LearningModelStateCatGrK5,LearningModelStateCatGr68,LearningModelStateCatGr912,EnrollmentInPerson,EnrollmentHybrid,EnrollmentVirtual",
"Academia Cesar Chavez Charter School,Charter agency,518,Weekly,9/1/20,9/8/20,,,,,,K: No Data Available; Gr1: No Data Available; Gr2: No Data Available; Gr3: No Data Available; Gr4: No Data Available; Gr5: No Data Available,Gr6: No Data Available; Gr7: No Data Available; Gr8: No Data Available,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,",
"Academia Cesar Chavez Charter School,Charter agency,518,Weekly,9/9/20,9/11/20,,Virtual,Virtual,,No Current Model,K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance,Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,",
"Academia Cesar Chavez Charter School,Charter agency,518,Weekly,9/12/20,9/18/20,Virtual,Virtual,Virtual,,Distance,K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance,Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,"
     ]

        with open("example.csv", 'w') as f:
            f.write(exampleString)
            f.close()

        resultData = csvManipulation.returnLines("example.csv")
        self.assertEqual(exampleString, exampleListForm)

    def testSchoolObjectCreation(self):
        return

    def testSchoolDistrictObjectCreation(self):
        return

if __name__ == '__main__':
    unittest.main()