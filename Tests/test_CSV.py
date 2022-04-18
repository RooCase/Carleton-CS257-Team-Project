"""
Tests by Roo Case.
"""
import unittest

from Main_Project_Scripts import csvManipulation
from Main_Project_Scripts.csvManipulation import findIndividualGroups, createDistrict


class CSVTest(unittest.TestCase):
    def testLineCSVFile(self):
        """
        Tests turning lines from a CSV file into lists, mainly testing csvManipulation.findLines(), by way of the
        helper function writeAndRead().
        :return: nothing
        """
        exampleListForm = [['Yes', 'Academia Cesar Chavez Charter School', 'Regular school', 'Academia Cesar Chavez Charter Schools', '518', '8/30/20', '9/4/20', 'Closed', '', '', 'K: No Data Available; Gr1: No Data Available; Gr2: No Data Available; Gr3: No Data Available; Gr4: No Data Available; Gr5: No Data Available', 'Gr6: No Data Available; Gr7: No Data Available; Gr8: No Data Available', 'Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA', '', '', '55'], ['Yes', 'Academia Cesar Chavez Charter School', 'Regular school', 'Academia Cesar Chavez Charter Schools', '518', '9/5/20', '9/11/20', 'Virtual', 'Virtual', 'Virtual', 'K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance', 'Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance', 'Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA', '', '', '55'], ['Yes', 'Academia Cesar Chavez Charter School', 'Regular school', 'Academia Cesar Chavez Charter Schools', '518', '9/12/20', '9/19/20', 'Virtual', 'Virtual', 'Virtual', 'K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance', 'Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance', 'Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA', '', '', '55']]
        exampleString = """Charter,SchoolName,SchoolType,DistrictName,EnrollmentTotal,TimePeriodStart,TimePeriodEnd,LearningModel,LearningModelGrK5,LearningModelGr68,LearningModelStateCatGrK5,LearningModelStateCatGr68,LearningModelStateCatGr912,EnrollmentInPerson,EnrollmentHybrid,StaffCount
Yes,Academia Cesar Chavez Charter School,Regular school,Academia Cesar Chavez Charter Schools,518,8/30/20,9/4/20,Closed,,,K: No Data Available; Gr1: No Data Available; Gr2: No Data Available; Gr3: No Data Available; Gr4: No Data Available; Gr5: No Data Available,Gr6: No Data Available; Gr7: No Data Available; Gr8: No Data Available,Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA,,,55
Yes,Academia Cesar Chavez Charter School,Regular school,Academia Cesar Chavez Charter Schools,518,9/5/20,9/11/20,Virtual,Virtual,Virtual,K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance,Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance,Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA,,,55
Yes,Academia Cesar Chavez Charter School,Regular school,Academia Cesar Chavez Charter Schools,518,9/12/20,9/19/20,Virtual,Virtual,Virtual,K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance,Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance,Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA,,,55
"""
        resultData = self.writeAndRead(exampleString)
        self.assertEqual(resultData, exampleListForm)

    def testSchoolObjectCreation(self):
        """
        tests the creation of a school object from a CSV input.
        :return: none
        """
        exampleString = """Charter,SchoolName,SchoolType,DistrictName,EnrollmentTotal,TimePeriodStart,TimePeriodEnd,LearningModel,LearningModelGrK5,LearningModelGr68,LearningModelStateCatGrK5,LearningModelStateCatGr68,LearningModelStateCatGr912,EnrollmentInPerson,EnrollmentHybrid,StaffCount
Yes,Academia Cesar Chavez Charter School,Regular school,Academia Cesar Chavez Charter Schools,518,8/30/20,9/4/20,Closed,,,K: No Data Available; Gr1: No Data Available; Gr2: No Data Available; Gr3: No Data Available; Gr4: No Data Available; Gr5: No Data Available,Gr6: No Data Available; Gr7: No Data Available; Gr8: No Data Available,Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA,,,55
Yes,Academia Cesar Chavez Charter School,Regular school,Academia Cesar Chavez Charter Schools,518,9/5/20,9/11/20,Virtual,Virtual,Virtual,K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance,Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance,Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA,,,55
Yes,Academia Cesar Chavez Charter School,Regular school,Academia Cesar Chavez Charter Schools,518,9/12/20,9/19/20,Virtual,Virtual,Virtual,K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance,Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance,Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA,,,55
        """
        exampleData = self.writeAndRead(exampleString)
        exampleSchool = csvManipulation.createSchool(exampleData)
        sampleReturnedInfo = exampleSchool.get_school_info()
        supposedReturned = f"""
School name: Academia Cesar Chavez Charter School.\nThis is a charter school with a student body of 518 students.\nThese grades are available: K, Gr1, Gr2, Gr3, Gr4, Gr5, Gr6, Gr7, Gr8
"""
        self.assertEqual(sampleReturnedInfo, supposedReturned)

    def testSchoolDistrictObjectCreation(self):
        """
        tests the creation of a school district object from a CSV input.
        :return: none
        """
        sampleData = """Achieve Language Academy,Charter agency,413,Weekly,5/15/21,5/21/21,In-person,In-person,In-person,,In-Person,K: AllInPerson; Gr1: AllInPerson; Gr2: AllInPerson; Gr3: AllInPerson; Gr4: AllInPerson; Gr5: AllInPerson,Gr6: AllInPerson; Gr7: AllInPerson; Gr8: AllInPerson,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,
Achieve Language Academy,Charter agency,413,Weekly,5/22/21,5/28/21,In-person,In-person,In-person,,In-Person,K: AllInPerson; Gr1: AllInPerson; Gr2: AllInPerson; Gr3: AllInPerson; Gr4: AllInPerson; Gr5: AllInPerson,Gr6: AllInPerson; Gr7: AllInPerson; Gr8: AllInPerson,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,
Achieve Language Academy,Charter agency,413,Weekly,5/29/21,6/4/21,In-person,In-person,In-person,,In-Person,K: AllInPerson; Gr1: AllInPerson; Gr2: AllInPerson; Gr3: AllInPerson; Gr4: AllInPerson; Gr5: AllInPerson,Gr6: AllInPerson; Gr7: AllInPerson; Gr8: AllInPerson,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,
Ada-Borup Public School District,Regular local school district,578,Weekly,9/1/20,9/8/20,,,,,,K: No Data Available; Gr1: No Data Available; Gr2: No Data Available; Gr3: No Data Available; Gr4: No Data Available; Gr5: No Data Available,Gr6: No Data Available; Gr7: No Data Available; Gr8: No Data Available,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,
Ada-Borup Public School District,Regular local school district,578,Weekly,9/9/20,9/11/20,In-person,In-person,In-person,In-person,In-Person,K: AllInPerson; Gr1: AllInPerson; Gr2: AllInPerson; Gr3: AllInPerson; Gr4: AllInPerson; Gr5: AllInPerson,Gr6: AllInPerson; Gr7: AllInPerson; Gr8: AllInPerson,Gr9: AllInPerson; Gr10: AllInPerson; Gr11: AllInPerson; Gr12: AllInPerson,,,
Ada-Borup Public School District,Regular local school district,578,Weekly,9/12/20,9/18/20,In-person,In-person,In-person,In-person,In-Person,K: AllInPerson; Gr1: AllInPerson; Gr2: AllInPerson; Gr3: AllInPerson; Gr4: AllInPerson; Gr5: AllInPerson,Gr6: AllInPerson; Gr7: AllInPerson; Gr8: AllInPerson,Gr9: AllInPerson; Gr10: AllInPerson; Gr11: AllInPerson; Gr12: AllInPerson,,,
Morris Dance School District,Regular local school district,413,Weekly,5/15/21,5/21/21,In-person,In-person,In-person,,In-Person,K: AllInPerson; Gr1: AllInPerson; Gr2: AllInPerson; Gr3: AllInPerson; Gr4: AllInPerson; Gr5: AllInPerson,Gr6: AllInPerson; Gr7: AllInPerson; Gr8: AllInPerson,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,
Morris Dance School District,Regular local school district,413,Weekly,5/22/21,5/28/21,In-person,In-person,In-person,,In-Person,K: AllInPerson; Gr1: AllInPerson; Gr2: AllInPerson; Gr3: AllInPerson; Gr4: AllInPerson; Gr5: AllInPerson,Gr6: AllInPerson; Gr7: AllInPerson; Gr8: AllInPerson,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,
Morris Dance School District,Regular local school district,413,Weekly,5/29/21,6/4/21,In-person,In-person,In-person,,In-Person,K: AllInPerson; Gr1: AllInPerson; Gr2: AllInPerson; Gr3: AllInPerson; Gr4: AllInPerson; Gr5: AllInPerson,Gr6: AllInPerson; Gr7: AllInPerson; Gr8: AllInPerson,Gr9: No Data Available; Gr10: No Data Available; Gr11: No Data Available; Gr12: No Data Available,,,
"""
        parsed = self.writeAndRead(sampleData)
        districtLines = findIndividualGroups(parsed)
        districts = []
        for districtSection in districtLines:
            district = createDistrict(districtSection, None)
            if district != None:
                districts.append(district)

        self.assertEqual(districts[0].get_district_data(), """District name: Ada-Borup Public School District
Enrollment for this district: 578
List of schools:\n""")
        self.assertEqual(districts[1].get_district_data(),"""District name: Morris Dance School District
Enrollment for this district: 413
List of schools:\n""")

    def writeAndRead(self, exampleString):
        """
        A helper function. Creates a CSV file and then reads from it using the CSV module, to simulate what the application will be doing on a real dataset.
        :param exampleString: the input into a csv file. It is assumed that the string is already comma-delimited.
        :return: returns the list output from the CSV dataset.
        """
        with open("example.csv", 'w') as f:
            f.write(exampleString)
            f.close()

        return csvManipulation.findLines("example.csv")


if __name__ == '__main__':
    unittest.main()
