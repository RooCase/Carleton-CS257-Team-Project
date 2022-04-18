"""
Non-CLI functions written by Roo Case.

This is the main python file, that has the highest amount of abstraction. The code for our command-line-interface is
here, as well as the helper functions that are a part of that.
"""

import sys
import Main_Project_Scripts.district
import Main_Project_Scripts.school
from Main_Project_Scripts.csvManipulation import findIndividualGroups, findLines, createSchool, createDistrict

def importSchools():
    """
    Default helper script for setting up a list of schools.
    :return: a list of schools
    """
    listOfSchools = []
    parsedCSV = findIndividualGroups(findLines("/Users/roocase/Documents/CS257/team-project-team-a/Data/Minnesota_Schools_Modified.csv"))
    for group in parsedCSV:
        listOfSchools.append(createSchool(group))
    return listOfSchools


def importDistricts(schools):
    """
    Default helper script for setting up a list of districts.
    :param: a list of all schools
    :return: a list of districts
    """
    listOfDistricts = []
    parsedCSV = findIndividualGroups(findLines("/Users/roocase/Documents/CS257/team-project-team-a/Data/Minnesota_Districts_LearningModelData_Modified.csv"))

    for group in parsedCSV:
        
        district = (createDistrict(group, schools))
        if district != None:
            listOfDistricts.append(district)
    return listOfDistricts

def list_objects(objectList):
    output = ''
    for object in objectList:
        output += f'{object.name}\n'
    return output

def find_object_by_name(listOfObjects, objectName):
    for object in listOfObjects:
        if object.name == objectName:
            return object

def setup():
    """
    A quick helper function that sets up the data in the proper manner.
    :return: schools: list of all schools in the Schools dataset.
             districts: a list of all districts in the Districts dataset.
    """
    schools = importSchools()
    districts = importDistricts(schools)
    
    return schools, districts

if __name__ == '__main__':
    schools, districts = setup()

    argumentList = sys.argv[1:]

    if argumentList[0] == "-s":
        resultSchool = find_object_by_name(schools, argumentList[1])
        if resultSchool == None:
            print("School Not Found")
        else:
            print(resultSchool.get_school_info())

    if argumentList[0] == "-d":
        resultDistrict = find_object_by_name(districts, argumentList[1])
        if resultDistrict == None:
            print("District Not Found")
        else:
            print(find_object_by_name(districts, argumentList[1]).get_district_data())

    if argumentList[0] == "--list-districts":
       print(list_objects(districts))
    
    if argumentList[0] == "--list-schools":
       print(list_objects(schools))